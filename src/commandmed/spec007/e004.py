"""Identity-bound E004 execution request envelope.

This module validates and canonicalizes a future live-tournament invocation. It
never opens a model, benchmark, device, network connection, shell, or process.
The output is a deterministic request for a separately governed external
executor after all existing E003/A15 gates have already passed.
"""

from __future__ import annotations

import re
from typing import Any

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.foundation import (
    is_canonical_sha256,
    validate_closed_object,
)

PLAN_REQUIRED_FIELDS = frozenset(
    {
        "plan_id",
        "plan_version",
        "candidate_id",
        "candidate_revision",
        "e001_manifest_sha256",
        "e002_authorization_git_blob",
        "e003_authorization_git_blob",
        "model_artifact_access_authority",
        "e003_execution_authority",
        "benchmark_payload_execution_authority",
        "a15_activation_id",
        "a15_activation_record_sha256",
        "preconstruction_snapshot_sha256",
        "spec005_preflight_state",
        "device_execution_readiness_sha256",
        "device_execution_readiness_state",
        "model_artifact_sha256",
        "evaluation_artifact_sha256",
        "evaluation_input_class",
        "evaluation_purpose",
        "lineage_record_sha256",
        "lineage_state",
        "contamination_evidence_sha256",
        "contamination_state",
        "runtime_entrypoint",
        "runtime_executable_sha256",
        "llama_cpp_core_revision",
        "tokenizer_config_sha256",
        "environment_manifest_sha256",
        "argv",
        "expected_raw_output_artifact_id",
        "no_spend_assertion",
        "no_credentials_assertion",
    }
)
SHA256_FIELDS = (
    "e001_manifest_sha256",
    "a15_activation_record_sha256",
    "preconstruction_snapshot_sha256",
    "device_execution_readiness_sha256",
    "model_artifact_sha256",
    "evaluation_artifact_sha256",
    "lineage_record_sha256",
    "contamination_evidence_sha256",
    "runtime_executable_sha256",
    "tokenizer_config_sha256",
    "environment_manifest_sha256",
)
GIT_SHA_FIELDS = (
    "candidate_revision",
    "e002_authorization_git_blob",
    "e003_authorization_git_blob",
    "llama_cpp_core_revision",
)
EXPECTED_STATES = {
    "model_artifact_access_authority": "AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY",
    "e003_execution_authority": "AUTHORIZED_E003_FROZEN_TOURNAMENT_ONLY",
    "benchmark_payload_execution_authority": "AUTHORIZED_E003_A15_BOUND_PUBLIC_TOURNAMENT_INPUTS_ONLY",
    "spec005_preflight_state": "PREFLIGHT_COMPLETE",
    "device_execution_readiness_state": "PRE_EXECUTION_READY",
    "evaluation_input_class": "PUBLIC_UNGATED",
    "evaluation_purpose": "CHECKPOINT_SELECTION",
    "lineage_state": "ELIGIBLE",
    "contamination_state": "ASSESSED_CLEAN",
}
PROHIBITED_CONTENT_MARKERS = (
    "PRIVATE_GOLD",
    "COMMANDMED_CLINICAL_GOLD",
    "COMMANDMED_ARABIC_GOLD",
    "COMMANDMED_MULTIMODAL_GOLD",
    "PHI_PAYLOAD",
    "CREDENTIAL",
    "API_KEY",
    "ACCESS_TOKEN",
    "PASSWORD",
)
PROHIBITED_ARGV_MARKERS = (
    "--api-key",
    "--apikey",
    "--token",
    "--password",
    "--credential",
    "hf_token",
)
PROHIBITED_ENTRYPOINTS = frozenset(
    {"sh", "bash", "zsh", "fish", "cmd", "cmd.exe", "powershell", "pwsh"}
)
_GIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")
_ENTRYPOINT_RE = re.compile(r"^[A-Za-z0-9._+\-]+$")


def _resolved_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and "\x00" not in value


def _contains_prohibited_marker(value: Any) -> bool:
    if isinstance(value, str):
        upper = value.upper()
        return any(marker in upper for marker in PROHIBITED_CONTENT_MARKERS)
    if isinstance(value, dict):
        return any(_contains_prohibited_marker(item) for item in value.values())
    if isinstance(value, list):
        return any(_contains_prohibited_marker(item) for item in value)
    return False


def _validate_argv(plan: dict[str, Any]) -> list[str]:
    errors: list[str] = []
    argv = plan.get("argv")
    if not isinstance(argv, list) or not argv:
        return ["E004:argv_NON_EMPTY_STRING_LIST_REQUIRED"]
    if any(not _resolved_string(token) for token in argv):
        errors.append("E004:argv_NON_EMPTY_STRING_LIST_REQUIRED")
        return errors
    if any("\n" in token or "\r" in token for token in argv):
        errors.append("E004:argv_CONTROL_SEPARATOR_PROHIBITED")

    lowered = [token.casefold() for token in argv]
    if any(
        marker in token
        for token in lowered
        for marker in PROHIBITED_ARGV_MARKERS
    ):
        errors.append("E004:argv_CREDENTIAL_OR_SECRET_FLAG_PROHIBITED")

    entrypoint = plan.get("runtime_entrypoint")
    if not _resolved_string(entrypoint) or not _ENTRYPOINT_RE.fullmatch(entrypoint):
        errors.append("E004:runtime_entrypoint_SIMPLE_IDENTITY_REQUIRED")
    elif entrypoint.casefold() in PROHIBITED_ENTRYPOINTS:
        errors.append("E004:SHELL_ENTRYPOINT_PROHIBITED")
    elif argv[0] != entrypoint:
        errors.append("E004:argv_ENTRYPOINT_MISMATCH")
    return errors


def validate_e004_execution_plan(plan: Any) -> list[str]:
    """Validate one exact future E004 invocation plan; fail closed."""
    errors = validate_closed_object(
        plan,
        required_fields=PLAN_REQUIRED_FIELDS,
        field="E004ExecutionPlan",
    )
    if not isinstance(plan, dict):
        return errors

    for field in ("plan_id", "candidate_id", "a15_activation_id"):
        if not _resolved_string(plan.get(field)):
            errors.append(f"E004:{field}_RESOLVED_STRING_REQUIRED")
    if plan.get("plan_version") != "1.0":
        errors.append("E004:plan_version_MUST_BE_1.0")

    for field in SHA256_FIELDS:
        if not is_canonical_sha256(plan.get(field)):
            errors.append(f"E004:{field}_CANONICAL_SHA256_REQUIRED")
    for field in GIT_SHA_FIELDS:
        value = plan.get(field)
        if not isinstance(value, str) or _GIT_SHA_RE.fullmatch(value) is None:
            errors.append(f"E004:{field}_EXACT_GIT_SHA_REQUIRED")

    for field, expected in EXPECTED_STATES.items():
        if plan.get(field) != expected:
            errors.append(f"E004:{field}_MUST_BE_{expected}")

    if plan.get("no_spend_assertion") is not True:
        errors.append("E004:NO_SPEND_ASSERTION_REQUIRED")
    if plan.get("no_credentials_assertion") is not True:
        errors.append("E004:NO_CREDENTIALS_ASSERTION_REQUIRED")

    if _contains_prohibited_marker(plan):
        errors.append("E004:PROHIBITED_PAYLOAD_OR_SECRET_MARKER")

    errors.extend(_validate_argv(plan))
    return sorted(set(errors))


def build_e004_execution_request(plan: Any) -> dict[str, object]:
    """Build an immutable request for a separately governed external executor.

    This function performs no execution. A blocked plan returns no request.
    """
    errors = validate_e004_execution_plan(plan)
    if errors:
        return {
            "state": "BLOCKED",
            "reason_codes": errors,
            "execution_performed": False,
            "request": None,
        }

    assert isinstance(plan, dict)
    request = {
        "request_schema": "commandmed-e004-execution-request-v1",
        "plan": dict(plan),
    }
    request_sha = compute_canonical_sha256(request)
    return {
        "state": "READY_FOR_EXTERNAL_EXECUTOR",
        "reason_codes": [],
        "execution_performed": False,
        "request_canonical_sha256": request_sha,
        "request": request,
    }
