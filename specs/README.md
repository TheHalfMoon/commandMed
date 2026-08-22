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
| 000 | Program Charter | `CLOSED_CANONICAL` | — | Planning package canonical at `b0398f2fe514bd3ccd339908d739aef61055f929`; closure evidence in `specs/000-program-charter/closeout.md`. State becomes effective when this closure-only PR is merged and canonical main is verified. |
| 001 | Evaluation Charter | `ACTIVE` (Implementation candidate under review) | 000 | Implementation complete on feature branch; pending canonical review and post-merge closure PR. T001-T010 executed offline with zero model/training runs. Candidate evidence in `specs/001-eval-charter/closeout.md`. |
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

## Spec 000 closure rule

The `CLOSED_CANONICAL` state above is a state transition carried by the dedicated closure-only PR. It becomes effective only when that PR is merged to canonical `main` and the resulting GitHub merge SHA is immediately verified as live main.

The closeout file is bound to the already-known planning-package merge and canonical artifact blobs. The closure PR's own future merge SHA is represented by GitHub's canonical merge record; a recursive third PR is not required solely to rewrite that SHA into repository text.

## Spec 001 staged authority

Spec 001 deliberately starts with a narrow bootstrap gate:

1. after Spec 000 closure becomes effective, T001 alone is authorized;
2. T001 initializes Spec Kit `agy` from immutable source commit `489a3d51d152fa160d88d86781a924e99c4af832`, records bootstrap source/environment/dependency evidence, reconciles generated changes, and runs planning analysis;
3. if T001 acceptance passes with no material contradiction, T002–T010 may proceed in their declared dependency order;
4. failure of T001 is a hard stop, not permission to bypass Spec Kit or overwrite canonical planning files.

## Planning rule

Do not generate detailed implementation plans for blocked future specs merely to make the repository look complete. Add detail when the dependency frontier reaches that spec.

## Branch/PR rule

Prefer one bounded spec per implementation branch/PR. A spec's merged closeout evidence, not mere code existence, is what unblocks the next spec.

## Training authority

**No spec currently authorizes training or model execution.** Spec 001 T001 is the next bounded authority only after Spec 000 closure becomes effective, and it is governance/bootstrap analysis only.
