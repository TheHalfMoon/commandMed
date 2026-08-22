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
| 001 | Evaluation Charter | `CLOSED_CANONICAL` | 000 | Implementation squash-merged canonically as `531343f785a6430036cbb2770d0504676514b9a7`; exact-head evidence and closure record in `specs/001-eval-charter/closeout.md`. State becomes effective only when this closure-only PR is merged and canonical main is verified. |
| 002 | Safety Gates | `AUTHORIZED_TO_START` | 001 | Becomes effective only after this Spec 001 closure-only PR is merged and canonical main is verified. Bounded safety-gate work only; no model execution/training authority. |
| 003 | Data, License & Provenance | `BLOCKED` | 001 | Spec 001 planning dependency is satisfied by this closure, but implementation remains unactivated pending a separate explicit activation decision under the one-active-spec discipline. |
| 004 | Tournament Harness | `BLOCKED` | 001, 002, 003 | Fixture-only harness before model execution. |
| 005 | Base Model Tournament | `BLOCKED` | 004 + required founder license/device decisions | Baseline only; no training. |
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

## Spec 000 closure rule

The `CLOSED_CANONICAL` state for Spec 000 became effective through its dedicated closure-only PR and canonical-main verification. Its closeout file binds the already-known planning-package merge and canonical artifact blobs; the closure PR's own merge identity is GitHub's canonical merge record.

## Spec 001 closure authority

Spec 001 implementation was exact-head qualified and squash-merged canonically as `531343f785a6430036cbb2770d0504676514b9a7`. The `CLOSED_CANONICAL` transition above becomes effective only when the dedicated Spec 001 closure-only PR is merged and canonical `main` is immediately verified.

After that transition:

1. Spec 001 is closed; no further Spec 001 implementation authority exists except separately reviewed corrective maintenance.
2. Spec 002 alone becomes `AUTHORIZED_TO_START` under its bounded Safety Gates scope.
3. Spec 003's planning dependency on Spec 001 is satisfied, but Spec 003 implementation remains blocked until separately activated; this preserves the one-active-spec execution discipline.
4. Spec 004+ remain blocked by their declared dependencies.
5. No model execution or training authority is created by Spec 001 closure.

## Planning rule

Do not generate detailed implementation plans for blocked future specs merely to make the repository look complete. Add detail when the dependency frontier reaches that spec.

## Branch/PR rule

Prefer one bounded spec per implementation branch/PR. A spec's merged closeout evidence, not mere code existence, is what unblocks the next spec.

## Training authority

**No spec currently authorizes training or model execution.** After Spec 001 closure becomes effective, Spec 002 is the next bounded implementation authority and is limited to Safety Gates work under its own contract.