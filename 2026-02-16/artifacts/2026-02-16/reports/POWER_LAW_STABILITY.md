# Power-law Stability

- seed=42, n_boot=500
- estimator: alpha from lambda_k = a * k^(-alpha) fit on covariance eigenspectrum (K=60 padded)

## Bootstrap CI95
- baseline alpha mean=11.526189, CI95=[11.338063, 11.703646]
- shuffled alpha mean=10.347051, CI95=[10.227629, 10.468815]
- random-matrix alpha mean=10.123905, CI95=[10.101994, 10.143326]

## Comparisons
- baseline vs shuffled: different, p_empirical=0.001996
- baseline vs random-matrix: different, p_empirical=0.001996

## Conclusion
- supported / weak-mixed / not supported should be based on CI separation + empirical p-values.
- information geometry only; no physical claim.
