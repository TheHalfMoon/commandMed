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
| 003 | Data, License & Provenance | `AUTHORIZED_TO_START` | 001 | Spec 002 canonical closure clears the one-active-spec frontier; implementation remains `NOT_STARTED` until explicitly begun under Spec 003 scope. |
| 004 | Tournament Harness | `BLOCKED` | 001, 002, 003 | Fixture-only harness before any separately authorized model execution. |
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

## Current execution frontier — Spec 003 authorization

Spec 002 implementation is canonical at `b637382fd9a0d8a02f71c11073a5276d61726bb6` and its dedicated closure transition marks it `CLOSED_CANONICAL`.

Spec 003 — Data, License & Provenance — is therefore `AUTHORIZED_TO_START`, but implementation is still `NOT_STARTED` until explicitly initiated under its own bounded plan/review lifecycle. This transition does not authorize model execution, benchmark payload execution, PHI/restricted data access, real Gold access, or training.

## Spec 002 closure rule

The Spec 002 implementation merge alone did not close the spec. This dedicated closure-only change binds the qualified implementation evidence to canonical merge `b637382fd9a0d8a02f71c11073a5276d61726bb6`; `CLOSED_CANONICAL` becomes effective only after this closure PR is reviewed, merged, and resulting canonical `main` is verified.

## Planning rule

Do not generate detailed implementation plans for blocked future specs merely to make the repository look complete. Add detail when the dependency frontier reaches that spec.

## Branch/PR rule

Prefer one bounded spec per implementation branch/PR. A spec's merged closeout evidence, not mere code existence, is what unblocks the next spec.

## Training authority

**No spec currently authorizes training, model execution, or benchmark payload execution.** Spec 003 is only authorized to start its bounded governance work; implementation remains not started until explicitly initiated.
