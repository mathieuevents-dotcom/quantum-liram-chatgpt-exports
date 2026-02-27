#!/usr/bin/env python3
from __future__ import annotations

import argparse
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

INPUT = Path("reports/elements_pcs_atomicprops_merged.csv")
REPORTS = Path("reports")
FIGURES = Path("figures")

OUT_PROJ = REPORTS / "phi3_projection.csv"
OUT_SHUFFLED = REPORTS / "phi3_projection_shuffled.csv"
OUT_ANALYSIS = REPORTS / "phi3_geometry_analysis.md"
OUT_FIG = FIGURES / "phi3_cluster_labeled.svg"
OUT_OVERVIEW = REPORTS / "overview.html"


def build_projection(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    for col in ["pc1", "pc2", "pc3", "atomic_number", "period", "group"]:
        out[col] = pd.to_numeric(out[col], errors="coerce")

    out = out.dropna(subset=["symbol", "pc1", "pc2", "pc3", "atomic_number"]).copy()
    out["phi3"] = np.sqrt(out["pc1"] ** 2 + out["pc2"] ** 2 + out["pc3"] ** 2)
    out["radius_pc12"] = np.sqrt(out["pc1"] ** 2 + out["pc2"] ** 2)

    ranks = out["phi3"].rank(method="first")
    out["cluster"] = pd.qcut(ranks, q=3, labels=["C1", "C2", "C3"]).astype(str)

    keep_cols = [
        "symbol",
        "atomic_number",
        "period",
        "group",
        "pc1",
        "pc2",
        "pc3",
        "radius_pc12",
        "phi3",
        "cluster",
    ]
    return out[keep_cols].sort_values("atomic_number").reset_index(drop=True)


def write_analysis(proj: pd.DataFrame, shuffled: pd.DataFrame, seed: int) -> None:
    corr_phi3_pc1 = proj["phi3"].corr(proj["pc1"])
    corr_phi3_z = proj["phi3"].corr(proj["atomic_number"])
    corr_shuffled_z = shuffled["phi3_shuffled"].corr(shuffled["atomic_number"])

    cluster_counts = proj["cluster"].value_counts().sort_index()

    lines = [
        "# Phi3 Geometry Analysis",
        "",
        "> [!NOTE]",
        "> ## Data provenance",
        "> - **Pourquoi `reports/phi3_projection.csv` manquait**: le dépôt ne contenait pas de stage dédié `phi3` ni de contrat de sortie imposant ce fichier. Le pipeline historique produisait des artefacts PCA/atomic props, mais pas de projection `phi3` nominale.",
        "> - **Construction du seed dataset (valeurs, source, méthode)**: `phi3_projection.csv` est construit à partir de `reports/elements_pcs_atomicprops_merged.csv` (source locale), lui-même obtenu via `bash tools/run_atomicprops_analysis.sh` (`compute_element_pcs.py` + fusion avec `data/external/atomic_properties/atomic_properties_clean.csv`). La méthode applique `phi3 = sqrt(pc1^2 + pc2^2 + pc3^2)`, `radius_pc12 = sqrt(pc1^2 + pc2^2)`, puis un clustering déterministe en 3 quantiles (`C1/C2/C3`) sur le rang de `phi3`.",
        "> - **Remplacement futur par des données réelles**: remplacer la source d'entrée par un export brut versionné (ex: `data/raw/...`) contenant les variables physiques d'origine; recalculer `pc1/pc2/pc3` avec la même procédure; conserver les mêmes noms de colonnes (`symbol`, `atomic_number`, `pc1`, `pc2`, `pc3`) pour garder `scripts/run_phi3.sh` compatible sans modification.",
        "",
        "## Seed Policy",
        f"- Global seed used for this run: `{seed}`",
        "- `phi3_projection_shuffled.csv` is generated with deterministic permutation based on this seed.",
        "",
        "## Dataset Summary",
        f"- Rows: `{len(proj)}`",
        f"- Phi3 mean: `{proj['phi3'].mean():.6f}`",
        f"- Phi3 std: `{proj['phi3'].std(ddof=0):.6f}`",
        f"- Corr(phi3, pc1): `{corr_phi3_pc1:.6f}`",
        f"- Corr(phi3, atomic_number): `{corr_phi3_z:.6f}`",
        f"- Corr(phi3_shuffled, atomic_number): `{corr_shuffled_z:.6f}`",
        "",
        "## Cluster Counts",
    ]

    for cluster, count in cluster_counts.items():
        lines.append(f"- {cluster}: `{int(count)}`")

    OUT_ANALYSIS.write_text("\n".join(lines) + "\n", encoding="utf-8")


def save_cluster_figure(proj: pd.DataFrame) -> None:
    color_map = {"C1": "#1f77b4", "C2": "#ff7f0e", "C3": "#2ca02c"}
    FIGURES.mkdir(parents=True, exist_ok=True)

    fig, ax = plt.subplots(figsize=(9, 6), dpi=220)

    for cluster in ["C1", "C2", "C3"]:
        sub = proj[proj["cluster"] == cluster]
        if sub.empty:
            continue
        ax.scatter(
            sub["pc1"],
            sub["pc2"],
            s=35,
            alpha=0.85,
            c=color_map[cluster],
            edgecolors="black",
            linewidths=0.3,
            label=f"{cluster} (n={len(sub)})",
        )

        # Label one representative per cluster for readability.
        top = sub.nlargest(1, "phi3")
        for _, row in top.iterrows():
            ax.text(row["pc1"], row["pc2"], str(row["symbol"]), fontsize=8, ha="left", va="bottom")

    ax.set_title("Phi3 Clusters in PC1-PC2 Space")
    ax.set_xlabel("PC1")
    ax.set_ylabel("PC2")
    ax.grid(alpha=0.25)
    ax.legend(loc="best", frameon=True)

    fig.tight_layout()
    fig.savefig(OUT_FIG)
    plt.close(fig)


def write_overview(seed: int, n_rows: int) -> None:
    html = f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\" />
  <title>Phi3 Overview</title>
  <style>
    body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; margin: 2rem; line-height: 1.5; }}
    code {{ background: #f2f2f2; padding: 0.1rem 0.35rem; border-radius: 4px; }}
    ul {{ margin-top: 0.4rem; }}
  </style>
</head>
<body>
  <h1>Phi3 Overview</h1>
  <p>Deterministic run completed with seed <code>{seed}</code> and <code>{n_rows}</code> rows.</p>
  <h2>Artifacts</h2>
  <ul>
    <li><a href=\"phi3_projection.csv\">reports/phi3_projection.csv</a></li>
    <li><a href=\"phi3_projection_shuffled.csv\">reports/phi3_projection_shuffled.csv</a></li>
    <li><a href=\"phi3_geometry_analysis.md\">reports/phi3_geometry_analysis.md</a></li>
    <li><a href=\"../figures/phi3_cluster_labeled.svg\">figures/phi3_cluster_labeled.svg</a></li>
  </ul>
</body>
</html>
"""
    OUT_OVERVIEW.write_text(html, encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser(description="Generate deterministic phi3 outputs")
    parser.add_argument("--seed", type=int, default=42, help="Global random seed")
    args = parser.parse_args()

    if not INPUT.exists():
        raise FileNotFoundError(f"Missing required input: {INPUT}")

    REPORTS.mkdir(parents=True, exist_ok=True)
    FIGURES.mkdir(parents=True, exist_ok=True)

    rng = np.random.default_rng(args.seed)

    base = pd.read_csv(INPUT)
    proj = build_projection(base)
    proj.to_csv(OUT_PROJ, index=False)

    shuffled = proj.copy()
    shuffled["phi3_shuffled"] = rng.permutation(proj["phi3"].to_numpy())
    shuffled = shuffled[["symbol", "atomic_number", "phi3", "phi3_shuffled", "cluster"]]
    shuffled.to_csv(OUT_SHUFFLED, index=False)

    write_analysis(proj, shuffled, args.seed)
    save_cluster_figure(proj)
    write_overview(args.seed, len(proj))

    print(f"Wrote: {OUT_OVERVIEW}")
    print(f"Wrote: {OUT_PROJ}")
    print(f"Wrote: {OUT_SHUFFLED}")
    print(f"Wrote: {OUT_ANALYSIS}")
    print(f"Wrote: {OUT_FIG}")


if __name__ == "__main__":
    main()
