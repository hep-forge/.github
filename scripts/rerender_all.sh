#!/usr/bin/env bash
# Regenerate README.md for every feedstock, pointed at hep-forge, and
# sync the CI workflow from scripts/templates/autoupload.yml (the
# workflow is part of the render: README badges and the workflow must
# agree on names/behavior), plus the hep-bot comment workflow and the
# AGENTS.md that tells coding agents working inside a feedstock where the
# hep-forge rules live.
# Usage: bash scripts/rerender_all.sh [org] [package]
set -e
ORG="${1:-hep-forge}"
ONLY="${2:-}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPT="$ROOT/scripts/generate_readme.py"
TEMPLATE="$ROOT/scripts/templates/autoupload.yml"
COMMENT_TEMPLATE="$ROOT/scripts/templates/hep-bot-comment.yml"
AGENTS_TEMPLATE="$ROOT/scripts/templates/AGENTS.md"

cd "$ROOT"

for dir in feedstocks/*-feedstock; do
    [ -f "$dir/recipe/meta.yaml" ] || continue
    [ -n "$ONLY" ] && [ "$dir" != "feedstocks/${ONLY%-feedstock}-feedstock" ] && continue
    echo "=== $dir ==="
    mkdir -p "$dir/.github/workflows"
    cp "$TEMPLATE" "$dir/.github/workflows/autoupload.yml"
    echo "Synced .github/workflows/autoupload.yml"
    cp "$COMMENT_TEMPLATE" "$dir/.github/workflows/hep-bot-comment.yml"
    echo "Synced .github/workflows/hep-bot-comment.yml"
    cp "$AGENTS_TEMPLATE" "$dir/AGENTS.md"
    echo "Synced AGENTS.md"
    python3 "$SCRIPT" "$dir" "$ORG"
done
