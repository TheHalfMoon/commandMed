from __future__ import annotations

import copy
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

from scripts.e004_aya_43_dataset_snapshot_v1 import (
    CANONICAL_ORDER_IDENTITY,
    CONTAMINATION_REPORT_ID,
    EXPECTED_AYA43_SET_SHA256,
    EXPECTED_DUPLICATE_REPORT_SHA256,
    QUARANTINE_SOURCE_ID,
    QUARANTINE_VERIFICATION_ID,
    SNAPSHOT_ID,
    build_quarantine_verification,
    construct,
    load_duplicate_evidence,
    reconstruct_aya43_bundle,
)
from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.curriculum import validate_duplicate_contamination_report
from src.commandmed.spec007.quarantine import validate_quarantine_binding
from src.commandmed.spec007.snapshot import (
    compute_dataset_snapshot_sha256,
    validate_dataset_snapshot,
)


class Aya43DatasetSnapshotV1Tests(unittest.TestCase):
    def test_reconstructed_bundle_is_exact_safe_aya43_subject(self) -> None:
        bundle = reconstruct_aya43_bundle()
        self.assertEqual(43, bundle["eligible_record_count"])
        self.assertEqual(EXPECTED_AYA43_SET_SHA256, bundle["eligible_record_id_set_sha256"])
        self.assertFalse(bundle["raw_aya_text_persisted"])
        self.assertFalse(bundle["user_id_read"])
        self.assertFalse(bundle["remote_model_or_ai_record_processing"])

    def test_duplicate_report_is_exact_pass_and_hash_bound(self) -> None:
        report, digest = load_duplicate_evidence()
        self.assertEqual("PASS", report["disposition"])
        self.assertEqual([], report["near_duplicate_groups"])
        self.assertEqual([], report["benchmark_overlap_findings"])
        self.assertEqual(EXPECTED_DUPLICATE_REPORT_SHA256, digest)
        self.assertEqual(digest, compute_canonical_sha256(report))
        self.assertEqual([], validate_duplicate_contamination_report(report))

    def test_duplicate_report_tamper_fails_closed(self) -> None:
        report, _ = load_duplicate_evidence()
        evidence_path = Path(tempfile.mkdtemp()) / "near-dup.json"
        tampered = {
            "artifact_id": "e004-aya-43-near-duplicate-assessment-evidence-v1",
            "candidate_content_sha256_set_sha256": "ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64",
            "candidate_manifest_canonical_sha256": "dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99",
            "candidate_record_id_set_sha256": "d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83",
            "compare_fields": ["inputs", "targets"],
            "duplicate_report": copy.deepcopy(report),
            "duplicate_report_canonical_sha256": EXPECTED_DUPLICATE_REPORT_SHA256,
            "input_window_count": 46,
            "matched_ngram_persisted": False,
            "method_id": "AYA_43_INTERNAL_13_TOKEN_EXACT_NEAR_DUPLICATE_V1",
            "model_inference_used": False,
            "near_duplicate_pair_count": 0,
            "near_duplicate_pair_count_by_field": {},
            "ngram_length_tokens": 13,
            "normalization": "UNICODE_NFKC_CASEFOLD",
            "raw_text_persisted": False,
            "schema_version": "1",
            "selected_record_count": 43,
            "selected_record_id_set_sha256": EXPECTED_AYA43_SET_SHA256,
            "semantic_judge_used": False,
            "source_file_sha256": "51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06",
            "target_window_count": 480,
            "tokenization": "PYTHON_UNICODE_REGEX_WORD_TOKENS",
            "user_id_read": False,
        }
        tampered["duplicate_report"]["near_duplicate_groups"] = [["a", "b"]]
        evidence_path.write_text(json.dumps(tampered), encoding="utf-8")
        with patch("scripts.e004_aya_43_dataset_snapshot_v1.NEAR_DUP_PATH", evidence_path):
            with self.assertRaises(SystemExit):
                load_duplicate_evidence()

    def test_quarantine_verification_is_exact_train_binding(self) -> None:
        verification = build_quarantine_verification()
        self.assertEqual(QUARANTINE_VERIFICATION_ID, verification["quarantine_verification_id"])
        self.assertEqual("PASS", verification["status"])
        self.assertEqual(QUARANTINE_SOURCE_ID, verification["binding"]["source_id"])
        self.assertEqual("TRAIN", verification["binding"]["purpose"])
        self.assertTrue(verification["binding"]["allowed"])
        self.assertTrue(verification["binding"]["can_train"])
        self.assertFalse(verification["binding"]["can_select_model"])
        self.assertEqual([], validate_quarantine_binding(verification["binding"]))

    def test_constructed_snapshot_is_exact_ordered_and_valid(self) -> None:
        bundle = construct()
        snapshot = bundle["dataset_snapshot"]
        self.assertEqual(SNAPSHOT_ID, snapshot["snapshot_id"])
        self.assertEqual(CANONICAL_ORDER_IDENTITY, snapshot["canonical_order_identity"])
        self.assertEqual(43, snapshot["record_count"])
        self.assertEqual(snapshot["record_ids"], sorted(snapshot["record_ids"]))
        self.assertEqual(CONTAMINATION_REPORT_ID, snapshot["contamination_report_id"])
        self.assertEqual(QUARANTINE_VERIFICATION_ID, snapshot["quarantine_verification_id"])
        self.assertIsNone(snapshot["rendered_token_count"])
        self.assertIsNone(snapshot["supervised_token_count"])
        self.assertEqual([], validate_dataset_snapshot(snapshot))
        self.assertEqual(snapshot["snapshot_sha256"], compute_dataset_snapshot_sha256(snapshot))
        self.assertFalse(bundle["raw_aya_text_persisted"])
        self.assertFalse(bundle["user_id_read"])
        self.assertFalse(bundle["model_inference_used"])
        self.assertFalse(bundle["training_performed"])
        self.assertEqual(0, bundle["current_authorized_spend_usd"])


if __name__ == "__main__":
    unittest.main()
