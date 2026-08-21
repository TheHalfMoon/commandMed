"""Fail-closed semantic validation for commandMed evaluation governance contracts."""

from __future__ import annotations

import re
from typing import Any

from .model import (
    AccessClass,
    CapabilityDomain,
    ContaminationSensitivity,
    GateEvaluationState,
    GoldFamilyId,
    IntendedUse,
    MetricDirection,
    Modality,
    Purpose,
    Role,
    ThresholdState,
    VerificationStatus,
)

# Date format regex YYYY-MM-DD
DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")

# Disallowed payload keys that must never appear in metadata artifacts
PROHIBITED_PAYLOAD_KEYS = {
    "patient_name",
    "mrn",
    "raw_phi",
    "case_payload",
    "case_text",
    "question_text",
    "gold_label_answers",
    "real_cases",
}

# Required prohibited uses for any private Gold protocol
MANDATORY_GOLD_PROHIBITIONS = {
    "TRAIN",
    "CPT",
    "SFT",
    "TEACHER_GEN",
    "DISTILLATION",
    "DPO_RL",
    "PROMPT_TUNING",
    "HYPERPARAMETER_SELECTION",
    "CHECKPOINT_SELECTION",
    "BACKBONE_SELECTION",
}


def check_no_payload_markers(obj: Any, path: str = "") -> list[str]:
    """Recursively check that no prohibited case/PHI payload keys exist."""
    errors: list[str] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            current_path = f"{path}.{k}" if path else str(k)
            if k.lower() in PROHIBITED_PAYLOAD_KEYS:
                errors.append(
                    f"Prohibited payload key '{k}' found at '{current_path}'. "
                    "Case content/PHI must not be stored in evaluation governance metadata."
                )
            errors.extend(check_no_payload_markers(v, current_path))
    elif isinstance(obj, list):
        for idx, item in enumerate(obj):
            current_path = f"{path}[{idx}]"
            errors.extend(check_no_payload_markers(item, current_path))
    return errors


def validate_benchmark(entry: dict[str, Any], index: int = 0) -> list[str]:
    """Validate a single benchmark metadata entry."""
    errors: list[str] = []
    prefix = f"Benchmark[{index}]"

    # Required fields
    required_fields = [
        "benchmark_id",
        "canonical_name",
        "primary_source",
        "verification_date",
        "artifact_version",
        "access_class",
        "license_status",
        "languages",
        "roles",
        "modalities",
        "capability_domains",
        "contamination_sensitivity",
        "intended_use",
        "verification_status",
        "notes",
    ]

    for f in required_fields:
        if f not in entry:
            errors.append(f"{prefix}: Missing required field '{f}'")
        elif entry[f] is None:
            errors.append(f"{prefix}: Field '{f}' cannot be null")

    if errors:
        return errors

    b_id = entry.get("benchmark_id", "")
    if not isinstance(b_id, str) or not b_id.strip():
        errors.append(f"{prefix}: 'benchmark_id' must be a non-empty string")
    prefix = f"Benchmark({b_id or index})"

    # Date format
    v_date = entry.get("verification_date", "")
    if v_date != "UNRESOLVED" and not DATE_PATTERN.match(str(v_date)):
        errors.append(
            f"{prefix}: 'verification_date' must be 'YYYY-MM-DD' or 'UNRESOLVED', got '{v_date}'"
        )

    # Access class
    acc = entry.get("access_class")
    if acc not in {e.value for e in AccessClass}:
        errors.append(
            f"{prefix}: Invalid access_class '{acc}'. Must be one of {[e.value for e in AccessClass]}"
        )

    # Verification status
    v_stat = entry.get("verification_status")
    if v_stat not in {e.value for e in VerificationStatus}:
        errors.append(
            f"{prefix}: Invalid verification_status '{v_stat}'. Must be one of {[e.value for e in VerificationStatus]}"
        )

    # Verified status requires non-empty primary_source and valid date
    if v_stat == VerificationStatus.VERIFIED.value:
        src = entry.get("primary_source", "").strip()
        if not src or src == "UNRESOLVED":
            errors.append(
                f"{prefix}: VERIFIED benchmark must have a non-empty primary_source reference"
            )
        if not DATE_PATTERN.match(str(v_date)):
            errors.append(
                f"{prefix}: VERIFIED benchmark must have a valid verification_date"
            )

    # Intended use
    i_use = entry.get("intended_use")
    if i_use not in {e.value for e in IntendedUse}:
        errors.append(
            f"{prefix}: Invalid intended_use '{i_use}'. Must be one of {[e.value for e in IntendedUse]}"
        )

    # Contamination sensitivity
    c_sens = entry.get("contamination_sensitivity")
    if c_sens not in {e.value for e in ContaminationSensitivity}:
        errors.append(
            f"{prefix}: Invalid contamination_sensitivity '{c_sens}'. Must be one of {[e.value for e in ContaminationSensitivity]}"
        )

    # Arrays validation
    for arr_field, allowed_enum, enum_name in [
        ("roles", Role, "Role"),
        ("modalities", Modality, "Modality"),
        ("capability_domains", CapabilityDomain, "CapabilityDomain"),
    ]:
        val = entry.get(arr_field)
        if not isinstance(val, list) or len(val) == 0:
            errors.append(f"{prefix}: '{arr_field}' must be a non-empty list")
        else:
            allowed_vals = {e.value for e in allowed_enum}
            for item in val:
                if item not in allowed_vals:
                    errors.append(
                        f"{prefix}: Invalid item '{item}' in '{arr_field}'. Allowed {enum_name} values: {sorted(allowed_vals)}"
                    )

    # Languages
    langs = entry.get("languages")
    if not isinstance(langs, list) or len(langs) == 0:
        errors.append(f"{prefix}: 'languages' must be a non-empty list of language codes")

    return errors


def validate_benchmark_registry(entries: list[dict[str, Any]]) -> tuple[bool, list[str]]:
    """Validate entire benchmark registry collection for schema correctness and duplicates."""
    errors: list[str] = []
    if not isinstance(entries, list) or len(entries) == 0:
        return False, ["Benchmark registry must be a non-empty list of benchmark records"]

    # Check payload markers
    errors.extend(check_no_payload_markers(entries, "benchmarks"))

    seen_ids: set[str] = set()
    for idx, entry in enumerate(entries):
        entry_errors = validate_benchmark(entry, idx)
        errors.extend(entry_errors)
        if not entry_errors:
            b_id = entry["benchmark_id"]
            if b_id in seen_ids:
                errors.append(f"Duplicate benchmark_id '{b_id}' found in registry")
            seen_ids.add(b_id)

    return len(errors) == 0, errors


def validate_metric(entry: dict[str, Any], index: int = 0) -> list[str]:
    """Validate a single metric / hard gate definition."""
    errors: list[str] = []
    prefix = f"Metric[{index}]"

    required_fields = [
        "metric_id",
        "name",
        "category",
        "description",
        "direction",
        "unit",
        "is_hard_gate",
        "threshold_state",
        "applicable_roles",
        "applicable_modalities",
        "applicable_languages",
        "required_evidence",
    ]

    for f in required_fields:
        if f not in entry:
            errors.append(f"{prefix}: Missing required field '{f}'")
        elif entry[f] is None:
            errors.append(f"{prefix}: Field '{f}' cannot be null")

    if errors:
        return errors

    m_id = entry.get("metric_id", "")
    if not isinstance(m_id, str) or not m_id.strip():
        errors.append(f"{prefix}: 'metric_id' must be a non-empty string")
    prefix = f"Metric({m_id or index})"

    # Direction
    direction = entry.get("direction")
    if direction not in {e.value for e in MetricDirection}:
        errors.append(
            f"{prefix}: Invalid direction '{direction}'. Must be one of {[e.value for e in MetricDirection]}"
        )

    # is_hard_gate
    if not isinstance(entry.get("is_hard_gate"), bool):
        errors.append(f"{prefix}: 'is_hard_gate' must be a boolean")

    # threshold_state
    t_state = entry.get("threshold_state")
    if t_state not in {e.value for e in ThresholdState}:
        errors.append(
            f"{prefix}: Invalid threshold_state '{t_state}'. Must be one of {[e.value for e in ThresholdState]}"
        )

    # Lists
    for arr_field, allowed_enum, enum_name in [
        ("applicable_roles", Role, "Role"),
        ("applicable_modalities", Modality, "Modality"),
    ]:
        val = entry.get(arr_field)
        if not isinstance(val, list) or len(val) == 0:
            errors.append(f"{prefix}: '{arr_field}' must be a non-empty list")
        else:
            allowed_vals = {e.value for e in allowed_enum}
            for item in val:
                if item not in allowed_vals:
                    errors.append(
                        f"{prefix}: Invalid item '{item}' in '{arr_field}'. Allowed {enum_name} values: {sorted(allowed_vals)}"
                    )

    if not isinstance(entry.get("applicable_languages"), list) or len(entry.get("applicable_languages")) == 0:
        errors.append(f"{prefix}: 'applicable_languages' must be a non-empty list")

    return errors


def validate_metrics_catalog(entries: list[dict[str, Any]]) -> tuple[bool, list[str]]:
    """Validate full metrics catalog."""
    errors: list[str] = []
    if not isinstance(entries, list) or len(entries) == 0:
        return False, ["Metrics catalog must be a non-empty list"]

    errors.extend(check_no_payload_markers(entries, "metrics"))

    seen_ids: set[str] = set()
    for idx, entry in enumerate(entries):
        entry_errors = validate_metric(entry, idx)
        errors.extend(entry_errors)
        if not entry_errors:
            m_id = entry["metric_id"]
            if m_id in seen_ids:
                errors.append(f"Duplicate metric_id '{m_id}' found in catalog")
            seen_ids.add(m_id)

    return len(errors) == 0, errors


def validate_gold_protocol(entry: dict[str, Any], index: int = 0) -> list[str]:
    """Validate a single Gold family protocol."""
    errors: list[str] = []
    prefix = f"GoldProtocol[{index}]"

    required_fields = [
        "family_id",
        "display_name",
        "purpose",
        "intended_strata",
        "content_location_policy",
        "allowed_access_roles",
        "adjudication_policy",
        "power_analysis_required",
        "prohibited_optimization_uses",
        "permitted_scoring_stages",
        "release_claim_scope",
        "audit_requirements",
    ]

    for f in required_fields:
        if f not in entry:
            errors.append(f"{prefix}: Missing required field '{f}'")
        elif entry[f] is None:
            errors.append(f"{prefix}: Field '{f}' cannot be null")

    if errors:
        return errors

    fam_id = entry.get("family_id", "")
    prefix = f"GoldProtocol({fam_id or index})"

    if fam_id not in {e.value for e in GoldFamilyId}:
        errors.append(
            f"{prefix}: Invalid family_id '{fam_id}'. Must be one of {[e.value for e in GoldFamilyId]}"
        )

    if entry.get("purpose") != Purpose.PRIVATE_GOLD.value:
        errors.append(
            f"{prefix}: 'purpose' must be '{Purpose.PRIVATE_GOLD.value}', got '{entry.get('purpose')}'"
        )

    # power_analysis_required MUST be True
    if entry.get("power_analysis_required") is not True:
        errors.append(
            f"{prefix}: 'power_analysis_required' must be strictly True. Private Gold claims require pre-run power analysis."
        )

    # prohibited_optimization_uses must cover all mandatory prohibitions
    prohibitions = entry.get("prohibited_optimization_uses")
    if not isinstance(prohibitions, list):
        errors.append(f"{prefix}: 'prohibited_optimization_uses' must be a list")
    else:
        proh_set = set(prohibitions)
        missing = MANDATORY_GOLD_PROHIBITIONS - proh_set
        if missing:
            errors.append(
                f"{prefix}: 'prohibited_optimization_uses' is missing mandatory prohibitions: {sorted(missing)}"
            )

    # Array checks
    for f in ["intended_strata", "allowed_access_roles", "permitted_scoring_stages"]:
        if not isinstance(entry.get(f), list) or len(entry.get(f)) == 0:
            errors.append(f"{prefix}: '{f}' must be a non-empty list")

    return errors


def validate_gold_protocols(entries: list[dict[str, Any]]) -> tuple[bool, list[str]]:
    """Validate the 3 canonical Gold family protocols."""
    errors: list[str] = []
    if not isinstance(entries, list) or len(entries) == 0:
        return False, ["Gold protocols must be a list"]

    errors.extend(check_no_payload_markers(entries, "gold_protocols"))

    seen_ids: set[str] = set()
    for idx, entry in enumerate(entries):
        entry_errors = validate_gold_protocol(entry, idx)
        errors.extend(entry_errors)
        if not entry_errors:
            f_id = entry["family_id"]
            if f_id in seen_ids:
                errors.append(f"Duplicate Gold family_id '{f_id}'")
            seen_ids.add(f_id)

    required_families = {e.value for e in GoldFamilyId}
    missing_families = required_families - seen_ids
    if missing_families:
        errors.append(f"Missing required canonical Gold families: {sorted(missing_families)}")

    return len(errors) == 0, errors


def validate_quarantine_rules(entries: list[dict[str, Any]]) -> tuple[bool, list[str]]:
    """Validate data purpose quarantine rules."""
    errors: list[str] = []
    if not isinstance(entries, list) or len(entries) == 0:
        return False, ["Quarantine rules must be a non-empty list"]

    allowed_purposes = {e.value for e in Purpose}
    seen_purposes: set[str] = set()

    for idx, r in enumerate(entries):
        p = r.get("purpose")
        prefix = f"QuarantineRule({p or idx})"
        if p not in allowed_purposes:
            errors.append(f"{prefix}: Invalid purpose '{p}'. Allowed: {sorted(allowed_purposes)}")
        if p in seen_purposes:
            errors.append(f"Duplicate quarantine rule for purpose '{p}'")
        seen_purposes.add(p)

        can_train = r.get("can_train")
        can_select = r.get("can_select_model")
        if not isinstance(can_train, bool) or not isinstance(can_select, bool):
            errors.append(f"{prefix}: 'can_train' and 'can_select_model' must be boolean")

        # Invariant: PRIVATE_GOLD and PUBLIC_EXTERNAL_EVAL can NEVER train
        if p in {Purpose.PRIVATE_GOLD.value, Purpose.PUBLIC_EXTERNAL_EVAL.value}:
            if can_train is True:
                errors.append(f"{prefix}: Quarantine violation: purpose '{p}' must have can_train=False")
            if p == Purpose.PRIVATE_GOLD.value and can_select is True:
                errors.append(f"{prefix}: Quarantine violation: purpose '{p}' must have can_select_model=False")

        if not isinstance(r.get("allowed_sources"), list):
            errors.append(f"{prefix}: 'allowed_sources' must be a list")
        if not isinstance(r.get("prohibited_sources"), list):
            errors.append(f"{prefix}: 'prohibited_sources' must be a list")

    missing = allowed_purposes - seen_purposes
    if missing:
        errors.append(f"Missing quarantine definitions for purposes: {sorted(missing)}")

    return len(errors) == 0, errors


def validate_contamination_records(entries: list[dict[str, Any]]) -> tuple[bool, list[str]]:
    """Validate benchmark contamination metadata interface."""
    errors: list[str] = []
    if not isinstance(entries, list) or len(entries) == 0:
        return False, ["Contamination records must be a non-empty list"]

    seen_ids: set[str] = set()
    for idx, item in enumerate(entries):
        asset_id = item.get("asset_id", "")
        prefix = f"ContaminationRecord({asset_id or idx})"
        if not asset_id or not isinstance(asset_id, str):
            errors.append(f"{prefix}: 'asset_id' must be a non-empty string")
        if asset_id in seen_ids:
            errors.append(f"Duplicate asset_id '{asset_id}' in contamination records")
        seen_ids.add(asset_id)

        for f in ["exact_match_status", "semantic_overlap_status", "methodology_interface", "notes"]:
            if f not in item or not isinstance(item[f], str):
                errors.append(f"{prefix}: Missing or non-string field '{f}'")

    return len(errors) == 0, errors


def evaluate_hard_gates(
    metrics_catalog: list[dict[str, Any]],
    evaluation_results: dict[str, dict[str, Any]],
) -> tuple[str, list[dict[str, Any]]]:
    """
    Evaluate hard gates against evaluation results.

    Rules:
    - Any evaluated hard gate that fails forces overall result to FAIL.
    - An aggregate score, no matter how high, CANNOT compensate for a hard gate failure.
    - If a required hard gate is NOT_EVALUATED or INSUFFICIENT_EVIDENCE or BLOCKED,
      the overall state cannot be PASS.
    - Returns (overall_state, gate_breakdown).
    """
    hard_gate_metrics = {
        m["metric_id"]: m for m in metrics_catalog if m.get("is_hard_gate") is True
    }

    gate_breakdown: list[dict[str, Any]] = []
    any_fail = False
    any_incomplete = False

    for m_id, m_meta in sorted(hard_gate_metrics.items()):
        res = evaluation_results.get(m_id)
        if res is None:
            status = GateEvaluationState.NOT_EVALUATED.value
            score = None
            reason = "Hard gate metric was not evaluated in this run"
            any_incomplete = True
        else:
            status = res.get("status", GateEvaluationState.NOT_EVALUATED.value)
            score = res.get("score")
            reason = res.get("reason", "")

            if status not in {e.value for e in GateEvaluationState}:
                status = GateEvaluationState.FAIL.value
                reason = f"Invalid evaluation status: {res.get('status')}"

            if status == GateEvaluationState.FAIL.value:
                any_fail = True
            elif status != GateEvaluationState.PASS.value:
                any_incomplete = True

        gate_breakdown.append(
            {
                "metric_id": m_id,
                "name": m_meta["name"],
                "category": m_meta["category"],
                "status": status,
                "score": score,
                "reason": reason,
            }
        )

    if any_fail:
        overall_state = GateEvaluationState.FAIL.value
    elif any_incomplete:
        overall_state = GateEvaluationState.INSUFFICIENT_EVIDENCE.value
    else:
        overall_state = GateEvaluationState.PASS.value

    return overall_state, gate_breakdown
