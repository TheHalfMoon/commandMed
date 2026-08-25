"""US1/T012 fixture tests: Spec 006 deterministic tool registry contract."""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from src.commandmed.eval_contract.canonical import (
    canonical_json_dumps,
    compute_canonical_sha256,
)
from src.commandmed.spec006.registry import (
    find_tool,
    validate_registry,
    validate_tool_record,
)

ROOT = Path(__file__).resolve().parents[2]
REGISTRY_PATH = ROOT / "data/spec006/tool_registry.json"


def load_registry():
    return json.loads(REGISTRY_PATH.read_text(encoding="utf-8"))


class TestToolRecordContract(unittest.TestCase):
    def setUp(self):
        self.registry = load_registry()
        self.sample = self.registry["tools"][0]

    def test_canonical_bundle_is_valid(self):
        self.assertEqual([], validate_registry(self.registry))

    def test_all_records_reject_network_and_authorize_nothing(self):
        for index, tool in enumerate(self.registry["tools"]):
            with self.subTest(index=index, tool_id=tool["tool_id"]):
                self.assertIs(False, tool["network_required"])
                self.assertEqual("NONE", tool["execution_authority"])

    def test_required_field_missing_rejected(self):
        record = copy.deepcopy(self.sample)
        del record["source_authority"]
        errors = validate_tool_record(record)
        self.assertTrue(any("source_authority" in error for error in errors))

    def test_undeclared_top_level_field_rejected(self):
        record = copy.deepcopy(self.sample)
        record["vendor_plugin"] = True
        errors = validate_tool_record(record)
        self.assertTrue(any("undeclared" in error and "vendor_plugin" in error for error in errors))

    def test_undeclared_nested_failure_semantics_field_rejected(self):
        record = copy.deepcopy(self.sample)
        record["failure_semantics"]["fallback_answer"] = "try anyway"
        errors = validate_tool_record(record)
        self.assertTrue(any("failure_semantics" in error and "undeclared" in error for error in errors))

    def test_network_required_must_be_false_const(self):
        record = copy.deepcopy(self.sample)
        record["network_required"] = True
        errors = validate_tool_record(record)
        self.assertTrue(any("network_required" in error for error in errors))

    def test_execution_authority_must_be_none(self):
        record = copy.deepcopy(self.sample)
        record["execution_authority"] = "AUTHORIZED_TO_START"
        errors = validate_tool_record(record)
        self.assertTrue(any("execution_authority" in error for error in errors))
        # Even the planning-authorized token must stay rejected at the
        # registry layer: authority escalation happens only via governance.
        record["execution_authority"] = "AUTHORIZED_TO_SPECIFY"
        self.assertTrue(validate_tool_record(record))

    def test_tool_content_identity_sha256_pattern(self):
        record = copy.deepcopy(self.sample)
        record["tool_content_identity"] = "XYZ"
        self.assertTrue(validate_tool_record(record))
        record["tool_content_identity"] = "A" * 64  # uppercase rejected
        self.assertTrue(validate_tool_record(record))

    def test_clinical_classes_require_provenance(self):
        record = copy.deepcopy(self.sample)
        record["result_provenance_required"] = False
        errors = validate_tool_record(record)
        if record["tool_class"] == "unit_conversion":
            return  # unit conversion is not clinical; provenance optional here
        self.assertTrue(any("result_provenance_required" in error for error in errors))

    def test_non_object_record_rejected(self):
        self.assertTrue(validate_tool_record(["not", "a", "dict"]))


class TestRegistryBundle(unittest.TestCase):
    def setUp(self):
        self.registry = load_registry()

    def test_duplicate_tool_id_rejected(self):
        bundle = copy.deepcopy(self.registry)
        duplicate = copy.deepcopy(bundle["tools"][0])
        bundle["tools"].append(duplicate)
        errors = validate_registry(bundle)
        self.assertTrue(any("duplicate tool_id" in error for error in errors))

    def test_registry_sha256_projection_mismatch_rejected(self):
        bundle = copy.deepcopy(self.registry)
        bundle["registry_sha256"] = "0" * 64
        errors = validate_registry(bundle)
        self.assertTrue(any("registry_sha256" in error and "mismatch" in error for error in errors))

    def test_registry_sha256_including_itself_would_mismatch(self):
        # Negative proof that the identity is the projection omitting the hash.
        bundle = copy.deepcopy(self.registry)
        projection_with_hash = {
            "registry_version": bundle["registry_version"],
            "tools": bundle["tools"],
            "registry_sha256": bundle["registry_sha256"],
        }
        wrong = compute_canonical_sha256(projection_with_hash)
        self.assertNotEqual(wrong, bundle["registry_sha256"])

    def test_empty_tools_array_rejected(self):
        bundle = copy.deepcopy(self.registry)
        bundle["tools"] = []
        errors = validate_registry(bundle)
        self.assertTrue(any("non-empty array" in error for error in errors))

    def test_undeclared_bundle_field_rejected(self):
        bundle = copy.deepcopy(self.registry)
        bundle["plugin_loader"] = {"enabled": True}
        errors = validate_registry(bundle)
        self.assertTrue(any("undeclared fields" in error and "plugin_loader" in error for error in errors))

    def test_canonical_hash_stability_across_key_ordering(self):
        reordered = {
            "tools": [dict(reversed(list(tool.items()))) for tool in self.registry["tools"]],
            "registry_sha256": self.registry["registry_sha256"],
            "registry_version": self.registry["registry_version"],
        }
        self.assertEqual(
            canonical_json_dumps(self.registry), canonical_json_dumps(reordered)
        )
        self.assertEqual([], validate_registry(reordered))

    def test_closed_allow_list_classes_only(self):
        allowed = {
            "unit_conversion",
            "pure_arithmetic",
            "validated_clinical_score",
            "interaction_lookup",
            "schema_validation",
            "evidence_retrieval",
        }
        for tool in self.registry["tools"]:
            with self.subTest(tool_id=tool["tool_id"]):
                self.assertIn(tool["tool_class"], allowed)

    def test_find_tool_lookup(self):
        first = self.registry["tools"][0]
        self.assertIs(first, find_tool(self.registry, first["tool_id"]))
        self.assertIsNone(find_tool(self.registry, "does_not_exist@v1"))
        self.assertIsNone(find_tool(None, "anything"))


if __name__ == "__main__":
    unittest.main()
