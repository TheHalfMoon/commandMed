# Spec 001 — Evaluation Charter

**State:** `T001_AUTHORIZED_TO_START` only after Spec 000 is `CLOSED_CANONICAL`; T002–T010 remain blocked until T001 safely reconciles Spec Kit bootstrap and planning analysis has no material contradiction
**Training authority:** NONE
**Model execution authority:** NONE

## Authority boundary

After Spec 000 is `CLOSED_CANONICAL`, only **T001 — Reconcile Spec Kit bootstrap** is authorized. T001 owns the safe `agy` initialization/reconciliation and planning-consistency analysis. T002–T010 do not become executable until T001 passes its acceptance criteria on the active branch.

This avoids a circular prerequisite: Spec Kit reconciliation is the first bounded action inside Spec 001, not a prerequisite that must somehow occur outside Spec 001 authority.

## Problem

commandMed cannot honestly compare, train, compress, or release models until it has a deterministic and auditable contract defining what will be measured, which failures are disqualifying, how private evaluation remains quarantined, and how benchmark/data identities are verified.

Without this charter, every later improvement is vulnerable to benchmark drift, contamination, cherry-picking, judge artifacts, moving thresholds, and post-hoc success definitions.

## Goal

Create the minimum local, deterministic evaluation-governance foundation that can freeze later experiments without downloading/running any model.

## User stories

### US1 — Researcher verifies evaluation assets

As a commandMed researcher, I can inspect a canonical benchmark registry and determine for every registered suite whether its current existence, source, version/access class, role/modality coverage, intended use, and contamination risk have been explicitly recorded.

**Independent test:** validate the registry against local fixture entries and reject missing required fields/duplicate identities.

### US2 — Safety owner sees non-negotiable gates

As a safety owner, I can inspect a canonical metrics/gates catalog that distinguishes optimization metrics from hard safety gates and prevents a high mean score from masking a critical failure.

**Independent test:** fixture evaluation where the aggregate score is excellent but one critical gate fails must produce an overall non-pass state.

### US3 — Gold curator can design holdouts without exposing cases

As a future Gold curator, I can follow a metadata/protocol contract for the three protected Gold families without placing any actual Gold case content in this repository.

**Independent test:** protocol validation proves that Gold identities/access roles/power-analysis requirements are represented while case payload fields are forbidden from ordinary repository fixtures.

### US4 — Experiment owner can bind an evaluation snapshot

As an experiment owner, I can deterministically serialize the evaluation charter and compute a stable digest so a later run can prove exactly which evaluation contract judged it.

**Independent test:** equivalent logical input serialized twice produces byte-identical canonical output and the same digest; semantic mutation changes the digest.

### US5 — Reviewer can see quarantine and contamination rules

As an independent reviewer, I can verify that private Gold, public benchmarks, training data, teacher data, and selection data have explicit separation rules and that the registry records contamination risk instead of pretending it does not exist.

**Independent test:** fixtures with prohibited split/usage combinations fail validation.

## Functional requirements

### FR-001 — Benchmark registry contract

The implementation SHALL define a machine-readable registry contract containing at least:

- stable `benchmark_id`;
- canonical name;
- primary/canonical source reference;
- verification date;
- artifact/version identifier when available;
- access class: `PUBLIC`, `GATED`, `PRIVATE_EXTERNAL`, or `REFERENCE_ONLY`;
- license/use-status field;
- languages;
- roles/audiences;
- modalities;
- capability domains;
- contamination sensitivity;
- intended commandMed use: development/reference/possible-release-gate;
- verification status and notes.

Unknown/uncertain facts must be representable explicitly; they may not be silently guessed.

### FR-002 — Initial verified registry scope

The initial planning registry SHALL include, at minimum, entries or explicitly justified exclusions for:

- MedHELM;
- HealthBench;
- HealthBench Hard;
- HealthBench Consensus;
- HealthBench Professional;
- MedXpertQA text/multimodal;
- MedQA;
- MedMCQA;
- PubMedQA;
- MedQAbstain;
- MedAbstain.

The implementation may add other verified 2026 suites only if doing so does not expand into model evaluation.

### FR-003 — Metrics catalog

Define canonical metric categories including at minimum:

- medical correctness/utility;
- critical-error/safety;
- emergency sensitivity;
- benign-case over-triage;
- abstention/selective risk;
- calibration;
- evidence/citation fidelity;
- active information acquisition;
- patient comprehension/actionability;
- professional workflow correctness;
- Arabic/English gap;
- longitudinal robustness;
- multimodal extraction/interpretation;
- device/resource metrics.

Metrics may be marked `DEFINED_NOT_YET_THRESHOLD_FROZEN` where later clinical/founder evidence is required.

### FR-004 — Hard-gate semantics

The contract SHALL encode that a hard-gate failure yields overall `FAIL` regardless of aggregate/average metrics.

It SHALL support `PASS`, `FAIL`, `NOT_EVALUATED`, and where appropriate `BLOCKED`/`INSUFFICIENT_EVIDENCE` states without coercing unknown results to zero or pass.

### FR-005 — Gold protocol

Define metadata/protocol contracts for:

- `COMMANDMED_CLINICAL_GOLD`;
- `COMMANDMED_ARABIC_GOLD`;
- `COMMANDMED_MULTIMODAL_GOLD`.

For each family, record intended strata, reviewer/adjudication requirements, access-control intent, power-analysis requirement, allowed scoring events, and prohibited optimization uses.

No real Gold cases are created or stored in Spec 001.

### FR-006 — Quarantine contract

Explicitly prohibit private Gold content from CPT, SFT, teacher generation, distillation, DPO/RL, prompt tuning, hyperparameter tuning, checkpoint selection, and backbone selection.

Define distinct logical purposes for:

- training;
- development;
- calibration;
- selection;
- external public evaluation;
- private Gold/final evaluation.

### FR-007 — Contamination contract

Define metadata and validation rules for known/possible benchmark overlap. The contract SHALL distinguish exact-content identity from semantic contamination risk.

Spec 001 does not need to implement a production semantic-overlap model. It must define the interface/evidence expected from later decontamination work.

### FR-008 — Canonical serialization and digest

Canonical charter/registry artifacts SHALL serialize deterministically using a documented algorithm and produce SHA-256 identities over canonical bytes.

Runtime timestamps/paths/machine identifiers SHALL NOT alter scientific identity unless explicitly defined as semantic fields.

### FR-009 — Fixture-only validation

Provide synthetic/non-medical fixtures sufficient to prove:

- valid registry acceptance;
- missing required field rejection;
- duplicate identity rejection;
- invalid enum/state rejection;
- hard-gate dominance;
- prohibited Gold-use rejection;
- deterministic serialization/digest;
- semantic mutation changes identity.

Fixtures must not contain patient data or copied restricted benchmark content.

### FR-010 — Closeout evidence

Spec 001 closeout SHALL report:

- exact HEAD;
- exact changed paths;
- test/validation commands and results;
- canonical registry/contract artifact digests;
- acceptance criterion status;
- unresolved benchmark/license facts;
- explicit statement that Spec 002+ are not started.

## Non-functional requirements

### NFR-001 — Determinism

Given the same semantic inputs and implementation version, generated canonical artifacts must be byte-identical.

### NFR-002 — Minimal dependencies

Prefer Python 3.11 standard library. A third-party dependency requires a written necessity in the plan and must be approved before addition.

### NFR-003 — Offline operation

The implemented validator/digest/tests must run offline. Source verification used to populate the registry may be performed as research, but runtime validation must not depend on network availability.

### NFR-004 — Fail closed

Invalid, incomplete, duplicate, or contradictory registry/gate/quarantine states must fail rather than be silently normalized into a valid state.

### NFR-005 — Human readability

Machine-readable artifacts must remain reviewable through concise generated or hand-authored Markdown documentation; do not build a UI.

## Explicit exclusions

Spec 001 MUST NOT:

- download model weights;
- execute model inference;
- train or fine-tune models;
- access PHI;
- access restricted clinical dataset contents;
- construct real Gold cases;
- call external judge/model APIs;
- benchmark a candidate model;
- select a backbone;
- implement a vector database;
- build RAG;
- create a web service/UI;
- define final clinical thresholds without required evidence/owner decisions.

## Initial benchmark-verification rule

Every external evaluation family must have a primary/current source recorded before it can be `VERIFIED`. Secondary blog posts/trackers may help discovery but cannot alone establish canonical identity.

## Acceptance criteria

1. Registry schema/contract exists and validates required metadata.
2. Initial named benchmark families are either `VERIFIED` with source evidence or explicitly `UNRESOLVED`/excluded; no phantom names are silently accepted.
3. Metrics catalog distinguishes optimization metrics from hard gates.
4. A synthetic high-average/critical-failure fixture yields overall `FAIL`.
5. Three Gold protocol records exist without real case content.
6. Gold quarantine/prohibited-use validation is enforced.
7. Contamination metadata/interface is defined.
8. Canonical serialization is deterministic and SHA-256 identity is stable.
9. Fixture-only tests cover required failure modes and pass.
10. No dependency/framework beyond what the minimal plan authorizes is introduced.
11. No model/data execution prohibited by this spec occurred.
12. Closeout evidence binds results to exact HEAD and exact artifact identities.

## Exit state

`CLOSED_CANONICAL` only when all acceptance criteria pass and unresolved external facts are explicitly recorded without weakening the contract.

Closing Spec 001 does NOT authorize model inference/training. It unblocks planning of Specs 002 and 003 only.
