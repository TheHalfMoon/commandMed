#!/usr/bin/env python3
"""Source-bound review-nomination coverage, never a declared V5 Holm family."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re

import v5_manuscript_development_evidence_audit as audit
from v5_development_evidence_writer import publish_no_clobber

PRE = 'docs/research/paper-rebuild-v2-2026-10-02/preregistration-v5.md'
MATRIX = 'docs/research/paper-rebuild-v2-2026-10-02/intervention-matrix-protocol.md'
HASHES = {
    PRE: 'cd8cec1821fc63042a3a0ac872a82697e401b447004f98ac02d84f61408352bf',
    MATRIX: '1641bb0d6cb5ecc75ff5430d43aacf5fd24c991fb6ec10e49a5f3a344781a76f',
}
INTERVENTIONS = (
    'A1_TS_V1', 'A2_SELBIAS_V1', 'B1_TYPED_V1', 'C1_CRDI_V1',
    'C2_CRDI_RETAIN_V1', 'D1_DEFER_V1', 'D2_RULETOOL_V1',
)
AXES = (
    'P1_CANONICAL_DECISION', 'P2_CALIBRATION', 'P3_COHERENCE',
    'P4_SEMANTIC_STABILITY', 'P5_EVIDENCE_RESPONSIVENESS',
    'P6_RULE_CONFORMANCE', 'P7_SELECTIVE_CONTROL', 'P8_CAPABILITY_RETENTION',
)
DEVELOPMENT_PATHS_WITH_THREE_SEED_RECORDS = frozenset(
    ('B1_TYPED_V1', 'C1_CRDI_V1', 'C2_CRDI_RETAIN_V1')
)


class CoverageContractError(ValueError):
    """A prospective source, candidate identity or review boundary drifted."""


def require(valid: bool, error: str) -> None:
    if not valid:
        raise CoverageContractError(error)


def extract_source_candidates(prereg: str, matrix: str) -> tuple[tuple[str, ...], tuple[str, ...]]:
    """Read only the explicitly named prospective source sections, never outcomes."""
    require('## Bound intervention specification IDs' in prereg, 'MISSING_INTERVENTION_SECTION')
    part = prereg.split('## Bound intervention specification IDs', 1)[1].split('\n## ', 1)[0]
    interventions = tuple(re.findall(r'`([A-D][12]_[A-Z0-9_]+_V1)`', part))
    require(len(interventions) == len(set(interventions)), 'DUPLICATED_INTERVENTION_IDS')
    require(interventions == INTERVENTIONS, 'FROZEN_INTERVENTION_IDS_DRIFT')

    require('Primary matrix columns:' in matrix, 'MISSING_ASSURANCE_AXES')
    part = matrix.split('Primary matrix columns:', 1)[1].split('\n## ', 1)[0]
    axes = tuple(re.findall(r'^- `([P][1-8]_[A-Z_]+)`:', part, flags=re.MULTILINE))
    require(len(axes) == len(set(axes)), 'DUPLICATED_AXIS_IDS')
    require(axes == AXES, 'FROZEN_ASSURANCE_AXES_DRIFT')
    return interventions, axes


def build_inventory(interventions: tuple[str, ...], axes: tuple[str, ...]) -> dict:
    require(interventions == INTERVENTIONS and axes == AXES, 'CANDIDATE_GRID_DRIFT')
    cells = []
    for intervention in interventions:
        for axis in axes:
            cells.append({
                'candidate_intervention': intervention,
                'candidate_assurance_axis': axis,
                'review_disposition': 'UNDETERMINED',
                'nomination_is_primary_non_target': None,
                'intervention_target_axis_independently_reviewed': None,
                'applicability_to_this_task_family': None,
                'hard_gate_measurement_metric_and_unit': None,
                'native_metric_better_direction': None,
                'fixed_policy_setting': None,
                'source_population_and_split': None,
                'coupling_classification': None,
                'eligible_effect_margin_prospectively_qualified': None,
                'exclusion_or_inclusion_rationale': None,
                'development_training_seeds_with_descriptive_records': (
                    [11, 29, 47] if intervention in DEVELOPMENT_PATHS_WITH_THREE_SEED_RECORDS else []
                ),
                'development_records_prove_family_membership': False,
            })
    require(len(cells) == 56 and len({(x['candidate_intervention'], x['candidate_assurance_axis']) for x in cells}) == 56,
            'INCOMPLETE_CANDIDATE_COVERAGE')
    return {
        'schema': 'commandmed.v5.non-target-holm-candidate-coverage.v1',
        'status': 'REVIEW_COVERAGE_INVENTORY_ONLY_NOT_HOLM_FAMILY',
        'source_sha256': HASHES,
        'candidate_intervention_count': len(interventions),
        'candidate_assurance_axis_count': len(axes),
        'potential_intervention_axis_slots_not_hypothesis_tests': len(cells),
        'candidate_slots': cells,
        'prospectively_reviewed_primary_non_target_hypotheses': None,
        'actual_primary_non_target_holm_family_size': None,
        'independently_reviewed_holm_membership': False,
        'crossed_source_case_calculator_seed_variance_qualified': False,
        'each_primary_effect_90_percent_power_qualified': False,
        'confirmatory_access_authorized': False,
        'clinical_claim_or_publication_authorized': False,
        'decision_required': (
            'Qualified external reviewer must individually disposition all 56 candidate pairs as '
            'primary, exploratory, out-of-scope or inapplicable with source-bound rationale, '
            'after separately nominating target properties and hard-gate metrics. '
            'No slot is automatically a hypothesis and none may be silently omitted.'
        ),
    }


def source_bound_inventory(root: Path = audit.ROOT) -> dict:
    require(audit.audit(root)['frozen_source_files_verified'] == 307, 'ORIGINAL_FROZEN_FILES_DRIFT')
    loaded = {}
    for relative, digest in HASHES.items():
        p = audit._locked_file(root.resolve(), relative, digest)
        loaded[relative] = p.read_text(encoding='utf-8')
    return build_inventory(*extract_source_candidates(loaded[PRE], loaded[MATRIX]))


def main() -> int:
    parser = argparse.ArgumentParser()
    cmd = parser.add_mutually_exclusive_group(required=True)
    cmd.add_argument('--verify', type=Path)
    cmd.add_argument('--output', type=Path)
    args = parser.parse_args()
    result = source_bound_inventory()
    payload = (json.dumps(result, sort_keys=True, indent=2, allow_nan=False) + '\n').encode('utf-8')
    if args.verify is not None:
        require(args.verify.is_file() and args.verify.read_bytes() == payload, 'CANDIDATE_COVERAGE_REPLAY_DRIFT')
    else:
        publish_no_clobber(args.output, payload)
    print(json.dumps({'status': result['status'], 'coverage_slots': 56, 'holm_family_size': None,
                      'confirmatory_authorized': False}, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
