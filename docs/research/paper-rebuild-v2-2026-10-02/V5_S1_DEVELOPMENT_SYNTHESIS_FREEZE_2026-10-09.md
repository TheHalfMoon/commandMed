# V5 S1 development synthesis mechanics freeze — 2026-10-09

Status: `PROSPECTIVE_FOR_FINAL_C2_SEED; DEVELOPMENT_ONLY`

This record freezes the mechanics of the final S1 cross-seed descriptive synthesis while C2 seed 47 is still running. C2 seeds 11 and 29 and all C1 seeds were already observed before this record, so this document does not convert any analysis into a preregistered confirmatory claim. It only prevents the final synthesis code from being changed in response to the remaining C2 seed-47 outcome.

## Scope

The synthesis is restricted to already-authorized development/calibration evidence. It may read:

- the durable baseline/B1 evidence from the complete bounded S1 baseline/B1 stage;
- the durable, reviewed C1 seeds 11, 29 and 47;
- the durable, reviewed C2 seeds 11, 29 and 47;
- C2's exported aggregate paired SQuAD retention metrics only.

The synthesis must fail closed until every required learned seed has a durable model-free verification receipt and a review record whose host-review state begins with `NO_MATERIAL_BLOCKER`.

No model call, optimizer step, intervention fit, confirmatory/reserve identity generation, holdout access, PHI, gated/private clinical data, paid API, or paid compute is part of this synthesis.

## Frozen descriptive outputs

For `S1_DEV_EVAL` and `S1_CAL_EVAL`, preserve the per-seed canonical/transformed:

- accuracy;
- negative log likelihood;
- multiclass Brier score;
- mean semantic Jensen-Shannon divergence.

For each learned intervention with seeds 11, 29 and 47, report only:

- the exact value by seed;
- arithmetic mean across the three seeds;
- minimum and maximum;
- sample standard deviation across the three training seeds.

For C2, apply the same descriptive cross-seed summary to the already-exported aggregate SQuAD v1.1 baseline/candidate EM and token-F1 values and paired aggregate deltas.

Between-training-seed standard deviation is a **training-randomness nuisance summary only**. It is not unchanged-base `repeatability95_j`, not a meaningful-effect margin, not a confidence interval, not a p-value, and not confirmatory inference.

## Explicitly excluded from this script

The synthesis must not:

- choose or modify any `m_j`;
- compute or claim TOST/equivalence/noninferiority;
- run Holm multiplicity procedures;
- estimate confirmatory power;
- invent calibration-bin counts, selective-risk thresholds, or AURC conventions that were not already frozen;
- average task variants as if they were independent source clusters;
- use SQuAD retention as evidence of general capability preservation;
- promote a development result to V5-C01 through V5-C07;
- materialize confirmatory or reserve identities.

Property-specific repeatability, calibration/selective-risk diagnostics, domain-floor justification, meaningful margins and power remain separate gates under the existing V5 protocols.

## Implementation

The project-owned implementation is `scripts/v5_s1_development_synthesis.py`. It is required to reject missing or unreviewed seed evidence, non-development analysis scope, nonzero spend, confirmatory/reserve flags, malformed evaluation counts, nonfinite values, or an incomplete seed set.

The output schema is `commandmed.v5.s1-development-synthesis.v1`.

This record does not close the scientific freeze. PR #320 remains OPEN / DRAFT / UNMERGED. Publication, merge, independent-family replication, confirmatory execution and reserve execution remain outside current authority.
