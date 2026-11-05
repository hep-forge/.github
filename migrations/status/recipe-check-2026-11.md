# Migration `recipe-check-2026-11`

rebuild, started 2026-11-05 07:09:33Z, updated 2026-11-05 08:06 UTC.

failed: 1 · blocked: 9 · building: 3 · waiting: 2 · done: 12

| Package | State | Detail |
|---|---|---|
| pythia | failed | [run](https://github.com/hep-forge/pythia-feedstock/actions/runs/41989326125) Unsatisfiable dependencies for platform linux-aarch64: {MatchSpec("gxx_linux-aarch64=14[build='^14.*$']"), MatchSpec("gcc_linux-aarch64=14[build='^14.*$']"), Ma |
| acts | blocked | dd4hep |
| dd4hep | blocked | hepmc |
| eic-smear | blocked | hepmc |
| epic | blocked | dd4hep |
| estarlight | blocked | hepmc |
| hepmc | blocked | pythia |
| hepmc-merger | blocked | hepmc |
| npsim | blocked | dd4hep |
| rapgap | blocked | hepmc, pythia |
| applgrid | building | moved 1.6.49 to main b360078 |
| geant | building | [run](https://github.com/hep-forge/geant-feedstock/actions/runs/41987139892) |
| thepeg | building | moved 2.3.0 to main 8aab09c |
| g4hepem | waiting | geant |
| xfitter | waiting | applgrid |
| apfel | done |  |
| djangoh | done |  |
| fastjet | done |  |
| fastnlo | done |  |
| framel-root | done |  |
| hell | done |  |
| hellx | done |  |
| jetphox | done |  |
| lhapdf | done |  |
| nlojetxx | done |  |
| numdiff | done |  |
| podio | done |  |
