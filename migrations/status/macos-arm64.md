# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 13:07 UTC.

failed: 3 · blocked: 5 · building: 8 · waiting: 16 · done: 39 · n/a: 25

| Package | State | Detail |
|---|---|---|
| djangoh | failed | [run](https://github.com/hep-forge/djangoh-feedstock/actions/runs/41616445733) CondaBuildUserError: TESTS FAILED: djangoh-4.6.21-h32763b8_0.conda |
| framel-root | failed | [run](https://github.com/hep-forge/framel-root-feedstock/actions/runs/41638115968) Error: /Users/runner/miniconda/conda-bld/framel-root_1793709849431/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeh |
| geant | failed | [run](https://github.com/hep-forge/geant-feedstock/actions/runs/41632952960) CondaBuildUserError: TESTS FAILED: geant-1!4.11.4.1-east.conda |
| acts | blocked | dd4hep |
| dd4hep | blocked | g4hepem, geant |
| epic | blocked | dd4hep |
| g4hepem | blocked | geant |
| npsim | blocked | dd4hep |
| delphes | building | moved 3.5.1 to main 040a7a4 |
| fastjet-contrib | building | moved 1.105 to main 19b41fa |
| hell | building | moved 3.1 to main 0575041 |
| hepmc | building | moved 3.3.1 to main 357200d |
| jana | building | moved 2026.03.01 to main 813a30b |
| lhapdf | building | moved 6.5.6 to main ac1c0ac |
| pepper | building | moved 1.14.1 to main 0aa00d5 |
| yoda | building | moved 2.1.4 to main 7c33318 |
| afterburner | waiting | hepmc |
| apfelgrid | waiting | applgrid, lhapdf |
| applgrid | waiting | fastnlo, lhapdf |
| dyturbo | waiting | hell, lhapdf |
| eic-smear | waiting | hepmc |
| estarlight | waiting | hepmc |
| fastnlo | waiting | lhapdf, yoda |
| hepmc-merger | waiting | hepmc |
| herwig7 | waiting | lhapdf, thepeg |
| jetphox | waiting | lhapdf |
| professor | waiting | yoda |
| rapgap | waiting | hepmc, lhapdf, rivet |
| rivet | waiting | fastjet-contrib, hepmc, yoda |
| thepeg | waiting | lhapdf |
| xfitter | waiting | apfelgrid, applgrid, dyturbo, lhapdf |
| xfitter-dev | waiting | apfelgrid, applgrid, dyturbo, lhapdf |
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
| difftop | done |  |
| edm4hep | done |  |
| emela | done |  |
| escalade | done |  |
| fastjet | done |  |
| framel | done |  |
| gosam | done |  |
| hathor | done |  |
| hellx | done |  |
| hoppet | done |  |
| inih | done |  |
| iregi | done |  |
| kalman | done |  |
| kfrlib | done |  |
| libdate-tz | done |  |
| looptools | done |  |
| minio-cpp | done |  |
| mpfun90 | done |  |
| nlojetxx | done |  |
| nnlojet | done |  |
| numdiff | done |  |
| oneloop | done |  |
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
