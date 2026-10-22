#!/usr/bin/env bash
# Register an existing hep-forge/<name>-feedstock GitHub repo as the
# submodule feedstocks/<name>-feedstock of this meta-repo, so render-sync,
# the README status table and the Makefile targets see it. A feedstock made
# by hand (or by an agent) instead of scripts/new_feedstock.sh starts out
# unregistered, and render-sync never touches it until this runs.
#
# Idempotent: an already registered feedstock is left alone.
# Stages .gitmodules + the gitlink; --commit also commits (not pushes).
#
# Usage:
#   bash scripts/register_feedstock.sh nestdaq [--commit]

set -euo pipefail
cd "$(dirname "$0")/.."

NAME="${1:?usage: register_feedstock.sh <name> [--commit]}"
NAME="${NAME%-feedstock}"
COMMIT=0
[ "${2:-}" = "--commit" ] && COMMIT=1

FS="feedstocks/${NAME}-feedstock"
URL="git@github.com:hep-forge/${NAME}-feedstock.git"

if git config -f .gitmodules --get "submodule.${FS}.path" >/dev/null 2>&1; then
  echo "$FS already registered"
  exit 0
fi

if ! git ls-remote --exit-code "https://github.com/hep-forge/${NAME}-feedstock.git" HEAD >/dev/null 2>&1; then
  echo "ERROR: hep-forge/${NAME}-feedstock does not exist or is empty -- use scripts/new_feedstock.sh" >&2
  exit 1
fi

git submodule add "$URL" "$FS"
[ -f "$FS/recipe/meta.yaml" ] || echo "WARNING: $FS has no recipe/meta.yaml yet; render-sync skips it until it does" >&2

if [ "$COMMIT" -eq 1 ]; then
  git commit -qm "Register ${NAME}-feedstock" -- .gitmodules "$FS"
  echo "Committed registration of $FS"
fi
