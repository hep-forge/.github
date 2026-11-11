# Migration `conda-forge-root`

rebuild, started 2026-11-10T16:33:00Z, updated 2026-11-11 02:25 UTC.

failed: 2 · blocked: 6 · building: 8 · ready: 3 · waiting: 18 · done: 5

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
| delphes | building | moved 3.5.1 to main e7f045f |
| gaudi | building | moved 40.6 to main f3acfc7 |
| hepmc | building | moved 3.3.1 to main f35a7d2 |
| rave | building | moved 0.6.25 to main 995d2de |
| root-plus | building | moved gamma to main 00f4f12 |
| roounfold | building | moved 3.1.0 to main adfa916 |
| scirooplot | building | moved 3.3.3 to main 6b86fe2 |
| vgm | ready |  |
| vmc | ready |  |
| yoda | ready |  |
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
| g4hepem | done |  |
| geant | done | built; channel not refreshed yet |
| lcg-relax | done |  |
| phlex | done |  |
| pythia | done | built; channel not refreshed yet |
