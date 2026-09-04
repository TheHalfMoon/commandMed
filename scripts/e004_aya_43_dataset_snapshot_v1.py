#!/usr/bin/env python3
"""Construct and validate the exact E004 Aya-43 research-component DatasetSnapshot.

This surface is repository-safe and deterministic. It consumes only the already
persisted hash/categorical Aya-43 curriculum bundle and repository-safe evidence.
It never reads raw Aya text, user identifiers, model weights, credentials, or a
network resource, and it never performs model inference or training.
"""

from __future__ import annotations

import argparse
import base64
import gzip
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

from src.commandmed.eval_contract.canonical import (
    canonical_json_dumps,
    compute_canonical_sha256,
)
from src.commandmed.spec007.curriculum import (
    validate_curriculum_record,
    validate_duplicate_contamination_report,
)
from src.commandmed.spec007.quarantine import (
    canonical_quarantine_matrix_sha256,
    evaluate_quarantine_source,
    validate_quarantine_binding,
)
from src.commandmed.spec007.research_scope import (
    validate_research_component_content_scope_verification,
)
from src.commandmed.spec007.snapshot import (
    build_dataset_snapshot,
    compute_dataset_snapshot_sha256,
    validate_dataset_snapshot,
)

ROOT = Path(__file__).resolve().parents[1]
SPEC_ROOT = ROOT / "specs" / "007-sft-v1"

DECISION_PATH = SPEC_ROOT / "e004-dataset-snapshot-quarantine-founder-decision-2026-09-04.md"
HEADER_PATH = SPEC_ROOT / "e004-aya-43-curriculum-and-scope-persistence-v1-header.json"
PART1_PATH = SPEC_ROOT / "e004-aya-43-curriculum-and-scope-persistence-v1-part-01.json"
PART2_PATH = SPEC_ROOT / "e004-aya-43-curriculum-and-scope-persistence-v1-part-02.json"
CHUNK_PATHS = [
    SPEC_ROOT / f"e004-aya-43-curriculum-and-scope-persistence-v1-packed-chunk-{index:02d}.b64"
    for index in range(1, 7)
]
NEAR_DUP_PATH = SPEC_ROOT / "e004-aya-43-near-duplicate-assessment-evidence-v1.json"
CONTAMINATION_PATH = SPEC_ROOT / "e004-aya-135-qualification-evidence-v1.json"

EXPECTED_SOURCE_FILE_SHA256 = "51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06"
EXPECTED_CANDIDATE_MANIFEST_SHA256 = "dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99"
EXPECTED_CANDIDATE_RECORD_ID_SET_SHA256 = "d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83"
EXPECTED_CANDIDATE_CONTENT_SHA256_SET_SHA256 = "ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64"
EXPECTED_AYA43_SET_SHA256 = "417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4"
EXPECTED_AYA43_BUNDLE_SHA256 = "f12f70a754e39d395c4d5999fcae1d6718640b1a97931fd9f48321469b87be03"
EXPECTED_DUPLICATE_REPORT_SHA256 = "562c3f3726538d27f2d40e2f20a762764b9f21c3675a3621672755c7cbc9d6b0"
EXPECTED_CONTAMINATION_RESULTS_SHA256 = "f584d937990972bc7101da95c0edba52e4537ef7f80f9afac10bbc55be102857"
EXPECTED_CONTAMINATION_SUMMARY_SHA256 = "35cf4db119dd21c32a05ddd7e222cc2d6bf1f9ee5c5c694b6e682f784eb02e89"

SNAPSHOT_ID = "e004-aya-43-research-component-dataset-snapshot-v1"
CANONICAL_ORDER_IDENTITY = "AYA_43_CURRICULUM_RECORD_ID_ASCENDING_V1"
DUPLICATE_REPORT_ID = "e004-aya-43-duplicate-contamination-report-v1"
CONTAMINATION_REPORT_ID = "e004-aya-135-qualification-evidence-v1"
QUARANTINE_VERIFICATION_ID = "e004-aya-43-train-quarantine-verification-v1"
QUARANTINE_SOURCE_ID = "VERIFIED_SFT_CURRICULUM_DATA"
QUARANTINE_PURPOSE = "TRAIN"

EXPECTED_FILE_SHA256 = {
    HEADER_PATH: "896d502cd9e18f207d1219da2c63daaaabf04904b5302c9ae217df4d056057a4",
    PART1_PATH: "e570ec057b474f5df7ed6f8cac5c1b4e1b508a095536b24cde25b30840445ca6",
    PART2_PATH: "69d046bd3fc5c75b510b51ac6ba6d1e163a9b77f04a5a132c7a86a8ed963dc0f",
    CHUNK_PATHS[0]: "bee023ecd73f1919f5130ac69403e9a7e50c1f38ad02f41e45b3d7b28d027ce6",
    CHUNK_PATHS[1]: "ae2ce7b57f9f81116c9527e7f791b23c7cf1626fc5030810c5db00625d41c424",
    CHUNK_PATHS[2]: "f0cc2d5aaf93884b23a58aca8d8f5b1adbde9ca17ea5114e255bcf6136e3ecd9",
    CHUNK_PATHS[3]: "0d9330d23a531477977fed7d204fce839658f97a7e8f47285121966e8020bc4f",
    CHUNK_PATHS[4]: "fbf35af63183e8e5e5e9c2e6e7169e25ea6048599a591567278f26d6dad0ef64",
    CHUNK_PATHS[5]: "3280d986af5fd567b9ca53e2c94c17ade53207b88a4e04544d89fb950fe3aa73",
}
EXPECTED_PACKED_GZIP_SHA256 = "928c69fecd957477ac931cd9464184e1f9455bd359f30258112158a6f8308139"
EXPECTED_PACKED_RAW_SHA256 = "ac0001440b55dd5469fe57ccbc367b530fc175bbaf7aceb3c1c5d11786eff5f5"


def _file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def _load_json(path: Path) -> dict[str, Any]:
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit(f"JSON_OBJECT_REQUIRED:{path.name}")
    return value


def _set_root(values: Iterable[str]) -> str:
    normalized = sorted(values)
    if len(normalized) != len(set(normalized)):
        raise SystemExit("SET_ROOT_DUPLICATE_VALUE")
    return hashlib.sha256(("\n".join(normalized) + "\n").encode("ascii")).hexdigest()


def _assert_decision() -> None:
    text = DECISION_PATH.read_text(encoding="utf-8")
    required = (
        "FOUNDER_DATASET_SNAPSHOT_QUARANTINE_DECISION=E004_DATASET_SNAPSHOT_QUARANTINE_DECISION_B",
        "DATASET_SNAPSHOT_AUTHORITY=AUTHORIZED_CONDITIONAL_EXACT_AYA_43_RESEARCH_COMPONENT_ONLY",
        "DUPLICATE_NEAR_DUPLICATE_ASSESSMENT_AUTHORITY=AUTHORIZED_EXACT_AYA_43_PREDECLARED_METHOD_ONLY",
        "QUARANTINE_VERIFICATION_CONSTRUCTION_AUTHORITY=AUTHORIZED_EXACT_VERIFIED_SFT_CURRICULUM_DATA_TRAIN_BINDING_ONLY",
        "SNAPSHOT_BUILDER_REPAIR_AUTHORITY=AUTHORIZED_NARROW_PROVENANCE_VS_QUARANTINE_SEMANTICS_REPAIR_ONLY",
        "TRAINING_AUTHORITY=NONE",
        "CURRENT_AUTHORIZED_SPEND_USD=0",
    )
    for line in required:
        if line not in text.splitlines():
            raise SystemExit(f"FOUNDER_DECISION_BINDING_MISMATCH:{line}")


def _assert_safe_repository_object(value: Any) -> None:
    prohibited_keys = {"inputs", "targets", "prompt", "prompt_text", "user_id"}
    if isinstance(value, dict):
        for key, child in value.items():
            if key in prohibited_keys:
                raise SystemExit(f"PROHIBITED_PERSISTED_KEY:{key}")
            _assert_safe_repository_object(child)
    elif isinstance(value, list):
        for child in value:
            _assert_safe_repository_object(child)


def reconstruct_aya43_bundle() -> dict[str, Any]:
    for path, expected in EXPECTED_FILE_SHA256.items():
        actual = _file_sha256(path)
        if actual != expected:
            raise SystemExit(f"PERSISTENCE_FILE_SHA256_MISMATCH:{path.name}:{actual}")

    header = _load_json(HEADER_PATH)
    if header.get("artifact_id") != "e004-aya-43-curriculum-and-scope-persistence-v1":
        raise SystemExit("PERSISTENCE_HEADER_ARTIFACT_ID_MISMATCH")
    if header.get("schema_version") != "1" or header.get("entry_count") != 43 or header.get("part_count") != 9:
        raise SystemExit("PERSISTENCE_HEADER_SHAPE_MISMATCH")
    if header.get("expected_full_bundle_sha256") != EXPECTED_AYA43_BUNDLE_SHA256:
        raise SystemExit("PERSISTENCE_HEADER_BUNDLE_SHA256_MISMATCH")

    packed_b64 = b"".join(path.read_bytes().strip() for path in CHUNK_PATHS)
    if len(packed_b64) != 10188:
        raise SystemExit(f"PACKED_BASE64_LENGTH_MISMATCH:{len(packed_b64)}")
    packed_gzip = base64.b64decode(packed_b64, validate=True)
    if hashlib.sha256(packed_gzip).hexdigest() != EXPECTED_PACKED_GZIP_SHA256:
        raise SystemExit("PACKED_GZIP_SHA256_MISMATCH")
    packed_raw = gzip.decompress(packed_gzip)
    if hashlib.sha256(packed_raw).hexdigest() != EXPECTED_PACKED_RAW_SHA256:
        raise SystemExit("PACKED_RAW_SHA256_MISMATCH")
    packed = json.loads(packed_raw)
    if not isinstance(packed, dict):
        raise SystemExit("PACKED_OBJECT_REQUIRED")
    if packed.get("artifact_id") != "e004-aya-43-curriculum-and-scope-persistence-packed-parts-v1":
        raise SystemExit("PACKED_ARTIFACT_ID_MISMATCH")
    if packed.get("schema_version") != "1" or packed.get("first_part") != 3 or packed.get("last_part") != 9:
        raise SystemExit("PACKED_RANGE_MISMATCH")

    parts = [_load_json(PART1_PATH), _load_json(PART2_PATH), *packed.get("parts", [])]
    if len(parts) != 9:
        raise SystemExit("PERSISTENCE_PART_COUNT_MISMATCH")

    entries: list[dict[str, Any]] = []
    for expected_part, part in enumerate(parts, start=1):
        if not isinstance(part, dict):
            raise SystemExit(f"PART_OBJECT_REQUIRED:{expected_part}")
        if part.get("artifact_id") != "e004-aya-43-curriculum-and-scope-persistence-part-v1":
            raise SystemExit(f"PART_ARTIFACT_ID_MISMATCH:{expected_part}")
        if part.get("schema_version") != "1" or part.get("part") != expected_part or part.get("part_count") != 9:
            raise SystemExit(f"PART_IDENTITY_MISMATCH:{expected_part}")
        part_entries = part.get("entries")
        if not isinstance(part_entries, list) or not part_entries:
            raise SystemExit(f"PART_ENTRIES_INVALID:{expected_part}")
        if any(not isinstance(entry, dict) for entry in part_entries):
            raise SystemExit(f"PART_ENTRY_OBJECT_REQUIRED:{expected_part}")
        entries.extend(part_entries)

    if len(entries) != 43:
        raise SystemExit(f"PERSISTED_ENTRY_COUNT_MISMATCH:{len(entries)}")

    bundle_fields = header.get("bundle_fields")
    if not isinstance(bundle_fields, dict):
        raise SystemExit("BUNDLE_FIELDS_OBJECT_REQUIRED")
    bundle = dict(bundle_fields)
    bundle["entries"] = entries
    _assert_safe_repository_object(bundle)

    if bundle.get("eligible_record_count") != 43:
        raise SystemExit("BUNDLE_ELIGIBLE_COUNT_MISMATCH")
    if bundle.get("eligible_record_id_set_sha256") != EXPECTED_AYA43_SET_SHA256:
        raise SystemExit("BUNDLE_ELIGIBLE_SET_MISMATCH")
    if bundle.get("candidate_manifest_canonical_sha256") != EXPECTED_CANDIDATE_MANIFEST_SHA256:
        raise SystemExit("BUNDLE_CANDIDATE_MANIFEST_MISMATCH")
    if bundle.get("candidate_record_id_set_sha256") != EXPECTED_CANDIDATE_RECORD_ID_SET_SHA256:
        raise SystemExit("BUNDLE_CANDIDATE_RECORD_SET_MISMATCH")
    if bundle.get("candidate_content_sha256_set_sha256") != EXPECTED_CANDIDATE_CONTENT_SHA256_SET_SHA256:
        raise SystemExit("BUNDLE_CANDIDATE_CONTENT_SET_MISMATCH")
    if bundle.get("source_file_sha256") != EXPECTED_SOURCE_FILE_SHA256:
        raise SystemExit("BUNDLE_SOURCE_SHA256_MISMATCH")
    if bundle.get("raw_aya_text_persisted") is not False or bundle.get("user_id_read") is not False:
        raise SystemExit("BUNDLE_PRIVACY_BOUNDARY_MISMATCH")
    if bundle.get("remote_model_or_ai_record_processing") is not False:
        raise SystemExit("BUNDLE_EXTERNAL_PROCESSING_BOUNDARY_MISMATCH")

    bundle_bytes = json.dumps(
        bundle,
        ensure_ascii=False,
        sort_keys=True,
        separators=(",", ":"),
    ).encode("utf-8") + b"\n"
    actual_bundle_sha256 = hashlib.sha256(bundle_bytes).hexdigest()
    if actual_bundle_sha256 != EXPECTED_AYA43_BUNDLE_SHA256:
        raise SystemExit(f"FULL_BUNDLE_SHA256_MISMATCH:{actual_bundle_sha256}")

    candidate_ids: list[str] = []
    record_ids: set[str] = set()
    for index, entry in enumerate(entries):
        candidate_id = entry.get("candidate_record_id")
        curriculum = entry.get("curriculum_record")
        verification = entry.get("content_scope_verification")
        if not isinstance(candidate_id, str) or not isinstance(curriculum, dict) or not isinstance(verification, dict):
            raise SystemExit(f"PERSISTED_ENTRY_SHAPE_MISMATCH:{index}")
        candidate_ids.append(candidate_id)
        expected_record_id = f"aya-43:{candidate_id}"
        if curriculum.get("record_id") != expected_record_id:
            raise SystemExit(f"CURRICULUM_RECORD_ID_BINDING_MISMATCH:{index}")
        if expected_record_id in record_ids:
            raise SystemExit(f"DUPLICATE_CURRICULUM_RECORD_ID:{expected_record_id}")
        record_ids.add(expected_record_id)
        curriculum_errors = validate_curriculum_record(curriculum)
        if curriculum_errors:
            raise SystemExit(f"CURRICULUM_VALIDATION_FAILED:{index}:{'|'.join(curriculum_errors)}")
        verification_errors = validate_research_component_content_scope_verification(
            verification,
            curriculum,
        )
        if verification_errors:
            raise SystemExit(f"SCOPE_VERIFICATION_FAILED:{index}:{'|'.join(verification_errors)}")

    if _set_root(candidate_ids) != EXPECTED_AYA43_SET_SHA256:
        raise SystemExit("PERSISTED_AYA43_SET_ROOT_MISMATCH")
    return bundle


def load_duplicate_evidence() -> tuple[dict[str, Any], str]:
    evidence = _load_json(NEAR_DUP_PATH)
    expected_scalars = {
        "artifact_id": "e004-aya-43-near-duplicate-assessment-evidence-v1",
        "schema_version": "1",
        "method_id": "AYA_43_INTERNAL_13_TOKEN_EXACT_NEAR_DUPLICATE_V1",
        "source_file_sha256": EXPECTED_SOURCE_FILE_SHA256,
        "candidate_manifest_canonical_sha256": EXPECTED_CANDIDATE_MANIFEST_SHA256,
        "candidate_record_id_set_sha256": EXPECTED_CANDIDATE_RECORD_ID_SET_SHA256,
        "candidate_content_sha256_set_sha256": EXPECTED_CANDIDATE_CONTENT_SHA256_SET_SHA256,
        "selected_record_count": 43,
        "selected_record_id_set_sha256": EXPECTED_AYA43_SET_SHA256,
        "ngram_length_tokens": 13,
        "normalization": "UNICODE_NFKC_CASEFOLD",
        "tokenization": "PYTHON_UNICODE_REGEX_WORD_TOKENS",
        "near_duplicate_pair_count": 0,
        "duplicate_report_canonical_sha256": EXPECTED_DUPLICATE_REPORT_SHA256,
        "raw_text_persisted": False,
        "matched_ngram_persisted": False,
        "user_id_read": False,
        "model_inference_used": False,
        "semantic_judge_used": False,
    }
    for field, expected in expected_scalars.items():
        if evidence.get(field) != expected:
            raise SystemExit(f"NEAR_DUP_EVIDENCE_MISMATCH:{field}")
    if evidence.get("compare_fields") != ["inputs", "targets"]:
        raise SystemExit("NEAR_DUP_COMPARE_FIELDS_MISMATCH")
    if evidence.get("near_duplicate_pair_count_by_field") != {}:
        raise SystemExit("NEAR_DUP_PAIR_FIELD_COUNTS_MISMATCH")
    if not isinstance(evidence.get("input_window_count"), int) or evidence["input_window_count"] < 0:
        raise SystemExit("NEAR_DUP_INPUT_WINDOW_COUNT_INVALID")
    if not isinstance(evidence.get("target_window_count"), int) or evidence["target_window_count"] < 0:
        raise SystemExit("NEAR_DUP_TARGET_WINDOW_COUNT_INVALID")

    report = evidence.get("duplicate_report")
    if not isinstance(report, dict):
        raise SystemExit("DUPLICATE_REPORT_OBJECT_REQUIRED")
    if report.get("report_id") != DUPLICATE_REPORT_ID:
        raise SystemExit("DUPLICATE_REPORT_ID_MISMATCH")
    if report.get("input_snapshot_candidate_id") != SNAPSHOT_ID:
        raise SystemExit("DUPLICATE_REPORT_SNAPSHOT_ID_MISMATCH")
    if report.get("disposition") != "PASS":
        raise SystemExit("DUPLICATE_REPORT_NOT_PASS")
    if compute_canonical_sha256(report) != EXPECTED_DUPLICATE_REPORT_SHA256:
        raise SystemExit("DUPLICATE_REPORT_SHA256_MISMATCH")
    report_errors = validate_duplicate_contamination_report(report)
    if report_errors:
        raise SystemExit("DUPLICATE_REPORT_VALIDATION_FAILED:" + "|".join(report_errors))
    return report, EXPECTED_DUPLICATE_REPORT_SHA256


def load_contamination_evidence() -> dict[str, Any]:
    evidence = _load_json(CONTAMINATION_PATH)
    expected = {
        "artifact_id": CONTAMINATION_REPORT_ID,
        "candidate_count": 135,
        "candidate_manifest_canonical_sha256": EXPECTED_CANDIDATE_MANIFEST_SHA256,
        "candidate_record_id_set_sha256": EXPECTED_CANDIDATE_RECORD_ID_SET_SHA256,
        "candidate_content_sha256_set_sha256": EXPECTED_CANDIDATE_CONTENT_SHA256_SET_SHA256,
        "contamination_method_id": "AYA_135_PUBLIC_CANONICAL_TEXT_13_TOKEN_EXACT_V1",
        "contamination_results_sha256": EXPECTED_CONTAMINATION_RESULTS_SHA256,
        "contamination_summary_sha256": EXPECTED_CONTAMINATION_SUMMARY_SHA256,
        "source_file_sha256": EXPECTED_SOURCE_FILE_SHA256,
        "purpose": "TRAIN",
        "quarantine_state": "NOT_QUARANTINED",
        "quarantine_conflict_observed": False,
        "private_gold_used": False,
        "public_external_eval_used_as_training_source": False,
        "model_inference_used": False,
    }
    for field, expected_value in expected.items():
        if evidence.get(field) != expected_value:
            raise SystemExit(f"CONTAMINATION_EVIDENCE_MISMATCH:{field}")
    if evidence.get("contamination_state_counts") != {"ASSESSED_CLEAN": 135}:
        raise SystemExit("CONTAMINATION_STATE_COUNTS_MISMATCH")
    return evidence


def build_quarantine_verification() -> dict[str, Any]:
    decision = evaluate_quarantine_source(QUARANTINE_SOURCE_ID, QUARANTINE_PURPOSE)
    if decision.get("allowed") is not True:
        raise SystemExit("QUARANTINE_TRAIN_SOURCE_NOT_ALLOWED")
    if decision.get("can_train") is not True:
        raise SystemExit("QUARANTINE_TRAIN_SOURCE_CANNOT_TRAIN")
    if decision.get("can_select_model") is not False:
        raise SystemExit("QUARANTINE_TRAIN_SOURCE_CAN_SELECT_MODEL")
    matrix_sha = canonical_quarantine_matrix_sha256()
    if decision.get("quarantine_matrix_sha256") != matrix_sha:
        raise SystemExit("QUARANTINE_MATRIX_IDENTITY_MISMATCH")

    binding = {
        "binding_id": QUARANTINE_VERIFICATION_ID,
        "quarantine_matrix_sha256": matrix_sha,
        "purpose": QUARANTINE_PURPOSE,
        "source_id": QUARANTINE_SOURCE_ID,
        "allowed": True,
        "can_train": True,
        "can_select_model": False,
    }
    errors = validate_quarantine_binding(binding)
    if errors:
        raise SystemExit("QUARANTINE_BINDING_VALIDATION_FAILED:" + "|".join(errors))

    return {
        "quarantine_verification_id": QUARANTINE_VERIFICATION_ID,
        "status": "PASS",
        "binding": binding,
    }


def construct() -> dict[str, Any]:
    _assert_decision()
    aya43_bundle = reconstruct_aya43_bundle()
    duplicate_report, duplicate_report_sha256 = load_duplicate_evidence()
    contamination = load_contamination_evidence()
    quarantine_verification = build_quarantine_verification()

    entries = aya43_bundle["entries"]
    records = sorted(
        (dict(entry["curriculum_record"]) for entry in entries),
        key=lambda record: record["record_id"],
    )
    if len(records) != 43:
        raise SystemExit("SNAPSHOT_RECORD_COUNT_MISMATCH")
    if [record["record_id"] for record in records] != sorted(record["record_id"] for record in records):
        raise SystemExit("SNAPSHOT_CANONICAL_ORDER_MISMATCH")

    snapshot = build_dataset_snapshot(
        records,
        snapshot_id=SNAPSHOT_ID,
        canonical_order_identity=CANONICAL_ORDER_IDENTITY,
        duplicate_report_id=DUPLICATE_REPORT_ID,
        contamination_report_id=CONTAMINATION_REPORT_ID,
        quarantine_verification_id=QUARANTINE_VERIFICATION_ID,
    )
    errors = validate_dataset_snapshot(snapshot)
    if errors:
        raise SystemExit("DATASET_SNAPSHOT_VALIDATION_FAILED:" + "|".join(errors))
    if snapshot.get("record_count") != 43:
        raise SystemExit("DATASET_SNAPSHOT_RECORD_COUNT_MISMATCH")
    if snapshot.get("rendered_token_count") is not None or snapshot.get("supervised_token_count") is not None:
        raise SystemExit("DATASET_SNAPSHOT_UNAUTHORIZED_TOKEN_COUNTS")
    if snapshot.get("snapshot_sha256") != compute_dataset_snapshot_sha256(snapshot):
        raise SystemExit("DATASET_SNAPSHOT_SHA256_RECOMPUTATION_MISMATCH")

    bundle = {
        "artifact_id": "e004-aya-43-dataset-snapshot-and-supporting-evidence-v1",
        "schema_version": "1",
        "source_aya43_bundle_sha256": EXPECTED_AYA43_BUNDLE_SHA256,
        "eligible_record_count": 43,
        "eligible_record_id_set_sha256": EXPECTED_AYA43_SET_SHA256,
        "near_duplicate_assessment_evidence_id": "e004-aya-43-near-duplicate-assessment-evidence-v1",
        "duplicate_report": duplicate_report,
        "duplicate_report_canonical_sha256": duplicate_report_sha256,
        "contamination_report_id": CONTAMINATION_REPORT_ID,
        "contamination_results_sha256": contamination["contamination_results_sha256"],
        "quarantine_verification": quarantine_verification,
        "quarantine_verification_canonical_sha256": compute_canonical_sha256(
            quarantine_verification
        ),
        "dataset_snapshot": snapshot,
        "dataset_snapshot_sha256": snapshot["snapshot_sha256"],
        "raw_aya_text_persisted": False,
        "user_id_read": False,
        "model_inference_used": False,
        "training_performed": False,
        "current_authorized_spend_usd": 0,
    }
    _assert_safe_repository_object(bundle)
    return bundle


def _write_bundle(path: Path, bundle: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(canonical_json_dumps(bundle) + "\n", encoding="utf-8")


def _bundle_file_sha256(bundle: dict[str, Any]) -> str:
    return hashlib.sha256((canonical_json_dumps(bundle) + "\n").encode("utf-8")).hexdigest()


def validate_committed(path: Path) -> dict[str, Any]:
    expected = construct()
    actual = _load_json(path)
    if actual != expected:
        raise SystemExit("COMMITTED_DATASET_SNAPSHOT_BUNDLE_MISMATCH")
    return actual


def main() -> int:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    construct_parser = subparsers.add_parser("construct")
    construct_parser.add_argument("--out", required=True, type=Path)
    validate_parser = subparsers.add_parser("validate")
    validate_parser.add_argument("--bundle", required=True, type=Path)
    args = parser.parse_args()

    if args.command == "construct":
        bundle = construct()
        _write_bundle(args.out, bundle)
    else:
        bundle = validate_committed(args.bundle)

    print(f"DATASET_SNAPSHOT_RECORD_COUNT={bundle['dataset_snapshot']['record_count']}")
    print(f"DATASET_SNAPSHOT_SHA256={bundle['dataset_snapshot_sha256']}")
    print(f"QUARANTINE_VERIFICATION_STATUS={bundle['quarantine_verification']['status']}")
    print(f"QUARANTINE_MATRIX_SHA256={bundle['quarantine_verification']['binding']['quarantine_matrix_sha256']}")
    print(f"DUPLICATE_REPORT_SHA256={bundle['duplicate_report_canonical_sha256']}")
    print(f"DUPLICATE_REPORT_DISPOSITION={bundle['duplicate_report']['disposition']}")
    print(f"OUTPUT_FILE_SHA256={_bundle_file_sha256(bundle)}")
    print("RAW_AYA_TEXT_PERSISTED=NO")
    print("USER_ID_READ=NO")
    print("MODEL_INFERENCE_USED=NO")
    print("TRAINING_PERFORMED=NO")
    print("CURRENT_AUTHORIZED_SPEND_USD=0")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
