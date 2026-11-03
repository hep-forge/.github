# Migration `macos-arm64`

platform `macos-arm64`, started 2026-11-03 02:37:00Z, updated 2026-11-03 10:44 UTC.

failed: 8 · blocked: 10 · building: 4 · waiting: 9 · done: 40 · n/a: 25

| Package | State | Detail |
|---|---|---|
| djangoh | failed | [run](https://github.com/hep-forge/djangoh-feedstock/actions/runs/41616445733) CondaBuildUserError: TESTS FAILED: djangoh-4.6.21-h32763b8_0.conda |
| framel-root | failed | [run](https://github.com/hep-forge/framel-root-feedstock/actions/runs/41610885524) Error: /Users/runner/miniconda/conda-bld/framel-root_1793697974365/_h_env_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placehold_placeh |
| hell | failed | [run](https://github.com/hep-forge/hell-feedstock/actions/runs/41619092536) error: unknown type name 'pthread_mutex_t'; did you mean 'pthread_attr_t'? |
| jana | failed | [run](https://github.com/hep-forge/jana-feedstock/actions/runs/41616493671) error: field has incomplete type 'std::exception_ptr' |
| jetphox | failed | [run](https://github.com/hep-forge/jetphox-feedstock/actions/runs/41619108330) Error: HTTP 000 CONNECTION FAILED for url <https://lapth.cnrs.fr/PHOX_FAMILY/src/jetphox_1.3.1_4.tar.gz> |
| pepper | failed | [run](https://github.com/hep-forge/pepper-feedstock/actions/runs/41619131136) Error: Failed to download or patch source. Please see build log for info. |
| thepeg | failed | [run](https://github.com/hep-forge/thepeg-feedstock/actions/runs/41619152984) error: no member named 'mem_fun' in namespace 'std'; did you mean 'mem_fn'? |
| yoda | failed | [run](https://github.com/hep-forge/yoda-feedstock/actions/runs/41616568458) Unsatisfiable dependencies for platform osx-arm64: {MatchSpec("root_base==6.38.0=cxx20_h073445b_0"), MatchSpec("root==6.38.00=py313h14255da_0")} |
| apfelgrid | blocked | applgrid |
| applgrid | blocked | fastnlo |
| dyturbo | blocked | hell |
| fastnlo | blocked | yoda |
| herwig7 | blocked | thepeg |
| professor | blocked | yoda |
| rapgap | blocked | rivet |
| rivet | blocked | yoda |
| xfitter | blocked | apfelgrid, applgrid, dyturbo |
| xfitter-dev | blocked | apfelgrid, applgrid, dyturbo |
| delphes | building | moved 3.5.1 to main 3d485b8 |
| fastjet-contrib | building | moved 1.105 to main 0e00958 |
| geant | building | [run](https://github.com/hep-forge/geant-feedstock/actions/runs/41619079150) |
| hepmc | building | moved 3.3.1 to main 1b01268 |
| acts | waiting | dd4hep |
| afterburner | waiting | hepmc |
| dd4hep | waiting | g4hepem, geant, hepmc |
| eic-smear | waiting | hepmc |
| epic | waiting | dd4hep |
| estarlight | waiting | hepmc |
| g4hepem | waiting | geant |
| hepmc-merger | waiting | hepmc |
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
| nnlojet | done | built; channel not refreshed yet |
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
