from copy import deepcopy

from src.commandmed.spec007.e004_applicable_prerequisite_snapshot import (
    APPLICABLE_PREREQUISITE_GATE_IDS,
    CANONICAL_CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256,
    build_research_component_execution_request_with_prerequisites,
    compute_applicable_prerequisite_gate_set_sha256,
    compute_research_component_applicable_prerequisite_snapshot_sha256,
    validate_research_component_applicable_prerequisite_binding,
    validate_research_component_applicable_prerequisite_snapshot,
)
from src.commandmed.spec007.research_execution import (
    E002_MODEL_ARTIFACT_ACCESS_AUTHORITY,
    RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
    SUCCESSOR_MODEL_EXECUTION_AUTHORITY,
    SUCCESSOR_TOURNAMENT_EXECUTION_AUTHORITY,
    compute_research_component_preexecution_subject_sha256,
    validate_research_component_preexecution_subject,
)
from src.commandmed.spec007.research_scope import RESEARCH_COMPONENT_SCOPE_ID
from src.commandmed.spec007.research_tournament import (
    CONTROL_CANDIDATE,
    PRIMARY_CANDIDATES,
    RESEARCH_COMPONENT_EXECUTION_AUTHORITY_ID,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
)


def _snapshot() -> dict[str, object]:
    gate_records = [
        {
            "gate_id": gate_id,
            "evidence_id": f"SYNTHETIC-EVIDENCE-{index:02d}",
            "evidence_sha256": f"{index + 1:064x}",
            "evidence_repository_commit": f"{index + 1:040x}",
            "disposition": "PASS",
        }
        for index, gate_id in enumerate(APPLICABLE_PREREQUISITE_GATE_IDS)
    ]
    snapshot: dict[str, object] = {
        "schema_version": "1",
        "snapshot_id": "SP007-RO-001-SYNTHETIC-APPLICABLE-PREREQUISITES",
        "snapshot_sha256": "0" * 64,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "protocol_id": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
        "protocol_sha256": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
        "evaluation_asset_set_sha256": RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
        "candidate_artifact_bundle_set_sha256": (
            CANONICAL_CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256
        ),
        "gate_set_sha256": compute_applicable_prerequisite_gate_set_sha256(),
        "gate_records": gate_records,
        "disposition": "PASS",
    }
    snapshot["snapshot_sha256"] = (
        compute_research_component_applicable_prerequisite_snapshot_sha256(snapshot)
    )
    return snapshot


def _candidate_bindings() -> list[dict[str, object]]:
    bindings: list[dict[str, object]] = []
    candidates = [
        *(pair + ("PRIMARY", True) for pair in PRIMARY_CANDIDATES),
        CONTROL_CANDIDATE + ("CONTROL", False),
    ]
    artifact_markers = "1234"
    bundle_markers = "5678"
    runtime_artifact_markers = "9abc"
    runtime_executable_markers = "def0"
    revision_markers = "1234"
    tokenizer_markers = "5678"
    execution_plan_markers = "9abc"
    for index, (candidate_id, revision, role, winner_eligible) in enumerate(candidates):
        bindings.append(
            {
                "candidate_id": candidate_id,
                "upstream_revision": revision,
                "candidate_role": role,
                "winner_eligible": winner_eligible,
                "model_artifact_sha256": artifact_markers[index] * 64,
                "model_artifact_bytes": 1000 + index,
                "complete_bundle_sha256": bundle_markers[index] * 64,
                "complete_bundle_bytes": 2000 + index,
                "artifact_format": "SAFETENSORS",
                "artifact_access_state": "PUBLIC_UNGATED_EXACT_IDENTITY",
                "runtime_binding_authority_id": f"SYNTHETIC-RUNTIME-AUTHORITY-{index}",
                "runtime_artifact_sha256": runtime_artifact_markers[index] * 64,
                "runtime_entrypoint": "python3",
                "runtime_executable_sha256": runtime_executable_markers[index] * 64,
                "runtime_source_revision": revision_markers[index] * 40,
                "build_toolchain_identity": f"SYNTHETIC-BUILD-TOOLCHAIN-{index}",
                "runtime_format_compatibility_state": "PASS",
                "tokenizer_config_sha256": tokenizer_markers[index] * 64,
                "execution_plan_sha256": execution_plan_markers[index] * 64,
                "runtime_argv": ["python3", "synthetic-offline-runner.py"],
            }
        )
    return bindings


def _subject(snapshot: dict[str, object]) -> dict[str, object]:
    subject: dict[str, object] = {
        "schema_version": "1",
        "subject_id": "SP007-RO-001-SYNTHETIC-PREEXECUTION-SUBJECT",
        "subject_sha256": "0" * 64,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "protocol_id": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
        "protocol_sha256": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
        "evaluation_asset_set_sha256": RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
        "execution_authority_id": RESEARCH_COMPONENT_EXECUTION_AUTHORITY_ID,
        "model_artifact_access_authority": E002_MODEL_ARTIFACT_ACCESS_AUTHORITY,
        "model_execution_authority": SUCCESSOR_MODEL_EXECUTION_AUTHORITY,
        "tournament_execution_authority": SUCCESSOR_TOURNAMENT_EXECUTION_AUTHORITY,
        "candidate_runtime_bindings": _candidate_bindings(),
        "a1_a14_applicable_snapshot_id": snapshot["snapshot_id"],
        "a1_a14_applicable_snapshot_sha256": snapshot["snapshot_sha256"],
        "a1_a14_applicable_state": "PASS",
        "a15_activation_id": "SYNTHETIC-A15-ACTIVATION",
        "a15_activation_record_sha256": "b" * 64,
        "a15_authorization_decision_id": "SYNTHETIC-A15-FOUNDER-DECISION",
        "a15_state": "AUTHORIZED_TO_CONSTRUCT",
        "resource_binding_id": "SYNTHETIC-RESOURCE-BINDING",
        "resource_binding_sha256": "c" * 64,
        "resource_state": "PASS",
        "access_binding_id": "SYNTHETIC-ACCESS-BINDING",
        "access_binding_sha256": "d" * 64,
        "access_state": "PASS",
        "execution_environment_id": "SYNTHETIC-OFFLINE-ENVIRONMENT",
        "environment_manifest_sha256": "e" * 64,
        "network_during_execution": False,
        "authorized_spend_usd": 0,
        "credentials_used": False,
        "gated_assets_used": False,
        "private_gold_used": False,
        "phi_used": False,
        "winner_selection_performed": False,
    }
    subject["subject_sha256"] = compute_research_component_preexecution_subject_sha256(subject)
    return subject


def _rehash_snapshot(snapshot: dict[str, object]) -> dict[str, object]:
    snapshot["snapshot_sha256"] = (
        compute_research_component_applicable_prerequisite_snapshot_sha256(snapshot)
    )
    return snapshot


def _rehash_subject(subject: dict[str, object]) -> dict[str, object]:
    subject["subject_sha256"] = compute_research_component_preexecution_subject_sha256(subject)
    return subject


def test_exact_applicable_prerequisite_snapshot_validates() -> None:
    snapshot = _snapshot()
    assert validate_research_component_applicable_prerequisite_snapshot(snapshot) == []
    assert len(snapshot["gate_records"]) == 14


def test_missing_applicable_gate_fails_closed() -> None:
    snapshot = _snapshot()
    snapshot["gate_records"] = snapshot["gate_records"][:-1]
    _rehash_snapshot(snapshot)
    errors = validate_research_component_applicable_prerequisite_snapshot(snapshot)
    assert any("exactly 14 applicable gate records" in error for error in errors)


def test_duplicate_or_nonpass_gate_fails_closed() -> None:
    snapshot = _snapshot()
    records = snapshot["gate_records"]
    records[1]["gate_id"] = records[0]["gate_id"]
    records[2]["disposition"] = "INCOMPLETE"
    _rehash_snapshot(snapshot)
    errors = validate_research_component_applicable_prerequisite_snapshot(snapshot)
    assert any("duplicate gate_id" in error for error in errors)
    assert any("disposition must equal PASS" in error for error in errors)
    assert any("exact canonical applicable set" in error for error in errors)


def test_gate_evidence_identity_and_repository_commit_are_required() -> None:
    snapshot = _snapshot()
    record = snapshot["gate_records"][0]
    record["evidence_sha256"] = "NEEDS_EVIDENCE"
    record["evidence_repository_commit"] = "main"
    _rehash_snapshot(snapshot)
    errors = validate_research_component_applicable_prerequisite_snapshot(snapshot)
    assert any("evidence_sha256 must be lowercase sha256 hex" in error for error in errors)
    assert any("evidence_repository_commit must be an exact git sha" in error for error in errors)


def test_snapshot_self_hash_is_identity_bearing() -> None:
    snapshot = _snapshot()
    snapshot["gate_records"][0]["evidence_id"] = "TAMPERED"
    errors = validate_research_component_applicable_prerequisite_snapshot(snapshot)
    assert any("snapshot_sha256 mismatch" in error for error in errors)


def test_subject_requires_snapshot_from_authoritative_store() -> None:
    snapshot = _snapshot()
    subject = _subject(snapshot)
    assert validate_research_component_preexecution_subject(subject) == []
    errors = validate_research_component_applicable_prerequisite_binding(
        subject,
        prerequisite_snapshot_store={},
    )
    assert errors == [
        "ResearchComponentApplicablePrerequisiteBinding: applicable prerequisite "
        "snapshot not found in authoritative store"
    ]


def test_exact_subject_snapshot_binding_validates() -> None:
    snapshot = _snapshot()
    subject = _subject(snapshot)
    store = {snapshot["snapshot_sha256"]: snapshot}
    assert (
        validate_research_component_applicable_prerequisite_binding(
            subject,
            prerequisite_snapshot_store=store,
        )
        == []
    )


def test_subject_snapshot_id_mismatch_fails_closed() -> None:
    snapshot = _snapshot()
    subject = _subject(snapshot)
    subject["a1_a14_applicable_snapshot_id"] = "TAMPERED-SNAPSHOT-ID"
    _rehash_subject(subject)
    store = {snapshot["snapshot_sha256"]: snapshot}
    errors = validate_research_component_applicable_prerequisite_binding(
        subject,
        prerequisite_snapshot_store=store,
    )
    assert any("snapshot_id mismatch" in error for error in errors)


def test_valid_snapshot_does_not_create_live_execution_authority() -> None:
    snapshot = _snapshot()
    subject = _subject(snapshot)
    store = {snapshot["snapshot_sha256"]: snapshot}
    result = build_research_component_execution_request_with_prerequisites(
        subject,
        prerequisite_snapshot_store=store,
    )
    assert result["state"] == "BLOCKED"
    assert result["reason_codes"] == ["CURRENT_CANONICAL_PREEXECUTION_SUBJECT_NOT_AUTHORIZED"]
    assert result["execution_performed"] is False
    assert result["request"] is None


def test_deepcopy_tampering_does_not_mutate_valid_snapshot() -> None:
    original = _snapshot()
    tampered = deepcopy(original)
    tampered["candidate_artifact_bundle_set_sha256"] = "f" * 64
    _rehash_snapshot(tampered)
    assert validate_research_component_applicable_prerequisite_snapshot(original) == []
    assert any(
        "candidate_artifact_bundle_set_sha256 mismatch" in error
        for error in validate_research_component_applicable_prerequisite_snapshot(tampered)
    )
