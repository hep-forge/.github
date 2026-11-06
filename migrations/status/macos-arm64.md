# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-06 05:05 UTC.

failed: 3 · blocked: 9 · building: 1 · waiting: 2 · done: 56 · n/a: 25

| Package | State | Detail |
|---|---|---|
| delphes | failed | [run](https://github.com/hep-forge/delphes-feedstock/actions/runs/42160493774) Unsatisfiable dependencies for platform osx-arm64: {MatchSpec("pythia[version='>=8.3.12,<8.3.13.0a0']"), MatchSpec("root==6.38.04=py312_clang20")} |
| hepmc | failed | [run](https://github.com/hep-forge/hepmc-feedstock/actions/runs/42160511464) Unsatisfiable dependencies for platform osx-arm64: {MatchSpec("pythia[version='>=8.3.12,<8.3.13.0a0']"), MatchSpec("root==6.38.04=py312_clang20")} |
| root-plus | failed | [run](https://github.com/hep-forge/root-plus-feedstock/actions/runs/42160552045) Unsatisfiable dependencies for platform osx-arm64: {MatchSpec("macosx_deployment_target_osx-arm64=11.0"), MatchSpec("root==6.38.04=py312_clang20")} |
| afterburner | blocked | hepmc |
| dd4hep | blocked | hepmc |
| eic-smear | blocked | hepmc |
| escalade | blocked | root-plus |
| estarlight | blocked | hepmc |
| framel-root | blocked | root-plus |
| hepmc-merger | blocked | hepmc |
| rapgap | blocked | hepmc, rivet |
| rivet | blocked | hepmc |
| apfelgrid | building | moved 1.0.1 to main ef9aa9f |
| xfitter | waiting | apfelgrid |
| xfitter-dev | waiting | apfelgrid |
| acts | done |  |
| apfel | done |  |
| apfelxx | done |  |
| applgrid | done |  |
| chaplin | done |  |
| collier | done |  |
| combiner | done |  |
| covfie | done |  |
| cuba | done |  |
| cubature | done |  |
| curlpp | done |  |
| cuttools | done |  |
| difftop | done |  |
| djangoh | done |  |
| dyturbo | done |  |
| edm4hep | done |  |
| emela | done |  |
| epic | done |  |
| fastjet | done |  |
| fastjet-contrib | done |  |
| fastnlo | done |  |
| framel | done |  |
| g4hepem | done |  |
| geant | done |  |
| gosam | done |  |
| hathor | done |  |
| hell | done |  |
| hellx | done |  |
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
| npsim | done |  |
| numdiff | done |  |
| oneloop | done |  |
| pepper | done |  |
| pineappl | done |  |
| ploughshare | done |  |
| podio | done |  |
| professor | done |  |
| pythia | done |  |
| qcdnum | done |  |
| root | done |  |
| sz3 | done |  |
| thepeg | done |  |
| yoda | done |  |
| applfast | n/a | nothing published |
| cernlib | n/a | Linux only |
| eko | n/a | noarch |
| fairmq | n/a | Linux only |
| gaudi | n/a | Linux only |
| hammer | n/a | Linux only |
| herwig7 | n/a | Linux only |
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
| root-guard | n/a | noarch |
| roounfold | n/a | Linux only |
| scirooplot | n/a | Linux only |
| sherpa | n/a | Linux only |
| troll | n/a | Linux only |
| vgm | n/a | Linux only |
| vmc | n/a | Linux only |
| yadism | n/a | noarch |
