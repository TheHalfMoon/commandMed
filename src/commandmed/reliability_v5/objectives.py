"""Pure-math V5 objective primitives; no model loading, optimization, or training."""
from __future__ import annotations

import math
from collections.abc import Sequence

from .contracts import ReliabilityContractError
from .probability import ProbabilityContractError, normalize_probabilities, softmax

_OBJECTIVE_PROBABILITY_FLOOR = 1e-15


def _finite_vector(values: Sequence[float], *, field: str) -> tuple[float, ...]:
    if not values:
        raise ReliabilityContractError(f"{field}: expected non-empty vector")
    try:
        result = tuple(float(value) for value in values)
    except (TypeError, ValueError) as exc:
        raise ReliabilityContractError(f"{field}: values must be finite numbers") from exc
    if any(not math.isfinite(value) for value in result):
        raise ReliabilityContractError(f"{field}: values must be finite numbers")
    return result


def typed_readout_logits(
    hidden: Sequence[float],
    weights: Sequence[Sequence[float]],
    bias: Sequence[float],
) -> tuple[float, ...]:
    """Apply an explicit linear typed-decision readout to one frozen representation."""
    h = _finite_vector(hidden, field="hidden")
    b = _finite_vector(bias, field="bias")
    if len(weights) != len(b):
        raise ReliabilityContractError("weights: row count must equal bias length")
    rows = tuple(_finite_vector(row, field="weights") for row in weights)
    if any(len(row) != len(h) for row in rows):
        raise ReliabilityContractError("weights: every row must match hidden width")
    return tuple(sum(w * x for w, x in zip(row, h)) + offset for row, offset in zip(rows, b))


def typed_readout_probabilities(
    hidden: Sequence[float],
    weights: Sequence[Sequence[float]],
    bias: Sequence[float],
) -> tuple[float, ...]:
    return softmax(typed_readout_logits(hidden, weights, bias))


def _normalized_probabilities(values: Sequence[float], *, field: str) -> tuple[float, ...]:
    try:
        return normalize_probabilities(values)
    except (ProbabilityContractError, TypeError, ValueError) as exc:
        raise ReliabilityContractError(f"{field}: invalid probability vector") from exc


def negative_log_likelihood_for_target(
    probabilities: Sequence[float], target_index: int
) -> float:
    """Return objective NLL with the frozen probability floor used by V5 optimization mechanics."""
    p = _normalized_probabilities(probabilities, field="probabilities")
    if not isinstance(target_index, int) or isinstance(target_index, bool):
        raise ReliabilityContractError("target_index: expected integer")
    if target_index < 0 or target_index >= len(p):
        raise ReliabilityContractError("target_index: out of range")
    return -math.log(max(p[target_index], _OBJECTIVE_PROBABILITY_FLOOR))


def kl_divergence(reference: Sequence[float], candidate: Sequence[float]) -> float:
    """Return the V5 objective KL using the same frozen candidate-probability floor."""
    p = _normalized_probabilities(reference, field="reference")
    q = _normalized_probabilities(candidate, field="candidate")
    if len(p) != len(q):
        raise ReliabilityContractError("kl: probability vectors must have equal length")
    return sum(pi * math.log(pi / max(qi, _OBJECTIVE_PROBABILITY_FLOOR)) for pi, qi in zip(p, q) if pi > 0.0)


def jensen_shannon_divergence(left: Sequence[float], right: Sequence[float]) -> float:
    p = _normalized_probabilities(left, field="left")
    q = _normalized_probabilities(right, field="right")
    if len(p) != len(q):
        raise ReliabilityContractError("js: probability vectors must have equal length")
    midpoint = tuple((pi + qi) / 2.0 for pi, qi in zip(p, q))
    return 0.5 * kl_divergence(p, midpoint) + 0.5 * kl_divergence(q, midpoint)


def _nonnegative_scalar(value: float, *, field: str) -> float:
    try:
        result = float(value)
    except (TypeError, ValueError) as exc:
        raise ReliabilityContractError(f"{field}: expected finite non-negative number") from exc
    if not math.isfinite(result) or result < 0.0:
        raise ReliabilityContractError(f"{field}: expected finite non-negative number")
    return result


def contract_consistency_penalty(
    original: Sequence[float], transformed: Sequence[float]
) -> float:
    """Symmetric distribution shift penalty for meaning-preserving transformations."""
    return jensen_shannon_divergence(original, transformed)


def capability_retention_penalty(
    reference: Sequence[float], candidate: Sequence[float]
) -> float:
    """Directional KL penalty anchoring candidate behavior to a frozen reference."""
    return kl_divergence(reference, candidate)


def contract_regularized_objective(
    *,
    task_loss: float,
    original: Sequence[float],
    transformed: Sequence[float],
    contract_weight: float,
) -> float:
    """Pure C1 objective: task loss plus frozen semantic-contract penalty."""
    base = _nonnegative_scalar(task_loss, field="task_loss")
    weight = _nonnegative_scalar(contract_weight, field="contract_weight")
    return base + weight * contract_consistency_penalty(original, transformed)


def retention_regularized_objective(
    *,
    task_loss: float,
    original: Sequence[float],
    transformed: Sequence[float],
    contract_weight: float,
    retention_reference: Sequence[float],
    retention_candidate: Sequence[float],
    retention_weight: float,
) -> float:
    """Pure C2 objective: C1 plus a frozen capability-retention anchor."""
    total = contract_regularized_objective(
        task_loss=task_loss,
        original=original,
        transformed=transformed,
        contract_weight=contract_weight,
    )
    weight = _nonnegative_scalar(retention_weight, field="retention_weight")
    return total + weight * capability_retention_penalty(
        retention_reference, retention_candidate
    )
