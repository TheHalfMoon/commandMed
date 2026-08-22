"""Fail-closed semantic validation for commandMed evaluation governance contracts."""

from __future__ import annotations

import re
from datetime import date
from typing import Any

from .model import (
    AccessClass,
    CapabilityDomain,
    ContaminationSensitivity,
    ExactMatchStatus,
    GateEvaluationState,
    GoldFamilyId,
    IntendedUse,
    LicenseStatus,
    MetricDirection,
    Modality,
    Purpose,
    Role,
    SemanticOverlapStatus,
    ThresholdState,
    VerificationStatus,
)

DATE_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")

PROHIBITED_PAYLOAD_KEYS = {
    "patient_name", "mrn", "raw_phi", "case_payload", "case_text",
    "question_text", "gold_label_answers", "real_cases",
}

MANDATORY_GOLD_PROHIBITIONS = {
    "TRAIN", "CPT", "SFT", "TEACHER_GEN", "DISTILLATION", "DPO_RL",
    "PROMPT_TUNING", "HYPERPARAMETER_SELECTION", "CHECKPOINT_SELECTION",
    "BACKBONE_SELECTION",
}

PROHIBITED_GOLD_STAGE_SUBSTRINGS = {
    "SELECTION", "ADAPTER_GATE", "BACKBONE_GATE", "CHECKPOINT_GATE",
}

GOLD_FAMILY_IDS = {e.value for e in GoldFamilyId}

VALID_QUARANTINE_SOURCES = {
    "CALIBRATION_HOLD_OUT_SPLIT",
    "MODEL_SELECTION_DEV_SET",
    "PUBLIC_BENCHMARK_DEV_SPLITS",
    "HELD_OUT_SYNTHETIC_PILOT_CASES",
    "VERIFIED_DEV_SPLIT",
    "COMMANDMED_ARABIC_GOLD",
    "COMMANDMED_CLINICAL_GOLD",
    "COMMANDMED_MULTIMODAL_GOLD",
    "DEVELOPMENT_SPLITS",
    "PUBLIC_SCRAPED_DATA",
    "TRAINING_CORPORA",
    "PUBLIC_BENCHMARK_CANONICAL_TEST_SPLITS",
    "VERIFIED_PERMISSIVE_PRETRAINING_CORPUS",
    "VERIFIED_SFT_CURRICULUM_DATA",
    "VERIFIED_SYNTHETIC_DERIVED_EXAMPLES",
    "PUBLIC_EXTERNAL_EVAL",
}

EXPECTED_ALLOWED_SOURCES = {
    Purpose.TRAIN.value: {
        "VERIFIED_PERMISSIVE_PRETRAINING_CORPUS",
        "VERIFIED_SFT_CURRICULUM_DATA",
        "VERIFIED_SYNTHETIC_DERIVED_EXAMPLES",
    },
    Purpose.DEV.value: {"HELD_OUT_SYNTHETIC_PILOT_CASES", "VERIFIED_DEV_SPLIT"},
    Purpose.CALIBRATION.value: {"CALIBRATION_HOLD_OUT_SPLIT"},
    Purpose.CHECKPOINT_SELECTION.value: {"MODEL_SELECTION_DEV_SET", "PUBLIC_BENCHMARK_DEV_SPLITS"},
    Purpose.PUBLIC_EXTERNAL_EVAL.value: {"PUBLIC_BENCHMARK_CANONICAL_TEST_SPLITS"},
    Purpose.PRIVATE_GOLD.value: GOLD_FAMILY_IDS,
}

EXPECTED_PROHIBITED_SOURCES = {
    Purpose.TRAIN.value: GOLD_FAMILY_IDS | {"PUBLIC_EXTERNAL_EVAL"},
    Purpose.DEV.value: GOLD_FAMILY_IDS,
    Purpose.CALIBRATION.value: GOLD_FAMILY_IDS,
    Purpose.CHECKPOINT_SELECTION.value: GOLD_FAMILY_IDS,
    Purpose.PUBLIC_EXTERNAL_EVAL.value: GOLD_FAMILY_IDS,
    Purpose.PRIVATE_GOLD.value: {"DEVELOPMENT_SPLITS", "PUBLIC_SCRAPED_DATA", "TRAINING_CORPORA"},
}

EXPECTED_PURPOSE_FLAGS = {
    Purpose.TRAIN.value: (True, False),
    Purpose.DEV.value: (False, True),
    Purpose.CALIBRATION.value: (False, True),
    Purpose.CHECKPOINT_SELECTION.value: (False, True),
    Purpose.PUBLIC_EXTERNAL_EVAL.value: (False, False),
    Purpose.PRIVATE_GOLD.value: (False, False),
}


def _is_valid_calendar_date(value: Any) -> bool:
    if not isinstance(value, str) or not DATE_PATTERN.fullmatch(value):
        return False
    try:
        date.fromisoformat(value)
    except ValueError:
        return False
    return True


def _required_string(entry: dict[str, Any], field: str, prefix: str, errors: list[str]) -> str | None:
    value = entry.get(field)
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{prefix}: '{field}' must be a non-empty string")
        return None
    return value


def check_no_payload_markers(obj: Any, path: str = "") -> list[str]:
    """Recursively check that no prohibited case/PHI payload keys exist."""
    errors: list[str] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            current_path = f"{path}.{k}" if path else str(k)
            if isinstance(k, str) and k.lower() in PROHIBITED_PAYLOAD_KEYS:
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


def check_list_unique(items: list[Any], field_name: str, prefix: str) -> list[str]:
    """Reject non-string or duplicate elements in set-like metadata lists without raising."""
    errors: list[str] = []
    if not isinstance(items, list):
        return [f"{prefix}: '{field_name}' must be a list"]

    valid_items: list[str] = []
    for idx, item in enumerate(items):
        if not isinstance(item, str):
            errors.append(
                f"{prefix}: Item {idx} in set-like field '{field_name}' must be a string, got {type(item).__name__}"
            )
        else:
            valid_items.append(item)

    seen: set[str] = set()
    duplicates: set[str] = set()
    for item in valid_items:
        if item in seen:
            duplicates.add(item)
        seen.add(item)
    if duplicates:
        errors.append(
            f"{prefix}: Duplicate values found in set-like field '{field_name}': {sorted(duplicates)}"
        )
    return errors


def validate_benchmark(entry: Any, index: int = 0) -> list[str]:
    """Validate a single benchmark metadata entry with evidence-bound rules."""
    prefix = f"Benchmark[{index}]"
    if not isinstance(entry, dict):
        return [f"{prefix}: Benchmark record must be a JSON object"]

    errors: list[str] = []
    required_fields = [
        "benchmark_id", "canonical_name", "primary_source", "source_uri",
        "source_identifier", "source_revision", "verification_date",
        "artifact_version", "access_class", "license_status",
        "license_source_uri", "languages", "roles", "modalities",
        "capability_domains", "contamination_sensitivity", "intended_use",
        "verification_status", "notes",
    ]
    for field in required_fields:
        if field not in entry:
            errors.append(f"{prefix}: Missing required field '{field}'")
        elif entry[field] is None:
            errors.append(f"{prefix}: Field '{field}' cannot be null")
    if errors:
        return errors

    b_id = entry.get("benchmark_id")
    if not isinstance(b_id, str) or not b_id.strip():
        errors.append(f"{prefix}: 'benchmark_id' must be a non-empty string")
        display_id = str(index)
    else:
        display_id = b_id
    prefix = f"Benchmark({display_id})"

    scalar_string_fields = [
        "canonical_name", "primary_source", "source_uri", "source_identifier",
        "source_revision", "artifact_version", "license_status",
        "license_source_uri", "notes",
    ]
    for field in scalar_string_fields:
        _required_string(entry, field, prefix, errors)

    v_date = entry.get("verification_date")
    if v_date != "UNRESOLVED" and not _is_valid_calendar_date(v_date):
        errors.append(
            f"{prefix}: 'verification_date' must be a real calendar date in YYYY-MM-DD format or 'UNRESOLVED', got '{v_date}'"
        )

    acc = entry.get("access_class")
    if acc not in {e.value for e in AccessClass}:
        errors.append(f"{prefix}: Invalid access_class '{acc}'. Must be one of {[e.value for e in AccessClass]}")

    v_stat = entry.get("verification_status")
    if v_stat not in {e.value for e in VerificationStatus}:
        errors.append(
            f"{prefix}: Invalid verification_status '{v_stat}'. Must be one of {[e.value for e in VerificationStatus]}"
        )

    i_use = entry.get("intended_use")
    if i_use not in {e.value for e in IntendedUse}:
        errors.append(f"{prefix}: Invalid intended_use '{i_use}'. Must be one of {[e.value for e in IntendedUse]}")

    lic_raw = entry.get("license_status")
    lic_stat = lic_raw.strip() if isinstance(lic_raw, str) else None
    if lic_stat not in {e.value for e in LicenseStatus}:
        errors.append(
            f"{prefix}: Invalid license_status '{lic_raw}'. Must be one of the controlled vocabulary: {[e.value for e in LicenseStatus]}"
        )

    if v_stat == VerificationStatus.VERIFIED.value:
        for field in ("primary_source", "source_uri", "source_identifier", "license_source_uri"):
            value = entry.get(field)
            if not isinstance(value, str) or not value.strip() or value == "UNRESOLVED":
                label = "primary_source reference" if field == "primary_source" else field
                errors.append(f"{prefix}: VERIFIED benchmark must have a resolved {label}")
        if not _is_valid_calendar_date(v_date):
            errors.append(f"{prefix}: VERIFIED benchmark must have a valid verification_date matching a real YYYY-MM-DD calendar date")
        if not lic_stat or lic_stat == LicenseStatus.UNRESOLVED.value:
            errors.append(f"{prefix}: VERIFIED benchmark must have a resolved license_status (cannot be 'UNRESOLVED')")

    if lic_stat == LicenseStatus.COMPONENT_SPECIFIC.value:
        if i_use not in {IntendedUse.REFERENCE_ONLY.value, IntendedUse.PROHIBITED.value}:
            errors.append(
                f"{prefix}: Benchmark with license_status='COMPONENT_SPECIFIC' cannot have executable intended_use '{i_use}'. "
                f"Must be '{IntendedUse.REFERENCE_ONLY.value}' or '{IntendedUse.PROHIBITED.value}'. Component benchmarks must be registered individually before execution."
            )

    if v_stat == VerificationStatus.UNRESOLVED.value and i_use in {
        IntendedUse.DEVELOPMENT.value, IntendedUse.POSSIBLE_RELEASE_GATE.value,
    }:
        errors.append(
            f"{prefix}: UNRESOLVED benchmark cannot have executable intended_use '{i_use}'. "
            f"Must be '{IntendedUse.REFERENCE_ONLY.value}' or '{IntendedUse.PROHIBITED.value}'."
        )

    if lic_stat == LicenseStatus.UNRESOLVED.value and v_stat == VerificationStatus.VERIFIED.value:
        errors.append(f"{prefix}: Benchmark with license_status='UNRESOLVED' cannot have verification_status='VERIFIED'.")

    c_sens = entry.get("contamination_sensitivity")
    if c_sens not in {e.value for e in ContaminationSensitivity}:
        errors.append(
            f"{prefix}: Invalid contamination_sensitivity '{c_sens}'. Must be one of {[e.value for e in ContaminationSensitivity]}"
        )

    for arr_field, allowed_enum, enum_name in [
        ("roles", Role, "Role"),
        ("modalities", Modality, "Modality"),
        ("capability_domains", CapabilityDomain, "CapabilityDomain"),
    ]:
        value = entry.get(arr_field)
        if not isinstance(value, list) or not value:
            errors.append(f"{prefix}: '{arr_field}' must be a non-empty list")
            continue
        errors.extend(check_list_unique(value, arr_field, prefix))
        allowed_values = {e.value for e in allowed_enum}
        for item in value:
            if isinstance(item, str) and item not in allowed_values:
                errors.append(
                    f"{prefix}: Invalid item '{item}' in '{arr_field}'. Allowed {enum_name} values: {sorted(allowed_values)}"
                )

    languages = entry.get("languages")
    if not isinstance(languages, list) or not languages:
        errors.append(f"{prefix}: 'languages' must be a non-empty list of language codes")
    else:
        errors.extend(check_list_unique(languages, "languages", prefix))

    return errors


def validate_benchmark_registry(entries: Any) -> tuple[bool, list[str]]:
    errors: list[str] = []
    if not isinstance(entries, list) or not entries:
        return False, ["Benchmark registry must be a non-empty list of benchmark records"]
    errors.extend(check_no_payload_markers(entries, "benchmarks"))
    seen_ids: set[str] = set()
    for idx, entry in enumerate(entries):
        entry_errors = validate_benchmark(entry, idx)
        errors.extend(entry_errors)
        if isinstance(entry, dict):
            b_id = entry.get("benchmark_id")
            if isinstance(b_id, str) and b_id.strip():
                if b_id in seen_ids:
                    errors.append(f"Duplicate benchmark_id '{b_id}' found in registry")
                seen_ids.add(b_id)
    return len(errors) == 0, errors


def validate_metric(entry: Any, index: int = 0) -> list[str]:
    prefix = f"Metric[{index}]"
    if not isinstance(entry, dict):
        return [f"{prefix}: Metric record must be a JSON object"]
    errors: list[str] = []
    required_fields = [
        "metric_id", "name", "category", "description", "direction", "unit",
        "is_hard_gate", "threshold_state", "applicable_roles",
        "applicable_modalities", "applicable_languages", "required_evidence",
    ]
    for field in required_fields:
        if field not in entry:
            errors.append(f"{prefix}: Missing required field '{field}'")
        elif entry[field] is None:
            errors.append(f"{prefix}: Field '{field}' cannot be null")
    if errors:
        return errors

    m_id = entry.get("metric_id")
    if not isinstance(m_id, str) or not m_id.strip():
        errors.append(f"{prefix}: 'metric_id' must be a non-empty string")
        display_id = str(index)
    else:
        display_id = m_id
    prefix = f"Metric({display_id})"

    for field in ("name", "category", "description", "unit", "required_evidence"):
        _required_string(entry, field, prefix, errors)

    direction = entry.get("direction")
    if direction not in {e.value for e in MetricDirection}:
        errors.append(f"{prefix}: Invalid direction '{direction}'. Must be one of {[e.value for e in MetricDirection]}")
    if not isinstance(entry.get("is_hard_gate"), bool):
        errors.append(f"{prefix}: 'is_hard_gate' must be a boolean")
    threshold_state = entry.get("threshold_state")
    if threshold_state not in {e.value for e in ThresholdState}:
        errors.append(
            f"{prefix}: Invalid threshold_state '{threshold_state}'. Must be one of {[e.value for e in ThresholdState]}"
        )

    for arr_field, allowed_enum, enum_name in [
        ("applicable_roles", Role, "Role"),
        ("applicable_modalities", Modality, "Modality"),
    ]:
        value = entry.get(arr_field)
        if not isinstance(value, list) or not value:
            errors.append(f"{prefix}: '{arr_field}' must be a non-empty list")
            continue
        errors.extend(check_list_unique(value, arr_field, prefix))
        allowed_values = {e.value for e in allowed_enum}
        for item in value:
            if isinstance(item, str) and item not in allowed_values:
                errors.append(
                    f"{prefix}: Invalid item '{item}' in '{arr_field}'. Allowed {enum_name} values: {sorted(allowed_values)}"
                )

    languages = entry.get("applicable_languages")
    if not isinstance(languages, list) or not languages:
        errors.append(f"{prefix}: 'applicable_languages' must be a non-empty list")
    else:
        errors.extend(check_list_unique(languages, "applicable_languages", prefix))
    return errors


def validate_metrics_catalog(entries: Any) -> tuple[bool, list[str]]:
    if not isinstance(entries, list) or not entries:
        return False, ["Metrics catalog must be a non-empty list"]
    errors = check_no_payload_markers(entries, "metrics")
    seen_ids: set[str] = set()
    for idx, entry in enumerate(entries):
        entry_errors = validate_metric(entry, idx)
        errors.extend(entry_errors)
        if isinstance(entry, dict):
            m_id = entry.get("metric_id")
            if isinstance(m_id, str) and m_id.strip():
                if m_id in seen_ids:
                    errors.append(f"Duplicate metric_id '{m_id}' found in catalog")
                seen_ids.add(m_id)
    return len(errors) == 0, errors


def validate_gold_protocol(entry: Any, index: int = 0) -> list[str]:
    prefix = f"GoldProtocol[{index}]"
    if not isinstance(entry, dict):
        return [f"{prefix}: Gold protocol record must be a JSON object"]
    errors: list[str] = []
    required_fields = [
        "family_id", "display_name", "purpose", "intended_strata",
        "content_location_policy", "allowed_access_roles", "adjudication_policy",
        "power_analysis_required", "prohibited_optimization_uses",
        "permitted_scoring_stages", "release_claim_scope", "audit_requirements",
    ]
    for field in required_fields:
        if field not in entry:
            errors.append(f"{prefix}: Missing required field '{field}'")
        elif entry[field] is None:
            errors.append(f"{prefix}: Field '{field}' cannot be null")
    if errors:
        return errors

    family_id = entry.get("family_id")
    display_id = family_id if isinstance(family_id, str) and family_id else str(index)
    prefix = f"GoldProtocol({display_id})"
    if family_id not in GOLD_FAMILY_IDS:
        errors.append(f"{prefix}: Invalid family_id '{family_id}'. Must be one of {sorted(GOLD_FAMILY_IDS)}")
    if entry.get("purpose") != Purpose.PRIVATE_GOLD.value:
        errors.append(f"{prefix}: 'purpose' must be '{Purpose.PRIVATE_GOLD.value}', got '{entry.get('purpose')}'")
    for field in (
        "display_name", "content_location_policy", "adjudication_policy",
        "release_claim_scope", "audit_requirements",
    ):
        _required_string(entry, field, prefix, errors)
    if entry.get("power_analysis_required") is not True:
        errors.append(
            f"{prefix}: 'power_analysis_required' must be strictly True. Private Gold claims require pre-run power analysis."
        )

    prohibitions = entry.get("prohibited_optimization_uses")
    if not isinstance(prohibitions, list):
        errors.append(f"{prefix}: 'prohibited_optimization_uses' must be a list")
    else:
        errors.extend(check_list_unique(prohibitions, "prohibited_optimization_uses", prefix))
        valid_prohibitions = {x for x in prohibitions if isinstance(x, str)}
        missing = MANDATORY_GOLD_PROHIBITIONS - valid_prohibitions
        if missing:
            errors.append(
                f"{prefix}: 'prohibited_optimization_uses' is missing mandatory prohibitions: {sorted(missing)}"
            )

    scoring_stages = entry.get("permitted_scoring_stages")
    if not isinstance(scoring_stages, list) or not scoring_stages:
        errors.append(f"{prefix}: 'permitted_scoring_stages' must be a non-empty list")
    else:
        errors.extend(check_list_unique(scoring_stages, "permitted_scoring_stages", prefix))
        for stage in scoring_stages:
            if isinstance(stage, str):
                for prohibited_sub in PROHIBITED_GOLD_STAGE_SUBSTRINGS:
                    if prohibited_sub in stage.upper():
                        errors.append(
                            f"{prefix}: Contradiction in permitted_scoring_stages: '{stage}' contains prohibited keyword '{prohibited_sub}'. Private Gold cannot perform candidate selection."
                        )

    for field in ("intended_strata", "allowed_access_roles"):
        value = entry.get(field)
        if not isinstance(value, list) or not value:
            errors.append(f"{prefix}: '{field}' must be a non-empty list")
        else:
            errors.extend(check_list_unique(value, field, prefix))
    return errors


def validate_gold_protocols(entries: Any) -> tuple[bool, list[str]]:
    if not isinstance(entries, list) or not entries:
        return False, ["Gold protocols must be a list"]
    errors = check_no_payload_markers(entries, "gold_protocols")
    seen_ids: set[str] = set()
    for idx, entry in enumerate(entries):
        entry_errors = validate_gold_protocol(entry, idx)
        errors.extend(entry_errors)
        if isinstance(entry, dict):
            family_id = entry.get("family_id")
            if isinstance(family_id, str) and family_id:
                if family_id in seen_ids:
                    errors.append(f"Duplicate Gold family_id '{family_id}'")
                seen_ids.add(family_id)
    missing_families = GOLD_FAMILY_IDS - seen_ids
    if missing_families:
        errors.append(f"Missing required canonical Gold families: {sorted(missing_families)}")
    return len(errors) == 0, errors


def validate_quarantine_rules(entries: Any) -> tuple[bool, list[str]]:
    """Validate the canonical purpose/source quarantine matrix fail-closed."""
    if not isinstance(entries, list) or not entries:
        return False, ["Quarantine rules must be a non-empty list"]
    errors: list[str] = []
    allowed_purposes = {e.value for e in Purpose}
    seen_purposes: set[str] = set()

    for idx, rule in enumerate(entries):
        if not isinstance(rule, dict):
            errors.append(f"QuarantineRule[{idx}]: Quarantine rule must be a JSON object")
            continue
        purpose = rule.get("purpose")
        display_purpose = purpose if isinstance(purpose, str) and purpose else str(idx)
        prefix = f"QuarantineRule({display_purpose})"
        if purpose not in allowed_purposes:
            errors.append(f"{prefix}: Invalid purpose '{purpose}'. Allowed: {sorted(allowed_purposes)}")
            continue
        if purpose in seen_purposes:
            errors.append(f"Duplicate quarantine rule for purpose '{purpose}'")
        seen_purposes.add(purpose)

        can_train = rule.get("can_train")
        can_select = rule.get("can_select_model")
        if not isinstance(can_train, bool) or not isinstance(can_select, bool):
            errors.append(f"{prefix}: 'can_train' and 'can_select_model' must be boolean")
        else:
            expected_train, expected_select = EXPECTED_PURPOSE_FLAGS[purpose]
            if can_train != expected_train:
                errors.append(f"{prefix}: Quarantine violation: purpose '{purpose}' must have can_train={expected_train}")
            if can_select != expected_select:
                errors.append(f"{prefix}: Quarantine violation: purpose '{purpose}' must have can_select_model={expected_select}")

        parsed_sources: dict[str, set[str]] = {}
        for field in ("allowed_sources", "prohibited_sources"):
            value = rule.get(field)
            if not isinstance(value, list):
                errors.append(f"{prefix}: '{field}' must be a list")
                parsed_sources[field] = set()
                continue
            errors.extend(check_list_unique(value, field, prefix))
            source_set: set[str] = set()
            for source in value:
                if not isinstance(source, str):
                    continue
                if source not in VALID_QUARANTINE_SOURCES:
                    errors.append(f"{prefix}: Invalid quarantine source token '{source}' in '{field}'")
                source_set.add(source)
            parsed_sources[field] = source_set

        allowed_sources = parsed_sources.get("allowed_sources", set())
        prohibited_sources = parsed_sources.get("prohibited_sources", set())
        overlap = allowed_sources & prohibited_sources
        if overlap:
            errors.append(f"{prefix}: Source tokens cannot appear in both allowed_sources and prohibited_sources: {sorted(overlap)}")

        expected_allowed = EXPECTED_ALLOWED_SOURCES[purpose]
        if allowed_sources != expected_allowed:
            errors.append(
                f"{prefix}: allowed_sources must exactly match canonical matrix for purpose '{purpose}': {sorted(expected_allowed)}"
            )
        expected_prohibited = EXPECTED_PROHIBITED_SOURCES[purpose]
        if prohibited_sources != expected_prohibited:
            errors.append(
                f"{prefix}: prohibited_sources must exactly match canonical matrix for purpose '{purpose}': {sorted(expected_prohibited)}"
            )

        if purpose != Purpose.PRIVATE_GOLD.value and not GOLD_FAMILY_IDS.issubset(prohibited_sources):
            errors.append(f"{prefix}: All CommandMed private Gold families must be prohibited outside PRIVATE_GOLD")
        if purpose == Purpose.PRIVATE_GOLD.value and allowed_sources != GOLD_FAMILY_IDS:
            errors.append(f"{prefix}: PRIVATE_GOLD may allow only the three canonical Gold families")

    missing = allowed_purposes - seen_purposes
    if missing:
        errors.append(f"Missing quarantine definitions for purposes: {sorted(missing)}")
    return len(errors) == 0, errors


def validate_contamination_records(entries: Any) -> tuple[bool, list[str]]:
    """Validate benchmark contamination metadata interface with evidence symmetry."""
    if not isinstance(entries, list) or not entries:
        return False, ["Contamination records must be a non-empty list"]
    errors: list[str] = []
    seen_ids: set[str] = set()
    for idx, item in enumerate(entries):
        if not isinstance(item, dict):
            errors.append(f"ContaminationRecord[{idx}]: Contamination record must be a JSON object")
            continue
        asset_id = item.get("asset_id")
        display_id = asset_id if isinstance(asset_id, str) and asset_id else str(idx)
        prefix = f"ContaminationRecord({display_id})"
        if not isinstance(asset_id, str) or not asset_id:
            errors.append(f"{prefix}: 'asset_id' must be a non-empty string")
        elif asset_id in seen_ids:
            errors.append(f"Duplicate asset_id '{asset_id}' in contamination records")
        if isinstance(asset_id, str) and asset_id:
            seen_ids.add(asset_id)

        for field in (
            "exact_match_status", "semantic_overlap_status", "evidence_artifact_id",
            "methodology_interface", "notes",
        ):
            if field not in item or not isinstance(item[field], str):
                errors.append(f"{prefix}: Missing or non-string field '{field}'")

        exact_status = item.get("exact_match_status")
        if exact_status not in {e.value for e in ExactMatchStatus}:
            errors.append(f"{prefix}: Invalid exact_match_status '{exact_status}'. Allowed: {[e.value for e in ExactMatchStatus]}")
        semantic_status = item.get("semantic_overlap_status")
        if semantic_status not in {e.value for e in SemanticOverlapStatus}:
            errors.append(
                f"{prefix}: Invalid semantic_overlap_status '{semantic_status}'. Allowed: {[e.value for e in SemanticOverlapStatus]}"
            )

        evidence_raw = item.get("evidence_artifact_id")
        evidence_id = evidence_raw.strip() if isinstance(evidence_raw, str) else ""
        substantive_exact_states = {
            ExactMatchStatus.CHECKED_CLEAN.value,
            ExactMatchStatus.OVERLAP_FOUND.value,
            ExactMatchStatus.BLOCKED.value,
        }
        if exact_status in substantive_exact_states and evidence_id in {"", "NONE", "UNRESOLVED"}:
            errors.append(
                f"{prefix}: exact_match_status='{exact_status}' requires a resolved evidence_artifact_id (cannot be '{evidence_id}')"
            )
        substantive_semantic_states = {
            SemanticOverlapStatus.ASSESSED_LOW_RISK.value,
            SemanticOverlapStatus.ASSESSED_HIGH_RISK.value,
            SemanticOverlapStatus.BLOCKED.value,
        }
        if semantic_status in substantive_semantic_states and evidence_id in {"", "NONE", "UNRESOLVED"}:
            errors.append(
                f"{prefix}: semantic_overlap_status='{semantic_status}' requires a resolved evidence_artifact_id (cannot be '{evidence_id}')"
            )
    return len(errors) == 0, errors


def evaluate_hard_gates(
    metrics_catalog: Any,
    evaluation_results: Any,
) -> tuple[str, list[dict[str, Any]]]:
    """Evaluate hard gates, never allowing an absent gate set to pass."""
    if not isinstance(metrics_catalog, list) or not metrics_catalog:
        return GateEvaluationState.INSUFFICIENT_EVIDENCE.value, [
            {
                "status": GateEvaluationState.INSUFFICIENT_EVIDENCE.value,
                "reason": "Hard-gate catalog is empty or unavailable; PASS requires at least one defined hard gate",
            }
        ]

    hard_gate_metrics: dict[str, dict[str, Any]] = {}
    malformed_catalog = False
    for metric in metrics_catalog:
        if not isinstance(metric, dict):
            malformed_catalog = True
            continue
        if metric.get("is_hard_gate") is True:
            metric_id = metric.get("metric_id")
            if isinstance(metric_id, str) and metric_id:
                hard_gate_metrics[metric_id] = metric
            else:
                malformed_catalog = True

    if not hard_gate_metrics:
        reason = "No hard-gate metrics are defined; PASS requires at least one required hard gate"
        if malformed_catalog:
            reason += "; malformed metric records were also present"
        return GateEvaluationState.INSUFFICIENT_EVIDENCE.value, [
            {"status": GateEvaluationState.INSUFFICIENT_EVIDENCE.value, "reason": reason}
        ]

    if not isinstance(evaluation_results, dict):
        return GateEvaluationState.INSUFFICIENT_EVIDENCE.value, [
            {
                "status": GateEvaluationState.INSUFFICIENT_EVIDENCE.value,
                "reason": "Evaluation results must be a mapping keyed by hard-gate metric_id",
            }
        ]

    gate_breakdown: list[dict[str, Any]] = []
    any_fail = False
    any_incomplete = malformed_catalog
    for metric_id, metric_meta in sorted(hard_gate_metrics.items()):
        result = evaluation_results.get(metric_id)
        if result is None:
            status = GateEvaluationState.NOT_EVALUATED.value
            score = None
            reason = "Hard gate metric was not evaluated in this run"
            any_incomplete = True
        elif not isinstance(result, dict):
            status = GateEvaluationState.FAIL.value
            score = None
            reason = "Malformed hard-gate evaluation result; expected an object"
            any_fail = True
        else:
            raw_status = result.get("status", GateEvaluationState.NOT_EVALUATED.value)
            score = result.get("score")
            reason = result.get("reason", "")
            if raw_status not in {e.value for e in GateEvaluationState}:
                status = GateEvaluationState.FAIL.value
                reason = f"Invalid evaluation status: {raw_status}"
                any_fail = True
            else:
                status = raw_status
                if status == GateEvaluationState.FAIL.value:
                    any_fail = True
                elif status != GateEvaluationState.PASS.value:
                    any_incomplete = True
        gate_breakdown.append(
            {
                "metric_id": metric_id,
                "name": metric_meta.get("name", metric_id),
                "category": metric_meta.get("category", "UNSPECIFIED"),
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
