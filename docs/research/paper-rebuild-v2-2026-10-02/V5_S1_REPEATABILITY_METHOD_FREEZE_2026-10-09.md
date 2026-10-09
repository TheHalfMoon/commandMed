# V5 S1 unchanged-base repeatability method freeze — 2026-10-09

Status: `PROSPECTIVE_FROZEN_BEFORE_REPEATABILITY_MODEL_CALLS`

Authority: `V5_S1_KAGGLE_REPEATABILITY_RUNTIME_AUTHORIZATION_2026-10-09.md`.

## Purpose

Measure development-only unchanged-base numerical/decision repeatability needed by `POWER_AND_MARGIN_GATE_V5.md` without retraining B1 or changing any scientific model/interface setting.

## Runs

- exactly two complete independent private Kaggle base-only runs: `R1` then `R2`;
- both use `BASELINE_V1`, exact Qwen/Qwen3.5-0.8B-Base revision `dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`, direct bfloat16 and one scientific GPU `cuda:0`;
- both evaluate the complete existing 8,192 development/calibration task identities in canonical and transformed form: 16,384 prompts per run;
- no training, adapter, optimizer, checkpoint selection, retention decoding, temperature fit, selection-bias fit, defer-policy fit or rule-tool intervention;
- no partial run is admitted; `R2` starts only after `R1` is retrieved, model-free verified, reviewed, committed and pushed;
- no rerun of a completed repeat.

## Raw row contract

Each run exports exactly one ordered row per `(task_id, variant)` with: `task_id`, `calculator_id`, `split`, `variant`, `target_index`, `option_a_semantic`, `prompt_sha256`, and the two finite candidate logits `[A, B]`. No prompt text or protected payload is exported.

Rows are ordered by the existing deterministic development-example order, with `canonical` immediately followed by `transformed` for each task. Exact prompt/case/split identities must match the already-bound S1 preparation.

## Probability and metric mechanics

Analysis uses float64 arithmetic after export. Candidate probabilities are the stable two-class softmax of the exported A/B logits.

For each source task `i` and run `r`:

- `canonical_accuracy(i,r)`: 1 when canonical argmax equals the frozen target, else 0;
- `canonical_nll(i,r)`: negative log target probability, with the existing probability floor `1e-15`;
- `canonical_brier(i,r)`: two-class multiclass Brier score against the frozen target;
- transformed accuracy/NLL/Brier are computed identically as secondary diagnostics;
- `semantic_js(i,r)`: Jensen-Shannon divergence between canonical and transformed distributions after alignment to the same semantic MATCH/MISMATCH order using `option_a_semantic`.

## Repeatability estimator

For metric `j` and source task `i`, define the unchanged-base paired difference:

`d[i,j] = abs(metric(i,R2) - metric(i,R1))`.

The source task is the clustering unit. Canonical and transformed prompts are never treated as independent source cases.

For each metric, compute the empirical nearest-rank 95th percentile separately on `S1_DEV_EVAL` and `S1_CAL_EVAL`: sort the per-task absolute differences ascending and select element `ceil(0.95*n)-1` with zero-based indexing. No interpolation is used.

The frozen repeatability quantity is:

`repeatability95_j = max(q95_DEV_EVAL_j, q95_CAL_EVAL_j)`.

Primary repeatability quantities are frozen for canonical NLL, canonical Brier, canonical accuracy and semantic JS. Transformed NLL/Brier/accuracy are secondary diagnostics and are preserved but do not create additional primary margins.

If every paired value is identical, `repeatability95_j = 0` is reported rather than replaced by a positive floor. The final meaningful margin still uses the separate protocol rule `m_j = max(domain_floor_j, 2 * repeatability95_j)`.

## Missing/failure handling

- any missing row, duplicate row, identity mismatch, nonfinite logit, wrong order, changed prompt hash, changed target, changed semantic legend or incomplete matrix invalidates the repeat;
- any failed/partial repeat is preserved as negative evidence but contributes no repeatability estimate;
- no estimator, percentile rule, split pooling, run count or metric is changed after observing R1/R2 outputs.

## Runtime and evidence boundary

Every repeat requires fresh live-head/remote equality, current free-quota observation, atomic-duration admission, exact model/artifact/tokenizer/source verification, single-GPU isolation, preflight PASS and zero incremental spend. Outputs are private/versioned and independently retrieved.

A model-free verifier must reconstruct the complete row identity/order, recompute per-run analysis and, after both repeats are durable, reproduce the paired repeatability analysis without loading weights.

## Scope exclusions

This freeze does not choose calibration bins, selective-control thresholds, A1/A2/D1 tuning rules, domain floors, confirmatory identities or replication. It does not authorize publication or PR merge.
