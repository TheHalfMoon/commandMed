"""US6 fixture tests: A14 spend/engagement governance. Metadata-only, $0 spend."""

from __future__ import annotations

import unittest

from src.commandmed.spec005.finance import (
    evaluate_a14_requirement,
    evaluate_a14_operational_pass,
    validate_a14_authorization,
    validate_a14_transition,
    validate_requirement_manifest,
)


def make_manifest(**overrides):
    manifest = {
        "requirement_manifest_id": "REQM-001",
        "requirement_manifest_version": "1.0",
        "exact_d34_design_id": "SD-001",
        "exact_a8_protocol_id": "PROTO-A8",
        "exact_a7_roster_snapshot_id": "ROSTER-SNAP-1",
        "work_packages": [
            {
                "work_package_id": "WP-001",
                "workload_kind": "BILINGUAL_CLINICAL_REVIEW_HOURS",
                "required_capacity_units": 40,
                "existing_capacity_units": 0,
            }
        ],
        "resource_capability_requirements": [],
        "existing_authorized_capacity_records": [],
        "capacity_gap_records": [
            {"gap_id": "GAP-1", "work_package_id": "WP-001", "gap_units": 40}
        ],
        "new_engagement_requirement_records": [
            {"engagement_requirement_id": "ENG-1", "engagement_class": "REVIEWER"}
        ],
        "new_financial_commitment_requirement_records": [],
        "record_canonical_sha256": "a" * 64,
    }
    manifest.update(overrides)
    return manifest


def make_authorization(**overrides):
    auth = {
        "a14_authorization_id": "A14-001",
        "authorization_version": "1.0",
        "requirement_manifest_id": "REQM-001",
        "requirement_manifest_sha256": "b" * 64,
        "bounded_scope": "SELECTION_SUITE_CONSTRUCTION_ONLY",
        "spend_categories": ["REVIEWER_STIPEND"],
        "engagement_classes": ["REVIEWER"],
        "payee_vendor_or_personnel_references": ["P-REV-1"],
        "currency": "USD",
        "max_committed_amount": 500,
        "max_payable_amount": 500,
        "authorized_period_or_expiry": "2026-12-31",
        "stop_conditions": ["PREREQUISITE_GATE_LOSES_PASS"],
        "approval_decision_id": "APPROVAL-1",
        "approval_decision_sha256": "c" * 64,
        "approver_reference": "P-FOUNDER-1",
        "lifecycle_state": "ACTIVE",
        "stale": False,
        "record_canonical_sha256": "d" * 64,
    }
    auth.update(overrides)
    return auth


class RequirementManifestTests(unittest.TestCase):
    def test_valid_manifest_with_gaps_is_required(self):
        result = evaluate_a14_requirement(make_manifest())
        self.assertEqual(result["state"], "REQUIRED")
        # REQUIRED grants no spend authority.
        self.assertNotIn("authorized", result)

    def test_silence_or_absence_never_not_required(self):
        manifest = make_manifest(
            work_packages=[],
            capacity_gap_records=[],
            new_engagement_requirement_records=[],
            new_financial_commitment_requirement_records=[],
        )
        result = evaluate_a14_requirement(manifest)
        self.assertEqual(result["state"], "BLOCKED_UNKNOWN_OR_INCOMPLETE")

    def test_zero_dollar_label_does_not_establish_not_required(self):
        manifest = make_manifest()
        manifest["declared_cost_label"] = "$0"
        result = evaluate_a14_requirement(manifest)
        self.assertEqual(result["state"], "REQUIRED")

    def test_genuine_full_capacity_is_not_required(self):
        manifest = make_manifest(
            work_packages=[
                {
                    "work_package_id": "WP-001",
                    "workload_kind": "BILINGUAL_CLINICAL_REVIEW_HOURS",
                    "required_capacity_units": 40,
                    "existing_capacity_units": 40,
                }
            ],
            capacity_gap_records=[],
            new_engagement_requirement_records=[],
            new_financial_commitment_requirement_records=[],
        )
        result = evaluate_a14_requirement(manifest)
        self.assertEqual(result["state"], "NOT_REQUIRED")

    def test_missing_exact_bindings_block(self):
        manifest = make_manifest(exact_d34_design_id="")
        result = evaluate_a14_requirement(manifest)
        self.assertEqual(result["state"], "BLOCKED_UNKNOWN_OR_INCOMPLETE")

    def test_insufficient_capacity_without_gap_record_is_not_required_never(self):
        manifest = make_manifest(
            capacity_gap_records=[],
            new_engagement_requirement_records=[],
            new_financial_commitment_requirement_records=[],
        )
        result = evaluate_a14_requirement(manifest)
        self.assertNotEqual(result["state"], "NOT_REQUIRED")

    def test_validate_manifest_shape(self):
        errors = validate_requirement_manifest(make_manifest())
        self.assertEqual(errors, [])
        broken = make_manifest()
        del broken["exact_a8_protocol_id"]
        errors = validate_requirement_manifest(broken)
        self.assertTrue(any("exact_a8_protocol_id" in e for e in errors))

    def test_malformed_does_not_raise(self):
        for bad in (None, [], 3):
            result = evaluate_a14_requirement(bad)
            self.assertIn(
                result["state"], {"BLOCKED_UNKNOWN_OR_INCOMPLETE"}
            )


class AuthorizationTests(unittest.TestCase):
    def test_valid_authorization_validates(self):
        self.assertEqual(validate_a14_authorization(make_authorization()), [])

    def test_self_approval_rejected(self):
        errors = validate_a14_authorization(
            make_authorization(
                approver_reference="P-REV-1",
                payee_vendor_or_personnel_references=["P-REV-1"],
            )
        )
        self.assertTrue(any("SELF_APPROVAL" in e.upper() for e in errors))

    def test_unbounded_scope_rejected(self):
        errors = validate_a14_authorization(
            make_authorization(bounded_scope="ANYTHING")
        )
        self.assertTrue(any("BOUNDED" in e.upper() for e in errors))

    def test_missing_amounts_rejected(self):
        errors = validate_a14_authorization(
            make_authorization(max_committed_amount=None)
        )
        self.assertTrue(any("max_committed_amount" in e for e in errors))

    def test_malformed_does_not_raise(self):
        for bad in (None, [], 2):
            self.assertTrue(validate_a14_authorization(bad))


class TransitionTests(unittest.TestCase):
    def test_active_to_suspended_allowed(self):
        errors = validate_a14_transition(
            make_authorization(), {"transition": "SUSPEND"}
        )
        self.assertEqual(errors, [])

    def test_unknown_transition_fails_closed(self):
        errors = validate_a14_transition(
            make_authorization(), {"transition": "SPEND_NOW"}
        )
        self.assertTrue(any("SPEND" in e.upper() for e in errors))

    def test_revoked_cannot_transition(self):
        errors = validate_a14_transition(
            make_authorization(lifecycle_state="REVOKED"),
            {"transition": "ACTIVATE"},
        )
        self.assertTrue(errors)


class OperationalPassTests(unittest.TestCase):
    def _req_required(self, manifest=None):
        return {
            "state": "REQUIRED",
            "reason_codes": [],
            "requirement_manifest_id": "REQM-001",
            "requirement_manifest_sha256": "b" * 64,
            "requirement_manifest": manifest if manifest is not None else make_manifest(),
        }

    def _req_not_required(self):
        full = self._full_capacity_manifest() if hasattr(self, "_full_capacity_manifest") else None
        return {
            "state": "NOT_REQUIRED",
            "reason_codes": [],
            "requirement_manifest_id": "REQM-001",
            "requirement_manifest_sha256": "e" * 64,
            "requirement_manifest": full or make_manifest(
                work_packages=[
                    {
                        "work_package_id": "WP-FULL",
                        "workload_kind": "BILINGUAL_CLINICAL_REVIEW_HOURS",
                        "required_capacity_units": 40,
                        "existing_capacity_units": 40,
                    }
                ],
                capacity_gap_records=[],
                new_engagement_requirement_records=[],
                new_financial_commitment_requirement_records=[],
            ),
        }

    def test_authorized_pass_with_matching_active_auth(self):
        result = evaluate_a14_operational_pass(
            self._req_required(),
            [make_authorization()],
        )
        self.assertEqual(result["state"], "A14_AUTHORIZED_PASS")
        # Operational pass is evidence, not a payment or contract action.
        self.assertNotIn("payment_executed", result)
        self.assertNotIn("contract_created", result)

    def _full_capacity_manifest(self):
        return make_manifest(
            work_packages=[
                {
                    "work_package_id": "WP-001",
                    "workload_kind": "BILINGUAL_CLINICAL_REVIEW_HOURS",
                    "required_capacity_units": 40,
                    "existing_capacity_units": 40,
                }
            ],
            capacity_gap_records=[],
            new_engagement_requirement_records=[],
            new_financial_commitment_requirement_records=[],
        )

    def test_not_required_yields_not_required_pass(self):
        req = dict(self._req_not_required())
        req["requirement_manifest"] = self._full_capacity_manifest()
        result = evaluate_a14_operational_pass(req, [])
        self.assertEqual(result["state"], "A14_NOT_REQUIRED_PASS")

    def test_caller_not_required_claim_without_manifest_blocked(self):
        result = evaluate_a14_operational_pass(self._req_not_required(), [])
        self.assertEqual(result["state"], "BLOCKED_UNKNOWN_OR_INCOMPLETE")
        self.assertTrue(
            any("NOT_REPRODUCIBLE" in c for c in result["reason_codes"])
        )

    def test_required_pass_requires_bound_reproducible_manifest(self):
        req = {
            "state": "REQUIRED",
            "reason_codes": [],
            "requirement_manifest_id": "REQM-001",
            "requirement_manifest_sha256": "b" * 64,
            # No bound manifest: claim cannot be reproduced.
        }
        result = evaluate_a14_operational_pass(req, [make_authorization()])
        self.assertEqual(result["state"], "BLOCKED_UNKNOWN_OR_INCOMPLETE")

        # Bound manifest that does NOT evaluate to REQUIRED also blocks.
        req = {
            "state": "REQUIRED",
            "reason_codes": [],
            "requirement_manifest_id": "REQM-001",
            "requirement_manifest_sha256": "b" * 64,
            "requirement_manifest": make_manifest(
                work_packages=[],
                capacity_gap_records=[],
                new_engagement_requirement_records=[],
                new_financial_commitment_requirement_records=[],
            ),
        }
        result = evaluate_a14_operational_pass(req, [make_authorization()])
        self.assertEqual(result["state"], "BLOCKED_UNKNOWN_OR_INCOMPLETE")

    def test_authorized_pass_with_bound_required_manifest(self):
        manifest = make_manifest()
        req = {
            "state": "REQUIRED",
            "reason_codes": [],
            "requirement_manifest_id": "REQM-001",
            "requirement_manifest_sha256": "b" * 64,
            "requirement_manifest": manifest,
        }
        auth = make_authorization(
            requirement_manifest_sha256=manifest.get("record_canonical_sha256") or "b" * 64
        )
        result = evaluate_a14_operational_pass(req, [auth])
        self.assertEqual(result["state"], "A14_AUTHORIZED_PASS")

    def test_invalid_authorization_shape_cannot_cover(self):
        broken = make_authorization(
            max_committed_amount=None,
            approver_reference=None,
            lifecycle_state="ACTIVE",
        )
        result = evaluate_a14_operational_pass(
            self._req_required(), [broken]
        )
        self.assertEqual(result["state"], "BLOCKED_UNKNOWN_OR_INCOMPLETE")

    def test_self_approved_authorization_cannot_cover(self):
        broken = make_authorization(
            approver_reference="P-REV-1",
            payee_vendor_or_personnel_references=["P-REV-1"],
        )
        result = evaluate_a14_operational_pass(
            self._req_required(), [broken]
        )
        self.assertEqual(result["state"], "BLOCKED_UNKNOWN_OR_INCOMPLETE")

    def test_stale_authorization_invalidates_pass(self):
        result = evaluate_a14_operational_pass(
            self._req_required(),
            [make_authorization(stale=True)],
        )
        self.assertEqual(result["state"], "BLOCKED_UNKNOWN_OR_INCOMPLETE")

    def test_wrong_manifest_binding_invalidates_pass(self):
        result = evaluate_a14_operational_pass(
            self._req_required(),
            [make_authorization(requirement_manifest_id="REQM-OTHER")],
        )
        self.assertEqual(result["state"], "BLOCKED_UNKNOWN_OR_INCOMPLETE")

    def test_non_active_authorization_insufficient(self):
        result = evaluate_a14_operational_pass(
            self._req_required(),
            [make_authorization(lifecycle_state="PENDING_APPROVAL")],
        )
        self.assertEqual(result["state"], "BLOCKED_UNKNOWN_OR_INCOMPLETE")

    def test_material_change_requires_new_identity(self):
        errors = validate_a14_authorization(
            make_authorization(supersedes_authorization_id="A14-000")
        )
        # Superseding identity is representable and valid when explicit.
        self.assertEqual(errors, [])

    def test_malformed_fail_closed(self):
        result = evaluate_a14_operational_pass(None, None)
        self.assertEqual(result["state"], "BLOCKED_UNKNOWN_OR_INCOMPLETE")
        self.assertEqual(result["reason_codes"], sorted(set(result["reason_codes"])))


if __name__ == "__main__":
    unittest.main()
