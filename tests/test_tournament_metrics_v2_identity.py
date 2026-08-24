from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.tournament import (
    CANONICAL_METRICS_V2_BINDING,
    CANONICAL_UPSTREAM_IDENTITIES_V1,
    compute_canonical_tournament_artifact_identities,
    validate_metrics_v2_consumer_binding,
    validate_tournament_manifest,
)

ROOT = Path(__file__).resolve().parents[1]
V1_SHA256 = "304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a"
V2_SCHEMA_ID = "commandmed-metrics-catalog"
V2_SCHEMA_VERSION = "2.0"
V2_CATALOG_PATH = "data/eval/metrics-v2.json"


def load_json(path: str):
    return json.loads((ROOT / path).read_text(encoding="utf-8"))


def canonical_artifacts() -> dict:
    return {
        "benchmarks": load_json("data/eval/benchmarks.json"),
        "metrics": load_json("data/eval/metrics.json"),
        "gold_protocols": load_json("data/eval/gold_protocols.json"),
        "quarantine": load_json("data/eval/quarantine.json"),
        "safety_policy": load_json("data/eval/safety_policy.json"),
        "lineage_contract": load_json("data/lineage/lineage_contract.json"),
    }


def manifest() -> dict:
    return {
        "tournament_id": "fixture-v1-identity-preservation",
        "schema_version": "1.0",
        "execution_mode": "PRECOMPUTED_RESULTS_ONLY",
        "comparison_strategy": "LEXICOGRAPHIC_PREDECLARED",
        "comparison_metric_ids": [
            "active_info_acquisition_efficiency",
            "expected_calibration_error",
        ],
        "candidate_ids": ["fixture-model-a", "fixture-model-b"],
        "tie_policy": "NO_SELECTION_ON_TIE",
        "safety_scope": {
            "scope_id": "fixture-evidence-component-v1",
            "scope_kind": "COMPONENT_QUALIFICATION",
            "claimed_capabilities": ["EVIDENCE_GROUNDED_CLINICAL"],
            "out_of_scope_capabilities": [
                "ARABIC_CLINICAL",
                "PATIENT_CAREGIVER_SAFETY",
                "LAB_DOCUMENT",
            ],
        },
        "canonical_artifact_identities": dict(CANONICAL_UPSTREAM_IDENTITIES_V1),
    }


class TournamentMetricsV2IdentityTests(unittest.TestCase):
    def setUp(self):
        self.v1_artifacts = canonical_artifacts()
        self.v2_catalog = load_json(V2_CATALOG_PATH)
        self.v2_sha256 = compute_canonical_sha256(self.v2_catalog)

    def test_historical_v1_identity_map_and_behavior_are_unchanged(self):
        self.assertEqual(CANONICAL_UPSTREAM_IDENTITIES_V1["metrics_sha256"], V1_SHA256)
        self.assertEqual(
            compute_canonical_tournament_artifact_identities(self.v1_artifacts),
            CANONICAL_UPSTREAM_IDENTITIES_V1,
        )
        self.assertEqual(validate_tournament_manifest(manifest(), self.v1_artifacts), [])

    def test_v2_binding_is_exactly_identity_bound(self):
        self.assertEqual(
            CANONICAL_METRICS_V2_BINDING,
            {
                "metrics_contract_schema_id": V2_SCHEMA_ID,
                "metrics_contract_schema_version": V2_SCHEMA_VERSION,
                "metrics_catalog_path": V2_CATALOG_PATH,
                "metrics_catalog_sha256": self.v2_sha256,
            },
        )
        self.assertEqual(
            validate_metrics_v2_consumer_binding(
                dict(CANONICAL_METRICS_V2_BINDING), self.v2_catalog
            ),
            [],
        )

    def test_v2_sha_path_and_schema_version_mismatches_fail_closed(self):
        mutations = {
            "metrics_catalog_sha256": "0" * 64,
            "metrics_catalog_path": "data/eval/metrics.json",
            "metrics_contract_schema_version": "1.0",
            "metrics_contract_schema_id": "latest",
        }
        for field, value in mutations.items():
            with self.subTest(field=field):
                bad = dict(CANONICAL_METRICS_V2_BINDING)
                bad[field] = value
                self.assertTrue(validate_metrics_v2_consumer_binding(bad, self.v2_catalog))

    def test_v2_binding_rejects_v1_fallback(self):
        bad = dict(CANONICAL_METRICS_V2_BINDING)
        bad["metrics_catalog_path"] = "data/eval/metrics.json"
        bad["metrics_catalog_sha256"] = V1_SHA256
        errors = validate_metrics_v2_consumer_binding(bad, self.v2_catalog)
        self.assertTrue(errors)

    def test_v1_consumer_rejects_v2_fall_forward(self):
        bad_artifacts = copy.deepcopy(self.v1_artifacts)
        bad_artifacts["metrics"] = self.v2_catalog
        errors = validate_tournament_manifest(manifest(), bad_artifacts)
        self.assertTrue(errors)
        self.assertTrue(
            any(
                "metrics" in error.lower()
                or "CANONICAL_UPSTREAM_IDENTITIES_V1" in error
                for error in errors
            )
        )

    def test_v2_binding_rejects_catalog_semantic_mutation(self):
        mutated = copy.deepcopy(self.v2_catalog)
        mutated["metrics"][0]["evidence_requirements"][0]["requirement"] += " changed"
        errors = validate_metrics_v2_consumer_binding(
            dict(CANONICAL_METRICS_V2_BINDING), mutated
        )
        self.assertTrue(errors)

    def test_v2_binding_rejects_unknown_or_missing_fields(self):
        extra = dict(CANONICAL_METRICS_V2_BINDING)
        extra["latest"] = True
        self.assertTrue(validate_metrics_v2_consumer_binding(extra, self.v2_catalog))

        missing = dict(CANONICAL_METRICS_V2_BINDING)
        missing.pop("metrics_catalog_sha256")
        self.assertTrue(validate_metrics_v2_consumer_binding(missing, self.v2_catalog))

    def test_binding_does_not_trust_caller_supplied_sha_over_catalog_content(self):
        caller_binding = dict(CANONICAL_METRICS_V2_BINDING)
        mutated = copy.deepcopy(self.v2_catalog)
        mutated["schema_version"] = "2.1"
        caller_binding["metrics_catalog_sha256"] = compute_canonical_sha256(mutated)
        self.assertTrue(validate_metrics_v2_consumer_binding(caller_binding, mutated))


if __name__ == "__main__":
    unittest.main()
