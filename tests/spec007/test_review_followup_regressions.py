"""Final exact-head regression coverage requested during PR #53 review.

All fixtures are synthetic and offline. These tests exercise validation only;
no model, weight, dataset payload, device, network, credential, or training
execution is performed.
"""

from __future__ import annotations

import pytest

from src.commandmed.spec007.preservation import (
    evaluate_abort_sentinel_effect,
    validate_abort_sentinel_policy,
    validate_capability_preservation_binding,
)
from src.commandmed.spec007.selection import validate_checkpoint_ranking_inputs
from src.commandmed.spec007.sequence import (
    evaluate_truncation_admission,
    validate_loss_mask_policy,
    validate_packing_truncation_policy,
)
from tests.spec007.test_preservation_contracts import (
    valid_abort_policy,
    valid_capability_binding,
)
from tests.spec007.test_selection_reproducibility import separately_authorized_policy
from tests.spec007.test_sequence_contracts import valid_loss_policy, valid_packing_policy


@pytest.mark.parametrize("source_class", ["ABORT_SENTINEL", "PROTECTED_EVALUATION"])
def test_structurally_prohibited_ranking_class_fails_even_when_source_is_authorized(
    source_class: str,
) -> None:
    policy = separately_authorized_policy()
    policy["selection_source_ids"] = ["MODEL_SELECTION_DEV_SET"]
    authorization = policy["selection_source_purpose_authorization"]
    assert isinstance(authorization, dict)
    authorization["authorized_source_ids"] = ["MODEL_SELECTION_DEV_SET"]

    decision = validate_checkpoint_ranking_inputs(
        policy,
        [{"source_id": "MODEL_SELECTION_DEV_SET", "source_class": source_class}],
    )

    assert decision["allowed"] is False
    assert decision["reason_code"] == "RANKING_SOURCE_CLASS_PROHIBITED"


def test_nested_loss_rule_value_fails_closed_without_type_error() -> None:
    policy = valid_loss_policy()
    policy["token_class_rules"]["USER"] = ["MASKED"]
    errors = validate_loss_mask_policy(policy)
    assert errors
    assert any("token_class_rules.USER" in error for error in errors)


def test_nested_required_context_class_fails_closed_without_type_error() -> None:
    policy = valid_packing_policy()
    policy["required_context_classes"] = ["SUPERVISED_TARGET", ["SAFETY_OR_EMERGENCY_CONTEXT"]]
    errors = validate_packing_truncation_policy(policy)
    assert errors
    decision = evaluate_truncation_admission(policy, [], [])
    assert decision["allowed"] is False
    assert decision["reason_codes"] == ["INVALID_PACKING_POLICY"]


def test_nested_required_slice_fails_closed_without_type_error() -> None:
    binding = valid_capability_binding()
    binding["required_slices"] = ["SAFETY", ["ARABIC"]]
    errors = validate_capability_preservation_binding(binding)
    assert errors
    assert any("required_slices" in error for error in errors)


def test_nested_allowed_effect_fails_closed_without_type_error() -> None:
    policy = valid_abort_policy()
    policy["allowed_effects"] = ["CONTINUE", ["ABORT_RUN"]]
    errors = validate_abort_sentinel_policy(policy)
    assert errors
    assert any("allowed_effects entries must be strings" in error for error in errors)


def test_nested_effect_argument_fails_closed_without_type_error() -> None:
    decision = evaluate_abort_sentinel_effect(valid_abort_policy(), ["ABORT_RUN"])
    assert decision["allowed"] is False
    assert decision["reason_code"] == "EFFECT_NOT_AUTHORIZED"
