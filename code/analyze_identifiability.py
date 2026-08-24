"""Reproduce the aggregate-data audit and source-identifiability certificates.

This program does not simulate animal outcomes. It uses only published aggregate
means, constructs exact latent decompositions that reproduce those means, and
calculates design quantities whose assumptions are printed with the outputs.
"""

from __future__ import annotations

import argparse
import csv
import json
import math
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import nct, t


# Use editable, publisher-friendly TrueType text in vector figure outputs.
plt.rcParams.update({"pdf.fonttype": 42, "ps.fonttype": 42})


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "published_aggregate_data.csv"
EVIDENCE = ROOT / "evidence"


def read_records(path: Path = DATA) -> list[dict[str, object]]:
    records: list[dict[str, object]] = []
    with path.open(newline="", encoding="utf-8") as handle:
        for row in csv.DictReader(handle):
            item: dict[str, object] = dict(row)
            for key in ("mean_reported", "mean_nmol_per_ml"):
                item[key] = float(row[key])
            for key in ("sem_reported", "sem_nmol_per_ml"):
                item[key] = float(row[key]) if row[key] else None
            item["n"] = int(row["n"])
            records.append(item)
    return records


def get_record(records: list[dict[str, object]], tissue: str, group: str) -> dict[str, object]:
    matches = [r for r in records if r["tissue"] == tissue and r["group"] == group]
    if len(matches) != 1:
        raise ValueError(f"Expected one record for {tissue}/{group}; got {len(matches)}")
    return matches[0]


def micromol_per_l_to_nmol_per_ml(value: float) -> float:
    """Convert micromoles/L to nmol/mL.

    The numerical value is unchanged because both the amount numerator and the
    volume denominator acquire a factor of 1,000.
    """
    return value * 1_000.0 / 1_000.0


def welch_difference_ci(
    mean_a: float,
    sem_a: float,
    n_a: int,
    mean_b: float,
    sem_b: float,
    n_b: int,
    confidence: float = 0.95,
) -> dict[str, float]:
    """Welch interval for mean_a - mean_b from reported SEMs.

    This is an aggregate-data approximation; it is not a reanalysis of raw data
    and it does not reconstruct the authors' one-way-ANOVA/Tukey calculation.
    """
    variance_a = sem_a**2
    variance_b = sem_b**2
    se = math.sqrt(variance_a + variance_b)
    df = (variance_a + variance_b) ** 2 / (
        variance_a**2 / (n_a - 1) + variance_b**2 / (n_b - 1)
    )
    alpha = 1.0 - confidence
    critical = float(t.ppf(1.0 - alpha / 2.0, df))
    difference = mean_a - mean_b
    return {
        "difference": difference,
        "standard_error": se,
        "welch_df": df,
        "ci_low": difference - critical * se,
        "ci_high": difference + critical * se,
    }


def sharp_source_contrast_interval(n_lead: float, n_treated: float, coefficient: float = 1.0) -> tuple[float, float]:
    """Sharp interval for one source contrast under N = sum_j a_j x_j.

    There must be at least two nonnegative sources and at least one other source
    with a positive coefficient. The returned contrast is treated minus lead.
    """
    if n_lead <= 0 or n_treated <= 0 or coefficient <= 0:
        raise ValueError("Totals and the selected source coefficient must be positive")
    return (-n_lead / coefficient, n_treated / coefficient)


def source_fraction_contrast_interval(
    baseline_total: float,
    treated_total: float,
    baseline_lower: float,
    baseline_upper: float,
    treated_lower: float,
    treated_upper: float,
) -> tuple[float, float]:
    """Sharp weighted-source contrast interval under external fraction bounds.

    If u_gk = f_gk y_g and f_gk lies in a validated condition-specific
    interval, independent across conditions, the extrema occur at opposite
    fraction endpoints.
    """
    if baseline_total <= 0 or treated_total <= 0:
        raise ValueError("Bulk totals must be positive")
    for lower, upper in ((baseline_lower, baseline_upper), (treated_lower, treated_upper)):
        if not 0 <= lower <= upper <= 1:
            raise ValueError("Fraction bounds must satisfy 0 <= lower <= upper <= 1")
    return (
        treated_lower * treated_total - baseline_upper * baseline_total,
        treated_upper * treated_total - baseline_lower * baseline_total,
    )


def construct_witnesses(
    records: list[dict[str, object]], baseline_group: str = "lead_olive_oil"
) -> dict[str, dict[str, dict[str, list[float]]]]:
    """Two exact eNOS/iNOS decompositions for a baseline/high-dose comparison.

    The default is the primary nominal vehicle-reference comparison. Passing ``lead``
    reproduces the prespecified secondary descriptive comparison.
    """
    heart_lead = float(get_record(records, "heart", baseline_group)["mean_nmol_per_ml"])
    heart_treat = float(get_record(records, "heart", "lead_high_aseo")["mean_nmol_per_ml"])
    kidney_lead = float(get_record(records, "kidney", baseline_group)["mean_nmol_per_ml"])
    kidney_treat = float(get_record(records, "kidney", "lead_high_aseo")["mean_nmol_per_ml"])

    witnesses = {
        "partition_supporting": {
            "heart": {"baseline": [0.10, heart_lead - 0.10], "treated": [heart_treat - 0.10, 0.10]},
            "kidney": {"baseline": [0.10, kidney_lead - 0.10], "treated": [kidney_treat - 0.10, 0.10]},
        },
        "partition_reversing": {
            "heart": {"baseline": [heart_lead - 0.10, 0.10], "treated": [0.10, heart_treat - 0.10]},
            "kidney": {"baseline": [kidney_lead - 0.10, 0.10], "treated": [0.10, kidney_treat - 0.10]},
        },
    }
    return witnesses


def verify_witnesses(
    records: list[dict[str, object]],
    witnesses: dict[str, dict[str, dict[str, list[float]]]],
    baseline_group: str = "lead_olive_oil",
) -> dict[str, object]:
    expected = {
        "heart": {
            "baseline": float(get_record(records, "heart", baseline_group)["mean_nmol_per_ml"]),
            "treated": float(get_record(records, "heart", "lead_high_aseo")["mean_nmol_per_ml"]),
        },
        "kidney": {
            "baseline": float(get_record(records, "kidney", baseline_group)["mean_nmol_per_ml"]),
            "treated": float(get_record(records, "kidney", "lead_high_aseo")["mean_nmol_per_ml"]),
        },
    }
    checks: dict[str, object] = {}
    for witness_name, tissues in witnesses.items():
        witness_checks: dict[str, object] = {}
        for tissue, states in tissues.items():
            sums = {state: float(sum(parts)) for state, parts in states.items()}
            nonnegative = all(value >= -1e-12 for parts in states.values() for value in parts)
            strictly_positive = all(value > 0 for parts in states.values() for value in parts)
            exact = all(math.isclose(sums[state], expected[tissue][state], abs_tol=1e-12) for state in states)
            delta_e = states["treated"][0] - states["baseline"][0]
            delta_i = states["treated"][1] - states["baseline"][1]
            witness_checks[tissue] = {
                "nonnegative": nonnegative,
                "strictly_positive": strictly_positive,
                "totals_exact": exact,
                "delta_eNOS_component": delta_e,
                "delta_iNOS_component": delta_i,
            }
        checks[witness_name] = witness_checks

    support = checks["partition_supporting"]
    reverse = checks["partition_reversing"]
    sign_reversal = (
        support["heart"]["delta_eNOS_component"] > 0
        and reverse["heart"]["delta_eNOS_component"] < 0
        and support["kidney"]["delta_iNOS_component"] < 0
        and reverse["kidney"]["delta_iNOS_component"] > 0
    )
    return {"checks": checks, "claim_signs_reversed": sign_reversal}


def comparison_summary(
    records: list[dict[str, object]], baseline_group: str
) -> dict[str, object]:
    """Return observed contrasts and sharp single-source intervals by tissue."""
    tissues: dict[str, object] = {}
    for tissue in ("heart", "kidney"):
        baseline = float(get_record(records, tissue, baseline_group)["mean_nmol_per_ml"])
        treated = float(get_record(records, tissue, "lead_high_aseo")["mean_nmol_per_ml"])
        interval = list(sharp_source_contrast_interval(baseline, treated))
        tissues[tissue] = {
            "baseline_group": baseline_group,
            "baseline_bulk_nitrite_nmol_per_ml": baseline,
            "high_aseo_bulk_nitrite_nmol_per_ml": treated,
            "high_aseo_minus_baseline_nmol_per_ml": treated - baseline,
            "sharp_eNOS_component_contrast_interval": interval,
            "sharp_iNOS_component_contrast_interval": interval,
            "positive_sign_min_treated_lower_over_baseline_upper": baseline / treated,
            "negative_sign_min_baseline_lower_over_treated_upper": treated / baseline,
        }
    return tissues


def matrix_certificates() -> dict[str, object]:
    matrices = {
        "bulk_nitrite_only": np.array([[1.0, 1.0]]),
        "bulk_plus_proportional_orthogonal_assay": np.array([[1.0, 1.0], [2.0, 2.0]]),
        "bulk_plus_two_ideal_source_sensitive_rows": np.array([[1.0, 1.0], [1.0, 0.0], [0.0, 1.0]]),
    }
    out: dict[str, object] = {}
    for name, matrix in matrices.items():
        singular_values = np.linalg.svd(matrix, compute_uv=False)
        out[name] = {
            "matrix": matrix.tolist(),
            "rank": int(np.linalg.matrix_rank(matrix)),
            "singular_values": singular_values.tolist(),
        }
    return out


def two_sample_t_power(n_per_group: int, standardized_effect: float, alpha: float = 0.05) -> float:
    """Two-sided equal-size two-sample t-test power under a standardized effect."""
    df = 2 * n_per_group - 2
    ncp_value = standardized_effect * math.sqrt(n_per_group / 2.0)
    critical = float(t.ppf(1.0 - alpha / 2.0, df))
    return float(nct.cdf(-critical, df, ncp_value) + 1.0 - nct.cdf(critical, df, ncp_value))


def minimum_n(standardized_effect: float, target_power: float, alpha: float = 0.05) -> int:
    for n in range(2, 1001):
        if two_sample_t_power(n, standardized_effect, alpha) >= target_power:
            return n
    raise RuntimeError("Required n exceeds search cap")


def write_power_grid(path: Path) -> list[dict[str, float | int]]:
    rows: list[dict[str, float | int]] = []
    for effect in (0.5, 0.6, 0.8, 1.0, 1.2, 1.5):
        for target in (0.80, 0.90):
            rows.append(
                {
                    "standardized_effect": effect,
                    "target_power": target,
                    "alpha_two_sided": 0.05,
                    "n_per_group": minimum_n(effect, target),
                }
            )
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=list(rows[0]))
        writer.writeheader()
        writer.writerows(rows)
    return rows


def figure_observations(records: list[dict[str, object]], path_png: Path, path_pdf: Path) -> None:
    groups = ["control", "lead", "lead_olive_oil", "lead_high_aseo"]
    labels = ["Control", "Lead", "Lead + olive oil", "Lead + high ASEO"]
    colors = ["#9AA7B2", "#A53E3E", "#C08A3E", "#2F7D6D"]
    fig, axes = plt.subplots(1, 2, figsize=(10.2, 4.5), constrained_layout=True)
    for axis, tissue in zip(axes, ("heart", "kidney"), strict=True):
        values = [float(get_record(records, tissue, group)["mean_nmol_per_ml"]) for group in groups]
        sems = [get_record(records, tissue, group)["sem_nmol_per_ml"] for group in groups]
        x = np.arange(len(groups))
        if all(value is not None for value in sems):
            yerr = np.array([float(value) for value in sems])
            axis.errorbar(x, values, yerr=yerr, fmt="none", ecolor="#1F2933", capsize=4, lw=1.2, zorder=2)
        axis.scatter(x, values, c=colors, edgecolors="white", linewidths=0.9, s=78, zorder=3)
        axis.set_xticks(x, labels, rotation=17, ha="right")
        if tissue == "heart":
            axis.set_ylabel("Bulk nitrite (nmol/mL)")
        else:
            axis.set_ylabel("Bulk nitrite (micromol/L; numeric nmol/mL equivalent)")
        axis.set_title(f"{tissue.capitalize()} tissue - unlinked report")
        axis.grid(axis="y", color="#D9E0E6", linewidth=0.8, zorder=0)
        note = "mean +/- SEM, n=6" if tissue == "heart" else "NUMERIC UNCERTAINTY UNAVAILABLE; n=6"
        axis.text(0.98, 0.96, note, transform=axis.transAxes, ha="right", va="top", fontsize=8.2,
                  color="#455A64", weight="bold" if tissue == "kidney" else "normal",
                  bbox={"facecolor": "white", "edgecolor": "#CBD5DC", "alpha": 0.92, "pad": 3})
    fig.suptitle(
        "Published tissue-homogenate nitrite: nominal vehicle-reference contrasts\n"
        "(separate reports; no animal-level linkage or common source scale)",
        fontsize=12,
        weight="bold",
    )
    fig.savefig(path_png, dpi=220)
    fig.savefig(path_pdf)
    plt.close(fig)


def figure_witnesses(
    witnesses: dict[str, dict[str, dict[str, list[float]]]], path_png: Path, path_pdf: Path
) -> None:
    fig, axes = plt.subplots(2, 3, figsize=(11.5, 6.8), constrained_layout=True)
    witness_order = ["partition_supporting", "partition_reversing"]
    tissue_order = ["heart", "kidney"]
    colors = ["#2B6F97", "#D47A3A"]
    witness_titles = ["Allocation A: target sign", "Allocation B: reversed target sign"]
    for row, tissue in enumerate(tissue_order):
        tissue_max = max(
            sum(witnesses[witness_name][tissue][state])
            for witness_name in witness_order
            for state in ("baseline", "treated")
        )
        for col, witness_name in enumerate(witness_order):
            axis = axes[row, col]
            states = witnesses[witness_name][tissue]
            values = np.array([states["baseline"], states["treated"]], dtype=float)
            x = np.arange(2)
            axis.bar(x, values[:, 0], color=colors[0], label="eNOS-attributed component")
            axis.bar(x, values[:, 1], bottom=values[:, 0], color=colors[1], label="iNOS-attributed component")
            axis.set_xticks(x, ["Nominal reference", "High ASEO"])
            axis.set_title(witness_titles[col], fontsize=9.5)
            axis.set_ylim(0, tissue_max * 1.22)
            if col == 0:
                source_unit = "nmol/mL" if tissue == "heart" else "micromol/L equivalent"
                axis.set_ylabel(f"{tissue.capitalize()} weighted contributions\n({source_unit})")
            axis.grid(axis="y", color="#E1E7EC", linewidth=0.8, zorder=0)
            for idx, total in enumerate(values.sum(axis=1)):
                axis.text(idx, total + tissue_max * 0.025, f"total {total:.4g}", ha="center", va="bottom", fontsize=8)
            target_label = "Target under audit: Delta u_E" if tissue == "heart" else "Target under audit: Delta u_I"
            axis.text(0.02, 0.97, target_label, transform=axis.transAxes, ha="left", va="top", fontsize=8,
                      weight="bold", color="#194F70")

        geometry = axes[row, 2]
        support_states = witnesses["partition_supporting"][tissue]
        reverse_states = witnesses["partition_reversing"][tissue]
        baseline_total = sum(support_states["baseline"])
        treated_total = sum(support_states["treated"])
        delta_total = treated_total - baseline_total
        delta_e = np.linspace(-baseline_total, treated_total, 300)
        delta_i = delta_total - delta_e
        geometry.plot(delta_e, delta_i, color="#37474F", linewidth=2.0, label="sharp set")
        for witness_name, marker, label in (
            ("partition_supporting", "o", "Allocation A"),
            ("partition_reversing", "s", "Allocation B"),
        ):
            states = witnesses[witness_name][tissue]
            point = np.array(states["treated"]) - np.array(states["baseline"])
            geometry.scatter(point[0], point[1], marker=marker, s=55, label=label, zorder=3)
        geometry.axhline(0, color="#CBD5DC", linewidth=0.8)
        geometry.axvline(0, color="#CBD5DC", linewidth=0.8)
        geometry.set_xlabel("Delta u_E")
        geometry.set_ylabel("Delta u_I")
        geometry.set_title(f"{tissue.capitalize()}: full sharp set", fontsize=9.5)
        geometry.grid(color="#EEF1F4", linewidth=0.7)
        geometry.legend(frameon=False, fontsize=7.5, loc="best")
        geometry.margins(x=0.06, y=0.08)
    handles, labels = axes[0, 0].get_legend_handles_labels()
    fig.legend(handles, labels, loc="outside lower center", ncol=2, frameon=False)
    fig.suptitle(
        "Tissue-specific logical allocations and sharp identified sets\n"
        "(displayed together for convenience; separate unlinked reports)",
        fontsize=12,
        weight="bold",
    )
    fig.savefig(path_png, dpi=220)
    fig.savefig(path_pdf)
    plt.close(fig)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", type=Path, default=EVIDENCE)
    args = parser.parse_args()
    out = args.output_dir.resolve()
    out.mkdir(parents=True, exist_ok=True)

    records = read_records()
    heart_lead = get_record(records, "heart", "lead")
    heart_vehicle = get_record(records, "heart", "lead_olive_oil")
    heart_treat = get_record(records, "heart", "lead_high_aseo")
    heart_lead_ci = welch_difference_ci(
        float(heart_treat["mean_nmol_per_ml"]),
        float(heart_treat["sem_nmol_per_ml"]),
        int(heart_treat["n"]),
        float(heart_lead["mean_nmol_per_ml"]),
        float(heart_lead["sem_nmol_per_ml"]),
        int(heart_lead["n"]),
    )
    heart_vehicle_ci = welch_difference_ci(
        float(heart_treat["mean_nmol_per_ml"]),
        float(heart_treat["sem_nmol_per_ml"]),
        int(heart_treat["n"]),
        float(heart_vehicle["mean_nmol_per_ml"]),
        float(heart_vehicle["sem_nmol_per_ml"]),
        int(heart_vehicle["n"]),
    )

    primary_witnesses = construct_witnesses(records, "lead_olive_oil")
    primary_witness_certificate = verify_witnesses(records, primary_witnesses, "lead_olive_oil")
    secondary_witnesses = construct_witnesses(records, "lead")
    secondary_witness_certificate = verify_witnesses(records, secondary_witnesses, "lead")
    primary_comparison = comparison_summary(records, "lead_olive_oil")
    secondary_comparison = comparison_summary(records, "lead")

    power_rows = write_power_grid(out / "prospective_power_grid.csv")
    summary = {
        "scope": "Published aggregate values and deterministic identifiability calculations; no new animal data",
        "unit_identity": "1 micromol/L = 1 nmol/mL",
        "primary_nominal_vehicle_reference_analysis": {
            "comparison": "lead_high_aseo minus lead_olive_oil",
            "rationale": "The reported lead-plus-olive-oil group is used as a nominal vehicle reference; causal matching is not assumed",
            "tissues": primary_comparison,
            "heart_aggregate_welch_approximation_from_reported_sem": heart_vehicle_ci,
            "witness_certificate": primary_witness_certificate,
            "witnesses": primary_witnesses,
        },
        "secondary_lead_alone_analysis": {
            "comparison": "lead_high_aseo minus lead",
            "rationale": "Retained as a prespecified secondary descriptive comparison; it is not nominal vehicle-referenced",
            "tissues": secondary_comparison,
            "heart_aggregate_welch_approximation_from_reported_sem": heart_lead_ci,
            "witness_certificate": secondary_witness_certificate,
            "witnesses": secondary_witnesses,
        },
        "measurement_matrix_certificates": matrix_certificates(),
        "prospective_power_grid": power_rows,
        "power_grid_assumption": "Two-sided alpha 0.05, equal group sizes, independent Gaussian outcomes, standardized effect known",
    }
    (out / "verification_summary.json").write_text(json.dumps(summary, indent=2), encoding="utf-8")
    figure_observations(records, out / "published_bulk_directions.png", out / "published_bulk_directions.pdf")
    figure_witnesses(
        primary_witnesses,
        out / "source_partition_witnesses.png",
        out / "source_partition_witnesses.pdf",
    )
    print(json.dumps(summary, indent=2))


if __name__ == "__main__":
    main()
