# hep-forge

[![hep-bot version check](https://github.com/hep-forge/.github/actions/workflows/hep-bot-check.yml/badge.svg)](https://github.com/hep-forge/.github/actions/workflows/hep-bot-check.yml)
[![Render & README Sync](https://github.com/hep-forge/.github/actions/workflows/render-sync.yml/badge.svg)](https://github.com/hep-forge/.github/actions/workflows/render-sync.yml)

Conda packages for High Energy Physics software that conda-forge doesn't provide, or doesn't
build the way HEP users need. The packages are published on the
[hep-forge](https://anaconda.org/hep-forge) channel for linux-64 and linux-aarch64, and they
install alongside conda-forge. On Apple Silicon, use the linux-aarch64 packages in Docker. For
native macOS or Windows builds, look at [conda-forge](https://conda-forge.org).

This repository ([hep-forge/.github](https://github.com/hep-forge/.github)) holds every
feedstock as a submodule, plus the shared CI templates, the scripts and hep-bot.

## Where to start

| I want to... | Go to |
|---|---|
| install a package | [Install](#install), then pick from the [package table](#packages) |
| know whether a package is up to date, or why it isn't | `@hep-bot status <pkg>` in any issue or pull request |
| get software packaged that isn't here | [Package new software](#package-new-software) |
| publish a new version, or fix a broken one | [Common tasks](#common-tasks) |
| learn how hep-forge works | comment `@hep-bot help` on any issue: hep-bot answers with every command and a short guide per topic |

## Install

```bash
conda install -c hep-forge -c conda-forge <package>
```

Add `root-guard` so that conda never swaps in conda-forge's ROOT:

```bash
conda install -c hep-forge -c conda-forge root root-guard rivet lhapdf pythia
```

For a reproducible setup, use an `environment.yml`:

```yaml
name: myhep
channels: [hep-forge, conda-forge]
dependencies: [root, root-guard, lhapdf, cernlib]
```

```bash
conda env create -f environment.yml && conda activate myhep
```

## Packages

"Latest tag" is the feedstock's newest release tag. "Published" is what anaconda.org serves.
render-sync refreshes this table every day.

<!-- status:begin -->
_Last refreshed: 2026-10-30 (`python3 scripts/update_readme_status.py`)_

| Feedstock | Latest tag | Published | amd64 | arm64 |
|-----------|------------|-----------|-------|-------|
| [acts](https://github.com/hep-forge/acts-feedstock) | `46.8.1` | [`46.8.1`](https://anaconda.org/hep-forge/acts) | ✅ | ✅ |
| [afterburner](https://github.com/hep-forge/afterburner-feedstock) | `0.2.1` | [`0.2.1`](https://anaconda.org/hep-forge/afterburner) | ✅ | ✅ |
| [apfel](https://github.com/hep-forge/apfel-feedstock) | `3.1.1` | [`3.1.1`](https://anaconda.org/hep-forge/apfel) | ✅ | ✅ |
| [apfelgrid](https://github.com/hep-forge/apfelgrid-feedstock) | `1.0.1` | [`1.0.1`](https://anaconda.org/hep-forge/apfelgrid) | ✅ | ✅ |
| [apfelxx](https://github.com/hep-forge/apfelxx-feedstock) | `4.10.0` | [`4.10.0`](https://anaconda.org/hep-forge/apfelxx) | ✅ | ✅ |
| [applgrid](https://github.com/hep-forge/applgrid-feedstock) | `1.6.49` | [`1.6.49`](https://anaconda.org/hep-forge/applgrid) | ✅ | ✅ |
| [cernlib](https://github.com/hep-forge/cernlib-feedstock) | `2024.09.16.0-free` | [`2024.09.16.0.free`](https://anaconda.org/hep-forge/cernlib) | ✅ | ✅ |
| [chaplin](https://github.com/hep-forge/chaplin-feedstock) | `1.2` | [`1.2`](https://anaconda.org/hep-forge/chaplin) | ✅ | ✅ |
| [collier](https://github.com/hep-forge/collier-feedstock) | `1.2.10` | [`1.2.10`](https://anaconda.org/hep-forge/collier) | ✅ | ✅ |
| [combiner](https://github.com/hep-forge/combiner-feedstock) | `0.1.1` | [`0.1.1`](https://anaconda.org/hep-forge/combiner) | ✅ | ✅ |
| [covfie](https://github.com/hep-forge/covfie-feedstock) | `0.15.6` | [`0.15.6`](https://anaconda.org/hep-forge/covfie) | ✅ | ✅ |
| [cuba](https://github.com/hep-forge/cuba-feedstock) | `4.2.2` | [`4.2.2`](https://anaconda.org/hep-forge/cuba) | ✅ | ✅ |
| [cubature](https://github.com/hep-forge/cubature-feedstock) | `1.0.4` | [`1.0.4`](https://anaconda.org/hep-forge/cubature) | ✅ | ✅ |
| [curlpp](https://github.com/hep-forge/curlpp-feedstock) | `0.8.1.1` | [`0.8.1.1`](https://anaconda.org/hep-forge/curlpp) | ✅ | ✅ |
| [cuttools](https://github.com/hep-forge/cuttools-feedstock) | `2.0` | [`2.0`](https://anaconda.org/hep-forge/cuttools) | ✅ | ✅ |
| [dd4hep](https://github.com/hep-forge/dd4hep-feedstock) | `1.37` | [`1.37`](https://anaconda.org/hep-forge/dd4hep) | ✅ | ✅ |
| [delphes](https://github.com/hep-forge/delphes-feedstock) | `3.5.1` | [`3.5.1`](https://anaconda.org/hep-forge/delphes) | ✅ | ✅ |
| [difftop](https://github.com/hep-forge/difftop-feedstock) | `1.0.0` | [`1.0.0`](https://anaconda.org/hep-forge/difftop) | ✅ | ✅ |
| [djangoh](https://github.com/hep-forge/djangoh-feedstock) | `4.6.21` | [`4.6.21`](https://anaconda.org/hep-forge/djangoh) | ✅ | ✅ |
| [dyturbo](https://github.com/hep-forge/dyturbo-feedstock) | `1.4.2` | [`1.4.2`](https://anaconda.org/hep-forge/dyturbo) | ✅ | ✅ |
| [edm4hep](https://github.com/hep-forge/edm4hep-feedstock) | `1.0.0` | [`1.0.0`](https://anaconda.org/hep-forge/edm4hep) | ✅ | ✅ |
| [eic-smear](https://github.com/hep-forge/eic-smear-feedstock) | `1.2.3` | [`1.2.3`](https://anaconda.org/hep-forge/eic-smear) | ✅ | ✅ |
| [eko](https://github.com/hep-forge/eko-feedstock) | `0.14.6` | [`0.14.6`](https://anaconda.org/hep-forge/eko) | ✅ | ✅ |
| [emela](https://github.com/hep-forge/emela-feedstock) | `1.0.1` | [`1.0.1`](https://anaconda.org/hep-forge/emela) | ✅ | ✅ |
| [epic](https://github.com/hep-forge/epic-feedstock) | `26.06.0` | [`26.06.0`](https://anaconda.org/hep-forge/epic) | ✅ | ✅ |
| [escalade](https://github.com/hep-forge/escalade-feedstock) | `v9.08.26` | [`v9.08.26`](https://anaconda.org/hep-forge/escalade) | ✅ | ✅ |
| [estarlight](https://github.com/hep-forge/estarlight-feedstock) | `1.2.0` | [`1.2.0`](https://anaconda.org/hep-forge/estarlight) | ✅ | ✅ |
| [fairmq](https://github.com/hep-forge/fairmq-feedstock) | `1.11.0` | [`1.11.0`](https://anaconda.org/hep-forge/fairmq) | ✅ | ✅ |
| [fastjet-contrib](https://github.com/hep-forge/fastjet-contrib-feedstock) | `1.105` | [`1.105`](https://anaconda.org/hep-forge/fastjet-contrib) | ✅ | ✅ |
| [fastjet](https://github.com/hep-forge/fastjet-feedstock) | `3.5.3` | [`3.5.3`](https://anaconda.org/hep-forge/fastjet) | ✅ | ✅ |
| [fastnlo](https://github.com/hep-forge/fastnlo-feedstock) | `2.6.0` | [`2.6.0`](https://anaconda.org/hep-forge/fastnlo) | ✅ | ✅ |
| [framel](https://github.com/hep-forge/framel-feedstock) | `8.50.3` | [`8.50.3`](https://anaconda.org/hep-forge/framel) | ✅ | ✅ |
| [framel-root](https://github.com/hep-forge/framel-root-feedstock) | `1.0.0` | [`1.0.0`](https://anaconda.org/hep-forge/framel-root) | ✅ | ✅ |
| [g4hepem](https://github.com/hep-forge/g4hepem-feedstock) | `20251114` | [`20251114`](https://anaconda.org/hep-forge/g4hepem) | ✅ | ✅ |
| [gaudi](https://github.com/hep-forge/gaudi-feedstock) | `40.6` | [`40.6`](https://anaconda.org/hep-forge/gaudi) | ✅ | ✅ |
| [geant](https://github.com/hep-forge/geant-feedstock) | `11.4.1` | [`11.4.1`](https://anaconda.org/hep-forge/geant) | ✅ | ✅ |
| [gosam](https://github.com/hep-forge/gosam-feedstock) | `3.0.3` | [`3.0.3`](https://anaconda.org/hep-forge/gosam) | ✅ | ✅ |
| [hammer](https://github.com/hep-forge/hammer-feedstock) | `2.0.0` | [`2.0.0`](https://anaconda.org/hep-forge/hammer) | ✅ | ✅ |
| [hathor](https://github.com/hep-forge/hathor-feedstock) | `2.0` | [`2.0`](https://anaconda.org/hep-forge/hathor) | ✅ | ✅ |
| [hell](https://github.com/hep-forge/hell-feedstock) | `3.1` | [`3.1`](https://anaconda.org/hep-forge/hell) | ✅ | ✅ |
| [hellx](https://github.com/hep-forge/hellx-feedstock) | `3.0` | [`3.0`](https://anaconda.org/hep-forge/hellx) | ✅ | ✅ |
| [hepmc](https://github.com/hep-forge/hepmc-feedstock) | `3.3.1` | [`3.3.1`](https://anaconda.org/hep-forge/hepmc) | ✅ | ✅ |
| [hepmc-merger](https://github.com/hep-forge/hepmc-merger-feedstock) | `2.4.0` | [`2.4.0`](https://anaconda.org/hep-forge/hepmc-merger) | ✅ | ✅ |
| [herwig7](https://github.com/hep-forge/herwig7-feedstock) | `7.3.0` | [`7.3.0`](https://anaconda.org/hep-forge/herwig7) | ✅ | ✅ |
| [hoppet](https://github.com/hep-forge/hoppet-feedstock) | `2.2.0` | [`2.2.0`](https://anaconda.org/hep-forge/hoppet) | ✅ | ✅ |
| [inih](https://github.com/hep-forge/inih-feedstock) | `r60` | [`r60`](https://anaconda.org/hep-forge/inih) | ✅ | ✅ |
| [iregi](https://github.com/hep-forge/iregi-feedstock) | `1.1.0` | [`1.1.0`](https://anaconda.org/hep-forge/iregi) | ✅ | ✅ |
| [jana](https://github.com/hep-forge/jana-feedstock) | `2026.03.01` | [`2026.03.01`](https://anaconda.org/hep-forge/jana) | ✅ | ✅ |
| [jetphox](https://github.com/hep-forge/jetphox-feedstock) | `1.3.1_4` | [`1.3.1.4`](https://anaconda.org/hep-forge/jetphox) | ✅ | ✅ |
| [kfrlib](https://github.com/hep-forge/kfrlib-feedstock) | `7.0.1` | [`7.0.1`](https://anaconda.org/hep-forge/kfrlib) | ✅ | ✅ |
| [lcg-relax](https://github.com/hep-forge/lcg-relax-feedstock) | `6.1.2` | [`6.1.2`](https://anaconda.org/hep-forge/lcg-relax) | ✅ | ✅ |
| [lhapdf](https://github.com/hep-forge/lhapdf-feedstock) | `6.5.6` | [`6.5.6`](https://anaconda.org/hep-forge/lhapdf) | ✅ | ✅ |
| [libdate-tz](https://github.com/hep-forge/libdate-tz-feedstock) | `3.0.5` | [`3.0.5`](https://anaconda.org/hep-forge/libdate-tz) | ✅ | ✅ |
| [looptools](https://github.com/hep-forge/looptools-feedstock) | `2.16` | [`2.16`](https://anaconda.org/hep-forge/looptools) | ✅ | ✅ |
| [mcfm](https://github.com/hep-forge/mcfm-feedstock) | `10.3-applgrid` | [`10.3.applgrid`](https://anaconda.org/hep-forge/mcfm) | ✅ | ✅ |
| [minio-cpp](https://github.com/hep-forge/minio-cpp-feedstock) | `0.3.0.1` | [`0.3.0.1`](https://anaconda.org/hep-forge/minio-cpp) | ✅ | ✅ |
| [mpfun90](https://github.com/hep-forge/mpfun90-feedstock) | `2024.12.06` | [`2024.12.06`](https://anaconda.org/hep-forge/mpfun90) | ✅ | ✅ |
| [nestdaq](https://github.com/hep-forge/nestdaq-feedstock) | `1.0.0` | [`1.0.0`](https://anaconda.org/hep-forge/nestdaq) | ✅ | ✅ |
| [ninja-hep-ph](https://github.com/hep-forge/ninja-hep-ph-feedstock) | `1.2.1` | [`1.2.1`](https://anaconda.org/hep-forge/ninja-hep-ph) | ✅ | ✅ |
| [nlojetxx](https://github.com/hep-forge/nlojetxx-feedstock) | `4.1.3` | [`4.1.3`](https://anaconda.org/hep-forge/nlojetxx) | ✅ | ✅ |
| [nnlojet](https://github.com/hep-forge/nnlojet-feedstock) | `1.0.0` | [`1.0.0`](https://anaconda.org/hep-forge/nnlojet) | ✅ | ✅ |
| [nnpdf](https://github.com/hep-forge/nnpdf-feedstock) | `4.0.9` | [`4.0.9`](https://anaconda.org/hep-forge/nnpdf) | ✅ | ✅ |
| [npsim](https://github.com/hep-forge/npsim-feedstock) | `1.6.1` | [`1.6.1`](https://anaconda.org/hep-forge/npsim) | ✅ | ✅ |
| [numdiff](https://github.com/hep-forge/numdiff-feedstock) | `5.9.0` | [`5.9.0`](https://anaconda.org/hep-forge/numdiff) | ✅ | ✅ |
| [oneloop](https://github.com/hep-forge/oneloop-feedstock) | `3.7.2` | [`3.7.2`](https://anaconda.org/hep-forge/oneloop) | ✅ | ✅ |
| [pepper](https://github.com/hep-forge/pepper-feedstock) | `1.14.1` | [`1.14.1`](https://anaconda.org/hep-forge/pepper) | ✅ | ✅ |
| [phlex](https://github.com/hep-forge/phlex-feedstock) | `0.4.3` | — | ❌ | ❌ |
| [pineappl](https://github.com/hep-forge/pineappl-feedstock) | `0.8.6` | [`0.8.6`](https://anaconda.org/hep-forge/pineappl) | ✅ | ✅ |
| [ploughshare](https://github.com/hep-forge/ploughshare-feedstock) | `0.0.20` | [`0.0.20`](https://anaconda.org/hep-forge/ploughshare) | ✅ | ✅ |
| [podio](https://github.com/hep-forge/podio-feedstock) | `1.7.0` | [`1.7.0`](https://anaconda.org/hep-forge/podio) | ✅ | ✅ |
| [professor](https://github.com/hep-forge/professor-feedstock) | `2.5.9` | [`2.5.9`](https://anaconda.org/hep-forge/professor) | ✅ | ✅ |
| [pythia](https://github.com/hep-forge/pythia-feedstock) | `8.3.12` | [`8.3.12`](https://anaconda.org/hep-forge/pythia) | ✅ | ✅ |
| [qcdloop](https://github.com/hep-forge/qcdloop-feedstock) | `2.1.0` | [`2.1.0`](https://anaconda.org/hep-forge/qcdloop) | ✅ | ✅ |
| [qcdnum](https://github.com/hep-forge/qcdnum-feedstock) | `18.00.00` | [`18.00.00`](https://anaconda.org/hep-forge/qcdnum) | ✅ | ✅ |
| [rapgap](https://github.com/hep-forge/rapgap-feedstock) | `3.310` | [`3.310`](https://anaconda.org/hep-forge/rapgap) | ✅ | ✅ |
| [rave](https://github.com/hep-forge/rave-feedstock) | `0.6.25` | [`0.6.25`](https://anaconda.org/hep-forge/rave) | ✅ | ✅ |
| [rivet](https://github.com/hep-forge/rivet-feedstock) | `4.1.3` | [`4.1.3`](https://anaconda.org/hep-forge/rivet) | ✅ | ✅ |
| [root](https://github.com/hep-forge/root-feedstock) | `6.40.04` | [`6.40.04`](https://anaconda.org/hep-forge/root) | ✅ | ✅ |
| [root-guard](https://github.com/hep-forge/root-guard-feedstock) | `1.0` | [`1`](https://anaconda.org/hep-forge/root-guard) | ✅ | ✅ |
| [root-plus](https://github.com/hep-forge/root-plus-feedstock) | `beta` | [`beta`](https://anaconda.org/hep-forge/root-plus) | ✅ | ✅ |
| [roounfold](https://github.com/hep-forge/roounfold-feedstock) | `3.1.0` | [`3.1.0`](https://anaconda.org/hep-forge/roounfold) | ✅ | ✅ |
| [scirooplot](https://github.com/hep-forge/scirooplot-feedstock) | `3.3.3` | [`3.3.3`](https://anaconda.org/hep-forge/scirooplot) | ✅ | ✅ |
| [sherpa](https://github.com/hep-forge/sherpa-feedstock) | `2.2.16` | [`2.2.16`](https://anaconda.org/hep-forge/sherpa) | ✅ | ✅ |
| [sz3](https://github.com/hep-forge/sz3-feedstock) | `3.4.0` | [`3.4.0`](https://anaconda.org/hep-forge/sz3) | ✅ | ✅ |
| [thepeg](https://github.com/hep-forge/thepeg-feedstock) | `2.3.0` | [`2.3.0`](https://anaconda.org/hep-forge/thepeg) | ✅ | ✅ |
| [troll](https://github.com/hep-forge/troll-feedstock) | `3.3` | [`3.3`](https://anaconda.org/hep-forge/troll) | ✅ | ✅ |
| [vgm](https://github.com/hep-forge/vgm-feedstock) | `5.5` | [`5.5`](https://anaconda.org/hep-forge/vgm) | ✅ | ✅ |
| [vmc](https://github.com/hep-forge/vmc-feedstock) | `2.2` | [`2.2`](https://anaconda.org/hep-forge/vmc) | ✅ | ✅ |
| [xfitter-dev](https://github.com/hep-forge/xfitter-dev-feedstock) | `2.2.1` | [`2.2.1`](https://anaconda.org/hep-forge/xfitter-dev) | ✅ | ✅ |
| [xfitter](https://github.com/hep-forge/xfitter-feedstock) | `2.2.1` | [`2.2.1`](https://anaconda.org/hep-forge/xfitter) | ✅ | ✅ |
| [yadism](https://github.com/hep-forge/yadism-feedstock) | `0.12.5` | [`0.12.5`](https://anaconda.org/hep-forge/yadism) | ✅ | ✅ |
| [yoda](https://github.com/hep-forge/yoda-feedstock) | `2.1.4` | [`2.1.4`](https://anaconda.org/hep-forge/yoda) | ✅ | ✅ |

⚠️ = the latest feedstock tag is not published on anaconda.org (build failed or still running); tag `X-y` publishes as `X.y`.
<!-- status:end -->

## Working with hep-bot

hep-bot does the routine work for you. You talk to it in GitHub issues: write
`@hep-bot <command>` in a new issue or a comment, in this repo or in any feedstock. It
reacts with 👀 and answers in the same thread, usually within a minute. A repo it doesn't
know yet (a feedstock made by hand) gets its answer from the sweep within 20 minutes.

### Commands

| Command | What it does | Who |
|---|---|---|
| `@hep-bot help [<topic>]` | Lists every command with a short guide per topic, or posts one guide | anyone |
| `@hep-bot status [<pkg>]` | The feedstock's tags, its last builds and what is published on anaconda.org | anyone |
| `@hep-bot new <pkg> <upstream-url> [license=<spdx>] [maintainers=a,b] [summary]` | Creates `hep-forge/<pkg>-feedstock` with a starter recipe | members |
| `@hep-bot rerun [<pkg>] <tag>` | Rebuilds and publishes an existing tag, using the recipe as it was at that tag | members |
| `@hep-bot rerender [<pkg>]` | Refreshes the feedstock's CI and bot files, and registers it here if needed | members |

"Members" means org members and repo collaborators. Inside a feedstock, `<pkg>` is that
feedstock and can be left out. Plain wording works ("@hep-bot, please rerender"), and so do
questions: `@hep-bot how do I publish a new version?` gets the guide about releases. In pull
requests hep-bot answers `help` and `status` only. The *New feedstock* and *Rerender
feedstock* forms under **New issue** do the same as `new` and `rerender`.

The guides are short pages in
[`scripts/hep_bot/guide/`](https://github.com/hep-forge/.github/tree/main/scripts/hep_bot/guide),
also readable on GitHub:
[new](https://github.com/hep-forge/.github/blob/main/scripts/hep_bot/guide/new.md) (package new software),
[recipe](https://github.com/hep-forge/.github/blob/main/scripts/hep_bot/guide/recipe.md),
[release](https://github.com/hep-forge/.github/blob/main/scripts/hep_bot/guide/release.md) (tags, `head`, labels),
[rerun](https://github.com/hep-forge/.github/blob/main/scripts/hep_bot/guide/rerun.md),
[rerender](https://github.com/hep-forge/.github/blob/main/scripts/hep_bot/guide/rerender.md),
[updates](https://github.com/hep-forge/.github/blob/main/scripts/hep_bot/guide/updates.md) (the daily version check) and
[install](https://github.com/hep-forge/.github/blob/main/scripts/hep_bot/guide/install.md).

### Package new software

1. Check that it belongs here: compiled HEP software that conda-forge doesn't have, or
   doesn't build the way HEP users need. Pure-Python packages are already on pip, and
   generic libraries belong on conda-forge.
2. Open a [*New feedstock* issue](https://github.com/hep-forge/.github/issues/new?template=new-feedstock.yml),
   or comment `@hep-bot new mypkg https://github.com/org/mypkg license=MIT` in an issue here.
   hep-bot creates `hep-forge/mypkg-feedstock` and replies with the link.
3. Write the recipe in `recipe/` (version and sha256, dependencies, `build.sh`, a real test)
   in a PR on the feedstock. `@hep-bot help recipe` lists what it needs. Coding agents
   should read [AGENTS.md](https://github.com/hep-forge/.github/blob/main/AGENTS.md) first.
4. Once the PR is merged, push the version as a tag on `main`:
   `git tag 1.2.3 && git push origin 1.2.3`. That builds and publishes it, and from then on
   the daily version check keeps it up to date.

If the feedstock repo already exists (made by hand or by an agent), use
`@hep-bot rerender mypkg` instead of step 2. Locally,
`make new-feedstock NAME=mypkg REPO=<upstream-url>` does the same as step 2.

### Common tasks

| Task | How |
|---|---|
| See what is built and published | `@hep-bot status <pkg>` |
| Fix a feedstock made by hand | `@hep-bot rerender` in that feedstock |
| Publish a release | push the version tag on `main` (`git tag 1.2.3 && git push origin 1.2.3`), or wait for the next daily version check |
| Re-publish a recipe fix under the same version | merge the fix, then move the tag: `git tag -f 1.2.3 && git push -f origin refs/tags/1.2.3` (`rerun` would rebuild the recipe as it was at the tag) |
| Retry a build that failed outside the recipe (runner, download, missing dependency) | `@hep-bot rerun 1.2.3` |
| Follow upstream main | create a `head` tag once; hep-bot moves it whenever upstream gets a new commit |

Nothing is published without a tag. Merging a PR or pushing to `main` only changes the recipe.

## How a feedstock builds

- **Only a tag builds.** Pushing a tag such as `3.5.3` to a feedstock runs
  [`autoupload.yml`](https://github.com/hep-forge/.github/blob/main/scripts/templates/autoupload.yml):
  `conda build recipe` on linux-64 and linux-aarch64 (macos-arm64 is compiled but not published),
  then an upload to anaconda.org. Merging a PR or pushing to `main` publishes nothing.
- A numeric tag is a release: tag `X-y` publishes as `X.y`, and the tag must be a key of the
  `versions` dict in `recipe/meta.yaml`.
- **`head` is the tag that tracks upstream main/master.** The recipe maps the version `head`
  to the upstream branch (with a git source, `git_rev: {{ versions.get(version, "HEAD") }}`
  already does that). It publishes as version `head`, which conda ranks below every
  release, so you only get it if you ask for it: `conda install -c hep-forge xfitter=head`.
  hep-bot rebuilds `head` when upstream main moves.
- Branches are anaconda labels. `main` publishes to `main`, and a `legacy` branch publishes
  to `legacy` (`conda install -c hep-forge/label/legacy pythia`). A tag builds the branch it was
  created from.
- Each label keeps its newest 2 versions. Older versions are deleted unless they are listed in
  `extra.lts` in the recipe or carry the `keep` label
  (`anaconda copy hep-forge/<pkg>/<version> --from-label main --to-label keep`).
- Recipes pin their own compilers and a glibc 2.17 floor in `recipe/conda_build_config.yaml`.
  No conda-forge global pinning is applied. `make check-glibc` finds packages that leak
  newer glibc symbols anyway.

### Rendering, and what conda-smithy does here

`conda smithy rerender` does **not** produce the hep-forge CI. It writes conda-forge's own
workflows, which hep-forge doesn't use. The hep-forge render copies a few files from this
repo into every registered feedstock:

| File in the feedstock | Source here |
|---|---|
| `.github/workflows/autoupload.yml` | [`scripts/templates/autoupload.yml`](https://github.com/hep-forge/.github/blob/main/scripts/templates/autoupload.yml) |
| `.github/workflows/hep-bot-comment.yml` | [`scripts/templates/hep-bot-comment.yml`](https://github.com/hep-forge/.github/blob/main/scripts/templates/hep-bot-comment.yml) |
| `AGENTS.md` | [`scripts/templates/AGENTS.md`](https://github.com/hep-forge/.github/blob/main/scripts/templates/AGENTS.md) |
| `README.md` | [`scripts/generate_readme.py`](https://github.com/hep-forge/.github/blob/main/scripts/generate_readme.py) |

[render-sync](https://github.com/hep-forge/.github/actions/workflows/render-sync.yml) does this
every day for every feedstock that is a submodule here. A feedstock that is not registered
never gets rendered. That is why a repo created by hand ends up with stale or missing
workflows. `@hep-bot rerender <pkg>` registers it and renders it straight away.

I keep the hep-forge specifics in these templates and scripts instead of a conda-smithy fork,
because a fork would have to follow every conda-smithy release.

## How hep-bot works

hep-bot is GitHub Actions workflows in this repo plus the code in
[`scripts/hep_bot/`](https://github.com/hep-forge/.github/tree/main/scripts/hep_bot). There is
no server and no separate bot account: it acts with the org secret `HEP_BOT_TOKEN`, so its
comments, pushes and tags appear under the token owner's name. Each feedstock only carries
`.github/workflows/hep-bot-comment.yml`, which runs the code from this repo.

| Workflow | When | What it does |
|---|---|---|
| [version check](https://github.com/hep-forge/.github/actions/workflows/hep-bot-check.yml) | Daily, or manually (dry run by default) | For every feedstock: bumps the recipe to a newer upstream patch/minor release and tags it, so it builds and publishes. Tags recipes that are ahead of their newest tag, and rebuilds `head` when upstream main has moved or the recipe changed. Lists new major versions and git sources in the issue *[hep-bot] upstream updates that need a human* |
| [render-sync](https://github.com/hep-forge/.github/actions/workflows/render-sync.yml) | Daily, on template changes, or manually | Renders every feedstock, refreshes the table above and moves the submodule pointers |
| [ordered rebuild](https://github.com/hep-forge/.github/actions/workflows/hep-bot-rebuild.yml) | Manually | Rebuilds a package and everything that depends on it, tier by tier ([`dag.yaml`](https://github.com/hep-forge/.github/blob/main/scripts/hep_bot/dag.yaml)) |
| [new feedstock](https://github.com/hep-forge/.github/actions/workflows/new-feedstock.yml) | `@hep-bot new` or the issue form | Creates and registers a feedstock |
| [sweep](https://github.com/hep-forge/.github/actions/workflows/hep-bot-sweep.yml) | Every 10 minutes | Answers `@hep-bot` requests in any hep-forge repo that the repo's own workflow didn't handle |
| [channel maintenance](https://github.com/hep-forge/.github/actions/workflows/channel-maintenance.yml) | Mondays, or manually | Trims old versions channel-wide and moves `master` labels to `main` |

Upstream versions come from each recipe's source URL. Add an override in
[`sources.yaml`](https://github.com/hep-forge/.github/blob/main/scripts/hep_bot/sources.yaml)
only when that detection is wrong, and set `auto_update: false` in `dag.yaml` to leave a
package alone.

### Under the hood

Everything below runs in this repo or is copied from it.

```
 issue / comment in any repo ─┐
                              ├─► comment.py ──► workflow in this repo ──► reply on the issue
 sweep (every 10 min) ────────┘                  (render-sync, new-feedstock)

 version check (daily) ────► push a tag on a feedstock ──► its autoupload.yml builds
                                                           amd64 + arm64 ──► anaconda.org
```

- **Commands.** Each registered feedstock carries `hep-bot-comment.yml`. When an issue or
  comment mentions `@hep-bot`, it checks out
  [`scripts/hep_bot/comment.py`](https://github.com/hep-forge/.github/blob/main/scripts/hep_bot/comment.py)
  from this repo and runs it, so changing the bot never touches the feedstocks. Short
  jobs (`rerun`, `status`, `help`) are done right there. Long ones (`rerender`, `new`) start
  [render-sync](https://github.com/hep-forge/.github/actions/workflows/render-sync.yml) or
  [new-feedstock](https://github.com/hep-forge/.github/actions/workflows/new-feedstock.yml)
  here, which report back on the issue when they finish.
- **Sweep.** Repos without the workflow (new, or made by hand) can't trigger anything.
  Every 10 minutes [the sweep](https://github.com/hep-forge/.github/actions/workflows/hep-bot-sweep.yml)
  searches the org for `@hep-bot` requests and form issues from the last week and handles
  the unanswered ones with the same code.
- **No double answers.** Every bot reply ends with a hidden `<!-- hep-bot:<id> -->` marker
  naming the request it answered. The sweep skips requests that already have one, and the
  bot ignores any text carrying a marker, so it never reacts to its own messages.
- **Rendering.** render-sync puts each registered feedstock on its `main` tip, copies the
  templates from `scripts/templates/` (build workflow, bot workflow, AGENTS.md),
  regenerates the README, pushes, and moves the submodule pointers here. conda-smithy plays
  no part in this.
- **Version check.** For each feedstock it reads the `versions` dict and source URL of
  `recipe/meta.yaml`, finds the newest upstream release (`git ls-remote` on the upstream
  repo, or the download page), and either bumps the recipe and pushes the new tag, tags a
  recipe that is ahead of its newest tag, moves `head` (upstream committed, or the recipe
  changed since `head` was built), or lists the package in the tracking issue.
- **Publishing.** Only a tag push builds. The feedstock's own `autoupload.yml` builds
  linux-64 and linux-aarch64, uploads to anaconda.org under the branch's label, and trims
  old versions.
- **Identity.** All of this acts with the org secret `HEP_BOT_TOKEN`, a fine-grained token
  with Contents, Workflows, Actions, Issues and Administration rights on the org's repos.
  Regenerating it means updating the org secret straight away. Uploads use
  `ANACONDA_API_TOKEN`.

## Maintenance from a clone

```bash
git clone --recurse-submodules git@github.com:hep-forge/.github.git hep-feedstocks
cd hep-feedstocks
make status            # tags, labels and the latest run per feedstock (ARGS="--failed")
make inspect pythia    # published versions, tags, runs and error log for one package
make retag fastjet     # move the latest tag to main and rebuild with the current recipe
make rerun fastjet     # rebuild the latest tag as it is
make bot-check         # version check, dry run
make root-bump VERSION=6.40   # add a ROOT version to the downstream build matrices (keeps 2)
make check-glibc       # find published binaries that need a newer glibc than 2.17
```

Package names are bare (`root`, not `root-feedstock`). The full list is in the
[Makefile](https://github.com/hep-forge/.github/blob/main/Makefile).

## Self-hosted runners

GitHub-hosted runners stop after 6 hours, which is tight for ROOT. To use your own machine,
register an org runner (**hep-forge → Settings → Actions → Runners → New self-hosted runner**)
with the label `hep-forge-amd64` or `hep-forge-arm64`, and set that leg's `runs-on` in the
feedstock's `autoupload.yml`, e.g. `runs-on: [self-hosted, linux, ARM64, hep-forge-arm64]`.
Don't do that in the template, or render-sync overwrites it for every feedstock.

## Analysis replay

[`analyses/run_analysis.sh`](https://github.com/hep-forge/.github/blob/main/analyses/run_analysis.sh)
runs a Rivet analysis in a locked environment and compares the result with a reference
`.yoda` file in `analyses/reference/`. The
[analysis replay](https://github.com/hep-forge/.github/actions/workflows/replay-analysis.yml)
workflow runs the same thing on a self-hosted runner.

## License

[MIT](https://github.com/hep-forge/.github/blob/main/LICENSE). Each package keeps its own
upstream license.
