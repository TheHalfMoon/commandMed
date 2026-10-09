# V5 S1 unchanged-base repeatability R1 — 2026-10-09

Status: `COMPLETE_DEVELOPMENT_REPEAT_1; NOT_REPEATABILITY_ESTIMATE_YET`

Private Kaggle kernel `abdulazizshehri/commandmed-v5-base-repeatability-r1`, version 1, completed the first frozen base-only repeat at scientific source `e1b166ca88b1bd649e2a736e817603ec714b7192`, tree `7a1f20449a504daa8bf25e4936108d0bae6e0f51`. The run evaluated the complete 16,384-prompt development/calibration matrix in 5972.115509542 seconds with no training and zero optimizer steps.

Exact original ZIP SHA-256: `dfb35b0216369bbb87bcec75c5715df974bb9f736c0db0af98148cea91d99dac`. The model-free verifier passed archive integrity, exact source/runtime/hardware identity, all 16,384 ordered prompt identities, 8,192 source-task identities, finite two-candidate logits and deterministic analysis reproduction using the pre-existing absolute `1e-12` C1/C2 verification tolerance. No model weights were loaded by the verifier.

The first verifier invocation failed only because the repeatability verifier had required byte-identical JSON floats. Two mean semantic-JS values differed by `2.168404344971009e-19`; the verifier portability repair is separately preserved and reviewed. The scientific export was not changed or rerun.

| Partition | Canonical accuracy | Canonical NLL | Canonical Brier | Mean semantic JS |
| --- | ---: | ---: | ---: | ---: |
| S1_DEV_EVAL | 0.48125 | 0.7831774818054636 | 0.5799630568176445 | 0.0012071127534052986 |
| S1_CAL_EVAL | 0.49322916666666666 | 0.7744336625615333 | 0.5720342460601971 | 0.00119290658998289 |

R1 alone does not define `repeatability95_j`. The prospectively frozen estimator requires exactly two complete independent base-only repeats. R2 remains sequentially gated on this R1 evidence being reviewed, committed and pushed.

The parent allocation exposed two Tesla T4 devices while the scientific child used only physical GPU 0 as `cuda:0`. Exact Qwen/Qwen3.5-0.8B-Base revision `dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`, direct BF16, no-resume execution and zero incremental Founder spend were preserved.

This is development-only repeatability evidence. It does not establish clinical validity, confirmatory equivalence/noninferiority, meaningful margins, calibration/selective-control claims, replication, publication or deployment. PR #320 remains OPEN / DRAFT / UNMERGED.
