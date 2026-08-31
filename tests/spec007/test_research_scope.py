"""Offline tests for the SP007-RO-001 research-component scope binding."""

from __future__ import annotations

from copy import deepcopy

from src.commandmed.spec007.curriculum import compute_curriculum_record_sha256
from src.commandmed.spec007.research_scope import (
    RESEARCH_COMPONENT_ADMITTED_CAPABILITIES,
    RESEARCH_COMPONENT_CLAIM_CLASS,
    RESEARCH_COMPONENT_EXCLUDED_CAPABILITIES,
    RESEARCH_COMPONENT_REQUIRED_GUARDS,
    RESEARCH_COMPONENT_SCOPE_CLASS,
    RESEARCH_COMPONENT_SCOPE_ID,
    compute_research_component_content_scope_verification_sha256,
    compute_research_component_guard_snapshot_sha256,
    compute_research_component_scope_binding_sha256,
    compute_research_component_sentinel_fixture_sha256,
    compute_run_manifest_sha256,
    preflight_research_component_run_manifest,
    validate_research_component_guard_snapshot,
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


def run_manifest() -> dict[str, object]:
    return {
        "run_manifest_id": "run:research-component:synthetic:v1",
        "synthetic_fixture_only": True,
    }


def content_scope_verification(
    record: dict[str, object],
    targets: list[str] | None = None,
) -> dict[str, object]:
    verification: dict[str, object] = {
        "schema_version": "1",
        "verification_id": "scope-verification:synthetic:v1",
        "verification_sha256": "0" * 64,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "record_id": record["record_id"],
        "record_canonical_sha256": record["record_canonical_sha256"],
        "record_content_sha256": record["content_sha256"],
        "verified_target_capability_ids": targets or ["GENERAL_INSTRUCTION_FOLLOWING"],
        "excluded_capability_hits": [],
        "verification_method": "DETERMINISTIC_SCOPE_CLASSIFICATION",
        "disposition": "PASS",
    }
    verification["verification_sha256"] = (
        compute_research_component_content_scope_verification_sha256(verification)
    )
    return verification


def sentinel_fixture(guard_id: str) -> dict[str, object]:
    expected_action = (
        "ESCALATE"
        if guard_id == "RO_GUARD_003_EMERGENCY_SENTINEL"
        else "ABSTAIN"
    )
    fixture: dict[str, object] = {
        "schema_version": "1",
        "fixture_id": f"fixture:{guard_id.lower()}:synthetic:v1",
        "fixture_sha256": "0" * 64,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "guard_id": guard_id,
        "prompt_text": f"Synthetic guard stimulus for {guard_id}.",
        "expected_action": expected_action,
        "optimization_feedback_allowed": False,
    }
    fixture["fixture_sha256"] = compute_research_component_sentinel_fixture_sha256(
        fixture
    )
    return fixture


def valid_bundle() -> dict[str, object]:
    manifest = run_manifest()
    record = learner_record()
    verification = content_scope_verification(record)
    fixtures = [
        sentinel_fixture(guard)
        for guard in sorted(RESEARCH_COMPONENT_REQUIRED_GUARDS)
    ]
    fixture_store = {fixture["fixture_sha256"]: fixture for fixture in fixtures}
    verification_store = {verification["verification_sha256"]: verification}
    binding: dict[str, object] = {
        "schema_version": "1",
        "binding_id": "research-scope-binding:synthetic:v1",
        "binding_sha256": "0" * 64,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "scope_class": RESEARCH_COMPONENT_SCOPE_CLASS,
        "claim_class": RESEARCH_COMPONENT_CLAIM_CLASS,
        "run_manifest_id": manifest["run_manifest_id"],
        "run_manifest_sha256": compute_run_manifest_sha256(manifest),
        "gradient_record_bindings": [
            {
                "record_id": record["record_id"],
                "content_scope_verification_sha256": verification[
                    "verification_sha256"
                ],
                "target_capability_ids": ["GENERAL_INSTRUCTION_FOLLOWING"],
                "optimization_feedback_allowed": True,
            }
        ],
        "sentinel_fixture_sha256s": sorted(fixture_store),
        "excluded_capability_ids": sorted(RESEARCH_COMPONENT_EXCLUDED_CAPABILITIES),
        "required_guard_ids": sorted(RESEARCH_COMPONENT_REQUIRED_GUARDS),
        "system_qualification_created": False,
        "clinical_qualification_created": False,
    }
    binding["binding_sha256"] = compute_research_component_scope_binding_sha256(
        binding
    )
    return {
        "manifest": manifest,
        "curriculum_records": {record["record_id"]: record},
        "verification_store": verification_store,
        "fixture_store": fixture_store,
        "binding": binding,
    }


def guard_snapshot(bundle: dict[str, object]) -> dict[str, object]:
    binding = bundle["binding"]
    manifest = bundle["manifest"]
    fixture_store = bundle["fixture_store"]
    results = [
        {
            "sentinel_fixture_sha256": fixture_sha,
            "guard_id": fixture["guard_id"],
            "violation_count": 0,
            "disposition": "PASS",
        }
        for fixture_sha, fixture in sorted(fixture_store.items())
    ]
    snapshot: dict[str, object] = {
        "schema_version": "1",
        "snapshot_id": "guard-snapshot:synthetic:v1",
        "snapshot_sha256": "0" * 64,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "scope_binding_sha256": binding["binding_sha256"],
        "run_manifest_sha256": compute_run_manifest_sha256(manifest),
        "fixture_results": results,
        "disposition": "PASS",
    }
    snapshot["snapshot_sha256"] = compute_research_component_guard_snapshot_sha256(
        snapshot
    )
    return snapshot


def validate_bundle(bundle: dict[str, object]) -> list[str]:
    return validate_research_component_scope_binding(
        bundle["binding"],
        run_manifest=bundle["manifest"],
        curriculum_records=bundle["curriculum_records"],
        sentinel_fixture_store=bundle["fixture_store"],
        content_scope_verification_store=bundle["verification_store"],
    )


def successor_authority_state(
    bundle: dict[str, object],
    snapshot: dict[str, object],
    *,
    execution_authority: str = "AUTHORIZED",
) -> dict[str, object]:
    return {
        "training_authorization_id": "NONE",
        "finance_authorization_id": "NONE",
        "access_authorization_ids": [],
        "model_execution_authority": "AUTHORIZED",
        "weight_access_authority": "AUTHORIZED",
        "device_execution_authority": "AUTHORIZED",
        "research_component_scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "research_component_scope_binding_sha256": bundle["binding"][
            "binding_sha256"
        ],
        "research_component_run_manifest_sha256": compute_run_manifest_sha256(
            bundle["manifest"]
        ),
        "research_component_execution_authority": execution_authority,
        "research_component_guard_snapshot_sha256": snapshot["snapshot_sha256"],
    }


def preflight_bundle(
    bundle: dict[str, object],
    authority_state: dict[str, object],
    snapshot_store: dict[str, dict[str, object]],
) -> dict[str, object]:
    binding = bundle["binding"]
    return preflight_research_component_run_manifest(
        manifest=bundle["manifest"],
        component_store={},
        authority_state=authority_state,
        scope_binding_sha256=binding["binding_sha256"],
        scope_binding_store={binding["binding_sha256"]: binding},
        curriculum_records=bundle["curriculum_records"],
        sentinel_fixture_store=bundle["fixture_store"],
        content_scope_verification_store=bundle["verification_store"],
        guard_snapshot_store=snapshot_store,
    )


def test_valid_content_addressed_research_component_binding_passes() -> None:
    bundle = valid_bundle()
    assert validate_bundle(bundle) == []


def test_sentinel_content_change_with_reused_identity_fails() -> None:
    bundle = valid_bundle()
    fixture_sha = bundle["binding"]["sentinel_fixture_sha256s"][0]
    bundle["fixture_store"][fixture_sha]["prompt_text"] = "Changed synthetic content."

    errors = validate_bundle(bundle)

    assert any(
        "sentinel fixture" in error and "failed canonical" in error
        for error in errors
    )


def test_curriculum_content_change_invalidates_prior_scope_verification() -> None:
    bundle = valid_bundle()
    record = bundle["curriculum_records"]["synthetic-research-record-001"]
    record["content_sha256"] = "2" * 64
    record["record_canonical_sha256"] = compute_curriculum_record_sha256(record)

    errors = validate_bundle(bundle)

    assert any(
        "content scope verification failed canonical" in error for error in errors
    )


def test_binding_content_change_with_reused_binding_sha_fails() -> None:
    bundle = valid_bundle()
    bundle["binding"]["gradient_record_bindings"][0][
        "optimization_feedback_allowed"
    ] = False

    errors = validate_bundle(bundle)

    assert any("binding_sha256 mismatch" in error for error in errors)


def test_gradient_record_must_be_learner_researcher_only() -> None:
    bundle = valid_bundle()
    record = bundle["curriculum_records"]["synthetic-research-record-001"]
    record["role_class"] = "PATIENT_CAREGIVER"
    record["record_canonical_sha256"] = compute_curriculum_record_sha256(record)

    errors = validate_bundle(bundle)

    assert any(
        "content scope verification failed canonical" in error for error in errors
    )


def test_excluded_clinical_capability_cannot_be_gradient_target() -> None:
    bundle = valid_bundle()
    bundle["binding"]["gradient_record_bindings"][0]["target_capability_ids"] = [
        "PATIENT_SPECIFIC_DIAGNOSIS"
    ]
    bundle["binding"]["binding_sha256"] = (
        compute_research_component_scope_binding_sha256(bundle["binding"])
    )

    errors = validate_bundle(bundle)

    assert any("outside admitted scope" in error for error in errors)


def test_gradient_capability_vocabulary_is_frozen() -> None:
    bundle = valid_bundle()
    bundle["binding"]["gradient_record_bindings"][0]["target_capability_ids"] = [
        "UNDECLARED_RESEARCH_CAPABILITY"
    ]
    bundle["binding"]["binding_sha256"] = (
        compute_research_component_scope_binding_sha256(bundle["binding"])
    )

    errors = validate_bundle(bundle)

    assert any("outside admitted scope" in error for error in errors)
    assert "UNDECLARED_RESEARCH_CAPABILITY" not in RESEARCH_COMPONENT_ADMITTED_CAPABILITIES


def test_missing_content_addressed_guard_fixture_fails() -> None:
    bundle = valid_bundle()
    fixture_sha = bundle["binding"]["sentinel_fixture_sha256s"][0]
    del bundle["fixture_store"][fixture_sha]

    errors = validate_bundle(bundle)

    assert any("unresolved in authoritative store" in error for error in errors)


def test_excluded_capability_set_cannot_be_narrowed() -> None:
    bundle = valid_bundle()
    bundle["binding"]["excluded_capability_ids"] = sorted(
        RESEARCH_COMPONENT_EXCLUDED_CAPABILITIES
    )[1:]
    bundle["binding"]["binding_sha256"] = (
        compute_research_component_scope_binding_sha256(bundle["binding"])
    )

    errors = validate_bundle(bundle)

    assert any("must equal the canonical frozen set" in error for error in errors)


def test_guard_snapshot_is_content_addressed_and_zero_violation_only() -> None:
    bundle = valid_bundle()
    snapshot = guard_snapshot(bundle)

    assert validate_research_component_guard_snapshot(
        snapshot,
        scope_binding_sha256=bundle["binding"]["binding_sha256"],
        run_manifest_sha256=compute_run_manifest_sha256(bundle["manifest"]),
        sentinel_fixture_store=bundle["fixture_store"],
    ) == []

    tampered = deepcopy(snapshot)
    tampered["fixture_results"][0]["violation_count"] = 1
    errors = validate_research_component_guard_snapshot(
        tampered,
        scope_binding_sha256=bundle["binding"]["binding_sha256"],
        run_manifest_sha256=compute_run_manifest_sha256(bundle["manifest"]),
        sentinel_fixture_store=bundle["fixture_store"],
    )
    assert any("violation_count must equal integer 0" in error for error in errors)
    assert any("snapshot_sha256 mismatch" in error for error in errors)


def test_global_execution_authority_does_not_imply_successor_execution_authority() -> None:
    bundle = valid_bundle()
    snapshot = guard_snapshot(bundle)
    authority_state = successor_authority_state(
        bundle,
        snapshot,
        execution_authority="NONE",
    )

    result = preflight_bundle(
        bundle,
        authority_state,
        {snapshot["snapshot_sha256"]: snapshot},
    )

    assert result["allowed"] is False
    assert "RESEARCH_COMPONENT_EXECUTION_AUTHORITY_NONE" in result["reason_codes"]
    assert result["research_component_scope_validation_errors"] == []


def test_successor_authority_must_bind_exact_scope_binding_hash() -> None:
    bundle = valid_bundle()
    snapshot = guard_snapshot(bundle)
    authority_state = successor_authority_state(bundle, snapshot)
    authority_state["research_component_scope_binding_sha256"] = "f" * 64

    result = preflight_bundle(
        bundle,
        authority_state,
        {snapshot["snapshot_sha256"]: snapshot},
    )

    assert "RESEARCH_COMPONENT_SCOPE_BINDING_STALE_OR_MISMATCH" in result[
        "reason_codes"
    ]


def test_successor_authority_must_bind_exact_run_manifest_hash() -> None:
    bundle = valid_bundle()
    snapshot = guard_snapshot(bundle)
    authority_state = successor_authority_state(bundle, snapshot)
    authority_state["research_component_run_manifest_sha256"] = "e" * 64

    result = preflight_bundle(
        bundle,
        authority_state,
        {snapshot["snapshot_sha256"]: snapshot},
    )

    assert "RESEARCH_COMPONENT_RUN_MANIFEST_STALE_OR_MISMATCH" in result[
        "reason_codes"
    ]


def test_guard_snapshot_pass_cannot_be_self_asserted_without_record() -> None:
    bundle = valid_bundle()
    snapshot = guard_snapshot(bundle)
    authority_state = successor_authority_state(bundle, snapshot)

    result = preflight_bundle(bundle, authority_state, {})

    assert "RESEARCH_COMPONENT_GUARD_SNAPSHOT_NOT_PASS" in result["reason_codes"]
