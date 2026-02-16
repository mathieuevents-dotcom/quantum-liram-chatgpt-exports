# Repro Commands

Use these exact commands from repo root:

```bash
export OMP_NUM_THREADS=1 MKL_NUM_THREADS=1 OPENBLAS_NUM_THREADS=1 VECLIB_MAXIMUM_THREADS=1 NUMEXPR_NUM_THREADS=1 PYTHONHASHSEED=42
bash scripts/run_all.sh
```

- Deterministic seed: `42`.
- Seed enforcement locations: pipeline and analysis scripts (`random_state=42` / `np.random.default_rng(42)` conventions) and `PYTHONHASHSEED=42` in command.
