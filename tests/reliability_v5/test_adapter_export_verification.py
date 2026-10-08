"""Fail closed at the export trust boundary; no model or network required."""
import sys
import zipfile
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))
import v5_s1_verify_adapter_export as verifier


@pytest.mark.parametrize('name', ['../escape.json', '/absolute.json', 'C:/escape.json',
                                'folder\\escape.json', 'unexpected.json'])
def test_archive_rejects_unsafe_or_non_allowlisted_members(tmp_path, name):
    archive = tmp_path / 'export.zip'
    with zipfile.ZipFile(archive, 'w') as handle:
        handle.writestr(name, '{}')
    with pytest.raises(ValueError, match='ARCHIVE_MEMBER'):
        verifier.archive_members(archive)


def test_archive_rejects_case_insensitive_duplicates(tmp_path):
    archive = tmp_path / 'export.zip'
    with zipfile.ZipFile(archive, 'w') as handle:
        handle.writestr('adapter-analysis.json', '{}')
        handle.writestr('ADAPTER-ANALYSIS.JSON', '{}')
    with pytest.raises(ValueError, match='DUPLICATE_ARCHIVE_MEMBER'):
        verifier.archive_members(archive)


@pytest.mark.parametrize('payload', ['{"x":1,"x":2}', '{"x":NaN}', '{"x":Infinity}'])
def test_ambiguous_or_nonfinite_json_is_rejected(payload):
    with pytest.raises(ValueError):
        verifier.strict_json(payload)


def test_analysis_comparison_preserves_keys_and_declared_tolerance():
    verifier.close({'metric': .5 + 1e-13}, {'metric': .5})
    for actual in ({'metric': .5001}, {'metric': float('nan')}, {'other': .5}):
        with pytest.raises(ValueError):
            verifier.close(actual, {'metric': .5})


def test_original_seed_11_archive_inventory_and_crc_are_valid():
    repo = Path(__file__).resolve().parents[2]
    archive = repo / 'artifacts/v5/development/s1-kaggle-adapters/c1-seed-11-v4-2026-10-08/original-export.zip'
    payloads = verifier.archive_members(archive)
    result = verifier.strict_json(payloads['adapter-seed-result.json'])
    assert result['durable_export_verified'] is False
    assert result['medical_optimizer_steps'] == 32
    assert result['prompt_count'] == 16384
