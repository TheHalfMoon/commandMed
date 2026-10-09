"""Fixed downstream policy controls for CommandMed V5."""

from __future__ import annotations

import math
from collections.abc import Iterable, Sequence
from dataclasses import dataclass

from .probability import ProbabilityContractError, normalize_probabilities


@dataclass(frozen=True)
class SelectiveDecision:
    """Deterministic action produced under a frozen confidence threshold."""

    action: str
    semantic_index: int | None
    confidence: float
    deferred: bool


def fixed_defer_policy(
    probabilities: Iterable[float],
    threshold: float,
    *,
    action_labels: Sequence[str] | None = None,
    defer_label: str = "DEFER",
) -> SelectiveDecision:
    """Apply a fixed max-probability act/defer policy without threshold refitting."""
    vector = normalize_probabilities(probabilities)
    try:
        threshold = float(threshold)
    except (TypeError, ValueError) as exc:
        raise ProbabilityContractError("threshold: expected a number in [0, 1]") from exc
    if not math.isfinite(threshold) or not 0.0 <= threshold <= 1.0:
        raise ProbabilityContractError("threshold: expected a finite number in [0, 1]")
    if not isinstance(defer_label, str) or not defer_label.strip():
        raise ProbabilityContractError("defer_label: expected a non-empty string")
    if action_labels is None:
        labels = tuple(str(index) for index in range(len(vector)))
    else:
        labels = tuple(action_labels)
        if len(labels) != len(vector):
            raise ProbabilityContractError("action_labels: length must match candidate count")
        if any(not isinstance(label, str) or not label.strip() for label in labels):
            raise ProbabilityContractError("action_labels: every label must be a non-empty string")
        if len(set(labels)) != len(labels):
            raise ProbabilityContractError("action_labels: labels must be unique")
    if defer_label in labels:
        raise ProbabilityContractError("defer_label: must not collide with an action label")

    confidence = max(vector)
    semantic_index = vector.index(confidence)  # frozen tie rule: lowest semantic index wins.
    if confidence < threshold:
        return SelectiveDecision(
            action=defer_label,
            semantic_index=None,
            confidence=confidence,
            deferred=True,
        )
    return SelectiveDecision(
        action=labels[semantic_index],
        semantic_index=semantic_index,
        confidence=confidence,
        deferred=False,
    )
