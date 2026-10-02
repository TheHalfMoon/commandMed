"""Selection-bias controls for CommandMed V5.

The implementation is project-owned and derived from the published option-ID
prior concept. It intentionally does not vendor upstream research code.

Permutation convention: ``permutation[display_index] == semantic_index``.
"""

from __future__ import annotations

import math
from collections.abc import Iterable, Sequence

from .probability import ProbabilityContractError, normalize_probabilities, softmax

_EPSILON = 1e-12


def _validate_permutation(permutation: Sequence[int], size: int) -> tuple[int, ...]:
    if isinstance(permutation, (str, bytes)):
        raise ProbabilityContractError("permutation: expected integer indices")
    result = tuple(permutation)
    if len(result) != size:
        raise ProbabilityContractError("permutation: length must match candidate count")
    if any(not isinstance(value, int) or isinstance(value, bool) for value in result):
        raise ProbabilityContractError("permutation: every entry must be an integer")
    if set(result) != set(range(size)):
        raise ProbabilityContractError("permutation: expected a bijection over candidate indices")
    return result


def align_display_to_semantic(
    probabilities: Iterable[float], permutation: Sequence[int]
) -> tuple[float, ...]:
    """Map a displayed-slot distribution back to canonical semantic order."""
    display = normalize_probabilities(probabilities)
    mapping = _validate_permutation(permutation, len(display))
    semantic = [0.0] * len(display)
    for display_index, semantic_index in enumerate(mapping):
        semantic[semantic_index] = display[display_index]
    return tuple(semantic)


def mean_semantic_distribution(
    probability_rows: Iterable[Iterable[float]],
    permutations: Iterable[Sequence[int]],
) -> tuple[float, ...]:
    """Average permutation-aligned distributions in semantic candidate space."""
    rows = tuple(tuple(row) for row in probability_rows)
    maps = tuple(tuple(mapping) for mapping in permutations)
    if not rows or len(rows) != len(maps):
        raise ProbabilityContractError(
            "permutation rows: expected equal non-zero probability/permutation counts"
        )
    aligned = tuple(
        align_display_to_semantic(row, mapping) for row, mapping in zip(rows, maps)
    )
    size = len(aligned[0])
    if any(len(row) != size for row in aligned):
        raise ProbabilityContractError("permutation rows: inconsistent candidate counts")
    return normalize_probabilities(
        math.fsum(row[index] for row in aligned) / len(aligned)
        for index in range(size)
    )


def estimate_display_slot_prior(
    probability_rows: Iterable[Iterable[float]], *, epsilon: float = _EPSILON
) -> tuple[float, ...]:
    """Estimate a geometric-mean option-slot prior from displayed distributions."""
    rows = tuple(normalize_probabilities(row) for row in probability_rows)
    if not rows:
        raise ProbabilityContractError("prior rows: expected at least one probability vector")
    size = len(rows[0])
    if any(len(row) != size for row in rows):
        raise ProbabilityContractError("prior rows: inconsistent candidate counts")
    if not math.isfinite(epsilon) or epsilon <= 0.0:
        raise ProbabilityContractError("epsilon: expected a finite positive number")
    log_prior = tuple(
        math.fsum(math.log(row[index] + epsilon) for row in rows) / len(rows)
        for index in range(size)
    )
    return softmax(log_prior)


def debias_display_distribution(
    probabilities: Iterable[float],
    prior: Iterable[float],
    *,
    epsilon: float = _EPSILON,
) -> tuple[float, ...]:
    """Remove a frozen displayed-slot prior in log space and renormalize."""
    observed = normalize_probabilities(probabilities)
    prior_vector = normalize_probabilities(prior)
    if len(observed) != len(prior_vector):
        raise ProbabilityContractError("prior: candidate count must match probabilities")
    if not math.isfinite(epsilon) or epsilon <= 0.0:
        raise ProbabilityContractError("epsilon: expected a finite positive number")
    corrected_logits = tuple(
        math.log(probability + epsilon) - math.log(prior_probability + epsilon)
        for probability, prior_probability in zip(observed, prior_vector)
    )
    return softmax(corrected_logits)


def debias_and_align(
    probabilities: Iterable[float],
    prior: Iterable[float],
    permutation: Sequence[int],
) -> tuple[float, ...]:
    """Debias displayed option slots, then return canonical semantic probabilities."""
    corrected = debias_display_distribution(probabilities, prior)
    return align_display_to_semantic(corrected, permutation)
