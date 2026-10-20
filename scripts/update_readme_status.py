#!/usr/bin/env python3
"""Refresh the feedstock status table in the top-level README.md.

For every feedstock the table shows the latest feedstock git tag next to
what is actually published on anaconda.org (per architecture), so tag !=
published immediately exposes a failed or still-running build. Run it
AFTER a rebuild wave has finished (see scripts/arch_status.sh), then
commit the README:

    python3 scripts/update_readme_status.py
    git add README.md && git commit -m "docs: refresh feedstock status table"

The table lives between the status:begin/status:end markers; everything
else in README.md is left untouched.
"""
import json
import re
import subprocess
import sys
import urllib.request
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

ORG = "hep-forge"
ROOT = Path(__file__).resolve().parent.parent
BEGIN = "<!-- status:begin -->"
END = "<!-- status:end -->"

# anaconda.org subdir -> table column
ARCHES = {"linux-64": "amd64", "linux-aarch64": "arm64"}


def release_tags(feedstock: Path) -> set:
    """Non-numeric tags the recipe declares as real releases.

    Same extra.release_tags block the autoupload trim step reads (e.g.
    root-plus ships "beta" as its released version); flat list or keyed
    by branch label, all branches merged here.
    """
    try:
        import yaml
        text = (feedstock / "recipe" / "meta.yaml").read_text()
    except (ImportError, OSError):
        return set()
    text = re.sub(r"\{%.*?%\}", "", text, flags=re.DOTALL)
    text = re.sub(r"\{\{.*?\}\}", "JINJA_VALUE", text)
    try:
        meta = yaml.safe_load(text) or {}
    except yaml.YAMLError:
        return set()
    raw = (meta.get("extra") or {}).get("release_tags") or {}
    if isinstance(raw, list):
        return {str(v) for v in raw}
    return {str(v) for vs in raw.values() for v in (vs or [])}


def latest_tag(feedstock: Path) -> str:
    # A recipe versioned by name (extra.release_tags) releases from those
    # tags; any numeric tag left in such a repo predates the switch (e.g.
    # root-plus's 1.0.0 after consolidating onto beta). Among them take
    # the most recently created, since a name says nothing about order.
    named = release_tags(feedstock)
    if named:
        dated = subprocess.run(
            ["git", "-C", str(feedstock), "for-each-ref", "refs/tags",
             "--sort=-creatordate", "--format=%(refname:short)"],
            capture_output=True, text=True,
        ).stdout.split()
        for t in dated:
            if t in named:
                return t
    out = subprocess.run(
        ["git", "-C", str(feedstock), "tag", "--sort=-v:refname"],
        capture_output=True, text=True,
    ).stdout.split()
    if not out:
        # stale local clone: fall back to the remote's tags
        remote = subprocess.run(
            ["git", "-C", str(feedstock), "ls-remote", "--tags", "origin"],
            capture_output=True, text=True, timeout=30,
        ).stdout
        out = sorted((line.split("refs/tags/", 1)[1]
                      for line in remote.splitlines()
                      if "refs/tags/" in line and not line.endswith("^{}")),
                     reverse=True)
    # CI only fires on numeric tags; prefer those over master/beta/rNN
    numeric = [t for t in out if re.match(r"^\d", t)]
    return (numeric or out or [""])[0]


def normalize(v: str) -> str:
    """Version as conda compares it, for tag-vs-published matching.

    CI publishes tag "X-free" as version "X.free" (dashes become dots),
    and conda treats "1" and "1.0" as the same version.
    """
    parts = re.split(r"[._-]", v.lower())
    while len(parts) > 1 and parts[-1] == "0":
        parts.pop()
    return ".".join(parts)


def version_key(v: str):
    """Order versions numerically where possible ('6.38.04' > '6.4.2')."""
    return [int(p) if p.isdigit() else -1 for p in re.split(r"[._-]", v)]


def published(pkg: str, tag: str = "") -> dict:
    """{'version': str, 'matches_tag': bool, 'linux-64': bool, 'linux-aarch64': bool} or {}.

    Reports the version built from `tag` when anaconda.org has it, so a
    package whose newest tag is not its numerically highest version
    (named releases, older series re-tagged) is still matched; otherwise
    the newest published release.
    """
    url = f"https://api.anaconda.org/package/{ORG}/{pkg}"
    try:
        with urllib.request.urlopen(url, timeout=15) as resp:
            data = json.load(resp)
    except Exception:
        return {}
    files = data.get("files", [])
    versions = {f.get("version", "") for f in files}
    target = normalize(tag) if tag else None
    matching = [v for v in versions if target is not None and normalize(v) == target]
    if matching:
        latest = matching[0]
    else:
        # 'latest_version' can lag, and pre-policy '*.dev' uploads still
        # linger on the channel: ignore dev versions unless nothing else
        # exists, and order the rest numerically ourselves.
        releases = {v for v in versions if "dev" not in v} or versions
        latest = max(releases, key=version_key, default=data.get("latest_version", ""))
    state = {"version": latest, "matches_tag": bool(matching), **{s: False for s in ARCHES}}
    for f in files:
        if f.get("version") != latest:
            continue
        subdir = f.get("attrs", {}).get("subdir", "")
        for s in (ARCHES if subdir == "noarch" else [subdir]):
            if s in ARCHES:
                state[s] = True
    return state


def row(feedstock: Path) -> str:
    pkg = feedstock.name.replace("-feedstock", "")
    tag = latest_tag(feedstock) or "—"
    pub = published(pkg, "" if tag == "—" else tag)
    if not pub or not pub.get("version"):
        return f"| [{pkg}](https://github.com/{ORG}/{pkg}-feedstock) | `{tag}` | — | ❌ | ❌ |"
    marks = {s: ("✅" if pub[s] else "❌") for s in ARCHES}
    ver = pub["version"]
    ver_cell = f"`{ver}`" if pub["matches_tag"] else f"`{ver}` ⚠️"
    return (f"| [{pkg}](https://github.com/{ORG}/{pkg}-feedstock) | `{tag}` | "
            f"[{ver_cell}](https://anaconda.org/{ORG}/{pkg}) | "
            f"{marks['linux-64']} | {marks['linux-aarch64']} |")


def main() -> int:
    feedstocks = sorted(p for p in (ROOT / "feedstocks").glob("*-feedstock")
                        if (p / "recipe" / "meta.yaml").exists())
    with ThreadPoolExecutor(max_workers=8) as pool:
        rows = list(pool.map(row, feedstocks))

    table = "\n".join([
        f"_Last refreshed: {date.today().isoformat()} "
        f"(`python3 scripts/update_readme_status.py`)_",
        "",
        "| Feedstock | Latest tag | Published | amd64 | arm64 |",
        "|-----------|------------|-----------|-------|-------|",
        *rows,
        "",
        "⚠️ = the latest feedstock tag is not published on anaconda.org "
        "(build failed or still running); tag `X-y` publishes as `X.y`.",
    ])

    readme = ROOT / "README.md"
    text = readme.read_text()
    if BEGIN not in text or END not in text:
        print(f"Markers {BEGIN} / {END} not found in README.md", file=sys.stderr)
        return 1
    text = re.sub(
        re.escape(BEGIN) + r".*?" + re.escape(END),
        BEGIN + "\n" + table + "\n" + END,
        text, flags=re.DOTALL,
    )
    readme.write_text(text)
    print(f"Updated {readme} ({len(rows)} feedstocks)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
