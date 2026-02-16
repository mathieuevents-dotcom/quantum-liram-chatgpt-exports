# CGVC Formalism Appendix

## A1) Weighted cosine (explicit)
Given \(x,y \in \mathbb{R}^d\) and \(W=\mathrm{diag}(w_1,\dots,w_d)\), \(w_i\ge0\):
\[
\cos_W(x,y)=
\frac{\sum_{i=1}^d w_i x_i y_i}
{\sqrt{\sum_{i=1}^d w_i x_i^2}\sqrt{\sum_{i=1}^d w_i y_i^2}}.
\]

Special case \(W=I_d\):
\[
\cos(x,y)=
\frac{\sum_i x_i y_i}{\sqrt{\sum_i x_i^2}\sqrt{\sum_i y_i^2}}.
\]

## A2) Permutation null definition
For a metric \(T\) (e.g., AUC, ANOVA aggregate, periodicity score), define:
- observed value \(T_{\mathrm{obs}}\),
- null sample \(\{T^{(b)}\}_{b=1}^B\) obtained by random label permutation (or target permutation) with fixed seed and deterministic RNG.

Typical \(B\) in this repository: 200, 1000, or 2000 depending on script.

## A3) Empirical p-value computation
One-sided empirical p-value (upper-tail) is computed as:
\[
p_{\mathrm{emp}}=\frac{1+\sum_{b=1}^{B}\mathbf{1}[T^{(b)}\ge T_{\mathrm{obs}}]}{B+1}.
\]

This avoids zero p-values in finite permutation samples.

For lower-tail metrics, replace \(\ge\) by \(\le\).

## A4) Local maxima A/B/C classification rationale
Given a metric curve \(J(K)\):

- **A (strict isolated local maximum)**:
  \[
  J(37)>J(36)\;\text{and}\;J(37)>J(38),
  \]
  with permutation-based support where applicable.

- **B (plateau / tie neighborhood)**:
  \[
  |J(37)-J(36)|\le\varepsilon \;\text{or}\; |J(37)-J(38)|\le\varepsilon,
  \]
  where \(\varepsilon\) is a predefined tolerance from the sweep implementation.

- **C (not distinguishable from neighbors)**:
  differences with neighbors are not statistically supported under the null (e.g., p-values non-significant or null-overlapping uncertainty intervals).

This A/B/C scheme is descriptive and decision-theoretic; it does not assign physical meaning.

