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

| ID | Name | State at v0.1 | Depends on | Notes |
|---|---|---|---|---|
| 000 | Program Charter | `CANONICAL_PLANNING` | — | Establishes mission, authority, constitution and roadmap. |
| 001 | Evaluation Charter | `AUTHORIZED_TO_START` after planning PR is canonical and Spec Kit bootstrap is reconciled | 000 | First executable spec. No models/inference/training. |
| 002 | Safety Gates | `BLOCKED` | 001 | Freeze hard safety and escalation/tool boundaries. |
| 003 | Data, License & Provenance | `BLOCKED` | 001 | Machine-verifiable lineage/data-use contract. |
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

## Planning rule

Do not generate detailed implementation plans for blocked future specs merely to make the repository look complete. Add detail when the dependency frontier reaches that spec.

## Branch/PR rule

Prefer one bounded spec per implementation branch/PR. A spec's merged closeout evidence, not mere code existence, is what unblocks the next spec.

## Training authority

At this registry baseline, **no spec authorizes training or model execution**. Spec 001 is the only intended next executable unit and is fixture-only.
