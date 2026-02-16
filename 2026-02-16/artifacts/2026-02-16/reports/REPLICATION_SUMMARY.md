# Replication Summary

## Local corpus search result
- Status: no independent spectroscopy-like corpus found locally.
- Current pipeline corpus (already used): `data/external/raw/` (NIST ASD HTML dumps).
- Additional spectroscopy-like directories found:
  - `data/external/nist_raw/` (empty directory)
  - `data/external/processed/nist_lines_parsed/` and `data/external/processed/nist_levels_parsed/` (derived outputs, not independent raw corpus)
- No `data/alt/`, `datasets/`, or second NIST mirror raw corpus with lines+levels HTML was found.

## Implemented replication interface
- Added drop-in dataset contract:
  - `data/replication_dataset/README.md`
- Added deterministic runner:
  - `scripts/run_replication_dataset.sh`
- Dataset switch variable:
  - `DATASET_ID` (default: `current`)

## Required format for independent dataset
- Place files under:
  - `data/replication_dataset/<DATASET_ID>/raw/`
- Required files:
  - lines HTML: `NIST ASD Output_ Lines_<SYMBOL> I.html` (spacing/underscore variants accepted)
  - levels HTML: `NIST ASD Levels Output_<SYMBOL> I.html`

## Current replication execution status
- `DATASET_ID=current`: script exits with guidance (non-zero).
- `DATASET_ID=<missing>`: script exits with clear error and required path.

## Pending comparison outputs
Because no independent local dataset is present, the following cannot be computed yet:
- best K by period metric on alternate corpus
- permutation p-values on alternate corpus
- stability metrics on alternate corpus
- top discriminant layers on alternate corpus
- local-optimum check for 37 on alternate corpus

## Next deterministic command (once dataset is added)
```bash
DATASET_ID=<YOUR_DATASET_ID> bash scripts/run_replication_dataset.sh
```

