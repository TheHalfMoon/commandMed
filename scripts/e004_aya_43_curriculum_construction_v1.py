#!/usr/bin/env python3
"""Construct the exact Aya-43 hash-bound curriculum and scope bundle.

This script consumes only the repository-safe candidate manifest and hash/categorical
qualification evidence. It never reads Aya raw prompt/target text.
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable, Mapping

from src.commandmed.spec007.curriculum import (
    compute_curriculum_record_sha256,
    validate_curriculum_record,
)
from src.commandmed.spec007.research_scope import (
    RESEARCH_COMPONENT_SCOPE_ID,
    compute_research_component_content_scope_verification_sha256,
    validate_research_component_content_scope_verification,
)

METHOD_ID = "AYA_43_HASH_BOUND_CURRICULUM_CONSTRUCTION_V1"
AUTHORITY_ID = "E004_FINAL_CURRICULUM_ADMISSION_DECISION_B"
SOURCE_LICENSE_ID = (
    "COHERELABS_AYA_DATASET_"
    "F9EA04583F02A8F86404FF6C58BF75FE637DF8A2_APACHE_2_0"
)
SOURCE_REPOSITORY = "CohereLabs/aya_dataset"
SOURCE_REVISION = "f9ea04583f02a8f86404ff6c58bf75fe637df8a2"
SOURCE_FILE = "data/train-00000-of-00001.parquet"
SOURCE_FILE_SHA256 = "51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06"
FILTER_ID = "AYA_SP007_RO_001_CANDIDATE_FILTER_V1"
EXPECTED_CANDIDATE_COUNT = 135
EXPECTED_MANIFEST_CANONICAL_SHA256 = "dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99"
EXPECTED_MANIFEST_FILE_SHA256 = "bbc7188613f242b428b4ac4cad0297c9dfb31403f6fab146a1a8491a106b2d6e"
EXPECTED_CANDIDATE_RECORD_SET_SHA256 = "d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83"
EXPECTED_CANDIDATE_CONTENT_SET_SHA256 = "ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64"
EXPECTED_PROJECTION_SHA256 = "1c696862705e50f10b8621f425389f8f9db0122ef8cc3027e46d50d6835430e7"
EXPECTED_SPEC003_SHA256 = "a8807085864707ae88966f7a925bfd2a7fd05a0e683d70893a46d3b6d5dbdce4"
EXPECTED_ELIGIBLE_COUNT = 43
EXPECTED_ELIGIBLE_RECORD_SET_SHA256 = "417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4"
EXPECTED_CONTAMINATION_RESULTS_SHA256 = "f584d937990972bc7101da95c0edba52e4537ef7f80f9afac10bbc55be102857"
EXPECTED_MAP_PART_SHA256 = [
    "b6028a65c05d41a251ef8b4a5073d30e8b4048322853a97ad020783cdea79687",
    "59d1445a98f6ac5bfc8d50fb125700fbbd590d61f17b7fd35e1f9d0f428923a3",
    "48310fdf92872e39d0c4f9527dab52e6682b9a117040f2cedef70fcf4eb63ef2",
    "5d58375d6a36eaa1abb5fedda95004d12381e685b09b20c129171ddadf2d4b95",
    "13014dcfab8fc511554c2f4fcd7afa105a84c7ccd43cf449b583627ed0fb1597",
]

LANGUAGE_PROFILE = {
    "eng": {
        "primary_language": "en",
        "authored_language": "en",
        "translation_state": "ORIGINAL",
        "dialect_or_register": "GENERAL",
        "code_switch_state": "NOT_CLASSIFIED",
        "transliteration_state": "NOT_CLASSIFIED",
        "terminology_normalization_id": None,
        "qualified_review_state": "PASS",
    },
    "arb": {
        "primary_language": "ar",
        "authored_language": "ar",
        "translation_state": "ORIGINAL",
        "dialect_or_register": "AR_MSA",
        "code_switch_state": "NOT_CLASSIFIED",
        "transliteration_state": "NOT_CLASSIFIED",
        "terminology_normalization_id": None,
        "qualified_review_state": "PASS",
    },
}
CAPABILITY_TO_STRATUM = {
    "GENERAL_INSTRUCTION_FOLLOWING": "general_instruction_following",
    "GENERAL_ENGLISH_LANGUAGE": "general_english_language",
    "GENERAL_ARABIC_LANGUAGE_NON_CLINICAL": "general_arabic_language_non_clinical",
    "NON_CLINICAL_RESEARCH_LEARNING_FORMATTING": "non_clinical_research_learning_formatting",
}
EXPECTED_LANGUAGE_CAPABILITY = {
    "eng": "GENERAL_ENGLISH_LANGUAGE",
    "arb": "GENERAL_ARABIC_LANGUAGE_NON_CLINICAL",
}
FORMATTING_TASK_FAMILIES = {"SUMMARIZATION", "FORMATTING_ORGANIZATION"}
ALLOWED_TASK_FAMILIES = {
    "TRANSLATION",
    "SUMMARIZATION",
    "REWRITE_EDIT",
    "CREATIVE_OR_COMPOSITION",
    "LANGUAGE_LEARNING",
    "FORMATTING_ORGANIZATION",
}


def canonical_bytes(value: Any) -> bytes:
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode("utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def set_root(values: Iterable[str]) -> str:
    return hashlib.sha256(("\n".join(sorted(values)) + "\n").encode("ascii")).hexdigest()


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def load_candidate_manifest(path: Path) -> dict[str, Any]:
    if sha256_file(path) != EXPECTED_MANIFEST_FILE_SHA256:
        raise SystemExit("CANDIDATE_MANIFEST_FILE_SHA256_MISMATCH")
    manifest = load_json(path)
    if hashlib.sha256(canonical_bytes(manifest)).hexdigest() != EXPECTED_MANIFEST_CANONICAL_SHA256:
        raise SystemExit("CANDIDATE_MANIFEST_CANONICAL_SHA256_MISMATCH")
    expected = {
        "candidate_count": EXPECTED_CANDIDATE_COUNT,
        "filter_id": FILTER_ID,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "source_repository": SOURCE_REPOSITORY,
        "source_revision": SOURCE_REVISION,
        "source_file": SOURCE_FILE,
        "source_file_sha256": SOURCE_FILE_SHA256,
    }
    for key, value in expected.items():
        if manifest.get(key) != value:
            raise SystemExit(f"CANDIDATE_MANIFEST_{key.upper()}_MISMATCH")
    records = manifest.get("records")
    if not isinstance(records, list) or len(records) != EXPECTED_CANDIDATE_COUNT:
        raise SystemExit("CANDIDATE_MANIFEST_RECORD_COUNT_MISMATCH")
    ids = [str(item.get("candidate_record_id", "")) for item in records]
    contents = [str(item.get("content_sha256", "")) for item in records]
    if len(set(ids)) != EXPECTED_CANDIDATE_COUNT or set_root(ids) != EXPECTED_CANDIDATE_RECORD_SET_SHA256:
        raise SystemExit("CANDIDATE_MANIFEST_RECORD_SET_MISMATCH")
    if len(set(contents)) != EXPECTED_CANDIDATE_COUNT or set_root(contents) != EXPECTED_CANDIDATE_CONTENT_SET_SHA256:
        raise SystemExit("CANDIDATE_MANIFEST_CONTENT_SET_MISMATCH")
    return manifest


def load_projection(path: Path) -> dict[str, Any]:
    if sha256_file(path) != EXPECTED_PROJECTION_SHA256:
        raise SystemExit("PROJECTION_SHA256_MISMATCH")
    projection = load_json(path)
    supported = projection.get("rights_supported_candidate_ids")
    unresolved = projection.get("rights_unresolved_candidate_ids")
    if not isinstance(supported, list) or not isinstance(unresolved, list):
        raise SystemExit("PROJECTION_RIGHTS_SETS_INVALID")
    if len(supported) != EXPECTED_ELIGIBLE_COUNT:
        raise SystemExit("PROJECTION_ELIGIBLE_COUNT_MISMATCH")
    if set_root([str(item) for item in supported]) != EXPECTED_ELIGIBLE_RECORD_SET_SHA256:
        raise SystemExit("PROJECTION_ELIGIBLE_SET_MISMATCH")
    if set(supported) & set(unresolved):
        raise SystemExit("PROJECTION_RIGHTS_SET_OVERLAP")
    if len(set(supported) | set(unresolved)) != EXPECTED_CANDIDATE_COUNT:
        raise SystemExit("PROJECTION_TOTAL_SET_MISMATCH")
    return projection


def load_digest_map(paths: list[Path]) -> dict[str, str]:
    if len(paths) != 5:
        raise SystemExit("DIGEST_MAP_PART_COUNT_MISMATCH")
    result: dict[str, str] = {}
    for index, path in enumerate(paths):
        if sha256_file(path) != EXPECTED_MAP_PART_SHA256[index]:
            raise SystemExit(f"DIGEST_MAP_PART_{index + 1}_SHA256_MISMATCH")
        payload = load_json(path)
        if payload.get("part") != index + 1 or payload.get("part_count") != 5:
            raise SystemExit(f"DIGEST_MAP_PART_{index + 1}_IDENTITY_MISMATCH")
        for record in payload.get("records", []):
            candidate_id = str(record.get("candidate_record_id", ""))
            content_sha = str(record.get("content_sha256", ""))
            if candidate_id in result:
                raise SystemExit("DIGEST_MAP_DUPLICATE_RECORD_ID")
            result[candidate_id] = content_sha
    if len(result) != EXPECTED_CANDIDATE_COUNT:
        raise SystemExit("DIGEST_MAP_RECORD_COUNT_MISMATCH")
    if set_root(result.keys()) != EXPECTED_CANDIDATE_RECORD_SET_SHA256:
        raise SystemExit("DIGEST_MAP_RECORD_SET_MISMATCH")
    if set_root(result.values()) != EXPECTED_CANDIDATE_CONTENT_SET_SHA256:
        raise SystemExit("DIGEST_MAP_CONTENT_SET_MISMATCH")
    return result


def verify_contamination_evidence(path: Path) -> None:
    evidence = load_json(path)
    checks = {
        "candidate_count": EXPECTED_CANDIDATE_COUNT,
        "candidate_manifest_canonical_sha256": EXPECTED_MANIFEST_CANONICAL_SHA256,
        "candidate_record_id_set_sha256": EXPECTED_CANDIDATE_RECORD_SET_SHA256,
        "candidate_content_sha256_set_sha256": EXPECTED_CANDIDATE_CONTENT_SET_SHA256,
        "source_file_sha256": SOURCE_FILE_SHA256,
        "contamination_results_sha256": EXPECTED_CONTAMINATION_RESULTS_SHA256,
        "purpose": "TRAIN",
        "quarantine_state": "NOT_QUARANTINED",
    }
    for key, value in checks.items():
        if evidence.get(key) != value:
            raise SystemExit(f"CONTAMINATION_EVIDENCE_{key.upper()}_MISMATCH")
    if evidence.get("contamination_state_counts") != {"ASSESSED_CLEAN": EXPECTED_CANDIDATE_COUNT}:
        raise SystemExit("CONTAMINATION_STATE_COUNTS_MISMATCH")
    if evidence.get("quarantine_conflict_observed") is not False:
        raise SystemExit("QUARANTINE_CONFLICT")
    if evidence.get("private_gold_used") is not False:
        raise SystemExit("PRIVATE_GOLD_USE_CONFLICT")
    if evidence.get("public_external_eval_used_as_training_source") is not False:
        raise SystemExit("PUBLIC_EXTERNAL_EVAL_TRAINING_CONFLICT")


def expected_capabilities(language_code: str, task_family: str) -> list[str]:
    if language_code not in EXPECTED_LANGUAGE_CAPABILITY:
        raise ValueError("UNSUPPORTED_LANGUAGE_CODE")
    if task_family not in ALLOWED_TASK_FAMILIES:
        raise ValueError("UNSUPPORTED_TASK_FAMILY")
    values = {"GENERAL_INSTRUCTION_FOLLOWING", EXPECTED_LANGUAGE_CAPABILITY[language_code]}
    if task_family in FORMATTING_TASK_FAMILIES:
        values.add("NON_CLINICAL_RESEARCH_LEARNING_FORMATTING")
    return sorted(values)


def curriculum_strata(capabilities: list[str]) -> list[str]:
    unknown = sorted(set(capabilities) - set(CAPABILITY_TO_STRATUM))
    if unknown:
        raise ValueError(f"UNKNOWN_CAPABILITY:{','.join(unknown)}")
    return sorted({CAPABILITY_TO_STRATUM[item] for item in capabilities})


def build_curriculum_record(candidate: Mapping[str, Any], content_sha256: str) -> dict[str, Any]:
    candidate_id = str(candidate["candidate_record_id"])
    language_code = str(candidate["language_code"])
    task_family = str(candidate["task_family"])
    capabilities = [str(item) for item in candidate["verified_target_capability_ids"]]
    if capabilities != expected_capabilities(language_code, task_family):
        raise ValueError("CANDIDATE_CAPABILITY_MISMATCH")
    record: dict[str, Any] = {
        "schema_version": "1",
        "record_id": f"aya-43:{candidate_id}",
        "record_canonical_sha256": "0" * 64,
        "content_sha256": content_sha256,
        "source_authority_id": AUTHORITY_ID,
        "source_license_id": SOURCE_LICENSE_ID,
        "source_verification_status": "VERIFIED",
        "split_id": "VERIFIED_SFT_CURRICULUM_DATA",
        "contamination_status": "ASSESSED_CLEAN",
        "review_state": "PASS",
        "role_class": "LEARNER_RESEARCHER",
        "curriculum_strata": curriculum_strata(capabilities),
        "language_profile": dict(LANGUAGE_PROFILE[language_code]),
        "conversation_structure_id": "single-turn-v1",
        "knowledge_placement": "DURABLE_WEIGHT_ELIGIBLE",
        "quarantine_disposition": "PASS",
    }
    record["record_canonical_sha256"] = compute_curriculum_record_sha256(record)
    errors = validate_curriculum_record(record)
    if errors:
        raise ValueError(f"CURRICULUM_RECORD_INVALID:{'|'.join(errors)}")
    return record


def build_scope_verification(candidate: Mapping[str, Any], record: Mapping[str, Any]) -> dict[str, Any]:
    candidate_id = str(candidate["candidate_record_id"])
    verification: dict[str, Any] = {
        "schema_version": "1",
        "verification_id": f"aya-43-scope:{candidate_id}",
        "verification_sha256": "0" * 64,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "record_id": record["record_id"],
        "record_canonical_sha256": record["record_canonical_sha256"],
        "record_content_sha256": record["content_sha256"],
        "verified_target_capability_ids": [
            str(item) for item in candidate["verified_target_capability_ids"]
        ],
        "excluded_capability_hits": [],
        "verification_method": "DETERMINISTIC_SCOPE_CLASSIFICATION",
        "disposition": "PASS",
    }
    verification["verification_sha256"] = (
        compute_research_component_content_scope_verification_sha256(verification)
    )
    errors = validate_research_component_content_scope_verification(
        verification,
        curriculum_record=record,
    )
    if errors:
        raise ValueError(f"CONTENT_SCOPE_VERIFICATION_INVALID:{'|'.join(errors)}")
    return verification


def construct(
    candidate_manifest: Path,
    projection_path: Path,
    digest_map_parts: list[Path],
    contamination_evidence: Path,
) -> dict[str, Any]:
    manifest = load_candidate_manifest(candidate_manifest)
    projection = load_projection(projection_path)
    digest_map = load_digest_map(digest_map_parts)
    verify_contamination_evidence(contamination_evidence)

    eligible_ids = {str(item) for item in projection["rights_supported_candidate_ids"]}
    manifest_by_id = {str(item["candidate_record_id"]): item for item in manifest["records"]}
    if set(manifest_by_id) != set(digest_map):
        raise SystemExit("MANIFEST_DIGEST_MAP_ID_SET_MISMATCH")

    entries: list[dict[str, Any]] = []
    language_counts: collections.Counter[str] = collections.Counter()
    task_family_counts: collections.Counter[str] = collections.Counter()
    capability_counts: collections.Counter[str] = collections.Counter()

    for candidate_id in sorted(eligible_ids):
        candidate = manifest_by_id.get(candidate_id)
        if candidate is None:
            raise SystemExit("ELIGIBLE_ID_MISSING_FROM_MANIFEST")
        content_sha = digest_map[candidate_id]
        if candidate.get("content_sha256") != content_sha:
            raise SystemExit("ELIGIBLE_CONTENT_DIGEST_MISMATCH")
        record = build_curriculum_record(candidate, content_sha)
        verification = build_scope_verification(candidate, record)
        capabilities = [str(item) for item in candidate["verified_target_capability_ids"]]
        entry = {
            "candidate_record_id": candidate_id,
            "language_code": str(candidate["language_code"]),
            "task_family": str(candidate["task_family"]),
            "verified_target_capability_ids": capabilities,
            "curriculum_record": record,
            "content_scope_verification": verification,
        }
        entries.append(entry)
        language_counts[entry["language_code"]] += 1
        task_family_counts[entry["task_family"]] += 1
        capability_counts.update(capabilities)

    if len(entries) != EXPECTED_ELIGIBLE_COUNT:
        raise SystemExit("CURRICULUM_RECORD_COUNT_MISMATCH")
    if set_root(entry["candidate_record_id"] for entry in entries) != EXPECTED_ELIGIBLE_RECORD_SET_SHA256:
        raise SystemExit("CURRICULUM_RECORD_ID_SET_MISMATCH")
    if len({entry["curriculum_record"]["record_id"] for entry in entries}) != EXPECTED_ELIGIBLE_COUNT:
        raise SystemExit("CURRICULUM_RECORD_ID_DUPLICATE")
    if len({entry["content_scope_verification"]["verification_id"] for entry in entries}) != EXPECTED_ELIGIBLE_COUNT:
        raise SystemExit("CONTENT_SCOPE_VERIFICATION_ID_DUPLICATE")

    return {
        "artifact_id": "e004-aya-43-curriculum-and-scope-bundle-v1",
        "schema_version": "1",
        "method_id": METHOD_ID,
        "authority_id": AUTHORITY_ID,
        "scope_id": RESEARCH_COMPONENT_SCOPE_ID,
        "source_repository": SOURCE_REPOSITORY,
        "source_revision": SOURCE_REVISION,
        "source_file": SOURCE_FILE,
        "source_file_sha256": SOURCE_FILE_SHA256,
        "candidate_manifest_canonical_sha256": EXPECTED_MANIFEST_CANONICAL_SHA256,
        "candidate_manifest_file_sha256": EXPECTED_MANIFEST_FILE_SHA256,
        "candidate_record_id_set_sha256": EXPECTED_CANDIDATE_RECORD_SET_SHA256,
        "candidate_content_sha256_set_sha256": EXPECTED_CANDIDATE_CONTENT_SET_SHA256,
        "spec003_corrected_direct_digest_results_sha256": EXPECTED_SPEC003_SHA256,
        "eligible_record_count": EXPECTED_ELIGIBLE_COUNT,
        "eligible_record_id_set_sha256": EXPECTED_ELIGIBLE_RECORD_SET_SHA256,
        "language_counts": dict(sorted(language_counts.items())),
        "task_family_counts": dict(sorted(task_family_counts.items())),
        "capability_counts": dict(sorted(capability_counts.items())),
        "raw_aya_text_persisted": False,
        "user_id_read": False,
        "remote_model_or_ai_record_processing": False,
        "entries": entries,
    }


def validate_bundle(bundle: Mapping[str, Any]) -> None:
    if bundle.get("method_id") != METHOD_ID or bundle.get("authority_id") != AUTHORITY_ID:
        raise ValueError("BUNDLE_METHOD_OR_AUTHORITY_MISMATCH")
    entries = bundle.get("entries")
    if not isinstance(entries, list) or len(entries) != EXPECTED_ELIGIBLE_COUNT:
        raise ValueError("BUNDLE_ENTRY_COUNT_MISMATCH")
    if set_root(str(entry.get("candidate_record_id", "")) for entry in entries) != EXPECTED_ELIGIBLE_RECORD_SET_SHA256:
        raise ValueError("BUNDLE_ELIGIBLE_ID_SET_MISMATCH")
    for entry in entries:
        candidate_id = str(entry["candidate_record_id"])
        record = entry["curriculum_record"]
        verification = entry["content_scope_verification"]
        if record.get("record_id") != f"aya-43:{candidate_id}":
            raise ValueError("BUNDLE_RECORD_LINK_MISMATCH")
        if compute_curriculum_record_sha256(record) != record.get("record_canonical_sha256"):
            raise ValueError("BUNDLE_RECORD_HASH_MISMATCH")
        errors = validate_curriculum_record(record)
        if errors:
            raise ValueError(f"BUNDLE_RECORD_INVALID:{'|'.join(errors)}")
        if verification.get("verification_id") != f"aya-43-scope:{candidate_id}":
            raise ValueError("BUNDLE_VERIFICATION_LINK_MISMATCH")
        if compute_research_component_content_scope_verification_sha256(verification) != verification.get("verification_sha256"):
            raise ValueError("BUNDLE_VERIFICATION_HASH_MISMATCH")
        errors = validate_research_component_content_scope_verification(
            verification,
            curriculum_record=record,
        )
        if errors:
            raise ValueError(f"BUNDLE_VERIFICATION_INVALID:{'|'.join(errors)}")


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    construct_parser = subparsers.add_parser("construct")
    construct_parser.add_argument("--candidate-manifest", type=Path, required=True)
    construct_parser.add_argument("--projection", type=Path, required=True)
    construct_parser.add_argument("--digest-map-part", type=Path, action="append", required=True)
    construct_parser.add_argument("--contamination-evidence", type=Path, required=True)
    construct_parser.add_argument("--out", type=Path, required=True)

    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--bundle", type=Path, required=True)

    args = parser.parse_args()
    if args.command == "construct":
        bundle = construct(
            args.candidate_manifest,
            args.projection,
            args.digest_map_part,
            args.contamination_evidence,
        )
        args.out.write_bytes(canonical_bytes(bundle) + b"\n")
        print(
            json.dumps(
                {
                    "artifact_id": bundle["artifact_id"],
                    "eligible_record_count": bundle["eligible_record_count"],
                    "eligible_record_id_set_sha256": bundle["eligible_record_id_set_sha256"],
                    "language_counts": bundle["language_counts"],
                    "task_family_counts": bundle["task_family_counts"],
                    "capability_counts": bundle["capability_counts"],
                    "output_sha256": sha256_file(args.out),
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )
    else:
        bundle = load_json(args.bundle)
        validate_bundle(bundle)
        print(
            json.dumps(
                {
                    "artifact_id": bundle.get("artifact_id"),
                    "eligible_record_count": len(bundle["entries"]),
                    "output_sha256": sha256_file(args.bundle),
                    "validation": "PASS",
                },
                sort_keys=True,
                separators=(",", ":"),
            )
        )


if __name__ == "__main__":
    main()
