# Package new software
From "is it a fit for hep-forge?" to the first published build.

**1. Check that it belongs here.** hep-forge carries compiled HEP software (C++,
Fortran, mixed Python/C++). A package written entirely in Python is already
installable with pip, and generic non-HEP libraries belong on conda-forge. Also check
that the name isn't taken by an unrelated project on PyPI or conda-forge.

**2. Ask hep-bot for the feedstock**, in an issue on
[hep-forge/.github](https://github.com/hep-forge/.github/issues/new/choose):

```
@hep-bot new <pkg> <upstream-url> license=<spdx> maintainers=<you>,<colleague> One-line summary
```

or use the *New feedstock* issue form, which asks for the same fields. hep-bot creates
`hep-forge/<pkg>-feedstock` with a starter recipe, the CI and bot workflows, a README,
CODEOWNERS and `AGENTS.md`, registers it in hep-forge/.github, and replies with the link.
Only `<pkg>` and the URL are required; `maintainers` defaults to you.

**3. Write the recipe** in a PR on the new feedstock. The starter recipe doesn't build
yet. See `@hep-bot help recipe`.

**4. Merge, then push the version tag on `main`:**

```bash
git tag 1.2.3 && git push origin 1.2.3
```

The tag push builds linux-64 and linux-aarch64 and uploads to
[anaconda.org/hep-forge](https://anaconda.org/hep-forge). Merging alone publishes
nothing. See `@hep-bot help release`.

From then on the daily version check keeps the package on the latest upstream release
(`@hep-bot help updates`).

**The repo already exists?** If someone created `<pkg>-feedstock` by hand and it has a
recipe, don't run `new`: `@hep-bot rerender <pkg>` registers it and adds the hep-forge
files (`@hep-bot help rerender`).
