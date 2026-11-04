#!/usr/bin/env python3
"""Inventory and trim the hep-forge anaconda.org channel.

List every published package broken down by architecture (linux-64,
linux-aarch64, noarch, ...), and optionally remove excess versions --
old releases or stray *dev* uploads -- via anaconda-client.

Usage:
  python3 scripts/channel_packages.py                     # overview table
  python3 scripts/channel_packages.py --files pythia      # per-file listing
  python3 scripts/channel_packages.py --sizes             # total bytes per package (TSV)
  python3 scripts/channel_packages.py --trim pythia --keep 3
  python3 scripts/channel_packages.py --trim root --keep-versions 6.32.16,6.38.04
  python3 scripts/channel_packages.py --purge-dev         # drop *dev* versions
  python3 scripts/channel_packages.py --purge-dev --yes   # ... for real
  python3 scripts/channel_packages.py --retire-root-slots # builds of ROOT slots not in channel.yaml

Trim/purge are DRY-RUN unless --yes is given. Removal shells out to
`anaconda remove` and therefore needs anaconda-client logged in or
ANACONDA_API_TOKEN exported.
"""
import argparse
import concurrent.futures
import json
import os
import re
import subprocess
import sys
import urllib.request
from collections import defaultdict

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
API = "https://api.anaconda.org"
ORG = "hep-forge"


def fetch(path: str):
    with urllib.request.urlopen(f"{API}{path}", timeout=30) as resp:
        return json.load(resp)


def channel_packages(org: str):
    return fetch(f"/packages/{org}")


def package_files(org: str, pkg: str):
    return fetch(f"/package/{org}/{pkg}").get("files", [])


def version_key(version: str):
    # sortable-enough: numeric fields compared numerically, rest as text
    return [int(p) if p.isdigit() else p for p in version.replace("-", ".").split(".")]


def human_size(n: float) -> str:
    for unit in ("B", "KB", "MB"):
        if n < 1024:
            return f"{n:.0f}{unit}" if unit == "B" else f"{n:.1f}{unit}"
        n /= 1024
    return f"{n:.1f}GB"


def sizes(org: str):
    """One TSV line per package: name, total bytes, human size, per-label
    published-version counts (e.g. "main:2,old:5") -- everything
    `feedstock_status.sh` needs for its SIZE/LABELS columns, fetched
    concurrently since it's one anaconda.org call per package."""
    pkgs = [p["name"] for p in channel_packages(org)]

    def one(pkg):
        files = package_files(org, pkg)
        total = sum(f.get("size") or 0 for f in files)
        by_label = defaultdict(set)
        for f in files:
            for label in f.get("labels") or ["main"]:
                by_label[label].add(f.get("version", ""))
        labels = ",".join(f"{l}:{len(vs)}" for l, vs in sorted(by_label.items()))
        return pkg, total, labels

    results = {}
    with concurrent.futures.ThreadPoolExecutor(max_workers=16) as ex:
        for fut in concurrent.futures.as_completed(ex.submit(one, pkg) for pkg in pkgs):
            try:
                pkg, total, labels = fut.result()
                results[pkg] = (total, labels)
            except Exception:
                continue

    print("# package\tsize_bytes\tsize_human\tlabels(name:n_versions)")
    for pkg in sorted(results):
        total, labels = results[pkg]
        print(f"{pkg}\t{total}\t{human_size(total)}\t{labels}")


def overview(org: str):
    pkgs = channel_packages(org)
    arches = sorted({p2 for p in pkgs for p2 in (p.get("platforms") or ["?"])})
    header = f"{'PACKAGE':<24} {'LATEST':<14} {'#VER':>4}  " + "  ".join(f"{a:<13}" for a in arches)
    print(header)
    print("-" * len(header))
    for p in sorted(pkgs, key=lambda p: p["name"]):
        name = p["name"]
        versions = p.get("versions", [])
        platforms = set(p.get("platforms") or [])
        cells = "  ".join(f"{'yes' if a in platforms else '-':<13}" for a in arches)
        print(f"{name:<24} {p.get('latest_version', ''):<14} {len(versions):>4}  {cells}")


def files_listing(org: str, pkg: str):
    files = package_files(org, pkg)
    print(f"{'VERSION':<16} {'ARCH':<14} {'LABELS':<12} {'SIZE':>9}  BASENAME")
    print("-" * 90)
    for f in sorted(files, key=lambda f: (version_key(f.get('version', '')), f.get('attrs', {}).get('subdir', ''))):
        subdir = f.get("attrs", {}).get("subdir", "?")
        labels = ",".join(f.get("labels", []))
        print(f"{f.get('version', ''):<16} {subdir:<14} {labels:<12} {human_size(f.get('size') or 0):>9}  {f.get('basename', '')}")


def remove_spec(org: str, spec: str, yes: bool):
    cmd = ["anaconda"]
    token = os.environ.get("ANACONDA_API_TOKEN")
    if token:
        cmd += ["-t", token]
    cmd += ["remove", "--force", spec]
    if yes:
        print(f"REMOVING {spec}")
        subprocess.run(cmd, check=False)
    else:
        print(f"[dry-run] would remove {spec}   (rerun with --yes)")


def pinned_by(pkg: str):
    """Every feedstock that pins a specific version-line of `pkg` via its
    own conda_build_config.yaml (e.g. root: 6.34) -- dropping a version
    matching one of these breaks that feedstock's next build, and any
    already-published package of theirs that depends on the exact
    version removed. This is the live version of what used to be a
    hand-maintained comment in root-feedstock's meta.yaml (which had
    already gone stale); see also `make doctor <pkg>`."""
    import glob
    import re as _re
    from pathlib import Path

    import yaml

    def strip_jinja(text):
        text = _re.sub(r"\{%.*?%\}", "", text, flags=_re.DOTALL)
        text = _re.sub(r"\{#.*?#\}", "", text, flags=_re.DOTALL)  # Jinja comments
        text = _re.sub(r"\{\{.*?\}\}", "JINJA", text)
        return text

    result = defaultdict(list)  # version-line (str) -> [dependent_pkg, ...]
    for f in sorted(glob.glob("feedstocks/*-feedstock/recipe/conda_build_config.yaml")):
        dep_pkg = Path(f).parent.parent.name[: -len("-feedstock")]
        if dep_pkg == pkg:
            continue
        try:
            cbc = yaml.safe_load(strip_jinja(Path(f).read_text())) or {}
        except (OSError, yaml.YAMLError):
            continue
        variants = cbc.get(pkg)
        if isinstance(variants, list):
            for rv in variants:
                result[str(rv)].append(dep_pkg)
    return result


def trim(org: str, pkg: str, keep: int, yes: bool, keep_versions=None):
    files = package_files(org, pkg)
    versions = sorted({f.get("version", "") for f in files}, key=version_key, reverse=True)
    if keep_versions:
        keep_set = set(keep_versions)
        unknown = keep_set - set(versions)
        if unknown:
            print(f"{pkg}: WARNING -- --keep-versions has version(s) not published: {sorted(unknown)}")
    else:
        keep_set = set(versions[:keep])
    drop = [v for v in versions if v not in keep_set]
    if not drop:
        print(f"{pkg}: {len(versions)} version(s), nothing to trim (keeping {sorted(keep_set, key=version_key, reverse=True)})")
        return

    pins = pinned_by(pkg)
    blocked = [(v, line, deps) for v in drop for line, deps in pins.items() if v.startswith(line)]
    if blocked:
        print(f"{pkg}: REFUSING to drop version(s) still pinned by other feedstocks' conda_build_config.yaml:")
        for v, line, deps in blocked:
            print(f"  {v}  (matches {pkg}: {line})  <- pinned by {', '.join(deps)}")
        blocked_versions = {v for v, _, _ in blocked}
        drop = [v for v in drop if v not in blocked_versions]
        if not drop:
            print(f"{pkg}: nothing left to drop once pinned versions are excluded.")
            return
        print(f"{pkg}: proceeding with the remaining safe drop(s) only: {drop}")

    print(f"{pkg}: keeping {sorted(keep_set, key=version_key, reverse=True)}, dropping {drop}")
    for v in drop:
        remove_spec(org, f"{org}/{pkg}/{v}", yes)


def purge_dev(org: str, yes: bool):
    for p in sorted(channel_packages(org), key=lambda p: p["name"]):
        for v in p.get("versions", []):
            if "dev" in v:
                remove_spec(org, f"{org}/{p['name']}/{v}", yes)


def root_slots():
    """The ROOT minors channel.yaml keeps, e.g. {"6.38", "6.40"}."""
    import yaml
    with open(os.path.join(REPO, "channel.yaml")) as f:
        return {str(s) for s in (yaml.safe_load(f) or {}).get("root_slots", [])}


def root_slot(pkg: str, f: dict):
    """The ROOT minor a file belongs to: ROOT's own version, or the root6xx
    build string / root 6.xx.* dependency of a ROOT-dependent build."""
    if pkg == "root":
        m = re.match(r"(\d+)\.(\d+)\.", f.get("version", ""))
        return f"{m.group(1)}.{m.group(2)}" if m else None
    m = re.search(r"(?:^|_)root(\d)(\d\d)(?:_|$)", f.get("attrs", {}).get("build", ""))
    if m:
        return f"{m.group(1)}.{m.group(2)}"
    for dep in f.get("attrs", {}).get("depends", []) or []:
        m = re.match(r"root (\d+)\.(\d+)\.\*", dep)
        if m:
            return f"{m.group(1)}.{m.group(2)}"
    return None


def recipe_root_variants():
    """Feedstocks whose conda_build_config.yaml still builds a ROOT slot."""
    out = {}
    base = os.path.join(REPO, "feedstocks")
    for d in sorted(os.listdir(base)) if os.path.isdir(base) else []:
        path = os.path.join(base, d, "recipe", "conda_build_config.yaml")
        if not os.path.exists(path):
            continue
        m = re.search(r"^root:\s*\n((?:\s+-.*\n|\s*#.*\n)+)", open(path).read(), re.M)
        if m:
            vals = re.findall(r"^\s+-\s*['\"]?(\d+\.\d+)", m.group(1), re.M)
            if vals:
                out[d[: -len("-feedstock")]] = set(vals)
    return out


def retire_root_slots(org: str, yes: bool):
    keep = root_slots()
    print(f"ROOT slots kept (channel.yaml): {', '.join(sorted(keep))}")
    for pkg, vals in recipe_root_variants().items():
        if vals - keep:
            print(f"WARNING: {pkg} still builds ROOT {', '.join(sorted(vals - keep))}; "
                  f"drop it from recipe/conda_build_config.yaml")
    names = [p["name"] for p in channel_packages(org)]
    with concurrent.futures.ThreadPoolExecutor(8) as pool:
        files = dict(zip(names, pool.map(lambda n: package_files(org, n), names)))
    total, count = 0, 0
    for pkg in sorted(files):
        for f in sorted(files[pkg], key=lambda f: f.get("basename", "")):
            slot = root_slot(pkg, f)
            if slot is None or slot in keep:
                continue
            total += f.get("size") or 0
            count += 1
            print(f"  ROOT {slot}  {human_size(f.get('size') or 0):>9}  ", end="")
            remove_spec(org, f"{org}/{pkg}/{f['version']}/{f['basename']}", yes)
    print(f"{count} files, {human_size(total)} in ROOT slots outside channel.yaml"
          + ("" if yes else " (dry run: nothing removed)"))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--files", metavar="PKG", help="list every file of one package")
    ap.add_argument("--sizes", action="store_true", help="TSV: total size + per-label version counts, all packages")
    ap.add_argument("--trim", metavar="PKG", help="remove old versions of one package")
    ap.add_argument("--keep", type=int, default=3, help="versions to keep with --trim (default 3, keeps the N latest)")
    ap.add_argument("--keep-versions", metavar="V1,V2,...", help="with --trim: keep exactly these versions (overrides --keep), for non-contiguous keeps")
    ap.add_argument("--purge-dev", action="store_true", help="remove every *dev* version channel-wide")
    ap.add_argument("--retire-root-slots", action="store_true",
                    help="remove builds of ROOT slots not listed in channel.yaml (ROOT itself and root6xx builds)")
    ap.add_argument("--yes", action="store_true", help="actually delete (default: dry-run)")
    ap.add_argument("--org", default=ORG)
    args = ap.parse_args()

    if args.files:
        files_listing(args.org, args.files)
    elif args.sizes:
        sizes(args.org)
    elif args.trim:
        keep_versions = args.keep_versions.split(",") if args.keep_versions else None
        trim(args.org, args.trim, args.keep, args.yes, keep_versions)
    elif args.purge_dev:
        purge_dev(args.org, args.yes)
    elif args.retire_root_slots:
        retire_root_slots(args.org, args.yes)
    else:
        overview(args.org)


if __name__ == "__main__":
    sys.exit(main())
