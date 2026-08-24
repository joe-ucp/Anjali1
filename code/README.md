# Reproducibility

From the package root, install the exact tested environment from `requirements-lock.txt` (or the shorter direct-dependency list in `requirements.txt`), then run:

```powershell
py code\analyze_identifiability.py
py -m pytest -q tests -p no:cacheprovider
```

The analysis writes `evidence/verification_summary.json`, `evidence/prospective_power_grid.csv`, and both PDF/PNG versions of two figures. The reported lead-plus-olive-oil groups are used only as nominal vehicle references; causal matching is not assumed. Lead-alone results remain a prespecified secondary descriptive comparison. The tests independently check unit harmonization, both unadjusted heart Welch approximations, exact nominal-reference and secondary contrasts, sharp intervals, external fraction bounds, witness reconstruction and sign reversal, power calculations, and measurement-matrix ranks.

The cache provider is disabled because some managed Windows workspaces deny creation of pytest's temporary cache directories; this does not change test collection or assertions. The script uses no network access, random numbers, imputation, animal-level reconstruction, or simulated outcomes.
