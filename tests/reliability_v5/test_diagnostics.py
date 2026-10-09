from __future__ import annotations

import math

import pytest

from src.commandmed.reliability_v5.diagnostics import (
    DiagnosticContractError,
    ReliabilityBin,
    reliability_bins,
    risk_coverage_points,
    selective_risk_coverage,
    weighted_calibration_gap,
)


def test_reliability_bins_respect_explicit_edges() -> None:
    rows = reliability_bins(
        [0.10, 0.20, 0.80, 1.00],
        [0, 1, 1, 1],
        bin_edges=[0.0, 0.5, 1.0],
    )
    assert len(rows) == 2
    assert rows[0].count == 2
    assert rows[0].mean_confidence == pytest.approx(0.15)
    assert rows[0].event_rate == pytest.approx(0.5)
    assert rows[1].count == 2
    assert rows[1].mean_confidence == pytest.approx(0.9)
    assert rows[1].event_rate == pytest.approx(1.0)
    assert weighted_calibration_gap(rows) == pytest.approx(
        (2 * 0.35 + 2 * 0.10) / 4
    )


def test_reliability_bins_keep_empty_bins_without_nan() -> None:
    rows = reliability_bins(
        [0.1, 0.9],
        [0, 1],
        bin_edges=[0.0, 0.25, 0.75, 1.0],
    )
    assert rows[1] == ReliabilityBin(
        lower=0.25,
        upper=0.75,
        count=0,
        mean_confidence=0.0,
        event_rate=0.0,
        absolute_gap=0.0,
    )


@pytest.mark.parametrize(
    "confidences,outcomes,edges",
    [
        ([0.2], [0], [0.1, 1.0]),
        ([0.2], [2], [0.0, 1.0]),
        ([math.nan], [0], [0.0, 1.0]),
        ([0.2, 0.3], [0], [0.0, 1.0]),
        ([0.2], [0], [0.0, 0.5, 0.5, 1.0]),
    ],
)
def test_reliability_bins_fail_closed(confidences, outcomes, edges) -> None:
    with pytest.raises(DiagnosticContractError):
        reliability_bins(confidences, outcomes, bin_edges=edges)


def test_selective_risk_coverage_uses_explicit_mask() -> None:
    risk, coverage = selective_risk_coverage(
        [0.0, 1.0, 0.5, 0.25],
        [True, False, True, False],
    )
    assert risk == pytest.approx(0.25)
    assert coverage == pytest.approx(0.5)


def test_selective_risk_rejects_zero_coverage() -> None:
    with pytest.raises(DiagnosticContractError, match="zero accepted coverage"):
        selective_risk_coverage([0.0, 1.0], [False, False])


def test_risk_coverage_points_never_choose_thresholds() -> None:
    rows = risk_coverage_points(
        losses=[0.0, 1.0, 0.5],
        scores=[0.9, 0.4, 0.7],
        thresholds=[0.5, 0.8, 1.0],
        accept_if_at_least=True,
    )
    assert [row.threshold for row in rows] == [0.5, 0.8, 1.0]
    assert rows[0].coverage == pytest.approx(2 / 3)
    assert rows[0].risk == pytest.approx(0.25)
    assert rows[1].coverage == pytest.approx(1 / 3)
    assert rows[1].risk == pytest.approx(0.0)
    assert rows[2].coverage == 0.0
    assert rows[2].risk is None


def test_risk_coverage_rejects_duplicate_thresholds() -> None:
    with pytest.raises(DiagnosticContractError, match="duplicates"):
        risk_coverage_points(
            losses=[0.0],
            scores=[0.5],
            thresholds=[0.5, 0.5],
            accept_if_at_least=True,
        )
