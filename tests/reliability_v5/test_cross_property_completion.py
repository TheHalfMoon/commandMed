from __future__ import annotations

import json
import math
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import v5_s1_cross_property_completion as cross
import v5_s1_postprocessing_development as post


def _row(
    task: int,
    *,
    split: str,
    variant: str,
    probability_a: float,
    target_index: int = 0,
    option_a_semantic: str = "MATCH",
) -> dict:
    logits = [math.log(probability_a / (1.0 - probability_a)), 0.0]
    return {
        "task_id": f"{task:064x}",
        "calculator_id": "pmid:test",
        "split": split,
        "variant": variant,
        "target_index": target_index,
        "option_a_semantic": option_a_semantic,
        "prompt_sha256": f"{task + 1:064x}",
        "logits": logits,
    }


def _frozen_tuning(threshold: float = cross.FIXED_D1_THRESHOLD) -> dict:
    return {
        "tuning": {
            "D1_DEFER_V1": {
                "threshold": threshold,
                "risk_target": post.D1_RISK_TARGET,
            },
            "A1_TS_V1": {"temperature": 2.0},
            "A2_SELBIAS_V1": {"display_slot_prior": [0.6, 0.4]},
            "A1_THEN_A2": {
                "display_slot_prior_after_a1": [0.55, 0.45],
            },
            "A2_THEN_A1": {
                "temperature_after_a2": {"temperature": 3.0},
            },
        }
    }


def test_frozen_transform_bindings_do_not_refit() -> None:
    transforms = cross._transforms_from_frozen_artifact(_frozen_tuning())
    row = _row(
        1,
        split="S1_DEV_EVAL",
        variant="canonical",
        probability_a=0.8,
    )
    baseline = transforms["BASELINE_V1"](row)
    a1 = transforms["A1_TS_V1"](row)
    assert baseline[0] == pytest.approx(0.8)
    assert a1[0] != pytest.approx(baseline[0])
    assert set(transforms) == {
        "BASELINE_V1",
        "A1_TS_V1",
        "A2_SELBIAS_V1",
        "A1_THEN_A2",
        "A2_THEN_A1",
    }


def test_changed_d1_binding_fails_closed() -> None:
    with pytest.raises(cross.CrossPropertyError, match="D1_BINDING"):
        cross._transforms_from_frozen_artifact(_frozen_tuning(0.5))


def test_fixed_d1_uses_one_supplied_threshold_without_refitting(monkeypatch) -> None:
    monkeypatch.setattr(post, "SPLIT_COUNTS", {
        "S1_DEV_EVAL": 2,
        "S1_CAL_EVAL": 2,
    })
    rows = []
    task = 1
    for split in post.EVAL_SPLITS:
        for variant in post.VARIANTS:
            rows.append(
                _row(
                    task,
                    split=split,
                    variant=variant,
                    probability_a=0.95,
                    target_index=0,
                )
            )
            task += 1
            rows.append(
                _row(
                    task,
                    split=split,
                    variant=variant,
                    probability_a=0.90,
                    target_index=1,
                )
            )
            task += 1
    result = cross._fixed_d1(
        rows,
        post._baseline_transform,
        threshold=cross.FIXED_D1_THRESHOLD,
    )
    dev = result["S1_DEV_EVAL"]["canonical"]
    assert dev["threshold"] == cross.FIXED_D1_THRESHOLD
    assert dev["accepted"] == 2
    assert dev["coverage"] == 1.0
    assert dev["risk"] == pytest.approx(0.5)


def test_fixed_d1_rejects_any_other_threshold(monkeypatch) -> None:
    monkeypatch.setattr(post, "SPLIT_COUNTS", {
        "S1_DEV_EVAL": 1,
        "S1_CAL_EVAL": 1,
    })
    rows = []
    task = 1
    for split in post.EVAL_SPLITS:
        for variant in post.VARIANTS:
            rows.append(
                _row(
                    task,
                    split=split,
                    variant=variant,
                    probability_a=0.95,
                )
            )
            task += 1
    with pytest.raises(cross.CrossPropertyError, match="D1_THRESHOLD"):
        cross._fixed_d1(rows, post._baseline_transform, threshold=0.5)


def test_reviewed_seed_folder_requires_durable_review(tmp_path: Path) -> None:
    folder = tmp_path / "c2-seed-11-v1-2026-10-09"
    (folder / "evidence").mkdir(parents=True)
    (folder / "evidence" / "adapter-decision-matrix.json").write_text(
        "{}",
        encoding="utf-8",
    )
    (folder / "export-verification-receipt.json").write_text(
        json.dumps({
            "status": "PASS_MODEL_FREE_C2_EXPORT_VERIFICATION",
            "seed": 11,
            "intervention": "C2_CRDI_RETAIN_V1",
            "durable_export_verified": True,
        }),
        encoding="utf-8",
    )
    (folder / "validation-and-review.json").write_text(
        json.dumps({
            "spend_usd": 0,
            "host_review": "NO_MATERIAL_BLOCKER; fixture",
        }),
        encoding="utf-8",
    )
    assert cross._reviewed_seed_folder(
        tmp_path,
        prefix="c2",
        seed=11,
        expected_status="PASS_MODEL_FREE_C2_EXPORT_VERIFICATION",
        intervention="C2_CRDI_RETAIN_V1",
    ) == folder

    review = folder / "validation-and-review.json"
    review.write_text(
        json.dumps({"spend_usd": 0, "host_review": "BLOCKED"}),
        encoding="utf-8",
    )
    with pytest.raises(cross.CrossPropertyError, match="EXPECTED_ONE_REVIEWED"):
        cross._reviewed_seed_folder(
            tmp_path,
            prefix="c2",
            seed=11,
            expected_status="PASS_MODEL_FREE_C2_EXPORT_VERIFICATION",
            intervention="C2_CRDI_RETAIN_V1",
        )
