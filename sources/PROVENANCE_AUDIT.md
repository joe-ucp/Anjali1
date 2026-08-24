# Quotation-level provenance audit

Verified: 2026-08-24. This record supports the descriptive contrasts only. It does not establish treatment comparability, animal linkage, or source identity.

## Source records

- Cardiac: Rajpoot and Sharma (2025), DOI `10.1016/j.toxrep.2025.101950`, PMCID `PMC11869988`. The publisher PDF is not redistributed; the package preserves the DOI/PMCID, page and section locations, machine-readable transcription, and this audit record.
- Renal: Sharma and Sharma (2024), DOI `10.18311/ti/2024/v31i2/35881`. Full text was checked through the publisher-indexed public record. The publisher PDF is not redistributed; the package preserves the DOI, page and section locations, machine-readable transcription, and retrieval record.

## Cardiac report

| Field | Source location | Direct record | Audit consequence |
|---|---|---|---|
| High-dose and nominal-reference labels | Tables 2 and 4 | Group IV is lead nitrate plus high-dose ASEO; Group VI is lead nitrate plus vehicle control (olive oil). Table 2 lists the olive-oil dose as `N/A`. | The lead-plus-olive-oil group is only a nominal reference; causal comparability is undocumented. |
| Route/frequency/volume | Section 2.6 and Table 2 | Not reported for lead, ASEO, or olive oil. | No causal oil-effect claim is made. |
| Schedule reading 1 | Abstract | “After 12 days of lead exposure, treatments were administered for 30 days.” | This can imply 42 total days. |
| Schedule reading 2 | Section 2.6 | The study is described as “over a 30-day investigative period,” with adjuncts initiated on day 12 and continued to the end. | This implies 30 total days. The discrepancy does not alter Table 4 values but prevents treating the schedule as reproduced. |
| Tissue processing | Section 2.7 | Heart, 10% w/v homogenate in 0.1 M sodium-phosphate buffer, centrifuged 10,000 rpm for 15-20 minutes at 4 C. | Results are supernatant concentrations, not tissue-mass- or protein-normalized quantities. |
| Analyte and assay | Section 2.9 | Elabscience E-BC-K035-M; NO indirectly quantified as nitrite at 550 nm against a standard curve. | Operationally a bulk nitrite readout, not NO-source flux. Nitrate reduction and deproteinization were not reported. |
| Documented non-nitrite inconsistency | Results prose versus Table 3 | Prose reports LDL values of 86.57 and 85.75 ug/mL for silymarin and olive oil; Table 3 gives 85.43 and 81.62 ug/mL. | This concerns LDL, not Table 4 nitrite. It does not alter any value used in the present calculations. |

## Renal report

| Field | Source location | Direct record | Audit consequence |
|---|---|---|---|
| Route | Section 2.6 | “All the doses in the experimental duration were administered via oral gavage needle.” | Route is reported; dosing frequency is not. |
| Groups and schedule | Section 2.7 | All lead subgroups received 50 mg/kg lead nitrate for 30 days; adjuncts were added from day 12 to the end. ASEO doses were prepared in olive oil. | The olive-oil dose and volume remain unreported; the lead-plus-olive-oil group is only a nominal reference. |
| Tissue processing | Sections 2.8-2.9 | Kidney, 10% w/v homogenate in 0.1 M sodium-phosphate buffer, centrifuged 10,000 rpm for 10-15 minutes at 4 C. | Results are supernatant concentrations without tissue-mass or protein normalization. |
| Analyte and assay | Sections 2.10 and 3.1.7 | The report labels the result NO and names Elabscience E-BC-K035-M as the colorimetric kit. | The article does not state nitrate reduction, deproteinization, wavelength, or standard chemistry. The paper therefore uses “kit-defined NO/nitrite readout” when exact cross-report chemistry matters. |
| Values and uncertainty | Section 3.1.7 and Figure 5 | Six printed means are reported in micromol/L; Figure 5 displays mean plus/minus SEM but no numeric SEMs. | All six means are transcribed. No uncertainty was digitized from pixels and no renal interval was reconstructed. |

## Assay-interference boundary

Neither source report presents lead-nitrate spike/recovery, dilution-linearity, lot-specific instructions, or matrix-interference validation. Lead nitrate can affect biological nitrate-nitrite handling, but direct analytical interference is unresolved and is not asserted. A follow-up must use matrix-matched spike/recovery controls and document nitrate reduction and deproteinization explicitly.

## Completeness and selection

`data/published_aggregate_data.csv` includes all six reported groups for both tissues: control, lead, low-dose ASEO, high-dose ASEO, silymarin, and olive oil. The main figure displays four groups because the formal contrast uses the high-dose and nominal-reference pair and the lead-alone secondary comparison; omission from the figure is not omission from the transcription.
