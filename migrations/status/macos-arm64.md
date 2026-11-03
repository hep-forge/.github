# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 14:06 UTC.

failed: 7 · blocked: 20 · building: 1 · waiting: 1 · done: 42 · n/a: 25

| Package | State | Detail |
|---|---|---|
| delphes | failed | [run](https://github.com/hep-forge/delphes-feedstock/actions/runs/41646442050) error: no member named 'prev_permutation' in namespace 'std' |
| djangoh | failed | [run](https://github.com/hep-forge/djangoh-feedstock/actions/runs/41616445733) CondaBuildUserError: TESTS FAILED: djangoh-4.6.21-h32763b8_0.conda |
| framel-root | failed | [run](https://github.com/hep-forge/framel-root-feedstock/actions/runs/41646467428) error: ^[[0m^[[1mfile '/Users/runner/miniconda/conda-bld/framel-root_1793713279983/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_ |
| hepmc | failed | [run](https://github.com/hep-forge/hepmc-feedstock/actions/runs/41646475142) error: /Users/runner/miniconda/conda-bld/hepmc_1793713294877/_build_env/bin/arm64-apple-darwin20.0.0-install_name_tool: for: /Users/runner/miniconda/conda-bld/h |
| lhapdf | failed | [run](https://github.com/hep-forge/lhapdf-feedstock/actions/runs/41646483908) Segmentation fault: 11  python -c "import lhapdf; print(lhapdf.version())" |
| pepper | failed | [run](https://github.com/hep-forge/pepper-feedstock/actions/runs/41646496157) error: no member named 'getenv' in namespace 'std' |
| yoda | failed | [run](https://github.com/hep-forge/yoda-feedstock/actions/runs/41646514942) ld: framework not found -lz |
| acts | blocked | dd4hep |
| afterburner | blocked | hepmc |
| apfelgrid | blocked | applgrid, lhapdf |
| applgrid | blocked | fastnlo, lhapdf |
| dd4hep | blocked | hepmc |
| dyturbo | blocked | lhapdf |
| eic-smear | blocked | hepmc |
| epic | blocked | dd4hep |
| estarlight | blocked | hepmc |
| fastnlo | blocked | lhapdf, yoda |
| hepmc-merger | blocked | hepmc |
| herwig7 | blocked | lhapdf, thepeg |
| jetphox | blocked | lhapdf |
| npsim | blocked | dd4hep |
| professor | blocked | yoda |
| rapgap | blocked | hepmc, lhapdf, rivet |
| rivet | blocked | hepmc, yoda |
| thepeg | blocked | lhapdf |
| xfitter | blocked | apfelgrid, applgrid, dyturbo, lhapdf |
| xfitter-dev | blocked | apfelgrid, applgrid, dyturbo, lhapdf |
| geant | building | [run](https://github.com/hep-forge/geant-feedstock/actions/runs/41644315308) |
| g4hepem | waiting | geant |
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
| fastjet-contrib | done |  |
| framel | done |  |
| gosam | done |  |
| hathor | done |  |
| hell | done |  |
| hellx | done |  |
| hoppet | done |  |
| inih | done |  |
| iregi | done |  |
| jana | done |  |
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
