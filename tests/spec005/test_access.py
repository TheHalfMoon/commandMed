"""US5 fixture tests: A13 payload/result access firewall. Metadata only."""

from __future__ import annotations

import unittest

from src.commandmed.spec005.access import (
    evaluate_access_disposition,
    validate_access_grant_metadata,
    validate_access_policy,
)

ZONES = ("METADATA_ZONE", "SELECTION_CONTENT_ZONE", "CANDIDATE_RESULT_ZONE")


def make_policy(**overrides):
    policy = {
        "access_policy_id": "AP-001",
        "access_policy_version": "1.0",
        "resource_zones": list(ZONES),
        "default_disposition": "DENY",
        "private_gold_zone": "PRIVATE_GOLD_QUARANTINE_ZONE",
        "export_allowed": False,
        "copy_allowed": False,
        "record_canonical_sha256": "a" * 64,
    }
    policy.update(overrides)
    return policy


def make_grant(**overrides):
    grant = {
        "access_grant_id": "AG-001",
        "personnel_reference": "P-0001",
        "assignment_id": "ASG-001",
        "eligibility_record_id": "EL-001",
        "resource_zone": "METADATA_ZONE",
        "scope_id": "SUITE-1",
        "purpose": "CHECKPOINT_SELECTION",
        "grant_state": "PROPOSED",
        "authorization_reference": "AUTH-REF-1",
        "record_canonical_sha256": "b" * 64,
    }
    grant.update(overrides)
    return grant


def make_handshake(**overrides):
    handshake = {
        "signal": "ALLOW_GRANT_CONSIDERATION",
        "reason_codes": [],
    }
    handshake.update(overrides)
    return handshake


class PolicyTests(unittest.TestCase):
    def test_valid_policy_validates(self):
        self.assertEqual(validate_access_policy(make_policy()), [])

    def test_missing_zone_fails(self):
        policy = make_policy()
        policy["resource_zones"] = ZONES[:2]
        errors = validate_access_policy(policy)
        self.assertTrue(any("ZONE" in e.upper() for e in errors))

    def test_default_must_deny(self):
        errors = validate_access_policy(make_policy(default_disposition="ALLOW"))
        self.assertTrue(any("DEFAULT" in e.upper() and "DENY" in e.upper() for e in errors))

    def test_private_gold_outside_selection_zones(self):
        errors = validate_access_policy(
            make_policy(private_gold_zone="SELECTION_CONTENT_ZONE")
        )
        self.assertTrue(any("PRIVATE_GOLD" in e.upper() for e in errors))

    def test_malformed_does_not_raise(self):
        for bad in (None, 7, []):
            self.assertTrue(validate_access_policy(bad))


class GrantTests(unittest.TestCase):
    def test_metadata_zone_consideration_validates(self):
        errors = validate_access_grant_metadata(
            make_grant(), make_handshake()
        )
        self.assertEqual(errors, [])

    def test_content_or_result_zone_never_directly_granted(self):
        for zone in ("SELECTION_CONTENT_ZONE", "CANDIDATE_RESULT_ZONE"):
            errors = validate_access_grant_metadata(
                make_grant(resource_zone=zone), make_handshake()
            )
            self.assertTrue(
                any("DIRECT" in e.upper() or zone in e for e in errors),
                f"expected rejection for {zone}",
            )

    def test_allow_is_not_a_grant(self):
        errors = validate_access_grant_metadata(
            make_grant(grant_state="ACTIVE"), make_handshake()
        )
        self.assertTrue(any("NOT_A_GRANT" in e.upper() for e in errors))

    def test_unknown_zone_fails_closed(self):
        errors = validate_access_grant_metadata(
            make_grant(resource_zone="ZONE_HOLODECK"), make_handshake()
        )
        self.assertTrue(any("ZONE_HOLODECK" in e for e in errors))

    def test_malformed_does_not_raise(self):
        for bad in (None, [], "x"):
            errors = validate_access_grant_metadata(bad, make_handshake())
            self.assertIsInstance(errors, list)
            self.assertTrue(errors)


class DispositionTests(unittest.TestCase):
    def test_allow_signal_yields_consideration_not_access(self):
        result = evaluate_access_disposition(make_grant(), make_handshake())
        self.assertEqual(result["state"], "GRANT_CONSIDERATION_ALLOWED")
        self.assertNotIn("granted", result)

    def test_deny_cannot_be_overridden(self):
        handshake = make_handshake(signal="DENY_GRANT")
        grant = make_grant(caller_override=True, approved=True)
        result = evaluate_access_disposition(grant, handshake)
        self.assertEqual(result["state"], "DENIED")

    def test_revoke_signal_revokes(self):
        result = evaluate_access_disposition(
            make_grant(), make_handshake(signal="REVOKE_REQUIRED")
        )
        self.assertEqual(result["state"], "REVOCATION_REQUIRED")

    def test_stale_identity_requires_revalidation(self):
        result = evaluate_access_disposition(
            make_grant(),
            make_handshake(
                signal="REVALIDATION_REQUIRED",
                stale=True,
                identity_state="STALE_RECOMPUTE_REQUIRED",
            ),
        )
        self.assertEqual(result["state"], "REVALIDATION_REQUIRED")

    def test_result_zone_denied_to_active_content_roles(self):
        result = evaluate_access_disposition(
            make_grant(
                resource_zone="CANDIDATE_RESULT_ZONE",
                holder_role_class="CONTENT_AUTHOR_ARABIC_PAIRS",
                holder_result_exposure="RESULT_BLIND",
            ),
            make_handshake(),
        )
        self.assertEqual(result["state"], "DENIED")

    def test_default_deny_without_signal(self):
        result = evaluate_access_disposition(make_grant(), {})
        self.assertEqual(result["state"], "DENIED")

    def test_malformed_fail_closed(self):
        result = evaluate_access_disposition(None, None)
        self.assertEqual(result["state"], "DENIED")
        self.assertEqual(result["reason_codes"], sorted(set(result["reason_codes"])))


if __name__ == "__main__":
    unittest.main()
