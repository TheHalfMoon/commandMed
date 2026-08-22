from __future__ import annotations

import copy
import json
import math
import unittest
from pathlib import Path

from src.commandmed.tournament import (
    CANONICAL_UPSTREAM_IDENTITIES_V1,
    compute_canonical_tournament_artifact_identities,
    compute_tournament_manifest_sha256,
    compute_tournament_report_sha256,
    evaluate_tournament,
    validate_candidate_result,
    validate_tournament_manifest,
)

ROOT = Path(__file__).resolve().parents[1]


def canonical_artifacts() -> dict:
    return {
        "benchmarks": json.loads((ROOT / "data/eval/benchmarks.json").read_text(encoding="utf-8")),
        "metrics": json.loads((ROOT / "data/eval/metrics.json").read_text(encoding="utf-8")),
        "gold_protocols": json.loads((ROOT / "data/eval/gold_protocols.json").read_text(encoding="utf-8")),
        "quarantine": json.loads((ROOT / "data/eval/quarantine.json").read_text(encoding="utf-8")),
        "safety_policy": json.loads((ROOT / "data/eval/safety_policy.json").read_text(encoding="utf-8")),
        "lineage_contract": json.loads((ROOT / "data/lineage/lineage_contract.json").read_text(encoding="utf-8")),
    }


def safety_scope() -> dict:
    return {
        "scope_id": "fixture-evidence-component-v1",
        "scope_kind": "COMPONENT_QUALIFICATION",
        "claimed_capabilities": ["EVIDENCE_GROUNDED_CLINICAL"],
        "out_of_scope_capabilities": [
            "ARABIC_CLINICAL",
            "PATIENT_CAREGIVER_SAFETY",
            "LAB_DOCUMENT",
        ],
    }


def manifest(**overrides) -> dict:
    value = {
        "tournament_id": "fixture-tournament-001",
        "schema_version": "1.0",
        "execution_mode": "PRECOMPUTED_RESULTS_ONLY",
        "comparison_strategy": "LEXICOGRAPHIC_PREDECLARED",
        "comparison_metric_ids": [
            "active_info_acquisition_efficiency",
            "expected_calibration_error",
        ],
        "candidate_ids": ["fixture-model-a", "fixture-model-b"],
        "tie_policy": "NO_SELECTION_ON_TIE",
        "safety_scope": safety_scope(),
        "canonical_artifact_identities": dict(CANONICAL_UPSTREAM_IDENTITIES_V1),
    }
    value.update(overrides)
    return value


def lineage_record(candidate_id: str, **overrides) -> dict:
    suffix = "a" if candidate_id.endswith("a") else "b"
    revision = suffix * 40
    record = {
        "asset_id": candidate_id,
        "asset_class": "MODEL_OR_CHECKPOINT",
        "canonical_name": f"Fixture Candidate {candidate_id[-1].upper()}",
        "record_version": "1",
        "source_identifier": f"fixture:{candidate_id}",
        "source_uri": f"https://fixtures.example/{candidate_id}",
        "source_revision": revision,
        "source_verification_status": "VERIFIED",
        "source_evidence_uri": f"https://fixtures.example/{candidate_id}/revision/{revision}",
        "declared_use": "DEVELOPMENT_EVALUATION",
        "access_class": "PUBLIC",
        "rights_state": "SUPPORTED",
        "rights_evidence_uri": f"https://fixtures.example/{candidate_id}/rights/{revision}",
        "artifact_binding_state": "IMMUTABLE_REVISION_LOCATOR",
        "artifact_locator": f"artifacts/{candidate_id}.fixture",
        "phi_privacy_state": "NOT_APPLICABLE",
        "purpose": "DEV",
    }
    record.update(overrides)
    return record


def metric_result(status: str, score, evidence: str | None, reason: str = "fixture-only evidence") -> dict:
    return {
        "status": status,
        "score": score,
        "evidence_artifact_id": evidence,
        "reason": reason,
    }


def candidate_result(
    candidate_id: str,
    tournament_manifest: dict,
    *,
    info_score: float = 1.0,
    calibration_score: float = 0.2,
    lineage_overrides: dict | None = None,
) -> dict:
    lineage_overrides = lineage_overrides or {}
    return {
        "candidate_id": candidate_id,
        "tournament_manifest_sha256": compute_tournament_manifest_sha256(tournament_manifest),
        "candidate_lineage_record": lineage_record(candidate_id, **lineage_overrides),
        "metric_results": {
            "citation_entailment_fidelity": metric_result(
                "PASS", 1.0, f"fixture:safety:{candidate_id}"
            ),
            "active_info_acquisition_efficiency": metric_result(
                "PASS", info_score, f"fixture:info:{candidate_id}"
            ),
            "expected_calibration_error": metric_result(
                "PASS", calibration_score, f"fixture:calibration:{candidate_id}"
            ),
        },
    }


class TournamentManifestTests(unittest.TestCase):
    def setUp(self):
        self.artifacts = canonical_artifacts()
        self.manifest = manifest()

    def test_canonical_artifact_identities_are_exactly_pinned(self):
        self.assertEqual(
            compute_canonical_tournament_artifact_identities(self.artifacts),
            CANONICAL_UPSTREAM_IDENTITIES_V1,
        )

    def test_valid_manifest_passes(self):
        self.assertEqual(validate_tournament_manifest(self.manifest, self.artifacts), [])

    def test_candidate_order_is_nonsemantic_for_manifest_identity(self):
        reordered = copy.deepcopy(self.manifest)
        reordered["candidate_ids"].reverse()
        self.assertEqual(
            compute_tournament_manifest_sha256(self.manifest),
            compute_tournament_manifest_sha256(reordered),
        )

    def test_comparison_metric_order_is_semantic(self):
        reordered = copy.deepcopy(self.manifest)
        reordered["comparison_metric_ids"].reverse()
        self.assertNotEqual(
            compute_tournament_manifest_sha256(self.manifest),
            compute_tournament_manifest_sha256(reordered),
        )

    def test_duplicate_candidate_id_fails(self):
        bad = copy.deepcopy(self.manifest)
        bad["candidate_ids"].append("fixture-model-a")
        self.assertTrue(any("duplicate candidate" in error for error in validate_tournament_manifest(bad, self.artifacts)))

    def test_duplicate_comparison_metric_fails(self):
        bad = copy.deepcopy(self.manifest)
        bad["comparison_metric_ids"].append("active_info_acquisition_efficiency")
        self.assertTrue(any("duplicates" in error for error in validate_tournament_manifest(bad, self.artifacts)))

    def test_unknown_top_level_field_fails(self):
        bad = copy.deepcopy(self.manifest)
        bad["runner"] = "not-authorized"
        self.assertTrue(any("unknown fields" in error for error in validate_tournament_manifest(bad, self.artifacts)))

    def test_nested_execution_surface_key_fails(self):
        bad = copy.deepcopy(self.manifest)
        bad["safety_scope"]["prompt"] = "do not execute"
        self.assertTrue(any("prohibited execution/payload key" in error for error in validate_tournament_manifest(bad, self.artifacts)))

    def test_noncanonical_but_valid_artifact_bundle_fails_exact_pin(self):
        bad_artifacts = copy.deepcopy(self.artifacts)
        bad_artifacts["benchmarks"][0]["notes"] += " representation remains valid but semantics changed"
        errors = validate_tournament_manifest(self.manifest, bad_artifacts)
        self.assertTrue(any("CANONICAL_UPSTREAM_IDENTITIES_V1" in error for error in errors))

    def test_manifest_cannot_declare_alternate_identity_map(self):
        bad = copy.deepcopy(self.manifest)
        bad["canonical_artifact_identities"]["metrics_sha256"] = "0" * 64
        errors = validate_tournament_manifest(bad, self.artifacts)
        self.assertTrue(any("must equal CANONICAL_UPSTREAM_IDENTITIES_V1" in error for error in errors))

    def test_hard_gate_cannot_be_ranking_metric(self):
        bad = copy.deepcopy(self.manifest)
        bad["comparison_metric_ids"] = ["citation_entailment_fidelity"]
        self.assertTrue(any("hard-gate metric" in error for error in validate_tournament_manifest(bad, self.artifacts)))

    def test_wrong_execution_mode_strategy_and_tie_policy_fail(self):
        mutations = {
            "execution_mode": "RUN_MODELS",
            "comparison_strategy": "WEIGHTED_SUM",
            "tie_policy": "CANDIDATE_ID",
        }
        for field, value in mutations.items():
            with self.subTest(field=field):
                bad = copy.deepcopy(self.manifest)
                bad[field] = value
                self.assertTrue(validate_tournament_manifest(bad, self.artifacts))


class CandidateQualificationTests(unittest.TestCase):
    def setUp(self):
        self.artifacts = canonical_artifacts()
        self.manifest = manifest()

    def good(self, candidate_id: str = "fixture-model-a", **kwargs) -> dict:
        return candidate_result(candidate_id, self.manifest, **kwargs)

    def test_valid_candidate_passes_public_validator(self):
        self.assertEqual(validate_candidate_result(self.good(), self.manifest, self.artifacts), [])

    def test_wrong_manifest_digest_is_incomplete_and_blocks_selection(self):
        a = self.good("fixture-model-a", info_score=2.0)
        b = self.good("fixture-model-b", info_score=1.0)
        b["tournament_manifest_sha256"] = "0" * 64
        report = evaluate_tournament(self.manifest, [a, b], self.artifacts)
        self.assertEqual(report["tournament_state"], "NO_SELECTION")
        self.assertEqual(report["reason_code"], "CANDIDATE_EVIDENCE_INCOMPLETE")
        by_id = {item["candidate_id"]: item for item in report["candidate_reports"]}
        self.assertEqual(by_id["fixture-model-b"]["state"], "INCOMPLETE")
        self.assertIn("MANIFEST_IDENTITY_MISMATCH", by_id["fixture-model-b"]["reason_codes"])

    def test_prohibited_lineage_is_disqualified_and_other_candidate_can_win(self):
        a = self.good("fixture-model-a", info_score=2.0)
        b = self.good(
            "fixture-model-b",
            info_score=9.0,
            lineage_overrides={"rights_state": "INCOMPATIBLE"},
        )
        report = evaluate_tournament(self.manifest, [a, b], self.artifacts)
        self.assertEqual(report["tournament_state"], "SELECTED")
        self.assertEqual(report["selected_candidate_id"], "fixture-model-a")
        by_id = {item["candidate_id"]: item for item in report["candidate_reports"]}
        self.assertEqual(by_id["fixture-model-b"]["state"], "DISQUALIFIED")
        self.assertEqual(by_id["fixture-model-b"]["lineage_state"], "PROHIBITED")

    def test_reference_only_lineage_is_disqualified_not_incomplete(self):
        a = self.good("fixture-model-a", info_score=2.0)
        b = self.good(
            "fixture-model-b",
            info_score=9.0,
            lineage_overrides={"access_class": "REFERENCE_ONLY"},
        )
        report = evaluate_tournament(self.manifest, [a, b], self.artifacts)
        self.assertEqual(report["tournament_state"], "SELECTED")
        self.assertEqual(report["selected_candidate_id"], "fixture-model-a")
        by_id = {item["candidate_id"]: item for item in report["candidate_reports"]}
        self.assertEqual(by_id["fixture-model-b"]["state"], "DISQUALIFIED")
        self.assertEqual(by_id["fixture-model-b"]["lineage_state"], "REFERENCE_ONLY")

    def test_blocked_lineage_forces_no_selection(self):
        a = self.good("fixture-model-a", info_score=2.0)
        b = self.good(
            "fixture-model-b",
            info_score=1.0,
            lineage_overrides={"source_verification_status": "UNRESOLVED"},
        )
        report = evaluate_tournament(self.manifest, [a, b], self.artifacts)
        self.assertEqual(report["reason_code"], "CANDIDATE_EVIDENCE_INCOMPLETE")
        by_id = {item["candidate_id"]: item for item in report["candidate_reports"]}
        self.assertEqual(by_id["fixture-model-b"]["state"], "INCOMPLETE")
        self.assertEqual(by_id["fixture-model-b"]["lineage_state"], "BLOCKED")

    def test_safety_fail_disqualifies_candidate(self):
        a = self.good("fixture-model-a", info_score=2.0)
        b = self.good("fixture-model-b", info_score=9.0)
        b["metric_results"]["citation_entailment_fidelity"] = metric_result(
            "FAIL", 0.0, "fixture:safety:failed"
        )
        report = evaluate_tournament(self.manifest, [a, b], self.artifacts)
        self.assertEqual(report["tournament_state"], "SELECTED")
        self.assertEqual(report["selected_candidate_id"], "fixture-model-a")
        by_id = {item["candidate_id"]: item for item in report["candidate_reports"]}
        self.assertEqual(by_id["fixture-model-b"]["state"], "DISQUALIFIED")
        self.assertEqual(by_id["fixture-model-b"]["safety_state"], "FAIL")

    def test_missing_safety_evidence_is_incomplete(self):
        a = self.good("fixture-model-a", info_score=2.0)
        b = self.good("fixture-model-b", info_score=1.0)
        del b["metric_results"]["citation_entailment_fidelity"]
        report = evaluate_tournament(self.manifest, [a, b], self.artifacts)
        self.assertEqual(report["reason_code"], "CANDIDATE_EVIDENCE_INCOMPLETE")
        by_id = {item["candidate_id"]: item for item in report["candidate_reports"]}
        self.assertEqual(by_id["fixture-model-b"]["state"], "INCOMPLETE")
        self.assertEqual(by_id["fixture-model-b"]["safety_state"], "INSUFFICIENT_EVIDENCE")

    def test_missing_comparison_metric_is_incomplete(self):
        a = self.good("fixture-model-a", info_score=2.0)
        b = self.good("fixture-model-b", info_score=1.0)
        del b["metric_results"]["expected_calibration_error"]
        report = evaluate_tournament(self.manifest, [a, b], self.artifacts)
        self.assertEqual(report["reason_code"], "CANDIDATE_EVIDENCE_INCOMPLETE")
        by_id = {item["candidate_id"]: item for item in report["candidate_reports"]}
        self.assertIn("COMPARISON_EVIDENCE_INVALID", by_id["fixture-model-b"]["reason_codes"])

    def test_nonfinite_comparison_score_is_incomplete(self):
        for value in (math.nan, math.inf, -math.inf):
            with self.subTest(value=value):
                a = self.good("fixture-model-a", info_score=2.0)
                b = self.good("fixture-model-b", info_score=1.0)
                b["metric_results"]["expected_calibration_error"]["score"] = value
                report = evaluate_tournament(self.manifest, [a, b], self.artifacts)
                self.assertEqual(report["reason_code"], "CANDIDATE_EVIDENCE_INCOMPLETE")

    def test_missing_comparison_evidence_identity_is_incomplete(self):
        a = self.good("fixture-model-a", info_score=2.0)
        b = self.good("fixture-model-b", info_score=1.0)
        b["metric_results"]["expected_calibration_error"]["evidence_artifact_id"] = "UNRESOLVED"
        report = evaluate_tournament(self.manifest, [a, b], self.artifacts)
        self.assertEqual(report["reason_code"], "CANDIDATE_EVIDENCE_INCOMPLETE")

    def test_candidate_cannot_change_asset_class_or_declared_use(self):
        for field, value in (
            ("asset_class", "DATASET_OR_CORPUS"),
            ("declared_use", "TRAINING_OR_ADAPTATION"),
        ):
            with self.subTest(field=field):
                result = self.good()
                result["candidate_lineage_record"][field] = value
                errors = validate_candidate_result(result, self.manifest, self.artifacts)
                self.assertTrue(any(field in error for error in errors))

    def test_candidate_result_rejects_nested_payload_channel(self):
        result = self.good()
        result["candidate_lineage_record"]["model_output"] = "fixture text"
        errors = validate_candidate_result(result, self.manifest, self.artifacts)
        self.assertTrue(any("prohibited execution/payload key" in error for error in errors))


class TournamentComparisonTests(unittest.TestCase):
    def setUp(self):
        self.artifacts = canonical_artifacts()
        self.manifest = manifest()

    def result(self, candidate_id: str, info: float, calibration: float) -> dict:
        return candidate_result(
            candidate_id,
            self.manifest,
            info_score=info,
            calibration_score=calibration,
        )

    def test_unique_higher_better_candidate_is_selected(self):
        report = evaluate_tournament(
            self.manifest,
            [self.result("fixture-model-a", 2.0, 0.9), self.result("fixture-model-b", 1.0, 0.1)],
            self.artifacts,
        )
        self.assertEqual(report["tournament_state"], "SELECTED")
        self.assertEqual(report["selected_candidate_id"], "fixture-model-a")

    def test_lower_better_direction_breaks_second_metric_tie(self):
        report = evaluate_tournament(
            self.manifest,
            [self.result("fixture-model-a", 2.0, 0.4), self.result("fixture-model-b", 2.0, 0.2)],
            self.artifacts,
        )
        self.assertEqual(report["selected_candidate_id"], "fixture-model-b")

    def test_lexicographic_first_metric_dominates_later_metric(self):
        report = evaluate_tournament(
            self.manifest,
            [self.result("fixture-model-a", 2.0, 0.99), self.result("fixture-model-b", 1.0, 0.01)],
            self.artifacts,
        )
        self.assertEqual(report["selected_candidate_id"], "fixture-model-a")

    def test_exact_top_tie_never_uses_candidate_id_as_tiebreaker(self):
        report = evaluate_tournament(
            self.manifest,
            [self.result("fixture-model-a", 2.0, 0.2), self.result("fixture-model-b", 2.0, 0.2)],
            self.artifacts,
        )
        self.assertEqual(report["tournament_state"], "NO_SELECTION")
        self.assertEqual(report["reason_code"], "TOP_TIE")
        self.assertIsNone(report["selected_candidate_id"])

    def test_missing_declared_candidate_forces_no_selection(self):
        report = evaluate_tournament(
            self.manifest,
            [self.result("fixture-model-a", 2.0, 0.2)],
            self.artifacts,
        )
        self.assertEqual(report["reason_code"], "CANDIDATE_EVIDENCE_INCOMPLETE")
        by_id = {item["candidate_id"]: item for item in report["candidate_reports"]}
        self.assertEqual(by_id["fixture-model-b"]["state"], "INCOMPLETE")
        self.assertIn("MISSING_CANDIDATE_RESULT", by_id["fixture-model-b"]["reason_codes"])

    def test_duplicate_candidate_result_invalidates_result_set(self):
        a = self.result("fixture-model-a", 2.0, 0.2)
        b = self.result("fixture-model-b", 1.0, 0.3)
        report = evaluate_tournament(self.manifest, [a, copy.deepcopy(a), b], self.artifacts)
        self.assertEqual(report["reason_code"], "CANDIDATE_RESULT_SET_INVALID")
        self.assertTrue(any("duplicate candidate result" in error for error in report["result_set_errors"]))

    def test_unknown_extra_candidate_invalidates_result_set(self):
        a = self.result("fixture-model-a", 2.0, 0.2)
        b = self.result("fixture-model-b", 1.0, 0.3)
        extra = copy.deepcopy(a)
        extra["candidate_id"] = "fixture-model-extra"
        report = evaluate_tournament(self.manifest, [a, b, extra], self.artifacts)
        self.assertEqual(report["reason_code"], "CANDIDATE_RESULT_SET_INVALID")

    def test_candidate_input_order_does_not_change_report_or_identity(self):
        a = self.result("fixture-model-a", 2.0, 0.2)
        b = self.result("fixture-model-b", 1.0, 0.3)
        first = evaluate_tournament(self.manifest, [a, b], self.artifacts)
        second = evaluate_tournament(self.manifest, [b, a], self.artifacts)
        self.assertEqual(first, second)
        self.assertEqual(first["report_sha256"], second["report_sha256"])

    def test_report_hash_is_non_self_referential(self):
        report = evaluate_tournament(
            self.manifest,
            [self.result("fixture-model-a", 2.0, 0.2), self.result("fixture-model-b", 1.0, 0.3)],
            self.artifacts,
        )
        self.assertEqual(compute_tournament_report_sha256(report), report["report_sha256"])
        mutated_self = copy.deepcopy(report)
        mutated_self["report_sha256"] = "0" * 64
        self.assertEqual(compute_tournament_report_sha256(mutated_self), report["report_sha256"])

    def test_semantic_report_mutation_changes_identity(self):
        report = evaluate_tournament(
            self.manifest,
            [self.result("fixture-model-a", 2.0, 0.2), self.result("fixture-model-b", 1.0, 0.3)],
            self.artifacts,
        )
        mutated = copy.deepcopy(report)
        mutated["selected_candidate_id"] = "fixture-model-b"
        self.assertNotEqual(compute_tournament_report_sha256(mutated), report["report_sha256"])

    def test_invalid_manifest_returns_no_selection_without_candidate_ranking(self):
        bad = copy.deepcopy(self.manifest)
        bad["execution_mode"] = "RUN_MODELS"
        report = evaluate_tournament(bad, [], self.artifacts)
        self.assertEqual(report["tournament_state"], "NO_SELECTION")
        self.assertEqual(report["reason_code"], "INVALID_MANIFEST_OR_PROTOCOL")
        self.assertEqual(report["candidate_reports"], [])


if __name__ == "__main__":
    unittest.main()
