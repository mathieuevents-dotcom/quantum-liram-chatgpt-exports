# Kmax Extension Test

- K=1..60, variants: zeros / deterministic-noise / copy-last-layer

- padding_zeros: k*=1, H2(K≈37)=weak-mixed, pre_slope=0.0197173, post_slope=0.00175907
- padding_noise_deterministic: k*=1, H2(K≈37)=weak-mixed, pre_slope=0.0197261, post_slope=0.00382457
- padding_copy_last_layer: k*=1, H2(K≈37)=not supported, pre_slope=0.0195406, post_slope=0.0137988

## Conclusion
- Plateau-vs-saturation judged by consistency across the 3 padding variants.
- information geometry only; no physical claim.
