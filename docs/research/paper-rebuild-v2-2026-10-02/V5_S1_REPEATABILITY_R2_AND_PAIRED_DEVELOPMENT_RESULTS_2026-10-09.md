# V5 S1 independent base R2 and paired repeatability results — 2026-10-09

Status: `DEVELOPMENT_ONLY; R1_R2_MODEL_FREE_VERIFIED; DRAFT_EVIDENCE_FOR_REVIEW`.

## Exact upstream scientific execution

- Repository remains `TheHalfMoon/commandMed`. The frozen scientific R2 branch was `research/commandmed-paper-first-principles`, exact commit `819cf1dda443937eec0360e6051a89062b545cb9`, tree `4ee326864bb3c13aa6a34630aec629c358c1c582`. The PR #320 research branch is not advanced by preparing this evidence.
- Kaggle: private `abdulazizshehri/commandmed-v5-base-repeatability-r2`, version 1; terminal Kaggle `KernelWorkerStatus.COMPLETE`. This was an already-launched kernel, **not** a fresh run initiated during R2 collection.
- Atomic bootstrap: `ATOMIC_KERNEL_FINISHED`, `exit_code=0`, `exported_archive=true`. Scientific payload: `BASELINE_REPEAT_COMPLETE_DEVELOPMENT`, `complete_matrix=true`, `prompt_count=16384`, `optimizer_steps=0`, `training=false`, `resume=false`, `spend_usd=0`, `confirmatory_materialized=false`, `reserve_materialized=false`, `phi=false`.
- Underlying source cases: 8,192; canonical and transformed prompts: 16,384. Direct BF16 frozen Qwen/Qwen3.5-0.8B-Base, single **scientifically utilized** `cuda:0`. The physical Kaggle host reported **two** Tesla T4 devices; only one was exposed to / used by the scientific subprocess. Do not claim the physical host has only one GPU.
- R2 measured scientific wall time: 6,075.364370006 seconds. Kernel setup recorded removal of unused optional `torchao` before model load; the pinned torch package/model setting was preserved.
- The original R2 ZIP hash: `73f24c06f2d54e34cc20f2137f06b0728f02cccfc0d96c346f619d73184e4216`. Source-bound post-download independent model-free verifier: `PASS_MODEL_FREE_REPEATABILITY_EXPORT_VERIFICATION`, 16,384 ordered rows, 8,192 source cases, frozen source SHA `00a7a0089afffb66f2f32903bad94a5a2ea842841defb2d78e0686b0a5eb9ab9`, original archive hash, all ZIP entries and analysis reproduction.
- R2 receipt SHA: `f55e1b0271918538c16d347a1e91b0aeeece47acb84aa4314f3cc3169e45b4a2`; runtime record SHA `82f71fca47d41eb4f9d94243fa06ce78f7ee94ae1d1d821b9405e33b18a4e766`; physical record SHA `d21e9241b8ce1373b09ce4be2655a5a2cad8769b8d3a63bc59af8d02cca21f60`. Downloaded live-source wrapper SHA `d362eaa5e725e4a964d1b1cd9cb01260ba85674f29e496cddb8dc58e101132fd` is byte-equivalent to the committed atomic script after its three admission/header lines.
- R1 was independently retrieved/verified/preserved from earlier Kaggle kernel `abdulazizshehri/commandmed-v5-base-repeatability-r1` version 1 at scientific commit `e1b166ca88b1bd649e2a736e817603ec714b7192`; its original archive is `dfb35b0216369bbb87bcec75c5715df974bb9f736c0db0af98148cea91d99dac`. R1 and R2 have distinct Kaggle kernel identities and source Git heads; neither repeat was relaunched. Both used the same prospectively specified `repeat_rng_seed=991`, identical frozen model/inputs and closely matched runtime conditions. This is same-configuration repeatability, **not** between-seed, between-family or cross-device robustness.

## Frozen paired estimator results

The prospectively frozen absolute per-source-task difference, splitwise nearest-rank 95th percentile and maximum across DEV_EVAL/CAL_EVAL were applied using only the two **separately verified** archived development matrices. There are 3,840 DEV and 3,840 CAL source-task clusters (7,680 total); training and calibration-tuning cases do not enter the percentile. Corrected input-integrity guard from separate [PR #321](https://github.com/TheHalfMoon/commandMed/pull/321) was applied **only for strict run-label admission**; estimator mathematics remain unchanged.

Every one of the 16,384 ordered response rows is exactly equal between the two runs, including their logits. The distinct matrices differ in the top-level repeat metadata (R1=1, R2=2); this equality is independently testable and must not be misread as duplicated execution. R1 and R2 source identities and kernel provenance are separately verified.

| Property | DEV nearest-rank q95 | CAL nearest-rank q95 | `repeatability95` |
| --- | ---: | ---: | ---: |
| canonical accuracy | 0 | 0 | 0 |
| canonical NLL | 0 | 0 | 0 |
| canonical Brier | 0 | 0 | 0 |
| semantic JS | 0 | 0 | 0 |
| transformed accuracy (secondary) | 0 | 0 | 0 |
| transformed NLL (secondary) | 0 | 0 | 0 |
| transformed Brier (secondary) | 0 | 0 | 0 |

Paired estimator source SHA: `f6ace697d61de05c470c1260dafc7b54f13524b0dd2960e45c268c46bb7e64be`; interpretation is **unchanged-base same-seed numerical repeatability under the tested configuration only**. It is **not** a positive model quality, clinical safety, intervention efficacy, independent-family replication, or equivalence result.

The model remains near chance on frozen development rule-conformance: R2 DEV canonical accuracy `0.48125`, NLL `0.7831774818054636`, Brier `0.5799630568176445`; CAL canonical accuracy `0.49322916666666666`, NLL `0.7744336625615333`, Brier `0.5720342460601971`. Zero computational jitter cannot repair these negative scientific findings.

## Prospectively frozen research-scale effect margins

The separate nonclinical scale floors at `V5_DOMAIN_FLOOR_FREEZE_2026-10-09.md` were frozen **before** R1 output. Applying only the prescribed `m_j=max(domain_floor_j,2*repeatability95_j)` gives:

| Primary metric | Frozen native-unit benchmark floor | Two times repeatability95 | Calculated research-scale margin |
| --- | ---: | ---: | ---: |
| canonical accuracy | 0.01 | 0 | **0.01** |
| canonical NLL (nats) | 0.009950330853168092 | 0 | **0.009950330853168092** |
| canonical Brier | 0.02 | 0 | **0.02** |
| semantic JS (nats) | 0.006931471805599453 | 0 | **0.006931471805599453** |

Machine-readable calculations: `artifacts/v5/development/s1-kaggle-repeatability-runs/final-development-benchmark-margins-2026-10-09.json`, SHA `361ad34e0c2deb0ca7646cfb9dd9346bb63471296a003e9ef12a858743f6917f`. These are study-defined methodological effect margins, **NOT clinical safety/utility tolerances**. The zero repeatability term does not authorize zero-width equivalence or imply useful model performance.

## Fail-closed remaining gates

The final Holm conservative power plan **is not complete**: the numerically justified intervention-paired source-cluster SDs (for each declared non-target cell) and a prospectively bound exact size of the primary non-target hypothesis family have not been qualified here. No power value, adequacy conclusion or confirmatory generation is inferred. Further constructs (selective risk/coverage, narrow retention, coherence and clinical utility) receive no invented primary margins. The published paper/research program remains unproven.

No new model call, optimizer, duplicate R2, confirmatory/reserve identity, paid GPU/API, PHI or release. PR #320 and PR #321 remain DRAFT/UNMERGED. Evidence on this separate successor branch is subject to exact-head tests and review; no commit signing/review gate is claimed until genuinely satisfied.
