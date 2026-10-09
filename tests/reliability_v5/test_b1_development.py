from pathlib import Path
import sys

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import v5_s1_b1_development as b1


def test_checkpoint_uses_calibration_minimum_and_earliest_tie():
    assert b1.choose_epoch([2, 1, 1, 3]) == 2
    assert b1.choose_epoch([2, 1, .5]) == 3


@pytest.mark.parametrize("history", [[], [float("nan")], [float("inf")]])
def test_invalid_checkpoint_history_stops(history):
    with pytest.raises(ValueError):
        b1.choose_epoch(history)


@pytest.mark.parametrize("projected,available", [(float("nan"), 1000), (1, float("inf")), (500, 799), (0, 1000)])
def test_no_atomic_stage_admission_without_complete_duration(projected, available):
    with pytest.raises(RuntimeError, match="DURATION_BLOCKER"):
        b1.require_duration(projected, available)


def test_exact_reserved_duration_boundary_passes():
    b1.require_duration(500, 800)


def test_partial_scientific_matrix_cannot_be_accepted():
    with pytest.raises(RuntimeError, match="INCOMPLETE_MEDICAL_MATRIX"):
        b1.analyze_rows([dict(split="S1_DEV_EVAL", variant="canonical", task_id="fixture", target_index=0, logits=[0., 1.])])
