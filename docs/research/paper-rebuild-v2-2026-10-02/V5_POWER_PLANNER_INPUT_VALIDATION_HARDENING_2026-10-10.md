# V5 development-only power planner input-contract hardening — 2026-10-10

Status: `MECHANICS_ONLY_VALIDATION; NOT_PROSPECTIVE_FAMILY_FREEZE; NO_QUALIFIED_POWER`.

## Verified defect

The unfrozen mechanical planning helper `scripts/v5_power_margin_plan.py` previously accepted caller-supplied `desired_power=0.51`, `family_alpha=0.20`, `planned_clusters=2`, fabricated one-character 'hashes', and Boolean `paired_sd=false` (implicitly converted to zero). This allowed a caller to generate apparently valid development power-plan output by **weakening prespecified constants or fabricating evidence identifiers**. Each failure mode was reproduced against the pre-fix helper on the Mac on 2026-10-10. No confirmatory data or model call was involved.

## Narrow correction

The corrected helper rejects those unreviewed substitutions. It requires the **exact current frozen V5 planning constants** family-wise `alpha=0.05`, desired power `0.90` and planned primary source cases `4096`; the project may authorize a *versioned, reviewed redesign* for a different sample count later, not silently mutate these inputs. It rejects booleans and numeric strings for the numeric nuisance, floor and repeatability fields, and requires three complete lowercase 64-character SHA-256 strings for each reported development metric (domain-floor justification, repeatability evidence, paired SD evidence). Negative synthetic tests cover relaxed parameters, corrupted hash lengths/characters/case, and Boolean/typed SD for reproducibility.

The output includes explicit `false` flags for independently frozen/qualified Holm family membership, the source-case × training-seed nuisance model, final 90% power and confirmatory execution authorization. The arithmetic helper remains a **normal-approximation planning mechanic** and does not enumerate the actual non-target hypothesis family.

## What a passing input contract does **not** establish

- A syntactically correct 64-character hash does **not** prove the file exists, that the file is a reviewed justification, or that the value actually came from that file. A later separate source-bound, reviewer-approved family/evidence reader must independently verify membership and provenance.
- A caller-supplied `primary_non_target_family_size` is not a prospectively reviewed manifest; the planner cannot certify Holm multiplicity just from a valid integer.
- Within-seed task/source-case SDs are **not** a conservative crossed multi-training-seed nuisance estimate. The 64-generator's unique original source-case/task mapping does not close between-seed inferential uncertainty.
- Neither syntax checks nor passing pytest, GitHub CI, Alibaba OCR eligibility or a signed-off commit prove clinical utility, qualified 90% power or publication authority.

This narrow successor does not edit the original 307 frozen entries, the scientific protocol, available development evidence, frozen benchmark margins or claim ledger. It creates no research/GPU/Kaggle/PHI/confirmatory/reserve action. The exact family, proper training-seed uncertainty/missingness conventions and independent methodological approval remain documented in [issue #326](https://github.com/TheHalfMoon/commandMed/issues/326).

## Reproduction

```sh
PYTHONPATH=src python3 -m pytest -q tests/reliability_v5/test_power_margin_plan.py
```

Do not interpret `PASS_POWER_MARGIN_PLAN` or `all_metrics_meet_normal_approx_target` as a final inferential certificate; these remain **development mechanics only**.
