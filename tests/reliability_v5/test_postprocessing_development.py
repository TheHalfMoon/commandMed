from __future__ import annotations

import math
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import v5_s1_postprocessing_development as post


def _row(
    task: int,
    *,
    split: str = "S1_CAL_TUNE",
    variant: str = "canonical",
    logits: tuple[float, float] = (0.0, 0.0),
    target_index: int = 0,
    option_a_semantic: str = "MATCH",
) -> dict:
    return {
        "task_id": f"{task:064x}",
        "calculator_id": "pmid:test",
        "split": split,
        "variant": variant,
        "target_index": target_index,
        "option_a_semantic": option_a_semantic,
        "prompt_sha256": f"{task + 1:064x}",
        "logits": list(logits),
    }


def _logits_for_p0(probability: float) -> tuple[float, float]:
    return (math.log(probability / (1.0 - probability)), 0.0)


def test_semantic_alignment_and_target_flip_together() -> None:
    canonical = _row(1, logits=(2.0, 0.0), target_index=0, option_a_semantic="MATCH")
    swapped = _row(2, logits=(2.0, 0.0), target_index=0, option_a_semantic="MISMATCH")
    p1 = post._semantic_probabilities(post._display_probabilities(canonical), canonical)
    p2 = post._semantic_probabilities(post._display_probabilities(swapped), swapped)
    assert p1[0] > p1[1]
    assert p2[1] > p2[0]
    assert post._semantic_target(canonical) == 0
    assert post._semantic_target(swapped) == 1


def test_temperature_grid_exact_contract() -> None:
    grid = post._temperature_grid()
    assert len(grid) == 2401
    assert grid[0] == pytest.approx(-6.0)
    assert grid[-1] == pytest.approx(6.0)
    assert grid[1200] == pytest.approx(0.0)


def test_flat_logits_temperature_tie_resolves_to_one() -> None:
    rows = [_row(index, target_index=index % 2) for index in range(256)]
    fit = post.fit_temperature(rows, lambda row, t: post._a1_display(row, t))
    assert fit["log_temperature"] == pytest.approx(0.0)
    assert fit["temperature"] == pytest.approx(1.0)
    assert fit["boundary_selected"] is False


def test_a2_prior_uses_all_512_tuning_rows() -> None:
    rows = []
    for index in range(256):
        rows.append(_row(index, variant="canonical", logits=(1.0, 0.0)))
        rows.append(_row(index, variant="transformed", logits=(1.0, 0.0)))
    prior = post._fit_a2_prior(rows, post._baseline_transform)
    assert prior[0] > prior[1]
    assert sum(prior) == pytest.approx(1.0)


def test_d1_maximizes_coverage_subject_to_five_percent_risk() -> None:
    rows = []
    for index in range(256):
        if index < 128:
            logits = _logits_for_p0(0.99)
        else:
            logits = _logits_for_p0(0.40)  # wrong for target A, confidence 0.60
        rows.append(_row(index, logits=logits, target_index=0))
    fit = post.tune_d1(rows)
    assert fit["status"] == "FEASIBLE"
    assert fit["tuning_coverage"] == pytest.approx(0.5)
    assert fit["tuning_risk"] == pytest.approx(0.0)
    assert fit["threshold"] == pytest.approx(0.99)


def test_d1_reports_no_feasible_nonzero_coverage() -> None:
    rows = [
        _row(index, logits=_logits_for_p0(0.40), target_index=0)
        for index in range(256)
    ]
    fit = post.tune_d1(rows)
    assert fit["status"] == "NO_FEASIBLE_NONZERO_COVERAGE"
    assert fit["threshold"] is None
    assert fit["tuning_coverage"] == 0.0
    assert fit["tuning_risk"] is None


def test_tie_block_aurc_is_order_invariant() -> None:
    first = post._aurc_tie_block(
        scores=[0.9, 0.9, 0.6, 0.6],
        losses=[0.0, 1.0, 0.0, 1.0],
    )
    second = post._aurc_tie_block(
        scores=[0.9, 0.9, 0.6, 0.6],
        losses=[1.0, 0.0, 1.0, 0.0],
    )
    assert first["aurc_step_tie_block"] == pytest.approx(second["aurc_step_tie_block"])
    assert first["curve"] == second["curve"]
    assert first["aurc_step_tie_block"] == pytest.approx(0.5)


def test_temperature_fit_rejects_wrong_tuning_shape() -> None:
    with pytest.raises(post.PostprocessingError, match="256 canonical"):
        post.fit_temperature([_row(1)], lambda row, t: post._a1_display(row, t))


def test_nonfinite_logits_fail_closed() -> None:
    row = _row(1, logits=(math.nan, 0.0))
    with pytest.raises(post.PostprocessingError, match="nonfinite"):
        post._display_probabilities(row)
