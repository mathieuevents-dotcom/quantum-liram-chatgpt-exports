# Atomic Properties External Dataset

- Source URL: https://raw.githubusercontent.com/Bluegrams/periodic-table-data/master/Periodica.Data/Data/ElementData.csv
- Access date: 2026-02-19
- Upstream project: https://github.com/Bluegrams/periodic-table-data
- License note: BSD 3-Clause (upstream `LICENSE`).

## Raw file
- `atomic_properties_raw.csv`

## Column definitions + units (clean output)
- `atomic_number` (int)
- `symbol` (str)
- `name` (str)
- `period` (int)
- `group` (int)
- `electronegativity_pauling` (Pauling scale, unitless)
- `ionization_energy_1` (eV)
  - converted from source `IonizationEnergy` in kJ/mol using `eV = kJ/mol * 0.01036427230133138`
- `atomic_radius` (pm)
  - source field: `AtomicRadius` (pm)
- `source_note` (str)

## Block Mapping Note

- Block column derived from local dataset `data/external/atomic_properties/atomic_properties_raw.csv`.
