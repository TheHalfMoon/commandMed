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
from collections.abc import Collection, Mapping, Sequence

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


def deterministic_state_indices(
    calculator_id: str,
    total: int,
    *,
    count: int,
    salt: str,
    exclude_state_indices: Collection[int] = (),
) -> tuple[int, ...]:
    """Select unique state indices with a full-cycle deterministic walk."""
    if not isinstance(calculator_id, str) or not calculator_id.strip():
        raise ReliabilityContractError("calculator_id: expected a non-empty string")
    if not isinstance(total, int) or isinstance(total, bool) or total <= 0:
        raise ReliabilityContractError("total: expected a positive integer")
    if not isinstance(count, int) or isinstance(count, bool) or count <= 0:
        raise ReliabilityContractError("count: expected a positive integer")
    if not isinstance(salt, str) or not salt:
        raise ReliabilityContractError("salt: expected a non-empty string")

    raw_excluded = tuple(exclude_state_indices)
    if any(not isinstance(index, int) or isinstance(index, bool) for index in raw_excluded):
        raise ReliabilityContractError("exclude_state_indices: expected integers")
    if len(set(raw_excluded)) != len(raw_excluded):
        raise ReliabilityContractError("exclude_state_indices: duplicates are not allowed")
    excluded = set(raw_excluded)
    if any(index < 0 or index >= total for index in excluded):
        raise ReliabilityContractError("exclude_state_indices: index outside case space")
    if total - len(excluded) < count:
        raise ReliabilityContractError("case space after exclusions is smaller than requested count")

    digest = hashlib.sha256(f"{calculator_id}|{salt}".encode("utf-8")).digest()
    offset = int.from_bytes(digest[:8], "big") % total
    stride = _coprime_stride(int.from_bytes(digest[8:16], "big"), total)
    selected: list[int] = []
    for position in range(total):
        state_index = (offset + position * stride) % total
        if state_index in excluded:
            continue
        selected.append(state_index)
        if len(selected) == count:
            return tuple(selected)
    raise ReliabilityContractError("unable to select requested disjoint state indices")

def cases_from_state_indices(
    calculator_id: str,
    domains: Mapping[str, Sequence[object]],
    state_indices: Sequence[int],
) -> tuple[dict[str, object], ...]:
    """Materialize intrinsic case identities from already selected state indices."""
    normalized = expanded_domains(domains)
    total = math.prod(len(values) for _, values in normalized)
    raw_indices = tuple(state_indices)
    if any(not isinstance(index, int) or isinstance(index, bool) for index in raw_indices):
        raise ReliabilityContractError("state_indices: expected integers")
    if len(set(raw_indices)) != len(raw_indices):
        raise ReliabilityContractError("state_indices: duplicates are not allowed")

    cases: list[dict[str, object]] = []
    for state_index in raw_indices:
        if state_index < 0 or state_index >= total:
            raise ReliabilityContractError("state_indices: index outside case space")
        inputs = _state_from_index(normalized, state_index)
        canonical = json.dumps(inputs, sort_keys=True, separators=(",", ":"), ensure_ascii=True)
        case_id = hashlib.sha256(
            f"{calculator_id}|{state_index}|{canonical}".encode("utf-8")
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

def deterministic_cases(
    calculator_id: str,
    domains: Mapping[str, Sequence[object]],
    *,
    count: int = DEFAULT_CASE_COUNT,
    salt: str = "CommandMed-V5-RULE-ORACLE-CASES",
    exclude_state_indices: Collection[int] = (),
) -> tuple[dict[str, object], ...]:
    """Generate selected cases while keeping identity independent of selection salt."""
    total = case_space_size(domains)
    state_indices = deterministic_state_indices(
        calculator_id,
        total,
        count=count,
        salt=salt,
        exclude_state_indices=exclude_state_indices,
    )
    return cases_from_state_indices(calculator_id, domains, state_indices)
