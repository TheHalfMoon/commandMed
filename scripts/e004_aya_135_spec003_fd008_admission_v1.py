#!/usr/bin/env python3
"""Evaluate exact Aya-135 FD-008 categorical evidence with canonical Spec 003.

This adapter consumes repository-safe hash/categorical evidence only. It never
reads Aya raw text, never accepts caller-controlled admission state, and delegates
all admission decisions to ``evaluate_lineage_admission`` from the canonical
Spec 003 evaluator.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
from pathlib import Path
from typing import Any

from src.commandmed.eval_contract.lineage import (
    evaluate_lineage_admission,
    validate_lineage_contract,
    validate_lineage_record,
)

SOURCE_REPOSITORY = "CohereLabs/aya_dataset"
SOURCE_REVISION = "f9ea04583f02a8f86404ff6c58bf75fe637df8a2"
SOURCE_FILE = "data/train-00000-of-00001.parquet"
SOURCE_FILE_SHA256 = "51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06"
EXPECTED_COUNT = 135
EXPECTED_RECORD_ID_SET_SHA256 = "d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83"
EXPECTED_CONTENT_SET_SHA256 = "ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64"
EXPECTED_MANIFEST_CANONICAL_SHA256 = "dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99"
DETERMINISTIC_METHOD_ID = "AYA_135_LOCAL_DETERMINISTIC_RECORD_EVIDENCE_V1"
EXPECTED_DETERMINISTIC_OUTPUT_SHA256 = "129688b220a75773a7709c656a2aa313f2aed770541dc62a39b3351848beb07d"
EXPECTED_PROJECTION_FILE_SHA256 = "1c696862705e50f10b8621f425389f8f9db0122ef8cc3027e46d50d6835430e7"
EXPECTED_CONTAMINATION_METHOD_ID = "AYA_135_PUBLIC_CANONICAL_TEXT_13_TOKEN_EXACT_V1"
EXPECTED_CONTAMINATION_RESULTS_SHA256 = "f584d937990972bc7101da95c0edba52e4537ef7f80f9afac10bbc55be102857"
EVALUATOR_SOURCE_COMMIT = "7fa0b8d4baee9e6ef5f2a0ca30aaf0bd8199c6fc"
EVALUATOR_LINEAGE_BLOB_SHA = "5d7a5b6a8b48b2b5a7afea35ed18ceb1c9fe6425"
LINEAGE_CONTRACT_BLOB_SHA = "692de9b32271031b0f1dd9cc6edc98bc44b580b5"
ARTIFACT_ID = "e004-aya-135-spec003-post-fd008-admission-v1"
RIGHTS_EVIDENCE_URI = (
    "https://huggingface.co/datasets/CohereLabs/aya_dataset/blob/"
    f"{SOURCE_REVISION}/README.md"
)
SOURCE_EVIDENCE_URI = (
    "https://huggingface.co/datasets/CohereLabs/aya_dataset/blob/"
    f"{SOURCE_REVISION}/{SOURCE_FILE}"
)
SOURCE_URI = f"https://huggingface.co/datasets/CohereLabs/aya_dataset/tree/{SOURCE_REVISION}"


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def set_root(values: list[str]) -> str:
    return hashlib.sha256(("\n".join(sorted(values)) + "\n").encode("ascii")).hexdigest()


def _require_id_list(projection: dict[str, Any], key: str) -> list[str]:
    value = projection.get(key)
    if not isinstance(value, list) or any(
        not isinstance(item, str) or len(item) != 64 for item in value
    ):
        raise SystemExit(f"INVALID_{key.upper()}")
    if len(value) != len(set(value)):
        raise SystemExit(f"DUPLICATE_{key.upper()}")
    return sorted(value)


def load_projection(path: Path) -> dict[str, Any]:
    if file_sha256(path) != EXPECTED_PROJECTION_FILE_SHA256:
        raise SystemExit("DETERMINISTIC_PROJECTION_FILE_SHA256_MISMATCH")
    projection = json.loads(path.read_text(encoding="utf-8"))
    expected_scalars = {
        "artifact_id": "e004-aya-135-deterministic-admission-projection-v1",
        "schema_version": "1",
        "method_id": DETERMINISTIC_METHOD_ID,
        "deterministic_evidence_output_sha256": EXPECTED_DETERMINISTIC_OUTPUT_SHA256,
        "source_file_sha256": SOURCE_FILE_SHA256,
        "candidate_count": EXPECTED_COUNT,
        "candidate_manifest_canonical_sha256": EXPECTED_MANIFEST_CANONICAL_SHA256,
        "candidate_record_id_set_sha256": EXPECTED_RECORD_ID_SET_SHA256,
        "candidate_content_sha256_set_sha256": EXPECTED_CONTENT_SET_SHA256,
        "privacy_no_phi_known_count": 118,
        "scope_pass_count": EXPECTED_COUNT,
        "source_risk_clear_count": 43,
        "source_risk_unresolved_count": 92,
        "external_ai_or_model_used": False,
        "external_provider_used": False,
        "network_access_performed": False,
        "raw_text_persisted": False,
        "user_id_read": False,
    }
    for key, expected in expected_scalars.items():
        if projection.get(key) != expected:
            raise SystemExit(f"PROJECTION_{key.upper()}_MISMATCH")

    supported = _require_id_list(projection, "rights_supported_candidate_ids")
    unresolved = _require_id_list(projection, "rights_unresolved_candidate_ids")
    privacy_unresolved = _require_id_list(projection, "privacy_unresolved_candidate_ids")
    privacy_restricted = _require_id_list(projection, "privacy_restricted_or_phi_candidate_ids")
    scope_fail = _require_id_list(projection, "scope_fail_candidate_ids")
    scope_unresolved = _require_id_list(projection, "scope_unresolved_candidate_ids")

    supported_set = set(supported)
    unresolved_set = set(unresolved)
    if supported_set & unresolved_set:
        raise SystemExit("RIGHTS_STATE_SETS_OVERLAP")
    all_ids = sorted(supported_set | unresolved_set)
    if len(all_ids) != EXPECTED_COUNT or set_root(all_ids) != EXPECTED_RECORD_ID_SET_SHA256:
        raise SystemExit("PROJECTION_CANDIDATE_SET_MISMATCH")
    if len(supported) != 43 or len(unresolved) != 92:
        raise SystemExit("PROJECTION_RIGHTS_COUNTS_MISMATCH")
    if len(privacy_unresolved) != 17 or privacy_restricted:
        raise SystemExit("PROJECTION_PRIVACY_COUNTS_MISMATCH")
    if not set(privacy_unresolved).issubset(set(all_ids)):
        raise SystemExit("PRIVACY_IDS_OUTSIDE_CANDIDATE_SET")
    if scope_fail or scope_unresolved:
        raise SystemExit("SCOPE_NOT_FULLY_PASS")
    if not supported_set.isdisjoint(set(privacy_unresolved)):
        raise SystemExit("SUPPORTED_RIGHTS_PRIVACY_UNRESOLVED_INTERSECTION")

    expected_roots = {
        "rights_supported_candidate_ids_set_sha256": "417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4",
        "rights_unresolved_candidate_ids_set_sha256": "d68dc1bca8cc62fdffae22abc15c82ced31dcad262aebaafe7234d0b2c05ff95",
        "privacy_unresolved_candidate_ids_set_sha256": "12ca6f8d475395e36aab812b17f5d2e8fe86144597eab5c4f8720b56223fc85f",
    }
    roots_to_values = {
        "rights_supported_candidate_ids_set_sha256": supported,
        "rights_unresolved_candidate_ids_set_sha256": unresolved,
        "privacy_unresolved_candidate_ids_set_sha256": privacy_unresolved,
    }
    for key, expected in expected_roots.items():
        if projection.get(key) != expected or set_root(roots_to_values[key]) != expected:
            raise SystemExit(f"PROJECTION_{key.upper()}_MISMATCH")
    return projection


def verify_contamination_evidence(path: Path) -> None:
    evidence = json.loads(path.read_text(encoding="utf-8"))
    checks = {
        "candidate_count": EXPECTED_COUNT,
        "candidate_manifest_canonical_sha256": EXPECTED_MANIFEST_CANONICAL_SHA256,
        "candidate_record_id_set_sha256": EXPECTED_RECORD_ID_SET_SHA256,
        "candidate_content_sha256_set_sha256": EXPECTED_CONTENT_SET_SHA256,
        "source_file_sha256": SOURCE_FILE_SHA256,
        "contamination_method_id": EXPECTED_CONTAMINATION_METHOD_ID,
        "contamination_results_sha256": EXPECTED_CONTAMINATION_RESULTS_SHA256,
        "purpose": "TRAIN",
        "quarantine_state": "NOT_QUARANTINED",
    }
    for key, expected in checks.items():
        if evidence.get(key) != expected:
            raise SystemExit(f"CONTAMINATION_EVIDENCE_{key.upper()}_MISMATCH")
    if evidence.get("contamination_state_counts") != {"ASSESSED_CLEAN": EXPECTED_COUNT}:
        raise SystemExit("CONTAMINATION_STATE_COUNTS_MISMATCH")
    if evidence.get("quarantine_conflict_observed") is not False:
        raise SystemExit("QUARANTINE_CONFLICT")
    if evidence.get("private_gold_used") is not False:
        raise SystemExit("PRIVATE_GOLD_USE_CONFLICT")
    if evidence.get("public_external_eval_used_as_training_source") is not False:
        raise SystemExit("PUBLIC_EXTERNAL_EVAL_TRAINING_CONFLICT")


def build_lineage_record(candidate_id: str, projection: dict[str, Any]) -> dict[str, Any]:
    rights_supported = set(projection["rights_supported_candidate_ids"])
    privacy_unresolved = set(projection["privacy_unresolved_candidate_ids"])
    privacy_restricted = set(projection["privacy_restricted_or_phi_candidate_ids"])

    if candidate_id in privacy_restricted:
        privacy_state = "RESTRICTED_OR_PHI"
    elif candidate_id in privacy_unresolved:
        privacy_state = "UNRESOLVED"
    else:
        privacy_state = "NO_PHI_KNOWN"

    rights_state = "SUPPORTED" if candidate_id in rights_supported else "UNRESOLVED"
    return {
        "asset_id": f"aya-135:{candidate_id}",
        "asset_class": "DATASET_OR_CORPUS",
        "canonical_name": f"Aya exact candidate {candidate_id}",
        "record_version": "1",
        "source_identifier": f"{SOURCE_REPOSITORY}:{SOURCE_FILE}:{candidate_id}",
        "source_uri": SOURCE_URI,
        "source_revision": SOURCE_REVISION,
        "source_verification_status": "VERIFIED",
        "source_evidence_uri": SOURCE_EVIDENCE_URI,
        "declared_use": "TRAINING_OR_ADAPTATION",
        "access_class": "PUBLIC",
        "rights_state": rights_state,
        "rights_evidence_uri": RIGHTS_EVIDENCE_URI,
        "artifact_binding_state": "IMMUTABLE_REVISION_LOCATOR",
        "artifact_locator": f"{SOURCE_FILE}#candidate_record_id={candidate_id}",
        "phi_privacy_state": privacy_state,
        "purpose": "TRAIN",
        "quarantine_state": "NOT_QUARANTINED",
        "contamination_state": "ASSESSED_CLEAN",
        "origin_type": "ORIGINAL",
        "spdx_license_expression": "Apache-2.0",
    }


def evaluate(
    projection_path: Path,
    contamination_evidence_path: Path,
    contract_path: Path,
) -> dict[str, Any]:
    projection = load_projection(projection_path)
    verify_contamination_evidence(contamination_evidence_path)
    contract = json.loads(contract_path.read_text(encoding="utf-8"))
    contract_errors = validate_lineage_contract(contract)
    if contract_errors:
        raise SystemExit("SPEC003_CONTRACT_INVALID")

    candidate_ids = sorted(
        set(projection["rights_supported_candidate_ids"])
        | set(projection["rights_unresolved_candidate_ids"])
    )
    results: list[dict[str, Any]] = []
    state_counts: collections.Counter[str] = collections.Counter()
    reason_counts: collections.Counter[str] = collections.Counter()
    validation_error_count = 0

    for candidate_id in candidate_ids:
        lineage_record = build_lineage_record(candidate_id, projection)
        errors = validate_lineage_record(lineage_record, contract)
        if errors:
            validation_error_count += 1
            raise SystemExit(f"SPEC003_RECORD_INVALID:{candidate_id}")
        admission = evaluate_lineage_admission(lineage_record, contract)
        state = str(admission["state"])
        reasons = [str(item) for item in admission["reason_codes"]]
        state_counts[state] += 1
        reason_counts.update(reasons)
        results.append(
            {
                "candidate_record_id": candidate_id,
                "contract_sha256": admission["contract_sha256"],
                "record_sha256": admission["record_sha256"],
                "reason_codes": reasons,
                "state": state,
            }
        )

    if len(results) != EXPECTED_COUNT:
        raise SystemExit("SPEC003_RESULT_COUNT_MISMATCH")
    return {
        "artifact_id": ARTIFACT_ID,
        "candidate_count": EXPECTED_COUNT,
        "candidate_manifest_canonical_sha256": EXPECTED_MANIFEST_CANONICAL_SHA256,
        "candidate_record_id_set_sha256": EXPECTED_RECORD_ID_SET_SHA256,
        "contamination_method_id": EXPECTED_CONTAMINATION_METHOD_ID,
        "contamination_results_sha256": EXPECTED_CONTAMINATION_RESULTS_SHA256,
        "deterministic_evidence_method_id": DETERMINISTIC_METHOD_ID,
        "deterministic_evidence_output_sha256": EXPECTED_DETERMINISTIC_OUTPUT_SHA256,
        "deterministic_projection_sha256": EXPECTED_PROJECTION_FILE_SHA256,
        "evaluator_lineage_blob_sha": EVALUATOR_LINEAGE_BLOB_SHA,
        "evaluator_source_commit": EVALUATOR_SOURCE_COMMIT,
        "lineage_contract_blob_sha": LINEAGE_CONTRACT_BLOB_SHA,
        "reason_counts": dict(sorted(reason_counts.items())),
        "results": results,
        "schema_version": "1",
        "state_counts": dict(sorted(state_counts.items())),
        "validation_error_count": validation_error_count,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--projection", required=True, type=Path)
    parser.add_argument("--contamination-evidence", required=True, type=Path)
    parser.add_argument("--contract", required=True, type=Path)
    parser.add_argument("--out", required=True, type=Path)
    args = parser.parse_args()

    result = evaluate(args.projection, args.contamination_evidence, args.contract)
    args.out.write_bytes(canonical_bytes(result) + b"\n")
    summary = {
        "artifact_id": ARTIFACT_ID,
        "candidate_count": result["candidate_count"],
        "output_sha256": file_sha256(args.out),
        "reason_counts": result["reason_counts"],
        "state_counts": result["state_counts"],
        "validation_error_count": result["validation_error_count"],
    }
    print(json.dumps(summary, sort_keys=True, separators=(",", ":")))


if __name__ == "__main__":
    main()
