import json
from copy import deepcopy
from pathlib import Path

from src.commandmed.spec007.research_execution import (
    E002_MODEL_ARTIFACT_ACCESS_AUTHORITY,
    PRIMARY_PACKAGE_HARD_CAP_BYTES,
    RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
    RESEARCH_COMPONENT_RESOURCE_ASSET_ID,
    RESEARCH_COMPONENT_RESOURCE_ASSET_SHA256,
    RESEARCH_COMPONENT_RESOURCE_EVALUATOR_ID,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
    SUCCESSOR_MODEL_EXECUTION_AUTHORITY,
    SUCCESSOR_TOURNAMENT_EXECUTION_AUTHORITY,
    build_research_component_execution_request,
    compute_research_component_preexecution_subject_sha256,
    compute_research_component_resource_result_sha256,
    validate_research_component_execution_evidence_bundle,
    validate_research_component_preexecution_subject,
    validate_research_component_resource_result,
)
from src.commandmed.spec007.research_scope import (
    RESEARCH_COMPONENT_REQUIRED_GUARDS,
    RESEARCH_COMPONENT_SCOPE_ID,
)
from src.commandmed.spec007.research_tournament import (
    CANONICAL_GUARD_FIXTURE_SHA256,
    CONTROL_CANDIDATE,
    PRIMARY_CANDIDATES,
    RESEARCH_COMPONENT_EXECUTION_AUTHORITY_ID,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
    compute_research_component_tournament_evidence_pack_sha256,
)

_PROTOCOL_PATH = Path(
    "specs/007-sft-v1/e004-research-component-tournament-protocol-v1.json"
)


def _candidate_bindings() -> list[dict[str, object]]:
    bindings: list[dict[str, object]] = []
    all_candidates = [
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
    for index, (candidate_id, revision, role, winner_eligible) in enumerate(all_candidates):
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
        "a1_a14_applicable_snapshot_id": "SYNTHETIC-A1-A14-SNAPSHOT",
        "a1_a14_applicable_snapshot_sha256": "a" * 64,
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


def _rehash(subject: dict[str, object]) -> dict[str, object]:
    subject["subject_sha256"] = compute_research_component_preexecution_subject_sha256(subject)
    return subject


def _resource_result(subject: dict[str, object], candidate_index: int) -> dict[str, object]:
    candidate = subject["candidate_runtime_bindings"][candidate_index]
    probe_results = []
    for probe_index in range(1, 9):
        measured_runs = [
            {
                "run_index": run_index,
                "model_artifact_bytes": candidate["model_artifact_bytes"],
                "peak_rss_bytes": 10_000 + probe_index + run_index,
                "time_to_first_token_ms": 20.0 + run_index,
                "decode_tokens_per_second": 30.0 + run_index,
                "wall_clock_ms": 40.0 + run_index,
            }
            for run_index in range(1, 4)
        ]
        probe_results.append(
            {
                "probe_id": f"{RESEARCH_COMPONENT_RESOURCE_ASSET_ID}-PROBE-{probe_index:02d}",
                "warmup_runs_completed": 1,
                "measured_runs": measured_runs,
            }
        )
    result: dict[str, object] = {
        "schema_version": "1",
        "resource_result_id": f"RESOURCE-RESULT-{candidate_index}",
        "resource_result_sha256": "0" * 64,
        "execution_subject_sha256": subject["subject_sha256"],
        "candidate_id": candidate["candidate_id"],
        "upstream_revision": candidate["upstream_revision"],
        "resource_asset_id": RESEARCH_COMPONENT_RESOURCE_ASSET_ID,
        "resource_asset_sha256": RESEARCH_COMPONENT_RESOURCE_ASSET_SHA256,
        "execution_environment_id": subject["execution_environment_id"],
        "probe_results": probe_results,
        "disposition": "RECORDED",
    }
    result["resource_result_sha256"] = compute_research_component_resource_result_sha256(result)
    return result


def _canonical_protocol() -> dict[str, object]:
    return json.loads(_PROTOCOL_PATH.read_text(encoding="utf-8"))


def _evidence_pack(
    subject: dict[str, object],
    protocol: dict[str, object],
    resource_results: dict[str, dict[str, object]],
) -> dict[str, object]:
    candidate_results = []
    result_by_pair = {
        (result["candidate_id"], result["upstream_revision"]): result
        for result in resource_results.values()
    }
    for candidate in protocol["candidate_bindings"]:
        pair = (candidate["candidate_id"], candidate["upstream_revision"])
        resource_result = result_by_pair[pair]
        metric_results = []
        for asset in protocol["evaluation_asset_manifests"]:
            if asset["metric_family"] == "RESOURCE_EFFICIENCY":
                value_identity = resource_result["resource_result_sha256"]
                evaluator_id = RESEARCH_COMPONENT_RESOURCE_EVALUATOR_ID
            else:
                value_identity = f"SYNTHETIC-VALUE-{asset['asset_id']}"
                evaluator_id = f"SYNTHETIC-EVALUATOR-{asset['asset_id']}"
            metric_results.append(
                {
                    "metric_family": asset["metric_family"],
                    "asset_id": asset["asset_id"],
                    "value_identity": value_identity,
                    "deterministic_evaluator_id": evaluator_id,
                }
            )
        candidate_results.append(
            {
                "candidate_id": candidate["candidate_id"],
                "upstream_revision": candidate["upstream_revision"],
                "candidate_role": candidate["candidate_role"],
                "metric_results": metric_results,
                "resource_result_ids": [resource_result["resource_result_id"]],
                "qualification_disposition": "PASS",
            }
        )
    evidence: dict[str, object] = {
        "schema_version": "1",
        "evidence_pack_id": "SYNTHETIC-SP007-EVIDENCE-PACK",
        "evidence_pack_sha256": "0" * 64,
        "protocol_id": protocol["protocol_id"],
        "protocol_sha256": protocol["protocol_sha256"],
        "candidate_results": candidate_results,
        "sentinel_guard_results": [
            {
                "guard_id": guard_id,
                "fixture_sha256": CANONICAL_GUARD_FIXTURE_SHA256[guard_id],
                "violation_count": 0,
                "disposition": "PASS",
            }
            for guard_id in sorted(RESEARCH_COMPONENT_REQUIRED_GUARDS)
        ],
        "execution_environment_id": subject["execution_environment_id"],
        "execution_authority_id": RESEARCH_COMPONENT_EXECUTION_AUTHORITY_ID,
        "spend_usd": 0,
        "winner_selected": False,
        "recommendation": "NONE",
    }
    evidence["evidence_pack_sha256"] = compute_research_component_tournament_evidence_pack_sha256(
        evidence
    )
    return evidence


def test_structurally_complete_synthetic_subject_is_not_live_authority() -> None:
    subject = _subject()
    assert validate_research_component_preexecution_subject(subject) == []
    result = build_research_component_execution_request(subject)
    assert result["state"] == "BLOCKED"
    assert result["reason_codes"] == ["CURRENT_CANONICAL_PREEXECUTION_SUBJECT_NOT_AUTHORIZED"]
    assert result["execution_performed"] is False
    assert result["request"] is None


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
    assert "ResearchComponentPreExecutionSubject: evaluation_asset_set_sha256 mismatch" in errors


def test_a1_a14_a15_resource_and_access_are_noncompensable() -> None:
    subject = _subject()
    subject["a1_a14_applicable_state"] = "INCOMPLETE"
    subject["a15_state"] = "ABSENT"
    subject["resource_state"] = "BLOCKED"
    subject["access_state"] = "INCOMPLETE"
    _rehash(subject)
    errors = validate_research_component_preexecution_subject(subject)
    assert "ResearchComponentPreExecutionSubject: a1_a14_applicable_state must equal PASS" in errors
    assert (
        "ResearchComponentPreExecutionSubject: a15_state must equal AUTHORIZED_TO_CONSTRUCT"
        in errors
    )
    assert "ResearchComponentPreExecutionSubject: resource_state must equal PASS" in errors
    assert "ResearchComponentPreExecutionSubject: access_state must equal PASS" in errors


def test_zero_spend_network_and_protected_access_boundary_is_fail_closed() -> None:
    subject = _subject()
    subject["network_during_execution"] = True
    subject["authorized_spend_usd"] = 1
    subject["credentials_used"] = True
    subject["gated_assets_used"] = True
    subject["private_gold_used"] = True
    subject["phi_used"] = True
    subject["winner_selection_performed"] = True
    _rehash(subject)
    errors = validate_research_component_preexecution_subject(subject)
    assert "ResearchComponentPreExecutionSubject: network_during_execution must be false" in errors
    for field in (
        "credentials_used",
        "gated_assets_used",
        "private_gold_used",
        "phi_used",
        "winner_selection_performed",
    ):
        assert f"ResearchComponentPreExecutionSubject: {field} must be false" in errors
    assert "ResearchComponentPreExecutionSubject: authorized_spend_usd must equal 0" in errors


def test_complete_bundle_and_runtime_identity_are_required() -> None:
    subject = _subject()
    candidate = subject["candidate_runtime_bindings"][1]
    candidate["complete_bundle_sha256"] = "NEEDS_EVIDENCE"
    candidate["runtime_artifact_sha256"] = "NEEDS_EVIDENCE"
    candidate["runtime_executable_sha256"] = "NEEDS_EVIDENCE"
    candidate["runtime_source_revision"] = "main"
    candidate["build_toolchain_identity"] = ""
    candidate["execution_plan_sha256"] = "NEEDS_EVIDENCE"
    candidate["runtime_format_compatibility_state"] = "NEEDS_EVIDENCE"
    _rehash(subject)
    errors = validate_research_component_preexecution_subject(subject)
    for field in (
        "complete_bundle_sha256",
        "runtime_artifact_sha256",
        "runtime_executable_sha256",
        "runtime_source_revision",
        "build_toolchain_identity",
        "execution_plan_sha256",
        "runtime_format_compatibility_state",
    ):
        assert any(field in error for error in errors)


def test_primary_complete_bundle_hard_cap_is_noncompensable() -> None:
    subject = _subject()
    candidate = subject["candidate_runtime_bindings"][0]
    candidate["complete_bundle_bytes"] = PRIMARY_PACKAGE_HARD_CAP_BYTES + 1
    _rehash(subject)
    errors = validate_research_component_preexecution_subject(subject)
    assert any("frozen 700 MiB hard cap" in error for error in errors)


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


def test_resource_result_requires_exact_frozen_probe_shape() -> None:
    subject = _subject()
    result = _resource_result(subject, 0)
    assert validate_research_component_resource_result(result, subject=subject) == []
    result["probe_results"][0]["warmup_runs_completed"] = 0
    result["probe_results"][1]["measured_runs"] = result["probe_results"][1]["measured_runs"][:2]
    result["resource_result_sha256"] = compute_research_component_resource_result_sha256(result)
    errors = validate_research_component_resource_result(result, subject=subject)
    assert any("warmup_runs_completed must equal 1" in error for error in errors)
    assert any("exactly three records" in error for error in errors)


def test_resource_result_binds_model_artifact_bytes() -> None:
    subject = _subject()
    result = _resource_result(subject, 0)
    result["probe_results"][0]["measured_runs"][0]["model_artifact_bytes"] += 1
    result["resource_result_sha256"] = compute_research_component_resource_result_sha256(result)
    errors = validate_research_component_resource_result(result, subject=subject)
    assert any("model_artifact_bytes mismatch with execution subject" in error for error in errors)


def test_execution_evidence_bundle_binds_exact_resource_records() -> None:
    subject = _subject()
    protocol = _canonical_protocol()
    results = {
        result["resource_result_id"]: result
        for result in (_resource_result(subject, index) for index in range(4))
    }
    evidence = _evidence_pack(subject, protocol, results)
    assert (
        validate_research_component_execution_evidence_bundle(
            subject=subject,
            protocol=protocol,
            evidence_pack=evidence,
            resource_results=results,
        )
        == []
    )


def test_execution_evidence_bundle_rejects_unbound_resource_identity() -> None:
    subject = _subject()
    protocol = _canonical_protocol()
    results = {
        result["resource_result_id"]: result
        for result in (_resource_result(subject, index) for index in range(4))
    }
    evidence = _evidence_pack(subject, protocol, results)
    first = evidence["candidate_results"][0]
    resource_metric = next(
        item for item in first["metric_results"] if item["metric_family"] == "RESOURCE_EFFICIENCY"
    )
    resource_metric["value_identity"] = "UNBOUND"
    evidence["evidence_pack_sha256"] = compute_research_component_tournament_evidence_pack_sha256(
        evidence
    )
    errors = validate_research_component_execution_evidence_bundle(
        subject=subject,
        protocol=protocol,
        evidence_pack=evidence,
        resource_results=results,
    )
    assert any("value_identity must equal resource result sha256" in error for error in errors)


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
