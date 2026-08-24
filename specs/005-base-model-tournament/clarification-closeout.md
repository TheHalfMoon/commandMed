# Spec 005 — Clarification Closeout

**Status:** `CLARIFICATION_COMPLETE_READY_FOR_PLAN`
**Feature:** `005-base-model-tournament`
**Recorded on:** 2026-08-24
**Planning authority:** explicitly granted by the founder request to finish the Spec Kit plan and make it implementation-ready for JetBrains.

## 1. Lifecycle transition

Bounded clarification Sessions 1–14 are complete. Their accepted artifacts and `spec.md` are the frozen design input for planning.

```text
CLARIFICATION_LIFECYCLE=COMPLETE
NEXT_LIFECYCLE_STEP=PLAN
PLAN_AUTHORITY=AUTHORIZED_FOR_SPEC_KIT_PLANNING_ARTIFACTS
IMPLEMENTATION_AUTHORITY=NOT_GRANTED_BY_THIS_CLOSEOUT
```

This closeout authorizes only creation and reconciliation of Spec Kit planning artifacts (`research.md`, `plan.md`, `data-model.md`, `contracts/`, `quickstart.md`, requirements checklist, `tasks.md`, analysis, and implementation handoff). It does not authorize execution work that remains separately gated.

## 2. What is resolved

Planning must treat the following as frozen architecture, not open questions:

- common-core, base-only primary ranking;
- fully admitted primary candidates only;
- quality-floor-then-size-first ranking;
- dual reference/deployable evidence paths;
- sub-700 MiB mass-reach boundary with named device classes;
- GGUF/llama.cpp canonical deployable path with immutable runtime identity;
- 8K core / 16K stress, Q8_0 symmetric KV, fixed prompt/generation budgets, cold/no-cache measured runs;
- platform-native memory, timing, thermal and energy evidence semantics;
- five-fresh-run aggregation and fail-closed run semantics;
- noncompensable multi-lane medical quality architecture;
- intended-use, stratification, estimand-first statistics and paired Arabic parity architecture;
- independent clinical/statistical threshold governance;
- selection-safe non-Gold Arabic source architecture and five Arabic coverage anchors;
- contributor rights, non-PHI authoring, independent bilingual review, provenance, contamination and change-control architecture;
- personnel qualification/nonexposure/governance architecture;
- payload/result access firewall;
- spend/engagement authorization architecture;
- dependency-ordered preconstruction gates A1–A15.

## 3. Remaining unknowns are evidence inputs, not clarification debt

The following remain intentionally unresolved until their prerequisite evidence exists:

- exact metrics-v2 canonical identity until A1 corrective maintenance is implemented and merged;
- exact clinical thresholds/margins and per-stratum sample counts until the required scientific evidence and qualified review exist;
- exact selection-safe Arabic suite identities/case content until A1–A14 operational prerequisites pass and A15 separately activates construction;
- exact personnel roster and protected evidence until A7 is separately executed;
- exact storage/vendor/payment details until their separate gates require and authorize them;
- exact llama.cpp commit, platform build identities, OS/tool/signal identities and candidate artifacts until a later execution activation permits binding;
- actual contamination results until a frozen suite exists and assessment execution is separately authorized;
- any model, benchmark, device, provider, Gold, PHI, payment or tournament execution.

These items MUST be represented in implementation as explicit fail-closed prerequisite/evidence records. They MUST NOT be guessed, silently defaulted, or converted into permissive placeholders.

```text
UNRESOLVED_EVIDENCE_INPUT_EQUALS_NEEDS_CLARIFICATION=NO
UNRESOLVED_EVIDENCE_INPUT_EQUALS_FAIL_CLOSED_PREREQUISITE=YES
```

## 4. Hard implementation boundaries retained

Planning and implementation scaffolding must preserve:

```text
CURRENT_AUTHORIZED_SPEND_USD=0
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
A15_CONSTRUCTION_ACTIVATION_AUTHORITY=NONE
```

The planning package may implement validators, schemas, deterministic state machines, synthetic fixtures and offline tests for these gates. It may not perform the gated action itself.

## 5. Planning rule for JetBrains

The implementation plan MUST convert the clarification archive into a short dependency-ordered execution path. `tasks.md` becomes the authoritative implementation queue for the coding agent. Individual historical clarification files remain evidence/rationale and should not be treated as separate coding tasks.

A1 metrics-v2 corrective maintenance remains a mandatory separate branch/PR from canonical `main` and must land before Spec 005 code consumes metrics-v2.

After planning artifacts and requirements checklist are complete, run Spec Kit Analyze read-only. Implementation may start only when cross-artifact analysis has no unresolved CRITICAL/HIGH contradiction or missing hard requirement.