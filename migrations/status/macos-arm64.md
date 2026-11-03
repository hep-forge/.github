# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 19:25 UTC.

failed: 3 · blocked: 3 · building: 2 · waiting: 7 · done: 56 · n/a: 25

| Package | State | Detail |
|---|---|---|
| dd4hep | failed | [run](https://github.com/hep-forge/dd4hep-feedstock/actions/runs/41696687003) CMake Error at cmake/DD4hepBuild.cmake:72 (message): |
| estarlight | failed | [run](https://github.com/hep-forge/estarlight-feedstock/actions/runs/41699854952) error: variable 'nNonCriticalMissing' set but not used [-Werror,-Wunused-but-set-variable] |
| herwig7 | failed | [run](https://github.com/hep-forge/herwig7-feedstock/actions/runs/41699873358) error: use of undeclared identifier 'random_shuffle' |
| acts | blocked | dd4hep |
| epic | blocked | dd4hep |
| npsim | blocked | dd4hep |
| fastjet-contrib | building | moved 1.105, 1.103 to main 2a08431 |
| hoppet | building | moved 2.2.0, 1.2.0 to main c76b05a |
| apfelgrid | waiting | applgrid |
| applgrid | waiting | fastnlo, hoppet |
| fastnlo | waiting | hoppet |
| rapgap | waiting | rivet |
| rivet | waiting | fastjet-contrib |
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
