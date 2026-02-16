# Interaction Ablations

- seed=42, n_perm=2000

```text
                              ablation  roc_auc   pr_auc  acc_best    brier  p_perm_auc
                      ABL1_remove_psit 0.570334 0.417116  0.604483 0.471084    0.000500
               ABL5_rank_normalization 0.542892 0.420335  0.604812 0.319248    0.000500
ABL3_randomize_layer_order_per_element 0.516128 0.389300  0.604483 0.474375    0.071464
                ABL2_swap_cosine_to_L2 0.510999 0.381616  0.604812 0.450665    0.155422
                 ABL4_only_mid_b13_b24 0.498152 0.369841  0.604483 0.525062    0.584708
         ABL6_mutual_information_proxy 0.494900 0.365572  0.604483 0.472268    0.683658
                 ABL4_only_low_b01_b12 0.485600 0.394701  0.607119 0.557254    0.910545
                ABL4_only_high_b25_b37 0.451239 0.339389  0.604483 0.504078    1.000000
```
