# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 10:25 UTC.

failed: 4 · blocked: 8 · building: 8 · waiting: 13 · done: 38 · n/a: 25

| Package | State | Detail |
|---|---|---|
| djangoh | failed | [run](https://github.com/hep-forge/djangoh-feedstock/actions/runs/41616445733) CondaBuildUserError: TESTS FAILED: djangoh-4.6.21-h32763b8_0.conda |
| framel-root | failed | [run](https://github.com/hep-forge/framel-root-feedstock/actions/runs/41610885524) Error: /Users/runner/miniconda/conda-bld/framel-root_1793697974365/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeh |
| jana | failed | [run](https://github.com/hep-forge/jana-feedstock/actions/runs/41616493671) error: field has incomplete type 'std::exception_ptr' |
| yoda | failed | [run](https://github.com/hep-forge/yoda-feedstock/actions/runs/41616568458) Unsatisfiable dependencies for platform osx-arm64: {MatchSpec("root_base==6.38.0=cxx20_h073445b_0"), MatchSpec("root==6.38.00=py313h14255da_0")} |
| apfelgrid | blocked | applgrid |
| applgrid | blocked | fastnlo |
| fastnlo | blocked | yoda |
| professor | blocked | yoda |
| rapgap | blocked | rivet |
| rivet | blocked | yoda |
| xfitter | blocked | apfelgrid, applgrid |
| xfitter-dev | blocked | apfelgrid, applgrid |
| fastjet-contrib | building | moved 1.105 to main 0e00958 |
| geant | building | moved 11.4.1 to main a72584e |
| hell | building | moved 3.1 to main eea504f |
| jetphox | building | moved 1.3.1_4 to main 2511a9e |
| nnlojet | building | [run](https://github.com/hep-forge/nnlojet-feedstock/actions/runs/41610931735) |
| pepper | building | moved 1.14.1 to main 5fd171b |
| pythia | building | moved 8.3.12 to main bcf8338 |
| thepeg | building | moved 2.3.0 to main a45bf07 |
| acts | waiting | dd4hep |
| afterburner | waiting | hepmc |
| dd4hep | waiting | g4hepem, geant, hepmc |
| delphes | waiting | pythia |
| dyturbo | waiting | hell |
| eic-smear | waiting | hepmc |
| epic | waiting | dd4hep |
| estarlight | waiting | hepmc |
| g4hepem | waiting | geant |
| hepmc | waiting | pythia |
| hepmc-merger | waiting | hepmc |
| herwig7 | waiting | thepeg |
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
| lhapdf | done |  |
| libdate-tz | done |  |
| looptools | done |  |
| minio-cpp | done |  |
| mpfun90 | done |  |
| nlojetxx | done |  |
| numdiff | done |  |
| oneloop | done |  |
| pineappl | done |  |
| ploughshare | done |  |
| podio | done |  |
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
