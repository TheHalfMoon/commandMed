"""Statistical mechanics for the preregistered V5 paired analysis.

These helpers implement analysis contracts only. They do not select margins,
access confirmatory data, or promote any empirical claim.
"""
from __future__ import annotations

import math
import random
from statistics import NormalDist, fmean
from typing import Iterable, Sequence

from .contracts import EffectInterval


class StatisticsContractError(ValueError):
    """Raised when a V5 statistical contract is malformed."""


def _finite_values(values: Iterable[float], name: str) -> tuple[float, ...]:
    result = tuple(float(value) for value in values)
    if not result:
        raise StatisticsContractError(f"{name} must be non-empty")
    if any(not math.isfinite(value) for value in result):
        raise StatisticsContractError(f"{name} must contain only finite values")
    return result


def paired_mean_effect(
    baseline: Sequence[float], intervention: Sequence[float]
) -> float:
    """Return mean(intervention - baseline) for paired source clusters."""
    base = _finite_values(baseline, "baseline")
    treated = _finite_values(intervention, "intervention")
    if len(base) != len(treated):
        raise StatisticsContractError("paired vectors must have equal length")
    return fmean(treated[i] - base[i] for i in range(len(base)))


def _quantile(sorted_values: Sequence[float], probability: float) -> float:
    if not 0.0 <= probability <= 1.0:
        raise StatisticsContractError("quantile probability must be in [0, 1]")
    if len(sorted_values) == 1:
        return float(sorted_values[0])
    position = probability * (len(sorted_values) - 1)
    lower = math.floor(position)
    upper = math.ceil(position)
    if lower == upper:
        return float(sorted_values[lower])
    weight = position - lower
    return float(sorted_values[lower] * (1.0 - weight) + sorted_values[upper] * weight)


def paired_cluster_bootstrap_effect(
    baseline: Sequence[float],
    intervention: Sequence[float],
    *,
    resamples: int,
    seed: int,
    confidence: float = 0.95,
) -> EffectInterval:
    """Percentile CI with source-cluster-preserving paired resampling."""
    base = _finite_values(baseline, "baseline")
    treated = _finite_values(intervention, "intervention")
    if len(base) != len(treated):
        raise StatisticsContractError("paired vectors must have equal length")
    if resamples < 100:
        raise StatisticsContractError("resamples must be at least 100")
    if not 0.5 < confidence < 1.0:
        raise StatisticsContractError("confidence must be between 0.5 and 1")
    differences = tuple(treated[i] - base[i] for i in range(len(base)))
    rng = random.Random(seed)
    n = len(differences)
    draws = []
    for _ in range(resamples):
        draws.append(fmean(differences[rng.randrange(n)] for _ in range(n)))
    draws.sort()
    alpha = 1.0 - confidence
    point = fmean(differences)
    lower = _quantile(draws, alpha / 2.0)
    upper = _quantile(draws, 1.0 - alpha / 2.0)
    # The shared EffectInterval contract requires the point estimate inside the
    # interval. Percentile bootstrap intervals can exclude it under finite-sample
    # bias, so conservatively widen to include the observed paired estimate.
    return EffectInterval(
        estimate=point,
        lower=min(lower, point),
        upper=max(upper, point),
    )


def holm_adjusted_p_values(p_values: Sequence[float]) -> tuple[float, ...]:
    """Return Holm family-wise adjusted p-values in original order."""
    values = _finite_values(p_values, "p_values")
    if any(value < 0.0 or value > 1.0 for value in values):
        raise StatisticsContractError("p-values must be in [0, 1]")
    ordered = sorted(range(len(values)), key=lambda index: values[index])
    adjusted = [0.0] * len(values)
    running = 0.0
    m = len(values)
    for rank, index in enumerate(ordered):
        candidate = min(1.0, (m - rank) * values[index])
        running = max(running, candidate)
        adjusted[index] = running
    return tuple(adjusted)


def normal_approx_paired_mde(
    paired_sd: float,
    clusters: int,
    *,
    alpha: float = 0.05,
    power: float = 0.90,
) -> float:
    """Two-sided normal-approximation MDE for planning, not final inference."""
    if not math.isfinite(paired_sd) or paired_sd <= 0.0:
        raise StatisticsContractError("paired_sd must be finite and positive")
    if clusters < 2:
        raise StatisticsContractError("clusters must be at least 2")
    if not 0.0 < alpha < 1.0:
        raise StatisticsContractError("alpha must be in (0, 1)")
    if not 0.5 < power < 1.0:
        raise StatisticsContractError("power must be between 0.5 and 1")
    normal = NormalDist()
    z_alpha = normal.inv_cdf(1.0 - alpha / 2.0)
    z_power = normal.inv_cdf(power)
    return (z_alpha + z_power) * paired_sd / math.sqrt(clusters)


def normal_approx_required_clusters(
    paired_sd: float,
    effect: float,
    *,
    alpha: float = 0.05,
    power: float = 0.90,
) -> int:
    """Approximate paired-cluster count for a prespecified nonzero effect."""
    if not math.isfinite(effect) or effect <= 0.0:
        raise StatisticsContractError("effect must be finite and positive")
    if not math.isfinite(paired_sd) or paired_sd <= 0.0:
        raise StatisticsContractError("paired_sd must be finite and positive")
    if not 0.0 < alpha < 1.0:
        raise StatisticsContractError("alpha must be in (0, 1)")
    if not 0.5 < power < 1.0:
        raise StatisticsContractError("power must be between 0.5 and 1")
    normal = NormalDist()
    z_sum = normal.inv_cdf(1.0 - alpha / 2.0) + normal.inv_cdf(power)
    return max(2, math.ceil(((z_sum * paired_sd) / effect) ** 2))
