from copy import deepcopy

from src.commandmed.spec007.research_execution import (
    E002_MODEL_ARTIFACT_ACCESS_AUTHORITY,
    RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
    SUCCESSOR_MODEL_EXECUTION_AUTHORITY,
    SUCCESSOR_TOURNAMENT_EXECUTION_AUTHORITY,
    build_research_component_execution_request,
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


def _candidate_bindings() -> list[dict[str, object]]:
    bindings: list[dict[str, object]] = []
    all_candidates = [
        *(pair + ("PRIMARY", True) for pair in PRIMARY_CANDIDATES),
        CONTROL_CANDIDATE + ("CONTROL", False),
    ]
    for index, (candidate_id, revision, role, winner_eligible) in enumerate(all_candidates):
        marker = format(index + 1, "x")
        bindings.append(
            {
                "candidate_id": candidate_id,
                "upstream_revision": revision,
                "candidate_role": role,
                "winner_eligible": winner_eligible,
                "model_artifact_sha256": marker * 64,
                "model_artifact_bytes": 1000 + index,
                "artifact_format": "SAFETENSORS",
                "artifact_access_state": "PUBLIC_UNGATED_EXACT_IDENTITY",
                "runtime_binding_authority_id": f"SYNTHETIC-RUNTIME-AUTHORITY-{index}",
                "runtime_entrypoint": "python3",
                "runtime_executable_sha256": format(index + 5, "x") * 64,
                "runtime_source_revision": format(index + 9, "x") * 40,
                "runtime_format_compatibility_state": "PASS",
                "tokenizer_config_sha256": format(index + 13, "x") * 64,
                "runtime_argv": ["python3", "synthetic-offline-runner.py"],
            }
        )
    return bindings


def _subject() -> dict[str, object]:
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
        "a15_activation_id": "SYNTHETIC-A15-ACTIVATION",
        "a15_activation_record_sha256": "a" * 64,
        "a15_state": "PASS",
        "resource_binding_id": "SYNTHETIC-RESOURCE-BINDING",
        "resource_binding_sha256": "b" * 64,
        "resource_state": "PASS",
        "access_binding_id": "SYNTHETIC-ACCESS-BINDING",
        "access_binding_sha256": "c" * 64,
        "access_state": "PASS",
        "execution_environment_id": "SYNTHETIC-OFFLINE-ENVIRONMENT",
        "environment_manifest_sha256": "d" * 64,
        "authorized_spend_usd": 0,
        "credentials_used": False,
        "gated_assets_used": False,
        "private_gold_used": False,
        "phi_used": False,
        "winner_selection_performed": False,
    }
    subject["subject_sha256"] = compute_research_component_preexecution_subject_sha256(subject)
    return subject


def _rehash(subject: dict[str, object]) -> dict[str, object]:
    subject["subject_sha256"] = compute_research_component_preexecution_subject_sha256(subject)
    return subject


def test_valid_synthetic_subject_is_ready_without_execution() -> None:
    subject = _subject()
    assert validate_research_component_preexecution_subject(subject) == []
    result = build_research_component_execution_request(subject)
    assert result["state"] == "READY_FOR_EXTERNAL_EXECUTOR"
    assert result["execution_performed"] is False
    assert result["request"] is not None


def test_exact_frozen_candidate_set_is_required() -> None:
    subject = _subject()
    candidate = subject["candidate_runtime_bindings"][0]
    candidate["candidate_id"] = "unauthorized/model"
    _rehash(subject)
    errors = validate_research_component_preexecution_subject(subject)
    assert any("outside frozen E001 set" in error for error in errors)
    assert any("exact frozen E001 candidate set required" in error for error in errors)


def test_protocol_and_asset_set_are_exactly_bound() -> None:
    subject = _subject()
    subject["protocol_sha256"] = "f" * 64
    subject["evaluation_asset_set_sha256"] = "e" * 64
    _rehash(subject)
    errors = validate_research_component_preexecution_subject(subject)
    assert "ResearchComponentPreExecutionSubject: protocol_sha256 mismatch" in errors
    assert (
        "ResearchComponentPreExecutionSubject: evaluation_asset_set_sha256 mismatch"
        in errors
    )


def test_a15_resource_and_access_are_noncompensable() -> None:
    subject = _subject()
    subject["a15_state"] = "ABSENT"
    subject["resource_state"] = "BLOCKED"
    subject["access_state"] = "INCOMPLETE"
    _rehash(subject)
    errors = validate_research_component_preexecution_subject(subject)
    assert "ResearchComponentPreExecutionSubject: a15_state must equal PASS" in errors
    assert "ResearchComponentPreExecutionSubject: resource_state must equal PASS" in errors
    assert "ResearchComponentPreExecutionSubject: access_state must equal PASS" in errors


def test_zero_spend_and_protected_access_boundary_is_fail_closed() -> None:
    subject = _subject()
    subject["authorized_spend_usd"] = 1
    subject["credentials_used"] = True
    subject["gated_assets_used"] = True
    subject["private_gold_used"] = True
    subject["phi_used"] = True
    subject["winner_selection_performed"] = True
    _rehash(subject)
    errors = validate_research_component_preexecution_subject(subject)
    for field in (
        "credentials_used",
        "gated_assets_used",
        "private_gold_used",
        "phi_used",
        "winner_selection_performed",
    ):
        assert f"ResearchComponentPreExecutionSubject: {field} must be false" in errors
    assert "ResearchComponentPreExecutionSubject: authorized_spend_usd must equal 0" in errors


def test_runtime_identity_and_format_compatibility_are_required() -> None:
    subject = _subject()
    candidate = subject["candidate_runtime_bindings"][1]
    candidate["runtime_executable_sha256"] = "NEEDS_EVIDENCE"
    candidate["runtime_source_revision"] = "main"
    candidate["runtime_format_compatibility_state"] = "NEEDS_EVIDENCE"
    _rehash(subject)
    errors = validate_research_component_preexecution_subject(subject)
    assert any("runtime_executable_sha256" in error for error in errors)
    assert any("runtime_source_revision" in error for error in errors)
    assert any("runtime_format_compatibility_state" in error for error in errors)


def test_shell_and_credential_bearing_argv_are_prohibited() -> None:
    subject = _subject()
    candidate = subject["candidate_runtime_bindings"][2]
    candidate["runtime_entrypoint"] = "bash"
    candidate["runtime_argv"] = ["bash", "--api-key", "secret"]
    _rehash(subject)
    errors = validate_research_component_preexecution_subject(subject)
    assert any("shell entrypoints are prohibited" in error for error in errors)
    assert any("credential-bearing runtime arguments are prohibited" in error for error in errors)


def test_subject_hash_is_identity_bearing() -> None:
    subject = _subject()
    subject["execution_environment_id"] = "TAMPERED"
    errors = validate_research_component_preexecution_subject(subject)
    assert "ResearchComponentPreExecutionSubject: subject_sha256 mismatch" in errors


def test_blocked_subject_never_builds_an_execution_request() -> None:
    subject = _subject()
    subject["a15_state"] = "ABSENT_NOT_AUTHORIZED"
    _rehash(subject)
    result = build_research_component_execution_request(subject)
    assert result["state"] == "BLOCKED"
    assert result["execution_performed"] is False
    assert result["request"] is None


def test_runtime_binding_authority_cannot_be_empty() -> None:
    subject = _subject()
    candidate = subject["candidate_runtime_bindings"][3]
    candidate["runtime_binding_authority_id"] = ""
    _rehash(subject)
    errors = validate_research_component_preexecution_subject(subject)
    assert any("runtime_binding_authority_id is required" in error for error in errors)


def test_deepcopy_tampering_does_not_mutate_canonical_fixture() -> None:
    original = _subject()
    tampered = deepcopy(original)
    tampered["candidate_runtime_bindings"][0]["artifact_format"] = "UNKNOWN"
    _rehash(tampered)
    assert validate_research_component_preexecution_subject(original) == []
    assert any(
        "artifact_format is not allowed" in error
        for error in validate_research_component_preexecution_subject(tampered)
    )
