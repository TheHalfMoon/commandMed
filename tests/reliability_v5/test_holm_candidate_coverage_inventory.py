"""No statistical decisions may be manufactured by exhaustive candidate listing."""
from __future__ import annotations

import copy
import json
import subprocess
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / 'scripts'))
import v5_holm_family_coverage_inventory as grid


def test_source_bound_complete_56_candidate_grid_without_any_family_claim() -> None:
    result = grid.source_bound_inventory()
    assert result['potential_intervention_axis_slots_not_hypothesis_tests'] == 56
    assert len(result['candidate_slots']) == 56
    assert {(c['candidate_intervention'], c['candidate_assurance_axis']) for c in result['candidate_slots']} == {
        (i, a) for i in grid.INTERVENTIONS for a in grid.AXES
    }
    assert all(c['review_disposition'] == 'UNDETERMINED'
               and c['nomination_is_primary_non_target'] is None
               and c['hard_gate_measurement_metric_and_unit'] is None
               and c['development_records_prove_family_membership'] is False
               for c in result['candidate_slots'])
    assert result['actual_primary_non_target_holm_family_size'] is None
    assert result['prospectively_reviewed_primary_non_target_hypotheses'] is None
    for flag in ('independently_reviewed_holm_membership',
                 'crossed_source_case_calculator_seed_variance_qualified',
                 'each_primary_effect_90_percent_power_qualified',
                 'confirmatory_access_authorized', 'clinical_claim_or_publication_authorized'):
        assert result[flag] is False
    by_intervention = {i: [c for c in result['candidate_slots'] if c['candidate_intervention'] == i]
                       for i in grid.INTERVENTIONS}
    for intervention, cells in by_intervention.items():
        expected_seeds = [11, 29, 47] if intervention in grid.DEVELOPMENT_PATHS_WITH_THREE_SEED_RECORDS else []
        assert len(cells) == 8
        assert all(c['development_training_seeds_with_descriptive_records'] == expected_seeds for c in cells)


def test_exact_saved_bytes_and_no_clobber_replay(tmp_path: Path) -> None:
    saved = grid.audit.ROOT / 'artifacts/v5/development/s1-holm-coverage-2026-10-11/candidate-coverage.json'
    payload = (json.dumps(grid.source_bound_inventory(), sort_keys=True,
                          indent=2, allow_nan=False) + '\n').encode()
    assert saved.read_bytes() == payload
    cmd = [sys.executable, str(grid.audit.ROOT / 'scripts/v5_holm_family_coverage_inventory.py')]
    v = subprocess.run(cmd + ['--verify', str(saved)], cwd=tmp_path, capture_output=True, text=True)
    assert v.returncode == 0, v.stderr
    out = tmp_path / 'candidate-coverage.json'
    a = subprocess.run(cmd + ['--output', str(out)], cwd=tmp_path, capture_output=True, text=True)
    assert a.returncode == 0, a.stderr
    assert out.read_bytes() == payload
    b = subprocess.run(cmd + ['--output', str(out)], cwd=tmp_path, capture_output=True, text=True)
    assert b.returncode != 0
    assert out.read_bytes() == payload
    altered = tmp_path / 'altered.json'
    altered.write_bytes(payload + b'\n')
    c = subprocess.run(cmd + ['--verify', str(altered)], cwd=tmp_path, capture_output=True, text=True)
    assert c.returncode != 0
    assert 'CANDIDATE_COVERAGE_REPLAY_DRIFT' in c.stderr


@pytest.mark.parametrize('mutator,reason', [
    (lambda interventions, axes: (interventions[:-1], axes), 'CANDIDATE_GRID_DRIFT'),
    (lambda interventions, axes: (interventions, axes[:-1]), 'CANDIDATE_GRID_DRIFT'),
    (lambda interventions, axes: (interventions + (interventions[0],), axes), 'CANDIDATE_GRID_DRIFT'),
    (lambda interventions, axes: (interventions, axes + (axes[0],)), 'CANDIDATE_GRID_DRIFT'),
])
def test_missing_and_duplicate_candidates_fail_closed(mutator, reason: str) -> None:
    i, a = mutator(grid.INTERVENTIONS, grid.AXES)
    with pytest.raises(grid.CoverageContractError, match=reason):
        grid.build_inventory(i, a)


def test_frozen_sections_cannot_silently_change() -> None:
    a = (grid.audit.ROOT / grid.PRE).read_text()
    b = (grid.audit.ROOT / grid.MATRIX).read_text()
    assert grid.extract_source_candidates(a, b) == (grid.INTERVENTIONS, grid.AXES)
    with pytest.raises(grid.CoverageContractError, match='FROZEN_INTERVENTION_IDS_DRIFT'):
        grid.extract_source_candidates(a.replace('C2_CRDI_RETAIN_V1', 'C2_ALT_V1', 1), b)
    with pytest.raises(grid.CoverageContractError, match='FROZEN_ASSURANCE_AXES_DRIFT'):
        grid.extract_source_candidates(a, b.replace('P6_RULE_CONFORMANCE', 'P6_NEW_AXIS', 1))
    with pytest.raises(grid.CoverageContractError, match='DUPLICATED_AXIS_IDS'):
        grid.extract_source_candidates(a, b.replace('Primary matrix columns:',
                                                      'Primary matrix columns:\n- `P1_CANONICAL_DECISION`: duplicate\n', 1))


def test_source_hashes_are_byte_pinned_and_307_original_entries_preserved() -> None:
    result = grid.audit.audit()
    assert result['frozen_source_files_verified'] == 307
    for path, digest in grid.HASHES.items():
        assert grid.audit._digest(grid.audit.ROOT / path) == digest
