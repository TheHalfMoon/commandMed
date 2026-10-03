from __future__ import annotations

import unittest

from src.commandmed.reliability_v5.preflight import (
    APPROVED_MODEL_REPO,
    APPROVED_MODEL_REVISION,
    DevelopmentAuthority,
    DevelopmentRunManifest,
    evaluate_development_preflight,
)

GOOD_ARTIFACT = "a" * 64
GOOD_CODE = "b" * 40


def authority(**overrides):
    values = dict(approved=True, authority_id="FOUNDER_V5_DEV_BOUNDARY_V1")
    values.update(overrides)
    return DevelopmentAuthority(**values)


def manifest(**overrides):
    values = dict(
        action="INFERENCE",
        model_repo=APPROVED_MODEL_REPO,
        model_revision=APPROVED_MODEL_REVISION,
        model_artifact_sha256=GOOD_ARTIFACT,
        intervention_id="A1_TS_V1",
        data_roles=("RULE_ORACLE_DEVELOPMENT",),
        code_sha=GOOD_CODE,
        environment_id="sha256:" + "c" * 64,
        output_destination="artifacts/v5/development/fixture",
    )
    values.update(overrides)
    return DevelopmentRunManifest(**values)


class DevelopmentPreflightTests(unittest.TestCase):
    def test_default_authority_fails_closed(self):
        decision = evaluate_development_preflight(manifest(), DevelopmentAuthority())
        self.assertFalse(decision.allowed)
        self.assertIn("AUTHORITY_NOT_APPROVED", decision.reason_codes)

    def test_exact_synthetic_authorized_shape_passes(self):
        decision = evaluate_development_preflight(manifest(), authority())
        self.assertTrue(decision.allowed)
        self.assertEqual("PREFLIGHT_PASS", decision.state)
        self.assertEqual((), decision.reason_codes)

    def test_model_revision_and_artifact_identity_are_exact(self):
        decision = evaluate_development_preflight(
            manifest(model_revision="latest", model_artifact_sha256=""), authority()
        )
        self.assertFalse(decision.allowed)
        self.assertIn("MODEL_REVISION_MISMATCH", decision.reason_codes)
        self.assertIn("MODEL_ARTIFACT_HASH_MISSING_OR_INVALID", decision.reason_codes)

    def test_paid_resources_fail_both_authority_and_run_boundaries(self):
        decision = evaluate_development_preflight(
            manifest(paid_resource=True, expected_spend_usd=0.01),
            authority(paid_api=True, spend_usd=0.01),
        )
        self.assertFalse(decision.allowed)
        self.assertIn("AUTHORITY_COST_POLICY_VIOLATION", decision.reason_codes)
        self.assertIn("RUN_COST_POLICY_VIOLATION", decision.reason_codes)

    def test_confirmatory_or_reserve_materialization_is_forbidden(self):
        decision = evaluate_development_preflight(
            manifest(confirmatory_materialized=True, reserve_materialized=True), authority()
        )
        self.assertFalse(decision.allowed)
        self.assertIn("HOLDOUT_MATERIALIZATION_FORBIDDEN", decision.reason_codes)

    def test_phi_and_gated_data_fail_closed(self):
        decision = evaluate_development_preflight(
            manifest(contains_phi=True, uses_gated_data=True), authority()
        )
        self.assertFalse(decision.allowed)
        self.assertIn("PROTECTED_OR_GATED_DATA_FORBIDDEN", decision.reason_codes)

    def test_training_is_restricted_to_b1_c1_c2(self):
        blocked = evaluate_development_preflight(
            manifest(action="TRAINING", intervention_id="A1_TS_V1"), authority()
        )
        self.assertFalse(blocked.allowed)
        self.assertIn("TRAINING_INTERVENTION_NOT_ALLOWED", blocked.reason_codes)
        allowed = evaluate_development_preflight(
            manifest(action="TRAINING", intervention_id="B1_TYPED_V1"), authority()
        )
        self.assertTrue(allowed.allowed)

    def test_squad_retention_role_is_c2_only(self):
        blocked = evaluate_development_preflight(
            manifest(data_roles=("SQUAD_RETENTION",), intervention_id="C1_CRDI_V1"), authority()
        )
        self.assertFalse(blocked.allowed)
        self.assertIn("SQUAD_ROLE_REQUIRES_C2", blocked.reason_codes)
        allowed = evaluate_development_preflight(
            manifest(data_roles=("SQUAD_RETENTION",), intervention_id="C2_CRDI_RETAIN_V1"), authority()
        )
        self.assertTrue(allowed.allowed)

    def test_unknown_intervention_fails_for_inference_too(self):
        decision = evaluate_development_preflight(
            manifest(intervention_id="EXPERIMENTAL_LATEST"), authority()
        )
        self.assertFalse(decision.allowed)
        self.assertIn("INTERVENTION_NOT_ALLOWED", decision.reason_codes)

    def test_environment_and_output_identity_fail_closed(self):
        decision = evaluate_development_preflight(
            manifest(environment_id="latest", output_destination="../outside"), authority()
        )
        self.assertFalse(decision.allowed)
        self.assertIn("ENVIRONMENT_ID_INVALID", decision.reason_codes)
        self.assertIn("OUTPUT_DESTINATION_INVALID", decision.reason_codes)

    def test_unknown_role_and_bad_code_identity_fail(self):
        decision = evaluate_development_preflight(
            manifest(data_roles=("CONFIRMATORY",), code_sha="dirty"), authority()
        )
        self.assertFalse(decision.allowed)
        self.assertIn("DATA_ROLE_NOT_ALLOWED", decision.reason_codes)
        self.assertIn("CODE_SHA_INVALID", decision.reason_codes)


if __name__ == "__main__":
    unittest.main()
