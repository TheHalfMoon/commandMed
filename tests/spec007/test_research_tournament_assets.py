"""Offline qualification tests for SP007-RO-001 evaluation-asset freeze.

These tests validate only repository-authored non-clinical synthetic evaluation
fixtures and metadata. They do not load models, execute inference, start training,
access protected data, or select a winner.
"""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.research_tournament_assets import (
    CONTAMINATION_METHOD_ID,
    E001_CANDIDATE_MANIFEST_SHA256,
    E001_CANDIDATE_MANIFEST_VERSION,
    EXPECTED_QUARANTINE_MATRIX_SHA256,
    RIGHTS_INSTRUMENT_ID,
    build_protocol_asset_manifest,
    compute_contamination_method_sha256,
    compute_research_component_evaluation_asset_set_sha256,
    compute_research_component_evaluation_asset_sha256,
    compute_rights_instrument_sha256,
    evaluate_research_component_asset_admission,
    validate_frozen_research_component_tournament_subject,
    validate_research_component_contamination_method,
    validate_research_component_evaluation_asset,
    validate_research_component_evaluation_asset_set,
    validate_research_component_evaluation_rights_instrument,
)

ROOT = Path(__file__).resolve().parents[2]
SPEC = ROOT / "specs" / "007-sft-v1"


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


RIGHTS = load_json(
    SPEC / "e004-research-component-evaluation-asset-rights-instrument-v1.json"
)
CONTAMINATION = load_json(
    SPEC / "e004-research-component-evaluation-asset-contamination-method-v1.json"
)
ASSET_SET = load_json(
    SPEC / "e004-research-component-tournament-evaluation-assets-v1.json"
)
PROTOCOL = load_json(SPEC / "e004-research-component-tournament-protocol-v1.json")
LINEAGE_CONTRACT = load_json(ROOT / "data" / "lineage" / "lineage_contract.json")


class ResearchComponentEvaluationAssetFreezeTests(unittest.TestCase):
    def test_rights_instrument_is_exact_and_self_hashed(self):
        errors = validate_research_component_evaluation_rights_instrument(RIGHTS)
        self.assertEqual(
            errors,
            [],
            msg=(
                f"claimed={RIGHTS.get('instrument_sha256')} "
                f"computed={compute_rights_instrument_sha256(RIGHTS)} errors={errors}"
            ),
        )
        self.assertFalse(RIGHTS["training_or_adaptation_use_authorized"])
        self.assertFalse(RIGHTS["redistribution_rights_claim_created"])
        self.assertFalse(RIGHTS["commercial_rights_claim_created"])

    def test_contamination_method_is_exact_narrow_and_self_hashed(self):
        errors = validate_research_component_contamination_method(CONTAMINATION)
        self.assertEqual(
            errors,
            [],
            msg=(
                f"claimed={CONTAMINATION.get('method_sha256')} "
                f"computed={compute_contamination_method_sha256(CONTAMINATION)} "
                f"errors={errors}"
            ),
        )
        self.assertEqual(
            CONTAMINATION["pass_semantics"],
            "EXACT_FIXTURE_NONEXPOSURE_AND_NONADAPTIVE_PRE_RESULT_FREEZE_ONLY",
        )
        self.assertFalse(CONTAMINATION["semantic_task_novelty_claim"])
        self.assertFalse(CONTAMINATION["candidate_pretraining_corpus_inspection_claim"])
        self.assertFalse(CONTAMINATION["private_gold_comparison"])
        self.assertEqual(
            CONTAMINATION["candidate_manifest_version"],
            E001_CANDIDATE_MANIFEST_VERSION,
        )
        self.assertEqual(
            CONTAMINATION["candidate_manifest_sha256"],
            E001_CANDIDATE_MANIFEST_SHA256,
        )

    def test_asset_set_is_exactly_self_hashed(self):
        errors = validate_research_component_evaluation_asset_set(ASSET_SET)
        diagnostics = [
            {
                "asset_id": asset.get("asset_id"),
                "claimed": asset.get("asset_sha256"),
                "computed": compute_research_component_evaluation_asset_sha256(asset),
            }
            for asset in ASSET_SET.get("asset_records", [])
            if isinstance(asset, dict)
        ]
        self.assertEqual(
            errors,
            [],
            msg=(
                f"asset_set_claimed={ASSET_SET.get('asset_set_sha256')} "
                f"asset_set_computed={compute_research_component_evaluation_asset_set_sha256(ASSET_SET)} "
                f"asset_hashes={diagnostics} errors={errors}"
            ),
        )

    def test_every_asset_is_spec003_selection_eligible(self):
        for asset in ASSET_SET["asset_records"]:
            with self.subTest(asset_id=asset["asset_id"]):
                self.assertEqual(validate_research_component_evaluation_asset(asset), [])
                result = evaluate_research_component_asset_admission(
                    asset, LINEAGE_CONTRACT
                )
                self.assertEqual(
                    result.get("state"),
                    "ELIGIBLE",
                    msg=f"asset_id={asset['asset_id']} result={result}",
                )
                self.assertEqual(asset["split_id"], "MODEL_SELECTION_DEV_SET")
                self.assertEqual(asset["quarantine_purpose"], "CHECKPOINT_SELECTION")
                self.assertEqual(
                    asset["quarantine_matrix_sha256"],
                    EXPECTED_QUARANTINE_MATRIX_SHA256,
                )
                self.assertFalse(asset["optimization_feedback_allowed"])
                self.assertFalse(asset["candidate_outputs_observed_before_freeze"])
                self.assertFalse(asset["external_payloads_used"])

    def test_protocol_is_derived_from_exact_admitted_asset_set(self):
        errors = validate_frozen_research_component_tournament_subject(
            rights_instrument=RIGHTS,
            contamination_method=CONTAMINATION,
            asset_set=ASSET_SET,
            protocol=PROTOCOL,
            lineage_contract=LINEAGE_CONTRACT,
        )
        self.assertEqual(
            errors,
            [],
            msg=(
                f"protocol_claimed={PROTOCOL.get('protocol_sha256')} "
                f"protocol_computed={compute_canonical_sha256({k: v for k, v in PROTOCOL.items() if k != 'protocol_sha256'})} "
                f"errors={errors}"
            ),
        )
        expected = [
            build_protocol_asset_manifest(asset) for asset in ASSET_SET["asset_records"]
        ]
        self.assertEqual(PROTOCOL["evaluation_asset_manifests"], expected)
        self.assertTrue(PROTOCOL["pre_result_freeze"])
        self.assertFalse(PROTOCOL["candidate_result_visibility_before_freeze"])
        self.assertFalse(PROTOCOL["winner_selection_performed_by_protocol"])
        self.assertFalse(PROTOCOL["private_gold_allowed"])
        self.assertEqual(PROTOCOL["clinical_metric_ids_allowed"], [])
        self.assertEqual(PROTOCOL["authorized_spend_usd"], 0)

    def test_candidate_result_exposure_fails_closed(self):
        bad = copy.deepcopy(ASSET_SET)
        bad["asset_records"][0]["candidate_outputs_observed_before_freeze"] = True
        bad["asset_records"][0]["asset_sha256"] = (
            compute_research_component_evaluation_asset_sha256(
                bad["asset_records"][0]
            )
        )
        bad["asset_set_sha256"] = compute_research_component_evaluation_asset_set_sha256(
            bad
        )
        errors = validate_research_component_evaluation_asset_set(bad)
        self.assertTrue(any("candidate_outputs_observed_before_freeze" in e for e in errors))

    def test_external_payload_use_fails_closed(self):
        bad = copy.deepcopy(ASSET_SET["asset_records"][0])
        bad["external_payloads_used"] = True
        bad["asset_sha256"] = compute_research_component_evaluation_asset_sha256(bad)
        errors = validate_research_component_evaluation_asset(bad)
        self.assertTrue(any("external_payloads_used" in e for e in errors))

    def test_case_nonce_tamper_fails_closed(self):
        bad = copy.deepcopy(ASSET_SET["asset_records"][0])
        bad["cases"][0]["case_nonce"] = "0" * 16
        bad["asset_sha256"] = compute_research_component_evaluation_asset_sha256(bad)
        errors = validate_research_component_evaluation_asset(bad)
        self.assertTrue(any("case_nonce mismatch" in e for e in errors))

    def test_clinical_content_injection_fails_closed(self):
        bad = copy.deepcopy(ASSET_SET["asset_records"][0])
        bad["cases"][0]["prompt"] += " patient diagnosis"
        bad["asset_sha256"] = compute_research_component_evaluation_asset_sha256(bad)
        errors = validate_research_component_evaluation_asset(bad)
        self.assertTrue(any("clinical content is prohibited" in e for e in errors))

    def test_non_clinical_descriptor_does_not_trigger_positive_clinical_marker(self):
        english = next(
            asset
            for asset in ASSET_SET["asset_records"]
            if asset["metric_family"] == "GENERAL_ENGLISH_LANGUAGE"
        )
        self.assertEqual(validate_research_component_evaluation_asset(english), [])
        bad = copy.deepcopy(english)
        bad["cases"][0]["prompt"] = bad["cases"][0]["prompt"].replace(
            "non-clinical", "clinical", 1
        )
        bad["asset_sha256"] = compute_research_component_evaluation_asset_sha256(bad)
        errors = validate_research_component_evaluation_asset(bad)
        self.assertTrue(any("clinical content is prohibited" in e for e in errors))

    def test_protocol_manifest_drift_fails_closed(self):
        bad_protocol = copy.deepcopy(PROTOCOL)
        bad_protocol["evaluation_asset_manifests"][0]["content_sha256"] = "0" * 64
        bad_protocol["protocol_sha256"] = compute_canonical_sha256(
            {k: v for k, v in bad_protocol.items() if k != "protocol_sha256"}
        )
        errors = validate_frozen_research_component_tournament_subject(
            rights_instrument=RIGHTS,
            contamination_method=CONTAMINATION,
            asset_set=ASSET_SET,
            protocol=bad_protocol,
            lineage_contract=LINEAGE_CONTRACT,
        )
        self.assertTrue(any("evaluation_asset_manifests" in e for e in errors))

    def test_rights_instrument_does_not_expand_downstream_authority(self):
        self.assertEqual(RIGHTS["instrument_id"], RIGHTS_INSTRUMENT_ID)
        self.assertEqual(RIGHTS["permitted_use"], "COMPONENT_TOURNAMENT_SELECTION")
        self.assertFalse(RIGHTS["training_or_adaptation_use_authorized"])
        self.assertFalse(RIGHTS["redistribution_rights_claim_created"])
        self.assertFalse(RIGHTS["commercial_rights_claim_created"])
        self.assertEqual(RIGHTS["current_authorized_spend_usd"], 0)

    def test_contamination_method_identity_is_bound(self):
        self.assertEqual(CONTAMINATION["method_id"], CONTAMINATION_METHOD_ID)
        self.assertTrue(CONTAMINATION["fixture_construction_after_candidate_freeze"])
        self.assertFalse(CONTAMINATION["candidate_outputs_observed_before_fixture_freeze"])
        self.assertFalse(CONTAMINATION["adaptive_generation_from_candidate_outputs"])
        self.assertFalse(CONTAMINATION["external_payloads_used"])


if __name__ == "__main__":
    unittest.main()
