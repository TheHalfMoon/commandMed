"""Deterministic non-executing candidate-artifact bundle bindings for Spec 007.

This module validates canonical file-manifest identities only. It does not load
model weights, execute inference, inspect devices, invoke runtimes, select a
winner, access protected data, grant A15, start training, or grant spend.
"""

from __future__ import annotations

from pathlib import PurePosixPath
from typing import Any, Mapping

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.foundation import is_canonical_sha256, validate_closed_object
from src.commandmed.spec007.research_execution import PRIMARY_PACKAGE_HARD_CAP_BYTES
from src.commandmed.spec007.research_scope import RESEARCH_COMPONENT_SCOPE_ID
from src.commandmed.spec007.research_tournament import (
    CONTROL_CANDIDATE,
    PRIMARY_CANDIDATES,
    RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID,
)

RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256 = (
    "1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8"
)
CANDIDATE_ARTIFACT_BUNDLE_SET_ID = "SP007_RO_001_CANDIDATE_ARTIFACT_BUNDLE_SET_V1"
CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256 = (
    "ee97fe0751743cc0d3a564b8f91add3c336267f08f2da86bf125dd7333db83fd"
)
CANDIDATE_ARTIFACT_BUNDLE_IDENTITY_SEMANTICS = (
    "CANONICAL_FILE_MANIFEST_IDENTITY_V1"
)
COMPLETE_BUNDLE_SEMANTICS = "CANONICAL_FILE_MANIFEST_SHA256_V1"
MULTI_FILE_MODEL_ARTIFACT_SEMANTICS = (
    "CANONICAL_WEIGHT_SHARD_MANIFEST_SHA256_V1"
)

_ALLOWED_ARTIFACT_FORMATS = frozenset({"GGUF", "SAFETENSORS"})
_ALLOWED_MODEL_ARTIFACT_IDENTITY_KINDS = frozenset(
    {"SINGLE_FILE_SHA256", MULTI_FILE_MODEL_ARTIFACT_SEMANTICS}
)
_ALLOWED_FILE_PURPOSES = frozenset(
    {
        "DOCUMENTATION",
        "GENERATION_CONFIG",
        "MODEL_CONFIG",
        "MODEL_INDEX",
        "MODEL_WEIGHT",
        "MODEL_WEIGHT_SHARD",
        "TOKENIZER_ASSET",
        "TOKENIZER_CONFIG",
    }
)

_BUNDLE_SET_FIELDS = (
    "schema_version",
    "bundle_set_id",
    "bundle_set_sha256",
    "scope_id",
    "protocol_id",
    "protocol_sha256",
    "identity_semantics",
    "candidate_bundles",
)
_CANDIDATE_BUNDLE_FIELDS = (
    "candidate_id",
    "upstream_revision",
    "candidate_role",
    "winner_eligible",
    "artifact_format",
    "artifact_access_state",
    "model_artifact_identity_kind",
    "model_artifact_sha256",
    "model_artifact_bytes",
    "tokenizer_config_sha256",
    "complete_bundle_semantics",
    "complete_bundle_sha256",
    "complete_bundle_bytes",
    "files",
)
_FILE_FIELDS = (
    "path",
    "bytes",
    "sha256",
    "purpose",
    "source_repository",
    "source_revision",
)


def _nonempty(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip()) and "\x00" not in value


def _positive_int(value: Any) -> bool:
    return isinstance(value, int) and not isinstance(value, bool) and value > 0


def _self_hash(record: Mapping[str, Any], identity_field: str) -> str:
    projection = dict(record)
    projection.pop(identity_field, None)
    return compute_canonical_sha256(projection)


def compute_candidate_artifact_bundle_sha256(bundle: Mapping[str, Any]) -> str:
    """Compute the canonical file-manifest identity for one candidate bundle."""
    return _self_hash(bundle, "complete_bundle_sha256")


def compute_candidate_artifact_bundle_set_sha256(bundle_set: Mapping[str, Any]) -> str:
    """Compute the canonical identity for the complete four-candidate bundle set."""
    return _self_hash(bundle_set, "bundle_set_sha256")


def compute_multi_file_model_artifact_sha256(files: list[Mapping[str, Any]]) -> str:
    """Compute a canonical model-artifact identity over exact weight shards only."""
    weight_files = [
        {
            "path": item["path"],
            "bytes": item["bytes"],
            "sha256": item["sha256"],
        }
        for item in files
        if item.get("purpose") == "MODEL_WEIGHT_SHARD"
    ]
    return compute_canonical_sha256(
        {
            "schema_version": "1",
            "identity_semantics": MULTI_FILE_MODEL_ARTIFACT_SEMANTICS,
            "files": weight_files,
        }
    )


def _validate_file_record(value: Any, prefix: str) -> list[str]:
    errors = validate_closed_object(value, required_fields=_FILE_FIELDS, field=prefix)
    if errors or not isinstance(value, dict):
        return errors

    path = value.get("path")
    if not _nonempty(path):
        errors.append(f"{prefix}: path must be a non-empty POSIX relative path")
    else:
        posix = PurePosixPath(path)
        if posix.is_absolute() or ".." in posix.parts or "\\" in path:
            errors.append(f"{prefix}: path must be a safe POSIX relative path")
        if path != posix.as_posix():
            errors.append(f"{prefix}: path must use canonical POSIX spelling")

    if not _positive_int(value.get("bytes")):
        errors.append(f"{prefix}: bytes must be a positive integer")
    if not is_canonical_sha256(value.get("sha256")):
        errors.append(f"{prefix}: sha256 must be lowercase sha256 hex")
    if value.get("purpose") not in _ALLOWED_FILE_PURPOSES:
        errors.append(f"{prefix}: purpose is not allowed")
    for field in ("source_repository", "source_revision"):
        if not _nonempty(value.get(field)):
            errors.append(f"{prefix}: {field} must be non-empty")
    revision = value.get("source_revision")
    if isinstance(revision, str) and (
        len(revision) != 40 or any(ch not in "0123456789abcdef" for ch in revision)
    ):
        errors.append(f"{prefix}: source_revision must be an exact lowercase git sha")
    return errors


def _expected_candidates() -> dict[tuple[str, str], tuple[str, bool]]:
    expected = {pair: ("PRIMARY", True) for pair in PRIMARY_CANDIDATES}
    expected[CONTROL_CANDIDATE] = ("CONTROL", False)
    return expected


def _validate_model_artifact_identity(
    bundle: Mapping[str, Any], files: list[Mapping[str, Any]], prefix: str
) -> list[str]:
    errors: list[str] = []
    kind = bundle.get("model_artifact_identity_kind")
    if kind not in _ALLOWED_MODEL_ARTIFACT_IDENTITY_KINDS:
        return [f"{prefix}: model_artifact_identity_kind is not allowed"]

    if kind == "SINGLE_FILE_SHA256":
        model_files = [item for item in files if item.get("purpose") == "MODEL_WEIGHT"]
        if len(model_files) != 1:
            errors.append(
                f"{prefix}: SINGLE_FILE_SHA256 requires exactly one MODEL_WEIGHT file"
            )
            return errors
        model_file = model_files[0]
        if bundle.get("model_artifact_sha256") != model_file.get("sha256"):
            errors.append(f"{prefix}: model_artifact_sha256 mismatch")
        if bundle.get("model_artifact_bytes") != model_file.get("bytes"):
            errors.append(f"{prefix}: model_artifact_bytes mismatch")
        if any(item.get("purpose") == "MODEL_WEIGHT_SHARD" for item in files):
            errors.append(f"{prefix}: single-file model artifact cannot contain weight shards")
        return errors

    shard_files = [item for item in files if item.get("purpose") == "MODEL_WEIGHT_SHARD"]
    if len(shard_files) < 2:
        errors.append(
            f"{prefix}: multi-file model artifact requires at least two weight shards"
        )
        return errors
    if any(item.get("purpose") == "MODEL_WEIGHT" for item in files):
        errors.append(f"{prefix}: multi-file model artifact cannot contain MODEL_WEIGHT")
    expected_sha = compute_multi_file_model_artifact_sha256(files)
    expected_bytes = sum(int(item["bytes"]) for item in shard_files)
    if bundle.get("model_artifact_sha256") != expected_sha:
        errors.append(f"{prefix}: model_artifact_sha256 mismatch")
    if bundle.get("model_artifact_bytes") != expected_bytes:
        errors.append(f"{prefix}: model_artifact_bytes mismatch")
    return errors


def _validate_candidate_bundle(
    bundle: Any,
    *,
    expected: dict[tuple[str, str], tuple[str, bool]],
    seen: set[tuple[str, str]],
    prefix: str,
) -> list[str]:
    errors = validate_closed_object(
        bundle, required_fields=_CANDIDATE_BUNDLE_FIELDS, field=prefix
    )
    if errors or not isinstance(bundle, dict):
        return errors

    pair = (bundle.get("candidate_id"), bundle.get("upstream_revision"))
    expected_role = expected.get(pair)
    if expected_role is None:
        errors.append(f"{prefix}: candidate identity is outside frozen E001 set")
    else:
        if pair in seen:
            errors.append(f"{prefix}: duplicate candidate identity")
        seen.add(pair)
        role, winner_eligible = expected_role
        if bundle.get("candidate_role") != role:
            errors.append(f"{prefix}: candidate_role mismatch")
        if bundle.get("winner_eligible") is not winner_eligible:
            errors.append(f"{prefix}: winner_eligible mismatch")

    if bundle.get("artifact_format") not in _ALLOWED_ARTIFACT_FORMATS:
        errors.append(f"{prefix}: artifact_format is not allowed")
    kind = bundle.get("model_artifact_identity_kind")
    if bundle.get("artifact_format") == "GGUF" and kind != "SINGLE_FILE_SHA256":
        errors.append(f"{prefix}: GGUF model artifact must use SINGLE_FILE_SHA256")
    if kind == MULTI_FILE_MODEL_ARTIFACT_SEMANTICS and bundle.get("artifact_format") != "SAFETENSORS":
        errors.append(f"{prefix}: multi-file model artifact must use SAFETENSORS")
    if bundle.get("artifact_access_state") != "PUBLIC_UNGATED_EXACT_IDENTITY":
        errors.append(f"{prefix}: artifact_access_state must be exact public ungated")
    if bundle.get("complete_bundle_semantics") != COMPLETE_BUNDLE_SEMANTICS:
        errors.append(f"{prefix}: complete_bundle_semantics mismatch")

    for field in (
        "model_artifact_sha256",
        "tokenizer_config_sha256",
        "complete_bundle_sha256",
    ):
        if not is_canonical_sha256(bundle.get(field)):
            errors.append(f"{prefix}: {field} must be lowercase sha256 hex")
    for field in ("model_artifact_bytes", "complete_bundle_bytes"):
        if not _positive_int(bundle.get(field)):
            errors.append(f"{prefix}: {field} must be a positive integer")

    raw_files = bundle.get("files")
    if not isinstance(raw_files, list) or not raw_files:
        errors.append(f"{prefix}: files must be a non-empty list")
        return errors
    file_errors: list[str] = []
    for index, item in enumerate(raw_files):
        file_errors.extend(_validate_file_record(item, f"{prefix}.files[{index}]"))
    errors.extend(file_errors)
    if file_errors or not all(isinstance(item, dict) for item in raw_files):
        return errors

    files = list(raw_files)
    paths = [str(item["path"]) for item in files]
    if paths != sorted(paths):
        errors.append(f"{prefix}: files must be sorted by path")
    if len(paths) != len(set(paths)):
        errors.append(f"{prefix}: file paths must be unique")

    expected_bytes = sum(int(item["bytes"]) for item in files)
    if bundle.get("complete_bundle_bytes") != expected_bytes:
        errors.append(f"{prefix}: complete_bundle_bytes mismatch")

    tokenizer_config_files = [
        item for item in files if item.get("purpose") == "TOKENIZER_CONFIG"
    ]
    if len(tokenizer_config_files) != 1:
        errors.append(f"{prefix}: exactly one TOKENIZER_CONFIG file is required")
    elif bundle.get("tokenizer_config_sha256") != tokenizer_config_files[0].get("sha256"):
        errors.append(f"{prefix}: tokenizer_config_sha256 mismatch")

    errors.extend(_validate_model_artifact_identity(bundle, files, prefix))

    if (
        expected_role is not None
        and expected_role[0] == "PRIMARY"
        and _positive_int(bundle.get("complete_bundle_bytes"))
        and bundle["complete_bundle_bytes"] > PRIMARY_PACKAGE_HARD_CAP_BYTES
    ):
        errors.append(f"{prefix}: primary complete bundle exceeds frozen 700 MiB hard cap")

    claimed = bundle.get("complete_bundle_sha256")
    if is_canonical_sha256(claimed):
        expected_sha = compute_candidate_artifact_bundle_sha256(bundle)
        if claimed != expected_sha:
            errors.append(f"{prefix}: complete_bundle_sha256 mismatch")
    return errors


def validate_candidate_artifact_bundle_set(bundle_set: Any) -> list[str]:
    """Validate the exact four-candidate deterministic artifact-bundle set."""
    prefix = "CandidateArtifactBundleSet"
    errors = validate_closed_object(
        bundle_set, required_fields=_BUNDLE_SET_FIELDS, field=prefix
    )
    if errors or not isinstance(bundle_set, dict):
        return errors

    if bundle_set.get("schema_version") != "1":
        errors.append(f"{prefix}: schema_version must equal '1'")
    if bundle_set.get("bundle_set_id") != CANDIDATE_ARTIFACT_BUNDLE_SET_ID:
        errors.append(f"{prefix}: bundle_set_id mismatch")
    if bundle_set.get("scope_id") != RESEARCH_COMPONENT_SCOPE_ID:
        errors.append(f"{prefix}: scope_id mismatch")
    if bundle_set.get("protocol_id") != RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_ID:
        errors.append(f"{prefix}: protocol_id mismatch")
    if (
        bundle_set.get("protocol_sha256")
        != RESEARCH_COMPONENT_TOURNAMENT_PROTOCOL_SHA256
    ):
        errors.append(f"{prefix}: protocol_sha256 mismatch")
    if (
        bundle_set.get("identity_semantics")
        != CANDIDATE_ARTIFACT_BUNDLE_IDENTITY_SEMANTICS
    ):
        errors.append(f"{prefix}: identity_semantics mismatch")

    bundles = bundle_set.get("candidate_bundles")
    if not isinstance(bundles, list) or len(bundles) != 4:
        errors.append(f"{prefix}: candidate_bundles must contain exactly four records")
        return errors

    expected = _expected_candidates()
    expected_order = list(PRIMARY_CANDIDATES) + [CONTROL_CANDIDATE]
    actual_order = [
        (item.get("candidate_id"), item.get("upstream_revision"))
        for item in bundles
        if isinstance(item, dict)
    ]
    if actual_order != expected_order:
        errors.append(f"{prefix}: candidate_bundles must use frozen deterministic order")

    seen: set[tuple[str, str]] = set()
    for index, bundle in enumerate(bundles):
        errors.extend(
            _validate_candidate_bundle(
                bundle,
                expected=expected,
                seen=seen,
                prefix=f"{prefix}.candidate_bundles[{index}]",
            )
        )
    if seen != set(expected):
        errors.append(f"{prefix}: exact frozen E001 candidate set required")

    claimed = bundle_set.get("bundle_set_sha256")
    if not is_canonical_sha256(claimed):
        errors.append(f"{prefix}: bundle_set_sha256 must be lowercase sha256 hex")
    else:
        expected_sha = compute_candidate_artifact_bundle_set_sha256(bundle_set)
        if claimed != expected_sha:
            errors.append(f"{prefix}: bundle_set_sha256 mismatch")
        if claimed != CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256:
            errors.append(f"{prefix}: bundle_set_sha256 is not the canonical V1 binding")
    return errors
