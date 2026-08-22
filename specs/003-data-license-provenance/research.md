# Spec 003 — Data, License & Provenance Research / Clarification Record

**Date:** 2026-08-22
**Lifecycle stage:** `clarify`
**Canonical starting base:** `a57f87e77bbd396332b197342d8129f6805ba452`
**Authority:** metadata/governance research only; no data/model/benchmark payload access or execution

## 1. Question

What is the smallest machine-verifiable lineage design that satisfies the commandMed constitution and preserves the already-canonical Spec 001 benchmark/provenance semantics without creating a second framework?

## 2. Repository evidence reviewed

The canonical repository already establishes several mechanisms that must be reused:

- `src/commandmed/eval_contract/canonical.py` provides semantic canonical JSON normalization and SHA-256 identity, including `asset_id` as a stable record sort key.
- `src/commandmed/eval_contract/model.py` already defines controlled evaluation vocabularies for access, source verification, benchmark license status, intended use, purpose, and contamination state.
- `src/commandmed/eval_contract/validate.py` distinguishes source/family verification from executable intended use and requires concrete `artifact_version` plus immutable `source_revision` for executable benchmark records.
- `data/eval/benchmarks.json` proves that an executable artifact may be identity-bound by an exact artifact locator inside an immutable cryptographic source revision; a separate direct file SHA-256 is not universally present.
- `docs/evaluation/benchmark-registry.md` explicitly states that `VERIFIED` source/family status does not imply executable artifact binding and that mixed/component-specific rights remain reference-only until the actual component is registered.

This is the compatibility baseline. Spec 003 must generalize it, not invalidate it.

## 3. Public primary standards reviewed

These sources are design evidence only. They are not adopted wholesale, do not create runtime dependencies, and do not constitute legal advice.

### 3.1 SPDX Specification 3.0.1 — License Expressions

Primary source:

- https://spdx.github.io/spdx-spec/v3.0.1/annexes/spdx-license-expressions/

Relevant evidence:

- SPDX defines a machine-parseable license-expression grammar.
- Standard license identifiers can be combined with `AND`, `OR`, and `WITH`.
- Custom/non-standard licenses can be represented through `LicenseRef-*` rather than inventing a misleading standard identifier.

**Decision:** Spec 003 should permit a normalized SPDX expression where it accurately represents the source terms, while retaining exact license/terms evidence and explicit declared-use constraints. An SPDX expression is evidence metadata, not by itself a commandMed legal/use authorization.

**Compatibility rule:** do not replace the canonical Spec 001 `LicenseStatus` benchmark vocabulary merely to make every record look SPDX-native. A future common lineage envelope may map benchmark statuses to richer rights evidence without rewriting canonical benchmark truth.

### 3.2 MLCommons Croissant 1.1

Primary source:

- https://docs.mlcommons.org/croissant/docs/croissant-spec-1.1.html

Relevant evidence:

- Croissant separates dataset metadata, resources/files, structure, and ML semantics.
- It represents dataset versioning explicitly.
- `FileObject` resources may carry SHA-256 checksums.
- Version + checksums strengthen reproducibility and detection of changed resource bytes.
- The standard represents license metadata and resource URLs without requiring that every dataset use one storage mechanism.

**Decision:** borrow the concepts of versioned resources, exact resource locators, and optional/direct checksums. Do **not** add `mlcroissant`, JSON-LD, schema.org, or another serialization stack to Spec 003. commandMed can remain small, offline, standard-library JSON while being compatible with the useful semantics.

### 3.3 W3C PROV Data Model

Primary source:

- https://www.w3.org/TR/prov-dm/

Relevant evidence:

- PROV distinguishes entities, activities, agents, and derivation relations such as `wasDerivedFrom`.
- Provenance of a derived entity can therefore preserve both its parent entity identity and the activity/agent that produced it.

**Decision:** use the minimum parent/derivation semantics needed for commandMed synthetic and derived assets: parent asset IDs plus generator/activity/configuration identity where scientifically relevant. Do **not** implement a general PROV graph engine, RDF model, or PROV serialization.

### 3.4 DataCite Metadata Schema 4.6

Primary source:

- https://schema.datacite.org/meta/kernel-4.6/

Relevant evidence:

- DataCite provides versioned metadata for research outputs and supports persistent identifiers and typed relationships between research objects.

**Decision:** persistent external identifiers and typed relationships may be retained as evidence when available, but commandMed scientific identity remains governed by its exact source/artifact/content binding. A DOI or other persistent identifier is not a substitute for exact executable payload identity.

## 4. Clarification decisions

### C-001 — Avoid a mega-status

**Decision:** lineage dimensions remain independently represented. Do not collapse source verification, artifact binding, rights, privacy/access, split/quarantine, contamination, and synthetic lineage into one `verified=true` flag.

A single final admission result may use the smallest four-state vocabulary:

- `ELIGIBLE` — all dimensions required for the exact declared use are satisfied;
- `REFERENCE_ONLY` — metadata/source reference is permitted but the exact declared executable/optimization use is not;
- `BLOCKED` — required evidence or a prerequisite is unresolved/conditional;
- `PROHIBITED` — evidence establishes that the declared use is not permitted by commandMed policy or recorded source constraints.

The admission result must include machine-readable reasons/dimensions. It does not replace the underlying evidence fields.

### C-002 — Universal versus conditional fields

**Universal fields:**

- stable `asset_id`;
- asset class;
- canonical name;
- schema/record version;
- source identifier/location;
- source revision or explicit unbound state;
- source verification state/evidence;
- declared use;
- access classification;
- license/terms status and evidence reference;
- artifact-binding state;
- final admission state/reasons;
- canonical lineage-record identity.

**Conditional fields:**

- exact artifact locator and/or direct digest when exact payload identity is required;
- split/purpose/quarantine fields for data/evaluation/Gold assets;
- contamination/overlap fields when the asset can influence optimization, selection, or leakage-sensitive evaluation;
- PHI/de-identification fields for privacy-relevant assets;
- parent/generator/configuration fields for derived/synthetic/model-generated assets;
- component-specific rights evidence for mixed bundles/families;
- model/checkpoint-specific redistribution/use restrictions when applicable.

The validator should determine conditional requirements from asset class + declared use rather than requiring meaningless placeholder values for every class.

### C-003 — Exact artifact identity has two valid forms

**Decision:** direct content SHA-256 is preferred when bytes are available and should be used where practical, but it is **not** the only valid exact identity form.

An exact executable/admissible artifact may be bound by either:

1. a direct cryptographic digest of the exact payload bytes; or
2. an exact artifact locator/subresource inside a cryptographically immutable source revision whose revision identity binds the content.

If neither is available, the executable artifact is `UNBOUND` and cannot be admitted for a use requiring exact executable bytes.

This preserves the canonical Spec 001 benchmark behavior. Spec 003 must amend any wording that incorrectly requires a direct file digest in all cases.

### C-004 — Gated/private/reference-only assets remain truthful without payload access

**Decision:** when payload access is intentionally absent, record only what can be verified from public/authorized metadata:

- canonical source/family identity;
- immutable metadata/code/release revision if available;
- rights/access evidence;
- known component/asset identity;
- explicit executable artifact state `UNBOUND` if exact bytes are unavailable.

Do not fabricate a content digest or claim executable binding. `REFERENCE_ONLY` is a valid outcome.

### C-005 — Semantic identity versus audit metadata

**Identity-bearing when applicable:**

- stable asset/class identity;
- immutable source revision;
- exact artifact binding;
- declared use;
- rights/terms evidence identity;
- split/quarantine purpose;
- contamination resolution evidence identity;
- parent/generator/configuration identity for derived assets.

**Audit-only unless they change scientific meaning:**

- retrieval/check timestamp;
- local filesystem path;
- reviewer workstation/environment;
- display ordering;
- convenience URLs;
- free-form notes that do not alter the governed facts.

Changing audit-only metadata must not silently create a new scientific asset identity. Changing identity-bearing lineage must.

### C-006 — Reuse boundary

**Decision:** reuse `compute_canonical_sha256()` and semantic normalization from `eval_contract.canonical`. Reuse existing enums/semantics where they already express the required concept.

Do not force all asset classes through the benchmark-specific `BenchmarkRecord` or benchmark validator. The plan should prefer one small additive lineage module/validator and fixtures, importing proven canonicalization rather than mutating the Evaluation Charter into a universal registry.

Any new set-like lineage fields should be explicitly added to canonical normalization only if their order is semantically irrelevant and tests prove representation-order stability.

### C-007 — Purpose/use compatibility

**Decision:** preserve existing Spec 001 `Purpose` semantics (`TRAIN`, `DEV`, `CALIBRATION`, `CHECKPOINT_SELECTION`, `PUBLIC_EXTERNAL_EVAL`, `PRIVATE_GOLD`) for evaluation/data partitioning.

Spec 003's broader declared-use dimension may additionally cover teacher/synthetic generation, retrieval/evidence use, modification/derivation, and redistribution. It must map to — not erase — the existing purpose/quarantine rules.

### C-008 — Founder decision boundary

**Decision:** FD-001 remains unresolved. Spec 003 records factual commercial/redistribution/modification constraints and may return `BLOCKED`/conditional compatibility when final product posture is necessary.

Do not ask the founder to choose a release license merely to finish the lineage schema.

## 5. Rejected designs

### R-001 — Full SPDX/Croissant/PROV implementation

Rejected: unnecessary dependencies and complexity. Standards are used as design evidence only.

### R-002 — One giant universal enum

Rejected: it would hide which dimension failed and make source verification indistinguishable from use authorization.

### R-003 — Direct SHA-256 required for every executable asset

Rejected: unnecessarily breaks canonical Spec 001 artifacts that are exactly located inside immutable cryptographic revisions. Direct digest remains preferred when available.

### R-004 — License string alone authorizes use

Rejected: a license identifier does not encode all access, component, privacy, split, contamination, teacher-output, or project-policy constraints.

### R-005 — Download assets to resolve metadata uncertainty

Rejected in Spec 003 planning. Public/authorized metadata research is sufficient for the contract; unresolved payload identity remains fail-closed.

## 6. Clarify outcome

```text
CLARIFY_STATUS=PASS_WITH_SPEC_CORRECTION_REQUIRED
FOUNDER_DECISION_REQUIRED_NOW=NO
NEW_RUNTIME_DEPENDENCY_REQUIRED=NO
NETWORK_RUNTIME_REQUIRED=NO
DATA_PAYLOAD_ACCESS_REQUIRED=NO
MODEL_ACCESS_REQUIRED=NO
PHI_OR_PRIVATE_GOLD_ACCESS_REQUIRED=NO
NEXT=AMEND_SPEC_FOR_C003_AND_C007_THEN_PLAN
```

The specification must be corrected before `plan` so it does not require a direct file content hash where canonical Spec 001 exact-revision/artifact binding is already sufficient, and so checkpoint/model-selection purpose semantics remain explicit.