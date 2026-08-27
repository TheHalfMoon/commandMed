"""Purpose-aware binding to the canonical Spec 001 quarantine matrix."""

from __future__ import annotations

from pathlib import Path
from typing import Any

from src.commandmed.eval_contract.canonical import compute_canonical_sha256
from src.commandmed.eval_contract.validate import validate_quarantine_rules
from src.commandmed.spec007.foundation import (
    parse_json_object,
    validate_canonical_sha256,
    validate_closed_object,
)

_QUARANTINE_FILE = Path(__file__).resolve().parents[3] / "data" / "eval" / "quarantine.json"
_BINDING_FIELDS = (
    "binding_id",
    "quarantine_matrix_sha256",
    "purpose",
    "source_id",
    "allowed",
    "can_train",
    "can_select_model",
)


def _load_canonical_quarantine() -> dict[str, Any]:
    try:
        raw = _QUARANTINE_FILE.read_text(encoding="utf-8")
    except OSError as exc:
        raise ValueError(f"canonical quarantine matrix unavailable: {exc}") from exc

    parsed, errors = parse_json_object(raw, field="canonical_quarantine")
    if errors or parsed is None:
        raise ValueError("; ".join(errors or ["canonical quarantine parse failed"]))
    if set(parsed) != {"contamination_records", "quarantine_rules"}:
        raise ValueError("canonical quarantine object has unexpected fields")

    rules = parsed.get("quarantine_rules")
    if not isinstance(rules, list):
        raise ValueError("canonical quarantine rules must be a list")
    is_valid, validation_errors = validate_quarantine_rules(rules)
    if not is_valid:
        raise ValueError(
            "canonical quarantine rules invalid: " + "; ".join(validation_errors)
        )
    return parsed


def canonical_quarantine_matrix_sha256() -> str:
    """Return canonical identity of the authoritative purpose/source rule matrix."""
    parsed = _load_canonical_quarantine()
    return compute_canonical_sha256({"quarantine_rules": parsed["quarantine_rules"]})


def evaluate_quarantine_source(source_id: Any, purpose: Any) -> dict[str, Any]:
    """Evaluate one source/purpose pair against the canonical matrix, fail closed."""
    digest = canonical_quarantine_matrix_sha256()
    base = {
        "quarantine_matrix_sha256": digest,
        "purpose": purpose,
        "source_id": source_id,
        "allowed": False,
        "can_train": False,
        "can_select_model": False,
    }
    if not isinstance(purpose, str):
        return {**base, "reason_code": "UNKNOWN_PURPOSE"}
    if not isinstance(source_id, str) or not source_id:
        return {**base, "reason_code": "INVALID_SOURCE_ID"}

    rules = _load_canonical_quarantine()["quarantine_rules"]
    rule = next(
        (item for item in rules if isinstance(item, dict) and item.get("purpose") == purpose),
        None,
    )
    if rule is None:
        return {**base, "reason_code": "UNKNOWN_PURPOSE"}

    allowed_sources = rule.get("allowed_sources", [])
    prohibited_sources = rule.get("prohibited_sources", [])
    if source_id in prohibited_sources:
        return {**base, "reason_code": "PROHIBITED_SOURCE"}
    if source_id not in allowed_sources:
        return {**base, "reason_code": "SOURCE_NOT_AUTHORIZED"}

    return {
        **base,
        "allowed": True,
        "can_train": bool(rule.get("can_train")),
        "can_select_model": bool(rule.get("can_select_model")),
        "reason_code": "ALLOWED_SOURCE",
    }


def validate_quarantine_binding(binding: Any) -> list[str]:
    """Require an exact identity- and decision-bound canonical quarantine result."""
    prefix = "QuarantineBinding"
    errors = validate_closed_object(
        binding,
        required_fields=_BINDING_FIELDS,
        field=prefix,
    )
    if errors or not isinstance(binding, dict):
        return errors

    for field in ("binding_id", "purpose", "source_id"):
        value = binding.get(field)
        if not isinstance(value, str) or not value.strip():
            errors.append(f"{prefix}: '{field}' must be a non-empty string")
    errors.extend(
        validate_canonical_sha256(
            binding.get("quarantine_matrix_sha256"), "quarantine_matrix_sha256"
        )
    )
    for field in ("allowed", "can_train", "can_select_model"):
        if type(binding.get(field)) is not bool:
            errors.append(f"{prefix}: '{field}' must be boolean")

    if errors:
        return errors

    expected_digest = canonical_quarantine_matrix_sha256()
    if binding["quarantine_matrix_sha256"] != expected_digest:
        errors.append(f"{prefix}: quarantine_matrix_sha256 mismatch")

    decision = evaluate_quarantine_source(binding["source_id"], binding["purpose"])
    for field in ("allowed", "can_train", "can_select_model"):
        if binding[field] != decision[field]:
            errors.append(f"{prefix}: '{field}' does not match canonical decision")
    return errors
