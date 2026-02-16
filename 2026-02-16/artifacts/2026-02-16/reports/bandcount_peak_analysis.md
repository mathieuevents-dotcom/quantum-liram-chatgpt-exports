# Bandcount Peak Analysis

## Protocol
- seed=42
- n_bands in [25,30,32,36,37,38,40,50,64]
- permutations per n_bands: 200
- metrics: best_k, mean_top10_anova_block, mean_top10_anova_period, periodicity_strength, p-values

## Top 3 n_bands by metric
### mean_top10_anova_block
```text
 n_bands  mean_top10_anova_block
      50                7.121514
      64                6.821107
      38                6.790695
```
### mean_top10_anova_period
```text
 n_bands  mean_top10_anova_period
      37                27.367966
      36                26.987060
      64                26.351566
```
### periodicity_strength
```text
 n_bands  periodicity_strength
      30          2.542186e+07
      25          2.172618e+07
      38          1.635282e+07
```

## K=37 classification vs neighbors (36,38)
Legend: A=maximum strict local, B=plateau, C=non distinguable statistiquement des voisins.
- block: C
- period: A
- periodicity: C
- mean_top10_anova_block: 36=6.66726, 37=6.67723, 38=6.7907; p36=0.004975, p37=0.004975, p38=0.004975
- mean_top10_anova_period: 36=26.9871, 37=27.368, 38=22.1333; p36=0.004975, p37=0.004975, p38=0.004975
- periodicity_strength: 36=1.38415e+07, 37=1.34818e+07, 38=1.63528e+07; p36=0.199, p37=0.209, p38=0.1244

## Full results
```text
 n_bands  best_k  mean_top10_anova_block  mean_top10_anova_period  periodicity_strength  p_block  p_period  p_periodicity  n_perm
      25     4.0                5.410738                15.824156          2.172618e+07 0.004975  0.004975       0.159204     200
      30     3.0                6.696837                18.476710          2.542186e+07 0.004975  0.004975       0.169154     200
      32     3.0                6.406604                19.894960          1.628743e+07 0.004975  0.004975       0.189055     200
      36     3.0                6.667255                26.987060          1.384149e+07 0.004975  0.004975       0.199005     200
      37     3.0                6.677231                27.367966          1.348181e+07 0.004975  0.004975       0.208955     200
      38     3.0                6.790695                22.133327          1.635282e+07 0.004975  0.004975       0.124378     200
      40     3.0                6.164788                21.920092          1.224951e+07 0.004975  0.004975       0.288557     200
      50     3.0                7.121514                23.964314          9.384409e+06 0.004975  0.004975       0.104478     200
      64    46.0                6.821107                26.351566          6.345750e+06 0.004975  0.004975       0.184080     200
```
