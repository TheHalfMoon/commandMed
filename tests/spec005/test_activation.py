"""US7 fixture tests: A15 activation record validation. Synthetic only."""

from __future__ import annotations

import unittest

from src.commandmed.spec005.activation import (
    evaluate_activation_readiness,
    validate_activation_record,
)


def make_snapshot(**overrides):
    snapshot = {
        "snapshot_id": "SNAP-ACT-1",
        "snapshot_version": "1.0",
        "snapshot_sha256": "e" * 64,
        "computed_readiness": "READY_FOR_SEPARATE_ACTIVATION_NOT_AUTHORIZED",
        "requirements": {
            gate: {
                "state": "PASS",
                "record_id": f"REC-{gate}",
                "record_canonical_sha256": "a" * 64,
                "stale": False,
            }
            for gate in (
                "R1", "T1", "D34", "G1", "G2", "G3", "G4",
                "S1", "P1", "C1", "H1", "I1", "F1",
            )
        },
    }
    snapshot.update(overrides)
    return snapshot


def make_activation(**overrides):
    activation = {
        "activation_id": "ACT-SYNTHETIC-001",
        "activation_version": "1.0",
        "preconstruction_snapshot_id": "SNAP-ACT-1",
        "preconstruction_snapshot_sha256": "e" * 64,
        "required_gate_identities": {
            gate: {
                "record_id": f"REC-{gate}",
                "record_canonical_sha256": "a" * 64,
            }
            for gate in (
                "R1", "T1", "D34", "G1", "G2", "G3", "G4",
                "S1", "P1", "C1", "H1", "I1", "F1",
            )
        },
        "authorization_decision_id": "FOUNDER-DECISION-PENDING",
        "authorized_construction_scope": ["SELECTION_SUITE_CONSTRUCTION_ONLY"],
        "explicit_exclusions": [
            "MODEL_EXECUTION",
            "BENCHMARK_PAYLOAD_ACCESS",
            "PRIVATE_GOLD_ACCESS",
            "DEVICE_EXECUTION",
            "PROVIDER_GENERATION",
        ],
        "activation_state": "DRAFT_UNAUTHORIZED",
        "record_canonical_sha256": "c" * 64,
    }
    activation.update(overrides)
    return record if False else {**activation, **overrides} if False else activation


class ActivationRecordTests(unittest.TestCase):
    def test_valid_synthetic_record_validates(self):
        errors = validate_activation_record(make_activation(), make_snapshot())
        self.assertEqual(errors, [])

    def test_snapshot_binding_required(self):
        activation = make_activation()
        del activation["preconstruction_snapshot_id"]
        errors = validate_activation_record(activation, make_snapshot())
        self.assertTrue(any("preconstruction_snapshot_id" in e for e in errors))

    def test_snapshot_sha_mismatch_rejected(self):
        snapshot = make_snapshot(snapshot_sha256="d" * 64)
        self.assertIn(
            "Activation:PRECONSTRUCTION_SNAPSHOT_SHA_MISMATCH",
            validate_activation_record(make_activation(), snapshot),
        )

    def test_missing_snapshot_sha_rejected(self):
        snapshot = make_snapshot()
        del snapshot["snapshot_sha256"]
        errors = validate_activation_record(make_activation(), snapshot)
        self.assertTrue(any("SNAPSHOT_SHA256_REQUIRED" in e for e in errors))

    def test_unbound_gate_evidence_rejected(self):
        snapshot = make_snapshot()
        snapshot["requirements"]["G1"] = {"state": "PASS", "stale": False}
        errors = validate_activation_record(make_activation(), snapshot)
        self.assertTrue(any("G1_RECORD_ID_UNBOUND" in e for e in errors))

    def test_snapshot_sha_mismatch_still_detected(self):
        snapshot = make_snapshot(snapshot_sha256="d" * 64)
        errors = validate_activation_record(make_activation(), snapshot)
        self.assertTrue(any("SHA_MISMATCH" in e.upper() for e in errors))

    def _unused_legacy(self):
        snapshot = make_snapshot(snapshot_sha256="d" * 64)
        errors = validate_activation_record(make_activation(), snapshot)
        self.assertTrue(any("SHA" in e.upper() for e in errors))

    def test_activation_must_bind_gate_record_sha(self):
        activation = make_activation()
        activation["required_gate_identities"] = {
            gate: {"record_id": f"REC-{gate}"} for gate in (
                "R1", "T1", "D34", "G1", "G2", "G3", "G4",
                "S1", "P1", "C1", "H1", "I1", "F1",
            )
        }
        errors = validate_activation_record(activation, make_snapshot())
        self.assertTrue(any("SHA_MISMATCH" in e for e in errors))
        # Full binding remains valid.
        activation["required_gate_identities"] = {
            gate: {
                "record_id": f"REC-{gate}",
                "record_canonical_sha256": "a" * 64,
            }
            for gate in (
                "R1", "T1", "D34", "G1", "G2", "G3", "G4",
                "S1", "P1", "C1", "H1", "I1", "F1",
            )
        }
        self.assertEqual(validate_activation_record(activation, make_snapshot()), [])

    def test_wrong_bound_gate_sha_rejected(self):
        activation = make_activation()
        activation["required_gate_identities"] = {
            gate: {
                "record_id": f"REC-{gate}",
                "record_canonical_sha256": (
                    "a" * 64 if gate != "T1" else "f" * 64
                ),
            }
            for gate in (
                "R1", "T1", "D34", "G1", "G2", "G3", "G4",
                "S1", "P1", "C1", "H1", "I1", "F1",
            )
        }
        errors = validate_activation_record(activation, make_snapshot())
        self.assertTrue(any("T1" in e and "SHA" in e.upper() for e in errors))

    def test_gate_identity_mismatch_rejected(self):
        activation = make_activation()
        activation["required_gate_identities"]["T1"] = "REC-WRONG"
        errors = validate_activation_record(activation, make_snapshot())
        self.assertTrue(any("T1" in e for e in errors))

    def test_malformed_does_not_raise(self):
        for bad in (None, [], 4):
            errors = validate_activation_record(bad, make_snapshot())
            self.assertIsInstance(errors, list)
            self.assertTrue(errors)


class ActivationReadinessTests(unittest.TestCase):
    def test_complete_pass_snapshot_yields_ready_not_activated(self):
        result = evaluate_activation_readiness(
            make_activation(), make_snapshot()
        )
        self.assertEqual(result["state"], "READY_FOR_SEPARATE_AUTHORIZATION")
        # Synthetic readiness never creates real construction authority.
        self.assertNotIn("authorized", result)
        self.assertNotEqual(result["state"], "AUTHORIZED_TO_CONSTRUCT")

    def test_blocked_prerequisite_blocks_activation(self):
        snapshot = make_snapshot()
        snapshot["requirements"]["F1"] = {
            "state": "BLOCKED",
            "record_id": "REC-F1",
            "record_canonical_sha256": "a" * 64,
            "stale": False,
        }
        result = evaluate_activation_readiness(make_activation(), snapshot)
        self.assertEqual(result["state"], "BLOCKED")

    def test_stale_prerequisite_blocks(self):
        snapshot = make_snapshot()
        snapshot["requirements"]["G1"]["stale"] = True
        result = evaluate_activation_readiness(make_activation(), snapshot)
        self.assertEqual(result["state"], "BLOCKED")

    def test_missing_scientific_records_block(self):
        snapshot = make_snapshot()
        for gate in ("T1", "D34"):
            del snapshot["requirements"][gate]
        result = evaluate_activation_readiness(make_activation(), snapshot)
        self.assertEqual(result["state"], "BLOCKED")

    def test_snapshot_computed_state_enforced(self):
        snapshot = make_snapshot(computed_readiness="NOT_READY_TO_CONSTRUCT")
        result = evaluate_activation_readiness(make_activation(), snapshot)
        self.assertEqual(result["state"], "BLOCKED")

        snapshot = make_snapshot(computed_readiness="SOMEONE_ELSES_STATE")
        result = evaluate_activation_readiness(make_activation(), snapshot)
        self.assertEqual(result["state"], "BLOCKED")

    def test_caller_authorized_claim_not_trusted(self):
        activation = make_activation(activation_state="AUTHORIZED_TO_CONSTRUCT")
        result = evaluate_activation_readiness(activation, make_snapshot())
        self.assertNotEqual(result["state"], "AUTHORIZED_TO_CONSTRUCT")

    def test_malformed_fail_closed(self):
        result = evaluate_activation_readiness(None, None)
        self.assertEqual(result["state"], "BLOCKED")
        self.assertEqual(result["reason_codes"], sorted(set(result["reason_codes"])))


if __name__ == "__main__":
    unittest.main()
