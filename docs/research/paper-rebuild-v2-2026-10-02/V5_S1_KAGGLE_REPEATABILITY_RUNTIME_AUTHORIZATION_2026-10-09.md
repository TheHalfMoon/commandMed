# V5 S1 Kaggle unchanged-base repeatability runtime authorization — 2026-10-09

**Decision owner:** Founder
**Decision state:** `AUTHORIZED_PROSPECTIVELY; METHOD_FREEZE_AND_EXACT_RUN_GATES_REQUIRED`
**Request superseded:** `V5_S1_KAGGLE_REPEATABILITY_RUNTIME_AMENDMENT_REQUEST_2026-10-09.md`

## Authority source

After the pending repeatability runtime amendment was explicitly surfaced as a remaining development gate, the Founder directed the executor to continue through project completion. This authorization overlay applies that instruction narrowly to the already-requested development-only unchanged-base repeatability amendment. It does not authorize any confirmatory/reserve execution, replication, publication or PR merge.

## Authorized scope

The executor may run base-only development/calibration inference on the existing legitimate free private Kaggle runtime solely to measure unchanged-base repeatability required by the frozen V5 power/margin gate.

This is **not** a B1 retraining rerun. No B1 head is fit or evaluated. No adapter is created. No optimizer step, temperature fit, selection-bias fit, defer-threshold fit or deterministic-tool intervention is executed in the repeatability runs.

## Required order

1. Freeze and review the exact repeatability method before the first repeatability model call.
2. Commit/push that method and pass fresh exact-head tests plus zero-cost review.
3. For each repeat, pass fresh exact-run preflight, current free-quota/runtime admission and single-GPU isolation.
4. Execute complete atomic base-only matrices only; no partial/resume/session cycling.
5. Retrieve and model-free verify each output before the next repeat.
6. Compute `repeatability95_j` only from the prospectively frozen estimator.
7. Preserve all zero/nonzero repeatability observations without tuning the estimator to the result.

## Preserved invariants

- exact `Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68` and bound artifact bundle;
- direct bfloat16, text-only, one scientific GPU `cuda:0`;
- exact bound tokenizer, `ANSWER:\n` marker and A/B token identities;
- existing RULE_ORACLE development/calibration identities only;
- full 16,384-prompt canonical/transformed matrix per admitted repeat;
- no truncation, sampling, alternate model/revision/precision or shortened matrix;
- private versioned outputs, local retrieval and model-free verification;
- zero incremental Founder spend; no paid API/compute;
- no PHI, gated/private clinical data, confirmatory or reserve identity materialization;
- no multi-GPU, DDP, DataParallel, sharding, checkpoint resume, quota bypass or account/session cycling;
- PR #320 remains OPEN / DRAFT / UNMERGED.

## Explicit exclusions

Independent-family replication, confirmatory/reserve execution, publication and merge remain unauthorized. This overlay does not choose calibration/selective-control conventions or native-unit domain floors; those remain separate prospective scientific gates.
