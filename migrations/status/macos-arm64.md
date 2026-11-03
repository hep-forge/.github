# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 21:43 UTC.

failed: 3 · blocked: 5 · building: 1 · waiting: 4 · done: 58 · n/a: 25

| Package | State | Detail |
|---|---|---|
| dd4hep | failed | [run](https://github.com/hep-forge/dd4hep-feedstock/actions/runs/41715229101) CMake Error at cmake/DD4hepBuild.cmake:72 (message): |
| fastjet-contrib | failed | [run](https://github.com/hep-forge/fastjet-contrib-feedstock/actions/runs/41721620887) error: use of undeclared identifier 'back_inserter' |
| herwig7 | failed | [run](https://github.com/hep-forge/herwig7-feedstock/actions/runs/41718542029) No such file or directory |
| acts | blocked | dd4hep |
| epic | blocked | dd4hep |
| npsim | blocked | dd4hep |
| rapgap | blocked | rivet |
| rivet | blocked | fastjet-contrib |
| fastnlo | building | moved 2.6.0 to main c0ab739 |
| apfelgrid | waiting | applgrid |
| applgrid | waiting | fastnlo |
| xfitter | waiting | apfelgrid, applgrid |
| xfitter-dev | waiting | apfelgrid, applgrid |
| afterburner | done |  |
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
| eic-smear | done |  |
| emela | done |  |
| escalade | done |  |
| estarlight | done |  |
| fastjet | done |  |
| framel | done |  |
| framel-root | done | built; channel not refreshed yet |
| g4hepem | done |  |
| geant | done |  |
| gosam | done |  |
| hathor | done |  |
| hell | done |  |
| hellx | done |  |
| hepmc | done |  |
| hepmc-merger | done |  |
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
| professor | done |  |
| pythia | done |  |
| qcdnum | done |  |
| root-plus | done |  |
| sz3 | done |  |
| thepeg | done |  |
| yoda | done |  |
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
