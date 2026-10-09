"""Parameter-explicit calibration and selective-control diagnostics for V5.

These helpers deliberately do not choose a calibration definition, binning
scheme, confidence score, abstention threshold, risk target, or AURC convention.
Callers must supply those prospectively frozen choices. This module provides
mechanics only and does not access model outputs or confirmatory data.
"""
from __future__ import annotations

import math
from dataclasses import dataclass
from typing import Iterable, Sequence


class DiagnosticContractError(ValueError):
    """Raised when calibration/selective diagnostic inputs are malformed."""


@dataclass(frozen=True)
class ReliabilityBin:
    lower: float
    upper: float
    count: int
    mean_confidence: float
    event_rate: float
    absolute_gap: float


@dataclass(frozen=True)
class SelectivePoint:
    threshold: float
    coverage: float
    risk: float | None
    accepted: int
    total: int


def _finite(values: Iterable[float], field: str) -> tuple[float, ...]:
    result = tuple(float(value) for value in values)
    if not result:
        raise DiagnosticContractError(f"{field}: expected a non-empty sequence")
    if any(not math.isfinite(value) for value in result):
        raise DiagnosticContractError(f"{field}: all values must be finite")
    return result


def reliability_bins(
    confidences: Sequence[float],
    outcomes: Sequence[int | bool],
    *,
    bin_edges: Sequence[float],
) -> tuple[ReliabilityBin, ...]:
    """Bin caller-defined confidence/outcome pairs using explicit edges.

    Outcomes must be binary event indicators. Bins are left-closed and
    right-open except the final bin, which is closed on both ends. Empty bins
    are retained with zero-valued summaries and count zero so the caller can
    preserve the exact frozen bin layout without silent dropping.
    """
    conf = _finite(confidences, "confidences")
    if len(conf) != len(outcomes):
        raise DiagnosticContractError("confidences/outcomes: lengths must match")
    if any(value < 0.0 or value > 1.0 for value in conf):
        raise DiagnosticContractError("confidences: values must be in [0, 1]")
    binary = tuple(int(value) for value in outcomes)
    if any(value not in (0, 1) for value in binary):
        raise DiagnosticContractError("outcomes: expected binary event indicators")
    edges = _finite(bin_edges, "bin_edges")
    if len(edges) < 2 or edges[0] != 0.0 or edges[-1] != 1.0:
        raise DiagnosticContractError("bin_edges: must start at 0 and end at 1")
    if any(left >= right for left, right in zip(edges, edges[1:])):
        raise DiagnosticContractError("bin_edges: must be strictly increasing")

    result = []
    for index, (lower, upper) in enumerate(zip(edges, edges[1:])):
        final = index == len(edges) - 2
        positions = [
            i
            for i, value in enumerate(conf)
            if value >= lower and (value <= upper if final else value < upper)
        ]
        if positions:
            mean_confidence = math.fsum(conf[i] for i in positions) / len(positions)
            event_rate = math.fsum(binary[i] for i in positions) / len(positions)
            gap = abs(mean_confidence - event_rate)
        else:
            mean_confidence = event_rate = gap = 0.0
        result.append(
            ReliabilityBin(
                lower=lower,
                upper=upper,
                count=len(positions),
                mean_confidence=mean_confidence,
                event_rate=event_rate,
                absolute_gap=gap,
            )
        )
    if sum(row.count for row in result) != len(conf):
        raise DiagnosticContractError("bin_edges: did not cover every confidence")
    return tuple(result)


def weighted_calibration_gap(bins: Sequence[ReliabilityBin]) -> float:
    """Return count-weighted absolute gap for an already frozen bin layout."""
    rows = tuple(bins)
    total = sum(row.count for row in rows)
    if not rows or total <= 0:
        raise DiagnosticContractError("bins: expected at least one observed item")
    for row in rows:
        if row.count < 0 or any(
            not math.isfinite(value)
            for value in (
                row.lower,
                row.upper,
                row.mean_confidence,
                row.event_rate,
                row.absolute_gap,
            )
        ):
            raise DiagnosticContractError("bins: malformed reliability-bin value")
    return math.fsum(row.count * row.absolute_gap for row in rows) / total


def selective_risk_coverage(
    losses: Sequence[float],
    accepted: Sequence[bool],
) -> tuple[float, float]:
    """Return (risk, coverage) for an explicit caller-supplied acceptance mask."""
    values = _finite(losses, "losses")
    if len(values) != len(accepted):
        raise DiagnosticContractError("losses/accepted: lengths must match")
    mask = tuple(bool(value) for value in accepted)
    accepted_count = sum(mask)
    coverage = accepted_count / len(values)
    if accepted_count == 0:
        raise DiagnosticContractError(
            "accepted: selective risk is undefined at zero accepted coverage"
        )
    risk = math.fsum(
        value for value, keep in zip(values, mask) if keep
    ) / accepted_count
    return risk, coverage


def risk_coverage_points(
    losses: Sequence[float],
    scores: Sequence[float],
    *,
    thresholds: Sequence[float],
    accept_if_at_least: bool,
) -> tuple[SelectivePoint, ...]:
    """Evaluate explicit thresholds without choosing or optimizing them."""
    values = _finite(losses, "losses")
    confidence = _finite(scores, "scores")
    if len(values) != len(confidence):
        raise DiagnosticContractError("losses/scores: lengths must match")
    cuts = _finite(thresholds, "thresholds")
    if len(set(cuts)) != len(cuts):
        raise DiagnosticContractError("thresholds: duplicates are not admitted")
    rows = []
    for threshold in cuts:
        mask = tuple(
            score >= threshold if accept_if_at_least else score <= threshold
            for score in confidence
        )
        accepted_count = sum(mask)
        coverage = accepted_count / len(values)
        if accepted_count == 0:
            risk = None
        else:
            risk = math.fsum(
                value for value, keep in zip(values, mask) if keep
            ) / accepted_count
        rows.append(
            SelectivePoint(
                threshold=threshold,
                coverage=coverage,
                risk=risk,
                accepted=accepted_count,
                total=len(values),
            )
        )
    return tuple(rows)
