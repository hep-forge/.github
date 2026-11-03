# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 15:44 UTC.

failed: 3 · blocked: 9 · building: 5 · waiting: 3 · done: 51 · n/a: 25

| Package | State | Detail |
|---|---|---|
| jetphox | failed | [run](https://github.com/hep-forge/jetphox-feedstock/actions/runs/41663727977) ld: file not found: /Users/runner/miniconda/conda-bld/jetphox_1793719570984/_test_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_plac |
| thepeg | failed | [run](https://github.com/hep-forge/thepeg-feedstock/actions/runs/41663761347) Undefined symbols for architecture arm64: |
| yoda | failed | [run](https://github.com/hep-forge/yoda-feedstock/actions/runs/41663774495) ld: framework not found -lz |
| apfelgrid | blocked | applgrid |
| applgrid | blocked | fastnlo |
| fastnlo | blocked | yoda |
| herwig7 | blocked | thepeg |
| professor | blocked | yoda |
| rapgap | blocked | rivet |
| rivet | blocked | yoda |
| xfitter | blocked | apfelgrid, applgrid |
| xfitter-dev | blocked | apfelgrid, applgrid |
| afterburner | building | moved 0.2.1 to main d449630 |
| dd4hep | building | moved 1.37 to main eec505e |
| eic-smear | building | moved 1.2.3 to main 4fecb41 |
| estarlight | building | moved 1.2.0 to main a9227c8 |
| hepmc-merger | building | moved 2.4.0 to main d791b03 |
| acts | waiting | dd4hep |
| epic | waiting | dd4hep |
| npsim | waiting | dd4hep |
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
