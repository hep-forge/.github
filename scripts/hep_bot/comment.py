#!/usr/bin/env python3
"""hep-bot issue commands.

Run by .github/workflows/hep-bot-comment.yml (same file in this meta-repo
and in every feedstock, synced from scripts/templates/). The workflow
checks this script out of hep-forge/.github, so changing a command here
needs no fleet-wide re-sync.

Commands, in an issue body (on open) or a comment:

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
("@hep-bot, please rerender").
"""
import json
import os
import re
import subprocess
import sys

META_REPO = "hep-forge/.github"
ORG = "hep-forge"
TRUSTED = ("OWNER", "MEMBER", "COLLABORATOR")

event_name = os.environ["EVENT_NAME"]
event = json.load(open(os.environ["GITHUB_EVENT_PATH"]))
repo = os.environ["REPO"]
repo_name = repo.split("/", 1)[1]
has_pat = os.environ.get("HAS_PAT") == "true"
run_url = os.environ.get("RUN_URL", "")

issue = event["issue"]
issue_number = str(issue["number"])
if event_name == "issues":
    text = issue.get("body") or ""
    title = issue.get("title") or ""
    author = issue["user"]["login"]
    association = issue.get("author_association", "NONE")
else:
    text = event["comment"].get("body") or ""
    title = ""
    author = event["comment"]["user"]["login"]
    association = event["comment"].get("author_association", "NONE")

self_pkg = repo_name[: -len("-feedstock")] if repo_name.endswith("-feedstock") else None


def gh(*args, check=False):
    return subprocess.run(["gh", *args], capture_output=True, text=True, check=check)


def reply(msg):
    gh("issue", "comment", issue_number, "--repo", repo, "--body", msg)


def form_fields(body):
    """Issue-form body -> {heading: value}; '_No response_' counts as empty."""
    fields = {}
    for m in re.finditer(r"^###\s+(.+?)\s*\n(.*?)(?=^###\s|\Z)", body, re.M | re.S):
        value = m.group(2).strip()
        fields[m.group(1).strip().lower()] = "" if value == "_No response_" else value
    return fields


def parse():
    """-> (command, args list, kwargs dict) or None if not addressed to us."""
    low = title.lower()
    if low.startswith("[new-feedstock]"):
        f = form_fields(text)
        return "new", [f.get("package name", ""), f.get("upstream repository", "")], {
            "summary": f.get("summary", ""),
            "license": f.get("license", ""),
            "maintainers": f.get("maintainers", ""),
        }
    if low.startswith("[rerender]"):
        f = form_fields(text)
        pkg = f.get("package name", "")
        return "rerender", [pkg] if pkg else [], {}

    m = re.search(r"@hep-bot\b[\s,:]*(?:please\s+)?(rerun|rerender|render|new|help)\b(.*)",
                  text, re.I)
    if not m:
        return None
    cmd = m.group(1).lower()
    cmd = "rerender" if cmd == "render" else cmd
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


def authorized():
    if association in TRUSTED:
        return True
    # author_association can under-report (e.g. outside collaborators
    # added through a team); ask the API before refusing.
    r = gh("api", f"repos/{repo}/collaborators/{author}/permission", "--jq", ".permission")
    return r.returncode == 0 and r.stdout.strip() in ("admin", "maintain", "write")


def dispatch_meta(workflow, fields):
    """Start a workflow in the meta-repo; it replies on this issue when done."""
    if repo != META_REPO and not has_pat:
        return (f"this repo cannot start workflows in `{META_REPO}` (the `HEP_BOT_TOKEN` "
                f"secret is only set there). Open the same request as an issue in "
                f"[{META_REPO}](https://github.com/{META_REPO}/issues/new/choose).")
    args = ["workflow", "run", workflow, "--repo", META_REPO, "--ref", "main",
            "-f", f"issue_repo={repo}", "-f", f"issue_number={issue_number}"]
    for k, v in fields.items():
        args += ["-f", f"{k}={v}"]
    r = gh(*args)
    return None if r.returncode == 0 else f"failed to start `{workflow}`: {r.stderr.strip()}"


HELP = f"""Commands (repo collaborators only):

| Command | Does |
|---|---|
| `@hep-bot rerun [<pkg>] <tag>` | rebuild and publish an existing release tag (amd64 + arm64) |
| `@hep-bot rerender [<pkg>]` | re-apply the hep-forge render (CI workflow, bot workflow, README, AGENTS.md) and register the feedstock in `{META_REPO}` |
| `@hep-bot new <pkg> <upstream-url> [license=<spdx>] [maintainers=a,b] [summary...]` | scaffold `hep-forge/<pkg>-feedstock` with a starter recipe |

`<pkg>` defaults to this repo inside a `<pkg>-feedstock` repo. Publishing only happens on a numeric tag; neither `rerender` nor `new` publishes anything."""


def main():
    parsed = parse()
    if parsed is None:
        return  # some other @hep-bot mention
    cmd, tokens, kwargs = parsed

    if cmd == "help":
        reply(f"@{author} {HELP}")
        return

    if not authorized():
        reply(f"@{author} sorry, only repo collaborators can run hep-bot commands.")
        return

    if cmd == "rerun":
        if len(tokens) >= 2:
            pkg, version = tokens[0], tokens[1]
        elif len(tokens) == 1 and self_pkg:
            pkg, version = self_pkg, tokens[0]
        else:
            reply(f"@{author} usage: `@hep-bot rerun <tag>` in a feedstock, or "
                  f"`@hep-bot rerun <package> <tag>` anywhere.")
            return
        feedstock = f"{ORG}/{pkg}-feedstock"
        if feedstock != repo and not has_pat:
            reply(f"@{author} only `{META_REPO}` can rebuild other feedstocks; run this there "
                  f"or in `{feedstock}`'s own issues.")
            return
        if gh("repo", "view", feedstock).returncode != 0:
            reply(f"@{author} couldn't find `{feedstock}` -- use the bare package name.")
            return
        tags = subprocess.run(["git", "ls-remote", "--tags", f"https://github.com/{feedstock}.git",
                               f"refs/tags/{version}"], capture_output=True, text=True)
        if not tags.stdout.strip():
            reply(f"@{author} tag `{version}` not found on `{feedstock}`. Push the tag first "
                  f"(pushing it already starts the build), or check its spelling.")
            return
        r = gh("workflow", "run", "autoupload.yml", "--repo", feedstock, "--ref", version,
               "-f", "triggered_by=bot")
        if r.returncode != 0:
            reply(f"@{author} failed to trigger the rebuild: {r.stderr.strip()}")
            return
        reply(f"@{author} rebuilding `{pkg}` at `{version}` (amd64 + arm64): "
              f"[Actions](https://github.com/{feedstock}/actions/workflows/autoupload.yml).")

    elif cmd == "rerender":
        pkg = tokens[0] if tokens else self_pkg
        if not pkg:
            reply(f"@{author} which feedstock? `@hep-bot rerender <package>`.")
            return
        pkg = pkg.removesuffix("-feedstock")
        if gh("repo", "view", f"{ORG}/{pkg}-feedstock").returncode != 0:
            reply(f"@{author} couldn't find `{ORG}/{pkg}-feedstock`. To create it: "
                  f"`@hep-bot new {pkg} <upstream-url>`.")
            return
        err = dispatch_meta("render-sync.yml", {"feedstock": pkg})
        reply(f"@{author} {err}" if err else
              f"@{author} rendering `{pkg}-feedstock`; I'll report back here when it's done.")

    elif cmd == "new":
        name = (tokens[0] if tokens else "").removesuffix("-feedstock").lower()
        upstream = tokens[1] if len(tokens) > 1 else ""
        if not re.fullmatch(r"[a-z0-9][a-z0-9._-]*", name) or not upstream.startswith("http"):
            reply(f"@{author} usage: `@hep-bot new <package> <upstream-url> [license=<spdx>] "
                  f"[maintainers=a,b] [one-line summary]`.")
            return
        if gh("repo", "view", f"{ORG}/{name}-feedstock").returncode == 0:
            has_recipe = gh("api", f"repos/{ORG}/{name}-feedstock/contents/recipe/meta.yaml").returncode == 0
            if has_recipe:
                reply(f"@{author} `{ORG}/{name}-feedstock` already has a recipe -- "
                      f"use `@hep-bot rerender {name}` instead.")
                return
        maintainers = kwargs.get("maintainers") or author
        err = dispatch_meta("new-feedstock.yml", {
            "name": name,
            "upstream": upstream,
            "summary": kwargs.get("summary", "") or "TODO: one-line summary",
            "license": kwargs.get("license", "") or "TODO",
            "maintainers": maintainers,
        })
        reply(f"@{author} {err}" if err else
              f"@{author} scaffolding `{ORG}/{name}-feedstock`; I'll report back here when it's done.")


main()
