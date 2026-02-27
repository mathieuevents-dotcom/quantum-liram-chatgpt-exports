#!/usr/bin/env python3
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

INP = Path('reports/elements_pcs_atomicprops_merged.csv')
OUTDIR = Path('reports/figures')


def scatter_with_fit(df, x, y, xlabel, ylabel, title, out):
    d = df[[x, y]].dropna()
    if len(d) < 3:
        print(f'Skip {out}: insufficient data ({len(d)})')
        return
    xv = d[x].to_numpy(float)
    yv = d[y].to_numpy(float)

    m, b = np.polyfit(xv, yv, 1)
    xx = np.linspace(xv.min(), xv.max(), 200)
    yy = m * xx + b

    plt.figure(figsize=(6.5, 5))
    plt.scatter(xv, yv, s=26, alpha=0.8)
    plt.plot(xx, yy, color='red', linewidth=1.8)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.tight_layout()
    plt.savefig(out, dpi=250)
    plt.close()
    print(f'Wrote: {out}')


def main():
    df = pd.read_csv(INP)
    OUTDIR.mkdir(parents=True, exist_ok=True)

    scatter_with_fit(df, 'period', 'pc1', 'Period', 'PC1', 'PC1 vs Period', OUTDIR / 'fig_pc1_vs_period.png')
    scatter_with_fit(df, 'ionization_energy_1', 'pc1', 'Ionization energy 1 (eV)', 'PC1', 'PC1 vs Ionization Energy', OUTDIR / 'fig_pc1_vs_ionization.png')
    scatter_with_fit(df, 'electronegativity_pauling', 'pc1', 'Electronegativity (Pauling)', 'PC1', 'PC1 vs Electronegativity', OUTDIR / 'fig_pc1_vs_electronegativity.png')
    scatter_with_fit(df, 'atomic_radius', 'pc1', 'Atomic radius (pm)', 'PC1', 'PC1 vs Atomic Radius', OUTDIR / 'fig_pc1_vs_radius.png')
    scatter_with_fit(df, 'atomic_number', 'pc1', 'Atomic number', 'PC1', 'PC1 vs Atomic Number', OUTDIR / 'fig_pc1_vs_atomic_number.png')


if __name__ == '__main__':
    main()
