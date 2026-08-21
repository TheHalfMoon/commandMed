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

## Founder decisions required

### FD-001 — Release/licensing posture

**State:** FOUNDER_REQUIRED
**Needed before:** final candidate lineage selection / any incompatible training data use

Choose intended posture among possibilities such as:

- open weights with permissive downstream use;
- open weights under a responsible-use/custom license;
- research weights only;
- commercial product with or without public weights.

This decision controls acceptable base-model/data/teacher licenses.

### FD-002 — Target device tier

**State:** FOUNDER_REQUIRED
**Needed before:** final tournament qualification thresholds

Choose whether V1 must support:

- flagship phones only;
- flagship + modern midrange phones;
- broader constrained/mobile baseline.

The decision sets package/peak-RAM/latency/thermal budgets.

### FD-003 — Human/clinician evaluation budget

**State:** FOUNDER_REQUIRED
**Needed before:** final Gold construction and patient release evidence

Set a real budget/access strategy for clinician adjudication, Arabic clinical review, and human-factor testing. If the budget is unavailable, narrow the claims rather than simulating authority.

### FD-004 — Acceptable over-triage policy

**State:** FOUNDER_REQUIRED
**Needed before:** patient release gate freeze

Set the product/ethics tradeoff for escalation on clearly benign cases while preserving required emergency sensitivity. Exact thresholds require evidence and clinical governance, but the acceptable product posture is an owner decision.

### FD-005 — Failed-mode release policy

**State:** FOUNDER_REQUIRED
**Needed before:** release review

If one major mode fails a hard gate while others pass, decide whether to:

- disable the failing mode and release a narrower system;
- delay the entire release.

No hidden downgrade is allowed.

### FD-006 — Donor-origin restrictions

**State:** FOUNDER_REQUIRED
**Needed before:** tournament freeze if restrictions are desired

Decide whether commandMed inherits any model-origin restrictions from related research programs. Do not infer them automatically.

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
