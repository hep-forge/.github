# Instructions for coding agents in hep-forge/.github

This repo (cloned locally as `hep-feedstocks`) is the hep-forge meta-repo. It holds every
feedstock as a submodule under `feedstocks/`, the files rendered into every feedstock
(`scripts/templates/`), the scripts behind the Makefile, and hep-bot (`scripts/hep_bot/`,
`.github/workflows/`). The README is the human overview, and this file covers what you need
to change things safely. Each feedstock also gets a short `AGENTS.md`, rendered from
`scripts/templates/AGENTS.md`.

## hep-forge is not conda-forge

- The CI of every feedstock is `scripts/templates/autoupload.yml`, copied in by the render.
  `conda smithy rerender` doesn't produce it, and you don't need it to fix CI. The
  conda-forge files a smithy rerender writes (`.ci_support/`, `.circleci/`, `.scripts/`,
  `conda-build.yml`) are unused here.
- CI runs a plain `conda build recipe` with channels `hep-forge`, `conda-forge`, `defaults`
  and strict priority. There is no conda-forge global pinning, so recipes pin their own
  compilers and the glibc floor (`c_stdlib_version: 2.17`) in `recipe/conda_build_config.yaml`.
- Builds only run on tags: numeric release tags (`[0-9]*`), and `head` for upstream
  main/master. Release tag `X-y` publishes as `X.y`. A branch is an anaconda label
  (`main`, `legacy`, `eic`, ...). The upload keeps the newest 2 versions per label, plus
  `extra.lts`, the `keep` label and `head`.
- Linux 64 and aarch64 are published. macos-arm64 is compiled but not published. If a
  package can't build on macOS, use `skip: true  # [not linux]`. Nobody here can set
  Actions variables (`ANACONDA_COMPILE` / `ANACONDA_PUBLISH`) with the tokens that exist.

## Creating a feedstock

Preferred: `@hep-bot new <pkg> <upstream-url> [license=<spdx>] [maintainers=a,b] [summary]`
in an issue on hep-forge/.github, or the *New feedstock* issue form. Locally:

```bash
make new-feedstock NAME=<pkg> REPO=<upstream-url> SUMMARY="..." LICENSE=<spdx> MAINTAINERS=a,b
git commit -m "Register <pkg>-feedstock" .gitmodules feedstocks/<pkg>-feedstock && git push
```

`scripts/new_feedstock.sh` copies boilerplate from `feedstocks/inih-feedstock`, writes a
starter recipe and the rendered files (workflows, CODEOWNERS, README, AGENTS.md), and
creates the GitHub repo (or fills an empty one that already exists). Then it adds the
submodule. The starter recipe doesn't build yet. Fill in the version, sha256, dependencies,
`build.sh` and a real test.

If the feedstock repo already exists with commits (made by hand or by an agent), don't
scaffold it again. Register and render it with `@hep-bot rerender <pkg>`, or locally:

```bash
bash scripts/register_feedstock.sh <pkg> --commit
bash scripts/render_sync.sh --commit --only <pkg>
```

A feedstock that isn't a submodule here is invisible to render-sync, the status table, the
version check and every Makefile target.

## Traps

- Feedstock `.gitignore` files start with `*`. New files outside `recipe/` need `git add -f`,
  or they are silently left out. This is the usual reason a hand-made feedstock "didn't
  render".
- Don't edit rendered files in a feedstock (`autoupload.yml`, `hep-bot-comment.yml`,
  `README.md`, `AGENTS.md`). Edit the template or generator here. render-sync pushes the
  result to every feedstock, which is a fleet-wide change.
- `README.md` is a symlink to `profile/README.md`, which is also the org profile page.
  Stage `profile/README.md`, use absolute `https://github.com/hep-forge/.github/blob/main/...`
  links (relative links break on the org page), and never edit between the
  `status:begin`/`status:end` markers. `scripts/update_readme_status.py` owns that block.
- conda-build filters the environment, so variables set in CI don't reach `build.sh`.
- conda's `CMAKE_ARGS` sets `CMAKE_FIND_ROOT_PATH_MODE_INCLUDE=ONLY`, which hides headers in
  the source tree.
- `workflow_dispatch` reads the workflow file at the dispatched tag. An old tag that predates
  the current template can't be dispatched; move it with `make retag <pkg>`.
- `HEP_BOT_TOKEN` is meant to be an org secret. Where a workflow doesn't get it, it falls
  back to `GITHUB_TOKEN`, which can't push to or dispatch in other repos; the sweep
  then handles the request from here.
- CI submodule checkouts are `--depth 1` at the pinned commit. Scripts that change a
  feedstock first move it to its default-branch tip (see `scripts/render_sync.sh`).

## hep-bot

| Piece | Where |
|---|---|
| Issue commands (`rerun`, `rerender`, `new`, `help [<topic>]`) | `scripts/hep_bot/comment.py` (guides it quotes: `scripts/hep_bot/guide/*.md`), run by `hep-bot-comment.yml` in every feedstock and by `hep-bot-sweep.yml` (every 10 min, org-wide) here |
| Version check (bump + tag, `head` rebuilds, tracking issue) | `scripts/hep_bot/check_versions.py`, `bump_version.py`, `.github/workflows/hep-bot-check.yml` |
| Upstream overrides, dependency order, opt-out | `scripts/hep_bot/sources.yaml`, `scripts/hep_bot/dag.yaml` (`auto_update: false`) |
| Render of one or all feedstocks | `scripts/render_sync.sh`, `.github/workflows/render-sync.yml` |
| New feedstock | `scripts/new_feedstock.sh`, `.github/workflows/new-feedstock.yml` |

Before you trigger anything that pushes, run the dry runs:
`python3 scripts/hep_bot/check_versions.py --dry-run [--only pkg]` and
`bash scripts/render_sync.sh` without `--commit`.

## GitHub releases

A release exists only to host a file the recipe downloads, such as a mirror of the
upstream tarball. Its title is the tag and nothing else (`1.3.1_4`, not a description),
and it has no notes: people read the upstream changelog. Create it with
`gh release create <tag> <file> --title <tag> --notes ""`.

## Commits

No `Co-authored-by` or other AI attribution trailers in commits or PRs, here or in any
feedstock.
