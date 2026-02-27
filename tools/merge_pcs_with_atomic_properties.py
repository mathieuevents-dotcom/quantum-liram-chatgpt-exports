#!/usr/bin/env python3
from pathlib import Path
import pandas as pd

PCS = Path('reports/elements_pcs_atomicprops.csv')
PROPS = Path('data/external/atomic_properties/atomic_properties_clean.csv')
OUT = Path('reports/elements_pcs_atomicprops_merged.csv')


def main():
    pcs = pd.read_csv(PCS)
    props = pd.read_csv(PROPS)

    if 'atomic_number' in pcs.columns and 'atomic_number' in props.columns:
        merged = pcs.merge(props, on='atomic_number', how='left', suffixes=('', '_prop'))
        if 'symbol_prop' in merged.columns:
            merged['symbol'] = merged['symbol'].fillna(merged['symbol_prop'])
            merged = merged.drop(columns=['symbol_prop'])
        merge_mode = 'atomic_number'
    else:
        merged = pcs.merge(props, on='symbol', how='left', suffixes=('', '_prop'))
        merge_mode = 'symbol'

    OUT.parent.mkdir(parents=True, exist_ok=True)
    merged.to_csv(OUT, index=False)

    print(f'Wrote: {OUT}')
    print(f'Merge key: {merge_mode}')
    print('Missingness after merge:')
    for c in ['electronegativity_pauling', 'ionization_energy_1', 'atomic_radius', 'period', 'group']:
        if c in merged.columns:
            miss = int(merged[c].isna().sum())
            print(f'  {c}: missing={miss}/{len(merged)}')


if __name__ == '__main__':
    main()
