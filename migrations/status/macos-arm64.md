# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 09:17 UTC.

failed: 3 · blocked: 5 · building: 8 · ready: 6 · waiting: 20 · done: 29 · n/a: 25

| Package | State | Detail |
|---|---|---|
| djangoh | failed | [run](https://github.com/hep-forge/djangoh-feedstock/actions/runs/41608285136) No such file or directory |
| framel-root | failed | [run](https://github.com/hep-forge/framel-root-feedstock/actions/runs/41608307988) BuildScriptException: Command '['/bin/bash', '-o', 'errexit', '/Users/runner/miniconda/conda-bld/framel-root_1793696831142/work/conda_build.sh']' returned non-z |
| geant | failed | [run](https://github.com/hep-forge/geant-feedstock/actions/runs/41608314259) BuildScriptException: Command '['/bin/bash', '-o', 'errexit', '/Users/runner/miniconda/conda-bld/geant_1793696852441/work/conda_build.sh']' returned non-zero ex |
| acts | blocked | dd4hep |
| dd4hep | blocked | g4hepem, geant |
| epic | blocked | dd4hep |
| g4hepem | blocked | geant |
| npsim | blocked | dd4hep |
| fastjet | building | moved 3.5.3 to main d5fddba |
| gosam | building | [run](https://github.com/hep-forge/gosam-feedstock/actions/runs/41608319344) |
| hell | building | moved 3.1 to main 3935159 |
| hellx | building | moved 3.0 to main bb0e250 |
| hoppet | building | moved 2.2.0 to main 1b36ceb |
| iregi | building | moved 1.1.0 to main 85e37ca |
| jetphox | building | moved 1.3.1_4 to main 2511a9e |
| libdate-tz | building | moved 3.0.5 to main b88eb2e |
| nlojetxx | ready |  |
| nnlojet | ready |  |
| pepper | ready |  |
| podio | ready |  |
| pythia | ready |  |
| yoda | ready |  |
| afterburner | waiting | hepmc |
| apfelgrid | waiting | applgrid |
| applgrid | waiting | fastnlo, hoppet |
| delphes | waiting | pythia |
| dyturbo | waiting | hell, hellx |
| edm4hep | waiting | podio |
| eic-smear | waiting | hepmc |
| estarlight | waiting | hepmc |
| fastjet-contrib | waiting | fastjet |
| fastnlo | waiting | fastjet, hoppet, yoda |
| hepmc | waiting | pythia |
| hepmc-merger | waiting | hepmc |
| herwig7 | waiting | fastjet, thepeg |
| jana | waiting | podio |
| professor | waiting | yoda |
| rapgap | waiting | hepmc, pythia, rivet |
| rivet | waiting | fastjet, fastjet-contrib, hepmc, yoda |
| thepeg | waiting | fastjet |
| xfitter | waiting | apfelgrid, applgrid, dyturbo |
| xfitter-dev | waiting | apfelgrid, applgrid, dyturbo |
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
| hathor | done |  |
| inih | done |  |
| kalman | done |  |
| kfrlib | done |  |
| lhapdf | done |  |
| looptools | done |  |
| minio-cpp | done |  |
| mpfun90 | done |  |
| numdiff | done |  |
| oneloop | done |  |
| pineappl | done |  |
| ploughshare | done |  |
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
