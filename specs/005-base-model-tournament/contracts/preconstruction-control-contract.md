# Spec 005 — Preconstruction Control Contract

**Status:** `REPAIRED_COMPLETE`
**Contract type:** Internal deterministic Python/JSON interface contract.

This contract defines the implementation surface for Spec 005. It is metadata-only and does not authorize or transport model, benchmark, case, Gold, PHI, credential, payment, or device-execution payloads.

## 1. `commandmed.spec005.science`

```python
validate_selection_quality_contract(contract: object, metrics_v2: object) -> list[str]
validate_threshold_policy(record: object, quality_contract: object, metrics_v2: object) -> list[str]
validate_statistical_design(record: object, threshold_records: object, quality_contract: object) -> list[str]
evaluate_scientific_selection_readiness(records: object, quality_contract: object, metrics_v2: object) -> dict[str, object]
```

Requirements:

- exactly the seven required noncompensable quality lanes are recognized;
- every required lane/stratum has explicit metric/evidence-role mapping;
- threshold/margin records bind metric, estimand, direction, scope, clinical/statistical evidence and qualified review identities;
- missing exact threshold/margin required for a decision is `INCOMPLETE/BLOCKED`, never defaulted;
- A3+A4 is one atomic statistical/allocation identity binding estimand, unit, precision/power objective, nuisance assumptions, dependency/pairing, multiplicity, numeric N and allocation;
- Arabic parity is paired/root-case aware and cannot use an unpaired independent-two-sample shortcut;
- candidate-specific/post-result thresholds, nuisance inputs, N or allocation are rejected;
- caller-owned `pass`, `adequate`, `powered` or equivalent claims are not authoritative.

## 2. `commandmed.spec005.preconstruction`

```python
validate_preconstruction_contract(contract: object) -> list[str]
validate_source_route(record: object, contract: object) -> list[str]
validate_root_task_metadata(record: object, contract: object) -> list[str]
validate_pair_metadata(record: object, contract: object) -> list[str]
validate_review_binding(record: object, contract: object) -> list[str]
validate_contamination_plan(record: object, contract: object) -> list[str]
evaluate_preconstruction_snapshot(snapshot: object, contract: object, scientific_readiness: object) -> dict[str, object]
```

Requirements:

- ordinary malformed parsed JSON returns deterministic errors rather than raising;
- unknown states/fields covered by closed-shape rules fail closed;
- computed readiness ignores caller-owned `pass`, `ready`, `eligible` or equivalent claims;
- scientific A2/A3+A4 readiness is a required input and cannot be bypassed;
- dependency/staleness is computed from exact bound records;
- no clinical case text is accepted in metadata records.

## 3. `commandmed.spec005.personnel`

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

## 4. `commandmed.spec005.access`

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

## 5. `commandmed.spec005.finance`

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

## 6. `commandmed.spec005.device`

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

## 7. `commandmed.spec005.activation`

```python
validate_activation_record(record: object, snapshot: object) -> list[str]
evaluate_activation_readiness(record: object, snapshot: object) -> dict[str, object]
```

Requirements:

- a real activation must bind an exact current A1–A14 prerequisite snapshot, including A2/A3+A4 scientific records;
- stale/blocked/incomplete/mismatched prerequisite prevents activation readiness;
- caller-owned authorization claims are not trusted;
- synthetic fixture validation does not create canonical construction authority.

## 8. `commandmed.spec005.manifest`

```python
validate_spec005_manifest(manifest: object, artifacts: object) -> list[str]
build_spec004_projection(manifest: object, artifacts: object) -> dict[str, object]
evaluate_spec005_preflight(manifest: object, artifacts: object) -> dict[str, object]
```

Requirements:

- validates exact metrics-v2, selection-quality, threshold/statistical, preconstruction, device, candidate/admission and activation identities;
- preserves seven-lane noncompensable quality, common-core/base-only/fully-admitted rules;
- rejects Private Gold as selection evidence;
- unresolved metric/threshold/sample/runtime/evidence values block projection rather than defaulting;
- projection reuses existing Spec 004 tournament semantics;
- does not execute candidates or select a winner from fabricated evidence.

## 9. Error/result conventions

Validation functions return ordered deterministic error-code strings. Evaluation functions return JSON-compatible mappings with at least:

```text
state
reason_codes[]
```

and applicable exact identity fields.

Recommended global ordering:

```text
reason_codes = sorted(unique_reason_codes)
```

unless an inherited canonical contract defines a stronger ordering requirement.

Ordinary malformed input must not raise. Prefer fail-closed result objects for user-supplied parsed JSON.

## 10. Identity contract

Use the existing canonical SHA-256 helper on explicit identity-bearing projections.

Identity-bearing fields include governed scientific/policy values, metric/evidence-role mappings, threshold/margin/N/allocation values when frozen, immutable revisions, exact evidence references and dependency identities.

Exclude audit-only/local values when they do not change governed meaning. Material changes require a new identity; never silently rewrite history while retaining the prior digest.

## 11. Closed-content boundary

Reject/prohibit repository metadata objects embedding fields such as:

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

## 12. Offline fixture contract

Tests may construct synthetic dictionaries representing all state paths, including synthetic fully frozen scientific records and `AUTHORIZED_TO_CONSTRUCT`/`ACTIVE` states solely to prove validator semantics.

Synthetic fixture state:

```text
DOES_NOT_EQUAL_REAL_AUTHORITY
DOES_NOT_AUTHORIZE_PAYLOAD_ACCESS
DOES_NOT_AUTHORIZE_MODEL_EXECUTION
DOES_NOT_AUTHORIZE_DEVICE_EXECUTION
DOES_NOT_AUTHORIZE_SPEND
```

No test may require network, external provider, credential, model weight, benchmark/Gold payload, PHI, payment or device runtime.

## 13. Compatibility contract

- Historical V1 metric/tournament identities remain reproducible.
- A1 V2 is additive and explicit.
- Spec 005 science records consume metrics-v2 rather than inventing metric identities.
- Spec 005 does not redefine Spec 003 lineage admission.
- Spec 005 does not redefine Spec 002 safety hard-gate evaluation.
- Spec 005 does not replace Spec 004 deterministic comparison/no-selection logic.
- Spec 005 adds scientific threshold/statistical evidence, prerequisite governance, resource/device metadata and activation gating around those inherited contracts.

## 14. No implicit authority

No function in this package may perform an external side effect that turns a validated policy object into a real-world action. These modules expose no provider calls, downloads, subprocess/device runners, storage provisioning, payment actions, contract acceptance, credential access, model loading or inference.