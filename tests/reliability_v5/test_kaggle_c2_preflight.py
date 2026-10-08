"""Model-free tests for prospective private zero-cost Kaggle C2 admission."""
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import v5_s1_kaggle_c2_preflight as c2


def admission():
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
        "intervention": "C2_CRDI_RETAIN_V1",
        "resume": False,
        "retention_repo": c2.RETENTION_REPO,
        "retention_revision": c2.RETENTION_REVISION,
        "retention_file": c2.RETENTION_FILE,
        "retention_source_sha256": c2.RETENTION_SHA256,
        "seed": 11,
        "kernel_ref": c2.c2_kernel(11),
        "quota_observed_unix": 1000,
        "free_gpu_seconds_available": 100000,
        "requested_session_timeout_seconds": 42000,
    }


@pytest.mark.parametrize(
    "key,value",
    [
        ("private", False),
        ("new_purchase", True),
        ("expected_incremental_spend_usd", 1),
        ("scientific_gpu_count", 2),
        ("scientific_device", "cuda:1"),
        ("confirmatory_materialized", True),
        ("reserve_materialized", True),
        ("phi", True),
        ("intervention", "C1_CRDI_V1"),
        ("resume", True),
        ("retention_repo", "other/squad"),
        ("retention_revision", "0" * 40),
        ("retention_source_sha256", "0" * 64),
    ],
)
def test_c2_admission_rejects_scope_or_retention_drift(key, value):
    record = admission()
    record[key] = value
    with pytest.raises(RuntimeError):
        c2.validate_admission(record, now=1100)


@pytest.mark.parametrize("seed", [0, 12, True, "29", 29.0])
def test_c2_kernel_rejects_unfrozen_or_non_integer_seed(seed):
    with pytest.raises(RuntimeError, match="UNFROZEN_C2_SEED"):
        c2.c2_kernel(seed)


def test_c2_window_and_kernel_are_bound():
    record = admission()
    assert c2.validate_admission(record, now=1100) == 41900
    record["kernel_ref"] = c2.c2_kernel(29)
    with pytest.raises(RuntimeError, match="KERNEL_IDENTITY_MISMATCH"):
        c2.validate_admission(record, now=1100)
    record = admission()
    for now in (999, 1601):
        with pytest.raises(RuntimeError):
            c2.validate_admission(record, now=now)


def test_complete_c1_chain_is_required(monkeypatch, tmp_path):
    monkeypatch.setattr(c2.base, "REPO", tmp_path)
    with pytest.raises(RuntimeError, match="COMPLETE_C1_CHAIN"):
        c2.require_complete_c1_evidence()


def test_c2_seed11_has_no_c2_predecessor_but_seed29_does(monkeypatch, tmp_path):
    monkeypatch.setattr(c2.base, "REPO", tmp_path)
    assert c2.require_prior_c2_evidence(11) == []
    with pytest.raises(RuntimeError, match="PRIOR_C2_SEED"):
        c2.require_prior_c2_evidence(29)


def test_c2_adapter_admission_calls_complete_and_sequential_gates(monkeypatch):
    import v5_s1_kaggle_c2_adapter_development as runtime

    monkeypatch.setattr(runtime.metadata, "validate_admission", lambda record: 42000)
    calls = []
    monkeypatch.setattr(runtime.metadata, "require_complete_c1_evidence", lambda: calls.append("c1"))
    monkeypatch.setattr(runtime.metadata, "require_prior_c2_evidence", lambda seed: calls.append(("c2", seed)))
    record = admission()
    runtime.validate_admission(record)
    assert calls == ["c1", ("c2", 11)]
    record["intervention"] = "C1_CRDI_V1"
    with pytest.raises(RuntimeError, match="FROZEN_C2_SEEDS_ONLY"):
        runtime.validate_admission(record)


def test_c2_retention_source_identity_is_exact_frozen_contract():
    assert c2.RETENTION_REPO == "rajpurkar/squad"
    assert c2.RETENTION_REVISION == "7b6d24c440a36b6815f21b70d25016731768db1f"
    assert c2.RETENTION_FILE == "plain_text/validation-00000-of-00001.parquet"
    assert c2.RETENTION_SHA256 == "8c6646d36bd5a95061e076788cf3161d11f6f3e7d625dac7a83bbed0a49f69f7"

def test_c2_runtime_requires_c2_specific_preflight_pass_state():
    source = (Path(__file__).resolve().parents[2] / "scripts/v5_s1_kaggle_c2_adapter_development.py").read_text(encoding="utf-8")
    assert "if result['status']!='KAGGLE_C2_PREFLIGHT_PASS':" in source
