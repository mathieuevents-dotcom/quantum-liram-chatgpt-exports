# Generative Sweep v3

- seed=42; models=M1,M2,M3,M4,M5; Ktrue=37; Kmax=60.
- best model: M5
- best config: {'model': 'M5', 'lam': 0.2, 'cascade_sigma': 1.0, 'r_latent': 4}
- best match score: 83.715184
- real vs best erank: 11.129 vs 14.099
- real vs best alpha: 11.394 vs 2.327
- real vs best K90/K95/K99: 11/13/18 vs 15/21/34
- real vs best percolation K*: 5 vs 5
- real vs best modularity Kmax: 45 vs 39

- score weights include tail explicitly: alpha, K99, and cumvar L2.
- information geometry only; no physical claim.
