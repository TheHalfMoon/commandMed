# commandMed Spec Registry

This directory is the dependency-ordered **spec-of-specs** for commandMed.

The roadmap is not execution authority. Only one bounded spec becomes active at a time, and every spec must prove its exit conditions before a dependent spec may begin.

## State legend

- `CANONICAL_PLANNING` — definition is frozen enough to govern later work; not necessarily executable.
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
| 004 | Tournament Harness | `CLOSED_CANONICAL` | 001, 002, 003 | Effective only after this dedicated closure-only transition is reviewed, merged, and canonical `main` is verified. Qualified implementation merge `9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d`, tree `7e37fa626f825ee25271e0bf21a627a2e64e49da`; exact implementation head `cf6158ea4193aa7db895607c6fac5a3a1442f708`; final 48 focused / 9 hard-gate / 276 full tests and fresh independent review with no material blocker. Fixture/precomputed-results-only; no model or benchmark-payload execution authority. |
| 005 | Base Model Tournament | `BLOCKED` | 004 + required founder license/device decisions | Spec 004 closure alone does not authorize start. Baseline-only tournament; no training. Separate founder prerequisites and explicit authorization remain required. |
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

## Current execution frontier — Spec 004 canonical closure

Spec 004 — Tournament Harness — has a qualified fixture/precomputed-results-only implementation canonically merged through PR #28 at:

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

Fresh independent exact-head review found no material correctness, security, scientific-integrity, lifecycle, authorization, deterministic-reporting, or execution-surface blocker. All material inline review threads were resolved before the guarded squash merge. Temporary validation carrier PR #29 was closed without merge after canonical implementation evidence was captured.

This dedicated closure-only transition binds that already-canonical implementation evidence. The `CLOSED_CANONICAL` row for Spec 004 becomes effective only after the exact closure head is independently reviewed, guarded-merged, and the resulting canonical `main` plus lifecycle files are verified.

Spec 005 remains `BLOCKED`. Spec 004 closure does not satisfy Spec 005's separate founder license/device decisions and does not constitute explicit Spec 005 start authorization.

## Spec 004 closure rule

The Spec 004 implementation merge alone did not close the spec. The dedicated closure-only transition must contain lifecycle/documentation changes only and must bind:

- canonical implementation merge `9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d`;
- canonical implementation tree `7e37fa626f825ee25271e0bf21a627a2e64e49da`;
- final reviewed implementation head `cf6158ea4193aa7db895607c6fac5a3a1442f708`;
- exact-head GitHub qualification Run `32603944702` / Job `97106155513`;
- fresh independent exact-head review with no material blocker; and
- the unchanged authority boundary preserving `SPEC_005=BLOCKED`.

`CLOSED_CANONICAL` for Spec 004 becomes effective only after this closure PR is reviewed, merged, and resulting canonical `main` is verified.

## Planning rule

Do not generate detailed implementation plans for blocked future specs merely to make the repository look complete. Add detail when the dependency frontier reaches that spec and explicit authorization exists.

## Branch/PR rule

Prefer one bounded spec per implementation branch/PR. A spec's merged closeout evidence, not mere code existence, is what can satisfy its dependency edge. Satisfying a dependency does not itself grant start authority to the dependent spec when separate founder decisions or explicit authorization are required.

## Execution and training authority

**No spec currently authorizes training, model execution, model-weight access, benchmark payload execution, or real-model tournament execution.**

Spec 004 is a fixture/precomputed-results-only harness and grants no such authority. Spec 005 remains blocked and may not begin until its separate prerequisites are resolved and explicit bounded authorization is granted.
