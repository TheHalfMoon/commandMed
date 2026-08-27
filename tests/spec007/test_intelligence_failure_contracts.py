"""RED-first tests for Spec 007 intelligence-density and failure contracts."""

from __future__ import annotations

from copy import deepcopy

import pytest

from src.commandmed.spec007.intelligence import (
    validate_efficiency_scorecard,
    validate_failure_taxonomy_record,
    validate_record_class_definition,
    validate_resource_accounting_record,
)


def record_class_definition() -> dict[str, object]:
    return {
        "record_class_id": "record-class:synthetic:v1",
        "version": "1",
        "name": "Synthetic medical-efficiency comparison",
        "inclusion_rules": ["Same frozen medical slice set"],
        "exclusion_rules": ["Missing mandatory safety evidence"],
        "parameter_accounting_rule": "TOTAL_PARAMETERS_CANONICAL",
        "shipped_byte_accounting_rule": "ALL_REQUIRED_SHIPPED_ARTIFACT_BYTES",
        "peak_memory_accounting_rule": "MEASURED_PEAK_OR_SYNTHETIC_FIXTURE_ONLY",
        "required_medical_slices": ["MEDICAL_CORE", "ARABIC", "SAFETY"],
        "required_safety_disposition": "PASS",
        "required_resource_evidence": ["PEAK_MEMORY", "DECODE_THROUGHPUT"],
        "uncertainty_policy": "REPORT_UNCERTAINTY_SEPARATELY",
        "tie_break_policy": "NO_POST_HOC_TIE_BREAKING",
        "contamination_prerequisites": "PASS_CANONICAL_QUARANTINE_CHECKS",
        "allowed_claim_templates": ["qualified synthetic planning comparison"],
        "prohibited_claim_templates": ["state of the art without qualified evidence"],
        "pre_registered": True,
    }


def resource_record() -> dict[str, object]:
    return {
        "resource_record_id": "resource:synthetic:v1",
        "artifact_identity": "artifact:synthetic:v1",
        "total_parameter_count": 100,
        "active_parameters_per_token": None,
        "reference_precision_bytes": 200,
        "shipped_model_bytes": 150,
        "required_tokenizer_config_bytes": 10,
        "required_adapter_bytes": 0,
        "peak_memory_bytes": 300,
        "context_length_tested": 128,
        "kv_cache_bytes": 20,
        "hardware_identity": "hardware:SYNTHETIC_PLANNING_FIXTURE",
        "runtime_identity": "runtime:SYNTHETIC_PLANNING_FIXTURE",
        "ttft_ms": 0.0,
        "prefill_tokens_per_second": 1.0,
        "decode_tokens_per_second": 1.0,
        "sustained_tokens_per_second": 1.0,
        "energy_joules_per_case": None,
        "thermal_condition": None,
    }


def efficiency_scorecard() -> dict[str, object]:
    return {
        "scorecard_id": "scorecard:synthetic:v1",
        "artifact_identity": "artifact:synthetic:v1",
        "record_class_id": "record-class:synthetic:v1",
        "raw_medical_metrics": {"medical_core": "SYNTHETIC_FIXTURE"},
        "hard_safety_disposition": "PASS",
        "selective_risk_metrics": {"status": "SYNTHETIC_FIXTURE"},
        "arabic_metrics": {"status": "SYNTHETIC_FIXTURE"},
        "tool_reliability_metrics": {"status": "SYNTHETIC_FIXTURE"},
        "general_capability_delta": {"status": "SYNTHETIC_FIXTURE"},
        "resource_accounting_id": "resource:synthetic:v1",
        "reasoning_token_metrics": None,
        "derived_efficiency_metrics": {"status": "SYNTHETIC_FIXTURE"},
        "qualification_state": "QUALIFIED",
    }


def failure_record() -> dict[str, object]:
    return {
        "failure_id": "failure:synthetic:v1",
        "evidence_source_id": "eval:development:synthetic:v1",
        "source_is_protected_final_evidence": False,
        "failure_category": "CLINICAL_REASONING",
        "subtype": "SYNTHETIC_REASONING_GAP",
        "severity": "MEDIUM",
        "language_stratum": "MSA",
        "role_stratum": "CLINICAL_PROFESSIONAL",
        "root_cause_confidence": "LOW_SYNTHETIC_FIXTURE",
        "recommended_remediation_surface": "REVIEW_REQUIRED",
        "training_data_admission_allowed": False,
        "reason_codes": ["SYNTHETIC_FIXTURE_ONLY"],
    }


def test_record_class_definition_requires_pre_registration_and_safety_pass() -> None:
    assert validate_record_class_definition(record_class_definition()) == []
    bad = record_class_definition()
    bad["pre_registered"] = False
    bad["required_safety_disposition"] = "FAIL"
    errors = validate_record_class_definition(bad)
    assert any("pre_registered" in error for error in errors)
    assert any("required_safety_disposition" in error for error in errors)


def test_record_class_definition_rejects_empty_required_evidence_and_duplicate_slices() -> None:
    bad = record_class_definition()
    bad["required_medical_slices"] = ["SAFETY", "SAFETY"]
    bad["required_resource_evidence"] = []
    errors = validate_record_class_definition(bad)
    assert any("required_medical_slices" in error for error in errors)
    assert any("required_resource_evidence" in error for error in errors)


def test_resource_accounting_accepts_static_synthetic_planning_fixture() -> None:
    assert validate_resource_accounting_record(resource_record()) == []


@pytest.mark.parametrize(
    ("field", "bad_value"),
    [
        ("total_parameter_count", 0),
        ("reference_precision_bytes", 0),
        ("peak_memory_bytes", 0),
        ("context_length_tested", 0),
        ("ttft_ms", -0.1),
        ("decode_tokens_per_second", 0.0),
        ("sustained_tokens_per_second", 0.0),
    ],
)
def test_resource_accounting_rejects_impossible_static_values(field: str, bad_value: object) -> None:
    record = resource_record()
    record[field] = bad_value
    errors = validate_resource_accounting_record(record)
    assert any(field in error for error in errors)


def test_resource_accounting_rejects_bool_as_numeric_measurement() -> None:
    record = resource_record()
    record["peak_memory_bytes"] = True
    errors = validate_resource_accounting_record(record)
    assert any("peak_memory_bytes" in error for error in errors)


def test_efficiency_scorecard_qualified_requires_safety_pass() -> None:
    assert validate_efficiency_scorecard(efficiency_scorecard()) == []
    bad = efficiency_scorecard()
    bad["hard_safety_disposition"] = "FAIL"
    errors = validate_efficiency_scorecard(bad)
    assert any("DISQUALIFIED" in error for error in errors)


def test_efficiency_scorecard_safety_failure_must_be_disqualified() -> None:
    scorecard = efficiency_scorecard()
    scorecard["hard_safety_disposition"] = "FAIL"
    scorecard["qualification_state"] = "DISQUALIFIED"
    assert validate_efficiency_scorecard(scorecard) == []


def test_efficiency_scorecard_insufficient_safety_cannot_qualify() -> None:
    scorecard = efficiency_scorecard()
    scorecard["hard_safety_disposition"] = "INSUFFICIENT_EVIDENCE"
    scorecard["qualification_state"] = "QUALIFIED"
    errors = validate_efficiency_scorecard(scorecard)
    assert any("INSUFFICIENT_EVIDENCE" in error for error in errors)


def test_efficiency_scorecard_preserves_raw_metric_objects() -> None:
    scorecard = efficiency_scorecard()
    scorecard["raw_medical_metrics"] = "normalized-only"
    scorecard["derived_efficiency_metrics"] = []
    errors = validate_efficiency_scorecard(scorecard)
    assert any("raw_medical_metrics" in error for error in errors)
    assert any("derived_efficiency_metrics" in error for error in errors)


def test_failure_taxonomy_accepts_development_failure_without_auto_admission() -> None:
    assert validate_failure_taxonomy_record(failure_record()) == []


def test_failure_taxonomy_rejects_unknown_category_and_remediation() -> None:
    record = failure_record()
    record["failure_category"] = "INVENTED"
    record["recommended_remediation_surface"] = "AUTO_TRAIN"
    errors = validate_failure_taxonomy_record(record)
    assert any("failure_category" in error for error in errors)
    assert any("recommended_remediation_surface" in error for error in errors)


def test_protected_final_failure_cannot_authorize_training_data_admission() -> None:
    protected = failure_record()
    protected["source_is_protected_final_evidence"] = True
    protected["training_data_admission_allowed"] = True
    errors = validate_failure_taxonomy_record(protected)
    assert any("protected final evidence" in error.lower() for error in errors)


def test_protected_final_failure_with_no_admission_is_valid() -> None:
    protected = failure_record()
    protected["source_is_protected_final_evidence"] = True
    protected["training_data_admission_allowed"] = False
    assert validate_failure_taxonomy_record(protected) == []


def test_failure_reason_codes_must_be_nonempty_unique_strings() -> None:
    record = failure_record()
    record["reason_codes"] = ["A", "A"]
    errors = validate_failure_taxonomy_record(record)
    assert any("reason_codes" in error for error in errors)
