# Reproducibility

- Seed: `42`
- Permutations: `2000`

## SHA256
- `data/extracted/elements_table.csv`: `00a17eb523e012b8a161a6af73731a3dbc26fab081ef40d7239468aba74a0df7`
- `data/extracted/elements_labeled.csv`: `1eea77fcbaccaa0920882819942f741ea0c5145e4bd9fa556331becdcc51ab8b`
- `data/external/raw/nist_lines.csv`: `bdb68b029b0bff9df092bc04b500d1cbb16ec6b616e8b05dc7b663f7cd92ae3e`
- `data/external/processed/spectral_features.csv`: `7078d74e1fbab4c5390628846f620121c20409d3068662c98042358df4939684`
- `reports/tables/feature_tests.csv`: `3f77dd8dc035e2616a26814d509351148fd41fb98b76fd0d6be096f808fa312e`
- `reports/confusion_matrix.csv`: `a2ce5c9f7e06b0c03bb3dd917a65836565e154efe08c87d57801a7709d9129bf`
- `reports/validation_spectroscopy_summary.md`: `a4045ab595e41e3f1e27f5f13f902fcf8667ce66cb2a26bc039e8dae873d84d7`

## NIST Query Notes
- See `reports/reality_sources.md` for endpoint, date, and rate-limit notes.

<!-- NIST_ATOMIC_PROCESSING_START -->
## NIST Atomic Processing Manifest

### Input File Hashes
- `data/external/raw/NIST ASD Levels Output_C I.html`: `7e797ba51b6f6a74460400c47de72f053743bb9fab9ba4e7fc89b39b95940341`
- `data/external/raw/NIST ASD Levels Output_Fe I.html`: `abc0eb3e122c80effb1337aba816ac2a836c9207dadafe14a445335e8bd5a2c5`
- `data/external/raw/NIST ASD Levels Output_H I.html`: `0b545af5da58181a2cf7cb8f90fdb608d3979ff36308807498a071c1dd4e3d83`
- `data/external/raw/NIST ASD Levels Output_N I.html`: `4b07d661bd5ca3727c1e236d5c7679e65407934da8ffb08805d1380a81c2b547`
- `data/external/raw/NIST ASD Levels Output_O I.html`: `d822a2ac007701ccf29a5b9f17f0a745f321bd995fa04efd7698a76e56a772e4`
- `data/external/raw/NIST ASD Output_ Lines_C I.html`: `1eb1130a05bc5d40534e0b001815d3bac3e9ee32d6283c1649aafa85250d5e46`
- `data/external/raw/NIST ASD Output_ Lines_Fe I.html`: `4159a9c44ef809bcc8192b987c168795c941deab2fcb89d350b07990723688fe`
- `data/external/raw/NIST ASD Output_ Lines_H I.html`: `ade71ce59bc017d0b48f502b33cb48f4adb57f4b8f3a2727a4246ac5ea54d0ab`
- `data/external/raw/NIST ASD Output_ Lines_N I.html`: `03de37b542f87f71daae574ecba1b02fbd11b0028d68c76a6906d02cf5041b93`
- `data/external/raw/NIST ASD Output_ Lines_O I.html`: `27a7436a92ff350523c51847fcf57d986a727fe0d7a20a6fda935acc4bd9d371`

### Parse Mappings
- Lines parsing: extracted `wavelength_nm`, `Ritz`, `relative_intensity`, lower/upper energies and term labels from `|`-delimited rows inside `<pre>` blocks.
- Levels parsing: extracted `energy_cm1`, `term_symbol`, `configuration`, `J`, and metadata from `|`-delimited rows inside `<pre>` blocks.
- Frequency conversions:
  - Lines: `frequency_hz = 299792458 / (wavelength_nm * 1e-9)`
  - Levels: `frequency_hz = energy_cm1 * 100 * 299792458`

### Output Mappings
- Lines `NIST ASD Output_ Lines_C I.html` -> `data/external/processed/nist_lines_parsed/C_lines_parsed.csv` (2093 rows)
- Lines `NIST ASD Output_ Lines_Fe I.html` -> `data/external/processed/nist_lines_parsed/Fe_lines_parsed.csv` (9915 rows)
- Lines `NIST ASD Output_ Lines_H I.html` -> `data/external/processed/nist_lines_parsed/H_lines_parsed.csv` (509 rows)
- Lines `NIST ASD Output_ Lines_N I.html` -> `data/external/processed/nist_lines_parsed/N_lines_parsed.csv` (147 rows)
- Lines `NIST ASD Output_ Lines_O I.html` -> `data/external/processed/nist_lines_parsed/O_lines_parsed.csv` (172 rows)
- Levels `NIST ASD Levels Output_C I.html` -> `data/external/processed/nist_levels_parsed/C_levels_parsed.csv` (435 rows)
- Levels `NIST ASD Levels Output_Fe I.html` -> `data/external/processed/nist_levels_parsed/Fe_levels_parsed.csv` (847 rows)
- Levels `NIST ASD Levels Output_H I.html` -> `data/external/processed/nist_levels_parsed/H_levels_parsed.csv` (106 rows)
- Levels `NIST ASD Levels Output_N I.html` -> `data/external/processed/nist_levels_parsed/N_levels_parsed.csv` (381 rows)
- Levels `NIST ASD Levels Output_O I.html` -> `data/external/processed/nist_levels_parsed/O_levels_parsed.csv` (614 rows)

- Feature table output: `data/external/processed/spectral_features_atoms.csv`
<!-- NIST_ATOMIC_PROCESSING_END -->
