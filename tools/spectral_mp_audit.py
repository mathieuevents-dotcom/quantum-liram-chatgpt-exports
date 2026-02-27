#!/usr/bin/env python3
import csv
import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np


ROOT = Path.cwd()
REPORTS = ROOT / "reports"
FIGS = REPORTS / "figures"


def read_numeric_csv(path: Path) -> np.ndarray:
    rows = []
    with path.open("r", newline="") as f:
        reader = csv.reader(f)
        for row in reader:
            rows.append(row)
    if not rows:
        raise ValueError(f"Empty CSV: {path}")

    width = max(len(r) for r in rows)
    arr = np.full((len(rows), width), np.nan, dtype=float)
    for i, row in enumerate(rows):
        for j, cell in enumerate(row):
            c = cell.strip()
            if c == "":
                continue
            try:
                arr[i, j] = float(c)
            except ValueError:
                continue

    keep_rows = ~np.all(np.isnan(arr), axis=1)
    keep_cols = ~np.all(np.isnan(arr), axis=0)
    arr = arr[keep_rows][:, keep_cols]
    if arr.size == 0:
        raise ValueError(f"No numeric block found in: {path}")
    return arr


def discover_c_candidates() -> list[Path]:
    patterns = [
        "*correlation_matrix*.csv",
        "*layer_correlation_matrix*.csv",
        "*covariance*matrix*.csv",
        "*confusion_matrix*.csv",
    ]
    found = set()
    for pat in patterns:
        for p in ROOT.rglob(pat):
            if p.is_file():
                found.add(p)
    return sorted(found)


def score_c_candidate(path: Path, mat: np.ndarray) -> float:
    score = 0.0
    s = str(path).lower()
    name = path.name.lower()
    if "/reports/" in s:
        score += 50
    if "layer_correlation_matrix.csv" in name:
        score += 40
    elif "correlation_matrix.csv" in name:
        score += 30
    elif "covariance" in name:
        score += 20
    elif "confusion_matrix.csv" in name:
        score += 5

    if mat.ndim == 2 and mat.shape[0] == mat.shape[1]:
        score += 30
        score -= abs(mat.shape[0] - 37)
    else:
        score -= 100
    return score


def discover_x_candidates() -> list[Path]:
    pats = [
        "*X_matrix*.csv",
        "*features*.csv",
        "*bands*.csv",
        "*layer_features*.csv",
        "*inventory*.csv",
        "*compound_pair_scores*.csv",
    ]
    found = set()
    for pat in pats:
        for p in ROOT.rglob(pat):
            if p.is_file():
                found.add(p)
    return sorted(found)


def score_x_candidate(path: Path, mat: np.ndarray, c_dim: int) -> float:
    s = str(path).lower()
    name = path.name.lower()
    rows, cols = mat.shape
    score = 0.0

    if "/reports/" in s:
        score += 30
    if "features.csv" in name:
        score += 20
    if "k_37" in s:
        score += 15
    if rows > cols:
        score += 20
    score -= abs(cols - c_dim) * 2
    if rows < 20:
        score -= 100
    if cols < 5:
        score -= 100
    return score


def standardize(X: np.ndarray) -> np.ndarray:
    mu = np.mean(X, axis=0)
    sd = np.std(X, axis=0, ddof=0)
    sd_safe = np.where(sd > 0, sd, 1.0)
    return (X - mu) / sd_safe


def main() -> None:
    REPORTS.mkdir(parents=True, exist_ok=True)
    FIGS.mkdir(parents=True, exist_ok=True)

    print("== Spectral MP Audit ==")
    print(f"Repo root: {ROOT}")

    # A1: Discover C
    c_candidates = discover_c_candidates()
    if not c_candidates:
        raise FileNotFoundError("No correlation/covariance matrix CSV candidates found.")

    scored_c = []
    for p in c_candidates:
        try:
            m = read_numeric_csv(p)
        except Exception:
            continue
        scored_c.append((score_c_candidate(p, m), p, m))

    if not scored_c:
        raise RuntimeError("No numeric square matrix found among C candidates.")

    scored_c.sort(key=lambda x: x[0], reverse=True)
    _, c_path, C = scored_c[0]
    if C.shape[0] != C.shape[1]:
        raise RuntimeError(f"Selected C is not square: {c_path} shape={C.shape}")

    print(f"C selected: {c_path}")
    print(f"C shape: {C.shape}")

    # A2: Discover X
    x_candidates = discover_x_candidates()
    x_found = False
    X = None
    x_path = None
    c_dim = C.shape[0]
    scored_x = []
    for p in x_candidates:
        try:
            m = read_numeric_csv(p)
        except Exception:
            continue
        if m.ndim != 2:
            continue
        scored_x.append((score_x_candidate(p, m, c_dim), p, m))

    if scored_x:
        scored_x.sort(key=lambda x: x[0], reverse=True)
        best_score, x_path, X = scored_x[0]
        if best_score > -50:
            x_found = True
            print(f"X selected: {x_path}")
            print(f"X shape (raw numeric): {X.shape}")

    # B3: is_correlation
    diag_mean = float(np.mean(np.diag(C)))
    is_correlation = abs(diag_mean - 1.0) < 0.05
    print(f"diag_mean(C)={diag_mean:.6f}; is_correlation={is_correlation}")

    # B4/B5: N, T, reconcile
    if x_found:
        T = int(X.shape[0])
        Nx = int(X.shape[1])
        B = int(C.shape[0])
        N = Nx
        if Nx != B:
            if Nx == B:
                pass
            else:
                print(
                    f"WARNING: X columns ({Nx}) != C dimension ({B}); adapting N to C.shape[0]."
                )
                N = B
                if Nx > B:
                    X = X[:, :B]
                else:
                    pad = np.zeros((T, B - Nx), dtype=float)
                    X = np.hstack([X, pad])
        Xz = standardize(X)
    else:
        N = int(C.shape[0])
        T = max(5 * N, 200)
        print(f"T not found; using proxy T={T}; q=N/T")
        Xz = None

    # C1/C2 MP edge
    q = float(N) / float(T)
    if is_correlation:
        sigma2 = 1.0
        lambda_plus = (1.0 + math.sqrt(q)) ** 2
    else:
        if x_found and Xz is not None:
            sigma2 = float(np.var(Xz, ddof=0))
        else:
            sigma2 = float(np.mean(np.diag(C)))
        lambda_plus = sigma2 * (1.0 + math.sqrt(q)) ** 2

    eigvals = np.linalg.eigvalsh(C)
    eigvals = np.sort(eigvals)[::-1]
    lambda1_obs = float(eigvals[0])
    delta1 = float(lambda1_obs - lambda_plus)

    summary = {
        "C_path": str(c_path),
        "X_path": str(x_path) if x_found else None,
        "N": int(N),
        "T": int(T),
        "q": q,
        "diag_mean": diag_mean,
        "is_correlation": bool(is_correlation),
        "sigma2": sigma2,
        "lambda_plus": lambda_plus,
        "lambda1_obs": lambda1_obs,
        "delta1": delta1,
    }
    summary_path = REPORTS / "spectral_mp_summary.json"
    summary_path.write_text(json.dumps(summary, indent=2), encoding="utf-8")

    # D: spectrum plot
    fig_spec = FIGS / "eigen_spectrum_vs_mp.png"
    plt.figure(figsize=(8, 5))
    plt.plot(np.arange(1, len(eigvals) + 1), eigvals, marker="o", linewidth=1)
    plt.axhline(lambda_plus, color="red", linestyle="--", linewidth=1.5, label="MP edge")
    plt.title("Eigenvalue spectrum vs Marchenko–Pastur edge")
    plt.xlabel("Index")
    plt.ylabel("Eigenvalue")
    plt.legend()
    plt.tight_layout()
    plt.savefig(fig_spec, dpi=250)
    plt.close()

    # E: Monte Carlo null
    M = 500
    rng = np.random.default_rng(42)
    lambda1_null = np.empty(M, dtype=float)

    if x_found and Xz is not None:
        null_mode = "column_permutation_null"
        for i in range(M):
            Z = Xz.copy()
            for j in range(Z.shape[1]):
                rng.shuffle(Z[:, j])
            C_null = np.corrcoef(Z, rowvar=False)
            vals = np.linalg.eigvalsh(C_null)
            lambda1_null[i] = float(vals[-1])
    else:
        null_mode = "synthetic_gaussian_null"
        for i in range(M):
            G = rng.normal(0.0, 1.0, size=(T, N))
            C_null = np.corrcoef(G, rowvar=False)
            vals = np.linalg.eigvalsh(C_null)
            lambda1_null[i] = float(vals[-1])

    p_emp = float((1 + np.sum(lambda1_null >= lambda1_obs)) / (M + 1))

    null_csv = REPORTS / "montecarlo_lambda1_null.csv"
    with null_csv.open("w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["lambda1_null"])
        for v in lambda1_null:
            w.writerow([f"{v:.12g}"])

    pvalue = {
        "lambda1_obs": lambda1_obs,
        "lambda_plus": lambda_plus,
        "delta1": delta1,
        "p_emp": p_emp,
        "M": M,
        "null_mode": null_mode,
    }
    pvalue_path = REPORTS / "spectral_pvalue.json"
    pvalue_path.write_text(json.dumps(pvalue, indent=2), encoding="utf-8")

    fig_hist = FIGS / "lambda1_null_hist.png"
    plt.figure(figsize=(8, 5))
    plt.hist(lambda1_null, bins=30, alpha=0.8, edgecolor="black")
    plt.axvline(lambda1_obs, color="red", linestyle="--", linewidth=1.5, label="Observed lambda1")
    plt.title("Null distribution of top eigenvalue")
    plt.xlabel("lambda1_null")
    plt.ylabel("Frequency")
    plt.legend()
    plt.tight_layout()
    plt.savefig(fig_hist, dpi=250)
    plt.close()

    # G: LaTeX report
    tex_path = REPORTS / "spectral_mp_report.tex"
    tex = rf"""\documentclass[11pt]{{article}}
\usepackage[margin=1in]{{geometry}}
\usepackage{{graphicx}}
\usepackage{{amsmath}}
\usepackage{{booktabs}}
\title{{Spectral MP Audit}}
\date{{}}
\begin{{document}}
\maketitle

\section*{{Problem statement}}
We test whether the top eigenvalue of the observed matrix exceeds the Marchenko--Pastur (MP) bulk edge, consistent with a spike outside random-matrix noise.

\section*{{Definitions}}
Let $q=N/T$. The MP upper edge is
\[
\lambda_+ = \sigma^2(1+\sqrt{{q}})^2.
\]
For correlation-like matrices, $\sigma^2=1$.

\section*{{Data and parameter extraction}}
\begin{{itemize}}
\item Matrix $C$ path: \texttt{{{c_path}}}
\item $N={N}$, $T={T}$, $q={q:.6f}
\item Correlation-like: \texttt{{{is_correlation}}} (diag mean = {diag_mean:.6f})
\item $\sigma^2={sigma2:.6f}$
\end{{itemize}}
"""
    if not x_found:
        tex += r"\noindent\textbf{Note:} $T$ was not found from an observed design matrix and was set via conservative proxy $T=\max(5N,200)$." + "\n"
    tex += rf"""
\section*{{Results}}
\begin{{itemize}}
\item Observed $\lambda_1 = {lambda1_obs:.6f}$
\item MP edge $\lambda_+ = {lambda_plus:.6f}$
\item $\Delta_1=\lambda_1-\lambda_+ = {delta1:.6f}$
\item Empirical null p-value: $p_{{emp}}={p_emp:.6g}$ using $M={M}$ ({null_mode})
\end{{itemize}}

\section*{{Empirical Monte Carlo method}}
If an $X$ matrix is available, each column is independently permuted (after standardization) to generate null samples; otherwise, Gaussian synthetic null matrices are used under MP assumptions. For each null sample, the top eigenvalue is computed.

\section*{{Figures}}
\begin{{figure}}[h!]
\centering
\includegraphics[width=0.85\textwidth]{{figures/eigen_spectrum_vs_mp.png}}
\caption{{Eigenvalue spectrum vs MP edge.}}
\end{{figure}}

\begin{{figure}}[h!]
\centering
\includegraphics[width=0.85\textwidth]{{figures/lambda1_null_hist.png}}
\caption{{Null distribution of top eigenvalue with observed value.}}
\end{{figure}}

\end{{document}}
"""
    tex_path.write_text(tex, encoding="utf-8")

    print(f"Saved summary: {summary_path}")
    print(f"Saved pvalue: {pvalue_path}")
    print(f"Saved null csv: {null_csv}")
    print(f"Saved figure: {fig_spec}")
    print(f"Saved figure: {fig_hist}")
    print(f"Saved LaTeX: {tex_path}")
    print(f"delta1={delta1:.6f}")


if __name__ == "__main__":
    main()
