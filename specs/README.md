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
| 004 | Tournament Harness | `AUTHORIZED_TO_START` | 001, 002, 003 | Fixture-only harness lifecycle may begin; no model or benchmark-payload execution authority is granted. |
| 005 | Base Model Tournament | `BLOCKED` | 004 + required founder license/device decisions | Baseline-only tournament; no training. |
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

## Current execution frontier — Spec 004 authorization

Spec 003 — Data, License & Provenance — is canonically implemented through merge `a5fef84f9f0cee12dcd2ea6735888faee43db1ec`, with implementation tree `d7b2e11a8470ec66f50f1cff77bba4dddff20812`. Its dedicated closure evidence is recorded in `specs/003-data-license-provenance/closeout.md`.

Upon merge of the dedicated Spec 003 closure-only PR and verification of resulting canonical `main`, Spec 003 is `CLOSED_CANONICAL` and Spec 004 — Tournament Harness — is `AUTHORIZED_TO_START` under its own bounded Spec Kit lifecycle.

Spec 004 implementation remains `NOT_STARTED` until explicitly initiated. Its authorization is fixture-only and does not grant model execution, model-weight access, benchmark payload execution, tournament execution against candidate models, provider/API generation, PHI/restricted-data access, private-Gold payload access, gated-asset access, or training.

## Spec 003 closure rule

The Spec 003 implementation merge alone did not close the spec. This dedicated closure-only transition binds the final reviewed implementation head, exact-head GitHub qualification, independent review, canonical implementation merge `a5fef84f9f0cee12dcd2ea6735888faee43db1ec`, and canonical tree `d7b2e11a8470ec66f50f1cff77bba4dddff20812`.

`CLOSED_CANONICAL` for Spec 003 and `AUTHORIZED_TO_START` for Spec 004 become effective only after the closure PR is reviewed, merged, and resulting canonical `main` is verified.

## Planning rule

Do not generate detailed implementation plans for blocked future specs merely to make the repository look complete. Add detail when the dependency frontier reaches that spec.

## Branch/PR rule

Prefer one bounded spec per implementation branch/PR. A spec's merged closeout evidence, not mere code existence, is what unblocks the next spec.

## Execution and training authority

**No spec currently authorizes training, model execution, model-weight access, or benchmark payload execution.**

Spec 004 is authorized only to start its bounded fixture-only harness lifecycle after the Spec 003 closure transition becomes canonical. Any later execution authority requires a separate explicit bounded authorization after its prerequisites are proven.