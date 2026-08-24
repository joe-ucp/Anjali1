# Source index

Verified 2026-08-24. Persistent identifiers provide public provenance.

## Publications used in the manuscript

| Key | Publication / persistent identifier | Evidentiary use |
|---|---|---|
| Rajpoot2025 | Rajpoot A, Sharma V. *Toxicology Reports* 14 (2025) 101950. DOI: 10.1016/j.toxrep.2025.101950; PMCID: PMC11869988 | Heart nitrite means/SEM and model details |
| Sharma2024 | Sharma S, Sharma V. *Toxicology International* 31(2) (2024) 283-293. DOI: 10.18311/ti/2024/v31i2/35881 | Kidney kit-defined NO/nitrite means and renal comet table; full text checked on the publisher-indexed public record; no redistributable local PDF was supplied |
| Bryan2007 | Bryan NS, Grisham MB. *Free Radical Biology and Medicine* 43 (2007) 645-657. DOI: 10.1016/j.freeradbiomed.2007.04.026; PMCID: PMC2041919 | Interpretation limits of NO metabolites |
| Giustarini2008 | Giustarini D et al. *Methods in Enzymology* 440 (2008) 361-380. DOI: 10.1016/S0076-6879(07)00823-3 | Griess assay interference/standardization |
| Vaziri1999 | Vaziri ND, Ding Y, Ni Z. *Hypertension* 34 (1999) 558-562. DOI: 10.1161/01.HYP.34.4.558 | Lead can change NOx and NOS expression discordantly |
| Vaziri2001 | Vaziri ND, Ding Y. *Hypertension* 37(2) (2001) 223-226. DOI: 10.1161/01.HYP.37.2.223; PMID: 11230275 | Lead, superoxide, and NOS expression in coronary endothelial cells |
| Silveira2014 | Silveira EA et al. *Free Radical Biology and Medicine* 67 (2014) 366-376. DOI: 10.1016/j.freeradbiomed.2013.11.021 | Lead, vascular NO release, superoxide, eNOS/iNOS |
| Landmesser2003 | Landmesser U et al. *Journal of Clinical Investigation* 111 (2003) 1201-1209. DOI: 10.1172/JCI14172 | eNOS uncoupling and vascular oxidative stress |
| Kim2001 | Kim KM et al. *Free Radical Biology and Medicine* 30 (2001) 747-756. DOI: 10.1016/S0891-5849(01)00460-9 | Garlic sulfur compound, iNOS expression, and endothelial cGMP in cell systems |
| Lei2010 | Lei YP et al. *Molecular Nutrition & Food Research* 54 Suppl 1 (2010) S42-S52. DOI: 10.1002/mnfr.200900278 | Garlic-derived sulfur compound and endothelial NO signaling |
| Chang2019 | Chang F, Flavahan S, Flavahan NA. *American Journal of Physiology Heart and Circulatory Physiology* 316 (2019) H80-H88. DOI: 10.1152/ajpheart.00506.2018; PMCID: PMC6383358 | Low-temperature SDS-PAGE caveats for eNOS dimers |
| vanDalen2000 | van Dalen CJ et al. *Journal of Biological Chemistry* 275 (2000) 11638-11644. DOI: 10.1074/jbc.275.16.11638 | Myeloperoxidase provides a non-peroxynitrite route to tyrosine nitration |
| Gaut2002 | Gaut JP et al. *Journal of Clinical Investigation* 109(10) (2002) 1311-1319. DOI: 10.1172/JCI15021; PMID: 12021246 | In-vivo evidence that myeloperoxidase produces nitrating oxidants, limiting source-specific interpretation of 3-nitrotyrosine |
| PercieDuSert2020 | Percie du Sert N et al. *PLOS Biology* 18 (2020) e3000410. DOI: 10.1371/journal.pbio.3000410 | ARRIVE 2.0 design/reporting standard |
| Smith2018 | Smith AJ et al. *Laboratory Animals* 52(2) (2018) 135-141. DOI: 10.1177/0023677217724823 | PREPARE animal-study planning guidance |
| Tamer2010 | Tamer E. *Annual Review of Economics* 2 (2010) 167-195. DOI: 10.1146/annurev.economics.050708.143401 | Partial-identification framework and identified sets |
| ImbensManski2004 | Imbens GW, Manski CF. *Econometrica* 72(6) (2004) 1845-1857. DOI: 10.1111/j.1468-0262.2004.00555.x | Separation of sampling inference from partial identification |
| BoydVandenberghe2004 | Boyd S, Vandenberghe L. *Convex Optimization*. Cambridge University Press (2004). DOI: 10.1017/CBO9780511804441 | Linear-program duality |
| Searle1971 | Searle SR. *Linear Models*. John Wiley & Sons (1971) | Estimable linear functionals and row-space criterion |
| ElSayed2017 | El-Sayed HS et al. *Food Chemistry* 221 (2017) 196-204. DOI: 10.1016/j.foodchem.2016.10.052 | Garlic essential-oil chemical variability |
| Lin2022 | Lin YS et al. *Journal of Traditional and Complementary Medicine* 12 (2022) 536-544. DOI: 10.1016/j.jtcme.2022.05.001; PMCID: PMC9618392 | 28-day garlic essential-oil toxicology context, not dose equivalence |
| Massadeh2007 | Massadeh AM et al. *Biological Trace Element Research* 120 (2007) 227-234. DOI: 10.1007/s12011-007-8017-3 | Garlic can alter tissue lead burden, motivating toxicokinetic measurement |

## Source limitations that constrain claims

- No individual-animal data or raw assay files were supplied.
- The cardiac paper reports a 10% homogenate nitrite concentration but no tissue/protein normalization, calibration curves, technical replicate layout, or statistical-analysis section.
- Cardiac timing is internally ambiguous: the abstract can imply 12 days plus 30 treatment days, while Methods describe a 30-day study with treatment starting on day 12.
- The cardiac route, dosing frequency, dosing volume, vehicle volume, and batch-specific GC-MS abundances are not reported.
- The kidney article labels its result NO and reports numeric uncertainty only graphically; this package neither invents nor digitizes an SEM. The same assay catalog is named in both reports, but the renal article does not specify wavelength, standard chemistry, nitrate reduction, or deproteinization.
- The complete field-level audit, including route, schedule, vehicle, assay, normalization, and source locations, is in `PROVENANCE_AUDIT.md` and `../data/source_provenance.csv`.
- Heart and kidney results are reported in separate publications. The public reports provide no cross-publication animal identifiers, linkage file, or pairing key, so pairing is unavailable and the results cannot be treated as paired animal observations.
- Neither total nitrite nor 3-nitrotyrosine is source-specific by itself.
