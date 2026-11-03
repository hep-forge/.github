# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 09:25 UTC.

failed: 2 · blocked: 6 · building: 8 · ready: 4 · waiting: 19 · done: 32 · n/a: 25

| Package | State | Detail |
|---|---|---|
| hell | failed | [run](https://github.com/hep-forge/hell-feedstock/actions/runs/41609734397) No such file or directory |
| hoppet | failed | [run](https://github.com/hep-forge/hoppet-feedstock/actions/runs/41609747060) error: no member named 'vector' in namespace 'std' |
| apfelgrid | blocked | applgrid |
| applgrid | blocked | fastnlo, hoppet |
| dyturbo | blocked | hell |
| fastnlo | blocked | hoppet |
| xfitter | blocked | apfelgrid, applgrid, dyturbo |
| xfitter-dev | blocked | apfelgrid, applgrid, dyturbo |
| djangoh | building | moved 4.6.21 to main 8faabaf |
| fastjet | building | moved 3.5.3 to main d5fddba |
| framel-root | building | moved 1.0.0 to main 0aaead5 |
| geant | building | moved 11.4.1 to main a72584e |
| iregi | building | [run](https://github.com/hep-forge/iregi-feedstock/actions/runs/41609753314) |
| jetphox | building | [run](https://github.com/hep-forge/jetphox-feedstock/actions/runs/41609758787) |
| nlojetxx | building | moved 4.1.3 to main f2ebd59 |
| nnlojet | building | moved 1.0.0 to main fdaa634 |
| pepper | ready |  |
| podio | ready |  |
| pythia | ready |  |
| yoda | ready |  |
| acts | waiting | dd4hep |
| afterburner | waiting | hepmc |
| dd4hep | waiting | edm4hep, g4hepem, geant, hepmc, podio |
| delphes | waiting | pythia |
| edm4hep | waiting | podio |
| eic-smear | waiting | hepmc |
| epic | waiting | dd4hep |
| estarlight | waiting | hepmc |
| fastjet-contrib | waiting | fastjet |
| g4hepem | waiting | geant |
| hepmc | waiting | pythia |
| hepmc-merger | waiting | hepmc |
| herwig7 | waiting | fastjet, thepeg |
| jana | waiting | podio |
| npsim | waiting | dd4hep |
| professor | waiting | yoda |
| rapgap | waiting | hepmc, pythia, rivet |
| rivet | waiting | fastjet, fastjet-contrib, hepmc, yoda |
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
| inih | done |  |
| kalman | done |  |
| kfrlib | done |  |
| lhapdf | done |  |
| libdate-tz | done | built; channel not refreshed yet |
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
