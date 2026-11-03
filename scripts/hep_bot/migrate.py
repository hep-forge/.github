#!/usr/bin/env python3
"""Advance hep-forge migrations one step, the way conda-forge's bot does.

A migration is one change that has to travel down the dependency graph:
publish a new platform, or rebuild everything below a package after it
changed. It lives in migrations/<name>.yaml:

    name: macos-arm64
    created: 2026-11-03T00:00:00Z
    platform: macos-arm64      # platform migration: build and publish only this leg,
                               # opt the repo in when its newest tag passes
    packages: all              # or a list of feedstocks

    name: root-6.40
    created: 2026-11-10T00:00:00Z
    from: [root]               # rebuild migration: these and all their dependents,
                               # on the platforms each repo publishes

Every run is a short stateless pass; nothing waits for builds. For each
package the channel and the feedstock's runs say where it is:

    done      the channel already has what the migration asks for: never rebuilt
    building  a run of one of its tags is in flight
    failed    its newest tag failed at the current main; retried by itself once
              main moves (push a recipe fix and the next pass picks it up)
    blocked   a dependency in the migration failed
    waiting   a dependency in the migration is not done yet
    ready     every dependency is done: started now, max_running at a time

A package is started by moving its published tags to the feedstock's main
(the push starts the build; dispatching an old tag would run that tag's old
recipe and workflow). Status goes to migrations/status/<name>.md, and each
failing package gets one issue on its feedstock, closed once it builds.

Usage:
    migrate.py [--only <migration>] [--dry-run]
"""
import argparse
import datetime as dt
import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from dep_graph import requirement_names  # noqa: E402

ROOT = Path(__file__).resolve().parents[2]
MIGRATIONS = ROOT / "migrations"
ORG = "hep-forge"
CHANNEL = "https://conda.anaconda.org/hep-forge"
SUBDIRS = {"amd64": "linux-64", "arm64": "linux-aarch64", "macos-arm64": "osx-arm64"}
DEFAULT_PUBLISH = "amd64,arm64"       # autoupload.yml's default for ANACONDA_PUBLISH
TRIGGER_TAG = re.compile(r"^([0-9].*|head)$")   # tags whose push starts autoupload.yml


def gh(*args, check=False):
    r = subprocess.run(["gh", *args], capture_output=True, text=True)
    if check and r.returncode:
        raise RuntimeError(f"gh {' '.join(args)}: {r.stderr.strip()}")
    return r


def gh_json(*args):
    r = gh(*args)
    return json.loads(r.stdout) if r.returncode == 0 and r.stdout.strip() else None


def norm(v):
    """Compare tags and conda versions: 1.3.1_4 == 1.3.1.4, v9.08.26 == 9.08.26, 1!4.11 == 4.11."""
    return re.sub(r"[-_]", ".", v.split("!")[-1]).lstrip("v").lower()


def vkey(v):
    return [(0, int(x)) if x.isdigit() else (1, x) for x in re.split(r"[.]", norm(v))]


# --------------------------------------------------------------------------- world


class World:
    """What the channel and GitHub say right now. Read once per pass."""

    def __init__(self):
        self.repodata = {}
        for sub in list(SUBDIRS.values()) + ["noarch"]:
            with urllib.request.urlopen(f"{CHANNEL}/{sub}/repodata.json") as f:
                rd = json.load(f)
            self.repodata[sub] = list({**rd.get("packages", {}), **rd.get("packages.conda", {})}.values())
        self.feedstocks = sorted(
            r["name"][: -len("-feedstock")]
            for r in gh_json("repo", "list", ORG, "-L", "500", "--json", "name") or []
            if r["name"].endswith("-feedstock")
        )
        self._recipe, self._vars, self._tags, self._main = {}, {}, {}, {}

    def recipe(self, p):
        if p not in self._recipe:
            r = gh("api", f"repos/{ORG}/{p}-feedstock/contents/recipe/meta.yaml",
                   "-H", "Accept: application/vnd.github.raw")
            self._recipe[p] = r.stdout if r.returncode == 0 else ""
        return self._recipe[p]

    def deps(self, p, names):
        return sorted(n for n in requirement_names(self.recipe(p)) if n in names and n != p)

    def linux_only(self, p):
        return bool(re.search(r"^\s*skip:.*(\[not linux\]|# \[osx\]|\bosx\b)", self.recipe(p), re.M))

    def builds(self, p, sub):
        return [m for m in self.repodata[sub] if m["name"] == p]

    def noarch(self, p):
        return bool(self.builds(p, "noarch")) and not self.builds(p, "linux-64")

    def main_sha(self, p):
        if p not in self._main:
            d = gh_json("api", f"repos/{ORG}/{p}-feedstock/commits/main", "-q", "{sha: .sha}")
            self._main[p] = d["sha"] if d else None
        return self._main[p]

    def tags(self, p):
        if p not in self._tags:
            refs = gh_json("api", f"repos/{ORG}/{p}-feedstock/git/matching-refs/tags", "--paginate") or []
            self._tags[p] = {r["ref"][len("refs/tags/"):]: r["object"]["sha"] for r in refs}
        return self._tags[p]

    def variables(self, p):
        if p not in self._vars:
            d = gh_json("api", f"repos/{ORG}/{p}-feedstock/actions/variables") or {}
            self._vars[p] = {v["name"]: v["value"] for v in d.get("variables", [])}
        return self._vars[p]

    def runs(self, p, tag, since):
        d = gh_json("run", "list", "-R", f"{ORG}/{p}-feedstock", "-w", "autoupload.yml", "-b", tag,
                    "-L", "5", "--json", "databaseId,status,conclusion,createdAt,headSha,url") or []
        return [r for r in d if r["createdAt"] >= since]

    def published_tags(self, p):
        """Tags of the versions the channel serves: the newest, plus extra.lts / release_tags."""
        text = self.recipe(p)
        tags = self.tags(p)
        rel = re.search(r"release_tags:\s*\n\s+main:\s*\[([^\]]*)\]", text)
        if rel:
            return [t.strip(" '\"") for t in rel.group(1).split(",") if t.strip(" '\"") in tags]
        versions = sorted({m["version"] for m in self.builds(p, "linux-64") + self.builds(p, "noarch")}, key=vkey)
        if not versions:
            return []
        want = [versions[-1]]
        lts = re.search(r"\blts:\s*\[([^\]]*)\]", text)
        if lts:
            want += [v.strip(" '\"") for v in lts.group(1).split(",")]
        out = []
        for v in want:
            for t in sorted(tags):
                # geant's conda version 1!4.11.4.1 carries its tag 11.4.1 as a suffix
                same = norm(t) == norm(v) or norm(v).endswith("." + norm(t))
                if same and t not in out and any(norm(x) == norm(v) for x in versions):
                    out.append(t)
                    break
        return out


# ----------------------------------------------------------------------- migration


class Migration:
    def __init__(self, path, world):
        self.path, self.w = path, world
        spec = yaml.safe_load(path.read_text())
        self.name = spec["name"]
        self.created = str(spec["created"]).replace("+00:00", "Z")
        if not self.created.endswith("Z"):
            self.created = dt.datetime.fromisoformat(self.created).strftime("%Y-%m-%dT%H:%M:%SZ")
        self.platform = spec.get("platform")
        self.max_running = int(spec.get("max_running", 6))
        names = set(world.feedstocks)
        self.graph = {p: world.deps(p, names) for p in world.feedstocks}
        if "from" in spec:
            start = set(spec["from"])
            members, todo = set(start), list(start)
            while todo:
                d = todo.pop()
                for p, ds in self.graph.items():
                    if d in ds and p not in members:
                        members.add(p)
                        todo.append(p)
        else:
            pk = spec.get("packages", "all")
            members = set(world.feedstocks) if pk == "all" else set(pk)
        self.members = sorted(members - set(spec.get("exclude", [])))
        self.status_dir = MIGRATIONS / "status"
        cache = self.status_dir / f"{self.name}.json"
        self.cache = json.loads(cache.read_text()) if cache.exists() else {}

    # -- per package

    def publish_legs(self, p):
        return self.w.variables(p).get("ANACONDA_PUBLISH", DEFAULT_PUBLISH).split(",")

    def is_done(self, p, tags):
        newest = tags[0]
        if self.platform:
            return any(norm(m["version"]) == norm(newest) for m in self.w.builds(p, SUBDIRS[self.platform]))
        legs = self.legs(p)
        stamp = dt.datetime.fromisoformat(self.created.replace("Z", "+00:00")).timestamp() * 1000
        for leg in legs:
            fresh = [m for m in self.w.builds(p, SUBDIRS[leg])
                     if norm(m["version"]) == norm(newest) and m.get("timestamp", 0) >= stamp]
            if not fresh:
                return False
        return True

    def state(self, p):
        """(state, detail) for one package, ignoring its dependencies."""
        w = self.w
        if self.platform and (w.noarch(p) or (self.platform.startswith("macos") and w.linux_only(p))):
            return "n/a", "noarch" if w.noarch(p) else "Linux only"
        tags = w.published_tags(p)
        if not tags:
            return "n/a", "nothing published"
        if self.is_done(p, tags):
            return "done", ""
        runs = {t: w.runs(p, t, self.created) for t in tags}
        live = [r for rs in runs.values() for r in rs if r["status"] != "completed"]
        if live:
            return "building", live[0]["url"]
        last = runs[tags[0]][0] if runs[tags[0]] else None
        if last and last["conclusion"] == "success":
            # built, but the channel does not show it (yet): publish lag, or the
            # leg was not in ANACONDA_PUBLISH. Treat as done for scheduling.
            return "done", "built; channel not refreshed yet"
        if last and last["headSha"] == w.main_sha(p) and self.run_failed(p, last):
            return "failed", last["url"]
        return "todo", ""

    def legs(self, p):
        """The build legs this migration needs from p."""
        if self.platform:
            return [self.platform]
        # the default legs always, plus any the repo also publishes; a platform
        # migration in flight may have narrowed ANACONDA_PUBLISH to its leg alone
        published = self.publish_legs(p)
        if len(published) == 1 and published[0] not in DEFAULT_PUBLISH.split(","):
            published = []
        legs = set(DEFAULT_PUBLISH.split(",")) | set(published)
        return sorted(l for l in legs if l in SUBDIRS)

    def run_failed(self, p, run):
        """Did this run fail on a leg this migration needs? A run that built none of
        them (another migration's, say a macOS-only one) says nothing either way."""
        d = gh_json("run", "view", str(run["databaseId"]), "-R", f"{ORG}/{p}-feedstock", "--json", "jobs") or {}
        jobs = {j["name"]: j["conclusion"] for j in d.get("jobs", [])}
        mine = [c for name, c in jobs.items() if any(name.startswith(f"build ({l},") for l in self.legs(p))]
        if not mine:
            return False
        failed = any(c != "success" for c in mine) or jobs.get("publish") not in ("success", "skipped", None)
        if failed and self.transient(p, run):
            return False
        return failed

    TRANSIENT = re.compile(r"CONNECTION FAILED|Could not download|ReadTimeoutError|"
                           r"Connection reset by peer|Temporary failure in name resolution")

    def transient(self, p, run):
        """A source download that timed out is the server's fault, not the recipe's:
        start again, up to three times per feedstock commit."""
        key = f"{p}@{run['headSha']}"
        retries = self.cache.setdefault("retries", {})
        seen = self.cache.setdefault("transient_runs", {})
        rid = str(run["databaseId"])
        if rid not in seen:
            log = gh("run", "view", rid, "-R", f"{ORG}/{p}-feedstock", "--log-failed").stdout
            seen[rid] = bool(self.TRANSIENT.search(log))
            if seen[rid]:
                retries[key] = retries.get(key, 0) + 1
        return seen[rid] and retries.get(key, 0) <= 3

    # -- actions

    def start(self, p, dry):
        tags = self.w.published_tags(p)
        main = self.w.main_sha(p)
        if dry:
            return f"would move {', '.join(tags)} to main {main[:7]}"
        repo = f"{ORG}/{p}-feedstock"
        if self.platform:
            # Build only the migrated leg. A repo that already publishes it keeps its
            # ANACONDA_PUBLISH: with one leg compiled, only that leg is uploaded.
            gh("variable", "set", "ANACONDA_COMPILE", "-R", repo, "--body", self.platform, check=True)
            if self.platform not in self.publish_legs(p):
                gh("variable", "set", "ANACONDA_PUBLISH", "-R", repo, "--body", self.platform, check=True)
        for t in tags:
            if self.w.tags(p).get(t) != main:
                gh("api", "-X", "PATCH", f"repos/{repo}/git/refs/tags/{t}", "-f", f"sha={main}",
                   "-F", "force=true", check=True)
            if self.w.tags(p).get(t) == main or not TRIGGER_TAG.match(t):
                # no push event: an unchanged tag, or one the push trigger ignores
                gh("workflow", "run", "autoupload.yml", "-R", repo, "--ref", t, "-f", "triggered_by=bot",
                   check=True)
        return f"moved {', '.join(tags)} to main {main[:7]}"

    def settle_platform_vars(self, p, state, dry):
        """Platform migration: opt a passing repo in for good, hand a failed one back."""
        if not self.platform or dry:
            return
        repo = f"{ORG}/{p}-feedstock"
        v = self.w.variables(p)
        if state == "done":
            if v.get("ANACONDA_PUBLISH") == self.platform:
                legs = DEFAULT_PUBLISH.split(",") + [self.platform]
                gh("variable", "set", "ANACONDA_PUBLISH", "-R", repo, "--body", ",".join(legs))
            if v.get("ANACONDA_COMPILE") == self.platform:
                gh("variable", "delete", "ANACONDA_COMPILE", "-R", repo)
        elif state == "failed":
            if v.get("ANACONDA_PUBLISH") == self.platform:
                gh("variable", "delete", "ANACONDA_PUBLISH", "-R", repo)
            if v.get("ANACONDA_COMPILE") == self.platform:
                gh("variable", "delete", "ANACONDA_COMPILE", "-R", repo)

    def failure_line(self, url):
        if url in self.cache.get("why", {}):
            return self.cache["why"][url]
        rid = url.rstrip("/").split("/")[-1]
        repo = "/".join(url.split("/")[3:5])
        log = gh("run", "view", rid, "-R", repo, "--log-failed").stdout
        pat = re.compile(r"(error:.*|Error: .*|nothing provides .*|Unsatisfiable .*|"
                         r"CondaBuildUserError: .*|BuildScriptException.*|No such file or directory.*)")
        why = next((m.group(1)[:160] for line in log.splitlines() if (m := pat.search(line))), "")
        self.cache.setdefault("why", {})[url] = why
        return why

    # -- one pass

    def advance(self, dry):
        own = {p: self.state(p) for p in self.members}
        final = {}

        def resolve(p, stack=()):
            if p in final:
                return final[p]
            s, d = own[p]
            if s in ("done", "n/a", "building", "failed"):
                final[p] = (s, d)
                return final[p]
            deps = [x for x in self.graph.get(p, []) if x in own and x not in stack]
            dstates = {x: resolve(x, stack + (p,))[0] for x in deps}
            bad = sorted(x for x, s2 in dstates.items() if s2 in ("failed", "blocked"))
            wait = sorted(x for x, s2 in dstates.items() if s2 not in ("done", "n/a"))
            if bad:
                final[p] = ("blocked", ", ".join(bad))
            elif wait:
                final[p] = ("waiting", ", ".join(wait))
            else:
                final[p] = ("ready", "")
            return final[p]

        for p in self.members:
            resolve(p)

        running = sum(1 for s, _ in final.values() if s == "building")
        denied = None
        for p in self.members:
            s, d = final[p]
            self.settle_platform_vars(p, s, dry)
            self.report(p, s, d, dry)
            if s != "ready" or running >= self.max_running:
                continue
            if denied:
                final[p] = ("ready", f"not started: {denied}")
                continue
            try:
                final[p] = ("building", self.start(p, dry))
                running += 1
            except RuntimeError as e:
                # Not the package's fault, so not "failed": it stays ready and
                # takes no slot. A permission refusal would refuse every other
                # package the same way, so this pass stops starting any.
                final[p] = ("ready", f"could not start: {e}")
                if "HTTP 403" in str(e):
                    denied = "HEP_BOT_TOKEN was refused (HTTP 403) on an earlier package this pass"
        return final

    # -- failure issues

    def issue_title(self):
        return f"[{self.name}] build failed"

    def report(self, p, state, detail, dry):
        """Keep one issue per failing package on its feedstock, conda-forge style:
        opened when it fails, updated when a new attempt fails, closed once it builds."""
        issues = self.cache.setdefault("issues", {})
        repo = f"{ORG}/{p}-feedstock"
        if state == "failed" and detail.startswith("http"):
            known = issues.get(p)
            if known and known["run"] == detail:
                return
            why = self.failure_line(detail)
            body = (f"The `{self.name}` migration failed to build `{p}` at `main` "
                    f"{(self.w.main_sha(p) or '')[:7]}.\n\n"
                    f"- Run: {detail}\n- First error: `{why or 'see the run log'}`\n\n"
                    f"Push a fix to `main` and hep-bot retries by itself on its next pass. "
                    f"Packages below this one wait meanwhile. Status: "
                    f"https://github.com/{ORG}/.github/blob/main/migrations/status/{self.name}.md\n\n"
                    f"<!-- hep-bot: migration {self.name} -->")
            if dry:
                return
            if known:
                gh("issue", "comment", str(known["number"]), "-R", repo, "--body", body)
                known["run"] = detail
            else:
                r = gh("issue", "create", "-R", repo, "--title", self.issue_title(), "--body", body)
                m = re.search(r"/issues/(\d+)", r.stdout)
                if m:
                    issues[p] = {"number": int(m.group(1)), "run": detail}
        elif state == "done" and p in issues and not dry:
            n = issues.pop(p)["number"]
            gh("issue", "close", str(n), "-R", repo, "--comment",
               f"Built and published by the `{self.name}` migration. Closing.\n\n"
               f"<!-- hep-bot: migration {self.name} -->")

    def write_status(self, final):
        self.status_dir.mkdir(parents=True, exist_ok=True)
        order = ["failed", "blocked", "building", "ready", "waiting", "done", "n/a"]
        counts = {s: sum(1 for x, _ in final.values() if x == s) for s in order}
        kind = f"platform `{self.platform}`" if self.platform else "rebuild"
        lines = [f"# Migration `{self.name}`", "",
                 f"{kind}, started {self.created}, updated "
                 f"{dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M')} UTC.", "",
                 " · ".join(f"{s}: {n}" for s, n in counts.items() if n), "",
                 "| Package | State | Detail |", "|---|---|---|"]
        for p in sorted(final, key=lambda p: (order.index(final[p][0]), p)):
            s, d = final[p]
            if s == "failed" and d.startswith("http"):
                d = f"[run]({d}) {self.failure_line(d)}".strip()
            elif s == "building" and d.startswith("http"):
                d = f"[run]({d})"
            lines.append(f"| {p} | {s} | {d.replace('|', '/')} |")
        (self.status_dir / f"{self.name}.md").write_text("\n".join(lines) + "\n")
        (self.status_dir / f"{self.name}.json").write_text(json.dumps(self.cache, indent=1) + "\n")
        return counts


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--only", help="advance this migration only (its name)")
    ap.add_argument("--dry-run", action="store_true", help="report and plan, change nothing")
    a = ap.parse_args()
    paths = sorted(MIGRATIONS.glob("*.yaml"))
    if a.only:
        paths = [p for p in paths if p.stem == a.only]
    if not paths:
        print("no migrations")
        return
    world = World()
    for path in paths:
        m = Migration(path, world)
        final = m.advance(a.dry_run)
        counts = m.write_status(final)
        print(f"{m.name}: " + ", ".join(f"{s} {n}" for s, n in counts.items() if n))
        for p, (s, d) in sorted(final.items()):
            if s in ("building", "failed", "blocked", "ready") or a.dry_run:
                print(f"  {p:18} {s:9} {d}")


if __name__ == "__main__":
    main()
