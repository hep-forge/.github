## Hi there 👋

This forge implements `autoupload.yml/autodelete.yml` CI/CD automation for `linux-64` only.

Any contribution implementing specific self-hosted runners in HEP Forge, using any external CI as natural improvement for CI/CD, would be very welcome.

## HEP Forge Channel

Packages are available and listed in https://anaconda.org/hep-forge/
You can also sort by version pre-compiled and install the one you prefer.

## Conda minimal installation

Please refer to this page to learn how to install conda.
https://docs.anaconda.com/miniconda/install/#quick-command-line-install

Many flavors of conda are available: `anaconda`, `miniconda`, `conda`, `mamba`.
We recommend `miniconda` or `mamba`.

## Examples

You can create a conda environment by executing the following lines
```
conda create -n myenv # change `myenv` as you wish
conda activate myenv # enable the environment
conda -c hep-forge -c conda-forge cernlib root lhapdf # As an example you can install cernlib, root, lhapdf in a second.
```

Additionally, you can also provide a one line command, such as
```
conda create -n myenv -c hep-forge -c conda-forge cernlib root lhapdf 
conda activate myenv
```

You can switch between environment by activating another environment you created or deactivate it as follows:
```
conda deactivate
```
