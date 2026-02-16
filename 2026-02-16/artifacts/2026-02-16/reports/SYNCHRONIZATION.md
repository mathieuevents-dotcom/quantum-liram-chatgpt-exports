# SYNCHRONIZATION
- seed=42, K=1..60, n_perm(phase)=2000, n_perm(aux)=400, max_lag=2
- no_timeseries: proxy used with rows sorted by atomic number
- score S(K): average of adjacent and long-range max-lag cross-correlation (cumulative 1..K).
- S(21)=0.345862, S(37)=0.396730
- dS/dK at 21=0.017272, at 37=-0.016225
- strongest effect z=39.677, min empirical p=0.000500
- verdict: supported
- controls: shuffle_temporal_order, phase_randomized_surrogate, random matched-spectrum.
- Guardrail: information geometry only; no physical claim.
