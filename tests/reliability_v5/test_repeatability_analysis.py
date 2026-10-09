from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import v5_s1_repeatability_analysis as repeatability


def _matrix() -> dict:
    rows = []
    splits = (
        ["S1_TRAIN"] * 256
        + ["S1_DEV_EVAL"] * 3840
        + ["S1_CAL_TUNE"] * 256
        + ["S1_CAL_EVAL"] * 3840
    )
    for index, split in enumerate(splits):
        task_id = f"task-{index:04d}"
        for variant in ("canonical", "transformed"):
            rows.append(
                {
                    "task_id": task_id,
                    "calculator_id": f"calc-{index % 64:02d}",
                    "split": split,
                    "variant": variant,
                    "target_index": index % 2,
                    "option_a_semantic": "MATCH" if index % 2 == 0 else "MISMATCH",
                    "prompt_sha256": f"{index:064x}"[-64:] if variant == "canonical" else f"{index + 10000:064x}"[-64:],
                    "logits": [0.25, -0.25] if variant == "canonical" else [0.20, -0.20],
                }
            )
    return {"complete": True, "intervention": "BASELINE_V1", "repeat": 1, "rows": rows}


def test_identical_runs_have_zero_primary_repeatability() -> None:
    first = _matrix()
    second = copy.deepcopy(first)
    second["repeat"] = 2
    result = repeatability.compare(first, second)
    assert result["eval_task_count"] == 7680
    assert result["repeat_count"] == 2
    for metric in repeatability.PRIMARY_METRICS:
        assert result["metrics"][metric]["repeatability95"] == 0.0


def test_nearest_rank_95_is_no_interpolation() -> None:
    values = [0.0] * 95 + [1.0] * 5
    assert repeatability._nearest_rank_95(values) == 0.0
    values = [0.0] * 94 + [1.0] * 6
    assert repeatability._nearest_rank_95(values) == 1.0


def test_cross_run_identity_change_fails_closed() -> None:
    first = _matrix()
    second = copy.deepcopy(first)
    second["repeat"] = 2
    second["rows"][512]["prompt_sha256"] = "f" * 64
    with pytest.raises(repeatability.RepeatabilityContractError, match="CROSS_RUN_IDENTITY_MISMATCH"):
        repeatability.compare(first, second)


def test_incomplete_matrix_fails_closed() -> None:
    first = _matrix()
    first["rows"].pop()
    with pytest.raises(repeatability.RepeatabilityContractError, match="16384"):
        repeatability.compare(first, copy.deepcopy(first))
