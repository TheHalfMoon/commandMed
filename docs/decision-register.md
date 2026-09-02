# commandMed Decision Register

**Status:** ACTIVE
**Baseline:** Grand Master Plan v0.1 — 2026-08-21

This register separates evidence-resolvable questions from true founder decisions. Do not ask for a founder decision earlier than the dependency requires it.

## Decision states

- `LOCKED` — planning decision is currently canonical.
- `TEST_BEFORE_LOCK` — empirical evidence must decide.
- `FOUNDER_REQUIRED` — value/product/ownership choice cannot be responsibly derived from evidence alone.
- `DEFERRED` — intentionally not needed yet.

## Locked decisions

### D-001 — Evaluation precedes training

**State:** LOCKED

No optimization run may precede a frozen evaluation contract capable of judging it.

### D-002 — Resource-based definition of small

**State:** LOCKED

Model size claims use installed bytes, peak RAM, context/KV memory, latency, energy and thermal measurements on named devices. Parameter count is descriptive only.

### D-003 — Three training behavior classes

**State:** LOCKED

Use `PATIENT_CAREGIVER`, `CLINICAL_PROFESSIONAL`, and `LEARNER_RESEARCHER` unless evidence later proves finer routing is required. Preserve role-specific evaluation slices.

### D-004 — Hybrid system architecture

**State:** LOCKED

commandMed may combine a compact shared reasoning core with specialized perception/signal modules and deterministic tools. "One product" does not require "one neural network."

### D-005 — Three private Gold families

**State:** LOCKED

Use `COMMANDMED_CLINICAL_GOLD`, `COMMANDMED_ARABIC_GOLD`, and `COMMANDMED_MULTIMODAL_GOLD`. Device performance uses a separate evidence pack.

### D-006 — MedGemma training-output default

**State:** LOCKED until explicit override

MedGemma/HAI-DEF assets are reference/evaluation-only. Do not use their outputs to train commandMed unless an explicit lineage/license decision authorizes it.

### D-007 — LFM candidate status

**State:** LOCKED until license decision

LFM models may be researched but are conditional-license candidates. Do not lock the commercial lineage to LFM until intended use is confirmed compatible or a separate license is obtained.

### D-008 — RL truth boundary

**State:** LOCKED

RLVR/GRPO is restricted to tasks with defensible reward correctness. LLM judges cannot be the sole authority for medical truth.

### D-009 — CPT is conditional

**State:** LOCKED

Medical continued pretraining must compete against a cheaper no-CPT/distillation+retrieval strategy under pre-registered evaluation.

### D-010 — Patient human evaluation

**State:** LOCKED

Patient-facing benefit/safety claims require human evidence in addition to model-only evaluation.

## Test before lock

### T-001 — Core/backbone winner

**State:** TEST_BEFORE_LOCK
**Due before:** Spec 006/007 lineage lock

Decide through the frozen model tournament, not preference.

### T-002 — Unified vs structured document perception

**State:** TEST_BEFORE_LOCK

Compare end-to-end compact VLM against `perception/OCR -> typed extraction -> deterministic validation -> reasoning` under equivalent resource and quality constraints.

### T-003 — CPT value

**State:** TEST_BEFORE_LOCK

Run pre-registered CPT-vs-null ablation. If CPT does not justify its cost/regression risk, do not do it.

### T-004 — Distillation complexity

**State:** TEST_BEFORE_LOCK

Begin with minimum license-clean teacher strategy; add specialized/multiple teachers only for measured gaps.

### T-005 — DPO necessity

**State:** TEST_BEFORE_LOCK

Do not schedule DPO as ceremony. Use it only if a measurable preference/alignment deficit remains.

### T-006 — Quantization floor

**State:** TEST_BEFORE_LOCK

Q4 is not automatically final and Q2/Q3 are not automatically acceptable. Medical equivalence gates determine the floor.

### T-007 — Runtime stack

**State:** TEST_BEFORE_LOCK

Choose the minimum runtime set needed by the winning architecture and named device matrix.

## Founder decisions

### FD-001 — Release/licensing posture

**State:** LOCKED
**Founder decision:** `OPEN_WEIGHTS_PERMISSIVE_DOWNSTREAM_USE`
**Decision date:** 2026-08-23
**Needed before:** final candidate lineage selection / any incompatible training data use

Intent:

- prefer an Apache-2.0-compatible release lineage where legally supportable;
- preserve commercial downstream use where the complete base/data/teacher lineage permits it;
- preserve public weight redistribution where the complete lineage permits it;
- keep custom/restrictive-license candidates research-only or conditional until exact intended-use compatibility is proven;
- do not select a final release lineage whose obligations conflict with this posture without a separate explicit founder override.

This decision sets the intended release posture. Exact base-model, dataset, teacher, and derivative-license compatibility remains an evidence-gated provenance question and must be proven before irreversible use or final selection.

### FD-002 — Target device tier

**State:** LOCKED
**Founder decision:** `FLAGSHIP_PLUS_MODERN_MIDRANGE`
**Decision date:** 2026-08-23
**Needed before:** final tournament qualification thresholds

Intent:

- V1 tournament qualification must cover both flagship and modern midrange phones;
- Spec 005 must freeze exact named-device/resource classes and package, peak-RAM, latency, energy, and thermal thresholds before any live tournament execution;
- do not prematurely require a broader constrained/mobile baseline;
- parameter count alone is not evidence of device fit.

This decision fixes the target device tier but does not itself define numeric qualification thresholds; those thresholds remain a Spec 005 specification/clarification task and require evidence before execution.

### FD-003 — Human/clinician evaluation budget

**State:** FOUNDER_REQUIRED
**Needed before:** final Gold construction and patient release evidence

Set a real budget/access strategy for clinician adjudication, Arabic clinical review, and human-factor testing. If the budget is unavailable, narrow the claims rather than simulating authority.

### FD-004 — Acceptable over-triage policy

**State:** LOCKED
**Founder decision:** `BALANCED_BURDEN_WITH_NONCOMPENSABLE_SAFETY`
**Decision ID:** `FD004_DECISION_B`
**Decision date:** 2026-08-28
**Needed before:** patient release gate freeze

Intent:

- reduce unnecessary escalation burden only after frozen noncompensable safety gates are satisfied;
- require benign over-triage burden to be measured and bounded;
- never allow convenience, engagement, average utility, or lower over-triage to compensate for a safety-gate failure;
- require qualified clinical/statistical evidence before any numeric benign over-triage ceiling is proposed or frozen.

This decision fixes the product/ethics posture only. It does not select a numeric threshold, satisfy `T1_A2`, complete E004, advance E005, authorize model conversion or contamination assessment, activate A15, authorize training or external reviewer outreach, or authorize spend.

### FD-005 — Failed-mode release policy

**State:** FOUNDER_REQUIRED
**Needed before:** release review

If one major mode fails a hard gate while others pass, decide whether to:

- disable the failing mode and release a narrower system;
- delay the entire release.

No hidden downgrade is allowed.

### FD-006 — Donor-origin restrictions

**State:** LOCKED
**Founder decision:** `NOT_INVOKED`
**Decision date:** 2026-08-23
**Needed before:** tournament freeze if restrictions are desired

commandMed does not automatically inherit model-origin restrictions from related research programs. Candidate eligibility is governed by commandMed's own frozen evaluation, provenance, safety, licensing, device, and authorization contracts. Any future donor-origin restriction requires a separate explicit founder decision.

### FD-007 — Repository independent review policy

**State:** LOCKED
**Founder decision:** `REMOVE_MANDATORY_INDEPENDENT_REPOSITORY_REVIEW_GATE`
**Decision date:** 2026-09-02
**Needed before:** prospective repository/PR qualification and merge decisions

Intent:

- independent repository review, bot review, peer review, exact-head review, and reviewer `MATERIAL_BLOCKER=NO` are optional by default rather than universal PR/merge gates;
- deterministic validation, evidence-dependent gates, bounded authority, exact identity checks, CI/status checks, branch/ruleset requirements, and unresolved-thread reconciliation remain required where applicable;
- historical review evidence remains valid and is not rewritten;
- a later bounded authority may explicitly reintroduce a repository reviewer for a specifically named task;
- domain-qualified human evidence that is itself required for scientific, clinical, statistical, privacy, rights, governance, or human-factor validity is unaffected unless separately amended.

The constitutional amendment record is `docs/repository-review-gate-amendment-2026-09-02.md`.

This decision creates no model/weight access, conversion, inference, benchmark, contamination, A15, training, credential, protected-data, paid-compute, procurement/payment, or spend authority.

## Spec 005 entry consequence

The founder prerequisites needed to begin Spec 005 specification are satisfied by `FD-001`, `FD-002`, and `FD-006` above.

This permits **specification-stage work only** after these decisions are merged to canonical `main` and canonical state is verified. It does not by itself authorize live tournament execution or any asset access.

```text
SPEC_005_ENTRY_AFTER_CANONICAL_DECISION_MERGE=AUTHORIZED_TO_SPECIFY
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
```

## Deferred decisions

### DF-001 — Final public model naming

**State:** DEFERRED

Use neutral research candidate IDs until evidence identifies a release candidate.

### DF-002 — Voice/video product experience

**State:** DEFERRED

Architecture may preserve future interfaces, but UX/product commitments wait for the corresponding modality specs.

### DF-003 — One checkpoint vs multiple release tiers

**State:** DEFERRED

Do not pre-create Pocket/Clinical/Vision products until the tournament and device evidence demonstrate a real need.
