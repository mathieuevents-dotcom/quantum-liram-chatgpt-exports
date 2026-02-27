# Phi3 End-to-End Repro

## Prerequisites
- Python 3.11 (recommended; 3.10+ should work)
- `pip` available from your Python install

## Installation
```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```

## One-Command Reproduction
```bash
bash scripts/run_phi3.sh
```

## Outputs
Main outputs are generated in:
- `reports/overview.html` (central overview)
- `reports/phi3_projection.csv`
- `reports/phi3_projection_shuffled.csv`
- `reports/phi3_geometry_analysis.md`
- `figures/phi3_cluster_labeled.svg`

Additional intermediate artifacts are produced under `reports/` and `reports/figures/` by the upstream analysis scripts.

## Seed Policy
- Global seed is fixed to `42` by default in `scripts/run_phi3.sh` (`SEED=${SEED:-42}`).
- The seed is passed to `tools/generate_phi3_outputs.py --seed <SEED>`.
- Deterministic randomness is implemented with `numpy.random.default_rng(seed)` for shuffle generation.
- To override while staying deterministic:
  ```bash
  SEED=123 bash scripts/run_phi3.sh
  ```

## Data Provenance
> [!NOTE]
> - **Pourquoi `reports/phi3_projection.csv` manquait**: il n'existait pas de phase `phi3` dédiée dans le pipeline, donc aucun artefact `phi3_projection.csv` n'était garanti.
> - **Construction du seed dataset (valeurs, source, méthode)**: le fichier est généré depuis `reports/elements_pcs_atomicprops_merged.csv`, produit par `bash tools/run_atomicprops_analysis.sh` à partir des features spectrales locales et de `data/external/atomic_properties/atomic_properties_clean.csv`. Les valeurs `phi3` sont calculées par `sqrt(pc1^2 + pc2^2 + pc3^2)`, puis un clustering déterministe en 3 quantiles (`C1/C2/C3`) est appliqué.
> - **Remplacement par des données réelles**: injecter un dataset source versionné (ex: `data/raw/...`) avec les variables d'origine, recalculer `pc1/pc2/pc3` avec la même méthode, et conserver les colonnes `symbol`, `atomic_number`, `pc1`, `pc2`, `pc3` pour garder le runner `bash scripts/run_phi3.sh` compatible.
