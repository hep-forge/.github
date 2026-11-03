# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 19:05 UTC.

failed: 3 · blocked: 8 · building: 5 · done: 55 · n/a: 25

| Package | State | Detail |
|---|---|---|
| dd4hep | failed | [run](https://github.com/hep-forge/dd4hep-feedstock/actions/runs/41696687003) CMake Error at cmake/DD4hepBuild.cmake:72 (message): |
| fastnlo | failed | [run](https://github.com/hep-forge/fastnlo-feedstock/actions/runs/41690593739) Unsatisfiable dependencies for platform osx-arm64: {MatchSpec("yoda=1.9.9"), MatchSpec("hoppet=1.2.0")} |
| rivet | failed | [run](https://github.com/hep-forge/rivet-feedstock/actions/runs/41690660290) Unsatisfiable dependencies for platform osx-arm64: {MatchSpec("fastjet-contrib==1.103=h75d2b18_1")} |
| acts | blocked | dd4hep |
| apfelgrid | blocked | applgrid |
| applgrid | blocked | fastnlo |
| epic | blocked | dd4hep |
| npsim | blocked | dd4hep |
| rapgap | blocked | rivet |
| xfitter | blocked | apfelgrid, applgrid |
| xfitter-dev | blocked | apfelgrid, applgrid |
| estarlight | building | moved 1.2.0 to main cb241c5 |
| fastjet-contrib | building | moved 1.105, 1.103 to main 2a08431 |
| herwig7 | building | moved 7.3.0 to main d7ef6d2 |
| hoppet | building | moved 2.2.0, 1.2.0 to main c76b05a |
| yoda | building | moved 2.1.4, 1.9.9 to main f125746 |
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
