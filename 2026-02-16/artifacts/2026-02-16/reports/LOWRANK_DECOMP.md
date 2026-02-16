# Low-rank Decomposition

- matrix: covariance of padded layer matrix (Kmax=60)
- decomposition: eig/SVD; robust PCA not run (dependency-free mode)
- K@90% variance: 11
- K@95% variance: 13
- K@99% variance: 18
- residual energy at r=10: 0.101935
- residual energy at r=14: 0.034876
- residual energy at r=30: 0.000005

## Conclusion
- structure is compatible with a compact low-rank core plus additional refinements.
- information geometry only; no physical claim.
