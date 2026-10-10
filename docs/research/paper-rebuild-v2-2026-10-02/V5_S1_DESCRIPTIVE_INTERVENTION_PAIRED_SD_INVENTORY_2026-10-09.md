# V5 S1 complete development-only paired source-task SD inventory — 2026-10-09

Status: `MODEL_FREE_DESCRIPTIVE_NUISANCE_INVENTORY; NOT_FROZEN_FOR_CONFIRMATORY_POWER`.

## Purpose and allowable interpretation

All already-preserved baseline/B1, C1 and C2 medical-decision matrices contain enough paired `task_id` and frozen prompt metadata for **descriptive** source-task-level intervention-minus-baseline effects. This inventory does not re-use confirmatory/reserve data and does not run models or select endpoints. Its purpose is to show which development-only nuisance estimates **could** enter a future prospectively declared non-target power plan after the hypothesis family, seed modeling, and conservative variance rules have been fixed.

## Provenance and mechanics

- Project-owned offline analyzer: `scripts/v5_s1_development_paired_sd_inventory.py`. It reuses the *already tested* numerical `_row_metrics` from the frozen unchanged-base analysis for four primary metric definitions.
- Inputs: the separately committed 16,384-row baseline decision matrix, the exact independently verified R1 baseline for a source/row/logit consistency cross-check, and the nine already qualified complete B1/C1/C2 seed 11/29/47 development matrices.
- For each candidate input, it validates the complete ordered 16,384-row matrix, exact run intervention/seed, canonical/transformed source-task pairing, matching target, calculator/split/semantic/prompt identities, finite logits and all 3,840 source-case clusters in each DEV_EVAL and CAL_EVAL split. It refuses unmatched or missing evidence instead of imputing.
- For each intervention/seed/split/primary metric, computes all paired `candidate - unchanged baseline` per-source-case changes, their arithmetic mean and sample SD with `ddof=1`. NLL/Brier/JS are in raw (lower-is-better) metric orientation, so sign must be oriented for effect claims; paired SD is sign-invariant.
- Exact input SHA-256 values are included in machine-readable output. The result is deterministic and may be recomputed locally without weights, inference, Kaggle, network or API cost.
- This covers **9** intervention-seed matrices × **2** evaluation splits × **4** metrics = **72** descriptive sample SD cells (3,840 source cases per split). Training/CAL_TUNE cases are excluded.

## Reproducibility and selected facts

Output: `artifacts/v5/development/s1-paired-sd-inventory-2026-10-09/development-paired-sd.json`, SHA-256 `b1edf781b61d3f5ce227c08908ca43ad9864c0b398a7318c33895951af37bacd`. A separately written independent one-off analyzer, run before the checked utility was authored, produced numerically identical all 72 per-cell descriptive records.

As examples only, DEV_EVAL canonical accuracy paired source-task SD is approximately:

| Development condition | SD |
| --- | ---: |
| B1 seed 11 | 0.0510377 |
| B1 seed 29 | 0.998123 |
| C1 seed 11 | 0.136948 |
| C1 seed 29 | 0.807714 |
| C2 seed 11 | 0.0994853 |
| C2 seed 29 | 0.747907 |

The large contrasts across seeds make it unsafe to silently use a single favorable per-seed SD for future power. B1 seed-29 DEV canonical NLL paired SD is about 17.6174; C1 seed-11 DEV canonical NLL paired SD is about 0.135624. These distributions are developmental observations, not effect-significance or clinical-reliability conclusions.

## What this DOES NOT close

1. The **exact primary non-target hypothesis family**, including applicable interventions, endpoints, hard gates and multiplicity count, remains unbound for power. Selecting cells after examining these SDs could bias the analysis.
2. The three fixed learning seeds are part of the design; a single seed's within-source-case SD does **not** incorporate between-training-seed variability or crossed source/seed dependence. An explicit conservative combination/model is still needed.
3. Frozen benchmark-scale effect margins now exist separately (from R1/R2 repeatability and prospectively frozen domain floors). They are nonclinical; no raw SD here is automatically a final bound or evidence of 90% power at 4,096 clusters.
4. No individual condition is promoted into the primary family or independent-family replication, no confirmatory or reserve identities are generated, and no clinical/publication/merge authority is inferred.

The standing paper-first development research remains **unproven**. PRs #320, #321 and #322 remain draft, and this descriptive inventory is likewise draft-only pending independent review, signature compliance and a separate prospective family/variance-model decision.
