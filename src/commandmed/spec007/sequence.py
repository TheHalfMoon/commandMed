"""Offline prompt, loss-mask, packing, and semantic sequence contracts."""

from __future__ import annotations

from typing import Any, Iterable

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.spec007.foundation import (
    validate_canonical_sha256,
    validate_closed_object,
)

_TOKEN_CLASSES = (
    "SYSTEM",
    "USER",
    "ASSISTANT_NATURAL_LANGUAGE",
    "ASSISTANT_TOOL_CALL",
    "TOOL_RESULT",
    "SAFETY_CONTROL",
    "SEPARATOR_OR_SPECIAL",
    "PADDING",
)
_TOKEN_RULES = frozenset({"SUPERVISED", "MASKED"})
_REQUIRED_CONTEXT_CLASSES = frozenset(
    {
        "PATIENT_FACTS_REQUIRED_FOR_TARGET",
        "SAFETY_OR_EMERGENCY_CONTEXT",
        "TOOL_SCHEMA_REQUIRED_FOR_TARGET",
        "SUPERVISED_TARGET",
        "MATERIAL_CONVERSATION_STATE",
    }
)
_RENDERING_FIELDS = (
    "policy_id",
    "policy_sha256",
    "base_checkpoint_binding_id",
    "tokenizer_identity",
    "chat_template_identity",
    "normalization_policy",
    "system_message_policy",
    "tool_schema_rendering_policy",
    "bos_policy",
    "eos_policy",
    "special_token_map_identity",
    "target_turn_policy",
    "multi_turn_continuation_policy",
)
_LOSS_FIELDS = (
    "policy_id",
    "policy_sha256",
    "rendering_policy_id",
    "token_class_rules",
    "unknown_token_class_behavior",
    "padding_behavior",
    "validation_fixture_set_id",
)
_PACKING_FIELDS = (
    "policy_id",
    "packing_mode",
    "cross_example_attention_allowed",
    "truncation_mode",
    "safe_segmentation_mode",
    "required_context_classes",
    "reason_code_vocabulary_id",
)
_FIXTURE_FIELDS = (
    "fixture_id",
    "turns",
    "tool_execution_performed",
    "model_execution_performed",
)
_TURN_FIELDS = ("turn_index", "token_class", "text_kind")


def _nonempty_string(value: Any) -> bool:
    return isinstance(value, str) and bool(value.strip())


def _self_excluding_sha256(record: dict[str, Any], identity_field: str) -> str:
    projection = dict(record)
    projection.pop(identity_field, None)
    return compute_canonical_sha256(projection)


def compute_prompt_rendering_policy_sha256(policy: dict[str, Any]) -> str:
    return _self_excluding_sha256(policy, "policy_sha256")


def compute_loss_mask_policy_sha256(policy: dict[str, Any]) -> str:
    return _self_excluding_sha256(policy, "policy_sha256")


def validate_prompt_rendering_policy(policy: Any) -> list[str]:
    prefix = "PromptRenderingPolicy"
    errors = validate_closed_object(policy, required_fields=_RENDERING_FIELDS, field=prefix)
    if errors or not isinstance(policy, dict):
        return errors

    for field in _RENDERING_FIELDS:
        if field == "policy_sha256":
            continue
        if not _nonempty_string(policy.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")
    errors.extend(validate_canonical_sha256(policy.get("policy_sha256"), "policy_sha256"))
    claimed = policy.get("policy_sha256")
    if (
        isinstance(claimed, str)
        and len(claimed) == 64
        and all(ch in "0123456789abcdef" for ch in claimed)
        and claimed != compute_prompt_rendering_policy_sha256(policy)
    ):
        errors.append(f"{prefix}: policy_sha256 mismatch")
    return errors


def validate_loss_mask_policy(policy: Any) -> list[str]:
    prefix = "LossMaskPolicy"
    errors = validate_closed_object(policy, required_fields=_LOSS_FIELDS, field=prefix)
    if errors or not isinstance(policy, dict):
        return errors

    for field in ("policy_id", "rendering_policy_id", "validation_fixture_set_id"):
        if not _nonempty_string(policy.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")
    errors.extend(validate_canonical_sha256(policy.get("policy_sha256"), "policy_sha256"))

    rules = policy.get("token_class_rules")
    if not isinstance(rules, dict):
        errors.append(f"{prefix}: token_class_rules must be an object")
    else:
        non_string_keys = [key for key in rules if not isinstance(key, str)]
        if non_string_keys:
            errors.append(f"{prefix}: token_class_rules keys must be strings")
        expected = set(_TOKEN_CLASSES)
        present = {key for key in rules if isinstance(key, str)}
        missing = sorted(expected - present)
        undeclared = sorted(present - expected)
        if missing:
            errors.append(f"{prefix}: token_class_rules missing {missing}")
        if undeclared:
            errors.append(f"{prefix}: token_class_rules undeclared {undeclared}")
        for token_class in sorted(expected & present):
            rule = rules[token_class]
            if not isinstance(rule, str) or rule not in _TOKEN_RULES:
                errors.append(
                    f"{prefix}: token_class_rules.{token_class} must be SUPERVISED or MASKED"
                )

    if policy.get("unknown_token_class_behavior") != "FAIL_CLOSED":
        errors.append(f"{prefix}: unknown_token_class_behavior must equal 'FAIL_CLOSED'")
    if policy.get("padding_behavior") != "MASKED":
        errors.append(f"{prefix}: padding_behavior must equal 'MASKED'")

    claimed = policy.get("policy_sha256")
    if (
        isinstance(claimed, str)
        and len(claimed) == 64
        and all(ch in "0123456789abcdef" for ch in claimed)
        and claimed != compute_loss_mask_policy_sha256(policy)
    ):
        errors.append(f"{prefix}: policy_sha256 mismatch")
    return errors


def validate_packing_truncation_policy(policy: Any) -> list[str]:
    prefix = "PackingTruncationPolicy"
    errors = validate_closed_object(policy, required_fields=_PACKING_FIELDS, field=prefix)
    if errors or not isinstance(policy, dict):
        return errors

    for field in ("policy_id", "safe_segmentation_mode", "reason_code_vocabulary_id"):
        if not _nonempty_string(policy.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")
    if policy.get("packing_mode") not in {"DISABLED", "BOUNDARY_SAFE", "NEEDS_EVIDENCE"}:
        errors.append(f"{prefix}: invalid packing_mode")
    if policy.get("cross_example_attention_allowed") is not False:
        errors.append(f"{prefix}: cross_example_attention_allowed must be false")
    if policy.get("truncation_mode") not in {"FAIL_CLOSED", "SAFE_SEGMENTATION_ONLY"}:
        errors.append(f"{prefix}: invalid truncation_mode")

    required = policy.get("required_context_classes")
    if not isinstance(required, list) or not required:
        errors.append(f"{prefix}: required_context_classes must be a non-empty list")
    else:
        if any(not isinstance(item, str) for item in required):
            errors.append(f"{prefix}: required_context_classes entries must be strings")
        else:
            if len(required) != len(set(required)):
                errors.append(f"{prefix}: required_context_classes must be unique")
            unknown = sorted(set(required) - _REQUIRED_CONTEXT_CLASSES)
            if unknown:
                errors.append(f"{prefix}: unknown required_context_classes {unknown}")
    return errors


def _context_set(value: Iterable[str], field: str) -> tuple[set[str] | None, list[str]]:
    try:
        materialized = list(value)
    except TypeError:
        return None, [f"{field}: expected iterable of strings"]
    if any(not isinstance(item, str) for item in materialized):
        return None, [f"{field}: entries must be strings"]
    return set(materialized), []


def evaluate_truncation_admission(
    policy: Any,
    present_context_classes: Iterable[str],
    retained_context_classes: Iterable[str],
) -> dict[str, Any]:
    """Evaluate semantic truncation without tokenization or model execution."""
    policy_errors = validate_packing_truncation_policy(policy)
    if policy_errors:
        return {
            "allowed": False,
            "reason_codes": ["INVALID_PACKING_POLICY"],
            "validation_errors": policy_errors,
        }
    present, present_errors = _context_set(present_context_classes, "present_context_classes")
    retained, retained_errors = _context_set(retained_context_classes, "retained_context_classes")
    context_errors = present_errors + retained_errors
    if context_errors or present is None or retained is None:
        return {
            "allowed": False,
            "reason_codes": ["INVALID_CONTEXT_CLASS_INPUT"],
            "validation_errors": context_errors,
        }
    required = set(policy["required_context_classes"])
    truncated = sorted((present & required) - retained)
    reasons = [f"REQUIRED_CONTEXT_TRUNCATED:{item}" for item in truncated]
    return {"allowed": not reasons, "reason_codes": reasons, "validation_errors": []}


def validate_multi_turn_semantic_fixture(
    fixture: Any, loss_policy: Any
) -> list[str]:
    """Validate static multi-turn/tool semantics while forbidding runtime execution."""
    prefix = "MultiTurnSemanticFixture"
    errors = validate_closed_object(fixture, required_fields=_FIXTURE_FIELDS, field=prefix)
    if errors or not isinstance(fixture, dict):
        return errors

    loss_errors = validate_loss_mask_policy(loss_policy)
    if loss_errors:
        errors.append(f"{prefix}: invalid loss policy")
        return errors

    if not _nonempty_string(fixture.get("fixture_id")):
        errors.append(f"{prefix}: fixture_id must be a non-empty string")
    if fixture.get("tool_execution_performed") is not False:
        errors.append(f"{prefix}: tool_execution_performed must be false")
    if fixture.get("model_execution_performed") is not False:
        errors.append(f"{prefix}: model_execution_performed must be false")

    turns = fixture.get("turns")
    if not isinstance(turns, list) or not turns:
        errors.append(f"{prefix}: turns must be a non-empty list")
        return errors

    expected_indexes = list(range(len(turns)))
    actual_indexes: list[Any] = []
    rules = loss_policy["token_class_rules"]
    for index, turn in enumerate(turns):
        turn_prefix = f"{prefix}.turns[{index}]"
        turn_errors = validate_closed_object(turn, required_fields=_TURN_FIELDS, field=turn_prefix)
        errors.extend(turn_errors)
        if turn_errors or not isinstance(turn, dict):
            continue
        actual_indexes.append(turn.get("turn_index"))
        token_class = turn.get("token_class")
        if token_class not in rules:
            errors.append(f"{turn_prefix}: unknown token_class '{token_class}'")
        if turn.get("text_kind") != "STATIC_SYNTHETIC":
            errors.append(f"{turn_prefix}: text_kind must equal 'STATIC_SYNTHETIC'")
    if actual_indexes != expected_indexes:
        errors.append(f"{prefix}: turn_index values must be contiguous from zero")
    return errors