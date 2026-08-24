from __future__ import annotations

import importlib.util
import math
from pathlib import Path

import numpy as np
import pytest


RUN_ROOT = Path(__file__).resolve().parents[1]
MODULE_PATH = RUN_ROOT / "code" / "analyze_identifiability.py"
SPEC = importlib.util.spec_from_file_location("analyze_identifiability", MODULE_PATH)
assert SPEC and SPEC.loader
analysis = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(analysis)


def assert_close(actual: float, expected: float, tolerance: float = 1e-12) -> None:
    assert math.isclose(actual, expected, rel_tol=tolerance, abs_tol=tolerance)


def test_all_reported_group_means_and_available_sems_match_the_source_tables() -> None:
    records = analysis.read_records()
    assert len(records) == 12

    expected = {
        ("heart", "control"): (10.43, 0.14),
        ("heart", "lead"): (1.38, 0.08),
        ("heart", "lead_low_aseo"): (1.82, 0.10),
        ("heart", "lead_high_aseo"): (6.29, 0.24),
        ("heart", "lead_silymarin"): (2.00, 0.04),
        ("heart", "lead_olive_oil"): (2.24, 0.04),
        ("kidney", "control"): (1.25, None),
        ("kidney", "lead"): (2.022, None),
        ("kidney", "lead_low_aseo"): (1.1216, None),
        ("kidney", "lead_high_aseo"): (0.7162, None),
        ("kidney", "lead_silymarin"): (0.6711, None),
        ("kidney", "lead_olive_oil"): (1.43, None),
    }

    observed = {(record["tissue"], record["group"]): record for record in records}
    assert set(observed) == set(expected)
    for key, (mean, sem) in expected.items():
        record = observed[key]
        assert_close(float(record["mean_reported"]), mean)
        assert_close(float(record["mean_nmol_per_ml"]), mean)
        if sem is None:
            assert record["sem_reported"] is None
            assert record["sem_nmol_per_ml"] is None
        else:
            assert_close(float(record["sem_reported"]), sem)
            assert_close(float(record["sem_nmol_per_ml"]), sem)


def test_kidney_unit_harmonization_applies_physical_conversion() -> None:
    # 1 micromol/L * (1000 nmol/micromol) / (1000 mL/L) = 1 nmol/mL.
    assert_close(analysis.micromol_per_l_to_nmol_per_ml(2.5), 2.5)
    records = analysis.read_records()
    renal_records = [record for record in records if record["reported_unit"] == "micromol/L"]
    assert len(renal_records) == 6
    for record in renal_records:
        converted = analysis.micromol_per_l_to_nmol_per_ml(float(record["mean_reported"]))
        assert_close(converted, float(record["mean_nmol_per_ml"]))


def test_primary_nominal_vehicle_reference_heart_welch_approximation() -> None:
    result = analysis.welch_difference_ci(6.29, 0.24, 6, 2.24, 0.04, 6)
    expected = {
        "difference": 4.05,
        "standard_error": 0.2433105012119288,
        "welch_df": 5.277563608326907,
        "ci_low": 3.4343160045039376,
        "ci_high": 4.665683995496062,
    }
    for key, value in expected.items():
        assert_close(result[key], value)


def test_secondary_lead_alone_heart_welch_approximation() -> None:
    result = analysis.welch_difference_ci(6.29, 0.24, 6, 1.38, 0.08, 6)
    expected = {
        "difference": 4.91,
        "standard_error": 0.25298221281347033,
        "welch_df": 6.097560975609756,
        "ci_low": 4.293367770100864,
        "ci_high": 5.526632229899136,
    }
    for key, value in expected.items():
        assert_close(result[key], value)


def test_primary_nominal_vehicle_reference_contrasts_and_sharp_endpoints() -> None:
    primary = analysis.comparison_summary(analysis.read_records(), "lead_olive_oil")
    expected = {
        "heart": (2.24, 6.29, 4.05, [-2.24, 6.29]),
        "kidney": (1.43, 0.7162, -0.7138, [-1.43, 0.7162]),
    }
    for tissue, (baseline, treated, difference, interval) in expected.items():
        result = primary[tissue]
        assert result["baseline_group"] == "lead_olive_oil"
        assert_close(result["baseline_bulk_nitrite_nmol_per_ml"], baseline)
        assert_close(result["high_aseo_bulk_nitrite_nmol_per_ml"], treated)
        assert_close(result["high_aseo_minus_baseline_nmol_per_ml"], difference)
        assert result["sharp_eNOS_component_contrast_interval"] == interval
        assert result["sharp_iNOS_component_contrast_interval"] == interval
        assert_close(result["positive_sign_min_treated_lower_over_baseline_upper"], baseline / treated)
        assert_close(result["negative_sign_min_baseline_lower_over_treated_upper"], treated / baseline)


def test_source_fraction_bounds_are_sharp_and_give_sign_conditions() -> None:
    heart = analysis.source_fraction_contrast_interval(2.24, 6.29, 0.20, 0.40, 0.30, 0.60)
    assert_close(heart[0], 0.30 * 6.29 - 0.40 * 2.24)
    assert_close(heart[1], 0.60 * 6.29 - 0.20 * 2.24)
    assert heart[0] > 0

    kidney = analysis.source_fraction_contrast_interval(1.43, 0.7162, 0.60, 0.90, 0.10, 0.50)
    assert_close(kidney[0], 0.10 * 0.7162 - 0.90 * 1.43)
    assert_close(kidney[1], 0.50 * 0.7162 - 0.60 * 1.43)
    assert kidney[1] < 0


@pytest.mark.parametrize(
    "arguments",
    [
        (0.0, 1.0, 0.0, 1.0, 0.0, 1.0),
        (1.0, 1.0, -0.1, 0.5, 0.0, 1.0),
        (1.0, 1.0, 0.7, 0.5, 0.0, 1.0),
        (1.0, 1.0, 0.0, 1.0, 0.0, 1.1),
    ],
)
def test_source_fraction_bounds_reject_invalid_inputs(arguments: tuple[float, ...]) -> None:
    with pytest.raises(ValueError):
        analysis.source_fraction_contrast_interval(*arguments)


def test_secondary_lead_alone_contrasts_and_sharp_endpoints() -> None:
    secondary = analysis.comparison_summary(analysis.read_records(), "lead")
    expected = {
        "heart": (1.38, 6.29, 4.91, [-1.38, 6.29]),
        "kidney": (2.022, 0.7162, -1.3058, [-2.022, 0.7162]),
    }
    for tissue, (baseline, treated, difference, interval) in expected.items():
        result = secondary[tissue]
        assert result["baseline_group"] == "lead"
        assert_close(result["baseline_bulk_nitrite_nmol_per_ml"], baseline)
        assert_close(result["high_aseo_bulk_nitrite_nmol_per_ml"], treated)
        assert_close(result["high_aseo_minus_baseline_nmol_per_ml"], difference)
        assert result["sharp_eNOS_component_contrast_interval"] == interval
        assert result["sharp_iNOS_component_contrast_interval"] == interval


def test_primary_witnesses_have_exact_components_sums_and_opposite_signs() -> None:
    records = analysis.read_records()
    witnesses = analysis.construct_witnesses(records, "lead_olive_oil")
    expected = {
        "partition_supporting": {
            "heart": {"baseline": [0.10, 2.14], "treated": [6.19, 0.10]},
            "kidney": {"baseline": [0.10, 1.33], "treated": [0.6162, 0.10]},
        },
        "partition_reversing": {
            "heart": {"baseline": [2.14, 0.10], "treated": [0.10, 6.19]},
            "kidney": {"baseline": [1.33, 0.10], "treated": [0.10, 0.6162]},
        },
    }
    for world, tissues in expected.items():
        for tissue, states in tissues.items():
            assert np.allclose(witnesses[world][tissue]["baseline"], states["baseline"], atol=1e-12)
            assert np.allclose(witnesses[world][tissue]["treated"], states["treated"], atol=1e-12)
            observed_totals = [sum(witnesses[world][tissue][state]) for state in ("baseline", "treated")]
            expected_totals = [sum(states[state]) for state in ("baseline", "treated")]
            assert np.allclose(observed_totals, expected_totals, atol=1e-12)
            assert min(value for parts in witnesses[world][tissue].values() for value in parts) > 0

    supporting = witnesses["partition_supporting"]
    reversing = witnesses["partition_reversing"]
    assert supporting["heart"]["treated"][0] - supporting["heart"]["baseline"][0] > 0
    assert reversing["heart"]["treated"][0] - reversing["heart"]["baseline"][0] < 0
    assert supporting["kidney"]["treated"][1] - supporting["kidney"]["baseline"][1] < 0
    assert reversing["kidney"]["treated"][1] - reversing["kidney"]["baseline"][1] > 0


def test_primary_and_secondary_witness_certificates_reconstruct_their_baselines() -> None:
    records = analysis.read_records()
    for baseline_group in ("lead_olive_oil", "lead"):
        witnesses = analysis.construct_witnesses(records, baseline_group)
        certificate = analysis.verify_witnesses(records, witnesses, baseline_group)
        assert certificate["claim_signs_reversed"]
        for world in certificate["checks"].values():
            for tissue in world.values():
                assert tissue["strictly_positive"]
                assert tissue["totals_exact"]


def test_measurement_matrix_certificates_have_expected_ranks_and_row_spaces() -> None:
    certificates = analysis.matrix_certificates()
    assert certificates["bulk_nitrite_only"]["rank"] == 1
    assert certificates["bulk_plus_proportional_orthogonal_assay"]["rank"] == 1
    assert certificates["bulk_plus_two_ideal_source_sensitive_rows"]["rank"] == 2

    bulk = np.array(certificates["bulk_nitrite_only"]["matrix"])
    proportional = np.array(certificates["bulk_plus_proportional_orthogonal_assay"]["matrix"])
    full = np.array(certificates["bulk_plus_two_ideal_source_sensitive_rows"]["matrix"])
    assert np.linalg.matrix_rank(np.vstack([bulk, proportional])) == 1
    assert np.linalg.matrix_rank(full) == 2

    enos_target = np.array([1.0, 0.0])
    total_target = np.array([1.0, 1.0])
    bulk_projection = bulk.T @ np.linalg.pinv(bulk @ bulk.T) @ bulk
    assert not np.allclose(bulk_projection @ enos_target, enos_target)
    assert np.allclose(bulk_projection @ total_target, total_target)


def test_power_is_monotone_and_minimum_n_crosses_target() -> None:
    assert analysis.two_sample_t_power(30, 0.8) > analysis.two_sample_t_power(20, 0.8)
    assert analysis.two_sample_t_power(20, 1.0) > analysis.two_sample_t_power(20, 0.8)
    for effect in (0.5, 0.8, 1.0):
        n = analysis.minimum_n(effect, 0.90)
        assert analysis.two_sample_t_power(n, effect) >= 0.90
        assert analysis.two_sample_t_power(n - 1, effect) < 0.90


@pytest.mark.parametrize("baseline,treated", [(0.0, 1.0), (1.0, 0.0), (-1.0, 1.0)])
def test_sharp_interval_rejects_nonpositive_totals(baseline: float, treated: float) -> None:
    with pytest.raises(ValueError):
        analysis.sharp_source_contrast_interval(baseline, treated)
