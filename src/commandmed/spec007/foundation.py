"""Minimal offline foundation for Spec 007 record validation.

This module owns only Spec 007-specific closed vocabulary and strict JSON/field
validation helpers. Canonical serialization and identity remain owned by
``eval_contract.canonical`` and are reused unchanged by the package API.
"""

from __future__ import annotations

import json
import re
from typing import Any, Iterable

ROLE_CLASSES = frozenset(
    {
        "PATIENT_CAREGIVER",
        "CLINICAL_PROFESSIONAL",
        "LEARNER_RESEARCHER",
    }
)

_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")


class _DuplicateJsonKeyError(ValueError):
    """Internal signal for deterministic duplicate-key rejection."""


def _unique_object_pairs(pairs: list[tuple[str, Any]]) -> dict[str, Any]:
    result: dict[str, Any] = {}
    for key, value in pairs:
        if key in result:
            raise _DuplicateJsonKeyError(key)
        result[key] = value
    return result


def parse_json_object(
    raw_text: Any, *, field: str = "record"
) -> tuple[dict[str, Any] | None, list[str]]:
    """Parse one JSON object without coercion and reject duplicate object keys."""
    if not isinstance(raw_text, str):
        return None, [f"{field}: expected JSON text string"]

    try:
        parsed = json.loads(raw_text, object_pairs_hook=_unique_object_pairs)
    except _DuplicateJsonKeyError as exc:
        return None, [f"{field}: duplicate JSON object key '{exc.args[0]}'"]
    except (json.JSONDecodeError, ValueError):
        return None, [f"{field}: malformed JSON"]

    if not isinstance(parsed, dict):
        return None, [f"{field}: expected JSON object"]
    return parsed, []


def validate_closed_object(
    record: Any,
    *,
    required_fields: Iterable[str],
    optional_fields: Iterable[str] = (),
    field: str = "record",
) -> list[str]:
    """Reject non-objects, missing required keys, and every undeclared key."""
    if not isinstance(record, dict):
        return [f"{field}: expected object record"]

    required = set(required_fields)
    declared = required | set(optional_fields)
    present = set(record)

    errors: list[str] = []
    missing = sorted(required - present)
    if missing:
        errors.append(f"{field}: required fields missing {missing}")

    undeclared = sorted(present - declared)
    if undeclared:
        errors.append(f"{field}: undeclared fields {undeclared}")
    return errors


def is_canonical_sha256(value: Any) -> bool:
    """Return true only for a lowercase 64-character SHA-256 hex string."""
    return isinstance(value, str) and _SHA256_RE.fullmatch(value) is not None


def validate_canonical_sha256(value: Any, field: str) -> list[str]:
    """Validate a lowercase SHA-256 identity without coercion."""
    if is_canonical_sha256(value):
        return []
    return [f"{field}: expected lowercase sha256 hex"]


def validate_role_class(value: Any, field: str = "role_class") -> list[str]:
    """Validate the frozen Spec 007 three-role training vocabulary."""
    if not isinstance(value, str):
        return [f"{field}: expected role-class string"]
    if value not in ROLE_CLASSES:
        return [f"{field}: unsupported value '{value}'"]
    return []
