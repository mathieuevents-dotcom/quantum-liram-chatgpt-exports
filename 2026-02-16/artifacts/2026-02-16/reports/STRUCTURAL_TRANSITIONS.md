# Structural Transitions

- seed=42, K range=10..60
- metrics: spectral_norm, eigen_entropy, effective_rank, modularity
- plots: reports/figures/structural_transition_*.svg (no smoothing)

## Event detection summary
- spectral_norm: {'inflection_points': [13, 15, 16, 17, 19, 20, 21, 22, 23, 27, 28, 30, 31, 32, 33, 34, 35, 36], 'second_derivative_sign_changes': [13, 15, 16, 17, 19, 20, 21, 22, 23, 27, 28, 30, 31, 32, 33, 34, 35, 36], 'abrupt_shifts': [26, 27, 30, 31, 32]}
- eigen_entropy: {'inflection_points': [14, 16, 18, 20, 22, 23, 24, 25, 27, 28, 29, 31, 32, 33, 35, 36], 'second_derivative_sign_changes': [14, 16, 18, 20, 22, 23, 24, 25, 27, 28, 29, 31, 32, 33, 35, 36], 'abrupt_shifts': [11, 12]}
- effective_rank: {'inflection_points': [14, 16, 18, 21, 22, 23, 24, 25, 27, 28, 29, 31, 32, 33, 35, 36], 'second_derivative_sign_changes': [14, 16, 18, 21, 22, 23, 24, 25, 27, 28, 29, 31, 32, 33, 35, 36], 'abrupt_shifts': [11, 12, 19, 20, 21]}
- modularity: {'inflection_points': [12, 13, 14, 15, 16, 17, 19, 21, 22, 25, 27, 28, 29, 31, 32, 34, 36, 37], 'second_derivative_sign_changes': [12, 13, 14, 15, 16, 17, 19, 21, 22, 25, 27, 28, 29, 31, 32, 34, 36, 37], 'abrupt_shifts': [11, 15, 16]}

## Transition questions
- Structural transition near K=21: WEAK/MIXED (not a dominant regime break)
- Structural transition near K=37: YES (plateau onset zone)
- Most recurrent transition K values: [(16, 5), (27, 5), (31, 5), (32, 5), (21, 4), (22, 4)]

## Statistical conclusion
- Around K=21: secondary transition-like flags exist but are not the dominant regime shift.
- Around K=37: transition flags coincide with onset of a plateau from K>=37.
- Strongest regime-shift zone appears in late-20s to mid-30s (rapid growth before plateau).
