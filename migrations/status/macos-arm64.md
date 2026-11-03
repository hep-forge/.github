# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 18:26 UTC.

failed: 2 · blocked: 5 · building: 3 · waiting: 4 · done: 57 · n/a: 25

| Package | State | Detail |
|---|---|---|
| fastnlo | failed | [run](https://github.com/hep-forge/fastnlo-feedstock/actions/runs/41690593739) Unsatisfiable dependencies for platform osx-arm64: {MatchSpec("yoda=1.9.9"), MatchSpec("hoppet=1.2.0")} |
| rivet | failed | [run](https://github.com/hep-forge/rivet-feedstock/actions/runs/41690660290) Unsatisfiable dependencies for platform osx-arm64: {MatchSpec("fastjet-contrib==1.103=h75d2b18_1")} |
| apfelgrid | blocked | applgrid |
| applgrid | blocked | fastnlo |
| rapgap | blocked | rivet |
| xfitter | blocked | apfelgrid, applgrid |
| xfitter-dev | blocked | apfelgrid, applgrid |
| estarlight | building | moved 1.2.0 to main 6992096 |
| herwig7 | building | moved 7.3.0 to main e6de32c |
| podio | building | moved 1.7.0 to main 16d86e4 |
| acts | waiting | dd4hep |
| dd4hep | waiting | podio |
| epic | waiting | dd4hep |
| npsim | waiting | dd4hep |
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
