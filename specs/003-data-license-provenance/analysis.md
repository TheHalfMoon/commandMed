# Spec 003 Analysis — Data, License & Provenance

**Spec:** `003-data-license-provenance`
**Analysis pass:** 2
**Status:** PASS
**Implementation authority:** BOUNDED_SPEC_003_ONLY
**Head reviewed:** `dc4848965771144d839b4f1b462c4785c1bde50b`
**Canonical base reverified:** `a57f87e77bbd396332b197342d8129f6805ba452`

## Inputs analyzed

- `.specify/memory/constitution.md`
- `AGENTS.md`
- `docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md`
- `docs/decision-register.md`
- `specs/README.md`
- canonical Spec 001 benchmark, Purpose, Gold, quarantine, validation, and canonicalization contracts
- canonical Spec 002 closure state
- `specs/003-data-license-provenance/spec.md`
- `specs/003-data-license-provenance/research.md`
- `specs/003-data-license-provenance/plan.md`
- `specs/003-data-license-provenance/tasks.md`
- `specs/003-data-license-provenance/checklists/requirements.md`

## Analyze Pass 1 finding reconciliation

### A003-01 — Contract input not explicitly validated

**Prior severity:** MATERIAL
**Resolution:** CLOSED

The repaired spec/plan now require `validate_lineage_contract()` before record validation or admission. Missing/weakened invariants and malformed vocabularies fail closed, and an invalid contract cannot authorize `ELIGIBLE`.

### A003-02 — Admission could be self-asserted

**Prior severity:** MATERIAL
**Resolution:** CLOSED

The evidence schema no longer trusts caller-provided admission. `admission_state` / `admission_reasons` are evaluator-owned computed output and are rejected as authoritative evidence input. The result is bound to the exact contract and scientific record identities.

### A003-03 — Immutable revision proof too weak

**Prior severity:** MATERIAL
**Resolution:** CLOSED

`IMMUTABLE_REVISION_LOCATOR` now requires an exact artifact locator plus conservative content-addressed/cryptographic revision evidence. V1 accepts canonical Git/Hugging Face commit-style 40/64-hex revisions; mutable/named labels such as `main`, `latest`, or `v1.0` cannot satisfy exact executable binding.

### A003-04 — SPDX field could overclaim validation

**Prior severity:** NON_BLOCKING_IF_CLARIFIED
**Resolution:** CLOSED

SPDX expressions are treated as rights evidence metadata only. Spec 003 does not claim legal correctness, current SPDX-list membership, or use compatibility from a partial/basic syntax check.

## Analyze Pass 2 additional finding

### A003-05 — Scientific record identity could be self-asserted

**Severity:** MATERIAL_IF_UNREPAIRED
**Resolution:** CLOSED_BEFORE_PASS

A remaining specification bullet previously implied that the input lineage record carried its scientific-record identity. This has been removed. The repaired spec explicitly requires scientific identity to be recomputed from the validated identity-bearing projection and rejects caller-provided `record_sha256`/equivalent computed identities in the minimal V1 evidence path.

## Requirement / plan / task consistency

### Contract trust boundary

PASS.

- contract is canonical governed metadata;
- contract validates before records;
- required invariant IDs cannot be silently removed;
- admission cannot be caller-controlled;
- malformed contract cannot return `ELIGIBLE`.

### Artifact identity

PASS.

Two exact-binding modes are coherent:

1. `DIRECT_DIGEST` — direct SHA-256 of exact payload bytes;
2. `IMMUTABLE_REVISION_LOCATOR` — exact artifact locator inside accepted cryptographic/content-addressed revision with source evidence.

`UNBOUND` remains truthful metadata and cannot satisfy an exact-byte use.

This preserves canonical Spec 001 benchmark behavior without forcing unnecessary migration.

### Rights / licensing

PASS.

- ambiguity remains fail-closed;
- component/mixed rights cannot widen automatically;
- SPDX/custom terms are evidence, not self-authorizing policy;
- FD-001 remains deferred until its actual dependency point;
- no legal-advice claim is introduced.

### Privacy / access

PASS.

- no real PHI/restricted payload is needed;
- unknown privacy blocks relevant use;
- de-identification classification alone does not override rights/access;
- V1 repository fixtures remain metadata-only/synthetic.

### Purpose / quarantine

PASS.

Existing `Purpose` values remain canonical. Private Gold, test, holdout, and checkpoint-selection semantics are not collapsed into a new generic use enum.

### Contamination

PASS.

Spec 003 records/validates contamination state only; it does not implement corpus matching. Unresolved/high-risk overlap cannot be laundered into clean optimization lineage.

### Synthetic / derived lineage

PASS.

Parent/generator/configuration/output-use evidence is conditionally required. The design preserves the default that external/model-generated output does not enter training lineage by omission.

### Scientific identity

PASS.

The plan uses an explicit identity-bearing projection with existing `compute_canonical_sha256()` and excludes audit-only timestamps/local paths rather than teaching the global canonicalizer to ignore arbitrary fields.

### Implementation minimality

PASS.

Planned implementation is bounded to:

- one contract JSON;
- one small `lineage.py` module;
- one focused unittest file;
- one reviewer-facing governance document;
- only minimal integration exports/canonical set-like additions if tests require them.

No DB, service, queue, JSON-LD/RDF stack, external registry, third-party runtime dependency, model framework, or network runtime is justified.

## Authority review

No later-stage authority is created by this PASS.

```text
MODEL_EXECUTION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
TEACHER_API_GENERATION_AUTHORITY=NONE
PHI_RESTRICTED_DATA_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_PAYLOAD_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
SPEC_004=BLOCKED
```

## Analysis result

```text
ANALYZE=PASS
ANALYSIS_PASS=2
OPEN_MATERIAL_FINDINGS=0
FOUNDER_DECISION_REQUIRED_NOW=NO
NEW_RUNTIME_DEPENDENCY_REQUIRED=NO
IMPLEMENTATION_AUTHORIZED=YES_FOR_BOUNDED_SPEC_003_TASKS_ONLY
NEXT=T003-01_CANONICAL_LINEAGE_CONTRACT
```

Implementation must remain on the existing Draft PR, preserve exact scope, and return to `REPAIR_REQUIRED` if new material contradictions emerge.