# Subgroup K Analysis

- Seed: 42
- K sweep: 30..50 step 1
- Permutations per K: 200
- Group1 (Z<=36): n=36
- Group2 (36<Z<=72): n=36
- Group3 (Z>72): n=36

Legend: A=local strict maximum; B=plateau; C=not significant.

## Group1 classifications
- mean_top10_anova_block: C
- mean_top10_anova_period: A
- periodicity_strength: C
- mean_top10_anova_block: K36=6.31499, K37=6.31911, K38=6.55215; p36=0.004975, p37=0.004975, p38=0.004975
- mean_top10_anova_period: K36=15.3439, K37=15.5148, K38=13.7321; p36=0.004975, p37=0.004975, p38=0.004975
- periodicity_strength: K36=9.05919e+06, K37=8.7884e+06, K38=6.22685e+06; p36=0.02985, p37=0.05473, p38=0.09453

## Group2 classifications
- mean_top10_anova_block: C
- mean_top10_anova_period: C
- periodicity_strength: C
- mean_top10_anova_block: K36=4.64771, K37=5.23764, K38=6.9289; p36=0.0199, p37=0.01493, p38=0.004975
- mean_top10_anova_period: K36=7.68069, K37=8.24047, K38=8.54606; p36=0.004975, p37=0.004975, p38=0.004975
- periodicity_strength: K36=433841, K37=396047, K38=371898; p36=0.004975, p37=0.004975, p38=0.004975

## Group3 classifications
- mean_top10_anova_block: C
- mean_top10_anova_period: C
- periodicity_strength: C
- mean_top10_anova_block: K36=1.52747, K37=1.76261, K38=1.72765; p36=0.4776, p37=0.3831, p38=0.4129
- mean_top10_anova_period: K36=7.17954, K37=7.22986, K38=7.23823; p36=0.004975, p37=0.004975, p38=0.004975
- periodicity_strength: K36=945081, K37=918968, K38=866531; p36=0.3134, p37=0.3383, p38=0.2736

## Group tables (head)
```text
Group1:
 K  mean_top10_anova_block  mean_top10_anova_period  periodicity_strength  best_k_silhouette  p_block  p_period  p_periodicity  n_perm  n_elements
30                6.405060                11.064171          1.018210e+07           0.395699 0.004975  0.009950       0.074627     200          36
31                6.067849                11.100954          9.712221e+06           0.384395 0.004975  0.004975       0.089552     200          36
32                5.946941                12.248002          9.921861e+06           0.394812 0.004975  0.014925       0.014925     200          36
33                6.245494                11.956189          9.599590e+06           0.390004 0.004975  0.014925       0.029851     200          36
34                6.227966                10.988018          7.668294e+06           0.414637 0.004975  0.004975       0.059701     200          36
35                6.254318                11.136561          7.527917e+06           0.307564 0.004975  0.009950       0.074627     200          36

Group2:
 K  mean_top10_anova_block  mean_top10_anova_period  periodicity_strength  best_k_silhouette  p_block  p_period  p_periodicity  n_perm  n_elements
30                6.366589                 9.757431         474852.686587           0.368315 0.009950  0.004975       0.024876     200          36
31                6.560801                10.005851         453981.808600           0.377605 0.004975  0.004975       0.019900     200          36
32                5.452648                 9.584545         424991.008035           0.379068 0.004975  0.004975       0.014925     200          36
33                4.571981                 9.060573         413841.340197           0.392581 0.014925  0.004975       0.014925     200          36
34                4.504397                 7.725034         435677.575857           0.394484 0.029851  0.004975       0.004975     200          36
35                4.469007                 8.256997         414420.639946           0.348742 0.029851  0.004975       0.004975     200          36

Group3:
 K  mean_top10_anova_block  mean_top10_anova_period  periodicity_strength  best_k_silhouette  p_block  p_period  p_periodicity  n_perm  n_elements
30                1.371231                 5.368106          1.360746e+06           0.707564 0.482587  0.014925       0.263682     200          36
31                1.482092                 5.948662          1.309245e+06           0.726867 0.492537  0.009950       0.343284     200          36
32                1.576292                 6.373620          1.186536e+06           0.727631 0.378109  0.009950       0.378109     200          36
33                1.560154                 6.764679          1.145887e+06           0.702329 0.452736  0.004975       0.398010     200          36
34                1.583325                 6.785865          1.070522e+06           0.700110 0.442786  0.004975       0.298507     200          36
35                1.608392                 7.516465          1.044582e+06           0.688572 0.462687  0.004975       0.258706     200          36
```
