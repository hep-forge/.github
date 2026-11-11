# Migration `conda-forge-root`

rebuild, started 2026-11-10T16:33:00Z, updated 2026-11-11 09:44 UTC.

failed: 8 · blocked: 9 · building: 3 · waiting: 3 · done: 19

| Package | State | Detail |
|---|---|---|
| combiner | failed | [run](https://github.com/hep-forge/combiner-feedstock/actions/runs/42950434757) No such file or directory |
| gaudi | failed | [run](https://github.com/hep-forge/gaudi-feedstock/actions/runs/42950439087) No such file or directory |
| hepmc-merger | failed | [run](https://github.com/hep-forge/hepmc-merger-feedstock/actions/runs/42995089475) CMake Error at CMakeLists.txt:45 (target_link_libraries): |
| jetphox | failed | [run](https://github.com/hep-forge/jetphox-feedstock/actions/runs/42987163534) error: conflicting types for 'sysconf'; have 'long int(void)' |
| podio | failed | [run](https://github.com/hep-forge/podio-feedstock/actions/runs/42987164613) CMake Error at cmake/podioBuild.cmake:205 (message): |
| root-plus | failed | [run](https://github.com/hep-forge/root-plus-feedstock/actions/runs/42995105019) error: namespaces can only be defined in global or namespace scope |
| roounfold | failed | [run](https://github.com/hep-forge/roounfold-feedstock/actions/runs/42952815617) No such file or directory |
| sherpa | failed | [run](https://github.com/hep-forge/sherpa-feedstock/actions/runs/42995114743) Unsatisfiable dependencies for platform linux-aarch64: {MatchSpec("hepmc=2.6")} |
| acts | blocked | dd4hep |
| dd4hep | blocked | edm4hep, podio |
| edm4hep | blocked | podio |
| epic | blocked | dd4hep |
| escalade | blocked | root-plus |
| framel-root | blocked | root-plus |
| jana | blocked | podio |
| nestdaq | blocked | root-plus |
| npsim | blocked | dd4hep |
| apfelgrid | building | moved 1.0.1 to main e909d55 |
| mcfm | building | moved 10.3-applgrid to main fa17657 |
| rivet | building | [run](https://github.com/hep-forge/rivet-feedstock/actions/runs/42995105904) |
| rapgap | waiting | rivet |
| xfitter | waiting | apfelgrid |
| xfitter-dev | waiting | apfelgrid |
| afterburner | done |  |
| applgrid | done |  |
| delphes | done |  |
| eic-smear | done |  |
| estarlight | done |  |
| fastnlo | done |  |
| g4hepem | done |  |
| geant | done | built; channel not refreshed yet |
| hammer | done |  |
| hepmc | done |  |
| lcg-relax | done |  |
| phlex | done |  |
| professor | done |  |
| pythia | done | built; channel not refreshed yet |
| rave | done |  |
| scirooplot | done |  |
| vgm | done |  |
| vmc | done |  |
| yoda | done |  |
