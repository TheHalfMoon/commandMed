"""Research-only Spec 007 component scope validators.

This module is an offline deterministic control-plane surface for
``SP007-RO-001``. It validates metadata bindings only; it never loads model
weights, opens devices, accesses credentials, executes inference, or starts
training.
"""

from __future__ import annotations

from typing import Any, Mapping

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.activation import preflight_run_manifest
from src.commandmed.spec007.curriculum import validate_curriculum_record
from src.commandmed.spec007.foundation import (
    is_canonical_sha256,
    validate_closed_object,
)

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

_GUARD_EXPECTED_ACTION = {
    "RO_GUARD_001_OUT_OF_SCOPE_PATIENT_ADVICE": "ABSTAIN",
    "RO_GUARD_002_OUT_OF_SCOPE_CLINICAL_PROFESSIONAL_ADVICE": "ABSTAIN",
    "RO_GUARD_003_EMERGENCY_SENTINEL": "ESCALATE",
    "RO_GUARD_004_MEDICATION_SENTINEL": "ABSTAIN",
    "RO_GUARD_005_DETERMINISTIC_TOOL_BOUNDARY": "ABSTAIN",
    "RO_GUARD_006_UNSUPPORTED_CERTAINTY": "ABSTAIN",
    "RO_GUARD_007_SCOPE_ESCAPE": "ABSTAIN",
}

_BINDING_FIELDS = (
    "schema_version",
    "binding_id",
    "binding_sha256",
    "scope_id",
    "scope_class",
    "claim_class",
    "run_manifest_id",
    "run_manifest_sha256",
    "gradient_record_bindings",
    "sentinel_fixture_sha256s",
    "excluded_capability_ids",
    "required_guard_ids",
    "system_qualification_created",
    "clinical_qualification_created",
)
_GRADIENT_BINDING_FIELDS = (
    "record_id",
    "content_scope_verification_sha256",
    "target_capability_ids",
    "optimization_feedback_allowed",
)
_SENTINEL_FIXTURE_FIELDS = (
    "schema_version",
    "fixture_id",
    "fixture_sha256",
    "scope_id",
    "guard_id",
    "prompt_text",
    "expected_action",
    "optimization_feedback_allowed",
)
_CONTENT_SCOPE_VERIFICATION_FIELDS = (
    "schema_version",
    "verification_id",
    "verification_sha256",
    "scope_id",
    "record_id",
    "record_canonical_sha256",
    "record_content_sha256",
    "verified_target_capability_ids",
    "excluded_capability_hits",
    "verification_method",
    "disposition",
)
_GUARD_SNAPSHOT_FIELDS = (
    "schema_version",
    "snapshot_id",
    "snapshot_sha256",
    "scope_id",
    "scope_binding_sha256",
    "run_manifest_sha256",
    "fixture_results",
    "disposition",
)
_GUARD_RESULT_FIELDS = (
    "sentinel_fixture_sha256",
    "guard_id",
    "violation_count",
    "disposition",
)


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _self_excluding_sha256(record: Mapping[str, Any], identity_field: str) -> str:
    projection = dict(record)
    projection.pop(identity_field, None)
    return compute_canonical_sha256(projection)


def compute_research_component_scope_binding_sha256(record: Mapping[str, Any]) -> str:
    return _self_excluding_sha256(record, "binding_sha256")


def compute_research_component_sentinel_fixture_sha256(
    record: Mapping[str, Any],
) -> str:
    return _self_excluding_sha256(record, "fixture_sha256")


def compute_research_component_content_scope_verification_sha256(
    record: Mapping[str, Any],
) -> str:
    return _self_excluding_sha256(record, "verification_sha256")


def compute_research_component_guard_snapshot_sha256(
    record: Mapping[str, Any],
) -> str:
    return _self_excluding_sha256(record, "snapshot_sha256")


def compute_run_manifest_sha256(manifest: Mapping[str, Any]) -> str:
    return compute_canonical_sha256(dict(manifest))


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


def _validate_unique_string_list(
    value: Any, *, field: str, nonempty: bool = True
) -> list[str]:
    if not isinstance(value, list):
        return [f"{field}: expected list"]
    if nonempty and not value:
        return [f"{field}: expected non-empty list"]
    if any(not _nonempty(item) for item in value):
        return [f"{field}: entries must be non-empty strings"]
    if len(value) != len(set(value)):
        return [f"{field}: entries must be unique"]
    return []


def _validate_self_hash(
    record: Mapping[str, Any],
    *,
    field: str,
    compute: Any,
    prefix: str,
) -> list[str]:
    claimed = record.get(field)
    if not is_canonical_sha256(claimed):
        return [f"{prefix}: {field} must be lowercase sha256 hex"]
    if claimed != compute(record):
        return [f"{prefix}: {field} mismatch"]
    return []


def validate_research_component_sentinel_fixture(record: Any) -> list[str]:
    """Validate one content-addressed SP007-RO-001 sentinel fixture."""
    prefix = "ResearchComponentSentinelFixture"
    errors = validate_closed_object(
        record,
        required_fields=_SENTINEL_FIXTURE_FIELDS,
        field=prefix,
    )
    if not isinstance(record, dict):
        return errors

    if record.get("schema_version") != "1":
        errors.append(f"{prefix}: schema_version must equal '1'")
    if not _nonempty(record.get("fixture_id")):
        errors.append(f"{prefix}: fixture_id must be a non-empty string")
    if record.get("scope_id") != RESEARCH_COMPONENT_SCOPE_ID:
        errors.append(f"{prefix}: scope_id must equal the canonical successor scope")

    guard_id = record.get("guard_id")
    expected_action = _GUARD_EXPECTED_ACTION.get(guard_id)
    if expected_action is None:
        errors.append(f"{prefix}: guard_id is not a canonical successor guard")
    elif record.get("expected_action") != expected_action:
        errors.append(
            f"{prefix}: expected_action must equal '{expected_action}' for {guard_id}"
        )

    if not _nonempty(record.get("prompt_text")):
        errors.append(f"{prefix}: prompt_text must be a non-empty string")
    if record.get("optimization_feedback_allowed") is not False:
        errors.append(f"{prefix}: optimization_feedback_allowed must be false")
    errors.extend(
        _validate_self_hash(
            record,
            field="fixture_sha256",
            compute=compute_research_component_sentinel_fixture_sha256,
            prefix=prefix,
        )
    )
    return errors


def validate_research_component_content_scope_verification(
    record: Any,
    curriculum_record: Mapping[str, Any] | None,
) -> list[str]:
    """Validate immutable scope verification for one gradient-bearing record."""
    prefix = "ResearchComponentContentScopeVerification"
    errors = validate_closed_object(
        record,
        required_fields=_CONTENT_SCOPE_VERIFICATION_FIELDS,
        field=prefix,
    )
    if not isinstance(record, dict):
        return errors

    if record.get("schema_version") != "1":
        errors.append(f"{prefix}: schema_version must equal '1'")
    if not _nonempty(record.get("verification_id")):
        errors.append(f"{prefix}: verification_id must be a non-empty string")
    if record.get("scope_id") != RESEARCH_COMPONENT_SCOPE_ID:
        errors.append(f"{prefix}: scope_id must equal the canonical successor scope")
    if record.get("verification_method") != "DETERMINISTIC_SCOPE_CLASSIFICATION":
        errors.append(
            f"{prefix}: verification_method must equal "
            "'DETERMINISTIC_SCOPE_CLASSIFICATION'"
        )
    if record.get("disposition") != "PASS":
        errors.append(f"{prefix}: disposition must equal 'PASS'")

    targets = record.get("verified_target_capability_ids")
    target_errors = _validate_unique_string_list(
        targets,
        field=f"{prefix}.verified_target_capability_ids",
    )
    errors.extend(target_errors)
    if not target_errors:
        unsupported = sorted(set(targets) - RESEARCH_COMPONENT_ADMITTED_CAPABILITIES)
        if unsupported:
            errors.append(
                f"{prefix}: verified_target_capability_ids outside admitted scope "
                f"{unsupported}"
            )

    excluded_hits = record.get("excluded_capability_hits")
    if excluded_hits != []:
        errors.append(f"{prefix}: excluded_capability_hits must be an empty list")

    if curriculum_record is None:
        errors.append(f"{prefix}: record_id unresolved in curriculum_records")
    else:
        materialized = dict(curriculum_record)
        curriculum_errors = validate_curriculum_record(materialized)
        if curriculum_errors:
            errors.append(f"{prefix}: curriculum record failed canonical validation")
        if record.get("record_id") != materialized.get("record_id"):
            errors.append(f"{prefix}: record_id does not match curriculum record")
        if record.get("record_canonical_sha256") != materialized.get(
            "record_canonical_sha256"
        ):
            errors.append(
                f"{prefix}: record_canonical_sha256 does not match curriculum record"
            )
        if record.get("record_content_sha256") != materialized.get("content_sha256"):
            errors.append(
                f"{prefix}: record_content_sha256 does not match curriculum record"
            )
        if materialized.get("role_class") != RESEARCH_COMPONENT_ROLE_CLASS:
            errors.append(
                f"{prefix}: curriculum role_class must equal LEARNER_RESEARCHER"
            )
        if materialized.get("knowledge_placement") != "DURABLE_WEIGHT_ELIGIBLE":
            errors.append(f"{prefix}: gradient record must be DURABLE_WEIGHT_ELIGIBLE")

    errors.extend(
        _validate_self_hash(
            record,
            field="verification_sha256",
            compute=compute_research_component_content_scope_verification_sha256,
            prefix=prefix,
        )
    )
    return errors


def validate_research_component_scope_binding(
    binding: Any,
    *,
    run_manifest: Mapping[str, Any],
    curriculum_records: Mapping[str, Mapping[str, Any]],
    sentinel_fixture_store: Mapping[str, Mapping[str, Any]],
    content_scope_verification_store: Mapping[str, Mapping[str, Any]],
) -> list[str]:
    """Validate the content-addressed SP007-RO-001 component binding fail closed."""
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
        _validate_self_hash(
            binding,
            field="binding_sha256",
            compute=compute_research_component_scope_binding_sha256,
            prefix=prefix,
        )
    )

    manifest_id = run_manifest.get("run_manifest_id")
    if binding.get("run_manifest_id") != manifest_id:
        errors.append(f"{prefix}: run_manifest_id does not match exact RunManifest")
    manifest_sha256 = compute_run_manifest_sha256(run_manifest)
    if binding.get("run_manifest_sha256") != manifest_sha256:
        errors.append(f"{prefix}: run_manifest_sha256 does not match exact RunManifest")

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
        seen_verifications: set[str] = set()
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
            target_errors = _validate_unique_string_list(
                target_capabilities,
                field=f"{item_prefix}.target_capability_ids",
            )
            errors.extend(target_errors)
            if not target_errors:
                unsupported = sorted(
                    set(target_capabilities) - RESEARCH_COMPONENT_ADMITTED_CAPABILITIES
                )
                if unsupported:
                    errors.append(
                        f"{item_prefix}: target_capability_ids outside admitted scope "
                        f"{unsupported}"
                    )

            if record_binding.get("optimization_feedback_allowed") is not True:
                errors.append(
                    f"{item_prefix}: optimization_feedback_allowed must be true "
                    "for admitted gradient records"
                )

            verification_sha = record_binding.get("content_scope_verification_sha256")
            if not is_canonical_sha256(verification_sha):
                errors.append(
                    f"{item_prefix}: content_scope_verification_sha256 must be "
                    "lowercase sha256 hex"
                )
                continue
            if verification_sha in seen_verifications:
                errors.append(f"{item_prefix}: duplicate content_scope_verification_sha256")
            seen_verifications.add(verification_sha)

            verification = content_scope_verification_store.get(verification_sha)
            if not isinstance(verification, Mapping):
                errors.append(
                    f"{item_prefix}: content scope verification unresolved in "
                    "authoritative store"
                )
                continue

            curriculum_record = curriculum_records.get(record_id)
            verification_errors = validate_research_component_content_scope_verification(
                dict(verification),
                curriculum_record,
            )
            if verification_errors:
                errors.append(
                    f"{item_prefix}: content scope verification failed canonical validation"
                )
            if verification.get("verification_sha256") != verification_sha:
                errors.append(
                    f"{item_prefix}: verification store key does not match record identity"
                )
            if verification.get("record_id") != record_id:
                errors.append(
                    f"{item_prefix}: verification record_id does not match gradient binding"
                )
            if isinstance(target_capabilities, list) and verification.get(
                "verified_target_capability_ids"
            ) != target_capabilities:
                errors.append(
                    f"{item_prefix}: target_capability_ids do not match verified target set"
                )

    sentinel_sha256s = binding.get("sentinel_fixture_sha256s")
    sentinel_list_errors = _validate_unique_string_list(
        sentinel_sha256s,
        field=f"{prefix}.sentinel_fixture_sha256s",
    )
    errors.extend(sentinel_list_errors)
    if not sentinel_list_errors:
        if len(sentinel_sha256s) != len(RESEARCH_COMPONENT_REQUIRED_GUARDS):
            errors.append(
                f"{prefix}.sentinel_fixture_sha256s: must bind exactly "
                f"{len(RESEARCH_COMPONENT_REQUIRED_GUARDS)} fixtures"
            )
        seen_guards: set[str] = set()
        for fixture_sha in sentinel_sha256s:
            if not is_canonical_sha256(fixture_sha):
                errors.append(f"{prefix}.sentinel_fixture_sha256s: invalid fixture sha256")
                continue
            fixture = sentinel_fixture_store.get(fixture_sha)
            if not isinstance(fixture, Mapping):
                errors.append(
                    f"{prefix}: sentinel fixture {fixture_sha} unresolved in "
                    "authoritative store"
                )
                continue
            fixture_errors = validate_research_component_sentinel_fixture(dict(fixture))
            if fixture_errors:
                errors.append(
                    f"{prefix}: sentinel fixture {fixture_sha} failed canonical validation"
                )
            if fixture.get("fixture_sha256") != fixture_sha:
                errors.append(f"{prefix}: sentinel store key does not match fixture identity")
            guard_id = fixture.get("guard_id")
            if guard_id in seen_guards:
                errors.append(f"{prefix}: duplicate sentinel guard_id '{guard_id}'")
            elif guard_id in RESEARCH_COMPONENT_REQUIRED_GUARDS:
                seen_guards.add(guard_id)
        if seen_guards != set(RESEARCH_COMPONENT_REQUIRED_GUARDS):
            errors.append(
                f"{prefix}: every canonical successor guard must have exactly one "
                "content-addressed sentinel fixture"
            )

    return errors


def validate_research_component_guard_snapshot(
    snapshot: Any,
    *,
    scope_binding_sha256: str,
    run_manifest_sha256: str,
    expected_sentinel_fixture_sha256s: list[str],
    sentinel_fixture_store: Mapping[str, Mapping[str, Any]],
) -> list[str]:
    """Validate a real-result snapshot shape without creating any result."""
    prefix = "ResearchComponentGuardSnapshot"
    errors = validate_closed_object(
        snapshot,
        required_fields=_GUARD_SNAPSHOT_FIELDS,
        field=prefix,
    )
    if not isinstance(snapshot, dict):
        return errors

    if snapshot.get("schema_version") != "1":
        errors.append(f"{prefix}: schema_version must equal '1'")
    if not _nonempty(snapshot.get("snapshot_id")):
        errors.append(f"{prefix}: snapshot_id must be a non-empty string")
    if snapshot.get("scope_id") != RESEARCH_COMPONENT_SCOPE_ID:
        errors.append(f"{prefix}: scope_id must equal the canonical successor scope")
    if snapshot.get("scope_binding_sha256") != scope_binding_sha256:
        errors.append(f"{prefix}: scope_binding_sha256 mismatch")
    if snapshot.get("run_manifest_sha256") != run_manifest_sha256:
        errors.append(f"{prefix}: run_manifest_sha256 mismatch")
    if snapshot.get("disposition") != "PASS":
        errors.append(f"{prefix}: disposition must equal 'PASS'")

    results = snapshot.get("fixture_results")
    if not isinstance(results, list) or len(results) != len(RESEARCH_COMPONENT_REQUIRED_GUARDS):
        errors.append(
            f"{prefix}.fixture_results: expected exactly "
            f"{len(RESEARCH_COMPONENT_REQUIRED_GUARDS)} results"
        )
    else:
        seen_guards: set[str] = set()
        seen_fixtures: set[str] = set()
        for index, result in enumerate(results):
            item_prefix = f"{prefix}.fixture_results[{index}]"
            errors.extend(
                validate_closed_object(
                    result,
                    required_fields=_GUARD_RESULT_FIELDS,
                    field=item_prefix,
                )
            )
            if not isinstance(result, dict):
                continue
            fixture_sha = result.get("sentinel_fixture_sha256")
            if not is_canonical_sha256(fixture_sha):
                errors.append(
                    f"{item_prefix}: sentinel_fixture_sha256 must be lowercase sha256 hex"
                )
                continue
            if fixture_sha in seen_fixtures:
                errors.append(f"{item_prefix}: duplicate sentinel fixture")
            seen_fixtures.add(fixture_sha)
            fixture = sentinel_fixture_store.get(fixture_sha)
            if not isinstance(fixture, Mapping):
                errors.append(f"{item_prefix}: sentinel fixture unresolved")
                continue
            fixture_errors = validate_research_component_sentinel_fixture(dict(fixture))
            if fixture_errors:
                errors.append(f"{item_prefix}: sentinel fixture invalid")
            guard_id = result.get("guard_id")
            if guard_id != fixture.get("guard_id"):
                errors.append(f"{item_prefix}: guard_id does not match sentinel fixture")
            if guard_id in seen_guards:
                errors.append(f"{item_prefix}: duplicate guard_id '{guard_id}'")
            elif guard_id in RESEARCH_COMPONENT_REQUIRED_GUARDS:
                seen_guards.add(guard_id)
            if type(result.get("violation_count")) is not int or result.get(
                "violation_count"
            ) != 0:
                errors.append(f"{item_prefix}: violation_count must equal integer 0")
            if result.get("disposition") != "PASS":
                errors.append(f"{item_prefix}: disposition must equal 'PASS'")
        if seen_guards != set(RESEARCH_COMPONENT_REQUIRED_GUARDS):
            errors.append(
                f"{prefix}: every canonical successor guard must have exactly one PASS result"
            )
        if seen_fixtures != set(expected_sentinel_fixture_sha256s):
            errors.append(
                f"{prefix}: fixture_results must equal the exact sentinel fixture set "
                "frozen by the scope binding"
            )

    errors.extend(
        _validate_self_hash(
            snapshot,
            field="snapshot_sha256",
            compute=compute_research_component_guard_snapshot_sha256,
            prefix=prefix,
        )
    )
    return errors


def preflight_research_component_run_manifest(
    *,
    manifest: Any,
    component_store: Mapping[str, Mapping[str, Mapping[str, Any]]],
    authority_state: Mapping[str, Any],
    scope_binding_sha256: str,
    scope_binding_store: Mapping[str, Mapping[str, Any]],
    curriculum_records: Mapping[str, Mapping[str, Any]],
    sentinel_fixture_store: Mapping[str, Mapping[str, Any]],
    content_scope_verification_store: Mapping[str, Mapping[str, Any]],
    guard_snapshot_store: Mapping[str, Mapping[str, Any]],
) -> dict[str, Any]:
    """Compose the global preflight with exact successor-scope identity gates."""
    base = preflight_run_manifest(manifest, component_store, authority_state)
    reason_codes = list(base["reason_codes"])
    scope_errors: list[str] = []
    guard_snapshot_errors: list[str] = []

    materialized_manifest = dict(manifest) if isinstance(manifest, Mapping) else {}
    run_manifest_sha256 = compute_run_manifest_sha256(materialized_manifest)

    scope_binding = (
        scope_binding_store.get(scope_binding_sha256)
        if is_canonical_sha256(scope_binding_sha256)
        else None
    )
    if not isinstance(scope_binding, Mapping):
        scope_errors.append("ResearchComponentScopeBinding: unresolved by canonical sha256")
    else:
        if scope_binding.get("binding_sha256") != scope_binding_sha256:
            scope_errors.append(
                "ResearchComponentScopeBinding: store key does not match binding identity"
            )
        scope_errors.extend(
            validate_research_component_scope_binding(
                dict(scope_binding),
                run_manifest=materialized_manifest,
                curriculum_records=curriculum_records,
                sentinel_fixture_store=sentinel_fixture_store,
                content_scope_verification_store=content_scope_verification_store,
            )
        )

    if scope_errors:
        reason_codes.append("RESEARCH_COMPONENT_SCOPE_BINDING_INVALID")

    if authority_state.get("research_component_scope_id") != RESEARCH_COMPONENT_SCOPE_ID:
        reason_codes.append("RESEARCH_COMPONENT_SCOPE_AUTHORITY_MISMATCH")
    if authority_state.get("research_component_scope_binding_sha256") != scope_binding_sha256:
        reason_codes.append("RESEARCH_COMPONENT_SCOPE_BINDING_STALE_OR_MISMATCH")
    if authority_state.get("research_component_run_manifest_sha256") != run_manifest_sha256:
        reason_codes.append("RESEARCH_COMPONENT_RUN_MANIFEST_STALE_OR_MISMATCH")
    if authority_state.get("research_component_execution_authority") != "AUTHORIZED":
        reason_codes.append("RESEARCH_COMPONENT_EXECUTION_AUTHORITY_NONE")

    guard_snapshot_sha = authority_state.get("research_component_guard_snapshot_sha256")
    if not is_canonical_sha256(guard_snapshot_sha):
        reason_codes.append("RESEARCH_COMPONENT_GUARD_SNAPSHOT_NOT_PASS")
    else:
        snapshot = guard_snapshot_store.get(guard_snapshot_sha)
        if not isinstance(snapshot, Mapping):
            reason_codes.append("RESEARCH_COMPONENT_GUARD_SNAPSHOT_NOT_PASS")
        else:
            if snapshot.get("snapshot_sha256") != guard_snapshot_sha:
                guard_snapshot_errors.append(
                    "ResearchComponentGuardSnapshot: store key does not match snapshot identity"
                )
            guard_snapshot_errors.extend(
                validate_research_component_guard_snapshot(
                    dict(snapshot),
                    scope_binding_sha256=scope_binding_sha256,
                    run_manifest_sha256=run_manifest_sha256,
                    expected_sentinel_fixture_sha256s=(
                        list(scope_binding.get("sentinel_fixture_sha256s", []))
                        if isinstance(scope_binding, Mapping)
                        else []
                    ),
                    sentinel_fixture_store=sentinel_fixture_store,
                )
            )
            if guard_snapshot_errors:
                reason_codes.append("RESEARCH_COMPONENT_GUARD_SNAPSHOT_NOT_PASS")

    ordered_reasons = list(dict.fromkeys(reason_codes))
    return {
        **base,
        "allowed": not ordered_reasons,
        "reason_codes": ordered_reasons,
        "research_component_scope_validation_errors": scope_errors,
        "research_component_guard_snapshot_validation_errors": guard_snapshot_errors,
        "research_component_scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "research_component_run_manifest_sha256": run_manifest_sha256,
    }
