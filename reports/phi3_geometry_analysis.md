# Phi3 Geometry Analysis

> [!NOTE]
> ## Data provenance
> - **Pourquoi `reports/phi3_projection.csv` manquait**: le dépôt ne contenait pas de stage dédié `phi3` ni de contrat de sortie imposant ce fichier. Le pipeline historique produisait des artefacts PCA/atomic props, mais pas de projection `phi3` nominale.
> - **Construction du seed dataset (valeurs, source, méthode)**: `phi3_projection.csv` est construit à partir de `reports/elements_pcs_atomicprops_merged.csv` (source locale), lui-même obtenu via `bash tools/run_atomicprops_analysis.sh` (`compute_element_pcs.py` + fusion avec `data/external/atomic_properties/atomic_properties_clean.csv`). La méthode applique `phi3 = sqrt(pc1^2 + pc2^2 + pc3^2)`, `radius_pc12 = sqrt(pc1^2 + pc2^2)`, puis un clustering déterministe en 3 quantiles (`C1/C2/C3`) sur le rang de `phi3`.
> - **Remplacement futur par des données réelles**: remplacer la source d'entrée par un export brut versionné (ex: `data/raw/...`) contenant les variables physiques d'origine; recalculer `pc1/pc2/pc3` avec la même procédure; conserver les mêmes noms de colonnes (`symbol`, `atomic_number`, `pc1`, `pc2`, `pc3`) pour garder `scripts/run_phi3.sh` compatible sans modification.

## Seed Policy
- Global seed used for this run: `42`
- `phi3_projection_shuffled.csv` is generated with deterministic permutation based on this seed.

## Dataset Summary
- Rows: `108`
- Phi3 mean: `2.076327`
- Phi3 std: `3.170959`
- Corr(phi3, pc1): `-0.323230`
- Corr(phi3, atomic_number): `-0.279060`
- Corr(phi3_shuffled, atomic_number): `-0.125259`

## Cluster Counts
- C1: `36`
- C2: `36`
- C3: `36`
