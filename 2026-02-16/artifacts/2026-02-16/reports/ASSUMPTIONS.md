# Assumptions

- Dataset scope: local NIST ASD HTML exports found in `data/external/raw`.
- Feature construction fallback: log-spaced histogram bands over valid positive frequencies.
- ANOVA fallback: one-way F-statistic computed directly from sums of squares (no SciPy dependency).
- Periodicity strength: max DFT power near periods 2, 8, 18, 32.
- Missing property columns (electronegativity, ionization, radius) remain missing in local table.
- Inventory rows: 205
