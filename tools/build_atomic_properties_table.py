#!/usr/bin/env python3
from pathlib import Path
import pandas as pd
import numpy as np

RAW_JSON = Path('data/external/atomic_properties/atomic_properties_raw.json')
RAW_CSV = Path('data/external/atomic_properties/atomic_properties_raw.csv')
OUT = Path('data/external/atomic_properties/atomic_properties_clean.csv')

KJ_MOL_TO_EV = 0.01036427230133138


def canon_symbol(s):
    if not isinstance(s, str) or not s:
        return s
    s = s.strip()
    return s[:1].upper() + s[1:].lower()


def completeness_score(row, cols):
    return int(sum(pd.notna(row[c]) for c in cols))


def main():
    rows = []
    source_note = None
    if RAW_CSV.exists():
        raw = pd.read_csv(RAW_CSV)
        for _, e in raw.iterrows():
            ion1_kj = e.get('IonizationEnergy')
            row = {
                'atomic_number': e.get('AtomicNumber'),
                'symbol': canon_symbol(e.get('Symbol')),
                'name': e.get('EnglishName'),
                'period': e.get('Period'),
                'group': e.get('Group'),
                'electronegativity_pauling': e.get('Electronegativity'),
                'ionization_energy_1': float(ion1_kj) * KJ_MOL_TO_EV if pd.notna(ion1_kj) else np.nan,
                'atomic_radius': e.get('AtomicRadius'),
                'source_note': 'Bluegrams periodic-table-data CSV',
            }
            rows.append(row)
        source_note = str(RAW_CSV)
    elif RAW_JSON.exists():
        import json

        data = json.loads(RAW_JSON.read_text(encoding='utf-8'))
        elements = data.get('elements', [])
        for e in elements:
            ion1_kj = None
            ies = e.get('ionization_energies')
            if isinstance(ies, list) and len(ies) > 0 and ies[0] is not None:
                ion1_kj = ies[0]

            row = {
                'atomic_number': e.get('number'),
                'symbol': canon_symbol(e.get('symbol')),
                'name': e.get('name'),
                'period': e.get('period'),
                'group': e.get('group'),
                'electronegativity_pauling': e.get('electronegativity_pauling'),
                'ionization_energy_1': ion1_kj * KJ_MOL_TO_EV if ion1_kj is not None else np.nan,
                'atomic_radius': e.get('atomic_radius'),
                'source_note': 'Bowserinator Periodic-Table-JSON',
            }
            rows.append(row)
        source_note = str(RAW_JSON)
    else:
        raise FileNotFoundError(f'Missing raw dataset: expected {RAW_CSV} or {RAW_JSON}')

    df = pd.DataFrame(rows)
    df['atomic_number'] = pd.to_numeric(df['atomic_number'], errors='coerce').astype('Int64')
    df['period'] = pd.to_numeric(df['period'], errors='coerce').astype('Int64')
    df['group'] = pd.to_numeric(df['group'], errors='coerce').astype('Int64')

    float_cols = ['electronegativity_pauling', 'ionization_energy_1', 'atomic_radius']
    for c in float_cols:
        df[c] = pd.to_numeric(df[c], errors='coerce')

    df = df.dropna(subset=['atomic_number'])

    core = ['symbol', 'period', 'group', 'electronegativity_pauling', 'ionization_energy_1', 'atomic_radius']
    df['_score'] = df.apply(lambda r: completeness_score(r, core), axis=1)
    df = df.sort_values(['atomic_number', '_score'], ascending=[True, False])
    df = df.drop_duplicates(subset=['atomic_number'], keep='first').drop(columns=['_score'])

    wanted = [
        'atomic_number', 'symbol', 'name', 'period', 'group',
        'electronegativity_pauling', 'ionization_energy_1', 'atomic_radius', 'source_note'
    ]
    df = df[wanted].sort_values('atomic_number').reset_index(drop=True)

    OUT.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT, index=False)

    print(f'Source used: {source_note}')
    print(f'Wrote: {OUT}')
    print(f'Rows: {len(df)}')
    print('Coverage stats (non-missing):')
    for c in ['atomic_number', 'symbol', 'period', 'group', 'electronegativity_pauling', 'ionization_energy_1', 'atomic_radius']:
        print(f'  {c}: {int(df[c].notna().sum())}/{len(df)}')


if __name__ == '__main__':
    main()
