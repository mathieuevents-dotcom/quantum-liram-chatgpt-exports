# Projection Rules

## candidate_frequency_hz
1. Compute source frequency proxy by mode:
- `spectroscopy`: from `centroid_wavelength_nm` via `f=c/lambda`.
- `physchem`: from `ionization_energy_ev * (e/h)`; fallback `atomic_mass * 1e12`.
- `all`: prefer spectroscopy; else physchem chain above.
2. Fold to audible range by repeatedly dividing by 2 while `f>20000` and multiplying by 2 while `f<20`.

## candidate_polarity
- `top_band` in `{uv, visible}` -> `+`
- `top_band` in `{nir, ir, fir}` -> `-`
- otherwise `undefined`

## candidate_form
- Compute complexity from `entropy_over_bands` with optional `peak_count` adjustment.
- Thresholds: `<0.6 sphere`, `<1.0 spiral`, `<1.4 pyramid`, else `cube`.

## candidate_color
- Map `top_band` to discrete color set: uv->violet, visible->green, nir->red, ir->blue, fir->black.

## candidate_function
- Set to `undefined` (no defensible direct mapping from available reality features).

## candidate_class_4
- Deterministic class derived from `candidate_frequency_hz` thresholds:
- `<200 Earth`, `[200,1000) Water`, `[1000,5000) Air`, `>=5000 Fire`.
