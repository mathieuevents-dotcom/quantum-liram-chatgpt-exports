# Ablation Overview

## Reproducibility
- Input dataset: `data/extracted/elements_table.csv`
- Dataset SHA256: `00a17eb523e012b8a161a6af73731a3dbc26fab081ef40d7239468aba74a0df7`
- Random seed: `42`
- Permutations per experiment: `2000`

## Results
- Experiment A (labels from atomic_number+atomic_mass; test frequency): PASS
- Experiment B (labels from frequency; test categorical over-representation): FAIL
- Experiment C (labels from all numeric fields; predict from categorical): FAIL

## Pass/Fail Interpretation
- PASS means the experiment-specific criterion is met without using the same signal in both labeling and testing.
- Overall objective-evidence status: FAIL
