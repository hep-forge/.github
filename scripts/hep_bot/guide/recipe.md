# Write the recipe
What `recipe/` needs so that CI builds it, and the mistakes everyone makes once.

Everything you edit lives in `recipe/`: `meta.yaml`, `build.sh`,
`conda_build_config.yaml`, patches, test scripts. The other files are rendered and get
overwritten.

- **Versions.** The top of `meta.yaml` has a `versions` dict, version → sha256 of the
  source tarball, **newest first**. A release tag must be one of its keys. Get the
  hash with `curl -sL <url> | sha256sum`. Keep the header lines that read
  `COMMIT_VERSION`, `ANACONDA_PACKAGE` and `ANACONDA_VERSION`: CI sets them.
- **Compilers and glibc.** There is no conda-forge global pinning. The recipe pins its
  own compilers and the glibc 2.17 floor in `recipe/conda_build_config.yaml`
  (`c_stdlib_version: 2.17`); copy it from an existing feedstock such as
  [inih](https://github.com/hep-forge/inih-feedstock/tree/main/recipe).
- **Dependencies.** Channels are `hep-forge`, `conda-forge`, `defaults` with strict
  priority, so a hep-forge package wins over the conda-forge one of the same name.
- **`build.sh`.** CI variables don't reach it (conda-build filters the environment):
  export what the build needs there, e.g. `export CMAKE_POLICY_VERSION_MINIMUM=3.5`.
  conda's `CMAKE_ARGS` hides headers that sit in the source tree; pass their include
  directory explicitly.
- **Libraries** need `run_exports` (`pin_subpackage(name, max_pin="x.x")`) so that
  packages built against them pin a compatible version.
- **Test** the installed package for real: run the binary, import the module, compile a
  two-line program against the headers. `echo ok` is not a test.
- **macOS.** A macos-arm64 build runs but is never published. If the package can't build
  there, add `skip: true  # [not linux]` under `build:`.
- **New files outside `recipe/`.** The feedstock's `.gitignore` starts with `*`, so use
  `git add -f`, or the file silently stays out of the commit.
- Don't run `conda smithy rerender`. hep-forge doesn't use the files it writes.

Try it locally before tagging: `conda build recipe -c hep-forge -c conda-forge`.
Coding agents: point them at the feedstock's `AGENTS.md` first.
