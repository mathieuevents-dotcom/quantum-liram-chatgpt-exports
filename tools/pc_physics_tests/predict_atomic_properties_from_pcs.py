#!/usr/bin/env python3
from pathlib import Path
import json

import numpy as np
import pandas as pd
from scipy.stats import spearmanr
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, r2_score

SEED = 20260220
np.random.seed(SEED)

INP = Path('reports/elements_pcs_atomicprops_merged.csv')
OUT_SUMMARY_CSV = Path('reports/pc_physics_tests/property_prediction_summary.csv')
OUT_DETAILS_CSV = Path('reports/pc_physics_tests/property_prediction_details.csv')
OUT_JSON = Path('reports/pc_physics_tests/property_prediction_summary.json')

PROPERTY_CANDIDATES = {
    'ionization_energy_1': ['ionization_energy_1', 'ionization_energy', 'first_ionization_energy'],
    'electronegativity_pauling': ['electronegativity_pauling', 'electronegativity'],
    'atomic_radius': ['atomic_radius', 'atomic_radius_pm', 'radius'],
}

MODELS = {
    'M1_pcs': ['pc1', 'pc2', 'pc3'],
    'M2_atomic_number': ['atomic_number'],
    'M3_period_group': ['period', 'group'],
    'M4_atomic_number_period_group': ['atomic_number', 'period', 'group'],
}


def resolve_property(df, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    return None


def eval_fold(train_df, test_df, features, target):
    Xtr = train_df[features].to_numpy(float)
    ytr = train_df[target].to_numpy(float)
    Xte = test_df[features].to_numpy(float)
    yte = test_df[target].to_numpy(float)

    model = LinearRegression()
    model.fit(Xtr, ytr)
    pred = model.predict(Xte)

    r2 = np.nan
    if len(yte) >= 2:
        r2 = r2_score(yte, pred)
    mae = mean_absolute_error(yte, pred)
    sr, sp = (np.nan, np.nan)
    if len(yte) >= 2:
        sr, sp = spearmanr(yte, pred)

    return {
        'n_train': int(len(train_df)),
        'n_test': int(len(test_df)),
        'r2': float(r2) if np.isfinite(r2) else np.nan,
        'mae': float(mae),
        'spearman_rho': float(sr) if np.isfinite(sr) else np.nan,
        'spearman_p': float(sp) if np.isfinite(sp) else np.nan,
    }


def summarize_metric(values):
    v = np.array(values, dtype=float)
    v = v[np.isfinite(v)]
    if len(v) == 0:
        return np.nan, np.nan
    return float(np.mean(v)), float(np.std(v, ddof=0))


def main():
    if not INP.exists():
        raise FileNotFoundError(INP)
    df = pd.read_csv(INP)

    for c in set(sum(MODELS.values(), [])) | {'period'}:
        if c in df.columns:
            df[c] = pd.to_numeric(df[c], errors='coerce')

    property_map = {}
    for pname, cands in PROPERTY_CANDIDATES.items():
        col = resolve_property(df, cands)
        if col is not None:
            property_map[pname] = col

    details = []
    summary = []
    json_payload = {'input': str(INP), 'models': MODELS, 'properties': {}}

    for prop_name, prop_col in property_map.items():
        json_payload['properties'][prop_name] = {'source_column': prop_col, 'models': {}}

        for model_name, feats in MODELS.items():
            need_cols = list(dict.fromkeys(feats + [prop_col, 'period']))
            d = df[need_cols].dropna().copy()
            d['period'] = d['period'].astype(int)
            periods = sorted(d['period'].unique().tolist())

            fold_rows = []
            for p in periods:
                te = d[d['period'] == p]
                tr = d[d['period'] != p]
                if len(te) == 0 or len(tr) < max(5, len(feats) + 1):
                    continue
                r = eval_fold(tr, te, feats, prop_col)
                row = {
                    'property': prop_name,
                    'source_column': prop_col,
                    'model': model_name,
                    'features': '|'.join(feats),
                    'heldout_period': int(p),
                    **r,
                }
                fold_rows.append(row)
                details.append(row)

            n_folds = len(fold_rows)
            r2_mean, r2_std = summarize_metric([r['r2'] for r in fold_rows])
            mae_mean, mae_std = summarize_metric([r['mae'] for r in fold_rows])
            sp_mean, sp_std = summarize_metric([r['spearman_rho'] for r in fold_rows])

            srow = {
                'property': prop_name,
                'source_column': prop_col,
                'model': model_name,
                'features': '|'.join(feats),
                'n_folds': int(n_folds),
                'r2_mean': r2_mean,
                'r2_std': r2_std,
                'mae_mean': mae_mean,
                'mae_std': mae_std,
                'spearman_rho_mean': sp_mean,
                'spearman_rho_std': sp_std,
            }
            summary.append(srow)

            json_payload['properties'][prop_name]['models'][model_name] = {
                'features': feats,
                'n_folds': int(n_folds),
                'metrics': {
                    'r2_mean': r2_mean,
                    'r2_std': r2_std,
                    'mae_mean': mae_mean,
                    'mae_std': mae_std,
                    'spearman_rho_mean': sp_mean,
                    'spearman_rho_std': sp_std,
                },
                'folds': fold_rows,
            }

    OUT_SUMMARY_CSV.parent.mkdir(parents=True, exist_ok=True)
    pd.DataFrame(summary).to_csv(OUT_SUMMARY_CSV, index=False)
    pd.DataFrame(details).to_csv(OUT_DETAILS_CSV, index=False)
    OUT_JSON.write_text(json.dumps(json_payload, indent=2), encoding='utf-8')

    print(f'Wrote: {OUT_SUMMARY_CSV}')
    print(f'Wrote: {OUT_DETAILS_CSV}')
    print(f'Wrote: {OUT_JSON}')


if __name__ == '__main__':
    main()
