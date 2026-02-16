# PSY Law

This file defines a deterministic statistical scaffold only.

## Definitions
- `phi_plus_k = max(psi_k, 0)`
- `phi_minus_k = max(-psi_k, 0)`
- `phi_zero_k = exp(-|psi_k| / eps_zero)`
- `psi_t = sigmoid(mean(psi)) in [0,1]`
- `L6_psy_triad = eta_plus<phi+_A,phi+_B> + eta_minus<phi-_A,phi-_B> + eta_zero<phi0_A,phi0_B>`
- `L7_psy_triad_dynamic = L6 + eta_dyn * psi_t(A)*psi_t(B) * (<phi+_A,phi+_B> + <phi-_A,phi-_B> + 0.5<phi0_A,phi0_B>)`

## Parameters
- seed=42
- eta_plus=1.0, eta_minus=1.0, eta_zero=1.0, eta_dyn=0.5, eps_zero=0.25
- band weights: deterministic Ridge-to-Z absolute coefficients reused from ladder benchmark

## Note
- This is a benchmark test scaffold. No physical claim is made from these scores.
