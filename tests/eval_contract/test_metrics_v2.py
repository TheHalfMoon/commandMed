from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from src.commandmed.eval_contract.canonical import (
    canonical_json_dumps,
    compute_canonical_sha256,
    compute_file_canonical_sha256,
)
from src.commandmed.eval_contract.validate import (
    validate_metrics_catalog,
    validate_metrics_catalog_v2,
)

ROOT = Path(__file__).resolve().parents[2]
V1_PATH = ROOT / "data/eval/metrics.json"
V2_PATH = ROOT / "data/eval/metrics-v2.json"
V1_SHA256 = "304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a"

V2_SCHEMA_ID = "commandmed-metrics-catalog"
V2_SCHEMA_VERSION = "2.0"
V2_REQUIRED_METRIC_FIELDS = {
    "metric_id",
    "name",
    "category",
    "description",
    "direction",
    "unit",
    "is_hard_gate",
    "threshold_state",
    "applicable_roles",
    "applicable_modalities",
    "applicable_languages",
    "evidence_requirements",
}
V1_NON_EVIDENCE_FIELDS = V2_REQUIRED_METRIC_FIELDS - {"evidence_requirements"}
REQUIRED_ROLE_FIELDS = {
    "evidence_role",
    "purpose",
    "evidence_kind",
    "binding_mode",
    "source_policy",
    "requirement",
}


def load_json(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def metric_by_id(catalog: dict, metric_id: str) -> dict:
    return next(item for item in catalog["metrics"] if item["metric_id"] == metric_id)


class MetricsV2CatalogTests(unittest.TestCase):
    def setUp(self):
        self.v1 = load_json(V1_PATH)
        self.v2 = load_json(V2_PATH)

    def test_v1_identity_and_validator_remain_exactly_unchanged(self):
        self.assertEqual(compute_file_canonical_sha256(V1_PATH), V1_SHA256)
        self.assertEqual(validate_metrics_catalog(self.v1), (True, []))

    def test_v2_envelope_is_exact_and_valid(self):
        self.assertEqual(
            set(self.v2),
            {"schema_id", "schema_version", "supersedes_metrics_v1_sha256", "metrics"},
        )
        self.assertEqual(self.v2["schema_id"], V2_SCHEMA_ID)
        self.assertEqual(self.v2["schema_version"], V2_SCHEMA_VERSION)
        self.assertEqual(self.v2["supersedes_metrics_v1_sha256"], V1_SHA256)
        self.assertTrue(self.v2["metrics"])
        self.assertEqual(validate_metrics_catalog_v2(self.v2), (True, []))

    def test_v2_preserves_v1_metric_identity_and_non_evidence_semantics(self):
        self.assertEqual(
            {item["metric_id"] for item in self.v2["metrics"]},
            {item["metric_id"] for item in self.v1},
        )
        v1_by_id = {item["metric_id"]: item for item in self.v1}
        for v2_metric in self.v2["metrics"]:
            with self.subTest(metric_id=v2_metric["metric_id"]):
                self.assertEqual(set(v2_metric), V2_REQUIRED_METRIC_FIELDS)
                self.assertNotIn("required_evidence", v2_metric)
                v1_metric = v1_by_id[v2_metric["metric_id"]]
                for field in V1_NON_EVIDENCE_FIELDS:
                    self.assertEqual(v2_metric[field], v1_metric[field], field)
                self.assertTrue(v2_metric["evidence_requirements"])

    def test_non_arabic_metrics_do_not_gain_selection_or_gold_authority(self):
        prohibited_auto_roles = {
            "SELECTION_DEV",
            "PRIVATE_GOLD_FINAL_AUDIT",
            "PUBLIC_EXTERNAL_EVAL",
        }
        for metric in self.v2["metrics"]:
            if metric["metric_id"] == "arabic_clinical_parity_gap":
                continue
            roles = {entry["evidence_role"] for entry in metric["evidence_requirements"]}
            with self.subTest(metric_id=metric["metric_id"]):
                self.assertTrue(roles.isdisjoint(prohibited_auto_roles))

    def test_arabic_parity_has_exact_dual_lifecycle_roles(self):
        metric = metric_by_id(self.v2, "arabic_clinical_parity_gap")
        self.assertEqual(
            {entry["evidence_role"] for entry in metric["evidence_requirements"]},
            {"SELECTION_DEV", "PRIVATE_GOLD_FINAL_AUDIT"},
        )
        self.assertEqual(len(metric["evidence_requirements"]), 2)
        by_role = {entry["evidence_role"]: entry for entry in metric["evidence_requirements"]}
        selection = by_role["SELECTION_DEV"]
        final_audit = by_role["PRIVATE_GOLD_FINAL_AUDIT"]
        self.assertEqual(selection["purpose"], "CHECKPOINT_SELECTION")
        self.assertEqual(selection["binding_mode"], "MANIFEST_BOUND")
        self.assertEqual(selection["source_policy"], "SELECTION_SAFE_NON_GOLD")
        self.assertEqual(final_audit["purpose"], "PRIVATE_GOLD")
        self.assertEqual(final_audit["binding_mode"], "CANONICAL_FAMILY_BOUND")
        self.assertEqual(final_audit["source_policy"], "PRIVATE_GOLD_FAMILY")

    def test_evidence_requirement_records_have_exact_required_shape(self):
        for metric in self.v2["metrics"]:
            for requirement in metric["evidence_requirements"]:
                with self.subTest(metric_id=metric["metric_id"], role=requirement.get("evidence_role")):
                    self.assertEqual(set(requirement), REQUIRED_ROLE_FIELDS)
                    self.assertIsInstance(requirement["evidence_kind"], str)
                    self.assertTrue(requirement["evidence_kind"].strip())
                    self.assertIsInstance(requirement["requirement"], str)
                    self.assertTrue(requirement["requirement"].strip())

    def test_unknown_role_purpose_binding_and_source_policy_fail_closed(self):
        mutations = {
            "evidence_role": "LATEST_ROLE",
            "purpose": "LATEST_PURPOSE",
            "binding_mode": "LATEST_BINDING",
            "source_policy": "LATEST_SOURCE_POLICY",
        }
        for field, value in mutations.items():
            with self.subTest(field=field):
                bad = copy.deepcopy(self.v2)
                bad["metrics"][0]["evidence_requirements"][0][field] = value
                valid, errors = validate_metrics_catalog_v2(bad)
                self.assertFalse(valid)
                self.assertTrue(errors)

    def test_role_purpose_and_source_policy_mismatches_fail_closed(self):
        metric = metric_by_id(self.v2, "arabic_clinical_parity_gap")
        metric_index = self.v2["metrics"].index(metric)
        cases = (
            ("SELECTION_DEV", "purpose", "PRIVATE_GOLD"),
            ("SELECTION_DEV", "source_policy", "PRIVATE_GOLD_FAMILY"),
            ("PRIVATE_GOLD_FINAL_AUDIT", "purpose", "CHECKPOINT_SELECTION"),
            ("PRIVATE_GOLD_FINAL_AUDIT", "source_policy", "SELECTION_SAFE_NON_GOLD"),
        )
        for role, field, value in cases:
            with self.subTest(role=role, field=field):
                bad = copy.deepcopy(self.v2)
                requirements = bad["metrics"][metric_index]["evidence_requirements"]
                target = next(item for item in requirements if item["evidence_role"] == role)
                target[field] = value
                valid, errors = validate_metrics_catalog_v2(bad)
                self.assertFalse(valid)
                self.assertTrue(errors)

    def test_duplicate_or_missing_arabic_required_role_fails_closed(self):
        metric = metric_by_id(self.v2, "arabic_clinical_parity_gap")
        metric_index = self.v2["metrics"].index(metric)

        duplicate = copy.deepcopy(self.v2)
        duplicate_req = copy.deepcopy(duplicate["metrics"][metric_index]["evidence_requirements"][0])
        duplicate["metrics"][metric_index]["evidence_requirements"].append(duplicate_req)
        self.assertFalse(validate_metrics_catalog_v2(duplicate)[0])

        missing = copy.deepcopy(self.v2)
        missing["metrics"][metric_index]["evidence_requirements"] = [
            item
            for item in missing["metrics"][metric_index]["evidence_requirements"]
            if item["evidence_role"] != "SELECTION_DEV"
        ]
        self.assertFalse(validate_metrics_catalog_v2(missing)[0])

    def test_v2_evidence_role_order_is_semantically_nonsemantic(self):
        reordered = copy.deepcopy(self.v2)
        metric = metric_by_id(reordered, "arabic_clinical_parity_gap")
        metric["evidence_requirements"].reverse()
        self.assertEqual(
            compute_canonical_sha256(self.v2),
            compute_canonical_sha256(reordered),
        )

    def test_v2_role_semantic_mutation_changes_identity(self):
        mutated = copy.deepcopy(self.v2)
        metric = metric_by_id(mutated, "arabic_clinical_parity_gap")
        metric["evidence_requirements"][0]["requirement"] += " changed"
        self.assertNotEqual(
            compute_canonical_sha256(self.v2),
            compute_canonical_sha256(mutated),
        )

    def test_shared_purpose_records_tie_break_deterministically_by_role(self):
        """Records sharing a primary sort key stay order-independent via the
        evidence_role composite tie-break, even though duplicate roles are
        rejected by the validator for real catalogs."""
        shared_purpose = [
            {
                "evidence_role": "ZZ_ROLE",
                "purpose": "SHARED_PURPOSE",
                "evidence_kind": "synthetic",
                "binding_mode": "MANIFEST_BOUND",
                "source_policy": "IDENTITY_BOUND_QUALIFICATION_ASSET",
                "requirement": "same",
            },
            {
                "evidence_role": "AA_ROLE",
                "purpose": "SHARED_PURPOSE",
                "evidence_kind": "synthetic",
                "binding_mode": "MANIFEST_BOUND",
                "source_policy": "IDENTITY_BOUND_QUALIFICATION_ASSET",
                "requirement": "same",
            },
        ]
        self.assertEqual(
            compute_canonical_sha256(shared_purpose),
            compute_canonical_sha256(list(reversed(shared_purpose))),
        )

    def _role_record(self, role: str, purpose: str) -> dict:
        return {
            "evidence_role": role,
            "purpose": purpose,
            "evidence_kind": "synthetic",
            "binding_mode": "MANIFEST_BOUND",
            "source_policy": "IDENTITY_BOUND_QUALIFICATION_ASSET",
            "requirement": f"req-{role}",
        }

    def test_evidence_requirements_are_canonically_ordered_by_role(self):
        """Frozen contract CANONICAL_RECORD_SORT_KEY_ADD=evidence_role:
        inside an evidence_requirements collection, differing purpose values
        must not override evidence_role as the primary canonical identity."""
        presented = [
            self._role_record("ZZ_ROLE", "AAA_PURPOSE"),
            self._role_record("AA_ROLE", "ZZZ_PURPOSE"),
        ]
        container = {"evidence_requirements": presented}
        reversed_container = {
            "evidence_requirements": list(reversed(presented)),
        }

        normalized = json.loads(canonical_json_dumps(container))
        roles_in_canonical_order = [
            record["evidence_role"]
            for record in normalized["evidence_requirements"]
        ]
        self.assertEqual(roles_in_canonical_order, ["AA_ROLE", "ZZ_ROLE"])

        self.assertEqual(
            compute_canonical_sha256(container),
            compute_canonical_sha256(reversed_container),
        )


if __name__ == "__main__":
    unittest.main()
