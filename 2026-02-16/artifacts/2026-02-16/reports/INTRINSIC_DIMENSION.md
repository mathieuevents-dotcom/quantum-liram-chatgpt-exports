# Intrinsic Dimension

- seed=42, n_perm=1000
- estimators: participation ratio, effective rank, Levina-Bickel MLE
- systems: baseline K=1..60 padded, baseline K<=37 truncated, shuffled controls

## Core statistics (baseline full K=1..60)
- saturation_score_near_37 (effective_rank slope pre37-post37): 0.155549
- p_value_saturation (perm control): 1.000000
- spectral_gap_prominence_at_37: -0.617122
- p_value_gap37 (perm control): 0.998002

## Decisions
- Intrinsic dimension saturating near K≈37: weak-mixed
- Spectral gap near K≈37: not supported

## Guardrail
- information geometry only; no physical claim.
