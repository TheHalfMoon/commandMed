"""Fail-closed SP007-RO-001 tournament execution evidence contracts.

This module validates metadata only. It never downloads or loads model weights,
executes inference, opens a device, invokes a subprocess, accesses a network,
selects a winner, starts training, or grants authority.
"""

from __future__ import annotations

import re
from typing import Any, Mapping

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.foundation import is_canonical_sha256, validate_closed_object
from src.commandmed.spec007.research_scope import RESEARCH_COMPONENT_SCOPE_ID
from src.commandmed.spec007.research_tournament import (
    CONTROL_CANDIDATE,
    PRIMARY_CANDIDATES,
    RESEARCH_COMPONENT_EXECUTION_AUTHORITY_ID,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
    validate_research_component_tournament_evidence_pack,
    validate_research_component_tournament_protocol,
)

RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256 = (
    "1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8"
)
RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256 = (
    "709d5f73c1599364fc184b959cbdfd199c7ec07307fef8f8091d8eafb10f5454"
)
RESEARCH_COMPONENT_RESOURCE_ASSET_ID = "SP007-RO-001-EVAL-RESOURCE-EFFICIENCY-V1"
RESEARCH_COMPONENT_RESOURCE_ASSET_SHA256 = (
    "a1ddea12b740886643fc396c62553b1ab954404090d16db499a57e933056a200"
)
RESEARCH_COMPONENT_RESOURCE_EVALUATOR_ID = (
    "SP007_RO_001_RESOURCE_MEASUREMENT_EVALUATOR_V1"
)
E002_MODEL_ARTIFACT_ACCESS_AUTHORITY = (
    "AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY"
)
SUCCESSOR_MODEL_EXECUTION_AUTHORITY = (
    "AUTHORIZED_E001_FROZEN_CANDIDATES_ONLY_AFTER_PASS_PREFLIGHT"
)
SUCCESSOR_TOURNAMENT_EXECUTION_AUTHORITY = (
    "AUTHORIZED_SP007_RO_001_FROZEN_NONCLINICAL_PROTOCOL_ONLY_AFTER_PASS_PREFLIGHT"
)

# No exact live pre-execution subject is canonically authorized at this commit.
# A future gate-closing PR must replace this only with the exact canonical SHA-256
# after every applicable preflight prerequisite, including A15, is genuinely PASS.
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256: str | None = None

PRIMARY_PACKAGE_HARD_CAP_BYTES = 700 * 1024 * 1024
_ALLOWED_ARTIFACT_FORMATS = frozenset({"GGUF", "SAFETENSORS"})
_PROHIBITED_ENTRYPOINTS = frozenset(
    {"sh", "bash", "zsh", "fish", "cmd", "cmd.exe", "powershell", "pwsh"}
)
_PROHIBITED_ARGV_MARKERS = (
    "--api-key",
    "--apikey",
    "--token",
    "--password",
    "--credential",
    "hf_token",
)
_GIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
_ENTRYPOINT_RE = re.compile(r"^[A-Za-z0-9._+\-]+$")

_SUBJECT_FIELDS = (
    "schema_version",
    "subject_id",
    "subject_sha256",
    "scope_id",
    "protocol_id",
    "protocol_sha256",
    "evaluation_asset_set_sha256",
    "execution_authority_id",
    "model_artifact_access_authority",
    "model_execution_authority",
    "tournament_execution_authority",
    "candidate_runtime_bindings",
    "a1_a14_applicable_snapshot_id",
    "a1_a14_applicable_snapshot_sha256",
    "a1_a14_applicable_state",
    "a15_activation_id",
    "a15_activation_record_sha256",
    "a15_authorization_decision_id",
    "a15_state",
    "resource_binding_id",
    "resource_binding_sha256",
    "resource_state",
    "access_binding_id",
    "access_binding_sha256",
    "access_state",
    "execution_environment_id",
    "environment_manifest_sha256",
    "network_during_execution",
    "authorized_spend_usd",
    "credentials_used",
    "gated_assets_used",
    "private_gold_used",
    "phi_used",
    "winner_selection_performed",
)
_CANDIDATE_FIELDS = (
    "candidate_id",
    "upstream_revision",
    "candidate_role",
    "winner_eligible",
    "model_artifact_sha256",
    "model_artifact_bytes",
    "complete_bundle_sha256",
    "complete_bundle_bytes",
    "artifact_format",
    "artifact_access_state",
    "runtime_binding_authority_id",
    "runtime_artifact_sha256",
    "runtime_entrypoint",
    "runtime_executable_sha256",
    "runtime_source_revision",
    "build_toolchain_identity",
    "runtime_format_compatibility_state",
    "tokenizer_config_sha256",
    "execution_plan_sha256",
    "runtime_argv",
)
_RESOURCE_RESULT_FIELDS = (
    "schema_version",
    "resource_result_id",
    "resource_result_sha256",
    "execution_subject_sha256",
    "candidate_id",
    "upstream_revision",
    "resource_asset_id",
    "resource_asset_sha256",
    "execution_environment_id",
    "probe_results",
    "disposition",
)
_RESOURCE_PROBE_RESULT_FIELDS = (
    "probe_id",
    "warmup_runs_completed",
    "measured_runs",
)
_RESOURCE_MEASUREMENT_FIELDS = (
    "run_index",
    "model_artifact_bytes",
    "peak_rss_bytes",
    "time_to_first_token_ms",
    "decode_tokens_per_second",
    "wall_clock_ms",
)


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and "\x00" not in value


def _self_hash(record: Mapping[str, Any], identity_field: str) -> str:
    projection = dict(record)
    projection.pop(identity_field, None)
    return compute_canonical_sha256(projection)


def compute_research_component_preexecution_subject_sha256(
    subject: Mapping[str, Any],
) -> str:
    """Compute the canonical identity of one pre-execution subject."""
    return _self_hash(subject, "subject_sha256")


def compute_research_component_resource_result_sha256(
    result: Mapping[str, Any],
) -> str:
    """Compute the canonical identity of one resource measurement result."""
    return _self_hash(result, "resource_result_sha256")


def _validate_runtime_argv(binding: Mapping[str, Any], prefix: str) -> list[str]:
    errors: list[str] = []
    entrypoint = binding.get("runtime_entrypoint")
    argv = binding.get("runtime_argv")
    if not _nonempty(entrypoint) or _ENTRYPOINT_RE.fullmatch(str(entrypoint)) is None:
        errors.append(f"{prefix}: runtime_entrypoint must be a simple executable identity")
        return errors
    if str(entrypoint).casefold() in _PROHIBITED_ENTRYPOINTS:
        errors.append(f"{prefix}: shell entrypoints are prohibited")
    if not isinstance(argv, list) or not argv or any(not _nonempty(token) for token in argv):
        errors.append(f"{prefix}: runtime_argv must be a non-empty string list")
        return errors
    if argv[0] != entrypoint:
        errors.append(f"{prefix}: runtime_argv entrypoint mismatch")
    lowered = [str(token).casefold() for token in argv]
    if any(marker in token for token in lowered for marker in _PROHIBITED_ARGV_MARKERS):
        errors.append(f"{prefix}: credential-bearing runtime arguments are prohibited")
    if any("\n" in str(token) or "\r" in str(token) for token in argv):
        errors.append(f"{prefix}: runtime_argv control separators are prohibited")
    return errors


def _validate_candidate_runtime_bindings(value: Any) -> list[str]:
    prefix = "ResearchComponentPreExecutionSubject.candidate_runtime_bindings"
    if not isinstance(value, list) or len(value) != 4:
        return [f"{prefix}: exactly four frozen candidate bindings are required"]

    expected: dict[tuple[str, str], tuple[str, bool]] = {
        pair: ("PRIMARY", True) for pair in PRIMARY_CANDIDATES
    }
    expected[CONTROL_CANDIDATE] = ("CONTROL", False)
    seen: set[tuple[str, str]] = set()
    errors: list[str] = []

    for index, binding in enumerate(value):
        item_prefix = f"{prefix}[{index}]"
        item_errors = validate_closed_object(
            binding, required_fields=_CANDIDATE_FIELDS, field=item_prefix
        )
        errors.extend(item_errors)
        if item_errors or not isinstance(binding, dict):
            continue

        pair = (binding.get("candidate_id"), binding.get("upstream_revision"))
        expected_role = expected.get(pair)
        if expected_role is None:
            errors.append(f"{item_prefix}: candidate identity is outside frozen E001 set")
            continue
        if pair in seen:
            errors.append(f"{item_prefix}: duplicate candidate identity")
        seen.add(pair)

        role, winner_eligible = expected_role
        if binding.get("candidate_role") != role:
            errors.append(f"{item_prefix}: candidate_role mismatch")
        if binding.get("winner_eligible") is not winner_eligible:
            errors.append(f"{item_prefix}: winner_eligible mismatch")

        for field in (
            "model_artifact_sha256",
            "complete_bundle_sha256",
            "runtime_artifact_sha256",
            "runtime_executable_sha256",
            "tokenizer_config_sha256",
            "execution_plan_sha256",
        ):
            if not is_canonical_sha256(binding.get(field)):
                errors.append(f"{item_prefix}: {field} must be lowercase sha256 hex")
        for field in ("model_artifact_bytes", "complete_bundle_bytes"):
            if not isinstance(binding.get(field), int) or binding.get(field) <= 0:
                errors.append(f"{item_prefix}: {field} must be a positive integer")
        if (
            isinstance(binding.get("model_artifact_bytes"), int)
            and isinstance(binding.get("complete_bundle_bytes"), int)
            and binding["complete_bundle_bytes"] < binding["model_artifact_bytes"]
        ):
            errors.append(f"{item_prefix}: complete_bundle_bytes cannot be smaller than model_artifact_bytes")
        if role == "PRIMARY" and isinstance(binding.get("complete_bundle_bytes"), int):
            if binding["complete_bundle_bytes"] > PRIMARY_PACKAGE_HARD_CAP_BYTES:
                errors.append(f"{item_prefix}: primary complete bundle exceeds frozen 700 MiB hard cap")

        if binding.get("artifact_format") not in _ALLOWED_ARTIFACT_FORMATS:
            errors.append(f"{item_prefix}: artifact_format is not allowed")
        if binding.get("artifact_access_state") != "PUBLIC_UNGATED_EXACT_IDENTITY":
            errors.append(f"{item_prefix}: artifact_access_state must be exact public ungated")
        for field in ("runtime_binding_authority_id", "build_toolchain_identity"):
            if not _nonempty(binding.get(field)):
                errors.append(f"{item_prefix}: {field} is required")
        revision = binding.get("runtime_source_revision")
        if not isinstance(revision, str) or _GIT_SHA_RE.fullmatch(revision) is None:
            errors.append(f"{item_prefix}: runtime_source_revision must be an exact git sha")
        if binding.get("runtime_format_compatibility_state") != "PASS":
            errors.append(f"{item_prefix}: runtime_format_compatibility_state must equal PASS")
        errors.extend(_validate_runtime_argv(binding, item_prefix))

    if seen != set(expected):
        errors.append(f"{prefix}: exact frozen E001 candidate set required")
    return errors


def validate_research_component_preexecution_subject(subject: Any) -> list[str]:
    """Validate one exact SP007-RO-001 tournament subject structurally."""
    prefix = "ResearchComponentPreExecutionSubject"
    errors = validate_closed_object(subject, required_fields=_SUBJECT_FIELDS, field=prefix)
    if errors or not isinstance(subject, dict):
        return errors

    if subject.get("schema_version") != "1":
        errors.append(f"{prefix}: schema_version must equal '1'")
    if not _nonempty(subject.get("subject_id")):
        errors.append(f"{prefix}: subject_id must be non-empty")
    if subject.get("scope_id") != RESEARCH_COMPONENT_SCOPE_ID:
        errors.append(f"{prefix}: scope_id mismatch")
    if subject.get("protocol_id") != RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID:
        errors.append(f"{prefix}: protocol_id mismatch")
    if subject.get("protocol_sha256") != RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256:
        errors.append(f"{prefix}: protocol_sha256 mismatch")
    if subject.get("evaluation_asset_set_sha256") != RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256:
        errors.append(f"{prefix}: evaluation_asset_set_sha256 mismatch")
    if subject.get("execution_authority_id") != RESEARCH_COMPONENT_EXECUTION_AUTHORITY_ID:
        errors.append(f"{prefix}: execution_authority_id mismatch")
    if subject.get("model_artifact_access_authority") != E002_MODEL_ARTIFACT_ACCESS_AUTHORITY:
        errors.append(f"{prefix}: model_artifact_access_authority mismatch")
    if subject.get("model_execution_authority") != SUCCESSOR_MODEL_EXECUTION_AUTHORITY:
        errors.append(f"{prefix}: model_execution_authority mismatch")
    if subject.get("tournament_execution_authority") != SUCCESSOR_TOURNAMENT_EXECUTION_AUTHORITY:
        errors.append(f"{prefix}: tournament_execution_authority mismatch")

    errors.extend(_validate_candidate_runtime_bindings(subject.get("candidate_runtime_bindings")))

    for field in (
        "a1_a14_applicable_snapshot_id",
        "a15_activation_id",
        "a15_authorization_decision_id",
        "resource_binding_id",
        "access_binding_id",
        "execution_environment_id",
    ):
        if not _nonempty(subject.get(field)):
            errors.append(f"{prefix}: {field} must be non-empty")
    for field in (
        "a1_a14_applicable_snapshot_sha256",
        "a15_activation_record_sha256",
        "resource_binding_sha256",
        "access_binding_sha256",
        "environment_manifest_sha256",
    ):
        if not is_canonical_sha256(subject.get(field)):
            errors.append(f"{prefix}: {field} must be lowercase sha256 hex")

    if subject.get("a1_a14_applicable_state") != "PASS":
        errors.append(f"{prefix}: a1_a14_applicable_state must equal PASS")
    if subject.get("a15_state") != "AUTHORIZED_TO_CONSTRUCT":
        errors.append(f"{prefix}: a15_state must equal AUTHORIZED_TO_CONSTRUCT")
    if subject.get("resource_state") != "PASS":
        errors.append(f"{prefix}: resource_state must equal PASS")
    if subject.get("access_state") != "PASS":
        errors.append(f"{prefix}: access_state must equal PASS")
    if subject.get("network_during_execution") is not False:
        errors.append(f"{prefix}: network_during_execution must be false")
    if subject.get("authorized_spend_usd") != 0:
        errors.append(f"{prefix}: authorized_spend_usd must equal 0")
    for field in (
        "credentials_used",
        "gated_assets_used",
        "private_gold_used",
        "phi_used",
        "winner_selection_performed",
    ):
        if subject.get(field) is not False:
            errors.append(f"{prefix}: {field} must be false")

    claimed = subject.get("subject_sha256")
    if not is_canonical_sha256(claimed):
        errors.append(f"{prefix}: subject_sha256 must be lowercase sha256 hex")
    elif claimed != compute_research_component_preexecution_subject_sha256(subject):
        errors.append(f"{prefix}: subject_sha256 mismatch")
    return sorted(set(errors))


def _positive_number(value: Any) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0


def validate_research_component_resource_result(
    result: Any,
    *,
    subject: Mapping[str, Any],
) -> list[str]:
    """Validate one candidate's frozen SP007 resource-probe result record."""
    prefix = "ResearchComponentResourceResult"
    errors = validate_closed_object(result, required_fields=_RESOURCE_RESULT_FIELDS, field=prefix)
    if errors or not isinstance(result, dict):
        return errors
    if validate_research_component_preexecution_subject(subject):
        errors.append(f"{prefix}: bound pre-execution subject is invalid")
        return sorted(set(errors))

    if result.get("schema_version") != "1":
        errors.append(f"{prefix}: schema_version must equal '1'")
    if not _nonempty(result.get("resource_result_id")):
        errors.append(f"{prefix}: resource_result_id must be non-empty")
    if result.get("execution_subject_sha256") != subject.get("subject_sha256"):
        errors.append(f"{prefix}: execution_subject_sha256 mismatch")
    if result.get("resource_asset_id") != RESEARCH_COMPONENT_RESOURCE_ASSET_ID:
        errors.append(f"{prefix}: resource_asset_id mismatch")
    if result.get("resource_asset_sha256") != RESEARCH_COMPONENT_RESOURCE_ASSET_SHA256:
        errors.append(f"{prefix}: resource_asset_sha256 mismatch")
    if result.get("execution_environment_id") != subject.get("execution_environment_id"):
        errors.append(f"{prefix}: execution_environment_id mismatch")
    if result.get("disposition") != "RECORDED":
        errors.append(f"{prefix}: disposition must equal RECORDED")

    candidate_bindings = {
        (item.get("candidate_id"), item.get("upstream_revision")): item
        for item in subject.get("candidate_runtime_bindings", [])
        if isinstance(item, dict)
    }
    pair = (result.get("candidate_id"), result.get("upstream_revision"))
    candidate = candidate_bindings.get(pair)
    if candidate is None:
        errors.append(f"{prefix}: candidate identity is outside bound pre-execution subject")

    probe_results = result.get("probe_results")
    if not isinstance(probe_results, list) or len(probe_results) != 8:
        errors.append(f"{prefix}: probe_results must contain exactly eight frozen probes")
    else:
        seen_probe_ids: set[str] = set()
        for probe_index, probe_result in enumerate(probe_results, start=1):
            item_prefix = f"{prefix}.probe_results[{probe_index - 1}]"
            item_errors = validate_closed_object(
                probe_result, required_fields=_RESOURCE_PROBE_RESULT_FIELDS, field=item_prefix
            )
            errors.extend(item_errors)
            if item_errors or not isinstance(probe_result, dict):
                continue
            expected_probe_id = f"{RESEARCH_COMPONENT_RESOURCE_ASSET_ID}-PROBE-{probe_index:02d}"
            if probe_result.get("probe_id") != expected_probe_id:
                errors.append(f"{item_prefix}: probe_id mismatch")
            elif expected_probe_id in seen_probe_ids:
                errors.append(f"{item_prefix}: duplicate probe_id")
            else:
                seen_probe_ids.add(expected_probe_id)
            if probe_result.get("warmup_runs_completed") != 1:
                errors.append(f"{item_prefix}: warmup_runs_completed must equal 1")

            measurements = probe_result.get("measured_runs")
            if not isinstance(measurements, list) or len(measurements) != 3:
                errors.append(f"{item_prefix}: measured_runs must contain exactly three records")
                continue
            for run_index, measurement in enumerate(measurements, start=1):
                run_prefix = f"{item_prefix}.measured_runs[{run_index - 1}]"
                run_errors = validate_closed_object(
                    measurement, required_fields=_RESOURCE_MEASUREMENT_FIELDS, field=run_prefix
                )
                errors.extend(run_errors)
                if run_errors or not isinstance(measurement, dict):
                    continue
                if measurement.get("run_index") != run_index:
                    errors.append(f"{run_prefix}: run_index mismatch")
                for field in (
                    "model_artifact_bytes",
                    "peak_rss_bytes",
                    "time_to_first_token_ms",
                    "decode_tokens_per_second",
                    "wall_clock_ms",
                ):
                    if not _positive_number(measurement.get(field)):
                        errors.append(f"{run_prefix}: {field} must be a positive number")
                if candidate is not None and measurement.get("model_artifact_bytes") != candidate.get(
                    "model_artifact_bytes"
                ):
                    errors.append(f"{run_prefix}: model_artifact_bytes mismatch with execution subject")

    claimed = result.get("resource_result_sha256")
    if not is_canonical_sha256(claimed):
        errors.append(f"{prefix}: resource_result_sha256 must be lowercase sha256 hex")
    elif claimed != compute_research_component_resource_result_sha256(result):
        errors.append(f"{prefix}: resource_result_sha256 mismatch")
    return sorted(set(errors))


def validate_research_component_execution_evidence_bundle(
    *,
    subject: Any,
    protocol: Any,
    evidence_pack: Any,
    resource_results: Any,
) -> list[str]:
    """Compose subject, exact protocol, tournament pack, and resource records."""
    prefix = "ResearchComponentExecutionEvidenceBundle"
    errors = validate_research_component_preexecution_subject(subject)
    protocol_errors = validate_research_component_tournament_protocol(protocol)
    pack_errors = validate_research_component_tournament_evidence_pack(evidence_pack, protocol)
    errors.extend(f"{prefix}: protocol: {error}" for error in protocol_errors)
    errors.extend(f"{prefix}: evidence_pack: {error}" for error in pack_errors)
    if errors or not isinstance(subject, dict) or not isinstance(protocol, dict) or not isinstance(
        evidence_pack, dict
    ):
        return sorted(set(errors))

    if protocol.get("protocol_id") != subject.get("protocol_id"):
        errors.append(f"{prefix}: protocol_id mismatch with execution subject")
    if protocol.get("protocol_sha256") != subject.get("protocol_sha256"):
        errors.append(f"{prefix}: protocol_sha256 mismatch with execution subject")

    resource_asset = next(
        (
            asset
            for asset in protocol.get("evaluation_asset_manifests", [])
            if isinstance(asset, dict) and asset.get("metric_family") == "RESOURCE_EFFICIENCY"
        ),
        None,
    )
    if not isinstance(resource_asset, dict):
        errors.append(f"{prefix}: frozen resource asset manifest missing")
    else:
        if resource_asset.get("asset_id") != RESEARCH_COMPONENT_RESOURCE_ASSET_ID:
            errors.append(f"{prefix}: resource asset_id mismatch with canonical frozen asset")
        if resource_asset.get("content_sha256") != RESEARCH_COMPONENT_RESOURCE_ASSET_SHA256:
            errors.append(f"{prefix}: resource asset sha256 mismatch with canonical frozen asset")

    if evidence_pack.get("execution_environment_id") != subject.get("execution_environment_id"):
        errors.append(f"{prefix}: execution environment mismatch")
    if evidence_pack.get("execution_authority_id") != subject.get("execution_authority_id"):
        errors.append(f"{prefix}: execution authority mismatch")

    if not isinstance(resource_results, Mapping):
        errors.append(f"{prefix}: resource_results must be an ID-keyed mapping")
        return sorted(set(errors))

    candidate_results = evidence_pack.get("candidate_results") or []
    expected_resource_ids: set[str] = set()
    for candidate_result in candidate_results:
        if not isinstance(candidate_result, dict):
            continue
        resource_ids = candidate_result.get("resource_result_ids")
        if not isinstance(resource_ids, list) or len(resource_ids) != 1:
            errors.append(f"{prefix}: each candidate must bind exactly one resource result")
            continue
        resource_id = resource_ids[0]
        expected_resource_ids.add(resource_id)
        resource_result = resource_results.get(resource_id)
        if not isinstance(resource_result, dict):
            errors.append(f"{prefix}: resource result {resource_id} is missing")
            continue
        errors.extend(
            f"{prefix}: {error}"
            for error in validate_research_component_resource_result(resource_result, subject=subject)
        )
        if resource_result.get("candidate_id") != candidate_result.get("candidate_id") or resource_result.get(
            "upstream_revision"
        ) != candidate_result.get("upstream_revision"):
            errors.append(f"{prefix}: resource result candidate mismatch")

        resource_metric = next(
            (
                item
                for item in candidate_result.get("metric_results", [])
                if isinstance(item, dict) and item.get("metric_family") == "RESOURCE_EFFICIENCY"
            ),
            None,
        )
        if not isinstance(resource_metric, dict):
            errors.append(f"{prefix}: RESOURCE_EFFICIENCY metric result missing")
        else:
            if resource_metric.get("value_identity") != resource_result.get("resource_result_sha256"):
                errors.append(f"{prefix}: RESOURCE_EFFICIENCY value_identity must equal resource result sha256")
            if resource_metric.get("deterministic_evaluator_id") != RESEARCH_COMPONENT_RESOURCE_EVALUATOR_ID:
                errors.append(f"{prefix}: RESOURCE_EFFICIENCY deterministic_evaluator_id mismatch")

    if set(resource_results) != expected_resource_ids:
        errors.append(f"{prefix}: resource result store must exactly match evidence-pack references")
    return sorted(set(errors))


def build_research_component_execution_request(subject: Any) -> dict[str, object]:
    """Build a request only for the exact currently authorized canonical subject.

    Structural completeness is necessary but insufficient. At the current
    canonical state no exact pre-execution subject is authorized, so a synthetic
    or caller-asserted PASS cannot become executable.
    """
    errors = validate_research_component_preexecution_subject(subject)
    if errors:
        return {
            "state": "BLOCKED",
            "reason_codes": errors,
            "execution_performed": False,
            "request": None,
        }

    assert isinstance(subject, dict)
    if CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256 is None:
        return {
            "state": "BLOCKED",
            "reason_codes": ["CURRENT_CANONICAL_PREEXECUTION_SUBJECT_NOT_AUTHORIZED"],
            "execution_performed": False,
            "request": None,
        }
    if subject.get("subject_sha256") != CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256:
        return {
            "state": "BLOCKED",
            "reason_codes": ["PREEXECUTION_SUBJECT_SHA256_NOT_CURRENTLY_AUTHORIZED"],
            "execution_performed": False,
            "request": None,
        }

    request = {
        "request_schema": "commandmed-sp007-ro-001-execution-request-v1",
        "subject": dict(subject),
    }
    return {
        "state": "READY_FOR_EXTERNAL_EXECUTOR",
        "reason_codes": [],
        "execution_performed": False,
        "request_canonical_sha256": compute_canonical_sha256(request),
        "request": request,
    }
