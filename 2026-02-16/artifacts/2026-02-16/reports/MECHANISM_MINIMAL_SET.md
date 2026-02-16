# MECHANISM_MINIMAL_SET
- baseline: M5(lam=0.2, cascade_sigma=1.0, r_latent=4, Ktrue=37).
- ablations: no cascade, no latent, no long-range, no normalization-constraint proxy.
- law failure criteria: >15% degradation (directional) vs baseline on proxy metrics.

- baseline metrics: phi37=4.632220, cond=7.367793, sync37=0.600133, entropy37=2.601017
- strongest failure config: no_cascade_sigma0 (failed_laws=2)

## Component sensitivity
- no cascade: failed=2
- no latent: failed=2
- no long-range: failed=2
- no normalization-proxy: failed=1

- Guardrail: information geometry only; no physical claim.
