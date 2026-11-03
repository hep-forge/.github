# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 18:06 UTC.

failed: 3 · blocked: 4 · building: 3 · waiting: 5 · done: 56 · n/a: 25

| Package | State | Detail |
|---|---|---|
| estarlight | failed | [run](https://github.com/hep-forge/estarlight-feedstock/actions/runs/41686939043) error: unknown type name 'uint'; did you mean 'int'? |
| herwig7 | failed | [run](https://github.com/hep-forge/herwig7-feedstock/actions/runs/41680819372) No such file or directory |
| podio | failed | [run](https://github.com/hep-forge/podio-feedstock/actions/runs/41686977777) CMake Error at /Users/runner/miniconda/conda-bld/podio_1793727857226/_build_env/share/cmake-4.4/Modules/FindPackageHandleStandardArgs.cmake:290 (message): |
| acts | blocked | dd4hep |
| dd4hep | blocked | podio |
| epic | blocked | dd4hep |
| npsim | blocked | dd4hep |
| fastnlo | building | moved 2.6.0 to main c0ab739 |
| professor | building | moved 2.5.9 to main 9b5f0f8 |
| rivet | building | moved 4.1.3 to main 83e3efb |
| apfelgrid | waiting | applgrid |
| applgrid | waiting | fastnlo |
| rapgap | waiting | rivet |
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
| hepmc-merger | done |  |
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
| numdiff | done |  |
| oneloop | done |  |
| pepper | done |  |
| pineappl | done |  |
| ploughshare | done |  |
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
