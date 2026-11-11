# Migration `conda-forge-root`

rebuild, started 2026-11-10T16:33:00Z, updated 2026-11-11 02:43 UTC.

failed: 2 · blocked: 6 · building: 8 · waiting: 18 · done: 8

| Package | State | Detail |
|---|---|---|
| jetphox | failed | [run](https://github.com/hep-forge/jetphox-feedstock/actions/runs/42943592449) Unsatisfiable dependencies for platform linux-aarch64: {MatchSpec("root_base[version='>=6.38.6,<6.38.7.0a0']"), MatchSpec("root"), MatchSpec("gl2ps[version='>=1 |
| podio | failed | [run](https://github.com/hep-forge/podio-feedstock/actions/runs/42943598803) CMake Error at /home/runner/miniconda/conda-bld/podio_1794362782385/_build_env/share/cmake-4.4/Modules/FindPackageHandleStandardArgs.cmake:290 (message): |
| acts | blocked | dd4hep |
| dd4hep | blocked | edm4hep, podio |
| edm4hep | blocked | podio |
| epic | blocked | dd4hep |
| jana | blocked | podio |
| npsim | blocked | dd4hep |
| combiner | building | moved 0.1.1 to main 178e2f9 |
| gaudi | building | moved 40.6 to main f3acfc7 |
| hepmc | building | moved 3.3.1 to main f35a7d2 |
| root-plus | building | moved gamma to main 00f4f12 |
| roounfold | building | moved 3.1.0 to main adfa916 |
| vgm | building | moved 5.5 to main cec7ab3 |
| vmc | building | moved 2.2 to main f4d9b4e |
| yoda | building | moved 2.1.4, 1.9.9 to main f802357 |
| afterburner | waiting | hepmc |
| apfelgrid | waiting | applgrid |
| applgrid | waiting | fastnlo |
| eic-smear | waiting | hepmc |
| escalade | waiting | root-plus |
| estarlight | waiting | hepmc |
| fastnlo | waiting | yoda |
| framel-root | waiting | root-plus |
| hammer | waiting | hepmc |
| hepmc-merger | waiting | hepmc |
| mcfm | waiting | applgrid |
| nestdaq | waiting | root-plus |
| professor | waiting | yoda |
| rapgap | waiting | hepmc, rivet |
| rivet | waiting | hepmc, yoda |
| sherpa | waiting | hepmc |
| xfitter | waiting | apfelgrid, applgrid |
| xfitter-dev | waiting | apfelgrid, applgrid |
| delphes | done |  |
| g4hepem | done |  |
| geant | done | built; channel not refreshed yet |
| lcg-relax | done |  |
| phlex | done |  |
| pythia | done | built; channel not refreshed yet |
| rave | done |  |
| scirooplot | done |  |
