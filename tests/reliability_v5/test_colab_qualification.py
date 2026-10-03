"""Colab boundaries are checked without downloading or loading a model."""
import importlib.util
import sys
from pathlib import Path

import pytest

SCRIPTS = Path(__file__).resolve().parents[2] / "scripts"
sys.path.insert(0, str(SCRIPTS))
spec = importlib.util.spec_from_file_location("colab_qualification", SCRIPTS / "v5_s1_colab_qualification.py")
colab = importlib.util.module_from_spec(spec)
spec.loader.exec_module(colab)


def admission():
    return dict(cost_basis="COLAB_FREE_EXPOSED_RESOURCES", ui_subscription="NOT_SUBSCRIBED", compute_unit_balance=0, expected_incremental_spend_usd=0, new_purchase=False, normal_interactive_notebook=True, notebook_id="test-notebook", observed_remaining_runtime_seconds=19800)


@pytest.mark.parametrize("key,value", [("expected_incremental_spend_usd", 1), ("new_purchase", True), ("compute_unit_balance", 100), ("cost_basis", "PAY_AS_YOU_GO"), ("normal_interactive_notebook", False), ("notebook_id", ""), ("observed_remaining_runtime_seconds", float("nan")), ("observed_remaining_runtime_seconds", 0)])
def test_cost_and_runtime_fail_closed(key, value):
    record = admission()
    record[key] = value
    with pytest.raises(RuntimeError):
        colab.validate_admission(record)


def test_exact_head_and_dirty_source_block(monkeypatch):
    monkeypatch.setattr(colab.base, "git_text", lambda *args: "a" * 40 if args[0] == "rev-parse" else " M scripts/v5_s1_colab_qualification.py")
    with pytest.raises(RuntimeError, match="HEAD_MISMATCH"):
        colab.verify_head("b" * 40)
    with pytest.raises(RuntimeError, match="NON_EVIDENCE"):
        colab.verify_head("a" * 40)
    monkeypatch.setattr(colab.base, "git_text", lambda *args: "a" * 40 if args[0] == "rev-parse" else "?? artifacts/v5/development/s1-colab-resource-qualification/test/progress.json")
    assert colab.verify_head("a" * 40) == "a" * 40


def test_resource_headroom_stops_both_memory_domains():
    minimum = colab.base.MIN_MEMORY_HEADROOM
    colab.require_headroom(dict(ram_available_bytes=minimum, gpu_free_bytes=minimum))
    for key in ("ram_available_bytes", "gpu_free_bytes"):
        record = dict(ram_available_bytes=minimum, gpu_free_bytes=minimum)
        record[key] -= 1
        with pytest.raises(RuntimeError):
            colab.require_headroom(record)


def test_original_training_projection_preserved_and_scope_explicit():
    projection = colab.project_workload(180, 593)
    assert projection["original_256_example_seed_seconds"] == 46080
    assert projection["c2_training_length_sensitivity_seconds"] > projection["c1_training_length_sensitivity_seconds"]
    assert "not timed" in projection["limitations"]
