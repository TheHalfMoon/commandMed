"""Offline intelligence-density, resource-accounting, and failure contracts.

All validators in this module operate on supplied static records only. They do
not measure hardware, execute a runtime, run a model, or authorize training-data
admission from protected evaluation evidence.
"""

from __future__ import annotations

from typing import Any

from src.commandmed.spec007.foundation import validate_closed_object

_RECORD_CLASS_FIELDS = (
    "record_class_id",
    "version",
    "name",
    "inclusion_rules",
    "exclusion_rules",
    "parameter_accounting_rule",
    "shipped_byte_accounting_rule",
    "peak_memory_accounting_rule",
    "required_medical_slices",
    "required_safety_disposition",
    "required_resource_evidence",
    "uncertainty_policy",
    "tie_break_policy",
    "contamination_prerequisites",
    "allowed_claim_templates",
    "prohibited_claim_templates",
    "pre_registered",
)

_RESOURCE_REQUIRED_FIELDS = (
    "resource_record_id",
    "artifact_identity",
    "total_parameter_count",
    "reference_precision_bytes",
    "shipped_model_bytes",
    "required_tokenizer_config_bytes",
    "required_adapter_bytes",
    "peak_memory_bytes",
    "context_length_tested",
    "kv_cache_bytes",
    "hardware_identity",
    "runtime_identity",
    "ttft_ms",
    "prefill_tokens_per_second",
    "decode_tokens_per_second",
    "sustained_tokens_per_second",
)
_RESOURCE_OPTIONAL_FIELDS = (
    "active_parameters_per_token",
    "energy_joules_per_case",
    "thermal_condition",
)

_SCORECARD_REQUIRED_FIELDS = (
    "scorecard_id",
    "artifact_identity",
    "raw_medical_metrics",
    "hard_safety_disposition",
    "selective_risk_metrics",
    "arabic_metrics",
    "tool_reliability_metrics",
    "general_capability_delta",
    "resource_accounting_id",
    "derived_efficiency_metrics",
    "qualification_state",
)
_SCORECARD_OPTIONAL_FIELDS = ("record_class_id", "reasoning_token_metrics")
_SAFETY_DISPOSITIONS = frozenset({"PASS", "FAIL", "INSUFFICIENT_EVIDENCE"})
_QUALIFICATION_STATES = frozenset({"QUALIFIED", "DISQUALIFIED", "INSUFFICIENT_EVIDENCE"})

_FAILURE_FIELDS = (
    "failure_id",
    "evidence_source_id",
    "source_is_protected_final_evidence",
    "failure_category",
    "subtype",
    "severity",
    "language_stratum",
    "role_stratum",
    "root_cause_confidence",
    "recommended_remediation_surface",
    "training_data_admission_allowed",
    "reason_codes",
)
_FAILURE_CATEGORIES = frozenset(
    {
        "FACTUAL_KNOWLEDGE",
        "CLINICAL_REASONING",
        "ACTIVE_INFORMATION_ACQUISITION",
        "EVIDENCE_USE",
        "TOOL_SELECTION_OR_ARGUMENTS",
        "TOOL_RESULT_TRUST",
        "ABSTENTION_OR_OVERANSWERING",
        "ESCALATION_OR_EMERGENCY",
        "PATIENT_COMMUNICATION",
        "PROFESSIONAL_WORKFLOW",
        "ARABIC_OR_CODE_SWITCH",
        "STRUCTURED_OUTPUT",
        "PROVENANCE_OR_DATA",
        "EVALUATION_AMBIGUITY",
        "MUTABLE_KNOWLEDGE_PLACEMENT",
        "GENERAL_CAPABILITY_REGRESSION",
        "OTHER_REVIEW_REQUIRED",
    }
)
_REMEDIATION_SURFACES = frozenset(
    {
        "SFT_DATA",
        "RETRIEVAL_EVIDENCE",
        "DETERMINISTIC_TOOL",
        "SAFETY_POLICY",
        "EVALUATION_REPAIR",
        "NO_ACTION",
        "REVIEW_REQUIRED",
    }
)


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _validate_string_list(
    value: Any,
    field: str,
    *,
    min_items: int = 0,
    unique: bool = False,
    allow_empty_strings: bool = False,
) -> list[str]:
    if not isinstance(value, list):
        return [f"{field}: expected list"]
    errors: list[str] = []
    if len(value) < min_items:
        errors.append(f"{field}: requires at least {min_items} item(s)")
    if allow_empty_strings:
        bad = any(not isinstance(item, str) for item in value)
    else:
        bad = any(not _nonempty(item) for item in value)
    if bad:
        errors.append(f"{field}: entries must be strings" + ("" if allow_empty_strings else " and non-empty"))
    if unique and len(value) != len(set(item for item in value if isinstance(item, str))):
        errors.append(f"{field}: entries must be unique")
    return errors


def _is_int(value: Any) -> bool:
    return type(value) is int


def _is_number(value: Any) -> bool:
    return type(value) in (int, float)


def validate_record_class_definition(record: Any) -> list[str]:
    """Validate a pre-registered comparison class with mandatory safety PASS."""
    prefix = "RecordClassDefinition"
    errors = validate_closed_object(record, required_fields=_RECORD_CLASS_FIELDS, field=prefix)
    if errors or not isinstance(record, dict):
        return errors

    scalar_fields = (
        "record_class_id",
        "version",
        "name",
        "parameter_accounting_rule",
        "shipped_byte_accounting_rule",
        "peak_memory_accounting_rule",
        "uncertainty_policy",
        "tie_break_policy",
        "contamination_prerequisites",
    )
    for field in scalar_fields:
        if not _nonempty(record.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")

    errors.extend(_validate_string_list(record.get("inclusion_rules"), f"{prefix}.inclusion_rules", min_items=1))
    errors.extend(_validate_string_list(record.get("exclusion_rules"), f"{prefix}.exclusion_rules"))
    errors.extend(
        _validate_string_list(
            record.get("required_medical_slices"),
            f"{prefix}.required_medical_slices",
            min_items=1,
            unique=True,
        )
    )
    errors.extend(
        _validate_string_list(
            record.get("required_resource_evidence"),
            f"{prefix}.required_resource_evidence",
            min_items=1,
            unique=True,
        )
    )
    errors.extend(
        _validate_string_list(
            record.get("allowed_claim_templates"),
            f"{prefix}.allowed_claim_templates",
            allow_empty_strings=True,
        )
    )
    errors.extend(
        _validate_string_list(
            record.get("prohibited_claim_templates"),
            f"{prefix}.prohibited_claim_templates",
            min_items=1,
            allow_empty_strings=True,
        )
    )
    if record.get("required_safety_disposition") != "PASS":
        errors.append(f"{prefix}: required_safety_disposition must equal 'PASS'")
    if record.get("pre_registered") is not True:
        errors.append(f"{prefix}: pre_registered must be true")
    return errors


def validate_resource_accounting_record(record: Any) -> list[str]:
    """Validate supplied raw resource values without performing any measurement."""
    prefix = "ResourceAccountingRecord"
    errors = validate_closed_object(
        record,
        required_fields=_RESOURCE_REQUIRED_FIELDS,
        optional_fields=_RESOURCE_OPTIONAL_FIELDS,
        field=prefix,
    )
    if errors or not isinstance(record, dict):
        return errors

    for field in ("resource_record_id", "artifact_identity", "hardware_identity", "runtime_identity"):
        if not _nonempty(record.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")

    positive_ints = (
        "total_parameter_count",
        "reference_precision_bytes",
        "shipped_model_bytes",
        "peak_memory_bytes",
        "context_length_tested",
    )
    nonnegative_ints = (
        "required_tokenizer_config_bytes",
        "required_adapter_bytes",
        "kv_cache_bytes",
    )
    for field in positive_ints:
        value = record.get(field)
        if not _is_int(value) or value < 1:
            errors.append(f"{prefix}: {field} must be an integer >= 1")
    for field in nonnegative_ints:
        value = record.get(field)
        if not _is_int(value) or value < 0:
            errors.append(f"{prefix}: {field} must be an integer >= 0")

    active = record.get("active_parameters_per_token")
    if active is not None and (not _is_int(active) or active < 1):
        errors.append(f"{prefix}: active_parameters_per_token must be integer >= 1 or null")

    ttft = record.get("ttft_ms")
    if not _is_number(ttft) or ttft < 0:
        errors.append(f"{prefix}: ttft_ms must be a number >= 0")
    for field in ("prefill_tokens_per_second", "decode_tokens_per_second", "sustained_tokens_per_second"):
        value = record.get(field)
        if not _is_number(value) or value <= 0:
            errors.append(f"{prefix}: {field} must be a number > 0")

    energy = record.get("energy_joules_per_case")
    if energy is not None and (not _is_number(energy) or energy < 0):
        errors.append(f"{prefix}: energy_joules_per_case must be a number >= 0 or null")
    thermal = record.get("thermal_condition")
    if thermal is not None and not isinstance(thermal, str):
        errors.append(f"{prefix}: thermal_condition must be string or null")
    return errors


def validate_efficiency_scorecard(scorecard: Any) -> list[str]:
    """Validate raw+derived scorecard data while preserving hard-safety qualification rules."""
    prefix = "EfficiencyScorecard"
    errors = validate_closed_object(
        scorecard,
        required_fields=_SCORECARD_REQUIRED_FIELDS,
        optional_fields=_SCORECARD_OPTIONAL_FIELDS,
        field=prefix,
    )
    if errors or not isinstance(scorecard, dict):
        return errors

    for field in ("scorecard_id", "artifact_identity", "resource_accounting_id"):
        if not _nonempty(scorecard.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")
    record_class = scorecard.get("record_class_id")
    if record_class is not None and not isinstance(record_class, str):
        errors.append(f"{prefix}: record_class_id must be string or null")

    for field in (
        "raw_medical_metrics",
        "selective_risk_metrics",
        "arabic_metrics",
        "tool_reliability_metrics",
        "general_capability_delta",
        "derived_efficiency_metrics",
    ):
        if not isinstance(scorecard.get(field), dict):
            errors.append(f"{prefix}: {field} must be an object")
    reasoning = scorecard.get("reasoning_token_metrics")
    if reasoning is not None and not isinstance(reasoning, dict):
        errors.append(f"{prefix}: reasoning_token_metrics must be object or null")

    safety = scorecard.get("hard_safety_disposition")
    qualification = scorecard.get("qualification_state")
    if safety not in _SAFETY_DISPOSITIONS:
        errors.append(f"{prefix}: unsupported hard_safety_disposition")
    if qualification not in _QUALIFICATION_STATES:
        errors.append(f"{prefix}: unsupported qualification_state")

    if safety == "FAIL" and qualification != "DISQUALIFIED":
        errors.append(f"{prefix}: hard safety FAIL requires qualification_state='DISQUALIFIED'")
    if safety == "INSUFFICIENT_EVIDENCE" and qualification != "INSUFFICIENT_EVIDENCE":
        errors.append(
            f"{prefix}: hard safety INSUFFICIENT_EVIDENCE requires "
            "qualification_state='INSUFFICIENT_EVIDENCE'"
        )
    if qualification == "QUALIFIED" and safety != "PASS":
        errors.append(f"{prefix}: QUALIFIED requires hard_safety_disposition='PASS'")
    return errors


def validate_failure_taxonomy_record(record: Any) -> list[str]:
    """Validate failure classification and block protected-final evidence recycling."""
    prefix = "FailureTaxonomyRecord"
    errors = validate_closed_object(record, required_fields=_FAILURE_FIELDS, field=prefix)
    if errors or not isinstance(record, dict):
        return errors

    for field in (
        "failure_id",
        "evidence_source_id",
        "subtype",
        "severity",
        "language_stratum",
        "role_stratum",
        "root_cause_confidence",
    ):
        if not _nonempty(record.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")

    if type(record.get("source_is_protected_final_evidence")) is not bool:
        errors.append(f"{prefix}: source_is_protected_final_evidence must be boolean")
    if record.get("failure_category") not in _FAILURE_CATEGORIES:
        errors.append(f"{prefix}: unsupported failure_category")
    if record.get("recommended_remediation_surface") not in _REMEDIATION_SURFACES:
        errors.append(f"{prefix}: unsupported recommended_remediation_surface")
    if type(record.get("training_data_admission_allowed")) is not bool:
        errors.append(f"{prefix}: training_data_admission_allowed must be boolean")

    errors.extend(
        _validate_string_list(
            record.get("reason_codes"),
            f"{prefix}.reason_codes",
            min_items=1,
            unique=True,
        )
    )
    if (
        record.get("source_is_protected_final_evidence") is True
        and record.get("training_data_admission_allowed") is not False
    ):
        errors.append(
            f"{prefix}: protected final evidence cannot authorize training-data admission"
        )
    return errors
