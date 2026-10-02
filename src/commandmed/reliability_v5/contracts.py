"""Frozen mathematical contracts for the CommandMed V5 intervention study."""

from __future__ import annotations

import math
from dataclasses import dataclass


class ReliabilityContractError(ValueError):
    """Raised when a V5 intervention/assurance contract is malformed."""


@dataclass(frozen=True)
class EffectInterval:
    """Oriented paired effect and confidence interval; positive is better."""

    estimate: float
    lower: float
    upper: float

    def __post_init__(self) -> None:
        values = (float(self.estimate), float(self.lower), float(self.upper))
        if any(not math.isfinite(value) for value in values):
            raise ReliabilityContractError("effect interval: all values must be finite")
        if self.lower > self.upper:
            raise ReliabilityContractError("effect interval: lower cannot exceed upper")
        if not self.lower <= self.estimate <= self.upper:
            raise ReliabilityContractError("effect interval: estimate must lie inside interval")


def classify_effect(interval: EffectInterval, margin: float) -> str:
    """Classify against a frozen symmetric meaningful-effect margin."""
    margin = float(margin)
    if not math.isfinite(margin) or margin <= 0.0:
        raise ReliabilityContractError("margin: expected a finite positive number")
    if interval.lower > margin:
        return "IMPROVE"
    if interval.upper < -margin:
        return "HARM"
    if interval.lower >= -margin and interval.upper <= margin:
        return "EQUIVALENT"
    return "INCONCLUSIVE"


def hard_gate_noninferiority_pass(interval: EffectInterval, margin: float) -> bool:
    """Return true only when the lower bound clears the frozen harm margin."""
    margin = float(margin)
    if not math.isfinite(margin) or margin <= 0.0:
        raise ReliabilityContractError("margin: expected a finite positive number")
    return interval.lower >= -margin


def ordered_interaction(
    *, base: float, intervention_a: float, intervention_b: float, a_after_b: float
) -> float:
    """Compute Gamma[a|b,j] on one oriented assurance metric."""
    values = tuple(float(value) for value in (base, intervention_a, intervention_b, a_after_b))
    if any(not math.isfinite(value) for value in values):
        raise ReliabilityContractError("ordered interaction: all metric values must be finite")
    base_value, a_value, b_value, combined_value = values
    return combined_value - b_value - a_value + base_value


def order_gap(gamma_a_after_b: float, gamma_b_after_a: float) -> float:
    """Compute Kappa[a,b,j] as the difference between ordered interactions."""
    left = float(gamma_a_after_b)
    right = float(gamma_b_after_a)
    if not math.isfinite(left) or not math.isfinite(right):
        raise ReliabilityContractError("order gap: interaction values must be finite")
    return left - right
