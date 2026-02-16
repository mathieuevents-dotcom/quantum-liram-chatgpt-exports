# Generative Sweep

- seed=42, models=['M1', 'M2', 'M3'], lambda_grid=[0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]
- best model: M1 (lambda=0.1)
- best match score: 10.817879
- best vs real: erank 11.268 vs 11.129, alpha 1.599 vs 11.394, K90 9 vs 11
- best vs real dynamics: percolation K* 5 vs 5, modularity Kmax 45 vs 45

## Mechanism verdict
- minimal mechanism selected by lowest structural distance to real matrix.
- compare against shuffled/random controls in falsification step.
- Guardrail: information geometry only; no physical claim.
