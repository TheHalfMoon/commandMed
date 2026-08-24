"""US4 fixture tests: opaque personnel governance (A7). Synthetic only."""

from __future__ import annotations

import unittest

from src.commandmed.spec005.personnel import (
    evaluate_a7_handshake,
    evaluate_role_eligibility,
    validate_eligibility_record,
    validate_independence,
    validate_personnel_record,
    validate_role_assignment,
)


def make_identity(**overrides):
    record = {
        "personnel_reference": "P-0001",
        "identity_state": "VERIFIED",
        "record_version": "1.0",
        "protected_evidence_reference": "VAULT-REF-1",
        "record_canonical_sha256": "a" * 64,
    }
    record.update(overrides)
    return record


def make_evidence(**overrides):
    evidence = {
        "qualification_evidence_ids": ["QUAL-1"],
        "conflict_disposition_record_id": "CONF-1",
        "gold_exposure_disposition_record_id": "GOLD-1",
        "result_exposure_state": "RESULT_BLIND",
        "evidence_stale": False,
    }
    evidence.update(overrides)
    return evidence


def make_eligibility(**overrides):
    record = {
        "eligibility_record_id": "EL-001",
        "personnel_reference": "P-0001",
        "role_class": "CONTENT_AUTHOR_ARABIC_PAIRS",
        "suite_or_scope_id": "SUITE-SELECTION-DEV-1",
        "identity_record_id": "ID-001",
        "qualification_evidence_ids": ["QUAL-1"],
        "conflict_disposition_record_id": "CONF-1",
        "gold_exposure_disposition_record_id": "GOLD-1",
        "result_exposure_state": "RESULT_BLIND",
        "eligibility_state": "NOT_COMPUTED",
        "reason_codes": [],
        "record_canonical_sha256": "b" * 64,
    }
    record.update(overrides)
    return record


def make_assignment(**overrides):
    assignment = {
        "assignment_id": "ASG-001",
        "personnel_reference": "P-0001",
        "role_class": "CONTENT_AUTHOR_ARABIC_PAIRS",
        "suite_or_scope_id": "SUITE-SELECTION-DEV-1",
        "eligibility_record_id": "EL-001",
        "assignment_state": "PROPOSED",
        "record_canonical_sha256": "c" * 64,
    }
    assignment.update(overrides)
    return assignment
    return record


class IdentityTests(unittest.TestCase):
    def test_valid_identity_validates(self):
        self.assertEqual(validate_personnel_record(make_identity()), [])

    def test_opaque_reference_only(self):
        errors = validate_personnel_record(
            make_identity(personnel_reference="Jane Doe <jane@example.com>")
        )
        self.assertTrue(any("OPAQUE" in e.upper() for e in errors))

    def test_unknown_identity_state_fails_closed(self):
        errors = validate_personnel_record(make_identity(identity_state="MAYBE"))
        self.assertTrue(any("MAYBE" in e for e in errors))

    def test_malformed_does_not_raise(self):
        for bad in (None, 5, []):
            self.assertTrue(validate_personnel_record(bad))


class EligibilityTests(unittest.TestCase):
    def test_valid_eligibility_computes(self):
        result = evaluate_role_eligibility(make_eligibility(), make_evidence())
        self.assertEqual(result["state"], "ELIGIBLE")
        self.assertEqual(result["reason_codes"], [])

    def test_gold_exposure_blocks_content_roles(self):
        evidence = make_evidence(gold_exposure_state="EXPOSED_TO_PRIVATE_GOLD")
        result = evaluate_role_eligibility(make_eligibility(), evidence)
        self.assertEqual(result["state"], "INELIGIBLE")
        self.assertTrue(any("PRIVATE_GOLD" in c.upper() for c in result["reason_codes"]))

    def test_stale_evidence_blocks(self):
        result = evaluate_role_eligibility(
            make_eligibility(), make_evidence(evidence_stale=True)
        )
        self.assertEqual(result["state"], "BLOCKED_PENDING_EVIDENCE")

    def test_missing_qualification_blocks(self):
        result = evaluate_role_eligibility(
            make_eligibility(), make_evidence(qualification_evidence_ids=[])
        )
        self.assertEqual(result["state"], "BLOCKED_PENDING_EVIDENCE")

    def test_validate_eligibility_shape(self):
        errors = validate_eligibility_record(make_eligibility(), make_evidence())
        self.assertEqual(errors, [])
        broken = make_eligibility()
        del broken["suite_or_scope_id"]
        errors = validate_eligibility_record(broken, make_evidence())
        self.assertTrue(any("suite_or_scope_id" in e for e in errors))

    def test_result_exposed_cannot_be_result_blind(self):
        result = evaluate_role_eligibility(
            make_eligibility(),
            make_evidence(result_exposure_state="SAME_SUITE_RESULTS_EXPOSED"),
        )
        self.assertIn("PERSONNEL:SAME_SUITE_RESULT_EXPOSURE_INCOMPATIBLE", result["reason_codes"])

    def test_malformed_does_not_raise(self):
        for bad in (None, 3):
            result = evaluate_role_eligibility(bad, None)
            self.assertIn(result["state"], {"BLOCKED_PENDING_EVIDENCE", "INELIGIBLE"})


class AssignmentTests(unittest.TestCase):
    def _eligible(self):
        return {
            "state": "ELIGIBLE",
            "reason_codes": [],
            "personnel_reference": "P-0001",
            "role_class": "CONTENT_AUTHOR_ARABIC_PAIRS",
            "suite_or_scope_id": "SUITE-SELECTION-DEV-1",
        }

    def test_valid_assignment_validates(self):
        self.assertEqual(
            validate_role_assignment(make_assignment(), self._eligible()), []
        )

    def test_active_assignment_requires_eligible(self):
        errors = validate_role_assignment(
            make_assignment(assignment_state="ACTIVE"),
            {"state": "BLOCKED_PENDING_EVIDENCE", "reason_codes": ["X"]},
        )
        self.assertTrue(any("ELIGIB" in e.upper() for e in errors))

    def test_assignment_does_not_grant_access(self):
        # ACTIVE assignment carries no resource-access authority by contract.
        errors = validate_role_assignment(
            make_assignment(
                assignment_state="ACTIVE",
                grants_resource_access=True,
            ),
            self._eligible(),
        )
        self.assertTrue(any("ACCESS" in e.upper() for e in errors))


class IndependenceTests(unittest.TestCase):
    def _asg(self, ref, role_class="CONTENT_AUTHOR_ARABIC_PAIRS"):
        return {
            "assignment_id": f"ASG-{ref}",
            "personnel_reference": ref,
            "role_class": role_class,
            "suite_or_scope_id": "SUITE-1",
        }

    def test_distinct_people_pass(self):
        assignments = [
            self._asg("P-1"),
            self._asg("P-2"),
            self._asg("P-3", "CLINICAL_REVIEWER_ARABIC_PAIRS"),
        ]
        self.assertEqual(validate_independence(assignments), [])

    def test_same_person_author_and_reviewer_collides(self):
        assignments = [
            self._asg("P-1", "CONTENT_AUTHOR_ARABIC_PAIRS"),
            self._asg("P-1", "CLINICAL_REVIEWER_ARABIC_PAIRS"),
        ]
        errors = validate_independence(assignments)
        self.assertTrue(any("COLLISION" in e.upper() for e in errors))

    def test_adjudicator_collision_detected(self):
        assignments = [
            self._asg("P-1", "CONTENT_AUTHOR_ARABIC_PAIRS"),
            self._asg("P-2", "ADJUDICATOR_ARABIC_PAIRS"),
            self._asg("P-2", "CLINICAL_REVIEWER_ARABIC_PAIRS"),
        ]
        errors = validate_independence(assignments)
        self.assertTrue(errors)


class HandshakeTests(unittest.TestCase):
    def test_allow_grant_consideration_for_eligible(self):
        result = evaluate_a7_handshake(
            make_assignment(assignment_state="ACTIVE"),
            {
                "state": "ELIGIBLE",
                "reason_codes": [],
                "result_exposure_state": "RESULT_BLIND",
                "stale": False,
            },
        )
        self.assertEqual(result["signal"], "ALLOW_GRANT_CONSIDERATION")
        # ALLOW_GRANT_CONSIDERATION is NOT an actual grant.
        self.assertNotIn("granted_resource_access", result)

    def test_deny_for_ineligible(self):
        result = evaluate_a7_handshake(
            make_assignment(assignment_state="PROPOSED"),
            {"state": "INELIGIBLE", "reason_codes": ["X"], "stale": False},
        )
        self.assertEqual(result["signal"], "DENY_GRANT")

    def test_stale_requires_revalidation(self):
        result = evaluate_a7_handshake(
            make_assignment(assignment_state="ACTIVE"),
            {"state": "STALE_RECOMPUTE_REQUIRED", "reason_codes": [], "stale": True},
        )
        self.assertEqual(result["signal"], "REVALIDATION_REQUIRED")


if __name__ == "__main__":
    unittest.main()
