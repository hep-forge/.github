# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 16:05 UTC.

failed: 5 · blocked: 3 · building: 3 · waiting: 9 · done: 51 · n/a: 25

| Package | State | Detail |
|---|---|---|
| afterburner | failed | [run](https://github.com/hep-forge/afterburner-feedstock/actions/runs/41666854453) CMake Error at CMakeLists.txt:17 (find_package): |
| dd4hep | failed | [run](https://github.com/hep-forge/dd4hep-feedstock/actions/runs/41666878679) CMake Error at /Users/runner/miniconda/conda-bld/dd4hep_1793720680040/_build_env/share/cmake-4.4/Modules/FindPackageHandleStandardArgs.cmake:290 (message): |
| eic-smear | failed | [run](https://github.com/hep-forge/eic-smear-feedstock/actions/runs/41666907839) error: 'HepMC3/Version.h' file not found |
| estarlight | failed | [run](https://github.com/hep-forge/estarlight-feedstock/actions/runs/41666919867) error: argument 'X' of type 'double[]' with mismatched bound [-Werror,-Warray-parameter] |
| hepmc-merger | failed | [run](https://github.com/hep-forge/hepmc-merger-feedstock/actions/runs/41666972479) CMake Error at CMakeLists.txt:25 (find_package): |
| acts | blocked | dd4hep |
| epic | blocked | dd4hep |
| npsim | blocked | dd4hep |
| jetphox | building | moved 1.3.1_4 to main f0bbb7c |
| thepeg | building | moved 2.3.0 to main 7c264b8 |
| yoda | building | moved 2.1.4 to main 49dc26a |
| apfelgrid | waiting | applgrid |
| applgrid | waiting | fastnlo |
| fastnlo | waiting | yoda |
| herwig7 | waiting | thepeg |
| professor | waiting | yoda |
| rapgap | waiting | rivet |
| rivet | waiting | yoda |
| xfitter | waiting | apfelgrid, applgrid |
| xfitter-dev | waiting | apfelgrid, applgrid |
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
