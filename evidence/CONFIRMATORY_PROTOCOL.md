# Prospective planning supplement for vascular, cardiac, and renal nitric-oxide pathway coherence

Version: 1.2 working draft, 2026-08-24. **Status: NOT PERFORMED.** No feasibility pilot or confirmatory experimental unit has been enrolled, randomized, dosed, sampled, or analyzed under this plan. This document is a methods supplement, not a frozen or preregistration-ready protocol, and cannot authorize animal work.

## 1. Scientific question and claim boundary

In a prospectively locked lead-by-ASEO factorial study, does high-dose *Allium sativum* essential oil (ASEO) improve a prespecified cardiovascular functional endpoint and a prespecified renal functional endpoint among lead-exposed units, and are those effects coherent with a small tissue-matched eNOS/NOS2 support set?

This is a **pathway-coherence study**, not a literal partition of nitric-oxide production among eNOS, iNOS, nNOS, diet, microbes, storage pools, and analytical conversion. Protein abundance, phosphorylation, dimerization, cGMP, pharmacological perturbation, 3-nitrotyrosine, nitrite, and total NOx are imperfect pathway measurements; none is a calibrated source-specific flux assay. Accordingly:

- the strongest permitted conclusion is that prespecified functional and molecular measurements are coherent or incoherent with the proposed pathways;
- aortic function is evidence about the aorta, not direct evidence of cardiac function;
- cardiac molecular measurements support only a cardiac molecular-coherence conclusion unless a separately powered cardiac functional gate is added before preregistration; and
- no percentage or amount of NO may be assigned to an enzyme source unless a future source-selective assay is validated, calibrated in the study matrices, and shown to render the target source contrast identifiable. Adding such an assay would require an amended estimand, validation plan, multiplicity plan, and joint power calculation before confirmatory enrollment.

Bulk nitrite direction is secondary. Neither a Griess assay nor agreement between two total-NOx assays can satisfy a pathway gate or a source-partition claim.

## 2. What is fixed by this draft and what remains to be locked

### 2.1 Scientific features and candidate elements

- Species/strain candidate: healthy Swiss albino mice. A male-only design estimates a male-specific effect and requires explicit justification; broader biological scope requires sex-inclusive randomization or a prespecified later validation study.
- Candidate schedule requiring reconciliation and biological justification: lead nitrate 50 mg/kg on days 1--30 and authenticated ASEO 80 mg/kg on days 12--30. These dates are not treated as reproduced from the cardiac report.
- Four groups form a \(2\times2\) lead-by-ASEO factorial: neither exposure, lead only, ASEO only, and lead plus ASEO, each with the appropriate locked vehicle regimen.
- The primary simple effect is ASEO among lead-exposed units. The ASEO main effect, lead main effect, and lead-by-ASEO interaction are distinct estimands.
- The experimental unit is the smallest independently randomized exposure unit: an animal under individual randomization and dosing, but potentially a cage under shared feed, water, or another cage-level exposure. Rings, fields, lanes, wells, and repeated tissue measures are subsamples.
- Where animal-level dosing is selected, the same animal supplies endpoint blood, thoracic aorta, heart, urine, and both kidneys. Under cage-level assignment, animal measurements remain nested within the randomized cage.
- Aortic, cardiac, and renal measurements retain their organ labels and are not substituted for one another.
- Two primary functional domains and a smaller mechanistic support set are defined in Section 7. The claim tier and required set cannot be weakened after seeing confirmatory outcomes.

After those fields are locked, changing species, sex scope, lead salt/dose/window, ASEO dose/window, group structure, experimental unit, organ linkage, primary contrast, or required endpoint set defines a new protocol version and requires a new power calculation and preregistration.

### 2.2 Fields that must be established and locked before a confirmatory study

The prior reports do not supply enough information to infer route, formulation, or variance. A separately labeled feasibility/assay-development phase must establish the following without contributing animals or observations to the confirmatory analysis:

- supplier, health status, age, weight range, acclimatization, diet nitrate content, fasting policy, and collection time;
- sex scope, stratification, sex-by-treatment estimands where applicable, and the exact generalizability claim;
- route, frequency, dosing volume, formulation, vehicle, concentration, time of day, and order of administration for lead and ASEO;
- ASEO identity, purity, contaminant limits, marker compounds, marker acceptance ranges, stability interval, and storage limits;
- tissue-allocation map, assay SOPs, calibration models, analytical ranges, lower limits, recovery and precision thresholds, and technical-failure rules;
- the minimum scientifically important effects \(\delta_k\), harmful-direction veto limits, the SNP equivalence margin \(m_{SNP}\), and confidence-interval precision targets;
- composite definitions, direction coding, component weights, standardization constants, and missing-component rules;
- variance, covariance, repeated-measure correlation, cage effect, assay-batch effect, anticipated attrition, number of randomized units, animals per unit where relevant, and final joint-power simulations; and
- the exact models, contrasts, multiplicity method, convergence diagnostics, fallback models, and software versions.

Pilot values must be estimated without treatment-label fishing and justified biologically as well as statistically. Pilot data, code, and all candidate thresholds considered must be reported. If the required fields cannot be locked, or the jointly powered design is infeasible, the confirmatory study must not begin.

### 2.3 Preregistration and authorization sequence

The order is mandatory: (1) complete assay development and any separate pilot; (2) obtain ethics, veterinary, facility, and legal approvals; (3) lock the final protocol, statistical analysis plan, randomization algorithm, QC rules, estimands, thresholds, and sample size; (4) time-stamp and publicly preregister those materials; and only then (5) enroll, randomize, dose, collect data, or run confirmatory assays. Preregistration merely before unblinding is too late. No pilot animal may be rolled into the confirmatory cohort.

## 3. Intervention authentication and release gate

Before confirmatory allocation, assign the production batch a permanent ID and record botanical voucher, cultivar, origin, harvest and storage history, extraction method and yield, container/headspace, temperature, light exposure, and dates.

Run the locked GC-MS procedure with retention indices, blanks, internal standard, authentic standards where feasible, deconvolution rules, and at least three independent preparations. Release the batch only if the preregistered identity, purity, contaminant, stability, and marker-abundance criteria all pass. Report the complete chromatogram, peak areas, relative abundances, library-match criteria, replicate uncertainty, and retained sealed-reference inventory.

A batch that fails, expires, or lacks the required evidence produces **HOLD**. Biological outcomes cannot repair a failed batch gate.

## 4. Allocation, cages, masking, husbandry, and analysis unit

- Lock the exposure unit before randomization. With individual dosing, randomize animals within prespecified blocks and distribute treatments across cages. With shared feed/water or any cage-level exposure, randomize cages and treat cage as the experimental unit; do not analyze individual animals as independent replicates.
- Fix cage size, numbers of randomized cages or animal-level blocks, rack-position rotation, bedding-change schedule, enrichment, handling order, and cross-contamination controls before preregistration. No post-outcome regrouping is allowed.
- Represent cage according to assignment: as a prespecified block or cluster for individual dosing and as the randomized unit for shared exposure. The joint-power simulation must use the exact planned hierarchy and pilot correlation. A missing or treatment-confounded cage invokes the preregistered rule and may force HOLD.
- Keep the allocation key with personnel who neither dose nor measure outcomes. Dosing staff do not score outcomes. Use opaque animal and sample IDs; myography, echocardiography if added, assays, blots, microscopy, pathology, and primary analysis remain masked until the signed primary output is immutable.
- Randomize and balance dissection order, ring order, plate position, gel position, instrument run, and microscopy fields across groups and cage blocks.
- Lock humane endpoints, anesthesia/analgesia, euthanasia, enrichment, temperature, humidity, light cycle, food/water, welfare observations, adverse-event handling, and attrition reporting before preregistration.
- Analyze at the randomized-unit level or with the exact prespecified hierarchy. Rings, wells, lanes, instrument injections, fields, and animals nested in a randomized cage are subsamples; they do not independently increase \(n\).

## 5. Same-animal tissue and time mapping

Collect baseline weight and prespecified nonterminal measures before dosing. Collect endpoint urine and blood at locked times, then harvest thoracic aorta, heart, and both kidneys from the same animal under a randomized dissection schedule. The tissue-allocation map must reserve prespecified aortic segments for myography and aortic molecular assays; the segment used for each purpose must be constant across animals. If tissue mass requires pooling across animals, the relevant same-animal gate is no longer estimable and the confirmatory conclusion is HOLD.

Aortic function is paired only with aortic molecular measurements from that animal. Heart molecular measurements are analyzed as a separate same-animal organ profile and cannot be used to rescue a failed aortic gate. Renal pathway and injury measurements come from the same animal and are linked to its aortic and cardiac profile by animal ID. Cross-organ correlations and treatment-by-organ interactions are prespecified secondary estimands; they show coordinated response, not source partition.

## 6. Measurements and assay validity

### 6.1 Aortic function

Measure acetylcholine (ACh) and sodium nitroprusside (SNP) concentration-response curves in intact thoracic-aortic rings after a locked phenylephrine precontraction. Fit the locked nonlinear mixed-effects curve with ring nested in animal and the assignment-appropriate randomized-unit/cage hierarchy. Record KCl viability, endothelial-integrity controls, ring segment and length, bath composition, gas, temperature, equilibration, force calibration, concentration order, and washout. Apply exclusions only through masked preregistered QC rules.

Run the primary ACh series with and without L-NAME in matched rings. Endothelium-denuded rings are an assay-validity control. A 1400W series is mechanistic exploration unless selectivity, tissue exposure, and an additional powered estimand are validated and preregistered; it cannot establish NOS2-specific flux.

### 6.2 Aortic and cardiac mechanistic support set

Select a small support set before confirmatory power is finalized. Candidate measures are total eNOS, one prespecified activation/coupling measure, and cGMP, analyzed separately in aorta and heart. Normalize blots to validated total-protein loading. If dimer analysis is selected, validate low-temperature non-boiled handling with logged disruption controls. Validate cGMP recovery, dilution linearity, and freeze-thaw limits in each matrix. Do not require every candidate assay merely because tissue is available.

Any aortic and cardiac support summaries are distinct estimands with pilot-derived, preregistered direction coding, standardization constants, and weights. Each selected component and its simultaneous interval is reported. A component crossing a preregistered harmful-direction veto prevents a coherence pass even if a summary passes.

### 6.3 Renal primary function and mechanistic support

Lock one renal primary functional endpoint after feasibility; a measured GFR endpoint is preferred where validated, while biomarker-only alternatives require a biological rationale and explicit estimand. The renal mechanistic support set should contain NOS2 abundance plus at most one validated activity-sensitive or nitrative corroborating measurement. Because myeloperoxidase can nitrate tyrosine, 3-nitrotyrosine alone is neither a NOS2-origin assay nor proof of peroxynitrite.

Urinary KIM-1 normalized to urine creatinine, plasma cystatin C, creatinine, BUN, and blinded histopathology are candidate secondary or support outcomes. The selected primary, support set, direction coding, assay requirements, and harmful-direction vetoes must be locked from the pilot before preregistration.

### 6.4 Exposure and bulk assays

Quantify lead in blood, kidney, heart, and, where validated tissue mass permits, aorta by validated ICP-MS or graphite-furnace AAS with certified reference material, blanks, spikes, duplicates, LOD/LOQ, and locked batch-acceptance rules. The primary treatment effect is unadjusted for tissue lead; lead-adjusted analyses are exploratory because tissue lead may mediate treatment.

Run the source-report nitrite kit and an orthogonal total-NOx method. Normalize tissue measures to wet mass and validated protein content; retain standards, raw signal, recovery, dilution, and plate maps. These are secondary concordance endpoints only.

## 7. Confirmatory estimands and minimal decision set

Let \(T\) denote lead plus ASEO and \(L\) lead without ASEO under the locked vehicle regimen. For a randomized-unit outcome \(Y\), \(D(Y)=E(Y\mid T)-E(Y\mid L)\), adjusted only by the locked model. Direction-code outcomes so that positive is favorable. Every minimum effect, harmful-direction veto, and equivalence margin must be biologically justified and locked before preregistration. For operating-characteristic simulations, separately lock design alternatives \(\Delta^*_{ACh}>\delta_{ACh}\), \(\Delta^*_{renal}>\delta_{renal}\), and support-set alternatives strictly beyond their applicable Pass boundaries. These alternatives define planning scenarios; they do not replace or relax the decision thresholds.

The multiplicity procedure must produce simultaneous familywise 95% confidence intervals across both functional primaries, the small required support set for any pathway-coherence claim, model-validity estimands, and vetoes. A max-*t*/closed-testing procedure based on the fully specified hierarchy is preferred; a Bonferroni fallback may be used only if selected before preregistration. Assay batches, cage hierarchy, repeated rings, and paired organs are represented exactly as locked. Exploratory endpoints cannot alter the decision.

After all preregistered validity/QC conditions pass, apply the following minimal set:

1. **Cardiovascular functional primary:** \(D(Emax_{ACh})\). Pass if its simultaneous lower bound exceeds \(\delta_{ACh}\); Negative if its simultaneous upper bound is at or below \(\delta_{ACh}\); otherwise HOLD for inadequate precision. Denudation/L-NAME specificity and SNP preservation are validity/support conditions with prespecified attenuation and equivalence rules, not additional fishing opportunities.
2. **Renal functional primary:** \(D(Y_{renal})\) for the single locked renal-function endpoint. Pass if its simultaneous lower bound exceeds \(\delta_{renal}\); Negative if its simultaneous upper bound is at or below \(\delta_{renal}\); otherwise HOLD.
3. **Mechanistic support set:** the prespecified small aortic/cardiac eNOS-sGC-cGMP and renal NOS2/nitrative set. A pathway-coherence claim requires every selected directional condition to pass and no component to cross a harmful-direction veto. Failure rejects or leaves unresolved that stronger claim tier; it does not erase a separately valid functional effect.

The lead model also has preregistered validity estimands: lead exposure relative to control, lead-induced aortic impairment relative to control, and assay-positive-control performance. Their thresholds and simultaneous intervals are included in power and multiplicity. Failure caused by an invalid exposure/model or assay is HOLD, not evidence against ASEO.

## 8. Overall decision rule

Apply decisions in this order:

1. **HOLD for invalidity:** ethics, authorization, identity, dosing, batch, exposure/model, cage structure, masking, assay QC, or prespecified data-integrity requirements fail. No biological claim is made.
2. **Functional support:** report the cardiovascular and renal functional claims separately when their respective primaries Pass. A combined two-domain functional claim requires both primaries to Pass. None of these claims establishes a source mechanism.
3. **Pathway-coherence support:** both functional primaries and every required mechanistic-support condition Pass. This remains a coherence claim, not quantitative NO-source partition.
4. **Rigorous negative:** validity passes and a required endpoint is Negative. The rejected claim tier must be named: a mechanistic-support failure can reject the coherence conjunction without proving absence of functional benefit.
5. **HOLD for imprecision:** validity passes, no required endpoint is Negative, and one or more required intervals do not resolve the locked threshold.

Bulk heart-up/kidney-down nitrite direction may be reported as secondary concordance but cannot rescue any gate. Discordant organs or components must be reported without relabeling the endpoint family after analysis.

## 9. Joint sample size and precision requirement

The published \(n=6\) per group is not copied, and this draft intentionally gives **no executable sample size**. Before preregistration, use the separate pilot's randomized-unit and nested-animal covariance, cage correlation, repeated-ring structure, assay failure, and attrition estimates to simulate the complete four-group design and locked analysis.

The chosen number of randomized units and animals per unit, where relevant, must simultaneously satisfy all of the following under prespecified data-generating scenarios:

- at least 90% probability that the exposure/model validity conditions and the complete endpoint set for the selected claim tier jointly Pass at the global familywise error rate when every true effect equals or exceeds its locked design alternative, with each design alternative strictly beyond the applicable Pass boundary; no 90% Pass probability is claimed when a true effect lies exactly on a decision threshold;
- at least 90% probability of classifying a required gate Negative when its true effect is at the preregistered scientifically null value while the remaining validity conditions hold;
- at least 90% probability that SNP equivalence passes when the true contrast is zero; and
- the locked maximum confidence-interval width for every required estimand, including component-veto and model-validity estimands.

Power simulations must include multiplicity, nonlinear-curve estimation, the assignment-appropriate cage hierarchy, missingness, paired organs, and endpoint dependence. Report code, seeds, scenarios, operating-characteristic uncertainty, and sensitivity analyses. Inflate only for prospectively justified attrition; do not replace units after treatment labels or outcomes are known. If joint power and precision cannot be met within ethical and facility constraints, reduce the prespecified claim tier or do not proceed; no endpoint may be demoted after outcomes are seen.

The supplied `prospective_power_grid.csv` is only an idealized two-sample sensitivity illustration. It neither powers this protocol nor recommends an animal count.

## 10. Statistical execution and transparency

Use the preregistered nonlinear mixed model for concentration-response data; represent cage as block, cluster, or randomized unit according to assignment; use randomized-unit models for primary endpoints; and use a locked treatment-by-organ model only for secondary paired organ profiles. Report simultaneous effect intervals, raw support-component intervals, model diagnostics, and locked fallback analyses. No outcome-dependent exclusion is allowed. A technical rerun occurs only under a written group-blind QC rule.

Report missingness by randomized unit, animal, outcome, group, cage, assay batch, and reason. The primary analysis follows all randomized units under the locked missing-data estimand and model, with all measured animals nested as specified; bounded missing-not-at-random sensitivity analyses are required when attrition exceeds the preregistered trigger. Deviations and amendments remain date-stamped and cannot change the primary decision for data already collected.

At reporting, release de-identified unit-level and animal-level data, organ links, cage and batch identifiers, raw instrument exports, calibration and QC files, chromatograms, uncropped blots with exposure metadata, all exclusions, code, seeds, protocol deviations, negative and discordant results, a PREPARE planning record, and an ARRIVE 2.0 checklist.

**Status: NOT PERFORMED.** This draft specifies the claim boundary and the work needed before a confirmatory experiment can be preregistered. It supplies no biological evidence and no executable animal count.
