from __future__ import annotations

import copy
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import v5_s1_development_paired_sd_inventory as inventory


def _rows() -> list[dict]:
    rows = []
    for index, split in enumerate(("S1_DEV_EVAL", "S1_DEV_EVAL", "S1_CAL_EVAL", "S1_CAL_EVAL")):
        for variant in ("canonical", "transformed"):
            rows.append({
                "calculator_id": "calc-01",
                "task_id": f"task-{index}",
                "split": split,
                "variant": variant,
                "target_index": index % 2,
                "option_a_semantic": "MATCH",
                "prompt_sha256": f"{index}-{variant}",
                "logits": [0.1, 0.2],
            })
    return rows


def test_identical_paired_inputs_produce_zero_sample_sd(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(inventory, "EVAL_PER_SPLIT", 2)
    # The production indexer requires 16,384 rows. Reuse the small pair
    # via the same frozen _row_metrics construction for focused unit tests.
    rows = _rows()
    indexed = {}
    for offset in range(0, len(rows), 2):
        c, t = rows[offset : offset + 2]
        indexed[c["task_id"]] = (inventory._row_metrics(c, t), c, t)
    out = inventory._compute_pair(indexed, copy.deepcopy(indexed))
    assert set(out) == set(inventory.EVAL_SPLITS)
    for split in inventory.EVAL_SPLITS:
        for metric in inventory.PRIMARY_METRICS:
            assert out[split][metric]["paired_source_task_sample_sd"] == 0.0


def test_nonzero_source_task_delta_has_positive_sample_sd(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(inventory, "EVAL_PER_SPLIT", 2)
    rows = _rows()
    baseline = {
        rows[i]["task_id"]: (inventory._row_metrics(*rows[i : i + 2]), *rows[i : i + 2])
        for i in range(0, 8, 2)
    }
    candidate = copy.deepcopy(baseline)
    _, c, t = candidate["task-0"]
    c["logits"] = [3.0, -3.0]
    candidate["task-0"] = (inventory._row_metrics(c, t), c, t)
    result = inventory._compute_pair(baseline, candidate)
    assert result["S1_DEV_EVAL"]["canonical_nll"]["paired_source_task_sample_sd"] > 0.0
    assert result["S1_DEV_EVAL"]["canonical_accuracy"]["paired_source_task_sample_sd"] > 0.0
    assert result["S1_CAL_EVAL"]["canonical_accuracy"]["paired_source_task_sample_sd"] == 0.0


def test_cross_run_prompt_identity_change_rejected(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(inventory, "EVAL_PER_SPLIT", 2)
    rows = _rows()
    base = {rows[i]["task_id"]: (inventory._row_metrics(*rows[i : i + 2]), *rows[i : i + 2]) for i in range(0, 8, 2)}
    changed = copy.deepcopy(base)
    metric, c, t = changed["task-0"]
    c["prompt_sha256"] = "different"
    with pytest.raises(inventory.DescriptiveInventoryContractError, match="INTERVENTION_CHANGED"):
        inventory._compute_pair(base, changed)


def test_bad_sample_count_fails_closed() -> None:
    with pytest.raises(inventory.DescriptiveInventoryContractError, match="INCOMPLETE_16384"):
        inventory._validate_and_index(_rows())
