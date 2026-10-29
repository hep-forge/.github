# Install from hep-forge
How users get the packages.

```bash
conda install -c hep-forge -c conda-forge <pkg>
conda install -c hep-forge -c conda-forge <pkg>=1.2.3      # a given version
conda install -c hep-forge -c conda-forge <pkg>=head       # build of upstream main
conda install -c hep-forge/label/legacy -c conda-forge <pkg>   # another label
```

Put `hep-forge` before `conda-forge`, so that hep-forge's builds win where both
channels have a package. linux-64 and linux-aarch64 are published; macOS is not.

What is published, and whether the latest tag made it, is in the status table on
[hep-forge/.github](https://github.com/hep-forge/.github#readme). The files of each
version are on [anaconda.org/hep-forge](https://anaconda.org/hep-forge).
