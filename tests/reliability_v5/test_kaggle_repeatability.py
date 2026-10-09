from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import v5_s1_kaggle_repeatability as repeat_runtime


def admission() -> dict:
    return {
        "cost_basis": "KAGGLE_ZERO_COST_RUNTIME",
        "username": "abdulazizshehri",
        "private": True,
        "expected_incremental_spend_usd": 0,
        "new_purchase": False,
        "scientific_gpu_count": 1,
        "scientific_device": "cuda:0",
        "confirmatory_materialized": False,
        "reserve_materialized": False,
        "phi": False,
        "intervention": "BASELINE_V1",
        "purpose": "UNCHANGED_BASE_REPEATABILITY",
        "repeat": 1,
        "resume": False,
        "kernel_ref": repeat_runtime.kernel_ref(1),
        "quota_observed_unix": 1000,
        "free_gpu_seconds_available": 50000,
        "requested_session_timeout_seconds": 30000,
    }


@pytest.mark.parametrize(
    "key,value",
    [
        ("private", False),
        ("expected_incremental_spend_usd", 1),
        ("new_purchase", True),
        ("scientific_gpu_count", 2),
        ("scientific_device", "cuda:1"),
        ("confirmatory_materialized", True),
        ("reserve_materialized", True),
        ("phi", True),
        ("intervention", "B1_TYPED_V1"),
        ("purpose", "OTHER"),
        ("resume", True),
    ],
)
def test_repeatability_admission_rejects_scope_drift(key, value) -> None:
    record = admission()
    record[key] = value
    with pytest.raises(RuntimeError):
        repeat_runtime.validate_admission(record, now=1100)


@pytest.mark.parametrize("repeat", [0, 3, True, "1", 1.0])
def test_repeatability_kernel_rejects_unfrozen_repeat(repeat) -> None:
    with pytest.raises(RuntimeError, match="UNFROZEN_REPEATABILITY_REPEAT"):
        repeat_runtime.kernel_ref(repeat)


def test_repeatability_window_and_kernel_are_bound() -> None:
    record = admission()
    assert repeat_runtime.validate_admission(record, now=1100) == 29900
    record["kernel_ref"] = repeat_runtime.kernel_ref(2)
    with pytest.raises(RuntimeError, match="KERNEL_IDENTITY_MISMATCH"):
        repeat_runtime.validate_admission(record, now=1100)
    record = admission()
    for now in (999, 1601):
        with pytest.raises(RuntimeError):
            repeat_runtime.validate_admission(record, now=now)


def test_repeatability_r1_has_no_repeat_predecessor(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setattr(repeat_runtime.base, "REPO", tmp_path)
    assert repeat_runtime.require_prior_repeatability_evidence(1) == []
    with pytest.raises(RuntimeError, match="PRIOR_REPEATABILITY"):
        repeat_runtime.require_prior_repeatability_evidence(2)


def test_repeatability_requires_complete_c2_chain(monkeypatch, tmp_path: Path) -> None:
    monkeypatch.setattr(repeat_runtime.base, "REPO", tmp_path)
    with pytest.raises(RuntimeError, match="EXPECTED_ONE_DURABLE_EVIDENCE_FOLDER"):
        repeat_runtime.require_complete_c2_evidence()


def test_repeatability_runner_contains_no_training_action() -> None:
    source = (
        Path(__file__).resolve().parents[2]
        / "scripts"
        / "v5_s1_kaggle_repeatability.py"
    ).read_text(encoding="utf-8")
    assert 'preflight("TRAINING"' not in source
    assert "torch.optim" not in source
    assert "fit_head(" not in source
    assert "BASELINE_V1" in source
