# Spec 003 Analysis — Data, License & Provenance

**Spec:** `003-data-license-provenance`
**Analysis pass:** 1
**Status:** REPAIR_REQUIRED
**Implementation authority:** NONE
**Head reviewed:** `486ac3e8068001918397e9cb73be4427d51eb1a0`

## Inputs analyzed

- `.specify/memory/constitution.md`
- `AGENTS.md`
- `docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md`
- `docs/decision-register.md`
- `specs/README.md`
- Spec 001 canonical benchmark/purpose/quarantine contracts
- `src/commandmed/eval_contract/canonical.py`
- `src/commandmed/eval_contract/model.py`
- `src/commandmed/eval_contract/validate.py`
- `specs/003-data-license-provenance/spec.md`
- `specs/003-data-license-provenance/research.md`
- `specs/003-data-license-provenance/plan.md`
- `specs/003-data-license-provenance/tasks.md`
- `specs/003-data-license-provenance/checklists/requirements.md`

## Finding A003-01 — Contract input is not explicitly fail-closed validated

**Severity:** MATERIAL

The plan proposes `validate_lineage_record(record, contract)` but does not explicitly require validating the contract object itself before trusting its vocabularies/invariants.

A malformed or weakened contract must not be able to authorize records merely because the record validator reads values from it.

### Required repair

Add a public contract validator or equivalent immutable trusted-contract gate:

```text
validate_lineage_contract(contract) -> list[str]
```

It must reject malformed/missing top-level fields, unknown/duplicate closed vocabulary values, weakened invariant definitions, and non-canonical contract identity assumptions before any record can be evaluated.

Record/admission evaluation must refuse to operate as eligible when the contract is invalid.

## Finding A003-02 — Admission cannot be trusted from record input

**Severity:** MATERIAL

The specification/plan list `admission_state` and `admission_reasons` as record fields while also proposing an evaluator that computes admission.

If input-provided `ELIGIBLE` is trusted or merely validated syntactically, a caller could self-assert eligibility despite unresolved rights/privacy/contamination/binding state.

### Required repair

Separate:

- **lineage evidence record** — facts/evidence supplied for evaluation; and
- **computed admission result** — evaluator-owned output.

If a persisted envelope later stores an admission result, it must include the exact contract identity and record scientific identity and must be recomputed/verified rather than trusted.

The minimal Spec 003 implementation should prefer computed result output and keep self-asserted admission out of the evidence input schema.

## Finding A003-03 — `IMMUTABLE_REVISION_LOCATOR` proof is too weak

**Severity:** MATERIAL

The plan currently requires only a non-empty `source_revision` plus `artifact_locator` for `IMMUTABLE_REVISION_LOCATOR`.

That would allow mutable labels such as `main`, `latest`, or an arbitrary version string to masquerade as immutable identity.

### Required repair

The binding must carry evidence that the revision is content/cryptographically bound, not merely named.

Minimum acceptable implementation for this repository:

- direct payload SHA-256; **or**
- exact artifact locator plus a cryptographic/content-addressed revision identifier accepted by a conservative validator (e.g. canonical Git/Hugging Face commit-style hexadecimal revision) and its source evidence.

Reference-only assets may retain non-cryptographic version labels, but those labels cannot satisfy an exact executable binding by themselves.

## Finding A003-04 — SPDX field must not imply full license adjudication

**Severity:** NON_BLOCKING_IF_CLARIFIED

The plan mentions conservative syntax validation for optional SPDX expressions. A partial parser must not be represented as validating the legal correctness or current SPDX-list membership of a license expression.

### Required repair

Treat `spdx_license_expression` as normalized evidence metadata unless a complete bounded validator is explicitly implemented. Admission remains governed by recorded exact-use rights evidence state and fail-closed project policy, not by presence of a syntactically plausible SPDX string.

## Consistency checks that passed

- No founder decision is required now.
- Spec 003 does not need payload/model/PHI/Gold/gated access.
- Direct file digest is correctly no longer universal; canonical Spec 001 immutable-revision/artifact semantics can remain valid.
- Spec 001 Purpose/Gold/quarantine semantics are preserved rather than duplicated.
- No third-party runtime dependency is justified.
- No Spec 004 work is authorized.
- No training/model/benchmark execution authority is introduced.

## Analysis result

```text
ANALYZE=REPAIR_REQUIRED
MATERIAL_FINDINGS=3
NON_BLOCKING_FINDINGS=1
IMPLEMENTATION_AUTHORIZED=NO
NEXT=REPAIR_SPEC_PLAN_TASKS_CHECKLIST_THEN_RERUN_ANALYZE
```
