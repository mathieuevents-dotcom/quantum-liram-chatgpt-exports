# Calibration Sweep

## What was tested
Deterministic amplitude sweep to measure when information-geometry structure emerges in the 37-layer synthetic matrix under controlled signal injection.

## Parameters
- command: `python3 code/calibration_sweep.py`
- base_seed: `4200` (per amplitude seed = `4200 + idx`)
- N: `300`
- groups: `3`
- layers: `37`
- bands: `[(6,10), (22,27), (32,35)]`
- noise_sigma: `1.0`
- amplitudes: `[0.00, 0.05, 0.10, 0.15, 0.20, 0.30, 0.40, 0.60, 0.80, 1.00]`

## Results (key lines)

| amplitude | seed | pc1 | pc2 | pc3 | best_k | silhouette | non_nan_corr_count | top_abs_corr | robustness_mean |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 0.00 | 4200 | 0.045188 | 0.044168 | 0.043739 | 2 | 0.028038 | 111 | 0.164569 | 0.028302 |
| 0.05 | 4201 | 0.048049 | 0.044629 | 0.043563 | 2 | 0.029743 | 111 | 0.172270 | 0.030441 |
| 0.10 | 4202 | 0.046879 | 0.043516 | 0.042287 | 2 | 0.028373 | 111 | 0.174261 | 0.028917 |
| 0.15 | 4203 | 0.046343 | 0.042709 | 0.041445 | 2 | 0.026970 | 111 | 0.154759 | 0.027561 |
| 0.20 | 4204 | 0.048501 | 0.043152 | 0.042226 | 2 | 0.028595 | 111 | 0.152869 | 0.029343 |
| 0.30 | 4205 | 0.054662 | 0.044856 | 0.042752 | 2 | 0.034922 | 111 | 0.145158 | 0.035137 |
| 0.40 | 4206 | 0.079836 | 0.042214 | 0.041786 | 2 | 0.049381 | 111 | 0.145151 | 0.049014 |
| 0.60 | 4207 | 0.130370 | 0.044374 | 0.040528 | 2 | 0.084734 | 111 | 0.128777 | 0.086390 |
| 0.80 | 4208 | 0.223278 | 0.043347 | 0.040383 | 2 | 0.147301 | 111 | 0.108558 | 0.147736 |
| 1.00 | 4209 | 0.376351 | 0.042897 | 0.039776 | 2 | 0.233514 | 111 | 0.121861 | 0.234615 |

## Interpretation (information geometry only)
- Null control (`amplitude=0.00`) stays low on all main structure metrics (`pc1=0.045188`, `silhouette=0.028038`, `robustness=0.028302`), so no strong spurious structure was observed.
- Structure metrics scale upward with amplitude, with visible monotonic increase in `pc1_explained_variance_ratio`, `kmeans_silhouette`, and `robustness_silhouette_mean` over the upper half of the amplitude range.
- Correlation coverage stays constant (`111` finite values), indicating metric availability is stable across the sweep.
