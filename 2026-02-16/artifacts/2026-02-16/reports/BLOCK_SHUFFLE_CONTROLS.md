# Block Shuffle Controls

- blocks: [1..10],[11..20],[21..30],[31..40],[41..60]
- controls: shuffle within each block; permute blocks as units

## Structural scores comparison
```text
            condition  percolation_k_star  modularity_k_max  fusion_event_k  alpha_mean  alpha_ci95_low  alpha_ci95_high
             baseline                  11                45               1   11.518906       11.350558        11.693322
shuffle_within_blocks                  28                16               1    9.587514        9.450707         9.714407
  permute_block_order                  15                32               1   11.518906       11.350558        11.693321
```

## Conclusion
- large deviations vs baseline indicate dependence on cross-block ordering/coupling.
- information geometry only; no physical claim.
