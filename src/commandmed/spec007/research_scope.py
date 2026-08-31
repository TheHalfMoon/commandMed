"""Research-only Spec 007 component scope validators.

This module is an offline deterministic control-plane surface for
``SP007-RO-001``. It validates metadata bindings only; it never loads model
weights, opens devices, accesses credentials, executes inference, or starts
training.
"""

from __future__ import annotations

from typing import Any, Mapping

from src.commandmed.spec007.activation import preflight_run_manifest
from src.commandmed.spec007.curriculum import validate_curriculum_record
from src.commandmed.spec007.foundation import validate_closed_object

RESEARCH_COMPONENT_SCOPE_ID = "SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1"
RESEARCH_COMPONENT_SCOPE_CLASS = "COMPONENT_QUALIFICATION"
RESEARCH_COMPONENT_CLAIM_CLASS = "NON_CLINICAL_RESEARCH_ENGINEERING_ONLY"
RESEARCH_COMPONENT_ROLE_CLASS = "LEARNER_RESEARCHER"

RESEARCH_COMPONENT_ADMITTED_CAPABILITIES = frozenset(
    {
        "GENERAL_INSTRUCTION_FOLLOWING",
        "GENERAL_ENGLISH_LANGUAGE",
        "GENERAL_ARABIC_LANGUAGE_NON_CLINICAL",
        "NON_CLINICAL_RESEARCH_LEARNING_FORMATTING",
        "UNCERTAINTY_AND_ABSTENTION",
        "SYNTHETIC_NON_CLINICAL_TOOL_ROUTING",
        "REPRODUCIBLE_TRAINING_CONTROL_MECHANICS",
        "PROVENANCE_QUARANTINE_CONTAMINATION_ENFORCEMENT",
        "GENERAL_CAPABILITY_PRESERVATION",
    }
)

RESEARCH_COMPONENT_EXCLUDED_CAPABILITIES = frozenset(
    {
        "PATIENT_SPECIFIC_DIAGNOSIS",
        "PATIENT_SPECIFIC_DIFFERENTIAL_DIAGNOSIS",
        "PATIENT_OR_CAREGIVER_TREATMENT_ADVICE",
        "PATIENT_OR_CAREGIVER_TRIAGE",
        "EMERGENCY_DISPOSITION_OR_REASSURANCE",
        "MEDICATION_OR_DOSE_RECOMMENDATION",
        "ALLERGY_OR_INTERACTION_ADVICE",
        "RENAL_HEPATIC_MEDICATION_ADVICE",
        "PREGNANCY_OR_PEDIATRIC_CLINICAL_ADVICE",
        "CLINICAL_PROFESSIONAL_DECISION_SUPPORT",
        "CLINICAL_WORKFLOW_RECOMMENDATION",
        "LAB_REPORT_CLINICAL_EXTRACTION_OR_INTERPRETATION",
        "PATIENT_FACING_EVIDENCE_SUMMARY",
        "MEDICAL_CITATION_SUPPORT_CLAIM",
        "ARABIC_CLINICAL_PARITY_CLAIM",
        "CLINICAL_SELECTIVE_RISK_OR_COVERAGE_CLAIM",
        "BENIGN_CASE_OVER_TRIAGE_CLAIM",
        "CLINICAL_SAFETY_RATE_CLAIM",
    }
)

RESEARCH_COMPONENT_REQUIRED_GUARDS = frozenset(
    {
        "RO_GUARD_001_OUT_OF_SCOPE_PATIENT_ADVICE",
        "RO_GUARD_002_OUT_OF_SCOPE_CLINICAL_PROFESSIONAL_ADVICE",
        "RO_GUARD_003_EMERGENCY_SENTINEL",
        "RO_GUARD_004_MEDICATION_SENTINEL",
        "RO_GUARD_005_DETERMINISTIC_TOOL_BOUNDARY",
        "RO_GUARD_006_UNSUPPORTED_CERTAINTY",
        "RO_GUARD_007_SCOPE_ESCAPE",
    }
)

_SENTINEL_EXPECTED_ACTIONS = frozenset({"ABSTAIN", "ASK_MORE", "ESCALATE"})
_BINDING_FIELDS = (
    "schema_version",
    "binding_id",
    "scope_id",
    "scope_class",
    "claim_class",
    "gradient_record_bindings",
    "sentinel_fixture_bindings",
    "excluded_capability_ids",
    "required_guard_ids",
    "system_qualification_created",
    "clinical_qualification_created",
)
_GRADIENT_BINDING_FIELDS = (
    "record_id",
    "target_capability_ids",
    "content_scope_verification_state",
    "optimization_feedback_allowed",
)
_SENTINEL_BINDING_FIELDS = (
    "fixture_id",
    "guard_id",
    "expected_action",
    "optimization_feedback_allowed",
)


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _exact_unique_string_set(
    value: Any,
    expected: frozenset[str],
    *,
    field: str,
) -> list[str]:
    if not isinstance(value, list):
        return [f"{field}: expected list"]
    if any(not _nonempty(item) for item in value):
        return [f"{field}: entries must be non-empty strings"]
    if len(value) != len(set(value)):
        return [f"{field}: entries must be unique"]
    if set(value) != set(expected):
        return [f"{field}: must equal the canonical frozen set"]
    return []


def validate_research_component_scope_binding(
    binding: Any,
    curriculum_records: Mapping[str, Mapping[str, Any]],
) -> list[str]:
    """Validate the SP007-RO-001 component binding fail closed."""

    prefix = "ResearchComponentScopeBinding"
    errors = validate_closed_object(
        binding,
        required_fields=_BINDING_FIELDS,
        field=prefix,
    )
    if not isinstance(binding, dict):
        return errors

    if binding.get("schema_version") != "1":
        errors.append(f"{prefix}: schema_version must equal '1'")
    if not _nonempty(binding.get("binding_id")):
        errors.append(f"{prefix}: binding_id must be a non-empty string")
    if binding.get("scope_id") != RESEARCH_COMPONENT_SCOPE_ID:
        errors.append(f"{prefix}: scope_id must equal the canonical successor scope")
    if binding.get("scope_class") != RESEARCH_COMPONENT_SCOPE_CLASS:
        errors.append(f"{prefix}: scope_class must equal COMPONENT_QUALIFICATION")
    if binding.get("claim_class") != RESEARCH_COMPONENT_CLAIM_CLASS:
        errors.append(
            f"{prefix}: claim_class must equal NON_CLINICAL_RESEARCH_ENGINEERING_ONLY"
        )
    if binding.get("system_qualification_created") is not False:
        errors.append(f"{prefix}: system_qualification_created must be false")
    if binding.get("clinical_qualification_created") is not False:
        errors.append(f"{prefix}: clinical_qualification_created must be false")

    errors.extend(
        _exact_unique_string_set(
            binding.get("excluded_capability_ids"),
            RESEARCH_COMPONENT_EXCLUDED_CAPABILITIES,
            field=f"{prefix}.excluded_capability_ids",
        )
    )
    errors.extend(
        _exact_unique_string_set(
            binding.get("required_guard_ids"),
            RESEARCH_COMPONENT_REQUIRED_GUARDS,
            field=f"{prefix}.required_guard_ids",
        )
    )

    gradient_bindings = binding.get("gradient_record_bindings")
    if not isinstance(gradient_bindings, list) or not gradient_bindings:
        errors.append(f"{prefix}.gradient_record_bindings: expected non-empty list")
    else:
        seen_records: set[str] = set()
        for index, record_binding in enumerate(gradient_bindings):
            item_prefix = f"{prefix}.gradient_record_bindings[{index}]"
            errors.extend(
                validate_closed_object(
                    record_binding,
                    required_fields=_GRADIENT_BINDING_FIELDS,
                    field=item_prefix,
                )
            )
            if not isinstance(record_binding, dict):
                continue

            record_id = record_binding.get("record_id")
            if not _nonempty(record_id):
                errors.append(f"{item_prefix}: record_id must be a non-empty string")
                continue
            if record_id in seen_records:
                errors.append(f"{item_prefix}: duplicate record_id '{record_id}'")
            seen_records.add(record_id)

            target_capabilities = record_binding.get("target_capability_ids")
            if not isinstance(target_capabilities, list) or not target_capabilities:
                errors.append(f"{item_prefix}: target_capability_ids must be non-empty list")
            elif any(not _nonempty(item) for item in target_capabilities):
                errors.append(
                    f"{item_prefix}: target_capability_ids entries must be non-empty strings"
                )
            elif len(target_capabilities) != len(set(target_capabilities)):
                errors.append(f"{item_prefix}: target_capability_ids must be unique")
            else:
                unsupported = sorted(
                    set(target_capabilities) - RESEARCH_COMPONENT_ADMITTED_CAPABILITIES
                )
                if unsupported:
                    errors.append(
                        f"{item_prefix}: target_capability_ids outside admitted scope {unsupported}"
                    )

            if record_binding.get("content_scope_verification_state") != "PASS":
                errors.append(
                    f"{item_prefix}: content_scope_verification_state must equal 'PASS'"
                )
            if record_binding.get("optimization_feedback_allowed") is not True:
                errors.append(
                    f"{item_prefix}: optimization_feedback_allowed must be true "
                    "for admitted gradient records"
                )

            curriculum_record = curriculum_records.get(record_id)
            if not isinstance(curriculum_record, Mapping):
                errors.append(f"{item_prefix}: record_id unresolved in curriculum_records")
                continue
            materialized_record = dict(curriculum_record)
            if validate_curriculum_record(materialized_record):
                errors.append(f"{item_prefix}: curriculum record failed canonical validation")
            if materialized_record.get("role_class") != RESEARCH_COMPONENT_ROLE_CLASS:
                errors.append(
                    f"{item_prefix}: curriculum role_class must equal LEARNER_RESEARCHER"
                )
            if materialized_record.get("knowledge_placement") != "DURABLE_WEIGHT_ELIGIBLE":
                errors.append(
                    f"{item_prefix}: gradient record must be DURABLE_WEIGHT_ELIGIBLE"
                )

    sentinel_bindings = binding.get("sentinel_fixture_bindings")
    if not isinstance(sentinel_bindings, list) or not sentinel_bindings:
        errors.append(f"{prefix}.sentinel_fixture_bindings: expected non-empty list")
    else:
        seen_fixtures: set[str] = set()
        seen_guards: set[str] = set()
        for index, sentinel in enumerate(sentinel_bindings):
            item_prefix = f"{prefix}.sentinel_fixture_bindings[{index}]"
            errors.extend(
                validate_closed_object(
                    sentinel,
                    required_fields=_SENTINEL_BINDING_FIELDS,
                    field=item_prefix,
                )
            )
            if not isinstance(sentinel, dict):
                continue

            fixture_id = sentinel.get("fixture_id")
            if not _nonempty(fixture_id):
                errors.append(f"{item_prefix}: fixture_id must be a non-empty string")
            elif fixture_id in seen_fixtures:
                errors.append(f"{item_prefix}: duplicate fixture_id '{fixture_id}'")
            else:
                seen_fixtures.add(fixture_id)

            guard_id = sentinel.get("guard_id")
            if guard_id not in RESEARCH_COMPONENT_REQUIRED_GUARDS:
                errors.append(f"{item_prefix}: guard_id is not a canonical successor guard")
            elif guard_id in seen_guards:
                errors.append(f"{item_prefix}: duplicate guard_id '{guard_id}'")
            else:
                seen_guards.add(guard_id)

            if sentinel.get("expected_action") not in _SENTINEL_EXPECTED_ACTIONS:
                errors.append(
                    f"{item_prefix}: expected_action must be ABSTAIN, ASK_MORE, or ESCALATE"
                )
            if sentinel.get("optimization_feedback_allowed") is not False:
                errors.append(
                    f"{item_prefix}: optimization_feedback_allowed must be false "
                    "for abort/disqualify-only sentinel fixtures"
                )

        if seen_guards != set(RESEARCH_COMPONENT_REQUIRED_GUARDS):
            errors.append(
                f"{prefix}.sentinel_fixture_bindings: every canonical successor guard "
                "must have exactly one bound fixture"
            )

    return errors


def preflight_research_component_run_manifest(
    *,
    manifest: Any,
    component_store: Mapping[str, Mapping[str, Mapping[str, Any]]],
    authority_state: Mapping[str, Any],
    scope_binding: Any,
    curriculum_records: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    """Compose the existing preflight with explicit successor-scope hard gates.

    Historical/global execution authority is intentionally insufficient. The
    successor scope needs an exact scope identity, exact binding identity,
    successor-specific execution authority, and a real PASS guard snapshot.
    """

    base = preflight_run_manifest(manifest, component_store, authority_state)
    reason_codes = list(base["reason_codes"])
    scope_errors = validate_research_component_scope_binding(
        scope_binding,
        curriculum_records,
    )

    if scope_errors:
        reason_codes.append("RESEARCH_COMPONENT_SCOPE_BINDING_INVALID")

    binding_id = scope_binding.get("binding_id") if isinstance(scope_binding, Mapping) else None

    if authority_state.get("research_component_scope_id") != RESEARCH_COMPONENT_SCOPE_ID:
        reason_codes.append("RESEARCH_COMPONENT_SCOPE_AUTHORITY_MISMATCH")
    if authority_state.get("research_component_scope_binding_id") != binding_id:
        reason_codes.append("RESEARCH_COMPONENT_SCOPE_BINDING_STALE_OR_MISMATCH")
    if authority_state.get("research_component_execution_authority") != "AUTHORIZED":
        reason_codes.append("RESEARCH_COMPONENT_EXECUTION_AUTHORITY_NONE")
    if authority_state.get("research_component_guard_snapshot_state") != "PASS":
        reason_codes.append("RESEARCH_COMPONENT_GUARD_SNAPSHOT_NOT_PASS")

    ordered_reasons = list(dict.fromkeys(reason_codes))
    return {
        **base,
        "allowed": not ordered_reasons,
        "reason_codes": ordered_reasons,
        "research_component_scope_validation_errors": scope_errors,
        "research_component_scope_id": RESEARCH_COMPONENT_SCOPE_ID,
    }
