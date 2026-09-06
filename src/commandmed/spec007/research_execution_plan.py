"""Deterministic non-executing SP007-RO-001 execution-plan contracts.

The contract binds an exact guarded driver invocation and the exact backend
command families required by the frozen research-component tournament. It is
control-plane metadata only: validation never opens model weights, imports model
frameworks, invokes subprocesses, accesses a network, or grants authority.
"""

from __future__ import annotations

import re
from typing import Any, Mapping

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.foundation import is_canonical_sha256, validate_closed_object
from src.commandmed.spec007.research_candidate_bundle import (
    CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256,
)
from src.commandmed.spec007.research_execution import (
    RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
)
from src.commandmed.spec007.research_scope import RESEARCH_COMPONENT_SCOPE_ID
from src.commandmed.spec007.research_tournament import (
    CONTROL_CANDIDATE,
    PRIMARY_CANDIDATES,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
)

EXECUTION_PLAN_SET_ID = "SP007_RO_001_EXECUTION_PLAN_SET_V1"
EXECUTION_DRIVER_MODULE = "src.commandmed.spec007.research_tournament_executor"
EXECUTION_DRIVER_ENTRYPOINT = "python3.12"
EXECUTION_DRIVER_EXECUTABLE_SHA256 = (
    "a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223"
)
PREEXECUTION_SUBJECT_PATH = ".commandmed/spec007/preexecution-subject.json"
EXECUTION_PLAN_PATH = "specs/007-sft-v1/e004-successor-execution-plan-set-v1.json"

LLAMA_CPP_RUNTIME_ARCHIVE_SHA256 = (
    "91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583"
)
LLAMA_CPP_DISPATCHER_SHA256 = (
    "74e42a1bdeffb6e6dc14af499a1126895373f77e2b07d954c3aaa9dd895e8925"
)
LLAMA_CPP_SOURCE_REVISION = "c1d0e7a004015f23bc0233470b747b596f29b264"
LLAMA_CPP_BUILD_TOOLCHAIN = "GNU_11.4.0_LINUX_X86_64"
LLAMA_CPP_BACKEND_ENTRYPOINT = "llama"

TRANSFORMERS_INSTALLED_ENVIRONMENT_MANIFEST_SHA256 = (
    "54517b34077e193c9bc019e8a2b232d3c9b6d6a85c4c6df13bcd38aa2b66c384"
)
TRANSFORMERS_DEPENDENCY_SET_MANIFEST_SHA256 = (
    "bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05"
)
TRANSFORMERS_SOURCE_REVISION = "753d61104116eefc8ffc977327b441ee0c8d599f"
TRANSFORMERS_VERSION = "4.57.6"
TORCH_VERSION = "2.11.0+cpu"

_ALLOWED_BACKENDS = frozenset({"LLAMA_CPP", "TRANSFORMERS_TORCH_CPU"})
_ALLOWED_MC_ADAPTERS = frozenset(
    {
        "LLAMA_CPP_MULTIPLE_CHOICE_BINARY_V1",
        "TRANSFORMERS_NORMALIZED_CONTINUATION_LOG_LIKELIHOOD_V1",
    }
)
_ALLOWED_RESOURCE_ADAPTERS = frozenset(
    {
        "LLAMA_CPP_COMPLETION_RESOURCE_PROBE_V1",
        "TRANSFORMERS_GREEDY_RESOURCE_PROBE_V1",
    }
)
_FORBIDDEN_ARG_MARKERS = (
    "--api-key",
    "--apikey",
    "--token",
    "--password",
    "--credential",
    "hf_token",
    "hugging_face_hub_token",
)
_GIT_SHA_RE = re.compile(r"^[0-9a-f]{40}$")

_PLAN_SET_FIELDS = (
    "schema_version",
    "plan_set_id",
    "plan_set_sha256",
    "scope_id",
    "protocol_id",
    "protocol_sha256",
    "evaluation_asset_set_sha256",
    "candidate_artifact_bundle_set_sha256",
    "driver_module",
    "driver_entrypoint",
    "driver_executable_sha256",
    "preexecution_subject_path",
    "plans",
)
_PLAN_FIELDS = (
    "candidate_id",
    "upstream_revision",
    "candidate_role",
    "winner_eligible",
    "execution_plan_sha256",
    "candidate_complete_bundle_sha256",
    "tokenizer_config_sha256",
    "backend_family",
    "backend_runtime_artifact_sha256",
    "backend_runtime_entrypoint",
    "backend_runtime_executable_sha256",
    "backend_runtime_source_revision",
    "backend_build_toolchain_identity",
    "runtime_argv",
    "multiple_choice_adapter",
    "multiple_choice_argv_prefix",
    "resource_probe_adapter",
    "resource_probe_argv_prefix",
    "working_directory_semantics",
    "input_materialization_semantics",
    "network_requirement",
    "credential_requirement",
    "model_execution_requires_authorized_subject",
)


def _self_hash(record: Mapping[str, Any], field: str) -> str:
    projection = dict(record)
    projection.pop(field, None)
    return compute_canonical_sha256(projection)


def compute_execution_plan_sha256(plan: Mapping[str, Any]) -> str:
    return _self_hash(plan, "execution_plan_sha256")


def compute_execution_plan_set_sha256(plan_set: Mapping[str, Any]) -> str:
    return _self_hash(plan_set, "plan_set_sha256")


def expected_driver_argv(candidate_id: str) -> list[str]:
    return [
        EXECUTION_DRIVER_ENTRYPOINT,
        "-m",
        EXECUTION_DRIVER_MODULE,
        "--subject",
        PREEXECUTION_SUBJECT_PATH,
        "--plan",
        EXECUTION_PLAN_PATH,
        "--candidate-id",
        candidate_id,
    ]


def _expected_candidates() -> dict[tuple[str, str], tuple[str, bool]]:
    expected = {pair: ("PRIMARY", True) for pair in PRIMARY_CANDIDATES}
    expected[CONTROL_CANDIDATE] = ("CONTROL", False)
    return expected


def _validate_argv(value: Any, prefix: str) -> list[str]:
    if not isinstance(value, list) or not value:
        return [f"{prefix}: argv must be a non-empty list"]
    if any(not isinstance(token, str) or not token or "\x00" in token for token in value):
        return [f"{prefix}: argv tokens must be non-empty strings"]
    errors: list[str] = []
    lowered = [token.casefold() for token in value]
    if any(marker in token for token in lowered for marker in _FORBIDDEN_ARG_MARKERS):
        errors.append(f"{prefix}: credential-bearing argv is prohibited")
    if any("\n" in token or "\r" in token for token in value):
        errors.append(f"{prefix}: control separators are prohibited")
    return errors


def _validate_backend(plan: Mapping[str, Any], prefix: str) -> list[str]:
    errors: list[str] = []
    backend = plan.get("backend_family")
    if backend not in _ALLOWED_BACKENDS:
        return [f"{prefix}: backend_family is not allowed"]

    source_revision = plan.get("backend_runtime_source_revision")
    if not isinstance(source_revision, str) or _GIT_SHA_RE.fullmatch(source_revision) is None:
        errors.append(f"{prefix}: backend_runtime_source_revision must be exact git sha")

    for field in (
        "backend_runtime_artifact_sha256",
        "backend_runtime_executable_sha256",
        "candidate_complete_bundle_sha256",
        "tokenizer_config_sha256",
    ):
        if not is_canonical_sha256(plan.get(field)):
            errors.append(f"{prefix}: {field} must be lowercase sha256 hex")

    if backend == "LLAMA_CPP":
        expected = {
            "backend_runtime_artifact_sha256": LLAMA_CPP_RUNTIME_ARCHIVE_SHA256,
            "backend_runtime_entrypoint": LLAMA_CPP_BACKEND_ENTRYPOINT,
            "backend_runtime_executable_sha256": LLAMA_CPP_DISPATCHER_SHA256,
            "backend_runtime_source_revision": LLAMA_CPP_SOURCE_REVISION,
            "backend_build_toolchain_identity": LLAMA_CPP_BUILD_TOOLCHAIN,
            "multiple_choice_adapter": "LLAMA_CPP_MULTIPLE_CHOICE_BINARY_V1",
            "resource_probe_adapter": "LLAMA_CPP_COMPLETION_RESOURCE_PROBE_V1",
        }
        mc_prefix = plan.get("multiple_choice_argv_prefix")
        resource_prefix = plan.get("resource_probe_argv_prefix")
        if mc_prefix != [
            "llama",
            "perplexity",
            "--offline",
            "--device",
            "none",
            "--multiple-choice",
        ]:
            errors.append(f"{prefix}: llama.cpp multiple_choice_argv_prefix mismatch")
        if resource_prefix != [
            "llama",
            "completion",
            "--offline",
            "--device",
            "none",
            "--no-display-prompt",
            "--seed",
            "0",
            "--temp",
            "0",
            "--predict",
            "8",
        ]:
            errors.append(f"{prefix}: llama.cpp resource_probe_argv_prefix mismatch")
    else:
        expected = {
            "backend_runtime_artifact_sha256": TRANSFORMERS_INSTALLED_ENVIRONMENT_MANIFEST_SHA256,
            "backend_runtime_entrypoint": "python3.12",
            "backend_runtime_executable_sha256": EXECUTION_DRIVER_EXECUTABLE_SHA256,
            "backend_runtime_source_revision": TRANSFORMERS_SOURCE_REVISION,
            "backend_build_toolchain_identity": (
                f"PYTHON_3.12.3_TRANSFORMERS_{TRANSFORMERS_VERSION}_TORCH_{TORCH_VERSION}"
            ),
            "multiple_choice_adapter": (
                "TRANSFORMERS_NORMALIZED_CONTINUATION_LOG_LIKELIHOOD_V1"
            ),
            "resource_probe_adapter": "TRANSFORMERS_GREEDY_RESOURCE_PROBE_V1",
        }
        mc_prefix = plan.get("multiple_choice_argv_prefix")
        resource_prefix = plan.get("resource_probe_argv_prefix")
        expected_prefix = [
            "python3.12",
            "-m",
            EXECUTION_DRIVER_MODULE,
            "--backend-child",
            "transformers",
        ]
        if mc_prefix != expected_prefix + ["--mode", "multiple-choice"]:
            errors.append(f"{prefix}: transformers multiple_choice_argv_prefix mismatch")
        if resource_prefix != expected_prefix + ["--mode", "resource-probe"]:
            errors.append(f"{prefix}: transformers resource_probe_argv_prefix mismatch")

    for field, expected_value in expected.items():
        if plan.get(field) != expected_value:
            errors.append(f"{prefix}: {field} mismatch")
    return errors


def _validate_plan(
    plan: Any,
    *,
    expected: dict[tuple[str, str], tuple[str, bool]],
    seen: set[tuple[str, str]],
    prefix: str,
) -> list[str]:
    errors = validate_closed_object(plan, required_fields=_PLAN_FIELDS, field=prefix)
    if errors or not isinstance(plan, dict):
        return errors

    pair = (plan.get("candidate_id"), plan.get("upstream_revision"))
    expected_role = expected.get(pair)
    if expected_role is None:
        errors.append(f"{prefix}: candidate identity is outside frozen E001 set")
    else:
        if pair in seen:
            errors.append(f"{prefix}: duplicate candidate identity")
        seen.add(pair)
        role, winner_eligible = expected_role
        if plan.get("candidate_role") != role:
            errors.append(f"{prefix}: candidate_role mismatch")
        if plan.get("winner_eligible") is not winner_eligible:
            errors.append(f"{prefix}: winner_eligible mismatch")

    if not is_canonical_sha256(plan.get("execution_plan_sha256")):
        errors.append(f"{prefix}: execution_plan_sha256 must be lowercase sha256 hex")
    elif plan.get("execution_plan_sha256") != compute_execution_plan_sha256(plan):
        errors.append(f"{prefix}: execution_plan_sha256 mismatch")

    runtime_argv = plan.get("runtime_argv")
    errors.extend(_validate_argv(runtime_argv, f"{prefix}.runtime_argv"))
    if isinstance(plan.get("candidate_id"), str) and runtime_argv != expected_driver_argv(
        plan["candidate_id"]
    ):
        errors.append(f"{prefix}: guarded runtime_argv mismatch")

    for field in ("multiple_choice_argv_prefix", "resource_probe_argv_prefix"):
        errors.extend(_validate_argv(plan.get(field), f"{prefix}.{field}"))

    if plan.get("multiple_choice_adapter") not in _ALLOWED_MC_ADAPTERS:
        errors.append(f"{prefix}: multiple_choice_adapter is not allowed")
    if plan.get("resource_probe_adapter") not in _ALLOWED_RESOURCE_ADAPTERS:
        errors.append(f"{prefix}: resource_probe_adapter is not allowed")
    expected_static = {
        "working_directory_semantics": "REPOSITORY_ROOT",
        "input_materialization_semantics": (
            "FROZEN_EVALUATION_ASSET_SET_TO_EPHEMERAL_LOCAL_FILES_V1"
        ),
        "network_requirement": "OFFLINE_DEFAULT_DENY",
        "credential_requirement": "NONE",
        "model_execution_requires_authorized_subject": True,
    }
    for field, expected_value in expected_static.items():
        if plan.get(field) != expected_value:
            errors.append(f"{prefix}: {field} mismatch")

    errors.extend(_validate_backend(plan, prefix))
    return errors


def validate_execution_plan_set(plan_set: Any) -> list[str]:
    prefix = "ResearchComponentExecutionPlanSet"
    errors = validate_closed_object(
        plan_set, required_fields=_PLAN_SET_FIELDS, field=prefix
    )
    if errors or not isinstance(plan_set, dict):
        return errors

    expected_static = {
        "schema_version": "1",
        "plan_set_id": EXECUTION_PLAN_SET_ID,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "protocol_id": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
        "protocol_sha256": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
        "evaluation_asset_set_sha256": RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
        "candidate_artifact_bundle_set_sha256": CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256,
        "driver_module": EXECUTION_DRIVER_MODULE,
        "driver_entrypoint": EXECUTION_DRIVER_ENTRYPOINT,
        "driver_executable_sha256": EXECUTION_DRIVER_EXECUTABLE_SHA256,
        "preexecution_subject_path": PREEXECUTION_SUBJECT_PATH,
    }
    for field, expected_value in expected_static.items():
        if plan_set.get(field) != expected_value:
            errors.append(f"{prefix}: {field} mismatch")

    plans = plan_set.get("plans")
    if not isinstance(plans, list) or len(plans) != 4:
        errors.append(f"{prefix}: plans must contain exactly four records")
        return sorted(set(errors))

    expected = _expected_candidates()
    expected_order = list(PRIMARY_CANDIDATES) + [CONTROL_CANDIDATE]
    actual_order = [
        (item.get("candidate_id"), item.get("upstream_revision"))
        for item in plans
        if isinstance(item, dict)
    ]
    if actual_order != expected_order:
        errors.append(f"{prefix}: plans must use frozen deterministic candidate order")

    seen: set[tuple[str, str]] = set()
    for index, plan in enumerate(plans):
        errors.extend(
            _validate_plan(
                plan,
                expected=expected,
                seen=seen,
                prefix=f"{prefix}.plans[{index}]",
            )
        )
    if seen != set(expected):
        errors.append(f"{prefix}: exact frozen E001 candidate set required")

    claimed = plan_set.get("plan_set_sha256")
    if not is_canonical_sha256(claimed):
        errors.append(f"{prefix}: plan_set_sha256 must be lowercase sha256 hex")
    elif claimed != compute_execution_plan_set_sha256(plan_set):
        errors.append(f"{prefix}: plan_set_sha256 mismatch")
    return sorted(set(errors))
