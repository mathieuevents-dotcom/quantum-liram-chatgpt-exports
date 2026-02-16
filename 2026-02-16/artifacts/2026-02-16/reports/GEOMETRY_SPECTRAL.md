# GEOMETRY spectral

- Embeddings computed for n_bands in {32, 37, 64}.
- UMAP package unavailable locally; deterministic t-SNE fallback used for `manifold_umap.svg`.

## Geometry metrics table
```text
 n_bands  pc1_var  pc2_var  pc3_var  best_silhouette  best_k  modularity_knn_block  clustering_coeff_knn  assortativity_block  group_sep_top10_anova  mutual_info_group_cluster  corr_pc1_Z  corr_pc2_Z  corr_umap1_Z  corr_umap2_Z
      32 0.147903 0.131243 0.120432         0.740821       2              0.147593              0.551116             0.204215               6.406604                   0.019213    0.250723   -0.014242     -0.379738     -0.125288
      37 0.147901 0.127473 0.112900         0.728436       3              0.123446              0.539573             0.170794               6.677231                   0.039053   -0.269338    0.065757     -0.149781      0.509969
      64 0.136525 0.122380 0.110495         0.724833       3              0.145727              0.497950             0.201518               6.821107                   0.039053   -0.274586    0.033685     -0.291374     -0.082078
```

## Invariance notes (statistical)
- Best silhouette among tested regimes: n_bands=32
- Highest KNN modularity (block partition): n_bands=32
- Strongest |corr(PC1, Z)|: n_bands=64
- Statements above are descriptive and limited to computed metrics.
