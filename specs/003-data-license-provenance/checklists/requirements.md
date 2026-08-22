# Spec 003 Requirements Checklist — Data, License & Provenance

**Spec:** `003-data-license-provenance`
**Status:** REPAIRED_READY_FOR_ANALYZE_PASS_2
**Canonical base:** `a57f87e77bbd396332b197342d8129f6805ba452`

## Specification quality

- [x] Purpose is limited to a machine-verifiable lineage contract.
- [x] Asset classes are explicit and do not authorize payload access.
- [x] Source verification is distinct from executable artifact binding.
- [x] Exact artifact identity supports direct SHA-256 or cryptographic/content-addressed immutable-revision + exact locator.
- [x] Mutable/named-only revisions cannot satisfy immutable executable binding.
- [x] `UNBOUND` cannot become executable for a use requiring exact payload identity.
- [x] Rights/license ambiguity is fail-closed.
- [x] Access/privacy/PHI boundaries are explicit and fail-closed.
- [x] Spec 001 Purpose/Gold/quarantine semantics remain authoritative.
- [x] Contamination uncertainty is fail-closed where clean separation is required.
- [x] Synthetic/derived assets retain parent/generator/use-rights lineage.
- [x] Admission states are closed and scoped to exact declared use.
- [x] Admission is computed output, not caller-authoritative evidence.
- [x] Computed admission binds exact contract + scientific record identities.
- [x] The contract itself is fail-closed validated before use.
- [x] Audit-only metadata is separated from scientific identity.
- [x] Exclusions and Exit Evidence are explicit.

## Clarification quality

- [x] Initial clarification questions are resolved in `research.md`.
- [x] SPDX is design evidence/metadata, not automatic authorization or legal adjudication.
- [x] Croissant resource/version/checksum semantics are design evidence only.
- [x] W3C PROV derivation semantics are reduced to minimal parent/generator lineage.
- [x] DataCite identifiers do not substitute for exact payload identity.
- [x] Direct file SHA-256 is not universal when cryptographic immutable-container binding suffices.
- [x] Existing Spec 001 benchmark records do not require migration for schema aesthetics.
- [x] FD-001 is not required at this stage.

## Analyze Pass 1 repairs

- [x] A003-01 repaired: explicit `validate_lineage_contract()` path added.
- [x] A003-02 repaired: self-asserted admission removed from evidence trust boundary; evaluator owns result.
- [x] A003-03 repaired: immutable locator binding now requires conservative cryptographic/content-addressed revision evidence, not an arbitrary non-empty string.
- [x] A003-04 clarified: optional SPDX expression is evidence metadata; partial syntax checking cannot claim legal validity/list membership.

## Plan quality

- [x] Minimal target paths are enumerated.
- [x] No database, service, queue, remote registry, or third-party runtime dependency is planned.
- [x] One small lineage module/validator is preferred over a framework.
- [x] Existing canonicalization is reused.
- [x] Existing Purpose/quarantine semantics are reused rather than duplicated.
- [x] Policy/contract JSON contains metadata only.
- [x] Contract validation precedes record/admission evaluation.
- [x] Focused fixture-only tests cover critical fail-closed dimensions.
- [x] Spec 001 compatibility has an explicit test path.
- [x] Malformed input must collect errors rather than crash.
- [x] Scientific identity uses an explicit projection rather than arbitrary global ignores.
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

## Requirement-to-task/test coverage

- [x] Contract validity: T003-01/T003-02.
- [x] Evidence-record structural/source-vs-artifact validation: T003-03.
- [x] Direct/immutable cryptographic binding, rights, privacy: T003-04.
- [x] Purpose/Gold/quarantine/contamination/derived lineage: T003-05.
- [x] Scientific identity projection: T003-06.
- [x] Computed admission + identity binding + self-assertion rejection: T003-07.
- [x] Canonical Spec 001 compatibility: T003-08.
- [x] Documentation: T003-09.
- [x] Exact-head/full regression/negative verification: T003-10.
- [x] Qualified merge + dedicated closure: T003-11.

## Checklist result

```text
REQUIREMENTS_CHECKLIST=REPAIRED_READY_FOR_ANALYZE_PASS_2
UNRESOLVED_PRODUCT_DECISION=NO
KNOWN_MATERIAL_FINDING_UNREPAIRED=NO
IMPLEMENTATION_AUTHORITY=NOT_YET
NEXT=ANALYZE_PASS_2
```
