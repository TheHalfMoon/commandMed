"""Offline language, capability-preservation, and abort-sentinel contracts."""

from __future__ import annotations

from typing import Any

from src.commandmed.spec007.curriculum import TRANSLATION_STATES
from src.commandmed.spec007.foundation import validate_closed_object

_LANGUAGE_FIELDS = (
    "primary_language",
    "authored_language",
    "translation_state",
    "dialect_or_register",
    "code_switch_state",
    "transliteration_state",
    "terminology_normalization_id",
    "qualified_review_state",
)
_TOKENIZER_EVIDENCE_FIELDS = (
    "evidence_id",
    "candidate_id",
    "language_profile_id",
    "measurements",
    "execution_performed",
    "recommendation",
)
_TOKENIZER_MEASUREMENTS = (
    "token_count",
    "fragmentation_ratio",
    "byte_fallback_rate",
    "code_switch_fragmentation",
    "transliteration_fragmentation",
)
_CAPABILITY_FIELDS = (
    "binding_id",
    "base_checkpoint_binding_id",
    "candidate_checkpoint_id",
    "frozen_evaluation_protocol_id",
    "required_slices",
    "pre_registered_margins_id",
    "quarantine_verification_id",
)
_REQUIRED_SLICES = frozenset(
    {
        "GENERAL_REASONING",
        "INSTRUCTION_FOLLOWING",
        "MEDICAL_CORE",
        "ARABIC",
        "TOOL_BEHAVIOR",
        "ABSTENTION_SELECTIVE_RISK",
        "SAFETY",
    }
)
_ABORT_FIELDS = (
    "policy_id",
    "sentinel_set_id",
    "source_purpose_verification_id",
    "threshold_record_id",
    "allowed_effects",
    "can_rank_checkpoints",
    "can_tune_recipe",
    "can_change_hyperparameters",
    "frozen_before_run",
)
_ALLOWED_SENTINEL_EFFECTS = frozenset({"CONTINUE", "ABORT_RUN", "DISQUALIFY_RUN"})


def _nonempty(value: Any, *, min_length: int = 1) -> bool:
    return isinstance(value, str) and len(value) >= min_length and bool(value.strip())


def validate_language_profile(profile: Any) -> list[str]:
    """Validate the full Spec 007 LanguageProfile shape without runtime evidence."""
    prefix = "LanguageProfile"
    errors = validate_closed_object(profile, required_fields=_LANGUAGE_FIELDS, field=prefix)
    if errors or not isinstance(profile, dict):
        return errors

    for field in ("primary_language", "authored_language"):
        if not _nonempty(profile.get(field), min_length=2):
            errors.append(f"{prefix}: '{field}' must be a string of length >= 2")
    for field in (
        "dialect_or_register",
        "code_switch_state",
        "transliteration_state",
        "qualified_review_state",
    ):
        if not _nonempty(profile.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")
    if profile.get("translation_state") not in TRANSLATION_STATES:
        errors.append(f"{prefix}: invalid translation_state")
    normalization = profile.get("terminology_normalization_id")
    if normalization is not None and not isinstance(normalization, str):
        errors.append(f"{prefix}: terminology_normalization_id must be string or null")
    return errors


def validate_tokenizer_evidence_packet(packet: Any) -> list[str]:
    """Validate a future-only tokenizer evidence envelope; no measurements are allowed yet."""
    prefix = "TokenizerEvidencePacket"
    errors = validate_closed_object(
        packet, required_fields=_TOKENIZER_EVIDENCE_FIELDS, field=prefix
    )
    if errors or not isinstance(packet, dict):
        return errors

    for field in ("evidence_id", "candidate_id", "language_profile_id"):
        if not _nonempty(packet.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")

    measurements = packet.get("measurements")
    if not isinstance(measurements, dict):
        errors.append(f"{prefix}: measurements must be an object")
    else:
        expected = set(_TOKENIZER_MEASUREMENTS)
        string_keys = {key for key in measurements if isinstance(key, str)}
        if len(string_keys) != len(measurements):
            errors.append(f"{prefix}: measurements keys must be strings")
        missing = sorted(expected - string_keys)
        extra = sorted(string_keys - expected)
        if missing:
            errors.append(f"{prefix}: measurements missing {missing}")
        if extra:
            errors.append(f"{prefix}: measurements undeclared {extra}")
        for field in sorted(expected & string_keys):
            if measurements[field] != "NEEDS_EVIDENCE":
                errors.append(f"{prefix}: measurements.{field} must equal 'NEEDS_EVIDENCE'")

    if packet.get("execution_performed") is not False:
        errors.append(f"{prefix}: execution_performed must be false")
    if packet.get("recommendation") != "NONE":
        errors.append(f"{prefix}: recommendation must equal 'NONE'")
    return errors


def validate_capability_preservation_binding(binding: Any) -> list[str]:
    prefix = "CapabilityPreservationBinding"
    errors = validate_closed_object(binding, required_fields=_CAPABILITY_FIELDS, field=prefix)
    if errors or not isinstance(binding, dict):
        return errors

    for field in (
        "binding_id",
        "base_checkpoint_binding_id",
        "candidate_checkpoint_id",
        "frozen_evaluation_protocol_id",
        "pre_registered_margins_id",
        "quarantine_verification_id",
    ):
        if not _nonempty(binding.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")

    slices = binding.get("required_slices")
    if not isinstance(slices, list):
        errors.append(f"{prefix}: required_slices must be a list")
    elif any(not isinstance(item, str) for item in slices):
        errors.append(f"{prefix}: required_slices entries must be strings")
    else:
        if len(slices) != len(set(slices)):
            errors.append(f"{prefix}: required_slices must be unique")
        present = set(slices)
        if present != _REQUIRED_SLICES:
            missing = sorted(_REQUIRED_SLICES - present)
            extra = sorted(present - _REQUIRED_SLICES)
            if missing:
                errors.append(f"{prefix}: required_slices missing {missing}")
            if extra:
                errors.append(f"{prefix}: required_slices undeclared {extra}")
    return errors


def validate_abort_sentinel_policy(policy: Any) -> list[str]:
    prefix = "AbortSentinelPolicy"
    errors = validate_closed_object(policy, required_fields=_ABORT_FIELDS, field=prefix)
    if errors or not isinstance(policy, dict):
        return errors

    for field in (
        "policy_id",
        "sentinel_set_id",
        "source_purpose_verification_id",
        "threshold_record_id",
    ):
        if not _nonempty(policy.get(field)):
            errors.append(f"{prefix}: '{field}' must be a non-empty string")

    effects = policy.get("allowed_effects")
    if not isinstance(effects, list) or not effects:
        errors.append(f"{prefix}: allowed_effects must be a non-empty list")
    elif any(not isinstance(item, str) for item in effects):
        errors.append(f"{prefix}: allowed_effects entries must be strings")
    else:
        if len(effects) != len(set(effects)):
            errors.append(f"{prefix}: allowed_effects must be unique")
        unknown = sorted(set(effects) - _ALLOWED_SENTINEL_EFFECTS)
        if unknown:
            errors.append(f"{prefix}: unsupported allowed_effects {unknown}")

    for field in (
        "can_rank_checkpoints",
        "can_tune_recipe",
        "can_change_hyperparameters",
    ):
        if policy.get(field) is not False:
            errors.append(f"{prefix}: {field} must be false")
    if policy.get("frozen_before_run") is not True:
        errors.append(f"{prefix}: frozen_before_run must be true")
    return errors


def evaluate_abort_sentinel_effect(policy: Any, effect: Any) -> dict[str, Any]:
    """Admit only the three frozen sentinel effects; never create optimization signals."""
    errors = validate_abort_sentinel_policy(policy)
    if errors:
        return {
            "allowed": False,
            "reason_code": "INVALID_SENTINEL_POLICY",
            "validation_errors": errors,
        }
    if effect not in _ALLOWED_SENTINEL_EFFECTS or effect not in policy["allowed_effects"]:
        return {
            "allowed": False,
            "reason_code": "EFFECT_NOT_AUTHORIZED",
            "validation_errors": [],
        }
    return {"allowed": True, "reason_code": "AUTHORIZED_SENTINEL_EFFECT", "validation_errors": []}