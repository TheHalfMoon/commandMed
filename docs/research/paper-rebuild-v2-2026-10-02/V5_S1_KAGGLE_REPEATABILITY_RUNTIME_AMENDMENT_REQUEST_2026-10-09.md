# V5 S1 Kaggle unchanged-base repeatability runtime amendment request — 2026-10-09

**Decision owner:** Founder
**Decision state:** `REQUESTED_NOT_AUTHORIZED`
**Scope:** development-only unchanged-base repeatability evidence on the existing private zero-cost Kaggle path

## Why this request exists

The adopted V5 evaluation protocol requires unchanged-base repeated runs. The power/margin gate defines `repeatability95_j` from development-only unchanged-base paired differences.

The current bounded development authorization permits repeatability/nuisance estimation. However, the later 2026-10-08 Kaggle runtime amendment explicitly states `Do not rerun baseline/B1`. The durable evidence contains only one complete scientific baseline matrix. Later resource-timing probes are incomplete and do not preserve the raw repeated logits needed for property-level repeatability.

Therefore the executor must not treat the existing Kaggle amendment as permission to launch new unchanged-base scientific matrices.

## Requested narrow amendment

If approved, permit **base-only development/calibration inference for repeatability measurement** on the legitimate free private Kaggle allocation, subject to all existing exact-run gates.

This is not a B1 retraining rerun. The B1 typed heads remain untouched and are not refit. No adapter, optimizer, checkpoint selection, temperature fit, selection-bias fit, defer threshold fit, or rule-tool intervention is executed.

The exact repeat count, pairing rule and `repeatability95_j` aggregation mechanics must be frozen and reviewed before the first repeatability model call. This request does not itself select those scientific quantities.

## Invariants that remain unchanged

- model: `Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`;
- exact bound model bundle and tokenizer/interface;
- direct bfloat16 only;
- text-only path;
- one scientific GPU only: `cuda:0`;
- same committed RULE_ORACLE development/calibration identities and full paired prompt matrix;
- no truncation and no sampling;
- no confirmatory or reserve identity materialization;
- no PHI/private/gated clinical data;
- no paid API, paid compute, purchase, quota bypass, account cycling, session cycling, checkpoint resume, multi-GPU, DDP, DataParallel, tensor parallelism or sharding;
- zero incremental Founder spend;
- private versioned output, local retrieval, model-free verification, full tests/review, ordinary commit/push;
- PR #320 remains OPEN / DRAFT / UNMERGED;
- publication and merge remain unauthorized.

## Required prospective method freeze before any model action

A separate reviewed record must bind:

1. exact repeat count;
2. exact source-item pairing rule;
3. exact per-property repeated-run statistic;
4. exact mapping from repeated raw probabilities/logits to `repeatability95_j`;
5. missing/failed-run handling;
6. deterministic or stochastic-runtime interpretation;
7. complete-run duration/quota admission;
8. evidence schema and model-free verifier.

No repeatability output may be used to choose its own estimator after inspection.

## Requested authority state

```text
V5_KAGGLE_UNCHANGED_BASE_REPEATABILITY=REQUESTED_NOT_AUTHORIZED
BASE_ONLY_DEVELOPMENT_CALIBRATION_INFERENCE=REQUESTED_NOT_AUTHORIZED
B1_RETRAINING=NO
C1_C2_RETRAINING=NO
CONFIRMATORY_EXECUTION=NO
CONFIRMATORY_IDENTITY_MATERIALIZATION=NO
RESERVE_EXECUTION=NO
PAID_COMPUTE=NO
PAID_API=NO
PHI=NO
GATED_DATA=NO
INCREMENTAL_FOUNDER_SPEND_USD=0
```

Until explicit Founder approval is recorded, no new unchanged-base scientific matrix may be launched under this request.
