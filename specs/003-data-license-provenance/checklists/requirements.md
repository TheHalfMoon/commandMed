# Spec 003 Requirements Checklist — Data, License & Provenance

**Spec:** `003-data-license-provenance`
**Status:** PASS_CANDIDATE
**Canonical base:** `a57f87e77bbd396332b197342d8129f6805ba452`

## Specification quality

- [x] Purpose is limited to a machine-verifiable lineage contract.
- [x] Asset classes are explicit and do not authorize payload access.
- [x] Source verification is explicitly distinct from executable artifact binding.
- [x] Exact artifact identity supports both direct digest and immutable-revision-plus-artifact-locator binding.
- [x] `UNBOUND` cannot become executable for a use requiring exact payload identity.
- [x] Rights/license ambiguity is fail-closed.
- [x] Access/privacy/PHI boundaries are explicit and fail-closed.
- [x] Spec 001 Purpose/Gold/quarantine semantics remain authoritative.
- [x] Contamination uncertainty is fail-closed where clean separation is required.
- [x] Synthetic/derived assets retain parent/generator/use-rights lineage.
- [x] Admission states are closed and scoped to exact declared use.
- [x] Audit-only metadata is separated from scientific identity.
- [x] Exclusions are explicit.
- [x] Exit Evidence is explicit.

## Clarification quality

- [x] The five initial clarification questions are resolved in `research.md`.
- [x] SPDX is design evidence, not a runtime dependency or automatic authorization.
- [x] Croissant resource/version/checksum semantics are used only as design evidence.
- [x] W3C PROV derivation semantics are reduced to minimal parent/generator lineage.
- [x] DataCite identifiers do not substitute for exact payload identity.
- [x] Direct file SHA-256 is not incorrectly required when immutable-container binding is sufficient.
- [x] Existing Spec 001 benchmark records do not require migration merely for schema aesthetics.
- [x] FD-001 is not required at this stage.

## Plan quality

- [x] Minimal target paths are enumerated.
- [x] No database, service, queue, remote registry, or third-party runtime dependency is planned.
- [x] One small lineage module/validator is preferred over a framework.
- [x] Existing canonicalization is reused.
- [x] Existing Purpose/quarantine semantics are reused rather than duplicated.
- [x] Policy/contract JSON contains metadata only.
- [x] Focused fixture-only tests cover every critical fail-closed dimension.
- [x] Compatibility with canonical Spec 001 benchmark semantics has an explicit test path.
- [x] Malformed input must collect errors rather than crash.
- [x] Identity projection avoids globally ignoring arbitrary fields.
- [x] Full offline regression and compile checks are named.
- [x] Independent exact-head review remains required before merge.
- [x] Dedicated post-merge closure remains required.

## Safety / authority boundaries

- [x] No model download/load/execute authority.
- [x] No benchmark payload execution authority.
- [x] No training/adaptation/distillation/RL/QAT authority.
- [x] No teacher/API generation authority.
- [x] No PHI/restricted/private-Gold/gated payload access authority.
- [x] No Spec 004 work authority.
- [x] No legal-compliance claim is made.
- [x] No founder decision is manufactured.

## Requirement-to-test coverage

- [x] FR-001/FR-002: structural/source-vs-artifact tests planned.
- [x] FR-003: both exact-binding forms + unbound failure tests planned.
- [x] FR-004: rights evidence/SPDX/custom/component-specific fail-closed tests planned.
- [x] FR-005: privacy/PHI fixture-only tests planned.
- [x] FR-006: Purpose/Gold/quarantine compatibility tests planned.
- [x] FR-007: contamination-state admission tests planned.
- [x] FR-008: synthetic/derived parent/generator lineage tests planned.
- [x] FR-009/FR-010: canonicalization reuse and identity-projection tests planned.
- [x] FR-011: admission vocabulary/reason-code tests planned.
- [x] FR-012: malformed non-throwing/offline tests planned.
- [x] FR-013: dependency/diff inspection planned.
- [x] FR-014: identity-bearing mutation digest tests planned.
- [x] FR-015: FD-001 conditional/blocking behavior planned.
- [x] FR-016: Spec 001 compatibility mapping tests planned.

## Checklist result

```text
REQUIREMENTS_CHECKLIST=PASS_CANDIDATE
UNRESOLVED_PRODUCT_DECISION=NO
UNRESOLVED_SCIENTIFIC_CONTRADICTION=NO
IMPLEMENTATION_AUTHORITY=NOT_YET
NEXT=TASKS_THEN_ANALYZE
```
