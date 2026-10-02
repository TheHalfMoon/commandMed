"""Deterministic candidate-state generator for V5 rule-oracle fixtures.

The generator operates only on statically extracted Boolean/numeric threshold
metadata. It does not execute clinical calculator code and does not assert that
a generated value is clinically admissible; final domain bounds remain a
separate admission gate.
"""

from __future__ import annotations

import hashlib
import json
import math
from collections.abc import Mapping, Sequence

from .contracts import ReliabilityContractError

DEFAULT_CASE_COUNT = 64


def _expanded_values(values: Sequence[object]) -> tuple[object, ...]:
    if not values:
        raise ReliabilityContractError("domain constants: each field needs at least one value")
    if all(isinstance(value, bool) for value in values):
        return (False, True)
    numeric: list[float] = []
    for value in values:
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ReliabilityContractError("domain constants: only Boolean/numeric values are allowed")
        numeric_value = float(value)
        if not math.isfinite(numeric_value):
            raise ReliabilityContractError("domain constants: numeric values must be finite")
        numeric.append(numeric_value)
    expanded: set[float] = set()
    for threshold in numeric:
        near = max(1.0, abs(threshold) * 0.01)
        far = max(5.0, abs(threshold) * 0.10)
        expanded.update((threshold - far, threshold - near, threshold, threshold + near, threshold + far))
    return tuple(sorted(expanded))


def expanded_domains(
    domains: Mapping[str, Sequence[object]],
) -> tuple[tuple[str, tuple[object, ...]], ...]:
    """Normalize field order and expand threshold anchors without executing a rule."""
    if not isinstance(domains, Mapping) or not domains:
        raise ReliabilityContractError("domains: expected a non-empty mapping")
    result: list[tuple[str, tuple[object, ...]]] = []
    for name in sorted(domains):
        if not isinstance(name, str) or not name.strip():
            raise ReliabilityContractError("domains: field names must be non-empty strings")
        result.append((name, _expanded_values(tuple(domains[name]))))
    return tuple(result)


def case_space_size(domains: Mapping[str, Sequence[object]]) -> int:
    """Return the exact Cartesian size of the prospective static input space."""
    total = 1
    for _, values in expanded_domains(domains):
        total *= len(values)
    return total


def _coprime_stride(seed: int, modulus: int) -> int:
    if modulus <= 1:
        return 1
    stride = (seed % (modulus - 1)) + 1
    while math.gcd(stride, modulus) != 1:
        stride = (stride % (modulus - 1)) + 1
    return stride


def _state_from_index(
    normalized: tuple[tuple[str, tuple[object, ...]], ...], index: int
) -> dict[str, object]:
    state: dict[str, object] = {}
    remainder = index
    for name, values in reversed(normalized):
        remainder, digit = divmod(remainder, len(values))
        state[name] = values[digit]
    return {name: state[name] for name, _ in normalized}


def deterministic_cases(
    calculator_id: str,
    domains: Mapping[str, Sequence[object]],
    *,
    count: int = DEFAULT_CASE_COUNT,
    salt: str = "CommandMed-V5-RULE-ORACLE-CASES",
) -> tuple[dict[str, object], ...]:
    """Generate unique deterministic candidate states using a full-cycle index walk."""
    if not isinstance(calculator_id, str) or not calculator_id.strip():
        raise ReliabilityContractError("calculator_id: expected a non-empty string")
    if not isinstance(count, int) or isinstance(count, bool) or count <= 0:
        raise ReliabilityContractError("count: expected a positive integer")
    if not isinstance(salt, str) or not salt:
        raise ReliabilityContractError("salt: expected a non-empty string")

    normalized = expanded_domains(domains)
    total = math.prod(len(values) for _, values in normalized)
    if total < count:
        raise ReliabilityContractError(
            f"domains: case space {total} is smaller than requested count {count}"
        )

    digest = hashlib.sha256(f"{calculator_id}|{salt}".encode("utf-8")).digest()
    offset = int.from_bytes(digest[:8], "big") % total
    stride = _coprime_stride(int.from_bytes(digest[8:16], "big"), total)

    cases: list[dict[str, object]] = []
    for position in range(count):
        state_index = (offset + position * stride) % total
        inputs = _state_from_index(normalized, state_index)
        canonical = json.dumps(inputs, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
        case_id = hashlib.sha256(
            f"{calculator_id}|{state_index}|{canonical}|{salt}".encode("utf-8")
        ).hexdigest()
        cases.append(
            {
                "case_id": case_id,
                "calculator_id": calculator_id,
                "state_index": state_index,
                "inputs": inputs,
            }
        )
    return tuple(cases)

