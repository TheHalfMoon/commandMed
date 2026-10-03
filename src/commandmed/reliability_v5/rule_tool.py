"""Deterministic rule-tool routing primitive for V5.

This module defines the mechanical D2 interface. It does not authorize or
execute any clinical calculator unless a caller explicitly supplies a callable.
"""
from __future__ import annotations

import hashlib
import json
import math
import re
from collections.abc import Callable, Mapping
from dataclasses import dataclass
from typing import Any

from .contracts import ReliabilityContractError

_SHA256 = re.compile(r"^[0-9a-f]{64}$")


@dataclass(frozen=True)
class RuleToolResult:
    tool_id: str
    calculator_sha256: str
    input_sha256: str
    output_sha256: str
    raw_output: Any
    action: str


def _canonical_sha256(value: Any) -> str:
    payload = json.dumps(
        value,
        sort_keys=True,
        separators=(",", ":"),
        ensure_ascii=True,
        allow_nan=False,
    ).encode("utf-8")
    return hashlib.sha256(payload).hexdigest()


def _validate_inputs(inputs: Mapping[str, object]) -> dict[str, object]:
    if not isinstance(inputs, Mapping) or not inputs:
        raise ReliabilityContractError("inputs: expected a non-empty mapping")
    normalized: dict[str, object] = {}
    for key in sorted(inputs):
        if not isinstance(key, str) or not key.strip():
            raise ReliabilityContractError("inputs: keys must be non-empty strings")
        value = inputs[key]
        if isinstance(value, bool):
            normalized[key] = value
        elif isinstance(value, (int, float)):
            numeric = float(value)
            if not math.isfinite(numeric):
                raise ReliabilityContractError("inputs: numeric values must be finite")
            normalized[key] = value
        else:
            raise ReliabilityContractError("inputs: only Boolean/numeric values are admitted")
    return normalized


def execute_rule_tool(
    *,
    tool_id: str,
    calculator_sha256: str,
    inputs: Mapping[str, object],
    calculator: Callable[..., Any],
    action_mapper: Callable[[Any], str],
) -> RuleToolResult:
    """Execute a caller-supplied deterministic rule and bind input/output identities."""
    if not isinstance(tool_id, str) or not tool_id.strip():
        raise ReliabilityContractError("tool_id: expected a non-empty string")
    if not isinstance(calculator_sha256, str) or _SHA256.fullmatch(calculator_sha256) is None:
        raise ReliabilityContractError("calculator_sha256: expected lowercase sha256 hex")
    if not callable(calculator) or not callable(action_mapper):
        raise ReliabilityContractError("calculator/action_mapper: expected callables")

    normalized = _validate_inputs(inputs)
    raw_output = calculator(**normalized)
    action = action_mapper(raw_output)
    if not isinstance(action, str) or not action.strip():
        raise ReliabilityContractError("action_mapper: expected a non-empty string action")

    return RuleToolResult(
        tool_id=tool_id,
        calculator_sha256=calculator_sha256,
        input_sha256=_canonical_sha256(normalized),
        output_sha256=_canonical_sha256(raw_output),
        raw_output=raw_output,
        action=action,
    )
