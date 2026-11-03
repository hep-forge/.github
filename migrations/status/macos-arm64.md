# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 16:25 UTC.

failed: 7 · blocked: 12 · done: 52 · n/a: 25

| Package | State | Detail |
|---|---|---|
| afterburner | failed | [run](https://github.com/hep-forge/afterburner-feedstock/actions/runs/41666854453) CMake Error at CMakeLists.txt:17 (find_package): |
| dd4hep | failed | [run](https://github.com/hep-forge/dd4hep-feedstock/actions/runs/41666878679) CMake Error at /Users/runner/miniconda/conda-bld/dd4hep_1793720680040/_build_env/share/cmake-4.4/Modules/FindPackageHandleStandardArgs.cmake:290 (message): |
| eic-smear | failed | [run](https://github.com/hep-forge/eic-smear-feedstock/actions/runs/41666907839) error: 'HepMC3/Version.h' file not found |
| estarlight | failed | [run](https://github.com/hep-forge/estarlight-feedstock/actions/runs/41666919867) error: argument 'X' of type 'double[]' with mismatched bound [-Werror,-Warray-parameter] |
| hepmc-merger | failed | [run](https://github.com/hep-forge/hepmc-merger-feedstock/actions/runs/41666972479) CMake Error at CMakeLists.txt:25 (find_package): |
| thepeg | failed | [run](https://github.com/hep-forge/thepeg-feedstock/actions/runs/41670653035) No such file or directory |
| yoda | failed | [run](https://github.com/hep-forge/yoda-feedstock/actions/runs/41670662948) No such file or directory |
| acts | blocked | dd4hep |
| apfelgrid | blocked | applgrid |
| applgrid | blocked | fastnlo |
| epic | blocked | dd4hep |
| fastnlo | blocked | yoda |
| herwig7 | blocked | thepeg |
| npsim | blocked | dd4hep |
| professor | blocked | yoda |
| rapgap | blocked | rivet |
| rivet | blocked | yoda |
| xfitter | blocked | apfelgrid, applgrid |
| xfitter-dev | blocked | apfelgrid, applgrid |
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
| dyturbo | done |  |
| edm4hep | done |  |
| emela | done |  |
| escalade | done |  |
| fastjet | done |  |
| fastjet-contrib | done |  |
| framel | done |  |
| framel-root | done | built; channel not refreshed yet |
| g4hepem | done |  |
| geant | done | built; channel not refreshed yet |
| gosam | done |  |
| hathor | done |  |
| hell | done |  |
| hellx | done |  |
| hepmc | done |  |
| hoppet | done |  |
| inih | done |  |
| iregi | done |  |
| jana | done |  |
| jetphox | done |  |
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
