#!/usr/bin/env python3
"""hep-bot issue commands.

Two ways in, one handler:

  event mode   run by .github/workflows/hep-bot-comment.yml (same file in
               this meta-repo and in every feedstock, synced from
               scripts/templates/) on the issue or comment that was just
               written; answers within a minute.
  --sweep      run by .github/workflows/hep-bot-sweep.yml in this
               meta-repo every 10 minutes: searches every hep-forge repo
               for recent requests nobody answered -- repos without the
               workflow, or a run that failed -- and handles them. This
               is what makes the bot work org-wide.

The workflows check this script out of hep-forge/.github, so changing a
command here needs no fleet-wide re-sync.

Commands, in an issue body or a comment:

  @hep-bot rerun [<pkg>] <tag>      rebuild + publish an existing tag
  @hep-bot rerender [<pkg>]         re-apply the hep-forge render (CI
                                    workflow, bot workflow, README,
                                    AGENTS.md) and register the feedstock
                                    as a submodule here if it is missing
  @hep-bot new <pkg> <upstream-url> [license=<spdx>] [maintainers=a,b] [summary text...]
                                    scaffold hep-forge/<pkg>-feedstock
  @hep-bot help

Issues opened from the forms in .github/ISSUE_TEMPLATE/ carry no
command text; they are recognised by their title prefix
("[rerender]" / "[new-feedstock]") and their form fields.

<pkg> is inferred from the repo name inside <pkg>-feedstock repos.
"please", commas and colons around the command are tolerated
("@hep-bot, please rerender"). A line starting with @hep-bot that is not
a command gets the help text. Every handled request gets a 👀 reaction
and a reply carrying a hidden marker, so it is never handled twice.
"""
import json
import os
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone

META_REPO = "hep-forge/.github"
ORG = "hep-forge"
TRUSTED = ("OWNER", "MEMBER", "COLLABORATOR")
SWEEP_DAYS = 7         # how far back the sweep looks
SWEEP_GRACE_MIN = 10   # leave fresh requests to the per-repo workflow

has_pat = os.environ.get("HAS_PAT") == "true"


def gh(*args, check=False):
    return subprocess.run(["gh", *args], capture_output=True, text=True, check=check)


MARK = "<!-- hep-bot:"


def marker(source):
    return f"{MARK}{source} -->"


class Request:
    """One issue body or comment addressed to hep-bot."""

    def __init__(self, repo, issue_number, text, title, author, association, source, react_path):
        self.repo = repo
        self.repo_name = repo.split("/", 1)[1]
        self.issue = str(issue_number)
        self.text = text or ""
        self.title = title or ""
        self.author = author
        self.association = association or "NONE"
        self.source = source            # "issue-<id>" or "comment-<id>"
        self.react_path = react_path    # API path of the item's reactions
        n = self.repo_name
        self.self_pkg = n[: -len("-feedstock")] if n.endswith("-feedstock") else None

    def reply(self, msg, handled=True):
        """handled=False leaves the request open for the sweep."""
        tail = f"\n\n{marker(self.source)}" if handled else ""
        gh("issue", "comment", self.issue, "--repo", self.repo,
           "--body", f"@{self.author} {msg}{tail}")

    def ack(self):
        gh("api", "-X", "POST", self.react_path, "-f", "content=eyes")


def form_fields(body):
    """Issue-form body -> {heading: value}; '_No response_' counts as empty."""
    fields = {}
    for m in re.finditer(r"^###\s+(.+?)\s*\n(.*?)(?=^###\s|\Z)", body, re.M | re.S):
        value = m.group(2).strip()
        fields[m.group(1).strip().lower()] = "" if value == "_No response_" else value
    return fields


def parse(req):
    """-> (command, args list, kwargs dict), or None if not addressed to us."""
    low = req.title.lower()
    if low.startswith("[new-feedstock]"):
        f = form_fields(req.text)
        return "new", [f.get("package name", ""), f.get("upstream repository", "")], {
            "summary": f.get("summary", ""),
            "license": f.get("license", ""),
            "maintainers": f.get("maintainers", ""),
        }
    if low.startswith("[rerender]"):
        f = form_fields(req.text)
        pkg = f.get("package name", "")
        return "rerender", [pkg] if pkg else [], {}

    m = re.search(r"@hep-bot\b[\s,:]*(?:please\s+)?(rerun|rebuild|rerender|render|new|help)\b(.*)",
                  req.text, re.I)
    if not m:
        # "@hep-bot <something else>" at the start of a line is meant for
        # us: answer with the help. A mention mid-sentence ("thanks
        # @hep-bot") is not.
        if re.search(r"^\s*@hep-bot\b", req.text, re.I | re.M):
            return "help", [], {}
        return None
    cmd = {"render": "rerender", "rebuild": "rerun"}.get(m.group(1).lower(), m.group(1).lower())
    line = m.group(2).splitlines()[0] if m.group(2) else ""
    kwargs = {}
    for k, v in re.findall(r"\b(license|maintainers)=(\S+)", line):
        kwargs[k] = v
    line = re.sub(r"\b(license|maintainers)=\S+", "", line)
    if cmd == "rerun":
        # Trailing "for arm and amd" is accepted and ignored: both
        # architectures always rebuild together in one matrix run.
        line = re.split(r"\bfor\b", line, maxsplit=1, flags=re.I)[0]
    tokens = [t.strip(",.") for t in line.split()]
    tokens = [t for t in tokens if t and t.lower() not in ("please", "it", "this", "the", "feedstock")]
    if cmd == "new" and len(tokens) > 2:
        kwargs["summary"] = " ".join(tokens[2:])
        tokens = tokens[:2]
    return cmd, tokens, kwargs


def authorized(req):
    if req.association in TRUSTED:
        return True
    # author_association can under-report (e.g. outside collaborators
    # added through a team); ask the API before refusing.
    r = gh("api", f"repos/{req.repo}/collaborators/{req.author}/permission", "--jq", ".permission")
    return r.returncode == 0 and r.stdout.strip() in ("admin", "maintain", "write")


def dispatch_meta(req, workflow, fields):
    """Start a workflow in the meta-repo; it replies on the issue when done.
    True when started; otherwise it has already replied."""
    if req.repo != META_REPO and not has_pat:
        req.reply(f"got it. This repo can't reach `{META_REPO}` directly, so the org-wide "
                  f"sweep will pick this up within {SWEEP_GRACE_MIN} minutes.", handled=False)
        return False
    args = ["workflow", "run", workflow, "--repo", META_REPO, "--ref", "main",
            "-f", f"issue_repo={req.repo}", "-f", f"issue_number={req.issue}"]
    for k, v in fields.items():
        args += ["-f", f"{k}={v}"]
    r = gh(*args)
    if r.returncode != 0:
        req.reply(f"I couldn't start `{workflow}`: {r.stderr.strip()}")
        return False
    return True


HELP = f"""here is what I can do (org members and collaborators only):

| Command | What it does |
|---|---|
| `@hep-bot rerun [<pkg>] <tag>` | Rebuilds and publishes an existing tag (amd64 + arm64) |
| `@hep-bot rerender [<pkg>]` | Renders the feedstock (CI workflow, bot workflow, README, AGENTS.md) and registers it in `{META_REPO}` |
| `@hep-bot new <pkg> <upstream-url> [license=<spdx>] [maintainers=a,b] [summary]` | Creates `hep-forge/<pkg>-feedstock` with a starter recipe |
| `@hep-bot help` | This table |

`<pkg>` defaults to this repo inside a `<pkg>-feedstock` repo. Only a tag publishes: a numeric release tag, or `head` for upstream main/master. The issue forms in [New issue](https://github.com/{META_REPO}/issues/new/choose) do the same as `new` and `rerender`."""


def handle(req):
    parsed = parse(req)
    if parsed is None:
        return False
    cmd, tokens, kwargs = parsed
    req.ack()

    if cmd == "help":
        req.reply(HELP)
        return True

    if not authorized(req):
        req.reply("sorry, only org members and repo collaborators can run hep-bot commands.")
        return True

    if cmd == "rerun":
        if len(tokens) >= 2:
            pkg, version = tokens[0], tokens[1]
        elif len(tokens) == 1 and req.self_pkg:
            pkg, version = req.self_pkg, tokens[0]
        else:
            req.reply("usage: `@hep-bot rerun <tag>` in a feedstock, or "
                      "`@hep-bot rerun <package> <tag>` anywhere.")
            return True
        pkg = pkg.removesuffix("-feedstock")
        feedstock = f"{ORG}/{pkg}-feedstock"
        if feedstock != req.repo and not has_pat:
            req.reply(f"only `{META_REPO}` can rebuild other feedstocks; run this there "
                      f"or in `{feedstock}`'s own issues.")
            return True
        if gh("repo", "view", feedstock).returncode != 0:
            req.reply(f"I couldn't find `{feedstock}`. Use the bare package name.")
            return True
        tags = subprocess.run(["git", "ls-remote", "--tags", f"https://github.com/{feedstock}.git",
                               f"refs/tags/{version}"], capture_output=True, text=True)
        if not tags.stdout.strip():
            req.reply(f"tag `{version}` doesn't exist on `{feedstock}`. Pushing a new tag already "
                      f"starts the build.")
            return True
        r = gh("workflow", "run", "autoupload.yml", "--repo", feedstock, "--ref", version,
               "-f", "triggered_by=bot")
        if r.returncode != 0:
            req.reply(f"I couldn't start the rebuild: {r.stderr.strip()}")
            return True
        req.reply(f"rebuilding `{pkg}` at `{version}` (amd64 + arm64): "
                  f"[Actions](https://github.com/{feedstock}/actions/workflows/autoupload.yml).")

    elif cmd == "rerender":
        pkg = tokens[0] if tokens else req.self_pkg
        if not pkg:
            req.reply("which feedstock? `@hep-bot rerender <package>`.")
            return True
        pkg = pkg.removesuffix("-feedstock")
        if gh("repo", "view", f"{ORG}/{pkg}-feedstock").returncode != 0:
            req.reply(f"`{ORG}/{pkg}-feedstock` doesn't exist. To create it: "
                      f"`@hep-bot new {pkg} <upstream-url>`.")
            return True
        if dispatch_meta(req, "render-sync.yml", {"feedstock": pkg}):
            req.reply(f"rendering `{pkg}-feedstock`. I'll report back here when it's done.")

    elif cmd == "new":
        name = (tokens[0] if tokens else "").removesuffix("-feedstock").lower()
        upstream = tokens[1] if len(tokens) > 1 else ""
        if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", name) or not upstream.startswith("http"):
            req.reply("usage: `@hep-bot new <package> <upstream-url> [license=<spdx>] "
                      "[maintainers=a,b] [one-line summary]`.")
            return True
        if gh("repo", "view", f"{ORG}/{name}-feedstock").returncode == 0:
            if gh("api", f"repos/{ORG}/{name}-feedstock/contents/recipe/meta.yaml").returncode == 0:
                req.reply(f"`{ORG}/{name}-feedstock` already has a recipe. "
                          f"Use `@hep-bot rerender {name}` instead.")
                return True
        started = dispatch_meta(req, "new-feedstock.yml", {
            "name": name,
            "upstream": upstream,
            "summary": kwargs.get("summary", "") or "TODO: one-line summary",
            "license": kwargs.get("license", "") or "TODO",
            "maintainers": kwargs.get("maintainers") or req.author,
        })
        if started:
            req.reply(f"creating `{ORG}/{name}-feedstock`. I'll report back here when it's done.")
    return True


# -- event mode ----------------------------------------------------------------

def from_event():
    event = json.load(open(os.environ["GITHUB_EVENT_PATH"]))
    repo = os.environ["REPO"]
    issue = event["issue"]
    if os.environ["EVENT_NAME"] == "issues":
        return Request(repo, issue["number"], issue.get("body"), issue.get("title"),
                       issue["user"]["login"], issue.get("author_association"),
                       f"issue-{issue['id']}",
                       f"repos/{repo}/issues/{issue['number']}/reactions")
    c = event["comment"]
    return Request(repo, issue["number"], c.get("body"), "", c["user"]["login"],
                   c.get("author_association"), f"comment-{c['id']}",
                   f"repos/{repo}/issues/comments/{c['id']}/reactions")


# -- sweep mode ----------------------------------------------------------------

def api_json(path):
    r = gh("api", path)
    if r.returncode != 0:
        print(f"WARNING: gh api {path}: {r.stderr.strip()}", file=sys.stderr)
        return None
    return json.loads(r.stdout)


def sweep(dry_run=False):
    now = datetime.now(timezone.utc)
    since = (now - timedelta(days=SWEEP_DAYS)).strftime("%Y-%m-%d")
    grace = now - timedelta(minutes=SWEEP_GRACE_MIN)
    found = {}
    for q in (f'org:{ORG} "@hep-bot" updated:>={since}',
              f'org:{ORG} in:title "[rerender]" updated:>={since}',
              f'org:{ORG} in:title "[new-feedstock]" updated:>={since}'):
        r = gh("api", "-X", "GET", "search/issues", "-f", f"q={q} is:issue is:open",
               "-f", "per_page=100", "--jq", ".items[] | [.repository_url, .number] | @tsv")
        for line in r.stdout.splitlines():
            url, num = line.split("\t")
            found[(url.split("/repos/", 1)[1], int(num))] = True

    handled = 0
    for repo, num in found:
        issue = api_json(f"repos/{repo}/issues/{num}")
        if not issue or issue.get("pull_request"):
            continue
        comments = api_json(f"repos/{repo}/issues/{num}/comments?per_page=100") or []
        done = {m for c in comments for m in re.findall(r"<!-- hep-bot:(\S+) -->", c.get("body") or "")}
        items = [Request(repo, num, issue.get("body"), issue.get("title"), issue["user"]["login"],
                         issue.get("author_association"), f"issue-{issue['id']}",
                         f"repos/{repo}/issues/{num}/reactions")]
        items[0].created = issue["created_at"]
        for c in comments:
            if MARK in (c.get("body") or ""):
                continue  # our own replies
            req = Request(repo, num, c.get("body"), "", c["user"]["login"],
                          c.get("author_association"), f"comment-{c['id']}",
                          f"repos/{repo}/issues/comments/{c['id']}/reactions")
            req.created = c["created_at"]
            items.append(req)
        for req in items:
            created = datetime.fromisoformat(req.created.replace("Z", "+00:00"))
            if req.source in done or created > grace or created < now - timedelta(days=SWEEP_DAYS):
                continue
            if parse(req) is None:
                continue
            print(f"{'WOULD HANDLE' if dry_run else 'HANDLE'} {repo}#{num} {req.source}")
            if not dry_run:
                handle(req)
            handled += 1
    print(f"sweep: {len(found)} issue(s) looked at, {handled} request(s) handled")


if __name__ == "__main__":
    if "--sweep" in sys.argv:
        sweep(dry_run="--dry-run" in sys.argv)
    else:
        handle(from_event())
