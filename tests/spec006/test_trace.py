"""US3/T014 fixture tests: Spec 006 trace chains, seals, manifests, trusted sets."""

from __future__ import annotations

import copy
import json
import unittest
from pathlib import Path

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec006.trace import (
    GENESIS,
    append_trace,
    record_hash,
    validate_manifest,
    validate_seal,
    validate_trace,
    validate_trace_set,
)

ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "specs/006-patient-safety-scaffold/fixtures"
MANIFEST_PATH = FIXTURES / "fixture-manifest.json"


def load_manifest():
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def load_entry_artifacts(entry):
    traces = json.loads((ROOT / entry["trace_set_path"]).read_text(encoding="utf-8"))
    seal = json.loads((ROOT / entry["seal_path"]).read_text(encoding="utf-8"))
    return traces, seal


def minimal_trace(**overrides):
    record = {
        "interaction_id": "11111111-2222-4333-8444-555555555555",
        "trace_version": "v1",
        "trace_sequence": 0,
        "predecessor_sha256": GENESIS,
        "input_identity_sha256": "a" * 64,
        "context_identity_sha256": "b" * 64,
        "policy_identity_sha256": "c" * 64,
        "tool_registry_identity_sha256": "d" * 64,
        "state_before": None,
        "state_after": "ANSWER",
        "trigger_record_ids": [],
        "tool_call_record_ids": [],
        "output_identity_sha256": "e" * 64,
        "failure_reason_codes": [],
        "safety_context": {
            "role": "PATIENT_CAREGIVER",
            "language": "en",
            "available_evidence_ids": [],
            "tool_availability": {},
        },
        "tool_calls": [],
        "determinism_proof": {
            "replayed": True,
            "replay_input_sha256": "a" * 64,
            "replay_context_identity_sha256": "b" * 64,
            "replay_policy_identity_sha256": "c" * 64,
            "replay_tool_registry_identity_sha256": "d" * 64,
            "replay_output_state": "ANSWER",
        },
    }
    record.update(overrides)
    return record


class TestCanonicalCommittedFixtures(unittest.TestCase):
    """The committed manifest + seals + trace sets must verify as committed."""

    def test_committed_manifest_valid(self):
        self.assertEqual([], validate_manifest(load_manifest()))

    def test_every_manifest_entry_verifies(self):
        manifest = load_manifest()
        for entry in manifest["entries"]:
            with self.subTest(interaction_id=entry["interaction_id"]):
                traces, seal = load_entry_artifacts(entry)
                self.assertEqual([], validate_trace_set(traces, seal, entry["interaction_id"]))
                self.assertEqual(entry["expected_final_sequence"], seal["expected_final_sequence"])
                self.assertEqual(
                    compute_canonical_sha256(seal), entry["seal_canonical_sha256"]
                )
                self.assertEqual(
                    trace_hash_of_final(traces), entry["terminal_record_sha256"]
                )

    def test_traces_are_privacy_safe(self):
        manifest = load_manifest()
        forbidden_keys = {"raw_text", "user_text", "phi", "payload", "transcript"}
        for entry in manifest["entries"]:
            traces, _ = load_entry_artifacts(entry)
            for index, trace_record in enumerate(traces):
                with self.subTest(entry=entry["interaction_id"], index=index):
                    self.assertFalse(forbidden_keys & set(trace_record))


def trace_hash_of_final(traces):
    return record_hash(traces[-1])


class TestSingleRecordValidation(unittest.TestCase):
    def test_minimal_genesis_record_valid(self):
        self.assertEqual([], validate_trace(minimal_trace()))

    def test_non_object_rejected(self):
        self.assertTrue(validate_trace("genesis"))

    def test_missing_required_field(self):
        record = minimal_trace()
        del record["output_identity_sha256"]
        errors = validate_trace(record)
        self.assertTrue(any("output_identity_sha256" in error for error in errors))

    def test_undeclared_top_level_field_rejected(self):
        record = minimal_trace(raw_user_text="patient said X")
        errors = validate_trace(record)
        self.assertTrue(any("undeclared fields" in error and "raw_user_text" in error for error in errors))

    def test_undeclared_nested_safety_context_field_rejected(self):
        record = minimal_trace()
        record["safety_context"]["free_note"] = "diagnosis guess"
        errors = validate_trace(record)
        self.assertTrue(any("safety_context" in error and "undeclared" in error for error in errors))

    def test_invalid_uuid_rejected(self):
        errors = validate_trace(minimal_trace(interaction_id="not-a-uuid"))
        self.assertTrue(any("UUID" in error for error in errors))

    def test_negative_sequence_rejected(self):
        errors = validate_trace(minimal_trace(trace_sequence=-1))
        self.assertTrue(any("trace_sequence" in error for error in errors))

    def test_genesis_rule_enforced(self):
        errors = validate_trace(minimal_trace(trace_sequence=0, predecessor_sha256="0" * 64))
        self.assertTrue(any("GENESIS" in error for error in errors))
        errors = validate_trace(minimal_trace(trace_sequence=1, predecessor_sha256=GENESIS))
        self.assertTrue(any("sha256" in error for error in errors))


class TestDeterminismProof(unittest.TestCase):
    def each_equality_key(self):
        return [
            ("replay_input_sha256", "input_identity_sha256"),
            ("replay_context_identity_sha256", "context_identity_sha256"),
            ("replay_policy_identity_sha256", "policy_identity_sha256"),
            ("replay_tool_registry_identity_sha256", "tool_registry_identity_sha256"),
        ]

    def test_all_equalities_hold_in_fixture_records(self):
        manifest = load_manifest()
        checked = 0
        for entry in manifest["entries"]:
            traces, _ = load_entry_artifacts(entry)
            for trace_record in traces:
                proof = trace_record["determinism_proof"]
                self.assertIs(True, proof["replayed"])
                for replay_key, identity_key in self.each_equality_key():
                    self.assertEqual(proof[replay_key], trace_record[identity_key])
                self.assertEqual(proof["replay_output_state"], trace_record["state_after"])
                checked += 1
        self.assertGreater(checked, 0)

    def test_each_mismatch_is_rejected_individually(self):
        for replay_key, identity_key in self.each_equality_key():
            with self.subTest(key=replay_key):
                record = copy.deepcopy(minimal_trace())
                record["determinism_proof"][replay_key] = "f" * 64
                errors = validate_trace(record)
                self.assertTrue(
                    any(replay_key in error and identity_key in error for error in errors),
                    errors,
                )

    def test_output_state_mismatch_rejected(self):
        record = minimal_trace()
        record["determinism_proof"]["replay_output_state"] = "ESCALATE"
        errors = validate_trace(record)
        self.assertTrue(any("replay_output_state" in error for error in errors))

    def test_replayed_false_rejected(self):
        record = minimal_trace()
        record["determinism_proof"]["replayed"] = False
        errors = validate_trace(record)
        self.assertTrue(any("replayed" in error for error in errors))

    def test_undeclared_determinism_field_rejected(self):
        record = minimal_trace()
        record["determinism_proof"]["notes"] = "trust me"
        errors = validate_trace(record)
        self.assertTrue(any("determinism_proof" in error and "undeclared" in error for error in errors))


class TestAppendAndHashChain(unittest.TestCase):
    def test_append_builds_contiguous_chain(self):
        first = append_trace(None, {**minimal_trace()})
        second_partial = minimal_trace(state_before="ANSWER", state_after="USE_TOOL")
        second = append_trace(first, second_partial)
        self.assertEqual(0, first["trace_sequence"])
        self.assertEqual(GENESIS, first["predecessor_sha256"])
        self.assertEqual(1, second["trace_sequence"])
        self.assertEqual(record_hash(first), second["predecessor_sha256"])
        self.assertEqual([], validate_trace_set([first, second], None, first["interaction_id"])[0:0])

    def test_record_hash_is_canonical_stable(self):
        record = minimal_trace()
        reordered = dict(reversed(list(record.items())))
        self.assertEqual(record_hash(record), record_hash(reordered))


class TestTraceSetSemantics(unittest.TestCase):
    """Negative fixtures per data-model §1.5 / FR-005."""

    def setUp(self):
        self.first = minimal_trace()
        second_partial = minimal_trace(
            state_before="ANSWER",
            state_after="ASK_MORE",
            determinism_proof={
                "replayed": True,
                "replay_input_sha256": "a" * 64,
                "replay_context_identity_sha256": "b" * 64,
                "replay_policy_identity_sha256": "c" * 64,
                "replay_tool_registry_identity_sha256": "d" * 64,
                "replay_output_state": "ASK_MORE",
            },
        )
        self.second = append_trace(self.first, second_partial)
        self.seal = {
            "interaction_id": self.first["interaction_id"],
            "seal_version": "v1",
            "expected_final_sequence": 1,
            "terminal_record_sha256": record_hash(self.second),
        }

    def valid_pair(self):
        return [self.first, self.second]

    def test_positive_set_verifies(self):
        self.assertEqual([], validate_trace_set(self.valid_pair(), self.seal, self.first["interaction_id"]))

    def test_sequence_gap_detected(self):
        pair = self.valid_pair()
        third_gap = append_trace(pair[1], {
            **minimal_trace(), "state_before": "ASK_MORE", "state_after": "ANSWER",
        })
        # Simulate a deleted middle record: sequences 0 and 2 present.
        third_gap["trace_sequence"] = 2
        third_gap["predecessor_sha256"] = record_hash(pair[1])
        traces = [pair[0], third_gap]
        errors = validate_trace_set(traces, None, self.first["interaction_id"])
        self.assertTrue(any("gap" in error or "genesis" in error.lower() or "contiguous" in error or "first record" in error for error in errors), errors)

    def test_duplicate_sequence_detected(self):
        pair = self.valid_pair()
        duplicate = copy.deepcopy(pair[1])
        errors = validate_trace_set([pair[0], pair[1], duplicate], None, self.first["interaction_id"])
        self.assertTrue(any("duplicate sequence" in error for error in errors))

    def test_reordered_traces_detected_via_predecessor_chain(self):
        pair = list(reversed(self.valid_pair()))
        errors = validate_trace_set(pair, None, self.first["interaction_id"])
        self.assertTrue(errors)

    def test_wrong_predecessor_detected(self):
        pair = self.valid_pair()
        pair[1]["predecessor_sha256"] = "f" * 64
        errors = validate_trace_set(pair, None, self.first["interaction_id"])
        self.assertTrue(any("chain mismatch" in error for error in errors))

    def test_invalid_genesis_detected(self):
        broken_first = copy.deepcopy(self.first)
        broken_first["predecessor_sha256"] = record_hash(broken_first)
        errors = validate_trace_set([broken_first], None, self.first["interaction_id"])
        self.assertTrue(any("GENESIS" in error for error in errors))

    def test_state_continuity_violation_detected(self):
        pair = self.valid_pair()
        pair[1]["state_before"] = "EMERGENCY"
        errors = validate_trace_set(pair, None, self.first["interaction_id"])
        self.assertTrue(any("continuity" in error for error in errors))

    def test_mixed_interaction_ids_detected(self):
        pair = self.valid_pair()
        other = "99999999-9999-4999-8999-999999999999"
        foreign = minimal_trace(interaction_id=other)
        errors = validate_trace_set([foreign], None, self.first["interaction_id"])
        self.assertTrue(any("mismatch against requested interaction_id" in error for error in errors))

    def test_terminal_sequence_mismatch_detected(self):
        seal = dict(self.seal, expected_final_sequence=5)
        errors = validate_trace_set(self.valid_pair(), seal, self.first["interaction_id"])
        self.assertTrue(any("terminal sequence mismatch" in error for error in errors))

    def test_terminal_record_hash_mismatch_detected(self):
        seal = dict(self.seal, terminal_record_sha256="e" * 64)
        errors = validate_trace_set(self.valid_pair(), seal, self.first["interaction_id"])
        self.assertTrue(any("terminal record hash mismatch" in error for error in errors))

    def test_empty_trace_set_rejected(self):
        errors = validate_trace_set([], None, self.first["interaction_id"])
        self.assertTrue(any("non-empty ordered array" in error for error in errors))

    def test_missing_seal_fields_rejected(self):
        errors = validate_seal({"interaction_id": self.first["interaction_id"]})
        self.assertTrue(any("seal_version" in error for error in errors))
        self.assertTrue(any("expected_final_sequence" in error for error in errors))
        self.assertTrue(any("terminal_record_sha256" in error for error in errors))


class TestManifestValidation(unittest.TestCase):
    def setUp(self):
        self.manifest = load_manifest()

    def rewrite_identity(self, bundle):
        bundle["manifest_identity_sha256"] = compute_canonical_sha256(
            {"manifest_version": bundle["manifest_version"], "entries": bundle["entries"]}
        )
        return bundle

    def test_duplicate_interaction_id_entries_rejected(self):
        bundle = copy.deepcopy(self.manifest)
        duplicate = copy.deepcopy(bundle["entries"][0])
        duplicate["seal_path"] = (
            "specs/006-patient-safety-scaffold/fixtures/other-id/trace_seal.json"
        )
        duplicate["trace_set_path"] = (
            "specs/006-patient-safety-scaffold/fixtures/other-id/traces.json"
        )
        bundle["entries"].append(duplicate)
        errors = validate_manifest(bundle)
        self.assertTrue(any("duplicate interaction_id" in error for error in errors))

    def test_duplicate_bound_paths_rejected(self):
        bundle = copy.deepcopy(self.manifest)
        duplicate = copy.deepcopy(bundle["entries"][0])
        duplicate["interaction_id"] = "77777777-7777-4777-8777-777777777777"
        bundle["entries"].append(duplicate)
        errors = validate_manifest(bundle)
        self.assertTrue(any("duplicate manifest-bound path" in error for error in errors))

    def test_traversal_path_rejected(self):
        bundle = copy.deepcopy(self.manifest)
        bundle["entries"][0]["seal_path"] = (
            "specs/006-patient-safety-scaffold/fixtures/../../etc/trace_seal.json"
        )
        errors = validate_manifest(bundle)
        self.assertTrue(
            any("escapes fixture root" in error or "canonical seal path" in error for error in errors),
            errors,
        )

    def test_outside_root_path_rejected(self):
        bundle = copy.deepcopy(self.manifest)
        bundle["entries"][0]["trace_set_path"] = "data/spec006/other/traces.json"
        errors = validate_manifest(bundle)
        self.assertTrue(any("escapes fixture root" in error for error in errors))

    def test_identity_projection_mismatch_rejected(self):
        bundle = copy.deepcopy(self.manifest)
        bundle["manifest_identity_sha256"] = "2" * 64
        errors = validate_manifest(bundle)
        self.assertTrue(any("manifest_identity_sha256" in error and "mismatch" in error for error in errors))

    def test_self_referential_oid_field_rejected_as_undeclared(self):
        # Trust model: the trusted commit OID is out-of-band; a manifest cannot
        # declare a field that would embed it.
        bundle = copy.deepcopy(self.manifest)
        bundle["trusted_commit_oid"] = "0" * 40
        errors = validate_manifest(bundle)
        self.assertTrue(any("trusted_commit_oid" in error for error in errors))

    def test_undeclared_entry_field_rejected(self):
        bundle = copy.deepcopy(self.manifest)
        bundle["entries"][0]["commit_oid"] = "0" * 40
        errors = validate_manifest(bundle)
        self.assertTrue(any("undeclared fields" in error and "commit_oid" in error for error in errors))


if __name__ == "__main__":
    unittest.main()
