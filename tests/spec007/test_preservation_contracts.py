"""I016-I020 RED tests for language and capability/sentinel preservation."""

from __future__ import annotations

import copy
import unittest

from src.commandmed.spec007.preservation import (
    evaluate_abort_sentinel_effect,
    validate_abort_sentinel_policy,
    validate_capability_preservation_binding,
    validate_language_profile,
    validate_tokenizer_evidence_packet,
)


def valid_language_profile() -> dict:
    return {
        "primary_language": "ar",
        "authored_language": "ar",
        "translation_state": "ORIGINAL",
        "dialect_or_register": "SAUDI_GULF",
        "code_switch_state": "AR_EN_CODE_SWITCH",
        "transliteration_state": "ARABIZI_COVERED",
        "terminology_normalization_id": "arabic-clinical-terms-v1",
        "qualified_review_state": "PASS",
    }


def valid_capability_binding() -> dict:
    return {
        "binding_id": "capability-binding-v1",
        "base_checkpoint_binding_id": "NEEDS_EVIDENCE",
        "candidate_checkpoint_id": "NEEDS_EVIDENCE",
        "frozen_evaluation_protocol_id": "frozen-eval-v1",
        "required_slices": [
            "GENERAL_REASONING",
            "INSTRUCTION_FOLLOWING",
            "MEDICAL_CORE",
            "ARABIC",
            "TOOL_BEHAVIOR",
            "ABSTENTION_SELECTIVE_RISK",
            "SAFETY",
        ],
        "pre_registered_margins_id": "margins-v1",
        "quarantine_verification_id": "quarantine-v1",
    }


def valid_abort_policy() -> dict:
    return {
        "policy_id": "abort-sentinel-v1",
        "sentinel_set_id": "sentinel-set-v1",
        "source_purpose_verification_id": "source-purpose-v1",
        "threshold_record_id": "thresholds-v1",
        "allowed_effects": ["CONTINUE", "ABORT_RUN", "DISQUALIFY_RUN"],
        "can_rank_checkpoints": False,
        "can_tune_recipe": False,
        "can_change_hyperparameters": False,
        "frozen_before_run": True,
    }


class TestLanguageProfile(unittest.TestCase):
    def test_saudi_gulf_code_switch_and_transliteration_profile_passes(self):
        self.assertEqual([], validate_language_profile(valid_language_profile()))

    def test_msa_profile_with_explicit_null_normalization_passes(self):
        profile = valid_language_profile()
        profile.update(
            {
                "dialect_or_register": "MSA",
                "code_switch_state": "NONE",
                "transliteration_state": "NONE",
                "terminology_normalization_id": None,
            }
        )
        self.assertEqual([], validate_language_profile(profile))

    def test_normalization_key_and_review_state_are_mandatory(self):
        profile = valid_language_profile()
        del profile["terminology_normalization_id"]
        self.assertTrue(validate_language_profile(profile))
        profile = valid_language_profile()
        profile["qualified_review_state"] = ""
        self.assertTrue(validate_language_profile(profile))


class TestTokenizerEvidencePacket(unittest.TestCase):
    def test_all_measurements_remain_needs_evidence_without_execution(self):
        packet = {
            "evidence_id": "tokenizer-evidence-v1",
            "candidate_id": "FOUNDER_CHATGPT_SELECTION_REQUIRED",
            "language_profile_id": "arabic-profile-v1",
            "measurements": {
                "token_count": "NEEDS_EVIDENCE",
                "fragmentation_ratio": "NEEDS_EVIDENCE",
                "byte_fallback_rate": "NEEDS_EVIDENCE",
                "code_switch_fragmentation": "NEEDS_EVIDENCE",
                "transliteration_fragmentation": "NEEDS_EVIDENCE",
            },
            "execution_performed": False,
            "recommendation": "NONE",
        }
        self.assertEqual([], validate_tokenizer_evidence_packet(packet))

    def test_measured_value_execution_or_recommendation_is_rejected(self):
        packet = {
            "evidence_id": "tokenizer-evidence-v2",
            "candidate_id": "unauthorized-candidate",
            "language_profile_id": "arabic-profile-v1",
            "measurements": {
                "token_count": 123,
                "fragmentation_ratio": "NEEDS_EVIDENCE",
                "byte_fallback_rate": "NEEDS_EVIDENCE",
                "code_switch_fragmentation": "NEEDS_EVIDENCE",
                "transliteration_fragmentation": "NEEDS_EVIDENCE",
            },
            "execution_performed": True,
            "recommendation": "PREFER",
        }
        errors = validate_tokenizer_evidence_packet(packet)
        self.assertTrue(any("measurements" in e for e in errors))
        self.assertTrue(any("execution_performed" in e for e in errors))
        self.assertTrue(any("recommendation" in e for e in errors))


class TestCapabilityPreservationBinding(unittest.TestCase):
    def test_all_seven_required_slices_are_mandatory(self):
        self.assertEqual([], validate_capability_preservation_binding(valid_capability_binding()))
        binding = valid_capability_binding()
        binding["required_slices"].remove("SAFETY")
        self.assertTrue(validate_capability_preservation_binding(binding))

    def test_unknown_slice_rejected(self):
        binding = valid_capability_binding()
        binding["required_slices"][-1] = "HIDDEN_PREFERENCE"
        self.assertTrue(validate_capability_preservation_binding(binding))


class TestAbortSentinelPolicy(unittest.TestCase):
    def test_frozen_non_optimization_policy_passes(self):
        self.assertEqual([], validate_abort_sentinel_policy(valid_abort_policy()))

    def test_ranking_recipe_hyperparameter_authority_rejected(self):
        for field in ("can_rank_checkpoints", "can_tune_recipe", "can_change_hyperparameters"):
            policy = valid_abort_policy()
            policy[field] = True
            self.assertTrue(validate_abort_sentinel_policy(policy), field)

    def test_only_continue_abort_or_disqualify_effects_are_allowed(self):
        policy = valid_abort_policy()
        policy["allowed_effects"].append("PREFER_EARLY_STOPPING")
        self.assertTrue(validate_abort_sentinel_policy(policy))

    def test_sentinel_cannot_create_preferred_early_stopping(self):
        decision = evaluate_abort_sentinel_effect(valid_abort_policy(), "PREFER_EARLY_STOPPING")
        self.assertFalse(decision["allowed"])
        self.assertEqual("EFFECT_NOT_AUTHORIZED", decision["reason_code"])


if __name__ == "__main__":
    unittest.main()
