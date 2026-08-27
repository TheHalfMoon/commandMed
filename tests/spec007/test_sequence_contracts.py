"""I011-I015 RED tests for rendering, loss, packing, and semantic fixtures."""

from __future__ import annotations

import copy
import unittest

from src.commandmed.spec007.sequence import (
    compute_loss_mask_policy_sha256,
    compute_prompt_rendering_policy_sha256,
    evaluate_truncation_admission,
    validate_loss_mask_policy,
    validate_multi_turn_semantic_fixture,
    validate_packing_truncation_policy,
    validate_prompt_rendering_policy,
)

TOKEN_CLASSES = (
    "SYSTEM",
    "USER",
    "ASSISTANT_NATURAL_LANGUAGE",
    "ASSISTANT_TOOL_CALL",
    "TOOL_RESULT",
    "SAFETY_CONTROL",
    "SEPARATOR_OR_SPECIAL",
    "PADDING",
)


def valid_rendering_policy() -> dict:
    policy = {
        "policy_id": "render-policy-v1",
        "policy_sha256": "0" * 64,
        "base_checkpoint_binding_id": "NEEDS_EVIDENCE",
        "tokenizer_identity": "NEEDS_EVIDENCE",
        "chat_template_identity": "NEEDS_EVIDENCE",
        "normalization_policy": "PRESERVE_SEMANTICS_V1",
        "system_message_policy": "RENDER_EXPLICITLY",
        "tool_schema_rendering_policy": "RENDER_BOUND_TOOL_SCHEMA",
        "bos_policy": "EXPLICIT_POLICY_BOUND",
        "eos_policy": "EXPLICIT_POLICY_BOUND",
        "special_token_map_identity": "NEEDS_EVIDENCE",
        "target_turn_policy": "ASSISTANT_TARGETS_ONLY",
        "multi_turn_continuation_policy": "PRESERVE_REQUIRED_CONTEXT",
    }
    policy["policy_sha256"] = compute_prompt_rendering_policy_sha256(policy)
    return policy


def valid_loss_policy() -> dict:
    policy = {
        "policy_id": "loss-policy-v1",
        "policy_sha256": "0" * 64,
        "rendering_policy_id": "render-policy-v1",
        "token_class_rules": {
            "SYSTEM": "MASKED",
            "USER": "MASKED",
            "ASSISTANT_NATURAL_LANGUAGE": "SUPERVISED",
            "ASSISTANT_TOOL_CALL": "SUPERVISED",
            "TOOL_RESULT": "MASKED",
            "SAFETY_CONTROL": "SUPERVISED",
            "SEPARATOR_OR_SPECIAL": "MASKED",
            "PADDING": "MASKED",
        },
        "unknown_token_class_behavior": "FAIL_CLOSED",
        "padding_behavior": "MASKED",
        "validation_fixture_set_id": "synthetic-sequence-fixtures-v1",
    }
    policy["policy_sha256"] = compute_loss_mask_policy_sha256(policy)
    return policy


def valid_packing_policy() -> dict:
    return {
        "policy_id": "packing-v1",
        "packing_mode": "BOUNDARY_SAFE",
        "cross_example_attention_allowed": False,
        "truncation_mode": "SAFE_SEGMENTATION_ONLY",
        "safe_segmentation_mode": "RETAIN_ALL_REQUIRED_CONTEXT_CLASSES",
        "required_context_classes": [
            "PATIENT_FACTS_REQUIRED_FOR_TARGET",
            "SAFETY_OR_EMERGENCY_CONTEXT",
            "TOOL_SCHEMA_REQUIRED_FOR_TARGET",
            "SUPERVISED_TARGET",
            "MATERIAL_CONVERSATION_STATE",
        ],
        "reason_code_vocabulary_id": "spec007-truncation-reasons-v1",
    }


class TestPromptRenderingPolicy(unittest.TestCase):
    def test_valid_policy_passes_and_identity_is_bound(self):
        policy = valid_rendering_policy()
        self.assertEqual([], validate_prompt_rendering_policy(policy))
        bad = copy.deepcopy(policy)
        bad["policy_sha256"] = "f" * 64
        self.assertTrue(any("policy_sha256 mismatch" in e for e in validate_prompt_rendering_policy(bad)))

    def test_undeclared_and_missing_fields_fail(self):
        policy = valid_rendering_policy()
        del policy["bos_policy"]
        policy["extra"] = "forbidden"
        self.assertTrue(validate_prompt_rendering_policy(policy))


class TestLossMaskPolicy(unittest.TestCase):
    def test_every_required_token_class_is_explicit(self):
        policy = valid_loss_policy()
        self.assertEqual([], validate_loss_mask_policy(policy))
        self.assertEqual(set(TOKEN_CLASSES), set(policy["token_class_rules"]))

    def test_missing_unknown_or_invalid_token_rule_fails(self):
        for mutation in ("missing", "unknown", "invalid"):
            policy = valid_loss_policy()
            if mutation == "missing":
                del policy["token_class_rules"]["TOOL_RESULT"]
            elif mutation == "unknown":
                policy["token_class_rules"]["HIDDEN_REASONING"] = "SUPERVISED"
            else:
                policy["token_class_rules"]["USER"] = "AUTO"
            policy["policy_sha256"] = compute_loss_mask_policy_sha256(policy)
            self.assertTrue(validate_loss_mask_policy(policy), mutation)

    def test_fail_closed_and_padding_contracts_are_frozen(self):
        policy = valid_loss_policy()
        policy["unknown_token_class_behavior"] = "IGNORE"
        policy["padding_behavior"] = "SUPERVISED"
        policy["policy_sha256"] = compute_loss_mask_policy_sha256(policy)
        errors = validate_loss_mask_policy(policy)
        self.assertTrue(any("unknown_token_class_behavior" in e for e in errors))
        self.assertTrue(any("padding_behavior" in e for e in errors))


class TestPackingAndTruncation(unittest.TestCase):
    def test_valid_policy_passes(self):
        self.assertEqual([], validate_packing_truncation_policy(valid_packing_policy()))

    def test_cross_example_attention_and_unknown_context_fail(self):
        policy = valid_packing_policy()
        policy["cross_example_attention_allowed"] = True
        policy["required_context_classes"].append("UNDECLARED_CONTEXT")
        self.assertTrue(validate_packing_truncation_policy(policy))

    def test_required_context_cannot_be_silently_truncated(self):
        policy = valid_packing_policy()
        present = set(policy["required_context_classes"])
        retained = present - {"SAFETY_OR_EMERGENCY_CONTEXT"}
        decision = evaluate_truncation_admission(policy, present, retained)
        self.assertFalse(decision["allowed"])
        self.assertEqual(
            ["REQUIRED_CONTEXT_TRUNCATED:SAFETY_OR_EMERGENCY_CONTEXT"],
            decision["reason_codes"],
        )

    def test_complete_required_context_is_admitted(self):
        policy = valid_packing_policy()
        present = set(policy["required_context_classes"])
        decision = evaluate_truncation_admission(policy, present, present)
        self.assertTrue(decision["allowed"])
        self.assertEqual([], decision["reason_codes"])


class TestMultiTurnToolSemanticFixtures(unittest.TestCase):
    def test_static_multi_turn_tool_fixture_conforms_without_execution(self):
        fixture = {
            "fixture_id": "multi-turn-tool-001",
            "turns": [
                {"turn_index": 0, "token_class": "SYSTEM", "text_kind": "STATIC_SYNTHETIC"},
                {"turn_index": 1, "token_class": "USER", "text_kind": "STATIC_SYNTHETIC"},
                {"turn_index": 2, "token_class": "ASSISTANT_TOOL_CALL", "text_kind": "STATIC_SYNTHETIC"},
                {"turn_index": 3, "token_class": "TOOL_RESULT", "text_kind": "STATIC_SYNTHETIC"},
                {"turn_index": 4, "token_class": "ASSISTANT_NATURAL_LANGUAGE", "text_kind": "STATIC_SYNTHETIC"},
            ],
            "tool_execution_performed": False,
            "model_execution_performed": False,
        }
        self.assertEqual([], validate_multi_turn_semantic_fixture(fixture, valid_loss_policy()))

    def test_fixture_rejects_execution_or_unknown_token_class(self):
        fixture = {
            "fixture_id": "multi-turn-tool-002",
            "turns": [{"turn_index": 0, "token_class": "HIDDEN_REASONING", "text_kind": "STATIC_SYNTHETIC"}],
            "tool_execution_performed": True,
            "model_execution_performed": False,
        }
        errors = validate_multi_turn_semantic_fixture(fixture, valid_loss_policy())
        self.assertTrue(any("tool_execution_performed" in e for e in errors))
        self.assertTrue(any("unknown token_class" in e for e in errors))


if __name__ == "__main__":
    unittest.main()
