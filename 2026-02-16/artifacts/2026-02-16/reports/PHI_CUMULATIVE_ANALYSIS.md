# Phi Cumulative Analysis

- seed=42, K=1..60
- Phi-like metric: abs(off-diagonal covariance sum) / total variance on submatrix 1..K
- normalization: phi_norm = phi_raw / phi_shuffled (row-wise layer shuffle baseline)

## Regime-change candidates (local maxima of dPhi/dK)
- local maxima K: [5, 10, 15, 20, 25, 27, 31, 35, 43, 50, 53, 57]
- top derivative peaks K: [5, 15, 35, 31, 25, 27, 53, 10, 50, 20]

## Quick checks
- dPhi/dK at K=21: -0.066867
- dPhi/dK at K=37: -0.008372

- interpretation is structural/information-geometric only; no physical claim.
