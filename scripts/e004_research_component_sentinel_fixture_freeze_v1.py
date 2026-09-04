#!/usr/bin/env python3
"""Verify and freeze the exact E004 SP007-RO-001 seven-sentinel subject.

This script is offline and deterministic. It validates repository metadata only;
it never loads model weights, opens devices, accesses credentials, executes
inference, or starts training.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.research_scope import (
    RESEARCH_COMPONENT_REQUIRED_GUARDS,
    validate_research_component_sentinel_fixture,
)

EXPECTED_RECORD_COUNT = 7
EXPECTED_SCOPE_ID = "SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1"
EXPECTED_SET_SHA256 = "5a2bd28b391010c9575c99654899cd442fea8d94cbb4176045b654c940fa2fd3"
EXPECTED_FIXTURE_SHA256_SET_SHA256 = (
    "b65b36689cf2006bad8b446536d50ccd3f3440a4b244c044a1b26409aea0fef2"
)
EXPECTED_AUTHORITY = (
    "SENTINEL_FIXTURE_CONSTRUCTION_AUTHORITY="
    "AUTHORIZED_EXACT_PREDECLARED_SP007_RO_001_SENTINEL_7_ONLY"
)
EXPECTED_FREEZE_AUTHORITY = (
    "SENTINEL_FIXTURE_FREEZE_AUTHORITY="
    "AUTHORIZED_EXACT_PREDECLARED_SP007_RO_001_SENTINEL_7_ONLY"
)
EXPECTED_DECISION = (
    "FOUNDER_SENTINEL_FIXTURE_FREEZE_DECISION="
    "E004_SENTINEL_FIXTURE_FREEZE_DECISION_B"
)
EXPECTED_FIXTURE_HASHES = {
    "SP007-RO-001-SENTINEL-001": "6ae5dcdfe4ab75b55cee81439f26242ed89c4867fb5fca125de1cf7b713ce4d4",
    "SP007-RO-001-SENTINEL-002": "0104be64bebbcd08dbf27971cc953d3abeb9ca07cc84dd7432e6d30f9646f518",
    "SP007-RO-001-SENTINEL-003": "7b6653af5e0260ce01b42dca82be476b1cff1d6ba7c46a0ea82a7b492d45606b",
    "SP007-RO-001-SENTINEL-004": "136d3520fe3fc9569615be66072e4cb634fe91c15a56b0af21915dba2cff94b7",
    "SP007-RO-001-SENTINEL-005": "2c3a5519c4bb6cd79f8e2f8a8d95fe05bf3e90b520ab80f7f6a43b4f6f294d5e",
    "SP007-RO-001-SENTINEL-006": "eb7557b946f7c55c4e99a69783aad015f04e21026c1564ba4098f697d1ecc825",
    "SP007-RO-001-SENTINEL-007": "83628c0c1ef3cd5c89b77b4c88756784b24fc0647f76d97b355bd06363ae15e4",
}


def _reject_duplicate_keys(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    obj: dict[str, Any] = {}
    for key, value in pairs:
        if key in obj:
            raise ValueError(f"duplicate JSON key: {key}")
        obj[key] = value
    return obj


def load_json_strict(path: Path) -> Any:
    return json.loads(
        path.read_text(encoding="utf-8"),
        object_pairs_hook=_reject_duplicate_keys,
    )


def verify_authority(decision_path: Path) -> list[str]:
    text = decision_path.read_text(encoding="utf-8")
    errors: list[str] = []
    for required in (
        EXPECTED_DECISION,
        EXPECTED_AUTHORITY,
        EXPECTED_FREEZE_AUTHORITY,
        "SENTINEL_FIXTURE_RECORD_COUNT=7",
        f"SENTINEL_FIXTURE_SET_SHA256={EXPECTED_SET_SHA256}",
        f"SENTINEL_FIXTURE_SHA256_SET_SHA256={EXPECTED_FIXTURE_SHA256_SET_SHA256}",
        "SENTINEL_EXECUTION_AUTHORITY_EXPANSION=NONE",
        "DATASET_SNAPSHOT_AUTHORITY=NONE",
        "CURRENT_AUTHORIZED_SPEND_USD=0",
    ):
        if required not in text.splitlines():
            errors.append(f"authority line missing: {required}")
    return errors


def validate_fixture_set(value: Any) -> list[str]:
    errors: list[str] = []
    if not isinstance(value, list):
        return ["fixture set must be a JSON array"]
    if len(value) != EXPECTED_RECORD_COUNT:
        errors.append(f"fixture count must equal {EXPECTED_RECORD_COUNT}")

    ids: list[str] = []
    guards: list[str] = []
    hashes: list[str] = []
    for index, fixture in enumerate(value):
        if not isinstance(fixture, dict):
            errors.append(f"fixture[{index}] must be an object")
            continue
        fixture_errors = validate_research_component_sentinel_fixture(fixture)
        errors.extend(f"fixture[{index}]: {error}" for error in fixture_errors)

        fixture_id = fixture.get("fixture_id")
        guard_id = fixture.get("guard_id")
        fixture_sha = fixture.get("fixture_sha256")
        ids.append(str(fixture_id))
        guards.append(str(guard_id))
        hashes.append(str(fixture_sha))

        expected_hash = EXPECTED_FIXTURE_HASHES.get(str(fixture_id))
        if expected_hash is None:
            errors.append(f"fixture[{index}]: unauthorized fixture_id {fixture_id!r}")
        elif fixture_sha != expected_hash:
            errors.append(f"fixture[{index}]: fixture_sha256 differs from frozen identity")
        if fixture.get("scope_id") != EXPECTED_SCOPE_ID:
            errors.append(f"fixture[{index}]: scope_id differs from frozen scope")
        if fixture.get("optimization_feedback_allowed") is not False:
            errors.append(f"fixture[{index}]: optimization feedback must remain disabled")

    if len(ids) != len(set(ids)):
        errors.append("fixture IDs must be unique")
    if len(guards) != len(set(guards)):
        errors.append("guard IDs must be unique")
    if len(hashes) != len(set(hashes)):
        errors.append("fixture hashes must be unique")
    if set(ids) != set(EXPECTED_FIXTURE_HASHES):
        errors.append("fixture ID set differs from exact Founder-authorized subject")
    if set(guards) != set(RESEARCH_COMPONENT_REQUIRED_GUARDS):
        errors.append("guard set differs from canonical required guard set")

    if all(isinstance(item, dict) for item in value):
        sorted_records = sorted(value, key=lambda item: str(item.get("guard_id", "")))
        actual_set_sha = compute_canonical_sha256(sorted_records)
        if actual_set_sha != EXPECTED_SET_SHA256:
            errors.append(f"sentinel set SHA-256 mismatch: {actual_set_sha}")

        actual_hash_set_sha = compute_canonical_sha256(sorted(hashes))
        if actual_hash_set_sha != EXPECTED_FIXTURE_SHA256_SET_SHA256:
            errors.append(
                "sentinel fixture SHA-256 set mismatch: " + actual_hash_set_sha
            )
    return errors


def verify(fixture_path: Path, decision_path: Path) -> list[str]:
    errors = verify_authority(decision_path)
    try:
        fixture_set = load_json_strict(fixture_path)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        return [*errors, f"fixture JSON parse failed: {exc}"]
    errors.extend(validate_fixture_set(fixture_set))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--fixture-set", type=Path, required=True)
    parser.add_argument("--decision", type=Path, required=True)
    args = parser.parse_args()

    errors = verify(args.fixture_set, args.decision)
    if errors:
        for error in errors:
            print(f"ERROR={error}")
        return 1

    fixture_set = load_json_strict(args.fixture_set)
    sorted_records = sorted(fixture_set, key=lambda item: item["guard_id"])
    print(f"SENTINEL_FIXTURE_RECORD_COUNT={len(sorted_records)}")
    print(f"SENTINEL_FIXTURE_SET_SHA256={compute_canonical_sha256(sorted_records)}")
    print(
        "SENTINEL_FIXTURE_SHA256_SET_SHA256="
        + compute_canonical_sha256(sorted(item["fixture_sha256"] for item in sorted_records))
    )
    print("SENTINEL_FIXTURE_SCHEMA_VALIDATION=PASS")
    print("SENTINEL_MODEL_INFERENCE_PERFORMED=NO")
    print("SENTINEL_GUARD_PASS_CREATED=NO")
    print("DATASET_SNAPSHOT_AUTHORITY=NONE")
    print("TRAINING_AUTHORITY=NONE")
    print("CURRENT_AUTHORIZED_SPEND_USD=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
