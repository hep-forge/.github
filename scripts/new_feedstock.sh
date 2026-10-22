#!/usr/bin/env bash
# Scaffold a brand-new hep-forge feedstock: creates feedstocks/<name>-feedstock
# locally with a starter recipe, the boilerplate every feedstock carries
# (conda-forge.yml, LICENSE.txt, build-locally.py, .ci_support, .circleci --
# all generic and untouched by conda-smithy's actual build path here, see
# scripts/templates/autoupload.yml, so they're copied verbatim from an
# existing small feedstock rather than regenerated), the hep-forge CI
# workflow + hep-bot comment workflow + AGENTS.md, then creates the GitHub
# repo (or fills a pre-created empty one), pushes, and registers it as a
# submodule in this meta-repo. Run locally or by the new-feedstock
# workflow (`@hep-bot new <name> <upstream-url>`).
#
# The generated recipe/meta.yaml + build.sh are STARTERS, not working
# recipes -- fill in the real version/sha256/dependencies/build steps
# by hand afterward, same as every other feedstock.
#
# Usage:
#   bash scripts/new_feedstock.sh NAME=cnpy REPO=https://github.com/rogersce/cnpy \
#        SUMMARY="numpy-file I/O for C++" LICENSE=MIT MAINTAINERS=meiyasan,someone
#
# Required: NAME, REPO. Optional: SUMMARY (default "TODO"), LICENSE (default TODO),
# MAINTAINERS (comma list of GitHub logins, default meiyasan; first one owns
# .github/CODEOWNERS together with meiyasan).
# Reference skeleton is copied from feedstocks/inih-feedstock (smallest existing one).

set -euo pipefail

NAME=""
REPO=""
SUMMARY="TODO: one-line summary"
LICENSE="TODO"
MAINTAINERS="meiyasan"

for arg in "$@"; do
  case "$arg" in
    NAME=*)    NAME="${arg#NAME=}" ;;
    REPO=*)    REPO="${arg#REPO=}" ;;
    SUMMARY=*) SUMMARY="${arg#SUMMARY=}" ;;
    LICENSE=*) LICENSE="${arg#LICENSE=}" ;;
    MAINTAINERS=*) MAINTAINERS="${arg#MAINTAINERS=}" ;;
    *) echo "Unknown argument: $arg" >&2; exit 1 ;;
  esac
done

if [ -z "$NAME" ] || [ -z "$REPO" ]; then
  echo "Usage: bash scripts/new_feedstock.sh NAME=<pkg> REPO=<upstream-url> [SUMMARY=\"...\"] [LICENSE=<spdx>]" >&2
  exit 1
fi
[ -z "$SUMMARY" ] && SUMMARY="TODO: one-line summary"
[ -z "$LICENSE" ] && LICENSE="TODO"
[ -z "$MAINTAINERS" ] && MAINTAINERS="meiyasan"
MAINTAINERS="${MAINTAINERS//@/}"
MAINTAINERS="${MAINTAINERS// /}"

cd "$(dirname "$0")/.."

# An org admin may have created hep-forge/<name>-feedstock already (empty,
# no README/license): fill it instead of failing at `gh repo create`. A
# non-empty one is a feedstock someone already started -- register it
# (scripts/register_feedstock.sh) rather than overwrite it.
REMOTE_EXISTS=0
if gh repo view "hep-forge/${NAME}-feedstock" >/dev/null 2>&1; then
  if git ls-remote --exit-code "https://github.com/hep-forge/${NAME}-feedstock.git" HEAD >/dev/null 2>&1; then
    echo "ERROR: hep-forge/${NAME}-feedstock already has commits -- use scripts/register_feedstock.sh ${NAME}" >&2
    exit 1
  fi
  REMOTE_EXISTS=1
fi

FS="feedstocks/${NAME}-feedstock"
REF="feedstocks/inih-feedstock"   # generic-boilerplate donor, no package-specific content

if [ -e "$FS" ]; then
  echo "ERROR: $FS already exists" >&2
  exit 1
fi
if [ ! -d "$REF" ]; then
  echo "ERROR: reference skeleton $REF not found" >&2
  exit 1
fi

echo "=== Scaffolding $FS ==="
mkdir -p "$FS/recipe" "$FS/.github/workflows"

# --- generic boilerplate, copied verbatim (no package-specific content in these) ---
cp "$REF/conda-forge.yml"       "$FS/conda-forge.yml"
cp "$REF/LICENSE.txt"           "$FS/LICENSE.txt"
cp "$REF/build-locally.py"      "$FS/build-locally.py"
cp "$REF/Makefile"              "$FS/Makefile"
cp -r "$REF/.ci_support"        "$FS/.ci_support"
cp -r "$REF/.circleci"          "$FS/.circleci"
cp scripts/templates/autoupload.yml "$FS/.github/workflows/autoupload.yml"
cp scripts/templates/hep-bot-comment.yml "$FS/.github/workflows/hep-bot-comment.yml"
cp scripts/templates/AGENTS.md "$FS/AGENTS.md"
OWNERS="@meiyasan"
first="${MAINTAINERS%%,*}"
[ "$first" != "meiyasan" ] && OWNERS="@${first} ${OWNERS}"
echo "* ${OWNERS}" > "$FS/.github/CODEOWNERS"

cat > "$FS/.gitignore" <<'EOF'
!Makefile
!.github
EOF

# --- starter recipe (generic CMake skeleton; edit source/build/requirements per package) ---
cat > "$FS/recipe/meta.yaml" <<EOF
{% set versions = {
    "0.0.0": "REPLACE_WITH_SHA256"
} %}

{% set version = environ.get('COMMIT_VERSION', None) %}
{% set version = version or versions.keys()|first %}
{% set version = version|string %}

{% set name = environ.get('ANACONDA_PACKAGE', '${NAME}')|string|lower %}

package:
  name: {{ name }}
  version: {{ environ.get('ANACONDA_VERSION', version)|replace("-", ".") }}

source:
  url: "${REPO}/archive/refs/tags/{{ version }}.tar.gz"   # TODO: confirm upstream's actual tag/tarball naming
  {% if versions.get(version, None) %}
  sha256: {{ versions.get(version) }}
  {% endif %}

build:
  number: 0
  run_exports:
    - {{ pin_subpackage(name, max_pin="x.x.x") }}

requirements:
  build:
    - {{ compiler('c') }}
    - {{ compiler('cxx') }}
    - {{ stdlib('c') }}
    - cmake
    - make
  host:
    # TODO: library dependencies
  run:
    # TODO: runtime dependencies

test:
  commands:
    - echo "TODO: a real smoke test"

about:
  home: "${REPO}"
  license: "${LICENSE}"
  summary: "${SUMMARY}"

extra:
  recipe-maintainers:
$(echo "$MAINTAINERS" | tr ',' '\n' | sed '/^$/d;s/^/    - /')
EOF

cat > "$FS/recipe/build.sh" <<'EOF'
#! /usr/bin/bash
set -e

mkdir -p build
cd build

cmake .. \
  -DCMAKE_INSTALL_PREFIX="${PREFIX}" \
  -DCMAKE_BUILD_TYPE=Release

NPROC=$(nproc 2>/dev/null || sysctl -n hw.ncpu)
make -j"$NPROC"
make install
EOF

cat > "$FS/recipe/conda_build_config.yaml" <<'EOF'
c_stdlib:
  - sysroot                    # [linux]
  - macosx_deployment_target   # [osx]

c_stdlib_version:
  - 2.17  # [linux]
  - 11.0  # [osx]

c_compiler:
  - gcc
cxx_compiler:
  - gxx
EOF

# Same README every render produces (badges, install line, maintainers).
python3 scripts/generate_readme.py "$FS" hep-forge

# --- init, commit, create + push the GitHub repo ---
(
  cd "$FS"
  git init -q -b main
  git add -A
  git commit -q -m "Initial scaffold for ${NAME}-feedstock" \
    -m "Generated by scripts/new_feedstock.sh -- recipe is a starter, not yet a working build."
)

if [ "$REMOTE_EXISTS" -eq 1 ]; then
  echo "=== Pushing to the existing empty hep-forge/${NAME}-feedstock ==="
  (cd "$FS" && git remote add origin "https://github.com/hep-forge/${NAME}-feedstock.git" && git push -q -u origin main)
else
  echo "=== Creating hep-forge/${NAME}-feedstock on GitHub ==="
  gh repo create "hep-forge/${NAME}-feedstock" --public --source="$FS" --remote=origin --push \
    --description "${SUMMARY}"
fi

# gh defaults to an https remote regardless of the org's actual git_protocol
# setting; every other feedstock submodule here uses ssh, so match that
# (also needed for pushing without re-auth later).
(cd "$FS" && git remote set-url origin "git@github.com:hep-forge/${NAME}-feedstock.git")

# --- register as a submodule in this meta-repo ---
git submodule add "git@github.com:hep-forge/${NAME}-feedstock.git" "$FS"

echo ""
echo "=== Done: $FS ==="
echo "Next: edit $FS/recipe/{meta.yaml,build.sh} with the real version/deps/build steps"
echo "(a PR on the feedstock repo is fine), then push a numeric release tag on main"
echo "-- the tag push builds and publishes. Commit .gitmodules + $FS here."
