# V5 S1 cross-property development completion freeze — 2026-10-09

Status: `PROSPECTIVE_FROZEN_BEFORE_CROSS_PROPERTY_COMPLETION_OUTPUT`

## Purpose

Complete the development-only assurance-profile bookkeeping that can be derived from already-durable S1 decision matrices without any new model call or tuning.

This analysis is intentionally separate from the already-canonical post-processing result. It does not overwrite or reinterpret that artifact. It adds previously unreported cross-property diagnostics under parameters that were frozen before this completion output.

## Inputs

Only the following durable development/calibration sources are admitted:

- the complete baseline and B1 seed 11/29/47 decision matrices from the qualified baseline/B1 stage;
- the reviewed/model-free-verified C1 seed 11/29/47 decision matrices;
- the reviewed/model-free-verified C2 seed 11/29/47 decision matrices;
- the canonical post-processing artifact `artifacts/v5/development/s1-postprocessing-results-2026-10-09/development-postprocessing.json`, exact SHA-256 `51a4f0709620b48995d887fb2956c9c2fe0836ad37b286a2cddfd65e87979893`.

Confirmatory/reserve identities remain unmaterialized and inaccessible.

## Frozen completion rules

### Raw learned-condition assurance summaries

For raw B1, C1 and C2 seed matrices, independently for each seed, compute the already-frozen development summaries using the exact mechanics in `v5_s1_postprocessing_development.py`:

- canonical/transformed accuracy;
- canonical/transformed NLL;
- canonical/transformed two-class Brier;
- semantic MATCH reliability tables using exactly 10/15/20 equal-width bins, with 15 bins primary;
- paired canonical/transformed semantic Jensen-Shannon divergence.

No learned seed is pooled before its seed-specific result is preserved.

### Fixed D1 operational policy across conditions

The D1 threshold is **not refit**. Use exactly the baseline CAL_TUNE threshold already frozen and observed in the canonical post-processing artifact:

`0.8933094060543488`.

The selection score remains maximum semantic class probability. Accepted-case loss remains semantic top-1 0/1 error. Acceptance remains `score >= threshold`, preserving exact score ties.

Apply this one fixed threshold unchanged to:

- `BASELINE_V1`;
- `A1_TS_V1`;
- `A2_SELBIAS_V1`;
- `A1_THEN_A2`;
- `A2_THEN_A1`;
- raw B1 seed 11/29/47;
- raw C1 seed 11/29/47;
- raw C2 seed 11/29/47;
- C1-then-A1 seed 11/29/47 using the already-frozen seed-specific temperatures from the canonical post-processing analysis.

For every condition, split and variant, report accepted count, total count, coverage and accepted-case risk. Zero accepted coverage is reported with `risk=null`; it is never represented as zero risk.

The risk-coverage area remains the already-frozen deterministic whole-tie-block step area. The fixed-threshold result and full risk-coverage curve are distinct diagnostics.

### Assurance-axis completeness bookkeeping

For the bounded S1 RULE_ORACLE family:

- P1 canonical decision quality: measured by accuracy/NLL/Brier;
- P2 probability calibration: measured descriptively by the frozen reliability tables/gaps plus proper scores;
- P4 semantic stability: measured by paired semantic JS;
- P6 rule conformance: the binary MATCH/MISMATCH decision accuracy against the identity-bound deterministic calculator relation;
- P7 selective control: fixed D1 threshold risk and coverage plus the frozen tie-block risk-coverage diagnostic.

P3 probabilistic/logical coherence and P5 evidence responsiveness remain `NOT_APPLICABLE_OR_NOT_INSTANTIATED_IN_S1_RULE_ORACLE` unless a separately frozen task relation exists.

P8 capability retention is handled conservatively:

- B1 changes only the typed decision head while the base generative backbone is frozen; this is recorded as `BASE_BACKBONE_UNCHANGED_NOT_AN_EMPIRICAL_RETENTION_CLAIM`;
- C2 has the already-frozen narrow paired SQuAD v1.1 retention control;
- C1 changes model parameters but the admitted C1 runtime did not execute SQuAD. C1 P8 is therefore `NOT_MEASURED_DEVELOPMENT` and may not be imputed from C2.

This completion analysis does not authorize a C1 rerun or a new retention model call.

## Fail-closed requirements

The implementation must stop on:

- any missing/duplicate/incomplete decision matrix;
- any C1/C2 seed that is not durable, reviewed and model-free verified;
- a changed canonical post-processing artifact hash;
- any D1 threshold differing from the frozen value above;
- any changed A1/A2/C1-then-A1 tuning parameter relative to the canonical post-processing artifact;
- any nonfinite logits/probabilities;
- any attempt to tune thresholds, calibration bins or temperatures from evaluation rows;
- any request for confirmatory/reserve data.

## Interpretation boundary

These are development/calibration diagnostics only. They do not create an improve/harm/equivalent classification, a meaningful margin, a clinical-validity claim, a general retention claim, a confirmatory interaction claim, replication evidence, publication authority or merge authority.

PR #320 remains OPEN / DRAFT / UNMERGED.
