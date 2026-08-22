# commandMed Spec Registry

This directory is the dependency-ordered **spec-of-specs** for commandMed.

The roadmap is not execution authority. Only one bounded spec becomes active at a time, and every spec must prove its exit conditions before a dependent spec may begin.

## State legend

- `CANONICAL_PLANNING` — definition is frozen enough to govern later work; not necessarily executable.
- `AUTHORIZED_TO_SPECIFY` — specification-stage work may begin; does not authorize clarification, planning, implementation, execution, model/weight/data access, or later lifecycle stages.
- `AUTHORIZED_TO_START` — may be implemented under its bounded scope.
- `ACTIVE` — implementation/reconciliation in progress.
- `CLOSED_CANONICAL` — acceptance evidence is complete and merged canonically.
- `BLOCKED` — dependency/decision/gate prevents start.
- `DEFERRED` — intentionally outside the present execution horizon.

## Registry

| ID | Name | State | Depends on | Notes |
|---|---|---|---|---|
| 000 | Program Charter | `CLOSED_CANONICAL` | — | Planning package canonical at `b0398f2fe514bd3ccd339908d739aef61055f929`; closure evidence in `specs/000-program-charter/closeout.md`. |
| 001 | Evaluation Charter | `CLOSED_CANONICAL` | 000 | Implementation merge `531343f785a6430036cbb2770d0504676514b9a7`; closure merge `cc02b0d99d67e5a720502953c99307c8b991720d`. |
| 002 | Safety Gates | `CLOSED_CANONICAL` | 001 | Implementation merge `b637382fd9a0d8a02f71c11073a5276d61726bb6`; dedicated closure records final 54/9/157 exact-head qualification. |
| 003 | Data, License & Provenance | `CLOSED_CANONICAL` | 001 | Qualified implementation merge `a5fef84f9f0cee12dcd2ea6735888faee43db1ec`, tree `d7b2e11a8470ec66f50f1cff77bba4dddff20812`; final exact-head evidence: 71 focused / 9 hard-gate / 228 full tests and independent review with no material blocker. |
| 004 | Tournament Harness | `CLOSED_CANONICAL` | 001, 002, 003 | Effective only after this dedicated closure-only transition is independently reviewed, guarded-merged, and resulting canonical `main` is verified. Qualified implementation merge `9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d`, tree `7e37fa626f825ee25271e0bf21a627a2e64e49da`; exact implementation head `cf6158ea4193aa7db895607c6fac5a3a1442f708`; final 48 focused / 9 hard-gate / 276 full tests. Fixture/precomputed-results-only; no model or benchmark-payload execution authority. |
| 005 | Base Model Tournament | `AUTHORIZED_TO_SPECIFY` | 004 `CLOSED_CANONICAL` + `FD-001`/`FD-002`/`FD-006` `LOCKED` | Founder decisions canonical at `a68d37acd713049694106e81dc134ccf4d51feb9`. Specification-stage only; baseline-only/no training. No model execution, weight access, benchmark-payload execution, private-Gold access, provider generation, PHI access, or gated-asset access. |
| 006 | Patient Safety Scaffold & Deterministic Tools | `BLOCKED` | 002, 005 | Defense-in-depth interaction/tool boundary. |
| 007 | SFT V1 | `BLOCKED` | 003, 005, 006 | Three-class high-quality SFT. |
| 008 | Knowledge Strategy Ablation | `BLOCKED` | 007 | CPT vs no-CPT/distillation+retrieval. |
| 009 | Distillation V1 | `BLOCKED` | 008 | Minimum license-clean distillation; on-policy candidate. |
| 010 | RLVR V1 | `BLOCKED` | 009 | Verifiable tasks only; optional NO-GO outcome. |
| 011 | Calibration & Abstention | `BLOCKED` | relevant trained candidate | Selective risk and behavioral-state hardening. |
| 012 | Quantization & Device | `BLOCKED` | 011 | Medical re-gating on exact device/builds. |
| 013 | Arabic Deepening | `BLOCKED` | 007 + Arabic evaluation readiness | Fix measured Arabic gaps. |
| 014 | Multimodal Documents & Labs | `BLOCKED` | 004–006 | Unified-vs-structured perception falsification. |
| 015 | Human Evaluation | `BLOCKED` | patient/professional candidate + safety readiness | Patient comprehension and human+AI evidence. |
| 016 | Advanced Modality Adapters | `DEFERRED` | separate modality prerequisites | ECG, wearables, imaging volumes, WSI, audio/video etc. |
| 017 | Release Review & Paper | `BLOCKED` | all claimed capabilities | Independent review and claims package. |

## Spec 004 canonical closure record

Spec 004 has a qualified fixture/precomputed-results-only implementation canonically merged through [PR #28](https://github.com/TheHalfMoon/commandMed/pull/28):

```text
IMPLEMENTATION_MERGE=9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d
IMPLEMENTATION_TREE=7e37fa626f825ee25271e0bf21a627a2e64e49da
FINAL_REVIEWED_HEAD=cf6158ea4193aa7db895607c6fac5a3a1442f708
FINAL_VALIDATION_RUN=32603944702
FINAL_VALIDATION_JOB=97106155513
FOCUSED_SPEC004_TESTS=48/48 PASS
INHERITED_HARD_GATES=9/9 PASS
FULL_OFFLINE_SUITE=276/276 PASS
```

Direct implementation evidence:

- [GitHub Actions Run 32603944702](https://github.com/TheHalfMoon/commandMed/actions/runs/32603944702)
- [GitHub Actions Job 97106155513](https://github.com/TheHalfMoon/commandMed/actions/runs/32603944702/job/97106155513)
- [Fresh exact-head Qodo review result](https://github.com/TheHalfMoon/commandMed/pull/28#issuecomment-5383054440)
- [Qodo review update marker through exact `cf6158ea...`](https://github.com/TheHalfMoon/commandMed/pull/28#issuecomment-5383058920)

The fresh exact-head review reported no material correctness, security, scientific-integrity, lifecycle, authorization, deterministic-reporting, or execution-surface blocker. The guarded implementation merge used that exact head, after which canonical `main` was verified at `9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d` / tree `7e37fa626f825ee25271e0bf21a627a2e64e49da`. Temporary validation carrier PR #29 was closed without merge after evidence capture.

## Spec 004 dedicated closure transition

The implementation merge alone did not close Spec 004. This dedicated closure-only transition reconciles the complete lifecycle set:

- `specs/004-tournament-harness/closeout.md`
- `specs/004-tournament-harness/tasks.md`
- `specs/004-tournament-harness/review-reconciliation.md`
- `specs/004-tournament-harness/checklists/requirements.md`
- `specs/README.md`

The first closure candidate head `45037b988bd716adc1750199df6c6069ff15f5ac` was rejected as closure authority after [Qodo closure review](https://github.com/TheHalfMoon/commandMed/pull/30#issuecomment-5383104852) found:

```text
C004-01 NONCANONICAL_CLOSEOUT_STATUS
C004-02 STALE_SPEC004_LIFECYCLE_ARTIFACTS
C004-03 UNLINKED_CI_REVIEW_EVIDENCE
```

This repaired closure transition:

- uses the canonical `CLOSED_CANONICAL` status pattern with post-merge effectiveness qualifier;
- reconciles all five lifecycle/governance documents rather than only closeout/registry;
- links the exact Run, Job, implementation PR, exact-head review result, review update marker, and first closure review directly;
- introduces no source, test, data, dependency, workflow, runtime, execution, model, provider, credential, or authorization changes; and
- keeps Spec 005 explicitly `BLOCKED`.

Because the C004 repairs changed repository content, the first closure review is historical only. `CLOSED_CANONICAL` for Spec 004 becomes effective only after the repaired exact closure head receives a new fresh independent review with no material blocker, is guarded-merged unchanged, and the resulting canonical `main` plus lifecycle files are verified.

## Spec 005 specification boundary

Founder decisions `FD-001`, `FD-002`, and `FD-006` were canonically locked by PR #32 / merge `a68d37acd713049694106e81dc134ccf4d51feb9`. The dependency and founder-decision prerequisites for the **specify stage** are therefore satisfied.

Spec 005 is `AUTHORIZED_TO_SPECIFY` only. Its specification may define the tournament problem, inherited contracts, admission/comparability rules, fail-closed behavior, and questions that clarification must resolve. It must not freeze or execute a live tournament merely by naming candidate families.

Successful canonical definition of `specs/005-base-model-tournament/spec.md` advances only to a separately authorized clarification step.

## Planning rule

Do not generate detailed implementation plans for blocked future specs merely to make the repository look complete. Add detail only when the dependency frontier reaches that spec and explicit authorization exists.

## Branch/PR rule

Prefer one bounded spec per implementation branch/PR. A spec's merged closeout evidence, not mere code existence, is what can satisfy its dependency edge. Satisfying a dependency does not itself grant start authority to the dependent spec when separate founder decisions or explicit authorization are required.

## Execution and training authority

**No spec currently authorizes training, model execution, model-weight access, benchmark payload execution, or real-model tournament execution.**

```text
SPEC_005=AUTHORIZED_TO_SPECIFY
SPEC_005_LIFECYCLE_AUTHORITY=SPECIFY_ONLY
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AGAINST_MODELS=NONE
TRAINING_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
PHI_RESTRICTED_DATA_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_PAYLOAD_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
```
