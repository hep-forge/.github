# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 15:06 UTC.

failed: 6 · blocked: 17 · done: 48 · n/a: 25

| Package | State | Detail |
|---|---|---|
| dyturbo | failed | [run](https://github.com/hep-forge/dyturbo-feedstock/actions/runs/41656755309) error: variable-sized object may not be initialized |
| g4hepem | failed | [run](https://github.com/hep-forge/g4hepem-feedstock/actions/runs/41653610152) CMake Error at /Users/runner/miniconda/conda-bld/g4hepem_1793715996830/_build_env/share/cmake-4.4/Modules/FindPackageHandleStandardArgs.cmake:290 (message): |
| hepmc | failed | [run](https://github.com/hep-forge/hepmc-feedstock/actions/runs/41653633225) No such file or directory |
| jetphox | failed | [run](https://github.com/hep-forge/jetphox-feedstock/actions/runs/41656803823) error: use of built-in trait '__decay(decltype((std::__1::__to_address_helper<_Pointer, void>::__call)((declval<const _Pointer&>)())))' in function signature; u |
| thepeg | failed | [run](https://github.com/hep-forge/thepeg-feedstock/actions/runs/41656860653) error: no template named 'insert_iterator' in namespace 'std' |
| yoda | failed | [run](https://github.com/hep-forge/yoda-feedstock/actions/runs/41653703076) No such file or directory |
| acts | blocked | dd4hep |
| afterburner | blocked | hepmc |
| apfelgrid | blocked | applgrid |
| applgrid | blocked | fastnlo |
| dd4hep | blocked | g4hepem, hepmc |
| eic-smear | blocked | hepmc |
| epic | blocked | dd4hep |
| estarlight | blocked | hepmc |
| fastnlo | blocked | yoda |
| hepmc-merger | blocked | hepmc |
| herwig7 | blocked | thepeg |
| npsim | blocked | dd4hep |
| professor | blocked | yoda |
| rapgap | blocked | hepmc, rivet |
| rivet | blocked | hepmc, yoda |
| xfitter | blocked | apfelgrid, applgrid, dyturbo |
| xfitter-dev | blocked | apfelgrid, applgrid, dyturbo |
| apfel | done |  |
| apfelxx | done |  |
| chaplin | done |  |
| collier | done |  |
| combiner | done |  |
| covfie | done |  |
| cuba | done |  |
| cubature | done |  |
| curlpp | done |  |
| cuttools | done |  |
| delphes | done |  |
| difftop | done |  |
| djangoh | done |  |
| edm4hep | done |  |
| emela | done |  |
| escalade | done |  |
| fastjet | done |  |
| fastjet-contrib | done |  |
| framel | done |  |
| framel-root | done | built; channel not refreshed yet |
| geant | done | built; channel not refreshed yet |
| gosam | done |  |
| hathor | done |  |
| hell | done |  |
| hellx | done |  |
| hoppet | done |  |
| inih | done |  |
| iregi | done |  |
| jana | done |  |
| kalman | done |  |
| kfrlib | done |  |
| lhapdf | done |  |
| libdate-tz | done |  |
| looptools | done |  |
| minio-cpp | done |  |
| mpfun90 | done |  |
| nlojetxx | done |  |
| nnlojet | done |  |
| numdiff | done |  |
| oneloop | done |  |
| pepper | done |  |
| pineappl | done |  |
| ploughshare | done |  |
| podio | done |  |
| pythia | done |  |
| qcdnum | done |  |
| root-plus | done |  |
| sz3 | done |  |
| applfast | n/a | nothing published |
| cernlib | n/a | Linux only |
| eko | n/a | noarch |
| fairmq | n/a | Linux only |
| gaudi | n/a | Linux only |
| hammer | n/a | Linux only |
| lcg-relax | n/a | Linux only |
| lhapdf5 | n/a | nothing published |
| mcfm | n/a | Linux only |
| mg5amcnlo | n/a | Linux only |
| nestdaq | n/a | Linux only |
| ninja-hep-ph | n/a | Linux only |
| nnpdf | n/a | noarch |
| phlex | n/a | Linux only |
| qcdloop | n/a | Linux only |
| rave | n/a | Linux only |
| root | n/a | Linux only |
| root-guard | n/a | noarch |
| roounfold | n/a | Linux only |
| scirooplot | n/a | Linux only |
| sherpa | n/a | Linux only |
| troll | n/a | Linux only |
| vgm | n/a | Linux only |
| vmc | n/a | Linux only |
| yadism | n/a | noarch |
