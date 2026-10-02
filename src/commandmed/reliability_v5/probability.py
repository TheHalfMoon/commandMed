"""Pure probability utilities for the CommandMed V5 reliability study.

This module has no model, network, dataset, or accelerator dependency. It exists
so intervention behavior can be qualified mechanically before any model
execution is authorized.
"""

from __future__ import annotations

import math
from collections.abc import Iterable


class ProbabilityContractError(ValueError):
    """Raised when a probability/logit input violates the frozen contract."""


def _finite_vector(values: Iterable[float], *, field: str) -> tuple[float, ...]:
    if isinstance(values, (str, bytes)):
        raise ProbabilityContractError(f"{field}: expected a numeric iterable")
    vector = tuple(float(value) for value in values)
    if not vector:
        raise ProbabilityContractError(f"{field}: expected at least one value")
    if any(not math.isfinite(value) for value in vector):
        raise ProbabilityContractError(f"{field}: all values must be finite")
    return vector


def normalize_probabilities(values: Iterable[float]) -> tuple[float, ...]:
    """Return a normalized non-negative probability vector."""
    vector = _finite_vector(values, field="probabilities")
    if any(value < 0.0 for value in vector):
        raise ProbabilityContractError("probabilities: negative values are invalid")
    total = math.fsum(vector)
    if total <= 0.0:
        raise ProbabilityContractError("probabilities: total mass must be positive")
    return tuple(value / total for value in vector)


def softmax(logits: Iterable[float]) -> tuple[float, ...]:
    """Compute a numerically stable softmax over finite logits."""
    vector = _finite_vector(logits, field="logits")
    maximum = max(vector)
    exponentials = tuple(math.exp(value - maximum) for value in vector)
    total = math.fsum(exponentials)
    return tuple(value / total for value in exponentials)


def temperature_scale_logits(
    logits: Iterable[float], temperature: float
) -> tuple[float, ...]:
    """Apply frozen scalar temperature scaling and return probabilities."""
    try:
        temperature = float(temperature)
    except (TypeError, ValueError) as exc:
        raise ProbabilityContractError("temperature: expected a finite positive number") from exc
    if not math.isfinite(temperature) or temperature <= 0.0:
        raise ProbabilityContractError("temperature: expected a finite positive number")
    vector = _finite_vector(logits, field="logits")
    return softmax(value / temperature for value in vector)


def negative_log_likelihood(probabilities: Iterable[float], target: int) -> float:
    """Return single-item multiclass NLL using normalized probabilities."""
    vector = normalize_probabilities(probabilities)
    if not isinstance(target, int) or isinstance(target, bool) or not 0 <= target < len(vector):
        raise ProbabilityContractError("target: expected an in-range integer index")
    probability = vector[target]
    return math.inf if probability <= 0.0 else -math.log(probability)


def multiclass_brier(probabilities: Iterable[float], target: int) -> float:
    """Return the multiclass Brier score for one item."""
    vector = normalize_probabilities(probabilities)
    if not isinstance(target, int) or isinstance(target, bool) or not 0 <= target < len(vector):
        raise ProbabilityContractError("target: expected an in-range integer index")
    return math.fsum(
        (probability - (1.0 if index == target else 0.0)) ** 2
        for index, probability in enumerate(vector)
    )
