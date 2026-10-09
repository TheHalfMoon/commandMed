# V5 S1 post-processing development conventions freeze — 2026-10-09

Status: `PROSPECTIVE_FROZEN_BEFORE_POST_PROCESSING_DEVELOPMENT_OUTPUTS`

Scope: development/calibration-only application of the already-admitted mechanical interventions `A1_TS_V1`, `A2_SELBIAS_V1`, and `D1_DEFER_V1`, plus the ordered A1/A2 compositions and the technically meaningful C1-then-A1 composition.

This record does not authorize confirmatory/reserve access, independent-family replication, publication, merge, paid resources, PHI, or gated/private clinical data.

## Evidence source and partitions

The baseline source is the already-durable complete `BASELINE_V1` decision matrix from:

`artifacts/v5/development/s1-colab-resource-qualification/b1-complete-2026-10-04/baseline-decision-matrix.json`.

C1 composition analysis may read only the durable reviewed seed-11/29/47 C1 decision matrices.

The existing S1 partitions remain unchanged:

- `S1_CAL_TUNE` is the sole tuning/fitting split for A1, A2 and D1;
- `S1_DEV_EVAL` and `S1_CAL_EVAL` are evaluation-only development/calibration splits;
- `S1_TRAIN` is not used to tune these post-processing interventions;
- confirmatory/reserve identities remain unmaterialized and unavailable.

Canonical and transformed rows belonging to the same `task_id` remain one source task and are never treated as independent inferential clusters.

## Semantic alignment

Every A/B probability vector is first associated with the displayed A/B slots. For semantic diagnostics, align it into the fixed semantic order `(MATCH, MISMATCH)` using the row's `option_a_semantic` binding.

The semantic MATCH event is the calibration event. Its outcome is one when the frozen task target is MATCH and zero otherwise.

## Calibration diagnostics

NLL and multiclass Brier remain the primary probability-quality endpoints. Reliability summaries are secondary diagnostics and cannot substitute for proper scores.

For each evaluated condition and variant:

1. use semantic `p(MATCH)` versus the frozen binary MATCH event;
2. primary reliability table: 15 equal-width bins on `[0,1]`;
3. bin sensitivity: repeat with 10 and 20 equal-width bins;
4. each table preserves empty bins;
5. report count-weighted absolute calibration gap:
   `sum_b n_b * abs(mean_p_b - event_rate_b) / N`;
6. never optimize binning after seeing an intervention result.

No pooled canonical/transformed calibration claim replaces the separate variant reports.

## A1_TS_V1 scalar temperature

A1 is fit on **baseline S1_CAL_TUNE canonical logits only**.

The search variable is `log(T)`. The frozen deterministic candidate grid is:

- lower bound: `-6.000`;
- upper bound: `+6.000`;
- step: `0.005`;
- 2,401 candidates inclusive;
- `T = exp(log(T))`.

For each candidate, compute mean target NLL across all 256 canonical `S1_CAL_TUNE` tasks using the exact two-candidate softmax and the existing S1 tuning probability floor `1e-15`. This floor is used only for A1 tuning so an extreme grid point with an underflowed target probability remains numerically comparable; descriptive evaluation NLL remains the existing pure probability scorer. Choose the candidate with lowest mean tuning NLL. Exact numeric ties are resolved by: smaller `abs(log(T))`, then smaller `log(T)`.

The selected scalar is then frozen and applied unchanged to canonical and transformed evaluation rows. Record whether the selected point equals either grid boundary. Boundary selection is preserved as a limitation; the grid is not widened after inspecting results.

A1 changes probabilities only and must preserve displayed-logit ordering except exact ties.

## A2_SELBIAS_V1 display-slot prior

A2 estimates one displayed-slot prior using **all 512 baseline S1_CAL_TUNE rows**: 256 canonical plus 256 transformed.

Fit the prior in displayed A/B slot space using the existing project-owned geometric-mean estimator with `epsilon=1e-12`. Do not semantically align before fitting the display prior.

Apply that one frozen prior to every evaluation row in displayed-slot space, renormalize, then align to semantic MATCH/MISMATCH for semantic diagnostics.

No split-specific or evaluation-derived prior is permitted.

## Ordered A1/A2 compositions

Both orders are technically meaningful and are retained.

### A1 then A2

1. fit A1 temperature on baseline canonical `S1_CAL_TUNE`;
2. apply A1 to all 512 `S1_CAL_TUNE` rows;
3. estimate the A2 display-slot prior from those A1-transformed tuning probabilities;
4. evaluate by applying A1 first, then A2.

### A2 then A1

1. fit the baseline A2 display-slot prior from all 512 raw `S1_CAL_TUNE` rows;
2. apply A2 to canonical `S1_CAL_TUNE` rows;
3. convert the corrected positive probabilities to natural-log scores;
4. fit the scalar A1 temperature on those corrected canonical tuning scores using the identical frozen log-temperature grid;
5. evaluate by applying A2 first, then A1.

No symmetric interaction claim is made merely because both orders exist. Report both ordered effects and their order gap.

## C1 then A1 composition

The technically meaningful C1/A1 composition is C1 model adaptation followed by a fresh A1 fit.

For each durable C1 seed independently:

1. use that seed's C1 canonical `S1_CAL_TUNE` logits;
2. fit one temperature using the exact A1 grid above;
3. apply that seed-specific temperature to that seed's C1 evaluation rows.

The reverse order, fitting a baseline calibrator and then changing the model with C1, is not treated as an equivalent operational composition because C1 changes the logits on which the baseline calibration map was fit.

## D1_DEFER_V1 selective-control policy

D1 operates on the unmodified baseline semantic probability vector.

- selection score: maximum semantic class probability;
- accepted-case loss: top-1 semantic 0/1 error;
- methodological tuning target: empirical accepted-case risk `<= 0.05` on `S1_CAL_TUNE`;
- this 5% target is a methodological selective-control target, not a clinical safety tolerance.

Candidate thresholds are exactly the unique max-probability scores observed on canonical `S1_CAL_TUNE`. For each candidate, acceptance is `score >= threshold`, preserving ties as a block.

Choose the feasible threshold with maximum nonzero coverage subject to tuning risk `<=0.05`. Exact coverage ties choose the higher threshold. If no nonzero-coverage candidate is feasible, record `NO_FEASIBLE_NONZERO_COVERAGE`; do not invent a threshold and do not reinterpret zero coverage as zero risk.

Apply the selected threshold unchanged to canonical and transformed `S1_DEV_EVAL` and `S1_CAL_EVAL`. Every selective result reports risk and coverage together.

## Risk-coverage area convention

For descriptive risk-coverage curves, use the same max-semantic-probability score and 0/1 top-1 error.

Within each evaluation condition:

1. group exact equal scores into tie blocks;
2. order tie blocks from highest score to lowest;
3. after each whole block, compute cumulative coverage and cumulative accepted-case risk;
4. define the step-function area as:
   `AURC_STEP_TIE_BLOCK = sum_g (coverage_g - coverage_(g-1)) * risk_g`,
   with `coverage_0 = 0`.

This convention is deterministic and tie-order invariant. It is a secondary diagnostic; it is not a clinically calibrated risk guarantee.

## Development effect reporting

For every admitted condition, preserve at minimum:

- canonical/transformed accuracy;
- canonical/transformed NLL;
- canonical/transformed Brier;
- semantic JS between each task's canonical/transformed aligned distributions;
- calibration tables/gaps under 10/15/20 equal-width bins;
- where applicable, D1 risk, coverage and tie-block AURC.

No effect is labeled improve/harm/equivalent until native-unit margins and the frozen confidence procedure are available. These outputs remain descriptive development/calibration evidence.

## Fail-closed rules

The implementation must stop on missing/duplicate rows, wrong split counts, nonfinite logits/probabilities, identity mismatch, target/semantic mismatch, malformed tuning split, post-hoc parameter injection, unavailable durable C1 evidence, or any request to read confirmatory/reserve identities.

This freeze does not choose native-unit domain floors or meaningful margins and does not close the V5 scientific freeze.
