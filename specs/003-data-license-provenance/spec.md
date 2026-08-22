# Spec 003 — Data, License & Provenance

**Feature Branch:** `spec/003-data-license-provenance`
**Created:** 2026-08-22
**State:** SPECIFICATION_CANDIDATE
**Canonical starting base:** `a57f87e77bbd396332b197342d8129f6805ba452`
**Normative dependency:** Spec 001 — `CLOSED_CANONICAL`
**Execution-frontier predecessor:** Spec 002 — `CLOSED_CANONICAL`
**Training authority:** NONE
**Model execution authority:** NONE
**Benchmark payload execution authority:** NONE
**Data/model download authority:** NONE
**PHI/restricted-data access authority:** NONE

## 1. Purpose

Define the minimum machine-verifiable lineage contract that every commandMed data, model, evidence, and derived research asset must satisfy before a later bounded spec may admit that asset for a declared use.

Spec 003 turns the constitutional provenance rule into one reusable, fail-closed contract. It must make asset identity, source lineage, rights evidence, privacy/access status, split/quarantine state, contamination status, synthetic/teacher provenance, and verification state explicit enough that later specs cannot silently infer permission or scientific identity.

The core exit of this spec is a **machine-verifiable lineage contract**, not a corpus, data lake, model registry service, or ingestion pipeline.

## 2. Dependency and authority evidence

Canonical `main` at Spec 003 start is:

```text
MAIN=a57f87e77bbd396332b197342d8129f6805ba452
SPEC_001=CLOSED_CANONICAL
SPEC_002=CLOSED_CANONICAL
SPEC_003=AUTHORIZED_TO_START
SPEC_003_IMPLEMENTATION=NOT_STARTED
SPEC_004=BLOCKED
MODEL_EXECUTION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PHI_RESTRICTED_DATA_ACCESS_AUTHORITY=NONE
```

Spec 001 already provides mechanisms that Spec 003 must reuse rather than replace:

- deterministic semantic canonicalization;
- a machine-readable benchmark registry;
- source verification and immutable-revision binding rules;
- controlled license/access/use vocabularies for evaluation assets;
- fail-closed validation behavior;
- Gold/quarantine purpose separation;
- contamination-sensitive benchmark metadata.

Spec 003 generalizes those proven concepts across asset classes. It does not create a second canonicalization framework or duplicate the Evaluation Charter.

## 3. Governing invariants

The following are normative:

1. **Unclear rights block use.** Missing, ambiguous, conflicting, mutable-only, or unsupported rights evidence may never be interpreted as permission.
2. **Source verification is not executable-asset binding.** A source/family may be verified while an exact payload remains unbound and therefore non-executable/reference-only.
3. **Identity precedes use.** An asset admitted for execution, optimization, scoring, or promotion must be bound to an immutable source revision and exact artifact/content identity appropriate to that asset class.
4. **Declared use is explicit.** Evaluation, training, teacher generation, retrieval/evidence use, redistribution, modification, and commercial implications must not be conflated.
5. **Private Gold remains quarantined.** Metadata may describe Gold identities and controls; Gold payloads do not become training, teacher, prompt-tuning, checkpoint-selection, or model-selection material.
6. **No PHI in V1 repository artifacts.** Restricted or PHI-bearing material cannot be admitted into repository fixtures merely to exercise the contract.
7. **Contamination uncertainty is fail-closed.** Unknown or unresolved benchmark/holdout overlap cannot silently become clean lineage for an optimization use that requires separation.
8. **Synthetic/model-generated material keeps its parents.** Derived or model-generated assets must retain generator/teacher/source lineage and use-rights evidence; generated text is not provenance-free.
9. **Mutable operational metadata must not silently change scientific identity.** Retrieval/check timestamps are audit evidence, while scientific identity must remain bound to immutable source/content/configuration fields.
10. **A broader claim cannot inherit a narrower authorization.** Reference-only, component-specific, evaluation-only, non-commercial, or otherwise bounded rights cannot be promoted to a broader use by relabeling the asset.

## 4. Asset classes

The lineage contract must support at least these classes without requiring separate frameworks:

- `DATASET_OR_CORPUS`
- `BENCHMARK_OR_EVALUATION_ASSET`
- `PRIVATE_GOLD_METADATA`
- `MODEL_OR_CHECKPOINT`
- `MODEL_GENERATED_OR_SYNTHETIC_ASSET`
- `EVIDENCE_OR_RETRIEVAL_SOURCE`
- `DERIVED_RESEARCH_ARTIFACT`

These are lineage classes, not authorization to download or execute any corresponding payload.

An implementation may use one common envelope with class-specific required fields rather than unrelated schemas.

## 5. Minimum lineage envelope

Every record must carry enough information to answer the following questions deterministically where applicable.

### 5.1 Stable record identity

- stable `asset_id`;
- controlled asset class;
- human-readable canonical name;
- record/schema version;
- semantic/canonical record identity using the repository's existing canonicalization mechanism.

Duplicate stable identities or ambiguous identity-bearing fields fail validation.

### 5.2 Source and artifact identity

- canonical source identifier;
- canonical source location;
- immutable source revision/version when one exists;
- exact artifact locator/subresource where applicable;
- cryptographic content identity for any payload that is to become executable/admissible;
- explicit `UNBOUND`/equivalent state when exact executable bytes are not yet identity-bound;
- retrieval or verification time as audit metadata, not a substitute for immutable identity.

Mutable `main`, `master`, `latest`, landing-page, or convenience URLs may aid discovery but must not be the sole identity-bearing evidence when an immutable revision is required.

### 5.3 Rights and license evidence

The record must distinguish factual evidence from downstream policy decisions. At minimum record:

- license/status vocabulary;
- immutable or revision-bound license/terms evidence when available;
- declared use under review;
- research/evaluation implications;
- training/teacher-generation implications;
- modification/derivative implications;
- redistribution implications;
- commercial implications where the source terms make them explicit;
- component-specific or mixed-rights boundaries;
- unresolved/conflicting rights state with a reason.

A top-level code/framework license does not automatically license bundled, linked, gated, private, or separately distributed data.

FD-001 is not silently resolved by Spec 003. Where final product posture is required to decide compatibility, the lineage record remains conditional or blocked until that founder decision is actually due.

### 5.4 Access, privacy, and PHI

At minimum record:

- access classification;
- privacy/PHI classification;
- de-identification status where relevant;
- access/gating restrictions;
- whether payload presence in the repository is permitted.

Unknown privacy state cannot be upgraded to public/non-PHI by assumption.

### 5.5 Split and quarantine identity

Where applicable record:

- split identity or purpose;
- whether the split may participate in training, development, checkpoint selection, model selection, public evaluation, or private release evaluation;
- quarantine/holdout relation;
- any prohibited cross-use.

A test, private Gold, or quarantined asset cannot inherit the permissions of a training/development split from the same source family.

### 5.6 Contamination / benchmark-overlap state

Where applicable record:

- contamination sensitivity;
- overlap-check state;
- identity of compared benchmark/holdout set when known;
- evidence or rationale for the state;
- unresolved/suspected overlap state.

A contamination-sensitive asset with unresolved overlap cannot be represented as cleared for an optimization use that depends on clean separation.

### 5.7 Synthetic, teacher, and derived lineage

For generated or derived assets, record enough parentage to reconstruct the lineage boundary:

- origin type;
- parent/source asset identities;
- generator/teacher/provider identity and immutable revision where applicable;
- generation/configuration identity where scientifically relevant;
- output-use/license/terms evidence;
- verification/truth-boundary status;
- whether the output is permitted for the declared downstream use.

Canonical defaults remain in force: MedGemma/HAI-DEF outputs are reference/evaluation-only for training lineage unless explicitly overridden, and frontier API outputs do not become training data merely because they can be generated.

## 6. Verification and admission semantics

Spec 003 must preserve the distinction between evidence collection and use admission.

At minimum, the implementation must be able to represent these outcomes without ambiguity:

- source/family verified but executable artifact unbound;
- artifact identity bound but rights unresolved;
- rights evidenced but privacy/access blocks payload use;
- rights/privacy resolved but contamination or split use unresolved;
- reference-only use permitted;
- declared use eligible only after all required dimensions pass;
- explicitly prohibited use.

The exact machine vocabulary is finalized during `clarify`/`plan`, but it must be closed, validated, and fail-closed. Unknown states or missing required dimensions may not default to an allowed state.

No single boolean named `verified`, `licensed`, or `safe` may collapse source verification, exact artifact identity, rights compatibility, privacy, contamination, split purpose, and downstream-use admission into one ambiguous flag.

## 7. Intended declared-use dimensions

The contract must be able to evaluate or record at least these distinct use dimensions without assuming they are equivalent:

- `REFERENCE`
- `DEVELOPMENT_EVALUATION`
- `PRIVATE_RELEASE_EVALUATION`
- `TRAINING_OR_ADAPTATION`
- `TEACHER_OR_SYNTHETIC_GENERATION`
- `RETRIEVAL_OR_EVIDENCE_USE`
- `MODIFICATION_OR_DERIVATION`
- `REDISTRIBUTION`

Commercial compatibility is recorded as a rights constraint/evidence dimension until FD-001 becomes necessary; Spec 003 does not choose the final release posture.

## 8. Existing benchmark-registry compatibility

The Spec 001 benchmark registry is canonical prior art and must remain valid.

Spec 003 must preserve these established semantics:

- `VERIFIED` source/family status does not imply executable artifact binding;
- `REFERENCE_ONLY` is compatible with a verified family record;
- mixed/component-specific licenses do not inherit a framework license;
- unresolved license state cannot become executable development use;
- identity-bearing links should be immutable/pinned where possible;
- metadata registries contain zero benchmark case payloads;
- validation is offline and deterministic.

Spec 003 may define a common lineage envelope that existing benchmark records can map into, but it must not require needless migration or rewrite of canonical Spec 001 evidence merely for aesthetic uniformity.

## 9. User scenarios and independent tests

### US1 — Data steward rejects ambiguous rights

A metadata-only fixture with a canonical source but unresolved license/use evidence is rejected for training or executable development admission and remains blocked/reference-only as appropriate.

**Independent test:** pure local fixture; no external payload or network access.

### US2 — Researcher distinguishes verified family from executable payload

A family-level record may be source-verified while its separately distributed payload is `UNBOUND`. The validator proves that source verification alone cannot authorize execution.

### US3 — Gold custodian preserves quarantine

A `PRIVATE_GOLD_METADATA` fixture can represent identity, split purpose, and audit controls without storing case payloads. Any attempt to mark it training/checkpoint/model-selection eligible fails closed.

### US4 — Lineage reviewer blocks teacher-output laundering

A synthetic fixture without generator identity, parent/source lineage, or output-use evidence cannot become training/adaptation eligible. Reference/evaluation-only defaults remain enforceable for restricted teacher sources.

### US5 — Contamination reviewer blocks unresolved overlap

A contamination-sensitive asset whose overlap state is unresolved cannot become clean optimization input merely because its source and license are verified.

### US6 — Identity reviewer proves semantic stability

Representation-only ordering changes do not change the canonical lineage-record identity, while changing identity-bearing source revision, artifact identity, declared use, split, or rights evidence does.

### US7 — Model candidate remains license-neutral

A model/checkpoint record can capture exact upstream license and redistribution/commercial constraints without selecting the tournament winner or resolving FD-001 prematurely.

## 10. Edge cases

The contract/validator must fail closed for at least:

- duplicate `asset_id`;
- unknown asset class or use state;
- missing canonical source identifier;
- mutable-only source identity where immutable binding is required;
- executable/admissible payload with missing or malformed content hash;
- `UNBOUND` artifact marked executable;
- unresolved/conflicting license marked allowed;
- component-specific family license promoted to all components;
- missing license evidence URI/reference when required;
- unknown privacy/PHI state represented as repository-safe;
- PHI/restricted payload represented as a V1 repository fixture;
- private Gold/test/quarantine split marked training/checkpoint/model-selection eligible;
- contamination-sensitive optimization asset with unresolved overlap represented as clean;
- synthetic/teacher asset with missing parent/generator provenance;
- reference/evaluation-only teacher output marked training eligible;
- contradictory rights fields;
- malformed/non-string identity fields that would otherwise crash set/map operations;
- timestamps or local paths silently substituted for scientific identity;
- a narrower-use record promoted to a broader use without new evidence.

## 11. Functional requirements

- **FR-001:** Define one minimal machine-readable lineage envelope with controlled asset classes and stable identities.
- **FR-002:** Bind source/family verification separately from exact executable artifact identity.
- **FR-003:** Require immutable source revision and cryptographic payload identity before any use that requires exact executable bytes.
- **FR-004:** Record rights/license evidence and distinct downstream-use constraints without inferring permission from ambiguity.
- **FR-005:** Represent access, privacy/PHI, and de-identification boundaries fail-closed; prohibit PHI/restricted payload fixtures in V1 repository artifacts.
- **FR-006:** Bind split purpose and quarantine controls so Gold/test/holdout assets cannot be silently used for optimization or selection.
- **FR-007:** Represent contamination/benchmark-overlap state and block unresolved contamination where clean separation is required.
- **FR-008:** Require parent/generator/teacher lineage and output-use evidence for synthetic/model-generated/derived assets.
- **FR-009:** Preserve the existing Spec 001 benchmark registry semantics and reuse existing semantic canonicalization rather than introducing a new identity framework.
- **FR-010:** Separate audit metadata such as retrieval/verification timestamps from scientific identity-bearing fields.
- **FR-011:** Use a closed, machine-validated admission/use vocabulary; unknown or incomplete state must not default to allowed.
- **FR-012:** Keep all validation offline and deterministic using the standard library and already-approved repository mechanisms unless `plan` proves another dependency necessary.
- **FR-013:** Emit actionable validation reasons that identify the blocked lineage dimension without exposing restricted payload content.
- **FR-014:** Treat a material change to identity-bearing lineage or rights evidence as a new scientific record identity requiring re-verification.
- **FR-015:** Keep FD-001 unresolved until the dependency requires the founder's product/licensing posture; conditional compatibility must remain explicitly conditional meanwhile.

## 12. Clarifications required before plan

These are evidence/design questions for the Spec 003 `clarify` stage, not founder decisions unless evidence proves otherwise:

1. What is the smallest closed admission-state vocabulary that preserves independent source, artifact, rights, privacy, split, contamination, and synthetic-lineage dimensions without an ambiguous mega-status?
2. Which fields are universal versus required only for a given asset class or declared use?
3. Which existing Spec 001 validation/canonicalization functions can be reused directly, and where is a narrow additive validator required?
4. How should an external gated/reference-only asset record exact identity when payload bytes are intentionally inaccessible, while still preventing execution claims?
5. Which fields belong in semantic identity versus audit-only metadata so verification timestamps and local paths do not cause scientific identity drift?

No model, dataset, benchmark payload, gated asset, or private Gold content needs to be accessed to answer these questions.

## Exclusions

Spec 003 explicitly does **not** authorize or implement:

- downloading, cloning, materializing, or inspecting dataset payloads merely for Spec 003;
- downloading, loading, or executing model weights;
- benchmark payload execution or scoring;
- training, CPT, SFT, LoRA/QLoRA, distillation, DPO, RL/RLVR/GRPO, or QAT;
- teacher/API generation;
- access to PHI, restricted clinical datasets, private Gold payloads, credentials, or gated model/data assets;
- data cleaning, deduplication, tokenization, sampling, mixing, curriculum construction, or ingestion pipelines;
- a data lake, database, object store, service, queue, plugin framework, or remote registry;
- final model/tournament admission or winner selection;
- resolution of FD-001 before it is actually required;
- legal advice or an assertion that commandMed has legal authority beyond the recorded primary-source evidence;
- changes to Spec 002 safety-policy implementation or reconciliation of any later-discovered Spec 002 defect inside the Spec 003 branch;
- Spec 004 Tournament Harness implementation.

## 14. Acceptance criteria

Before Spec 003 implementation can become a closeout candidate, evidence must prove all of the following:

1. the bounded specification, clarification, plan, checklist, tasks, and analyze stages contain no unresolved material contradiction;
2. one minimal machine-readable lineage contract exists and covers the required asset/use dimensions;
3. validation is deterministic, offline, fail-closed, and non-throwing on malformed fixtures;
4. existing Spec 001 benchmark-registry semantics remain valid or have an explicitly justified compatibility mapping;
5. exact source verification cannot substitute for exact executable artifact binding;
6. ambiguous/unresolved rights cannot produce an allowed use;
7. privacy/PHI and access restrictions cannot be silently weakened;
8. split/quarantine controls prevent Gold/test/holdout leakage into prohibited uses;
9. contamination uncertainty blocks uses that require clean separation;
10. synthetic/model-generated assets cannot lose parent/generator/use-rights lineage;
11. canonical identity is stable under representation-only changes and changes under identity-bearing mutations;
12. no model, benchmark payload, training, PHI/restricted-data, real-Gold, or gated-asset execution occurred;
13. no unnecessary third-party dependency, service, or persistence layer was introduced;
14. exact-head tests and diff hygiene pass;
15. a fresh independent exact-head review finds no unresolved material blocker.

## Exit Evidence

Spec 003 may transition toward `CLOSED_CANONICAL` only with identity-bound evidence for:

- canonical starting base and final reviewed implementation head;
- exact changed-path inventory;
- machine-readable lineage-contract identity/hash;
- focused validator/fixture test results;
- full offline regression-suite results;
- compatibility evidence for existing Spec 001 benchmark records;
- semantic-identity stability tests;
- fail-closed malformed-input tests;
- proof that prohibited payload/model/training/PHI/Gold/gated access did not occur;
- independent exact-head review and finding reconciliation;
- canonical implementation merge identity;
- a dedicated post-merge closure transition verified on resulting `main`.

A green implementation merge alone does not make Spec 003 `CLOSED_CANONICAL`. Spec 004 remains blocked until Spec 003 has completed its own qualified implementation and canonical closure lifecycle.

## 16. Immediate next lifecycle step

`clarify` only.

The next work may inspect existing repository contracts and public primary-source standards/documentation as needed to resolve Section 12. It may not implement the lineage validator or ingest any external asset until clarification and planning are complete and analyzed.