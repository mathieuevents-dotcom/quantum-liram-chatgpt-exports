# Static vs Dynamic

- seed=42, n_perm=2000, identical_splits=StratifiedKFold(5)

```text
          model  roc_auc   pr_auc    brier  p_perm_auc
  STATIC_SIGNED 0.585735 0.443805 0.256801      0.0005
   FULL_DYNAMIC 0.579382 0.446225 0.265928      0.0005
STATIC_HARMONIC 0.370533 0.308743 0.328928      1.0000
```

Repro OK: timestamp=2026-02-15T11:25:27.136361+00:00, commit=NO_GIT_REPO
