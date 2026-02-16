# Percolation Controls

- seed=42, n_perm=2000
- controls: shuffle_temporal_order, phase_randomized_surrogate
- p-values from positional permutation null on transition score profiles

## p-values
- K≈21 vs shuffle control: p=0.553723
- K≈21 vs phase control: p=0.516242
- K*=11 vs shuffle control: p=0.056972
- K*=11 vs phase control: p=0.021489

## Control interpretation
- Smaller p indicates baseline transition score exceeds control-null expectation at that K.
- Compare K≈21 against K* to assess whether 21 is dominant or secondary.
