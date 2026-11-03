# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 11:06 UTC.

failed: 8 · blocked: 14 · building: 5 · waiting: 5 · done: 39 · n/a: 25

| Package | State | Detail |
|---|---|---|
| delphes | failed | [run](https://github.com/hep-forge/delphes-feedstock/actions/runs/41621710363) Unsatisfiable dependencies for platform osx-arm64: {MatchSpec("root==6.22.6=py38he9c1451_0"), MatchSpec("root_base==6.22.6=py38h1381eaf_0")} |
| djangoh | failed | [run](https://github.com/hep-forge/djangoh-feedstock/actions/runs/41616445733) CondaBuildUserError: TESTS FAILED: djangoh-4.6.21-h32763b8_0.conda |
| framel-root | failed | [run](https://github.com/hep-forge/framel-root-feedstock/actions/runs/41610885524) Error: /Users/runner/miniconda/conda-bld/framel-root_1793697974365/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeh |
| hell | failed | [run](https://github.com/hep-forge/hell-feedstock/actions/runs/41619092536) error: unknown type name 'pthread_mutex_t'; did you mean 'pthread_attr_t'? |
| hepmc | failed | [run](https://github.com/hep-forge/hepmc-feedstock/actions/runs/41621749351) Unsatisfiable dependencies for platform osx-arm64: {MatchSpec("root==6.38.00=py313h14255da_0"), MatchSpec("root_base==6.38.0=cxx20_h073445b_0")} |
| jetphox | failed | [run](https://github.com/hep-forge/jetphox-feedstock/actions/runs/41619108330) Error: HTTP 000 CONNECTION FAILED for url <https://lapth.cnrs.fr/PHOX_FAMILY/src/jetphox_1.3.1_4.tar.gz> |
| pepper | failed | [run](https://github.com/hep-forge/pepper-feedstock/actions/runs/41619131136) Error: Failed to download or patch source. Please see build log for info. |
| thepeg | failed | [run](https://github.com/hep-forge/thepeg-feedstock/actions/runs/41619152984) error: no member named 'mem_fun' in namespace 'std'; did you mean 'mem_fn'? |
| acts | blocked | dd4hep |
| afterburner | blocked | hepmc |
| dd4hep | blocked | hepmc |
| dyturbo | blocked | hell |
| eic-smear | blocked | hepmc |
| epic | blocked | dd4hep |
| estarlight | blocked | hepmc |
| hepmc-merger | blocked | hepmc |
| herwig7 | blocked | thepeg |
| npsim | blocked | dd4hep |
| rapgap | blocked | hepmc, rivet |
| rivet | blocked | hepmc |
| xfitter | blocked | dyturbo |
| xfitter-dev | blocked | dyturbo |
| fastjet-contrib | building | moved 1.105 to main 0e00958 |
| geant | building | moved 11.4.1 to main a72584e |
| jana | building | moved 2026.03.01 to main a1bc77d |
| lhapdf | building | moved 6.5.6 to main 53198d3 |
| yoda | building | moved 2.1.4 to main 8ebb17a |
| apfelgrid | waiting | applgrid, lhapdf |
| applgrid | waiting | fastnlo, lhapdf |
| fastnlo | waiting | lhapdf, yoda |
| g4hepem | waiting | geant |
| professor | waiting | yoda |
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
