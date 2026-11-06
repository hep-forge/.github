# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-06 05:24 UTC.

failed: 1 · blocked: 2 · building: 1 · waiting: 24 · done: 43 · n/a: 25

| Package | State | Detail |
|---|---|---|
| root-plus | failed | [run](https://github.com/hep-forge/root-plus-feedstock/actions/runs/42160552045) Unsatisfiable dependencies for platform osx-arm64: {MatchSpec("macosx_deployment_target_osx-arm64=11.0"), MatchSpec("root==6.38.04=py312_clang20")} |
| escalade | blocked | root-plus |
| framel-root | blocked | root-plus |
| root | building | [run](https://github.com/hep-forge/root-feedstock/actions/runs/42166939682) |
| acts | waiting | dd4hep, root |
| afterburner | waiting | hepmc, root |
| apfelgrid | waiting | applgrid, root |
| applgrid | waiting | fastnlo, root |
| combiner | waiting | root |
| dd4hep | waiting | edm4hep, hepmc, podio, root |
| delphes | waiting | root |
| edm4hep | waiting | podio |
| eic-smear | waiting | hepmc, root |
| epic | waiting | dd4hep, root |
| estarlight | waiting | hepmc |
| fastnlo | waiting | root, yoda |
| hepmc | waiting | root |
| hepmc-merger | waiting | hepmc, root |
| jana | waiting | podio, root |
| jetphox | waiting | root |
| npsim | waiting | dd4hep, root |
| podio | waiting | root |
| professor | waiting | yoda |
| rapgap | waiting | hepmc, rivet, root |
| rivet | waiting | hepmc, root, yoda |
| xfitter | waiting | apfelgrid, applgrid, root |
| xfitter-dev | waiting | apfelgrid, applgrid, root |
| yoda | waiting | root |
| apfel | done |  |
| apfelxx | done |  |
| chaplin | done |  |
| collier | done |  |
| covfie | done |  |
| cuba | done |  |
| cubature | done |  |
| curlpp | done |  |
| cuttools | done |  |
| difftop | done |  |
| djangoh | done |  |
| dyturbo | done |  |
| emela | done |  |
| fastjet | done |  |
| fastjet-contrib | done |  |
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
| pythia | done |  |
| qcdnum | done |  |
| sz3 | done |  |
| thepeg | done |  |
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
