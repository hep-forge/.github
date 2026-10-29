# Automatic version updates
What hep-bot does by itself every day, and when it asks a human.

The [version check](https://github.com/hep-forge/.github/actions/workflows/hep-bot-check.yml)
runs daily over every registered feedstock:

- **New patch or minor release upstream**, with a plain tarball source: hep-bot adds it
  to the `versions` dict with a fresh sha256, commits to `main` and pushes the tag, so
  it builds and publishes.
- **Recipe ahead of its tags** (someone added a version but didn't tag): hep-bot pushes
  the tag.
- **`head`**: moved and rebuilt when upstream main/master has new commits.
- **Needs a human** (new major version, git source, unusual download URL): listed in the
  issue *[hep-bot] upstream updates that need a human* on hep-forge/.github. Upstream
  sites that block bots are listed there too.

Upstream versions come from the recipe's source URL. If that detection is wrong, add an
entry to [`sources.yaml`](https://github.com/hep-forge/.github/blob/main/scripts/hep_bot/sources.yaml).
To keep hep-bot away from a package, set `auto_update: false` in
[`dag.yaml`](https://github.com/hep-forge/.github/blob/main/scripts/hep_bot/dag.yaml).
