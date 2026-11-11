# Migration `conda-forge-root`

rebuild, started 2026-11-10T16:33:00Z, updated 2026-11-11 03:05 UTC.

failed: 3 · blocked: 15 · building: 5 · waiting: 9 · done: 10

| Package | State | Detail |
|---|---|---|
| jetphox | failed | [run](https://github.com/hep-forge/jetphox-feedstock/actions/runs/42943592449) Unsatisfiable dependencies for platform linux-aarch64: {MatchSpec("root_base[version='>=6.38.6,<6.38.7.0a0']"), MatchSpec("root"), MatchSpec("gl2ps[version='>=1 |
| podio | failed | [run](https://github.com/hep-forge/podio-feedstock/actions/runs/42943598803) CMake Error at /home/runner/miniconda/conda-bld/podio_1794362782385/_build_env/share/cmake-4.4/Modules/FindPackageHandleStandardArgs.cmake:290 (message): |
| yoda | failed | [run](https://github.com/hep-forge/yoda-feedstock/actions/runs/42947953051) error: Cython is required for --enable-pyext. |
| acts | blocked | dd4hep |
| apfelgrid | blocked | applgrid |
| applgrid | blocked | fastnlo |
| dd4hep | blocked | edm4hep, podio |
| edm4hep | blocked | podio |
| epic | blocked | dd4hep |
| fastnlo | blocked | yoda |
| jana | blocked | podio |
| mcfm | blocked | applgrid |
| npsim | blocked | dd4hep |
| professor | blocked | yoda |
| rapgap | blocked | rivet |
| rivet | blocked | yoda |
| xfitter | blocked | apfelgrid, applgrid |
| xfitter-dev | blocked | apfelgrid, applgrid |
| combiner | building | moved 0.1.1 to main 178e2f9 |
| gaudi | building | moved 40.6 to main f3acfc7 |
| hepmc | building | moved 3.3.1 to main f35a7d2 |
| root-plus | building | moved gamma to main 00f4f12 |
| roounfold | building | moved 3.1.0 to main adfa916 |
| afterburner | waiting | hepmc |
| eic-smear | waiting | hepmc |
| escalade | waiting | root-plus |
| estarlight | waiting | hepmc |
| framel-root | waiting | root-plus |
| hammer | waiting | hepmc |
| hepmc-merger | waiting | hepmc |
| nestdaq | waiting | root-plus |
| sherpa | waiting | hepmc |
| delphes | done |  |
| g4hepem | done |  |
| geant | done | built; channel not refreshed yet |
| lcg-relax | done |  |
| phlex | done |  |
| pythia | done | built; channel not refreshed yet |
| rave | done |  |
| scirooplot | done |  |
| vgm | done |  |
| vmc | done |  |
