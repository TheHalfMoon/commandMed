"""Offline tests for the SP007-RO-001 research-component scope binding."""

from __future__ import annotations

from src.commandmed.spec007.curriculum import compute_curriculum_record_sha256
from src.commandmed.spec007.research_scope import (
    RESEARCH_COMPONENT_ADMITTED_CAPABILITIES,
    RESEARCH_COMPONENT_CLAIM_CLASS,
    RESEARCH_COMPONENT_EXCLUDED_CAPABILITIES,
    RESEARCH_COMPONENT_REQUIRED_GUARDS,
    RESEARCH_COMPONENT_SCOPE_CLASS,
    RESEARCH_COMPONENT_SCOPE_ID,
    preflight_research_component_run_manifest,
    validate_research_component_scope_binding,
)


def learner_record() -> dict[str, object]:
    record: dict[str, object] = {
        "schema_version": "1",
        "record_id": "synthetic-research-record-001",
        "record_canonical_sha256": "0" * 64,
        "content_sha256": "1" * 64,
        "source_authority_id": "synthetic-authority",
        "source_license_id": "synthetic-license",
        "source_verification_status": "VERIFIED",
        "split_id": "VERIFIED_SFT_CURRICULUM_DATA",
        "contamination_status": "ASSESSED_CLEAN",
        "review_state": "PASS",
        "role_class": "LEARNER_RESEARCHER",
        "curriculum_strata": ["general_instruction_following", "research_formatting"],
        "language_profile": {
            "primary_language": "en",
            "authored_language": "en",
            "translation_state": "ORIGINAL",
            "dialect_or_register": "GENERAL",
            "code_switch_state": "NONE",
            "transliteration_state": "NONE",
            "terminology_normalization_id": None,
            "qualified_review_state": "PASS",
        },
        "conversation_structure_id": "single-turn-v1",
        "knowledge_placement": "DURABLE_WEIGHT_ELIGIBLE",
        "quarantine_disposition": "PASS",
    }
    record["record_canonical_sha256"] = compute_curriculum_record_sha256(record)
    return record


def scope_binding() -> dict[str, object]:
    sentinel_bindings = [
        {
            "fixture_id": f"synthetic:{guard.lower()}:v1",
            "guard_id": guard,
            "expected_action": "ESCALATE"
            if guard == "RO_GUARD_003_EMERGENCY_SENTINEL"
            else "ABSTAIN",
            "optimization_feedback_allowed": False,
        }
        for guard in sorted(RESEARCH_COMPONENT_REQUIRED_GUARDS)
    ]
    return {
        "schema_version": "1",
        "binding_id": "research-scope-binding:synthetic:v1",
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "scope_class": RESEARCH_COMPONENT_SCOPE_CLASS,
        "claim_class": RESEARCH_COMPONENT_CLAIM_CLASS,
        "gradient_record_bindings": [
            {
                "record_id": "synthetic-research-record-001",
                "target_capability_ids": ["GENERAL_INSTRUCTION_FOLLOWING"],
                "content_scope_verification_state": "PASS",
                "optimization_feedback_allowed": True,
            }
        ],
        "sentinel_fixture_bindings": sentinel_bindings,
        "excluded_capability_ids": sorted(RESEARCH_COMPONENT_EXCLUDED_CAPABILITIES),
        "required_guard_ids": sorted(RESEARCH_COMPONENT_REQUIRED_GUARDS),
        "system_qualification_created": False,
        "clinical_qualification_created": False,
    }


def curriculum_records() -> dict[str, dict[str, object]]:
    return {"synthetic-research-record-001": learner_record()}


def test_valid_research_component_scope_binding_passes() -> None:
    assert validate_research_component_scope_binding(
        scope_binding(), curriculum_records()
    ) == []


def test_gradient_record_must_be_learner_researcher_only() -> None:
    records = curriculum_records()
    record = records["synthetic-research-record-001"]
    record["role_class"] = "PATIENT_CAREGIVER"
    record["record_canonical_sha256"] = compute_curriculum_record_sha256(record)

    errors = validate_research_component_scope_binding(scope_binding(), records)

    assert any("role_class must equal LEARNER_RESEARCHER" in error for error in errors)


def test_excluded_clinical_capability_cannot_be_gradient_target() -> None:
    binding = scope_binding()
    binding["gradient_record_bindings"][0]["target_capability_ids"] = [
        "PATIENT_SPECIFIC_DIAGNOSIS"
    ]

    errors = validate_research_component_scope_binding(binding, curriculum_records())

    assert any("outside admitted scope" in error for error in errors)


def test_gradient_capability_vocabulary_is_frozen() -> None:
    binding = scope_binding()
    binding["gradient_record_bindings"][0]["target_capability_ids"] = [
        "UNDECLARED_RESEARCH_CAPABILITY"
    ]

    errors = validate_research_component_scope_binding(binding, curriculum_records())

    assert any("outside admitted scope" in error for error in errors)
    assert "UNDECLARED_RESEARCH_CAPABILITY" not in RESEARCH_COMPONENT_ADMITTED_CAPABILITIES


def test_sentinel_fixtures_are_abort_disqualify_only() -> None:
    binding = scope_binding()
    binding["sentinel_fixture_bindings"][0]["optimization_feedback_allowed"] = True

    errors = validate_research_component_scope_binding(binding, curriculum_records())

    assert any(
        "optimization_feedback_allowed must be false" in error for error in errors
    )


def test_every_successor_guard_requires_one_bound_fixture() -> None:
    binding = scope_binding()
    binding["sentinel_fixture_bindings"].pop()

    errors = validate_research_component_scope_binding(binding, curriculum_records())

    assert any("every canonical successor guard" in error for error in errors)


def test_excluded_capability_set_cannot_be_narrowed() -> None:
    binding = scope_binding()
    binding["excluded_capability_ids"] = sorted(RESEARCH_COMPONENT_EXCLUDED_CAPABILITIES)[1:]

    errors = validate_research_component_scope_binding(binding, curriculum_records())

    assert any("must equal the canonical frozen set" in error for error in errors)


def test_content_scope_verification_is_required_for_gradient_records() -> None:
    binding = scope_binding()
    binding["gradient_record_bindings"][0]["content_scope_verification_state"] = (
        "NEEDS_EVIDENCE"
    )

    errors = validate_research_component_scope_binding(binding, curriculum_records())

    assert any("content_scope_verification_state" in error for error in errors)


def test_global_execution_authority_does_not_imply_successor_execution_authority() -> None:
    authority_state = {
        "training_authorization_id": "authorized:synthetic",
        "finance_authorization_id": "authorized:synthetic",
        "access_authorization_ids": [],
        "model_execution_authority": "AUTHORIZED",
        "weight_access_authority": "AUTHORIZED",
        "device_execution_authority": "AUTHORIZED",
        "research_component_scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "research_component_scope_binding_id": "research-scope-binding:synthetic:v1",
        "research_component_execution_authority": "NONE",
        "research_component_guard_snapshot_state": "PASS",
    }

    result = preflight_research_component_run_manifest(
        manifest={},
        component_store={},
        authority_state=authority_state,
        scope_binding=scope_binding(),
        curriculum_records=curriculum_records(),
    )

    assert result["allowed"] is False
    assert "RESEARCH_COMPONENT_EXECUTION_AUTHORITY_NONE" in result["reason_codes"]
    assert result["research_component_scope_validation_errors"] == []


def test_real_guard_snapshot_is_separate_from_fixture_binding() -> None:
    authority_state = {
        "training_authorization_id": "authorized:synthetic",
        "finance_authorization_id": "authorized:synthetic",
        "access_authorization_ids": [],
        "model_execution_authority": "AUTHORIZED",
        "weight_access_authority": "AUTHORIZED",
        "device_execution_authority": "AUTHORIZED",
        "research_component_scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "research_component_scope_binding_id": "research-scope-binding:synthetic:v1",
        "research_component_execution_authority": "AUTHORIZED",
        "research_component_guard_snapshot_state": "ABSENT",
    }

    result = preflight_research_component_run_manifest(
        manifest={},
        component_store={},
        authority_state=authority_state,
        scope_binding=scope_binding(),
        curriculum_records=curriculum_records(),
    )

    assert result["allowed"] is False
    assert "RESEARCH_COMPONENT_GUARD_SNAPSHOT_NOT_PASS" in result["reason_codes"]
