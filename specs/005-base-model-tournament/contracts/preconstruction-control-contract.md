# Spec 005 — Preconstruction Control Contract

**Status:** `COMPLETE`
**Contract type:** Internal deterministic Python/JSON interface contract.

This contract defines the implementation surface for Spec 005. It is intentionally metadata-only and does not authorize or transport model, benchmark, case, Gold, PHI, credential, payment, or device-execution payloads.

## 1. Public module interfaces

### `commandmed.spec005.preconstruction`

```python
validate_preconstruction_contract(contract: object) -> list[str]
validate_source_route(record: object, contract: object) -> list[str]
validate_root_task_metadata(record: object, contract: object) -> list[str]
validate_pair_metadata(record: object, contract: object) -> list[str]
validate_review_binding(record: object, contract: object) -> list[str]
validate_contamination_plan(record: object, contract: object) -> list[str]
evaluate_preconstruction_snapshot(snapshot: object, contract: object) -> dict[str, object]
```

Requirements:

- ordinary malformed parsed JSON returns deterministic errors rather than raising;
- unknown states/fields covered by closed-shape rules fail closed;
- computed readiness ignores caller-owned `pass`, `ready`, `eligible` or equivalent claims;
- dependency/staleness is computed from exact bound records;
- no clinical case text is accepted in metadata records.

### `commandmed.spec005.personnel`

```python
validate_personnel_record(record: object) -> list[str]
validate_eligibility_record(record: object, evidence: object) -> list[str]
evaluate_role_eligibility(record: object, evidence: object) -> dict[str, object]
validate_role_assignment(record: object, eligibility: object) -> list[str]
validate_independence(assignments: object) -> list[str]
evaluate_a7_handshake(assignment: object, eligibility: object) -> dict[str, object]
```

Requirements:

- public records use opaque personnel references;
- no self-verification/sole self-clearance;
- actual Private Gold exposure blocks selection-content roles under current policy;
- same-suite result exposure prevents return to a result-blind content role;
- stale eligibility cannot support active access consideration;
- role independence collisions fail closed.

### `commandmed.spec005.access`

```python
validate_access_policy(record: object) -> list[str]
validate_access_grant_metadata(record: object, a7_handshake: object) -> list[str]
evaluate_access_disposition(record: object, a7_handshake: object) -> dict[str, object]
```

Requirements:

- default deny;
- metadata, selection-content and candidate-result zones remain distinct;
- Private Gold is outside the selection zones;
- `ALLOW_GRANT_CONSIDERATION` is not itself an access grant;
- A7 `DENY_GRANT`, `REVOKE_REQUIRED`, or stale identity cannot be overridden;
- candidate results cannot flow back to active author/reviewer/adjudicator roles;
- no storage provisioning occurs.

### `commandmed.spec005.finance`

```python
validate_requirement_manifest(record: object) -> list[str]
evaluate_a14_requirement(record: object) -> dict[str, object]
validate_a14_authorization(record: object) -> list[str]
validate_a14_transition(authorization: object, transition: object) -> list[str]
evaluate_a14_operational_pass(requirements: object, authorizations: object) -> dict[str, object]
```

Requirements:

- current default/absence of evidence never implies `NOT_REQUIRED`;
- authorization approval, commitment/payment execution and reconciliation remain separate concepts;
- direct payee/beneficiary self-approval is rejected;
- only `ACTIVE` authorization may cover a prospective new commitment;
- material scope/cap/period/vendor/pricing change requires new/superseding identity;
- `$0`, free-tier labels or assumed volunteer capacity cannot establish PASS;
- no payment/contract/vendor operation occurs.

### `commandmed.spec005.device`

```python
validate_device_qualification_contract(contract: object) -> list[str]
validate_device_evidence_metadata(record: object, contract: object) -> list[str]
evaluate_device_preflight(records: object, contract: object) -> dict[str, object]
```

Requirements:

- validate five frozen target identities/classes and common protocol parameters;
- validate immutable runtime/build/tool/signal identity fields when evidence claims completeness;
- distinguish `HARD_FAIL` from `INCOMPLETE`;
- require five complete measured-run records for a numeric median;
- never invoke llama.cpp/model/device tooling.

### `commandmed.spec005.activation`

```python
validate_activation_record(record: object, snapshot: object) -> list[str]
evaluate_activation_readiness(record: object, snapshot: object) -> dict[str, object]
```

Requirements:

- a real activation must bind an exact current A1–A14 prerequisite snapshot;
- stale/blocked/incomplete/mismatched prerequisite prevents activation readiness;
- caller-owned authorization claims are not trusted;
- synthetic fixture validation does not create canonical construction authority.

### `commandmed.spec005.manifest`

```python
validate_spec005_manifest(manifest: object, artifacts: object) -> list[str]
build_spec004_projection(manifest: object, artifacts: object) -> dict[str, object]
evaluate_spec005_preflight(manifest: object, artifacts: object) -> dict[str, object]
```

Requirements:

- validates exact metrics-v2, preconstruction, device, candidate/admission and activation identities;
- preserves common-core/base-only/fully-admitted rules;
- rejects Private Gold as selection evidence;
- unresolved metric/threshold/sample/runtime/evidence values block projection rather than defaulting;
- projection reuses existing Spec 004 tournament semantics;
- does not execute candidates or select a winner from fabricated evidence.

## 2. Error/result conventions

Validation functions return ordered deterministic error-code strings. Evaluation functions return JSON-compatible mappings with at least:

```text
state
reason_codes[]
```

and identity fields applicable to their domain.

Recommended global ordering rule:

```text
reason_codes = sorted(unique_reason_codes)
```

unless an existing canonical repository contract already defines a stronger ordering requirement.

Ordinary malformed input must not raise. Programmer errors/internal invariant violations may raise only if existing repository conventions already do so; prefer fail-closed result objects for user-supplied parsed JSON.

## 3. Identity contract

Use the repository's existing canonical SHA-256 helper on an explicit identity-bearing projection.

Identity-bearing fields include governed scientific/policy values, immutable revisions, exact evidence references and dependency identities.

Exclude audit-only/local values when they do not change governed meaning, such as local paths, retrieval timestamps or workstation notes.

Material changes require a new identity. Never silently rewrite a historical record and retain its prior digest.

## 4. Closed-content boundary

The implementation MUST reject or prohibit repository metadata objects attempting to embed prohibited payload fields such as:

```text
clinical_case_text
prompt_text
arabic_case_text
english_case_text
answer_text
reference_answer_text
rubric_text
candidate_output_text
private_gold_case_content
phi_payload
credential_document
payment_instrument
```

Use opaque artifact/evidence references and cryptographic content identities instead.

## 5. Offline fixture contract

Tests may construct synthetic dictionaries representing all state paths, including synthetic `AUTHORIZED_TO_CONSTRUCT`/`ACTIVE` records solely to prove validator semantics.

A synthetic fixture state:

```text
DOES_NOT_EQUAL_REAL_AUTHORITY
DOES_NOT_AUTHORIZE_PAYLOAD_ACCESS
DOES_NOT_AUTHORIZE_MODEL_EXECUTION
DOES_NOT_AUTHORIZE_DEVICE_EXECUTION
DOES_NOT_AUTHORIZE_SPEND
```

No test may require network, external provider, credential, model weight, benchmark/Gold payload, PHI, payment or device runtime.

## 6. Compatibility contract

- Historical V1 metric/tournament identities remain reproducible.
- A1 V2 is additive and explicit.
- Spec 005 does not redefine Spec 003 lineage admission.
- Spec 005 does not redefine Spec 002 safety hard-gate evaluation.
- Spec 005 does not replace Spec 004 deterministic comparison/no-selection logic.
- Spec 005 adds prerequisite evidence, admission constraints, resource/device metadata and activation gating around those inherited contracts.

## 7. No implicit authority

No function in this package may perform an external side effect that turns a validated policy object into a real-world action. In particular, these modules expose no provider calls, downloads, subprocess/device runners, storage provisioning, payment actions, contract acceptance, credential access, model loading or inference.