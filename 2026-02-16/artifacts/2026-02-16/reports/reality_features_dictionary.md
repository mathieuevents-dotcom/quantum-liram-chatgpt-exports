# Reality Features Dictionary

## Core
- `atomic_number`: Integer element index (1..118).
- `symbol`: Chemical symbol from Quantum table alignment.
- `atomic_mass`: Atomic mass from Quantum table alignment.

## Physico-Chemical
- `electronegativity`: Pauling-like electronegativity if available.
- `atomic_radius_pm`: Atomic radius in picometers.
- `covalent_radius_pm`: Covalent radius in picometers.
- `ionization_energy_ev`: First ionization energy in eV.
- `electron_affinity_ev`: Electron affinity in eV.
- `density_g_cm3`: Density in g/cm^3.
- `melting_point_k`: Melting point in Kelvin.
- `boiling_point_k`: Boiling point in Kelvin.
- `oxidation_states_count`: Count of known oxidation states.

## Spectroscopy
- `line_count_total`: Number of spectral lines available.
- `centroid_wavelength_nm`: Mean wavelength (intensity-weighted if intensity exists).
- `wavelength_std_nm`: Standard deviation of wavelengths.
- `entropy_over_bands`: Shannon entropy over fixed wavelength bands.
- `top_band`: Most populated wavelength band (uv/visible/nir/ir/fir).

## Vibrational (Optional Hook)
- `peak_count`: Number of vibrational peaks available.
- `centroid_cm-1`: Mean vibrational wavenumber (intensity-weighted if intensity exists).
- `std_cm-1`: Standard deviation of vibrational wavenumbers.
- `band_entropy`: Shannon entropy over low/mid/high vibrational bands.
