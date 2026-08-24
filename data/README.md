# Data provenance

`published_aggregate_data.csv` is a manual transcription of published group-level values. Heart values are from Rajpoot and Sharma (2025), Table 4. Kidney values are from Sharma and Sharma (2024), Figure 5 and accompanying text. Units are harmonized using the identity 1 micromole/L = 1 nmol/mL. Blank kidney SEM fields are intentional because the graph shows error bars but does not print numerical SEMs.

For descriptive calculations, `lead_olive_oil` is the primary nominal vehicle reference for `lead_high_aseo`; causal matching is not assumed because route, frequency, formulation, and vehicle volume are not fully harmonized in the public reports. The `lead` comparator is retained as a prespecified secondary descriptive analysis. This hierarchy is analytical metadata and does not alter any transcribed value.

`published_renal_comet_data.csv` transcribes the renal comet-assay table from Sharma and Sharma (2024). It is descriptive context and is not used to identify NOS source.

These files contain no individual-animal observations, no reconstructed raw data, and no graph-digitized uncertainty. Every derived quantity in this package is either arithmetic on the reported aggregates or a deterministic mathematical construction.
