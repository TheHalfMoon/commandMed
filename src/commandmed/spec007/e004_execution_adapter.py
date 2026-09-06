"""Non-executing E004 llama.cpp execution-adapter control plane.

This module binds the frozen SP007-RO-001 evaluation semantics to deterministic
llama.cpp input bytes and argv projections. It never loads a model, opens a
device, invokes a process, accesses the network, selects a winner, or grants
execution authority.
"""

from __future__ import annotations

import hashlib
import re
import struct
from typing import Any, Mapping

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.foundation import is_canonical_sha256
from src.commandmed.spec007.research_execution import (
    RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
)
from src.commandmed.spec007.research_scope import RESEARCH_COMPONENT_SCOPE_ID
from src.commandmed.spec007.research_tournament import (
    PRIMARY_CANDIDATES,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
)
from src.commandmed.spec007.research_tournament_assets import (
    validate_research_component_evaluation_asset,
    validate_research_component_evaluation_asset_set,
)

LLAMA_CPP_SOURCE_REVISION = "c1d0e7a004015f23bc0233470b747b596f29b264"
LLAMA_RUNTIME_ARCHIVE_SHA256 = (
    "91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583"
)
LLAMA_PERPLEXITY_EXECUTABLE_SHA256 = (
    "1c06240ed8594fd377d655aef2dab0865431e3e779c06638474c96b38e6d74a0"
)
LLAMA_CLI_EXECUTABLE_SHA256 = (
    "f0034d9e6959f6c32b40cbb5326f41ccdbac21b77feb27a6f32c0a7465c9ebf7"
)
LLAMA_BUILD_TOOLCHAIN_IDENTITY = "GNU_11.4.0_LINUX_X86_64"

MULTIPLE_CHOICE_ASSET_KIND = "MULTIPLE_CHOICE_CONDITIONAL_LIKELIHOOD"
MULTIPLE_CHOICE_SCORING_METHOD = "NORMALIZED_CONDITIONAL_LOG_LIKELIHOOD_ARGMAX"
RESOURCE_ASSET_KIND = "RESOURCE_MEASUREMENT_PROTOCOL"
RESOURCE_SCORING_METHOD = "RESOURCE_MEASUREMENT_RECORD_V1"
LLAMA_MULTIPLE_CHOICE_INPUT_FORMAT = "LLAMA_CPP_MULTIPLE_CHOICE_LE32_V1"

FROZEN_EVALUATION_ASSETS: dict[str, tuple[str, str, str]] = {
    "SP007-RO-001-EVAL-INSTRUCTION-V1": (
        "34a0b5f35153f81da19d6f7ec85d2bd8f90c068a1d214dd5e4f146a7e332e237",
        MULTIPLE_CHOICE_ASSET_KIND,
        MULTIPLE_CHOICE_SCORING_METHOD,
    ),
    "SP007-RO-001-EVAL-ENGLISH-V1": (
        "fcd031071722117af6380d02287df815c81fcea1f9b9e28b0f6bff4f01ab24b5",
        MULTIPLE_CHOICE_ASSET_KIND,
        MULTIPLE_CHOICE_SCORING_METHOD,
    ),
    "SP007-RO-001-EVAL-ARABIC-NONCLINICAL-V1": (
        "4b5197c6a82be54ded43f790bc440dd0ca69f13c17c3d7f1adf42ebd5770414f",
        MULTIPLE_CHOICE_ASSET_KIND,
        MULTIPLE_CHOICE_SCORING_METHOD,
    ),
    "SP007-RO-001-EVAL-UNCERTAINTY-V1": (
        "5cc287e3ec9b7a16003a11bea234892f959df60f8a07debf12ec7b36a79d93c9",
        MULTIPLE_CHOICE_ASSET_KIND,
        MULTIPLE_CHOICE_SCORING_METHOD,
    ),
    "SP007-RO-001-EVAL-TOOL-ROUTING-V1": (
        "8665d5f2a128d74062f4f30178c9af602ee03be951a287fb049e208697931fdc",
        MULTIPLE_CHOICE_ASSET_KIND,
        MULTIPLE_CHOICE_SCORING_METHOD,
    ),
    "SP007-RO-001-EVAL-CAPABILITY-V1": (
        "7dd0a1131869b92ae57434c6b9ca4087cda17033b67d9d4bc636a1d6fb4da871",
        MULTIPLE_CHOICE_ASSET_KIND,
        MULTIPLE_CHOICE_SCORING_METHOD,
    ),
    "SP007-RO-001-EVAL-RESOURCE-EFFICIENCY-V1": (
        "a1ddea12b740886643fc396c62553b1ab954404090d16db499a57e933056a200",
        RESOURCE_ASSET_KIND,
        RESOURCE_SCORING_METHOD,
    ),
}

_LLAMA_CANDIDATES = frozenset(PRIMARY_CANDIDATES[:2])
_SAFE_PATH_RE = re.compile(r"^[^\x00\r\n]+$")


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and "\x00" not in value


def _safe_path(value: Any, field: str) -> str:
    if not _nonempty(value) or _SAFE_PATH_RE.fullmatch(str(value)) is None:
        raise ValueError(f"{field}: non-empty path without control separators required")
    return str(value)


def _require_frozen_asset(asset: Any) -> Mapping[str, Any]:
    errors = validate_research_component_evaluation_asset(asset)
    if errors or not isinstance(asset, dict):
        raise ValueError("evaluation asset is not canonically valid")
    asset_id = asset.get("asset_id")
    expected = FROZEN_EVALUATION_ASSETS.get(str(asset_id))
    if expected is None:
        raise ValueError("evaluation asset is outside the frozen SP007-RO-001 set")
    expected_sha, expected_kind, expected_scoring = expected
    if asset.get("asset_sha256") != expected_sha:
        raise ValueError("evaluation asset sha256 does not match frozen identity")
    if asset.get("asset_kind") != expected_kind:
        raise ValueError("evaluation asset kind does not match frozen identity")
    if asset.get("scoring_method") != expected_scoring:
        raise ValueError("evaluation asset scoring method does not match frozen identity")
    return asset


def _pack_u32(value: int) -> bytes:
    if not isinstance(value, int) or isinstance(value, bool) or not 0 <= value <= 0xFFFFFFFF:
        raise ValueError("value must fit unsigned 32-bit integer")
    return struct.pack("<I", value)


def _pack_i32(value: int) -> bytes:
    if not isinstance(value, int) or isinstance(value, bool):
        raise ValueError("value must be an integer")
    return struct.pack("<i", value)


def _pack_string(value: Any) -> bytes:
    if not _nonempty(value):
        raise ValueError("multiple-choice text must be a non-empty string")
    raw = str(value).encode("utf-8")
    return _pack_u32(len(raw)) + raw


def _serialize_multiple_choice_task(case: Mapping[str, Any]) -> bytes:
    prompt = case.get("prompt")
    choices = case.get("choices")
    correct_choice_id = case.get("correct_choice_id")
    if not isinstance(choices, list) or len(choices) != 4:
        raise ValueError("multiple-choice task requires exactly four choices")

    choice_ids = [choice.get("choice_id") for choice in choices if isinstance(choice, dict)]
    if choice_ids != ["A", "B", "C", "D"] or correct_choice_id not in choice_ids:
        raise ValueError("multiple-choice task requires ordered A-D choices and one answer")

    payload = bytearray(_pack_string(prompt))
    payload.extend(_pack_u32(len(choices)))
    for choice in choices:
        assert isinstance(choice, dict)
        payload.extend(_pack_string(choice.get("text")))
    for choice_id in choice_ids:
        payload.extend(_pack_i32(1 if choice_id == correct_choice_id else 0))

    # llama.cpp's current multiple-choice record has a second answer collection
    # reserved for multiple-correct-answer tasks. SP007-RO-001 uses only mc1.
    payload.extend(_pack_u32(0))
    return bytes(payload)


def serialize_llama_multiple_choice_asset(asset: Any) -> bytes:
    """Serialize one frozen MC asset into llama.cpp's exact native task format.

    The pinned runtime is Linux x86_64 and reads native uint32/int records. The
    adapter binds that observed little-endian environment explicitly as LE32.
    No model or executable is opened by this function.
    """
    record = _require_frozen_asset(asset)
    if record.get("asset_kind") != MULTIPLE_CHOICE_ASSET_KIND:
        raise ValueError("resource-measurement asset cannot be serialized as multiple choice")
    cases = record.get("cases")
    if not isinstance(cases, list) or len(cases) != 12:
        raise ValueError("frozen multiple-choice asset must contain exactly 12 cases")

    tasks = [_serialize_multiple_choice_task(case) for case in cases if isinstance(case, dict)]
    if len(tasks) != len(cases):
        raise ValueError("multiple-choice cases must be object records")

    header_size = 4 + 4 * len(tasks)
    offsets: list[int] = []
    cursor = header_size
    for task in tasks:
        offsets.append(cursor)
        cursor += len(task)
        if cursor > 0xFFFFFFFF:
            raise ValueError("serialized multiple-choice payload exceeds uint32 offset range")

    payload = bytearray(_pack_u32(len(tasks)))
    for offset in offsets:
        payload.extend(_pack_u32(offset))
    for task in tasks:
        payload.extend(task)
    return bytes(payload)


def compute_llama_multiple_choice_payload_sha256(asset: Any) -> str:
    """Return the raw-byte SHA-256 for one deterministic llama.cpp MC payload."""
    return hashlib.sha256(serialize_llama_multiple_choice_asset(asset)).hexdigest()


def build_llama_multiple_choice_argv(
    *, model_path: str, payload_path: str, task_count: int = 12
) -> list[str]:
    """Build one deterministic non-executing llama-perplexity argv projection."""
    model = _safe_path(model_path, "model_path")
    payload = _safe_path(payload_path, "payload_path")
    if task_count != 12:
        raise ValueError("frozen SP007-RO-001 multiple-choice task count must equal 12")
    return [
        "llama-perplexity",
        "--model",
        model,
        "--file",
        payload,
        "--multiple-choice",
        "--multiple-choice-tasks",
        "12",
        "--ctx-size",
        "512",
        "--offline",
    ]


def build_llama_resource_probe_argv(
    *, model_path: str, input_text: str, max_new_tokens: int
) -> list[str]:
    """Build deterministic greedy argv for one frozen resource probe."""
    model = _safe_path(model_path, "model_path")
    if not _nonempty(input_text) or "\r" in input_text or "\n" in input_text:
        raise ValueError("input_text must be one non-empty argv-safe token value")
    if max_new_tokens != 8:
        raise ValueError("frozen resource probe max_new_tokens must equal 8")
    return [
        "llama-cli",
        "--model",
        model,
        "--prompt",
        input_text,
        "--n-predict",
        "8",
        "--temp",
        "0",
        "--seed",
        "1",
        "--ctx-size",
        "512",
        "--no-conversation",
        "--no-display-prompt",
        "--offline",
    ]


def build_llama_resource_invocations(asset: Any, *, model_path: str) -> list[dict[str, Any]]:
    """Project all 32 frozen resource invocations without executing them."""
    record = _require_frozen_asset(asset)
    if record.get("asset_kind") != RESOURCE_ASSET_KIND:
        raise ValueError("multiple-choice asset cannot be projected as a resource protocol")
    probes = record.get("probes")
    if not isinstance(probes, list) or len(probes) != 8:
        raise ValueError("frozen resource asset must contain exactly eight probes")

    invocations: list[dict[str, Any]] = []
    for probe in probes:
        if not isinstance(probe, dict):
            raise ValueError("resource probes must be object records")
        probe_id = probe.get("probe_id")
        input_text = probe.get("input_text")
        max_new_tokens = probe.get("max_new_tokens")
        if probe.get("warmup_runs") != 1 or probe.get("measured_runs") != 3:
            raise ValueError("resource probe run counts do not match frozen protocol")
        argv = build_llama_resource_probe_argv(
            model_path=model_path,
            input_text=str(input_text),
            max_new_tokens=max_new_tokens,
        )
        invocations.append(
            {
                "invocation_id": f"{probe_id}-WARMUP-01",
                "probe_id": probe_id,
                "run_class": "WARMUP",
                "run_index": 1,
                "runtime_entrypoint": "llama-cli",
                "runtime_executable_sha256": LLAMA_CLI_EXECUTABLE_SHA256,
                "argv": argv,
            }
        )
        for run_index in range(1, 4):
            invocations.append(
                {
                    "invocation_id": f"{probe_id}-MEASURED-{run_index:02d}",
                    "probe_id": probe_id,
                    "run_class": "MEASURED",
                    "run_index": run_index,
                    "runtime_entrypoint": "llama-cli",
                    "runtime_executable_sha256": LLAMA_CLI_EXECUTABLE_SHA256,
                    "argv": argv,
                }
            )
    return invocations


def compute_e004_llama_adapter_manifest_sha256(manifest: Mapping[str, Any]) -> str:
    projection = dict(manifest)
    projection.pop("adapter_sha256", None)
    return compute_canonical_sha256(projection)


def build_e004_llama_adapter_manifest(
    asset_set: Any,
    *,
    candidate_id: str,
    upstream_revision: str,
    model_path: str,
    payload_directory: str,
) -> dict[str, Any]:
    """Build a complete non-executing adapter manifest for one GGUF candidate."""
    errors = validate_research_component_evaluation_asset_set(asset_set)
    if errors or not isinstance(asset_set, dict):
        raise ValueError("evaluation asset set is not canonically valid")
    if asset_set.get("asset_set_sha256") != RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256:
        raise ValueError("evaluation asset set identity mismatch")

    pair = (candidate_id, upstream_revision)
    if pair not in _LLAMA_CANDIDATES:
        raise ValueError("candidate is not assigned to the pinned llama.cpp GGUF route")
    model = _safe_path(model_path, "model_path")
    payload_dir = _safe_path(payload_directory, "payload_directory").rstrip("/")

    records = asset_set.get("asset_records")
    if not isinstance(records, list) or len(records) != 7:
        raise ValueError("frozen asset set must contain exactly seven records")

    operations: list[dict[str, Any]] = []
    for raw_asset in sorted(records, key=lambda item: str(item.get("asset_id", ""))):
        asset = _require_frozen_asset(raw_asset)
        asset_id = str(asset.get("asset_id"))
        if asset.get("asset_kind") == MULTIPLE_CHOICE_ASSET_KIND:
            payload_sha = compute_llama_multiple_choice_payload_sha256(asset)
            payload_path = f"{payload_dir}/{asset_id}.mcbin"
            operations.append(
                {
                    "operation_id": f"{asset_id}-MC-SCORE",
                    "operation_kind": "MULTIPLE_CHOICE_SCORE",
                    "asset_id": asset_id,
                    "asset_sha256": asset.get("asset_sha256"),
                    "scoring_method": MULTIPLE_CHOICE_SCORING_METHOD,
                    "input_format": LLAMA_MULTIPLE_CHOICE_INPUT_FORMAT,
                    "input_sha256": payload_sha,
                    "expected_output_kind": "ASSET_ACCURACY_RECORD_V1",
                    "invocations": [
                        {
                            "invocation_id": f"{asset_id}-MC-SCORE-01",
                            "probe_id": None,
                            "run_class": "SCORING",
                            "run_index": 1,
                            "runtime_entrypoint": "llama-perplexity",
                            "runtime_executable_sha256": LLAMA_PERPLEXITY_EXECUTABLE_SHA256,
                            "argv": build_llama_multiple_choice_argv(
                                model_path=model,
                                payload_path=payload_path,
                            ),
                        }
                    ],
                }
            )
        elif asset.get("asset_kind") == RESOURCE_ASSET_KIND:
            operations.append(
                {
                    "operation_id": f"{asset_id}-RESOURCE",
                    "operation_kind": "RESOURCE_MEASUREMENT",
                    "asset_id": asset_id,
                    "asset_sha256": asset.get("asset_sha256"),
                    "scoring_method": RESOURCE_SCORING_METHOD,
                    "input_format": "FROZEN_RESOURCE_PROBE_RECORDS_V1",
                    "input_sha256": asset.get("asset_sha256"),
                    "expected_output_kind": "RESOURCE_MEASUREMENT_RECORD_V1",
                    "invocations": build_llama_resource_invocations(
                        asset, model_path=model
                    ),
                }
            )
        else:
            raise ValueError("unsupported frozen evaluation asset kind")

    manifest: dict[str, Any] = {
        "schema_version": "1",
        "adapter_id": f"SP007-RO-001-LLAMA-ADAPTER::{candidate_id}@{upstream_revision}",
        "adapter_sha256": "0" * 64,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "protocol_id": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
        "protocol_sha256": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
        "evaluation_asset_set_sha256": RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
        "candidate_id": candidate_id,
        "upstream_revision": upstream_revision,
        "candidate_role": "PRIMARY",
        "backend_family": "LLAMA_CPP_GGUF",
        "backend_source_revision": LLAMA_CPP_SOURCE_REVISION,
        "runtime_artifact_sha256": LLAMA_RUNTIME_ARCHIVE_SHA256,
        "build_toolchain_identity": LLAMA_BUILD_TOOLCHAIN_IDENTITY,
        "operations": operations,
        "execution_performed": False,
        "authorized_spend_usd": 0,
    }
    manifest["adapter_sha256"] = compute_e004_llama_adapter_manifest_sha256(manifest)
    return manifest


def validate_e004_llama_adapter_manifest(manifest: Any) -> list[str]:
    """Validate a built llama adapter manifest without creating authority."""
    if not isinstance(manifest, dict):
        return ["E004LlamaAdapterManifest: expected object"]
    errors: list[str] = []
    pair = (manifest.get("candidate_id"), manifest.get("upstream_revision"))
    if pair not in _LLAMA_CANDIDATES:
        errors.append("E004LlamaAdapterManifest: candidate route mismatch")
    expected = {
        "schema_version": "1",
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "protocol_id": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
        "protocol_sha256": RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256,
        "evaluation_asset_set_sha256": RESEARCH_COMPONENT_EVALUATION_ASSET_SET_SHA256,
        "candidate_role": "PRIMARY",
        "backend_family": "LLAMA_CPP_GGUF",
        "backend_source_revision": LLAMA_CPP_SOURCE_REVISION,
        "runtime_artifact_sha256": LLAMA_RUNTIME_ARCHIVE_SHA256,
        "build_toolchain_identity": LLAMA_BUILD_TOOLCHAIN_IDENTITY,
        "execution_performed": False,
        "authorized_spend_usd": 0,
    }
    for field, value in expected.items():
        if manifest.get(field) != value:
            errors.append(f"E004LlamaAdapterManifest: {field} mismatch")
    if not is_canonical_sha256(manifest.get("adapter_sha256")):
        errors.append("E004LlamaAdapterManifest: adapter_sha256 must be canonical")
    elif manifest.get("adapter_sha256") != compute_e004_llama_adapter_manifest_sha256(manifest):
        errors.append("E004LlamaAdapterManifest: adapter_sha256 mismatch")

    operations = manifest.get("operations")
    if not isinstance(operations, list) or len(operations) != 7:
        errors.append("E004LlamaAdapterManifest: exactly seven operations required")
        return sorted(set(errors))
    asset_ids = [op.get("asset_id") for op in operations if isinstance(op, dict)]
    if set(asset_ids) != set(FROZEN_EVALUATION_ASSETS):
        errors.append("E004LlamaAdapterManifest: exact frozen asset coverage required")
    for operation in operations:
        if not isinstance(operation, dict):
            errors.append("E004LlamaAdapterManifest: operation must be an object")
            continue
        asset_id = str(operation.get("asset_id"))
        expected_asset = FROZEN_EVALUATION_ASSETS.get(asset_id)
        if expected_asset is None or operation.get("asset_sha256") != expected_asset[0]:
            errors.append(f"E004LlamaAdapterManifest: {asset_id} identity mismatch")
            continue
        invocations = operation.get("invocations")
        expected_count = 32 if expected_asset[1] == RESOURCE_ASSET_KIND else 1
        if not isinstance(invocations, list) or len(invocations) != expected_count:
            errors.append(
                f"E004LlamaAdapterManifest: {asset_id} invocation count must equal {expected_count}"
            )
            continue
        for invocation in invocations:
            if not isinstance(invocation, dict):
                errors.append(f"E004LlamaAdapterManifest: {asset_id} invocation malformed")
                continue
            executable = invocation.get("runtime_executable_sha256")
            argv = invocation.get("argv")
            entrypoint = invocation.get("runtime_entrypoint")
            if not is_canonical_sha256(executable):
                errors.append(f"E004LlamaAdapterManifest: {asset_id} executable sha invalid")
            if not isinstance(argv, list) or not argv or argv[0] != entrypoint:
                errors.append(f"E004LlamaAdapterManifest: {asset_id} argv mismatch")
            if isinstance(argv, list) and "--offline" not in argv:
                errors.append(f"E004LlamaAdapterManifest: {asset_id} offline flag required")
    return sorted(set(errors))
