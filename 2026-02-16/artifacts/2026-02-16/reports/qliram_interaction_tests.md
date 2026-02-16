# qliram interaction tests

## Methods
- Pair scores computed from 37D signatures: cosine, dot-product, weighted dot-product.
- Weighted score uses diagonal weights from ridge fit on proxy target: Z.
- Test 1: same-group / same-period enrichment with Cohen's d and permutation p-values (1000 shuffles).
- Test 2: local co-occurrence proxy if parsable local datasets exist; otherwise NO_DATA.

## Data availability for co-occurrence proxy
- files_used: 0
```text
NO_DATA
```

## Results
```text
                        test                  relation  score  n_pos  n_neg   mean_pos    mean_neg  mean_diff  cohen_d  perm_pvalue  status
same_group_period_enrichment                same_group  S_cos    639   5139   0.220451    0.023785   0.196666 0.480606     0.000999      OK
same_group_period_enrichment                same_group  S_dot    639   5139   3.920809   -0.876318   4.797126 0.430800     0.000999      OK
same_group_period_enrichment                same_group S_wdot    639   5139 170.377367  -30.973376 201.350743 0.406328     0.000999      OK
same_group_period_enrichment               same_period  S_cos   1090   4688   0.354141   -0.026219   0.380360 0.985034     0.000999      OK
same_group_period_enrichment               same_period  S_dot   1090   4688   6.496037   -1.936579   8.432616 0.785072     0.000999      OK
same_group_period_enrichment               same_period S_wdot   1090   4688 406.209513 -105.176922 511.386435 1.117254     0.000999      OK
          cooccurrence_proxy cooccur_vs_matched_random    ALL      0      0        NaN         NaN        NaN      NaN          NaN NO_DATA
```

All statements are statistical and descriptive; no physical mechanism is inferred.
