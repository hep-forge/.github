#!/usr/bin/env python3
"""
Keep every feedstock on its latest upstream release, and published.

For each feedstock (dag.yaml order first, then the rest; `auto_update: false`
in dag.yaml opts a package out):

  BUMP     upstream has a newer release with the same major version and the
           recipe's source is a plain tarball URL: add it to the `versions`
           dict (fresh sha256, build number 0), commit to the feedstock's
           default branch, and push the version tag -- the tag push builds
           and publishes.
  TAG      the recipe already carries a version newer than every tag (e.g. a
           hand edit, or an older hep-bot run that bumped without tagging):
           push that tag.
  HEAD     the feedstock has a `head` tag (the build of upstream's
           main/master) and either upstream committed since that build last
           ran, or the feedstock's recipe/ changed since the commit `head`
           points at: move `head` to the default branch tip, which rebuilds it.
           Having the tag is the opt-in; auto_update doesn't affect it.
  MANUAL   newer upstream release that needs a human: a new major version,
           a git source, or a URL with more jinja than {{ version }}. Listed
           in one tracking issue on the meta-repo instead of being touched.

Upstream versions come from scripts/hep_bot/sources.yaml when the package is
listed there, otherwise from the recipe itself: `git ls-remote --tags` for
GitHub/GitLab archive URLs and git_url sources, or the download directory's
listing for other tarball URLs.

The meta-repo submodule pointers are committed straight to main (render-sync
does the same daily), not through PRs.

Usage:
    python check_versions.py [--dry-run] [--only pkg[,pkg...]]

Requires: requests, pyyaml, packaging; GITHUB_TOKEN with push rights on the
feedstocks (and issues on the meta-repo) unless --dry-run.
"""
import argparse
import os
import re
import subprocess
import sys
import tempfile
from datetime import datetime
from pathlib import Path

import requests
import yaml
from packaging.version import InvalidVersion, Version

REPO_ROOT = Path(__file__).parents[2]
SOURCES = yaml.safe_load((Path(__file__).parent / "sources.yaml").read_text()) or {}
DAG = yaml.safe_load((Path(__file__).parent / "dag.yaml").read_text()) or {}
META_REPO = "hep-forge/.github"
TRACKING_TITLE = "[hep-bot] upstream updates that need a human"
NUM = r"\d+(?:\.\d+)+"
# Identify the bot to upstream download servers.
HEADERS = {"User-Agent": "hep-bot (+https://github.com/hep-forge/.github)"}


def V(s):
    try:
        v = Version(s)
    except (InvalidVersion, TypeError):
        return None
    return None if v.is_prerelease or v.is_devrelease else v


def git(*args, cwd=REPO_ROOT, check=True):
    return subprocess.run(["git", *args], cwd=cwd, check=check, capture_output=True, text=True)


# -- recipe ------------------------------------------------------------------

def feedstock_dir(name):
    return REPO_ROOT / "feedstocks" / f"{name}-feedstock"


def sync_to_default_branch(name):
    """CI checks submodules out at the pinned (possibly old) commit; work on
    the default branch tip instead, so we read and extend the live recipe."""
    d = feedstock_dir(name)
    out = git("ls-remote", "--symref", "origin", "HEAD", cwd=d).stdout
    m = re.search(r"refs/heads/(\S+)\s+HEAD", out)
    branch = m.group(1) if m else "main"
    git("fetch", "-q", "origin", branch, cwd=d)
    git("checkout", "-q", "-B", branch, f"origin/{branch}", cwd=d)
    return branch


def recipe(name):
    meta = feedstock_dir(name) / "recipe" / "meta.yaml"
    if not meta.exists():
        return None
    text = meta.read_text()
    m = re.search(r"versions\s*=\s*\{(.*?)\}", text, re.S)
    keys = re.findall(r'"([^"]+)"\s*:', m.group(1)) if m else []
    # First source only ("- url:" in a multi-source recipe): the package's
    # own upstream; later sources are add-ons built on top of it.
    url = re.search(r'^\s*(?:-\s*)?url:\s*"?([^"\n#]+)"?', text, re.M)
    git_url = re.search(r'^\s*(?:-\s*)?git_url:\s*"?([^"\n#]+)"?', text, re.M)
    if url and git_url:
        # whichever comes first is the first source
        url, git_url = (url, None) if url.start() < git_url.start() else (None, git_url)
    return {
        "text": text,
        "keys": keys,
        "current": recipe_version(text),
        "url": url.group(1).strip() if url else None,
        "git_url": git_url.group(1).strip() if git_url else None,
    }


def recipe_version(text):
    m = re.search(r"versions\s*=\s*\{(.*?)\}", text, re.S)
    keys = re.findall(r'"([^"]+)"\s*:', m.group(1)) if m else []
    numeric = [k for k in keys if V(k)]
    return max(numeric, key=V) if numeric else None


def breaking(old, new):
    """New major version -- or new minor for 0.x, where minors break APIs."""
    o, n = V(old), V(new)
    if o.major != n.major:
        return True
    return o.major == 0 and o.minor != n.minor


def plain_tarball(url):
    """True if {{ version }} is the only jinja in the source URL."""
    return bool(url) and "{{" not in re.sub(r"\{\{\s*version\s*\}\}", "", url)


# -- upstream ----------------------------------------------------------------

def latest_tag(repo_url, prefix=None, pattern=None):
    """Newest release among a git repo's tags. `prefix` is the exact text
    before the version (from the recipe URL); without it any leading name
    is allowed ("v1.2", "hoppet-2.3.0"). A `pattern` with several groups
    (pythia8318 -> 8, 3, 18) is joined with dots."""
    out = subprocess.run(["git", "ls-remote", "--tags", repo_url],
                         capture_output=True, text=True, timeout=60).stdout
    best = None
    for line in out.splitlines():
        tag = line.split("refs/tags/", 1)[-1].removesuffix("^{}")
        if pattern:
            m = re.fullmatch(pattern, tag)
            if not m:
                continue
            tag = ".".join(str(int(g)) for g in m.groups()) if len(m.groups()) > 1 else m.group(1)
        elif prefix is not None:
            if not tag.startswith(prefix):
                continue
            tag = tag[len(prefix):]
        else:
            m = re.fullmatch(rf"[A-Za-z_-]*?v?({NUM})", tag)
            tag = m.group(1) if m else ""
        if re.fullmatch(NUM, tag) and V(tag) and (best is None or V(tag) > V(best)):
            best = tag
    return best


def latest_listed(page, filename_template):
    """Newest version among files on a download page matching the URL's
    filename, with {{ version }} as the wildcard."""
    before, _, after = re.split(r"(\{\{\s*version\s*\}\})", filename_template, maxsplit=1)
    pattern = re.escape(before) + f"({NUM})" + re.escape(after)
    try:
        r = requests.get(page, timeout=20, headers=HEADERS)
        r.raise_for_status()
    except Exception as e:
        print(f"  WARNING: could not fetch {page}: {e}", file=sys.stderr)
        return None
    found = [v for v in re.findall(pattern, r.text) if V(v)]
    return max(found, key=V) if found else None


def upstream_repo(rec):
    """(git repo URL, tag prefix or None) of the recipe's upstream, if it is a
    git source or a GitHub/GitLab archive URL."""
    if rec["git_url"]:
        return rec["git_url"].removesuffix(".git"), None
    url = rec["url"] or ""
    # GitHub archive / release URLs, with the tag prefix the URL uses
    # ("v{{ version }}" -> "v").
    m = re.match(r"https?://github\.com/([^/]+/[^/]+)/(?:archive|releases)/(.*)", url)
    if m:
        pre = re.search(r"(?:tags/|download/|archive/)([^/{]*)\{\{\s*version", m.group(2))
        return f"https://github.com/{m.group(1)}", pre.group(1) if pre else None
    # GitLab-style archive URLs (gitlab.cern.ch, gitlab.com, git.ligo.org, ...)
    m = re.match(r"(https?://[^/]+/.+?)/-/archive/([^/{]*)\{\{\s*version", url)
    if m:
        return m.group(1), m.group(2)
    return None


def upstream_from_recipe(rec):
    url = rec["url"]
    if not rec["git_url"] and (not url or not re.search(r"\{\{\s*version\s*\}\}", url)):
        return None
    if repo := upstream_repo(rec):
        return latest_tag(*repo)
    if not plain_tarball(url):
        return None
    # Anything else: the download directory listing (hepforge "?f=" pages too).
    if "?f=" in url:
        page, fname = url.split("?f=", 1)
        fname = fname.rsplit("/", 1)[-1]
    else:
        page, fname = url.rsplit("/", 1)
        page += "/"
    return latest_listed(page, fname)


def upstream_from_sources(name):
    src = SOURCES[name]
    if src["type"] == "html_scrape":
        try:
            r = requests.get(src["url"], timeout=20, headers=HEADERS)
            r.raise_for_status()
        except Exception as e:
            print(f"  WARNING: could not fetch {src['url']}: {e}", file=sys.stderr)
            return None
        # A pattern with several groups (pythia8316 -> 8, 3, 16) is joined
        # with dots.
        found = [".".join(str(int(g)) for g in m) if isinstance(m, tuple) else m
                 for m in re.findall(src["pattern"], r.text)]
        found = [v for v in found if V(v)]
        return max(found, key=V) if found else None
    if src["type"] in ("git_tags", "gitlab_tags"):
        return latest_tag(src["url"], src.get("prefix"), src.get("pattern"))
    if src["type"] == "github_releases":
        headers = {}
        if token := os.environ.get("GITHUB_TOKEN"):
            headers["Authorization"] = f"Bearer {token}"
        try:
            r = requests.get(f"https://api.github.com/repos/{src['repo']}/releases/latest",
                             headers=headers, timeout=20)
            r.raise_for_status()
            return r.json().get("tag_name", "").lstrip("v") or None
        except Exception as e:
            print(f"  WARNING: could not fetch GitHub releases for {src['repo']}: {e}", file=sys.stderr)
            return None
    return None


def upstream(name, rec):
    return upstream_from_sources(name) if name in SOURCES else upstream_from_recipe(rec)


# -- actions -----------------------------------------------------------------

def feedstock_tags(name):
    out = git("ls-remote", "--tags", f"https://github.com/hep-forge/{name}-feedstock.git").stdout
    return {l.split("refs/tags/", 1)[1].removesuffix("^{}") for l in out.splitlines() if "refs/tags/" in l}


def push_tag(name, version, branch):
    d = feedstock_dir(name)
    git("tag", "-f", version, cwd=d)
    git("push", "-q", "--force", "origin", f"refs/tags/{version}", cwd=d)
    print(f"        pushed tag {version} on {branch} -> build + publish")


def tagged_recipe_version(name, version):
    d = feedstock_dir(name)
    ref = f"refs/tags/{version}"
    git("fetch", "-q", "--force", "origin", f"{ref}:{ref}", cwd=d)
    text = git("show", f"{version}:recipe/meta.yaml", cwd=d).stdout
    return recipe_version(text)


def upstream_head_time(repo_url):
    """Commit time (unix) of the upstream default branch tip."""
    with tempfile.TemporaryDirectory() as tmp:
        git("init", "-q", tmp)
        git("fetch", "-q", "--depth", "1", repo_url, "HEAD", cwd=tmp)
        return int(git("log", "-1", "--format=%ct", "FETCH_HEAD", cwd=tmp).stdout.strip())


def last_head_build_time(name):
    """Start time (unix) of the newest autoupload run at the `head` tag."""
    r = subprocess.run(["gh", "run", "list", "--repo", f"hep-forge/{name}-feedstock",
                        "--workflow", "autoupload.yml", "--branch", "head", "--limit", "1",
                        "--json", "createdAt", "--jq", ".[0].createdAt // empty"],
                       capture_output=True, text=True)
    stamp = r.stdout.strip()
    if not stamp:
        return 0
    return int(datetime.fromisoformat(stamp.replace("Z", "+00:00")).timestamp())


def recipe_changed_since_head(name, branch):
    """True if recipe/ differs between the commit the `head` tag points at
    and the default branch tip (a recipe fix that `head` hasn't picked up)."""
    out = git("ls-remote", f"https://github.com/hep-forge/{name}-feedstock.git",
              "refs/tags/head", "refs/tags/head^{}").stdout.split()
    if not out:
        return False
    head_sha = out[-2]  # peeled commit when annotated, else the tag's own
    r = subprocess.run(["gh", "api", f"repos/hep-forge/{name}-feedstock/compare/{head_sha}...{branch or 'main'}",
                        "--jq", '[.files[]?.filename | select(startswith("recipe/"))] | length'],
                       capture_output=True, text=True)
    return r.returncode == 0 and r.stdout.strip() not in ("", "0")


def refresh_head(name, branch):
    """Move `head` to the default branch tip (the push rebuilds it); if it is
    already there, dispatch the build at the tag instead."""
    d = feedstock_dir(name)
    git("tag", "-f", "head", cwd=d)
    pushed = git("push", "--porcelain", "-f", "origin", "refs/tags/head", cwd=d).stdout
    if "[up to date]" in pushed:
        subprocess.run(["gh", "workflow", "run", "autoupload.yml", "--repo",
                        f"hep-forge/{name}-feedstock", "--ref", "head", "-f", "triggered_by=bot"],
                       check=True)
    print(f"        rebuilding head of {name}")


def bump(name, old, new, branch):
    subprocess.run([sys.executable, str(Path(__file__).parent / "bump_version.py"), name, new],
                   check=True)
    d = feedstock_dir(name)
    git("add", "recipe/meta.yaml", cwd=d)
    git("commit", "-q", "-m", f"[hep-bot] bump to {new}", cwd=d)
    git("push", "-q", "origin", f"HEAD:refs/heads/{branch}", cwd=d)
    push_tag(name, new, branch)


def recipe_maintainers(name):
    meta = feedstock_dir(name) / "recipe" / "meta.yaml"
    try:
        text = meta.read_text()
        text = re.sub(r"\{%.*?%\}", "", text, flags=re.S)
        text = re.sub(r"\{#.*?#\}", "", text, flags=re.S)
        text = re.sub(r"\{\{.*?\}\}", "JINJA_VALUE", text)
        data = yaml.safe_load(text) or {}
    except (OSError, yaml.YAMLError):
        return []
    maintainers = (data.get("extra", {}) or {}).get("recipe-maintainers", []) or []
    if isinstance(maintainers, str):
        maintainers = [maintainers]
    return sorted({m for m in maintainers
                   if isinstance(m, str) and re.fullmatch(r"[A-Za-z0-9-]+", m)})


def update_tracking_issue(manual):
    """One open issue listing everything that needs a human; closed when empty."""
    r = subprocess.run(["gh", "issue", "list", "--repo", META_REPO, "--state", "open",
                        "--search", f'in:title "{TRACKING_TITLE}"', "--json", "number,title",
                        "--jq", f'.[] | select(.title == "{TRACKING_TITLE}") | .number'],
                       capture_output=True, text=True)
    number = r.stdout.split()[0] if r.stdout.split() else None
    if not manual:
        if number:
            subprocess.run(["gh", "issue", "close", number, "--repo", META_REPO,
                            "--comment", "Nothing left to update by hand."], check=False)
        return
    maintainers = {n: recipe_maintainers(n) for n, *_ in manual}
    rows = "\n".join(
        f"| [{n}](https://github.com/hep-forge/{n}-feedstock) | `{o}` | `{u}` | "
        f"{why} | {', '.join('@' + m for m in maintainers[n]) or 'not listed'} |"
        for n, o, u, why in manual)
    body = ("Upstream has newer releases that hep-bot does not apply on its own. Update the recipe "
            "and push the version tag, or set `auto_update: false` in `scripts/hep_bot/dag.yaml` "
            "to silence a package. This list is rewritten by every version check.\n\n"
            "| Feedstock | Recipe | Upstream | Why not automatic | Maintainers |\n"
            "|---|---|---|---|---|\n" + rows)
    if number:
        previous = subprocess.run(
            ["gh", "issue", "view", number, "--repo", META_REPO, "--json", "body", "--jq", ".body"],
            capture_output=True, text=True)
        subprocess.run(["gh", "issue", "edit", number, "--repo", META_REPO, "--body", body], check=False)
        if previous.returncode == 0 and previous.stdout.strip() == body:
            return
        recipients = sorted({m for values in maintainers.values() for m in values})
        packages = ", ".join(n for n, *_ in manual)
        mentions = " ".join("@" + m for m in recipients)
        notification = (f"Human action is requested for: {packages}.\n\n"
                        f"Please review the updated table above. {mentions}".rstrip())
        subprocess.run(["gh", "issue", "comment", number, "--repo", META_REPO,
                        "--body", notification], check=False)
    else:
        subprocess.run(["gh", "issue", "create", "--repo", META_REPO, "--title", TRACKING_TITLE,
                        "--body", body], check=False)


def commit_pointers(changed):
    if not changed:
        return
    git("add", *[f"feedstocks/{n}-feedstock" for n in changed])
    if not git("diff", "--cached", "--quiet", check=False).returncode:
        return
    git("commit", "-q", "-m", "[hep-bot] " + ", ".join(changed))
    if git("push", "-q", check=False).returncode:
        git("pull", "-q", "--rebase")
        git("push", "-q")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true", help="print the plan, change nothing")
    parser.add_argument("--only", default="", help="comma list of packages")
    args = parser.parse_args()

    names = [n for n in DAG if feedstock_dir(n).exists()]
    names += sorted(p.name[: -len("-feedstock")] for p in (REPO_ROOT / "feedstocks").glob("*-feedstock")
                    if p.name[: -len("-feedstock")] not in DAG)
    if args.only:
        names = [n for n in names if n in args.only.split(",")]

    changed, manual, failures = [], [], []
    for name in names:
        try:
            branch = sync_to_default_branch(name) if not args.dry_run else None
            rec = recipe(name)
            tags = feedstock_tags(name)
            if rec and "head" in tags and (repo := upstream_repo(rec)):
                if upstream_head_time(repo[0]) > last_head_build_time(name):
                    why = "upstream main/master moved since the last head build"
                elif recipe_changed_since_head(name, branch):
                    why = "recipe/ changed since the commit head points at"
                else:
                    why = None
                if why:
                    print(f"HEAD   {name}: {why}")
                    if not args.dry_run:
                        refresh_head(name, branch)
                        changed.append(name)

            if (DAG.get(name) or {}).get("auto_update") is False:
                continue
            if not rec or not rec["current"]:
                print(f"SKIP   {name}: no numeric version in recipe")
                continue
            cur = rec["current"]
            up = upstream(name, rec)
            newest_tag = max((t for t in tags if V(t)), key=V, default=None)

            if up and V(up) > V(cur):
                if breaking(cur, up):
                    why = "new major version"
                elif rec["git_url"] or not plain_tarball(rec["url"]):
                    why = "git or templated source"
                else:
                    why = None
                if why:
                    print(f"MANUAL {name}: {cur} -> {up} ({why})")
                    manual.append((name, cur, up, why))
                else:
                    print(f"BUMP   {name}: {cur} -> {up}")
                    if not args.dry_run:
                        bump(name, cur, up, branch)
                        changed.append(name)
                    continue

            if cur not in tags and (newest_tag is None or V(cur) > V(newest_tag)):
                print(f"TAG    {name}: recipe {cur} is newer than tag {newest_tag}")
                if not args.dry_run:
                    push_tag(name, cur, branch)
                    changed.append(name)
            elif cur in tags and (
                    (tagged_cur := tagged_recipe_version(name, cur)) is None
                    or V(tagged_cur) < V(cur)):
                print(f"TAG    {name}: tag {cur} points to recipe {tagged_cur}")
                if not args.dry_run:
                    push_tag(name, cur, branch)
                    changed.append(name)
            elif not (up and V(up) > V(cur)):
                print(f"OK     {name}: {cur}" + ("" if up else " (upstream unknown)"))
        except Exception as e:
            print(f"ERROR  {name}: {e}", file=sys.stderr)
            failures.append(name)

    if not args.dry_run:
        commit_pointers(changed)
        update_tracking_issue(manual)

    if summary := os.environ.get("GITHUB_STEP_SUMMARY"):
        with open(summary, "a") as f:
            f.write(f"### hep-bot version check\n\nUpdated: {', '.join(changed) or 'none'}\n\n"
                    f"Needs a human: {', '.join(n for n, *_ in manual) or 'none'}\n\n"
                    f"Errors: {', '.join(failures) or 'none'}\n")
    if failures:
        print(f"\n{len(failures)} package(s) failed: {', '.join(failures)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
