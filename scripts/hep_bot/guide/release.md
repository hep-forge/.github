# Publish a version
Only a tag builds. How tags, labels and old versions work.

- **A tag publishes, nothing else does.** Pushing a numeric tag runs the build on
  linux-64 and linux-aarch64 and uploads to anaconda.org/hep-forge. Merging a PR or
  pushing to `main` publishes nothing.

  ```bash
  git tag 1.2.3 && git push origin 1.2.3
  ```

  The tag is the version and must be a key of the `versions` dict in `meta.yaml`. Tag
  `X-y` publishes as `X.y`.
- **Fix a recipe without a new upstream version:** merge the fix, then move the tag so
  it points at the fixed recipe:

  ```bash
  git tag -f 1.2.3 && git push -f origin refs/tags/1.2.3
  ```

  `@hep-bot rerun 1.2.3` would rebuild the recipe *as it was at the tag*, without your
  fix (`@hep-bot help rerun`).
- **`head` follows upstream main/master.** Create a `head` tag once; hep-bot moves it
  and rebuilds whenever upstream gets a new commit or the recipe changes. It publishes
  as version `head`, which conda ranks below every release, so nobody gets it by
  accident.
- **Branches are labels.** Tags made on `main` publish to the `main` label; a `legacy`
  branch publishes to `legacy`. Put a second version line on its own branch and tag
  there.
- **Old versions.** Each label keeps its newest 2 versions. List versions that must stay
  in `extra.lts` in the recipe.

Follow a build under the feedstock's **Actions** tab (workflow *autoupload*).
