"""Fail-closed SP007-RO-001 tournament pre-execution envelope.

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
)

RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256 = (
    "1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8"
)
RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256 = (
    "709d5f73c1599364fc184b959cbdfd199c7ec07307fef8f8091d8eafb10f5454"
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
    "a15_activation_id",
    "a15_activation_record_sha256",
    "a15_state",
    "resource_binding_id",
    "resource_binding_sha256",
    "resource_state",
    "access_binding_id",
    "access_binding_sha256",
    "access_state",
    "execution_environment_id",
    "environment_manifest_sha256",
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
    "artifact_format",
    "artifact_access_state",
    "runtime_binding_authority_id",
    "runtime_entrypoint",
    "runtime_executable_sha256",
    "runtime_source_revision",
    "runtime_format_compatibility_state",
    "tokenizer_config_sha256",
    "runtime_argv",
)


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and "\x00" not in value


def _self_hash(subject: Mapping[str, Any]) -> str:
    projection = dict(subject)
    projection.pop("subject_sha256", None)
    return compute_canonical_sha256(projection)


def compute_research_component_preexecution_subject_sha256(
    subject: Mapping[str, Any],
) -> str:
    """Compute the canonical identity of one pre-execution subject."""
    return _self_hash(subject)


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

        if not is_canonical_sha256(binding.get("model_artifact_sha256")):
            errors.append(f"{item_prefix}: model_artifact_sha256 must be lowercase sha256 hex")
        if not isinstance(binding.get("model_artifact_bytes"), int) or binding.get(
            "model_artifact_bytes"
        ) <= 0:
            errors.append(f"{item_prefix}: model_artifact_bytes must be a positive integer")
        if binding.get("artifact_format") not in _ALLOWED_ARTIFACT_FORMATS:
            errors.append(f"{item_prefix}: artifact_format is not allowed")
        if binding.get("artifact_access_state") != "PUBLIC_UNGATED_EXACT_IDENTITY":
            errors.append(f"{item_prefix}: artifact_access_state must be exact public ungated")
        if not _nonempty(binding.get("runtime_binding_authority_id")):
            errors.append(f"{item_prefix}: runtime_binding_authority_id is required")
        if not is_canonical_sha256(binding.get("runtime_executable_sha256")):
            errors.append(f"{item_prefix}: runtime_executable_sha256 must be lowercase sha256 hex")
        revision = binding.get("runtime_source_revision")
        if not isinstance(revision, str) or _GIT_SHA_RE.fullmatch(revision) is None:
            errors.append(f"{item_prefix}: runtime_source_revision must be an exact git sha")
        if binding.get("runtime_format_compatibility_state") != "PASS":
            errors.append(f"{item_prefix}: runtime_format_compatibility_state must equal PASS")
        if not is_canonical_sha256(binding.get("tokenizer_config_sha256")):
            errors.append(f"{item_prefix}: tokenizer_config_sha256 must be lowercase sha256 hex")
        errors.extend(_validate_runtime_argv(binding, item_prefix))

    if seen != set(expected):
        errors.append(f"{prefix}: exact frozen E001 candidate set required")
    return errors


def validate_research_component_preexecution_subject(subject: Any) -> list[str]:
    """Validate one exact SP007-RO-001 tournament subject fail closed."""
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
    if (
        subject.get("evaluation_asset_set_sha256")
        != RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256
    ):
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
        "a15_activation_id",
        "resource_binding_id",
        "access_binding_id",
        "execution_environment_id",
    ):
        if not _nonempty(subject.get(field)):
            errors.append(f"{prefix}: {field} must be non-empty")
    for field in (
        "a15_activation_record_sha256",
        "resource_binding_sha256",
        "access_binding_sha256",
        "environment_manifest_sha256",
    ):
        if not is_canonical_sha256(subject.get(field)):
            errors.append(f"{prefix}: {field} must be lowercase sha256 hex")

    if subject.get("a15_state") != "PASS":
        errors.append(f"{prefix}: a15_state must equal PASS")
    if subject.get("resource_state") != "PASS":
        errors.append(f"{prefix}: resource_state must equal PASS")
    if subject.get("access_state") != "PASS":
        errors.append(f"{prefix}: access_state must equal PASS")
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


def build_research_component_execution_request(subject: Any) -> dict[str, object]:
    """Build a deterministic request for a separately governed external executor.

    This function performs no execution. Any unresolved or mismatched gate returns
    a BLOCKED result and no request.
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
