# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 10:07 UTC.

failed: 4 · blocked: 15 · building: 8 · waiting: 8 · done: 36 · n/a: 25

| Package | State | Detail |
|---|---|---|
| framel-root | failed | [run](https://github.com/hep-forge/framel-root-feedstock/actions/runs/41610885524) Error: /Users/runner/miniconda/conda-bld/framel-root_1793697974365/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeh |
| hell | failed | [run](https://github.com/hep-forge/hell-feedstock/actions/runs/41613447201) error: no member named 'terminate' in namespace 'std'; did you mean 'template'? |
| pepper | failed | [run](https://github.com/hep-forge/pepper-feedstock/actions/runs/41613486824) BuildScriptException: Command '['/bin/bash', '-o', 'errexit', '/Users/runner/miniconda/conda-bld/pepper_1793699635560/work/conda_build.sh']' returned non-zero e |
| pythia | failed | [run](https://github.com/hep-forge/pythia-feedstock/actions/runs/41613497895) error: linker command failed with exit code 1 (use -v to see invocation) |
| acts | blocked | dd4hep |
| afterburner | blocked | hepmc |
| dd4hep | blocked | hepmc |
| delphes | blocked | pythia |
| dyturbo | blocked | hell |
| eic-smear | blocked | hepmc |
| epic | blocked | dd4hep |
| estarlight | blocked | hepmc |
| hepmc | blocked | pythia |
| hepmc-merger | blocked | hepmc |
| npsim | blocked | dd4hep |
| rapgap | blocked | hepmc, pythia, rivet |
| rivet | blocked | hepmc |
| xfitter | blocked | dyturbo |
| xfitter-dev | blocked | dyturbo |
| djangoh | building | moved 4.6.21 to main b922735 |
| edm4hep | building | moved 1.0.0 to main 81a70e2 |
| fastjet | building | moved 3.5.3 to main 117d9db |
| geant | building | [run](https://github.com/hep-forge/geant-feedstock/actions/runs/41610892109) |
| jana | building | moved 2026.03.01 to main 33af1e2 |
| jetphox | building | moved 1.3.1_4 to main 2511a9e |
| nnlojet | building | [run](https://github.com/hep-forge/nnlojet-feedstock/actions/runs/41610931735) |
| yoda | building | moved 2.1.4 to main 2c7ebbd |
| apfelgrid | waiting | applgrid |
| applgrid | waiting | fastnlo |
| fastjet-contrib | waiting | fastjet |
| fastnlo | waiting | fastjet, yoda |
| g4hepem | waiting | geant |
| herwig7 | waiting | fastjet, thepeg |
| professor | waiting | yoda |
| thepeg | waiting | fastjet |
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
| emela | done |  |
| escalade | done |  |
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
