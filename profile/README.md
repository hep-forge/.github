## Hi there 👋

This forge implements `autoupload.yml/autodelete.yml` CI/CD automation for `linux` operating system.
It supports both AMD64 (x86) and ARM64 (aarch64) architectures

Any contribution implementing specific self-hosted runners in this HEP-Forge, using any external CI as natural improvement for CI/CD, would be very welcome too.
If you are looking for a more generic approach including macOS and window, please refer to `conda-forge` website

## HEP Forge Channel

This is a distribution channel implementing many HEP scientific models and packages including some specific requirements.

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
conda create -n myhep # change `myenv` as you wish
conda activate myhep # enable the environment
conda -c hep-forge -c conda-forge cernlib root lhapdf # As an example you can install cernlib, root, lhapdf in a second.
```

You can also provide a one line command, such as
```
conda create -n myhep -c hep-forge -c conda-forge cernlib root lhapdf 
conda activate myhep
```

You can switch between environment by activating another environment you created or deactivate it as follows:
```
conda deactivate
```

Additionally, you can share you environment by providing a minimal `environment.yml` file to people, such as:
```
# environment.yml
name: myhep
channels:
  - hep-forge
  - conda-forge
```

Environment file can be shared using:
```
conda create -n myhep -f environment.yml
```

## How to add new software into the HEP channel ?

Please start a discussion on github to reach us and contribute. Current configuration is limited to `linux-64` platform, but it is compatible with `conda-smithy`.
Also, a template example if provided in this organization:
- http://github.com/hep-forge/helloworld ; this is the effective software package you want to distribute
- http://github.com/hep-forge/helloworld-feedstock ; this repository is the one responsible for publishing in HEP channel.
