"""Fail-closed model-free tests for the prospective C2 export verifier."""
import sys
import zipfile
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "scripts"))
import v5_s1_verify_c2_adapter_export as verifier


@pytest.mark.parametrize(
    "name",
    ["../escape.json", "/absolute.json", "C:/escape.json", "folder\\escape.json", "unexpected.json"],
)
def test_c2_archive_rejects_unsafe_or_non_allowlisted_members(tmp_path, name):
    archive = tmp_path / "export.zip"
    with zipfile.ZipFile(archive, "w") as handle:
        handle.writestr(name, "{}")
    with pytest.raises(ValueError, match="ARCHIVE_MEMBER"):
        verifier.archive_members(archive)


def test_c2_archive_rejects_case_insensitive_duplicates(tmp_path):
    archive = tmp_path / "export.zip"
    with zipfile.ZipFile(archive, "w") as handle:
        handle.writestr("adapter-analysis.json", "{}")
        handle.writestr("ADAPTER-ANALYSIS.JSON", "{}")
    with pytest.raises(ValueError, match="DUPLICATE_ARCHIVE_MEMBER"):
        verifier.archive_members(archive)


@pytest.mark.parametrize("payload", ['{"x":1,"x":2}', '{"x":NaN}', '{"x":Infinity}'])
def test_c2_ambiguous_or_nonfinite_json_is_rejected(payload):
    with pytest.raises(ValueError):
        verifier.strict_json(payload)


def test_c2_core_inventory_contains_retention_and_all_action_preflights():
    required = {
        "retention-preparation-preload.json",
        "retention-preparation.json",
        "retention-resource-timing.json",
        "paired-retention-aggregate.json",
        "adapter-preflight-02-retention-resource.json",
        "adapter-preflight-03-maintenance-resource-backward.json",
        "adapter-preflight-04-complete-base-retention.json",
        "adapter-preflight-06-maintenance-training.json",
        "adapter-preflight-08-complete-candidate-retention.json",
    }
    assert required.issubset(verifier.CORE)


def test_c2_verifier_binds_exact_public_retention_source():
    assert verifier.retention.SOURCE_REPO == "rajpurkar/squad"
    assert verifier.retention.SOURCE_REVISION == "7b6d24c440a36b6815f21b70d25016731768db1f"
    assert verifier.retention.SOURCE_FILE_SHA256 == "8c6646d36bd5a95061e076788cf3161d11f6f3e7d625dac7a83bbed0a49f69f7"
