"""Deterministic non-executing E004 four-candidate execution-plan control plane.

This module composes the canonical llama.cpp and Transformers/PyTorch adapter
manifests into exact per-candidate plan identities and top-level orchestration
argv. It does not implement the external executor, load model weights, invoke a
process, access the network, select a winner, activate A15, or perform execution.
"""

from __future__ import annotations

from typing import Any, Mapping

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.e004_execution_adapter import (
    LLAMA_BUILD_TOOLCHAIN_IDENTITY,
    LLAMA_CLI_EXECUTABLE_SHA256,
    LLAMA_CPP_SOURCE_REVISION,
    LLAMA_PERPLEXITY_EXECUTABLE_SHA256,
    LLAMA_RUNTIME_ARCHIVE_SHA256,
    build_e004_llama_adapter_manifest,
    validate_e004_llama_adapter_manifest,
)
from src.commandmed.spec007.e004_transformers_adapter import (
    PYTHON_RUNTIME_ENTRYPOINT,
    PYTHON_RUNTIME_SHA256,
    PYTHON_RUNTIME_VERSION,
    TORCH_MODULE_SHA256,
    TORCH_VERSION,
    TRANSFORMERS_DEPENDENCY_SET_MANIFEST_SHA256,
    TRANSFORMERS_INSTALLED_ENVIRONMENT_MANIFEST_SHA256,
    TRANSFORMERS_MODULE_SHA256,
    TRANSFORMERS_SOURCE_REVISION,
    TRANSFORMERS_VERSION,
    build_e004_transformers_adapter_manifest,
    validate_e004_transformers_adapter_manifest,
)
from src.commandmed.spec007.foundation import is_canonical_sha256, validate_closed_object
from src.commandmed.spec007.research_candidate_bundle import (
    CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256,
    validate_candidate_artifact_bundle_set,
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

ORCHESTRATOR_CONTRACT_ID = "COMMANDMED_E004_EXTERNAL_EXECUTOR_CONTRACT_V1"
ORCHESTRATOR_ENTRYPOINT = "commandmed-e004-external-executor-v1"
ORCHESTRATOR_IMPLEMENTATION_STATE = "NEEDS_FUTURE_EXECUTION_ENVIRONMENT_BINDING"
RUNTIME_FORMAT_COMPATIBILITY_STATE = "NEEDS_EMPIRICAL_MODEL_LOAD_EVIDENCE"
WORKSPACE_LAYOUT_ID = "SP007_RO_001_RELATIVE_WORKSPACE_V1"

FROZEN_CANDIDATES = (*PRIMARY_CANDIDATES, CONTROL_CANDIDATE)
_LLAMA_CANDIDATES = frozenset(PRIMARY_CANDIDATES[:2])

_PLAN_FIELDS = (
    "schema_version",
    "execution_plan_id",
    "execution_plan_sha256",
    "scope_id",
    "protocol_id",
    "protocol_sha256",
    "evaluation_asset_set_sha256",
    "candidate_bundle_set_sha256",
    "candidate_id",
    "upstream_revision",
    "candidate_role",
    "winner_eligible",
    "artifact_format",
    "model_artifact_sha256",
    "model_artifact_bytes",
    "complete_bundle_sha256",
    "complete_bundle_bytes",
    "tokenizer_config_sha256",
    "candidate_bundle_relative_path",
    "workspace_layout_id",
    "backend_family",
    "backend_runtime_identity",
    "adapter_id",
    "adapter_sha256",
    "adapter_operation_set_sha256",
    "orchestrator_contract_id",
    "orchestrator_implementation_state",
    "runtime_entrypoint",
    "runtime_argv",
    "runtime_format_compatibility_state",
    "future_execution_environment_state",
    "execution_performed",
    "authorized_spend_usd",
)
_PLAN_SET_FIELDS = (
    "schema_version",
    "plan_set_id",
    "plan_set_sha256",
    "scope_id",
    "protocol_id",
    "protocol_sha256",
    "evaluation_asset_set_sha256",
    "candidate_bundle_set_sha256",
    "execution_plans",
    "execution_performed",
    "authorized_spend_usd",
)


def _self_hash(record: Mapping[str, Any], identity_field: str) -> str:
    projection = dict(record)
    projection.pop(identity_field, None)
    return compute_canonical_sha256(projection)


def compute_e004_execution_plan_sha256(plan: Mapping[str, Any]) -> str:
    """Compute one deterministic per-candidate execution-plan identity."""
    return _self_hash(plan, "execution_plan_sha256")


def compute_e004_execution_plan_set_sha256(plan_set: Mapping[str, Any]) -> str:
    """Compute the deterministic identity of the four-candidate plan set."""
    return _self_hash(plan_set, "plan_set_sha256")


def _bundle_for_candidate(
    bundle_set: Any, candidate_id: str, upstream_revision: str
) -> Mapping[str, Any]:
    errors = validate_candidate_artifact_bundle_set(bundle_set)
    if errors or not isinstance(bundle_set, dict):
        raise ValueError("candidate artifact bundle set is not canonically valid")
    if bundle_set.get("bundle_set_sha256") != CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256:
        raise ValueError("candidate artifact bundle set identity mismatch")
    bundles = bundle_set.get("candidate_bundles")
    if not isinstance(bundles, list):
        raise ValueError("candidate artifact bundle records are missing")
    pair = (candidate_id, upstream_revision)
    if pair not in FROZEN_CANDIDATES:
        raise ValueError("candidate is outside the frozen E001 set")
    for bundle in bundles:
        if not isinstance(bundle, dict):
            continue
        if (bundle.get("candidate_id"), bundle.get("upstream_revision")) == pair:
            return bundle
    raise ValueError("candidate artifact bundle is missing")


def _candidate_index(pair: tuple[str, str]) -> int:
    try:
        return FROZEN_CANDIDATES.index(pair) + 1
    except ValueError as exc:
        raise ValueError("candidate is outside the frozen E001 set") from exc


def _llama_model_relative_path(bundle: Mapping[str, Any], candidate_root: str) -> str:
    files = bundle.get("files")
    if not isinstance(files, list):
        raise ValueError("candidate artifact file manifest is missing")
    model_files = [
        item
        for item in files
        if isinstance(item, dict) and item.get("purpose") == "MODEL_WEIGHT"
    ]
    if len(model_files) != 1 or not isinstance(model_files[0].get("path"), str):
        raise ValueError("GGUF candidate must bind exactly one model-weight file")
    path = str(model_files[0]["path"])
    if "\x00" in path or "\r" in path or "\n" in path or path.startswith("/"):
        raise ValueError("candidate model path must be a safe relative path")
    return f"{candidate_root}/{path}"


def _backend_runtime_identity(pair: tuple[str, str]) -> dict[str, Any]:
    if pair in _LLAMA_CANDIDATES:
        return {
            "runtime_family": "LLAMA_CPP_GGUF",
            "runtime_source_revision": LLAMA_CPP_SOURCE_REVISION,
            "runtime_artifact_sha256": LLAMA_RUNTIME_ARCHIVE_SHA256,
            "build_toolchain_identity": LLAMA_BUILD_TOOLCHAIN_IDENTITY,
            "entrypoint_executables": [
                {
                    "entrypoint": "llama-perplexity",
                    "executable_sha256": LLAMA_PERPLEXITY_EXECUTABLE_SHA256,
                },
                {
                    "entrypoint": "llama-cli",
                    "executable_sha256": LLAMA_CLI_EXECUTABLE_SHA256,
                },
            ],
        }
    return {
        "runtime_family": "TRANSFORMERS_TORCH_CPU",
        "runtime_source_revision": TRANSFORMERS_SOURCE_REVISION,
        "runtime_artifact_sha256": TRANSFORMERS_INSTALLED_ENVIRONMENT_MANIFEST_SHA256,
        "build_toolchain_identity": (
            f"PYTHON_{PYTHON_RUNTIME_VERSION}_TRANSFORMERS_{TRANSFORMERS_VERSION}_"
            f"TORCH_{TORCH_VERSION}_CPU"
        ),
        "entrypoint_executables": [
            {
                "entrypoint": PYTHON_RUNTIME_ENTRYPOINT,
                "executable_sha256": PYTHON_RUNTIME_SHA256,
            }
        ],
        "dependency_set_manifest_sha256": TRANSFORMERS_DEPENDENCY_SET_MANIFEST_SHA256,
        "transformers_module_sha256": TRANSFORMERS_MODULE_SHA256,
        "torch_module_sha256": TORCH_MODULE_SHA256,
    }


def _build_runtime_argv(
    *,
    execution_plan_id: str,
    candidate_id: str,
    upstream_revision: str,
    backend_family: str,
    adapter_sha256: str,
) -> list[str]:
    return [
        ORCHESTRATOR_ENTRYPOINT,
        "--execution-plan-id",
        execution_plan_id,
        "--candidate-id",
        candidate_id,
        "--candidate-revision",
        upstream_revision,
        "--backend-family",
        backend_family,
        "--adapter-sha256",
        adapter_sha256,
        "--candidate-bundle-set-sha256",
        CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256,
        "--evaluation-asset-set-sha256",
        RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
        "--network-mode",
        "offline",
        "--authorized-spend-usd",
        "0",
    ]


def build_e004_candidate_execution_plan(
    asset_set: Any,
    bundle_set: Any,
    *,
    candidate_id: str,
    upstream_revision: str,
) -> dict[str, Any]:
    """Compose one exact non-executing plan from the canonical adapter route."""
    bundle = _bundle_for_candidate(bundle_set, candidate_id, upstream_revision)
    pair = (candidate_id, upstream_revision)
    candidate_index = _candidate_index(pair)
    candidate_root = f"candidates/candidate-{candidate_index:02d}"

    if pair in _LLAMA_CANDIDATES:
        if bundle.get("artifact_format") != "GGUF":
            raise ValueError("llama.cpp route requires the frozen GGUF bundle")
        adapter = build_e004_llama_adapter_manifest(
            asset_set,
            candidate_id=candidate_id,
            upstream_revision=upstream_revision,
            model_path=_llama_model_relative_path(bundle, candidate_root),
            payload_directory=f"evaluation/candidate-{candidate_index:02d}",
        )
        adapter_errors = validate_e004_llama_adapter_manifest(adapter, asset_set)
        if adapter_errors:
            raise ValueError("llama.cpp adapter manifest is not canonically valid")
        backend_family = "LLAMA_CPP_GGUF"
    else:
        if bundle.get("artifact_format") != "SAFETENSORS":
            raise ValueError("Transformers route requires the frozen SAFETENSORS bundle")
        adapter = build_e004_transformers_adapter_manifest(
            asset_set,
            bundle_set,
            candidate_id=candidate_id,
            upstream_revision=upstream_revision,
        )
        adapter_errors = validate_e004_transformers_adapter_manifest(
            adapter, asset_set, bundle_set
        )
        if adapter_errors:
            raise ValueError("Transformers adapter manifest is not canonically valid")
        backend_family = "TRANSFORMERS_TORCH_CPU"

    execution_plan_id = (
        f"SP007-RO-001-EXECUTION-PLAN::{candidate_id}@{upstream_revision}"
    )
    plan: dict[str, Any] = {
        "schema_version": "1",
        "execution_plan_id": execution_plan_id,
        "execution_plan_sha256": "0" * 64,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "protocol_id": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
        "protocol_sha256": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
        "evaluation_asset_set_sha256": RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
        "candidate_bundle_set_sha256": CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256,
        "candidate_id": candidate_id,
        "upstream_revision": upstream_revision,
        "candidate_role": bundle.get("candidate_role"),
        "winner_eligible": bundle.get("winner_eligible"),
        "artifact_format": bundle.get("artifact_format"),
        "model_artifact_sha256": bundle.get("model_artifact_sha256"),
        "model_artifact_bytes": bundle.get("model_artifact_bytes"),
        "complete_bundle_sha256": bundle.get("complete_bundle_sha256"),
        "complete_bundle_bytes": bundle.get("complete_bundle_bytes"),
        "tokenizer_config_sha256": bundle.get("tokenizer_config_sha256"),
        "candidate_bundle_relative_path": candidate_root,
        "workspace_layout_id": WORKSPACE_LAYOUT_ID,
        "backend_family": backend_family,
        "backend_runtime_identity": _backend_runtime_identity(pair),
        "adapter_id": adapter.get("adapter_id"),
        "adapter_sha256": adapter.get("adapter_sha256"),
        "adapter_operation_set_sha256": compute_canonical_sha256(adapter.get("operations")),
        "orchestrator_contract_id": ORCHESTRATOR_CONTRACT_ID,
        "orchestrator_implementation_state": ORCHESTRATOR_IMPLEMENTATION_STATE,
        "runtime_entrypoint": ORCHESTRATOR_ENTRYPOINT,
        "runtime_argv": _build_runtime_argv(
            execution_plan_id=execution_plan_id,
            candidate_id=candidate_id,
            upstream_revision=upstream_revision,
            backend_family=backend_family,
            adapter_sha256=str(adapter.get("adapter_sha256")),
        ),
        "runtime_format_compatibility_state": RUNTIME_FORMAT_COMPATIBILITY_STATE,
        "future_execution_environment_state": "INCOMPLETE",
        "execution_performed": False,
        "authorized_spend_usd": 0,
    }
    plan["execution_plan_sha256"] = compute_e004_execution_plan_sha256(plan)
    return plan


def validate_e004_candidate_execution_plan(
    plan: Any, asset_set: Any, bundle_set: Any
) -> list[str]:
    """Validate one composed candidate plan against canonical inputs."""
    prefix = "E004CandidateExecutionPlan"
    errors = validate_closed_object(plan, required_fields=_PLAN_FIELDS, field=prefix)
    if errors or not isinstance(plan, dict):
        return errors
    candidate_id = plan.get("candidate_id")
    upstream_revision = plan.get("upstream_revision")
    if not isinstance(candidate_id, str) or not isinstance(upstream_revision, str):
        return sorted(set(errors + [f"{prefix}: candidate identity must be strings"]))
    try:
        expected = build_e004_candidate_execution_plan(
            asset_set,
            bundle_set,
            candidate_id=candidate_id,
            upstream_revision=upstream_revision,
        )
    except ValueError as exc:
        return sorted(set(errors + [f"{prefix}: {exc}"]))

    for field in _PLAN_FIELDS:
        if plan.get(field) != expected.get(field):
            errors.append(f"{prefix}: {field} mismatch")
    for field in (
        "execution_plan_sha256",
        "protocol_sha256",
        "evaluation_asset_set_sha256",
        "candidate_bundle_set_sha256",
        "model_artifact_sha256",
        "complete_bundle_sha256",
        "tokenizer_config_sha256",
        "adapter_sha256",
        "adapter_operation_set_sha256",
    ):
        if not is_canonical_sha256(plan.get(field)):
            errors.append(f"{prefix}: {field} must be canonical sha256")
    claimed_plan_sha = plan.get("execution_plan_sha256")
    if (
        is_canonical_sha256(claimed_plan_sha)
        and claimed_plan_sha != compute_e004_execution_plan_sha256(plan)
    ):
        errors.append(f"{prefix}: execution_plan_sha256 mismatch")
    if plan.get("runtime_entrypoint") != ORCHESTRATOR_ENTRYPOINT:
        errors.append(f"{prefix}: runtime_entrypoint mismatch")
    argv = plan.get("runtime_argv")
    if not isinstance(argv, list) or not argv or argv[0] != ORCHESTRATOR_ENTRYPOINT:
        errors.append(f"{prefix}: runtime_argv must bind the exact top-level entrypoint")
    if plan.get("runtime_format_compatibility_state") != RUNTIME_FORMAT_COMPATIBILITY_STATE:
        errors.append(f"{prefix}: empirical runtime compatibility must remain unresolved")
    if plan.get("orchestrator_implementation_state") != ORCHESTRATOR_IMPLEMENTATION_STATE:
        errors.append(f"{prefix}: future executor implementation must remain unbound")
    if plan.get("future_execution_environment_state") != "INCOMPLETE":
        errors.append(f"{prefix}: future execution environment must remain incomplete")
    if plan.get("execution_performed") is not False:
        errors.append(f"{prefix}: execution_performed must be false")
    if plan.get("authorized_spend_usd") != 0:
        errors.append(f"{prefix}: authorized_spend_usd must equal zero")
    return sorted(set(errors))


def build_e004_four_candidate_execution_plan_set(
    asset_set: Any, bundle_set: Any
) -> dict[str, Any]:
    """Build the exact four-candidate non-executing execution-plan set."""
    plans = [
        build_e004_candidate_execution_plan(
            asset_set,
            bundle_set,
            candidate_id=candidate_id,
            upstream_revision=upstream_revision,
        )
        for candidate_id, upstream_revision in FROZEN_CANDIDATES
    ]
    plan_set: dict[str, Any] = {
        "schema_version": "1",
        "plan_set_id": "SP007_RO_001_FOUR_CANDIDATE_EXECUTION_PLAN_SET_V1",
        "plan_set_sha256": "0" * 64,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "protocol_id": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
        "protocol_sha256": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
        "evaluation_asset_set_sha256": RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
        "candidate_bundle_set_sha256": CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256,
        "execution_plans": plans,
        "execution_performed": False,
        "authorized_spend_usd": 0,
    }
    plan_set["plan_set_sha256"] = compute_e004_execution_plan_set_sha256(plan_set)
    return plan_set


def validate_e004_four_candidate_execution_plan_set(
    plan_set: Any, asset_set: Any, bundle_set: Any
) -> list[str]:
    """Validate exact candidate coverage, order, identities, and self-hash."""
    prefix = "E004FourCandidateExecutionPlanSet"
    errors = validate_closed_object(
        plan_set, required_fields=_PLAN_SET_FIELDS, field=prefix
    )
    if errors or not isinstance(plan_set, dict):
        return errors
    plans = plan_set.get("execution_plans")
    if not isinstance(plans, list) or len(plans) != 4:
        return sorted(set(errors + [f"{prefix}: exactly four execution plans required"]))

    observed: list[tuple[Any, Any]] = []
    for index, plan in enumerate(plans):
        errors.extend(validate_e004_candidate_execution_plan(plan, asset_set, bundle_set))
        if isinstance(plan, dict):
            observed.append((plan.get("candidate_id"), plan.get("upstream_revision")))
        else:
            errors.append(f"{prefix}.execution_plans[{index}]: object required")
    if observed != list(FROZEN_CANDIDATES):
        errors.append(f"{prefix}: exact dependency-ordered frozen candidate set required")

    expected = build_e004_four_candidate_execution_plan_set(asset_set, bundle_set)
    for field in _PLAN_SET_FIELDS:
        if plan_set.get(field) != expected.get(field):
            errors.append(f"{prefix}: {field} mismatch")
    claimed_set_sha = plan_set.get("plan_set_sha256")
    if not is_canonical_sha256(claimed_set_sha):
        errors.append(f"{prefix}: plan_set_sha256 must be canonical sha256")
    elif claimed_set_sha != compute_e004_execution_plan_set_sha256(plan_set):
        errors.append(f"{prefix}: plan_set_sha256 mismatch")
    if plan_set.get("execution_performed") is not False:
        errors.append(f"{prefix}: execution_performed must be false")
    if plan_set.get("authorized_spend_usd") != 0:
        errors.append(f"{prefix}: authorized_spend_usd must equal zero")
    return sorted(set(errors))
