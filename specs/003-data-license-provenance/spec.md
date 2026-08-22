# Spec 003 — Data, License & Provenance

**Feature Branch:** `spec/003-data-license-provenance`
**Created:** 2026-08-22
**Canonical starting base:** `a57f87e77bbd396332b197342d8129f6805ba452`
**Normative dependency:** Spec 001 — `CLOSED_CANONICAL`
**Execution-frontier predecessor:** Spec 002 — `CLOSED_CANONICAL`
**Lifecycle:** `specify=COMPLETE_CANDIDATE`, `clarify=COMPLETE_CANDIDATE`, `plan=REPAIRING_AFTER_ANALYZE_PASS_1`
**Training authority:** NONE
**Model execution authority:** NONE
**Benchmark payload execution authority:** NONE
**Data/model payload download authority:** NONE
**PHI/restricted-data access authority:** NONE

## 1. Purpose

Define the minimum machine-verifiable lineage contract that every commandMed data, model, evidence, and derived research asset must satisfy before a later bounded spec may admit that asset for a declared use.

Spec 003 turns the constitutional provenance rule into one reusable, fail-closed contract. It must make asset identity, source lineage, rights evidence, privacy/access status, split/quarantine state, contamination status, synthetic/teacher provenance, and verification state explicit enough that later specs cannot silently infer permission or scientific identity.

The core exit is a **machine-verifiable lineage contract**, not a corpus, model registry service, ingestion pipeline, data lake, or legal-compliance engine.

The bounded clarification record is `specs/003-data-license-provenance/research.md`.

## 2. Dependency and authority evidence

Canonical `main` at Spec 003 start:

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

- semantic canonical JSON normalization and SHA-256 identity;
- a machine-readable benchmark registry;
- source verification and immutable-revision binding;
- controlled access/use/license semantics for evaluation assets;
- fail-closed validation;
- Gold/quarantine purpose separation;
- contamination-sensitive metadata.

Spec 003 generalizes those concepts across asset classes. It does not create a second canonicalization framework or rewrite the Evaluation Charter for aesthetic uniformity.

## 3. Governing invariants

1. **Unclear rights block the declared use.** Missing, ambiguous, conflicting, or unsupported rights evidence is never interpreted as permission.
2. **Source verification is not executable-artifact binding.** A source/family may be verified while an exact payload remains unbound and therefore non-executable/reference-only.
3. **Exact artifact identity precedes executable use.** Exact identity may be established either by a direct cryptographic digest of the payload or by an exact artifact locator inside a content-addressed/cryptographically bound immutable source revision.
4. **A named version is not automatically immutable.** `main`, `master`, `latest`, arbitrary version labels, or mutable tags cannot satisfy exact executable binding merely because they are non-empty strings.
5. **If neither exact-binding form exists, the artifact is `UNBOUND`.** An `UNBOUND` artifact cannot be admitted for a use requiring exact executable bytes.
6. **Declared uses remain distinct.** Evaluation, optimization, teacher generation, retrieval/evidence use, modification, redistribution, and commercial constraints are not interchangeable.
7. **Private Gold remains quarantined.** Gold metadata may be represented; Gold payloads do not enter training, teacher generation, prompt tuning, hyperparameter tuning, checkpoint selection, backbone/model selection, or other optimization.
8. **No PHI in V1 repository artifacts.** Unknown privacy state cannot be upgraded to public/non-PHI by assumption.
9. **Contamination uncertainty is fail-closed.** Unresolved benchmark/holdout overlap cannot become clean lineage for an optimization or leakage-sensitive use.
10. **Generated/derived assets keep their parents.** Synthetic/model-generated material must retain parent, generator/teacher, configuration, and output-use lineage where applicable.
11. **Audit metadata is not scientific identity by accident.** Retrieval/check timestamps, local paths, display ordering, and convenience URLs must not silently change scientific identity.
12. **Narrow rights never expand by relabeling.** Reference-only, component-specific, evaluation-only, non-commercial, or otherwise bounded evidence cannot authorize a broader use without new evidence.
13. **Admission is computed, not self-asserted.** Input lineage evidence never becomes `ELIGIBLE` because it contains an `admission_state` field. Admission is evaluator-owned output bound to the exact contract and scientific record identities.
14. **The contract itself is fail-closed validated.** A malformed, weakened, or unknown contract cannot authorize a record.

## 4. Asset classes

One common lineage envelope must support at least:

- `DATASET_OR_CORPUS`
- `BENCHMARK_OR_EVALUATION_ASSET`
- `PRIVATE_GOLD_METADATA`
- `MODEL_OR_CHECKPOINT`
- `MODEL_GENERATED_OR_SYNTHETIC_ASSET`
- `EVIDENCE_OR_RETRIEVAL_SOURCE`
- `DERIVED_RESEARCH_ARTIFACT`

These are metadata/lineage classes, not authority to access, download, or execute the corresponding payloads.

## 5. Lineage evidence record

### 5.1 Universal evidence fields

Every input lineage record must carry:

- stable `asset_id`;
- controlled asset class;
- canonical human-readable name;
- schema/record version;
- canonical source identifier;
- canonical source location;
- immutable/content-addressed source revision when available, otherwise an explicit unresolved/unbound state;
- source verification state and evidence reference;
- declared use;
- access classification;
- rights/license state and evidence reference;
- artifact-binding state;
- semantic/canonical scientific-record identity using the existing repository canonicalization mechanism.

The evidence record does **not** trust caller-provided admission state/reasons. If such fields are supplied to the minimal validator, they must be rejected as computed-output fields or ignored only under an explicit persisted-result verification path.

Duplicate stable IDs, malformed identity fields, unknown controlled states, or contradictory universal fields fail validation rather than raising an uncontrolled exception.

### 5.2 Conditional exact-artifact fields

When the declared use requires exact payload identity, establish one of:

**Direct binding**

- direct cryptographic digest of exact payload bytes (SHA-256 for the V1 contract); or

**Immutable-container binding**

- a content-addressed/cryptographically bound source revision accepted by a conservative validator;
- exact artifact locator/subresource inside that revision;
- source evidence binding the revision to the canonical source.

For the existing repository baseline, canonical Git/Hugging Face commit-style hexadecimal revisions are acceptable evidence for immutable-container binding. A non-cryptographic version label may remain useful reference metadata but cannot satisfy exact executable binding by itself.

A direct SHA-256 is preferred where exact bytes are available, but it is not universally mandatory when immutable-container binding already establishes exact content identity.

Mutable `main`, `master`, `latest`, landing-page, or convenience URLs may aid discovery but cannot be the sole identity-bearing evidence when immutable binding is required.

### 5.3 Rights and license evidence

Where applicable record:

- license/status classification;
- SPDX License Expression as normalized evidence metadata when it truthfully represents the terms;
- `LicenseRef-*` or exact custom/component-specific terms identity when a standard identifier is insufficient;
- immutable/revision-bound license or terms evidence when available;
- research/evaluation implications;
- training/teacher-generation implications;
- modification/derivative implications;
- redistribution implications;
- commercial constraints stated by the source terms;
- unresolved/conflicting/component-specific rights with reason.

Spec 003 does not claim that a partial SPDX syntax check proves legal correctness, current SPDX-list membership, or use compatibility. Exact declared-use admission remains governed by rights evidence state plus project policy.

A framework or repository code license does not automatically license bundled, linked, gated, private, or separately distributed data/components.

FD-001 remains unresolved. If final product posture is necessary to decide compatibility, admission is blocked/conditional rather than silently resolving the founder decision.

### 5.4 Access, privacy, and PHI

Where applicable record:

- access class;
- PHI/privacy classification;
- de-identification status;
- gating/restriction evidence;
- whether repository payload presence is permitted.

Unknown privacy state cannot produce a repository-safe or training-eligible result. A `DEIDENTIFIED` label alone is metadata, not proof that every later use is authorized.

### 5.5 Split, purpose, and quarantine

Spec 003 preserves the canonical Spec 001 `Purpose` semantics:

- `TRAIN`
- `DEV`
- `CALIBRATION`
- `CHECKPOINT_SELECTION`
- `PUBLIC_EXTERNAL_EVAL`
- `PRIVATE_GOLD`

Where applicable record exact split/purpose identity, quarantine relation, allowed/prohibited cross-use, and selection restrictions.

A test, private Gold, or quarantined asset cannot inherit train/dev permissions from another split in the same source family.

### 5.6 Contamination / benchmark overlap

Where applicable record:

- contamination sensitivity;
- exact-match and/or semantic-overlap assessment state as appropriate;
- identity of the compared benchmark/holdout set when known;
- evidence/rationale identity;
- unresolved/suspected overlap state.

Unresolved contamination blocks a declared use that requires clean optimization/evaluation separation.

### 5.7 Synthetic, teacher, and derived lineage

For generated or derived assets, record where applicable:

- origin type;
- parent/source `asset_id` values;
- generator/teacher/provider identity and immutable revision;
- generation/configuration identity when scientifically relevant;
- output-use/license/terms evidence;
- verification/truth-boundary status.

Canonical defaults remain in force: MedGemma/HAI-DEF outputs do not become commandMed training lineage without an explicit override, and frontier API outputs do not become training data merely because generation is technically available.

## 6. Contract validation

The machine-readable lineage contract is itself governed data.

Before record validation/admission, the implementation must reject at least:

- non-object/malformed contract;
- missing contract/schema identity;
- missing required vocabularies/invariants;
- duplicate values in closed vocabularies;
- unknown or weakened admission states;
- removal/weakening of required exact-binding semantics;
- a contract that permits `UNBOUND` exact-byte use;
- a contract that makes admission caller-controlled;
- malformed invariant records/IDs;
- a contract whose canonical identity cannot be computed.

Record evaluation against an invalid contract yields no `ELIGIBLE` result.

## 7. Computed admission semantics

Do not create one ambiguous `verified=true` mega-status.

The underlying evidence dimensions remain independently represented. A pure evaluator computes one result:

- `ELIGIBLE` — all evidence required for the exact declared use is satisfied;
- `REFERENCE_ONLY` — source/metadata reference is permitted but the exact requested executable/optimization use is not;
- `BLOCKED` — required evidence, identity, compatibility, or prerequisite remains unresolved/conditional;
- `PROHIBITED` — recorded source constraints or commandMed policy establish that the declared use is disallowed.

The result includes deterministic machine-readable reasons and binds:

- exact contract canonical identity; and
- exact lineage scientific-record identity.

Unknown admission values fail contract validation. Caller-provided `ELIGIBLE` is never authoritative.

`ELIGIBLE` is scoped to the exact declared use and does not imply release readiness, clinical safety, legal advice, or permission for another use.

## 8. Declared-use dimensions

The lineage contract must distinguish at least:

- `REFERENCE`
- `DEVELOPMENT_EVALUATION`
- `PRIVATE_RELEASE_EVALUATION`
- `TRAINING_OR_ADAPTATION`
- `TEACHER_OR_SYNTHETIC_GENERATION`
- `RETRIEVAL_OR_EVIDENCE_USE`
- `MODIFICATION_OR_DERIVATION`
- `REDISTRIBUTION`

These broader declared uses map to, but do not erase, canonical data/evaluation `Purpose` values such as `CHECKPOINT_SELECTION` and `PRIVATE_GOLD`.

Commercial compatibility remains a rights-constraint dimension until FD-001 is actually required.

## 9. Existing Spec 001 compatibility

The canonical benchmark registry remains valid prior art.

Spec 003 must preserve:

- `VERIFIED` source/family status does not imply executable artifact binding;
- `REFERENCE_ONLY` may coexist with verified source/family evidence;
- executable benchmark identity may use exact artifact + cryptographic/content-addressed immutable source revision without a separate file digest;
- mixed/component-specific licenses do not inherit a framework license;
- unresolved license/source state cannot become executable development use;
- metadata registries contain zero benchmark case payloads;
- validation remains offline and deterministic;
- existing `Purpose`, Gold, and quarantine semantics remain authoritative for evaluation/data partitioning.

No canonical Spec 001 record must be rewritten merely to fit a new aesthetic schema if a compatibility mapping is sufficient.

## 10. External standards boundary

The clarification record uses primary public standards only as design evidence:

- SPDX 3.0.1 license-expression semantics;
- MLCommons Croissant 1.1 version/resource/checksum concepts;
- W3C PROV entity/derivation concepts;
- DataCite 4.6 persistent-identifier/relationship concepts.

Spec 003 does not adopt `mlcroissant`, RDF/PROV tooling, DataCite infrastructure, or another runtime dependency. Standard-library JSON plus existing commandMed canonicalization is the default unless `plan` proves otherwise.

## 11. User scenarios and independent tests

### US1 — Invalid contract cannot authorize

A malformed/weakened contract cannot validate a record or return `ELIGIBLE`.

### US2 — Ambiguous rights fail closed

A metadata-only fixture with a canonical source but unresolved rights cannot become training or executable-development `ELIGIBLE`.

### US3 — Verified family remains non-executable when artifact is unbound

A source/family may be verified while its separately distributed payload is `UNBOUND`; admission remains reference-only/blocked for executable use.

### US4 — Immutable-container identity is cryptographically bound

An exact artifact locator plus accepted content-addressed/cryptographic source revision qualifies as exact binding. A mutable label such as `latest` does not.

### US5 — Caller cannot self-assert eligibility

An input record containing `admission_state=ELIGIBLE` cannot bypass recomputation and must be rejected/treated as non-authoritative input.

### US6 — Private Gold stays quarantined

A `PRIVATE_GOLD_METADATA` fixture can carry identity/control metadata without case payloads. Any prohibited optimization/selection use fails closed.

### US7 — Teacher-output laundering is blocked

Synthetic/model-generated data without parent/generator/configuration/use-rights lineage cannot become training/adaptation eligible.

### US8 — Contamination uncertainty blocks optimization

A contamination-sensitive asset with unresolved overlap cannot be represented as clean optimization input merely because source and rights evidence are verified.

### US9 — Semantic identity is stable

Representation-only ordering or audit timestamp changes do not alter the governed scientific identity; identity-bearing source/artifact/rights/split/parent changes do.

### US10 — Model lineage remains license-neutral

A model/checkpoint record captures exact source, terms, redistribution/commercial constraints, and declared-use compatibility without selecting a winner or resolving FD-001 prematurely.

## 12. Functional requirements

- **FR-001:** Define one minimal machine-readable lineage contract and evidence-record envelope with controlled asset classes and stable IDs.
- **FR-002:** Validate the contract itself fail-closed before trusting its vocabularies/invariants.
- **FR-003:** Keep source verification separate from exact executable-artifact binding.
- **FR-004:** Support both direct SHA-256 and accepted content-addressed/cryptographic immutable-revision-plus-artifact-locator binding; otherwise mark the artifact unbound.
- **FR-005:** Record rights/license evidence and declared-use constraints fail-closed; SPDX/custom terms are evidence, not automatic legal authorization.
- **FR-006:** Represent access, PHI/privacy, and de-identification boundaries fail-closed and prohibit PHI/restricted payload fixtures in V1 repository artifacts.
- **FR-007:** Preserve canonical Spec 001 purpose/quarantine semantics so Gold/test/holdout data cannot silently enter prohibited optimization or selection uses.
- **FR-008:** Represent contamination/overlap state and block unresolved contamination where clean separation is required.
- **FR-009:** Require parent/generator/configuration/output-use lineage for synthetic/model-generated/derived assets where applicable.
- **FR-010:** Reuse `eval_contract.canonical` and existing enums/semantics where suitable instead of introducing a second identity framework.
- **FR-011:** Separate audit-only metadata from identity-bearing lineage through an explicit scientific-identity projection.
- **FR-012:** Compute admission as evaluator-owned output `ELIGIBLE | REFERENCE_ONLY | BLOCKED | PROHIBITED`; never trust self-asserted admission input.
- **FR-013:** Bind computed admission output to both contract identity and scientific record identity, with deterministic reason codes.
- **FR-014:** Keep validation offline, deterministic, fail-closed, and non-throwing for malformed fixtures.
- **FR-015:** Add no new third-party runtime dependency unless later evidence proves it necessary; default is standard library only.
- **FR-016:** Material changes to identity-bearing lineage or rights evidence require a new canonical scientific-record identity and re-verification.
- **FR-017:** Keep FD-001 unresolved until its actual dependency point; conditional compatibility remains explicit meanwhile.
- **FR-018:** Preserve canonical Spec 001 benchmark records by compatibility mapping unless a scientifically necessary migration is proven.

## 13. Edge cases

The implementation must fail closed for at least:

- malformed/weakened contract;
- duplicate/non-string contract or record IDs;
- unknown asset class, declared use, binding state, or admission state;
- missing canonical source identity;
- mutable label (`main`, `master`, `latest`) used as immutable binding;
- arbitrary non-cryptographic version string used as immutable executable binding;
- `UNBOUND` artifact evaluated as executable/eligible;
- malformed direct SHA-256;
- caller-provided `admission_state` attempting to bypass computation;
- unresolved/conflicting rights evaluated as eligible;
- component-specific family rights promoted to every component;
- unknown PHI/privacy state evaluated as repository-safe;
- PHI/restricted payload represented as a V1 fixture;
- Gold/test/quarantine data marked for prohibited training/selection use;
- contamination-sensitive optimization asset with unresolved overlap marked clean;
- synthetic/derived asset missing required parent/generator lineage;
- reference/evaluation-only teacher output marked training eligible;
- contradictory rights/use fields;
- malformed list/identity values that would otherwise crash set/map/sort operations;
- audit timestamps or local paths substituted for scientific identity;
- narrow authorization promoted to broader use without new evidence.

## Exclusions

Spec 003 does **not** authorize or implement:

- downloading, cloning, materializing, or inspecting dataset payloads merely to finish this spec;
- downloading, loading, or executing model weights;
- benchmark payload execution or scoring;
- training, CPT, SFT, LoRA/QLoRA, distillation, DPO, RL/RLVR/GRPO, or QAT;
- teacher/API generation;
- PHI, restricted clinical data, private Gold payloads, credentials, or gated model/data access;
- data cleaning, deduplication, tokenization, sampling, mixing, curriculum construction, or ingestion pipelines;
- a data lake, database, object store, service, queue, plugin framework, or remote registry;
- a full SPDX/Croissant/PROV/DataCite implementation;
- final model/tournament admission or winner selection;
- resolution of FD-001 before it is required;
- legal advice or a claim of legal authority beyond recorded primary-source evidence;
- Spec 002 repair inside the Spec 003 branch;
- Spec 004 Tournament Harness implementation.

## Acceptance criteria

Before Spec 003 implementation can become a closeout candidate:

1. specification, clarification, plan, checklist, tasks, and final analyze contain no unresolved material contradiction;
2. the canonical lineage contract itself is fail-closed validated;
3. one minimal lineage evidence record covers the required classes/dimensions;
4. computed admission is evaluator-owned and bound to exact contract + scientific record identities;
5. validation is deterministic, offline, fail-closed, and non-throwing on malformed fixtures;
6. canonical Spec 001 benchmark-registry semantics remain valid through direct reuse or explicit compatibility mapping;
7. source verification cannot substitute for executable-artifact binding;
8. direct SHA-256 and cryptographic immutable-container binding are tested; mutable/named-only revisions cannot satisfy exact binding;
9. unresolved/contradictory rights cannot produce `ELIGIBLE`;
10. PHI/privacy/access restrictions cannot be silently weakened;
11. purpose/split/quarantine controls prevent Gold/test/holdout leakage into prohibited uses;
12. contamination uncertainty blocks uses requiring clean separation;
13. synthetic/model-generated assets cannot lose required parent/generator/use-rights lineage;
14. canonical scientific identity is stable under representation-only/audit-only changes and changes under identity-bearing mutations;
15. no prohibited payload/model/training/PHI/Gold/gated execution or access occurred;
16. no unnecessary dependency/service/persistence layer was introduced;
17. exact-head focused tests, full offline regression tests, diff hygiene, and independent review pass with no unresolved material blocker.

## Exit Evidence

Spec 003 may transition toward `CLOSED_CANONICAL` only with identity-bound evidence for:

- canonical starting base and final reviewed implementation head;
- exact changed-path inventory;
- machine-readable lineage-contract canonical identity/hash;
- focused contract/record/admission validator tests;
- full offline regression suite;
- compatibility evidence for existing Spec 001 benchmark records;
- direct-digest and cryptographic immutable-container binding tests;
- self-asserted-admission bypass tests;
- scientific-identity stability tests;
- malformed-input/non-throwing tests;
- proof that prohibited payload/model/training/PHI/Gold/gated access did not occur;
- independent exact-head review and finding reconciliation;
- canonical implementation merge identity;
- dedicated post-merge closure transition verified on resulting `main`.

A green implementation merge alone does not make Spec 003 `CLOSED_CANONICAL`. Spec 004 remains blocked until Spec 003 completes qualified implementation and canonical closure.

## Immediate next lifecycle step

Repair `plan.md`, `tasks.md`, and checklist against Analysis Pass 1, then rerun `analyze`.

Implementation remains unauthorized until analysis passes.