# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 12:06 UTC.

failed: 12 · blocked: 18 · building: 1 · waiting: 1 · done: 39 · n/a: 25

| Package | State | Detail |
|---|---|---|
| delphes | failed | [run](https://github.com/hep-forge/delphes-feedstock/actions/runs/41621710363) Unsatisfiable dependencies for platform osx-arm64: {MatchSpec("root==6.22.6=py38he9c1451_0"), MatchSpec("root_base==6.22.6=py38h1381eaf_0")} |
| djangoh | failed | [run](https://github.com/hep-forge/djangoh-feedstock/actions/runs/41616445733) CondaBuildUserError: TESTS FAILED: djangoh-4.6.21-h32763b8_0.conda |
| fastjet-contrib | failed | [run](https://github.com/hep-forge/fastjet-contrib-feedstock/actions/runs/41627231536) Error: HTTP 000 CONNECTION FAILED for url <http://fastjet.hepforge.org/contrib/downloads/fjcontrib-1.105.tar.gz> |
| framel-root | failed | [run](https://github.com/hep-forge/framel-root-feedstock/actions/runs/41610885524) Error: /Users/runner/miniconda/conda-bld/framel-root_1793697974365/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeh |
| hell | failed | [run](https://github.com/hep-forge/hell-feedstock/actions/runs/41619092536) error: unknown type name 'pthread_mutex_t'; did you mean 'pthread_attr_t'? |
| hepmc | failed | [run](https://github.com/hep-forge/hepmc-feedstock/actions/runs/41621749351) Unsatisfiable dependencies for platform osx-arm64: {MatchSpec("root==6.38.00=py313h14255da_0"), MatchSpec("root_base==6.38.0=cxx20_h073445b_0")} |
| jana | failed | [run](https://github.com/hep-forge/jana-feedstock/actions/runs/41624688034) error: no member named 'nothrow' in namespace 'std' |
| jetphox | failed | [run](https://github.com/hep-forge/jetphox-feedstock/actions/runs/41619108330) Error: HTTP 000 CONNECTION FAILED for url <https://lapth.cnrs.fr/PHOX_FAMILY/src/jetphox_1.3.1_4.tar.gz> |
| lhapdf | failed | [run](https://github.com/hep-forge/lhapdf-feedstock/actions/runs/41624694438) CondaBuildUserError: TESTS FAILED: lhapdf-6.5.6-py312h70343ba_0.conda |
| pepper | failed | [run](https://github.com/hep-forge/pepper-feedstock/actions/runs/41619131136) Error: Failed to download or patch source. Please see build log for info. |
| thepeg | failed | [run](https://github.com/hep-forge/thepeg-feedstock/actions/runs/41619152984) error: no member named 'mem_fun' in namespace 'std'; did you mean 'mem_fn'? |
| yoda | failed | [run](https://github.com/hep-forge/yoda-feedstock/actions/runs/41624722714) error: linker command failed with exit code 1 (use -v to see invocation) |
| acts | blocked | dd4hep |
| afterburner | blocked | hepmc |
| apfelgrid | blocked | applgrid, lhapdf |
| applgrid | blocked | fastnlo, lhapdf |
| dd4hep | blocked | hepmc |
| dyturbo | blocked | hell, lhapdf |
| eic-smear | blocked | hepmc |
| epic | blocked | dd4hep |
| estarlight | blocked | hepmc |
| fastnlo | blocked | lhapdf, yoda |
| hepmc-merger | blocked | hepmc |
| herwig7 | blocked | lhapdf, thepeg |
| npsim | blocked | dd4hep |
| professor | blocked | yoda |
| rapgap | blocked | hepmc, lhapdf, rivet |
| rivet | blocked | fastjet-contrib, hepmc, yoda |
| xfitter | blocked | apfelgrid, applgrid, dyturbo, lhapdf |
| xfitter-dev | blocked | apfelgrid, applgrid, dyturbo, lhapdf |
| geant | building | moved 11.4.1 to main a72584e |
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
