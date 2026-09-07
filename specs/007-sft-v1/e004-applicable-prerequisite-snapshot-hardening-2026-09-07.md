# E004 Applicable-Prerequisite Snapshot Hardening — 2026-09-07

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Predecessor frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v46-2026-09-07.md`
**Authority source:** canonical E004 CM-3 bounded corrective-maintenance authority
**Artifact class:** repository-only fail-closed pre-execution control-plane hardening
**Model execution effect:** NONE
**A15 effect:** NONE
**Training authority:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Close only the deterministic control-plane defect identified by V46: the successor `ResearchComponentPreExecutionSubject` carried an opaque `a1_a14_applicable_snapshot_sha256` plus caller-provided `PASS`, but no successor-specific content-addressed applicable-prerequisite snapshot validator or authoritative-store binding existed.

This hardening does not construct a live PASS snapshot. It creates the contract required to validate one later without fabricating any prerequisite evidence.

## 2. Implementation

Add:

```text
src/commandmed/spec007/e004_applicable_prerequisite_snapshot.py
tests/spec007/test_e004_applicable_prerequisite_snapshot.py
```

The implementation is additive. It does not alter:

```text
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=None
```

and therefore cannot make the current repository executable.

## 3. Exact applicable gate set

The snapshot requires exactly the 14 pre-execution evidence families already present in V46 and the current successor execution contract:

```text
SUCCESSOR_SCOPE_POLICY
SUCCESSOR_EXECUTION_AUTHORITY
EVALUATION_ASSET_QUALIFICATION
CANDIDATE_ARTIFACT_BUNDLE_BINDING
EXECUTION_PLAN_ARGV
MODEL_LOAD_COMPATIBILITY
ORCHESTRATOR_IMPLEMENTATION_BINDING
EXECUTION_ENVIRONMENT_BINDING
RESOURCE_BINDING
ACCESS_BINDING
CREDENTIAL_BOUNDARY
NETWORK_BOUNDARY
RETENTION_BOUNDARY
ZERO_INCREMENTAL_SPEND_BINDING
```

These are not new scientific thresholds or model-quality gates. They are a deterministic composition of already-required successor pre-execution evidence families.

The exact gate-set identity is computed with the repository canonical serializer from the ordered gate ID list.

## 4. Snapshot contract

Each snapshot must bind:

```text
schema_version
snapshot_id
snapshot_sha256
scope_id
protocol_id
protocol_sha256
evaluation_asset_set_sha256
candidate_artifact_bundle_set_sha256
gate_set_sha256
gate_records[]
disposition=PASS
```

Each gate record must bind:

```text
gate_id
evidence_id
evidence_sha256
evidence_repository_commit
disposition=PASS
```

The snapshot validator requires:

- exact successor scope identity;
- exact frozen tournament protocol identity;
- exact frozen evaluation asset-set identity;
- exact canonical four-candidate artifact-bundle-set identity;
- exactly 14 unique gate records equal to the closed applicable gate set;
- a non-empty evidence ID for every gate;
- a canonical SHA-256 identity for every gate's evidence;
- an exact 40-hex repository commit binding for every gate's evidence;
- `PASS` for every gate and the aggregate snapshot;
- canonical self-addressed snapshot SHA-256.

Missing, duplicate, extra, non-PASS, malformed, stale-by-identity, or tampered state fails closed.

## 5. Authoritative-store binding

A structurally valid pre-execution subject is no longer sufficient for the new authorization wrapper.

The subject's exact:

```text
a1_a14_applicable_snapshot_id
a1_a14_applicable_snapshot_sha256
a1_a14_applicable_state
```

must resolve through a caller-supplied authoritative snapshot store keyed by the exact snapshot SHA-256. The resolved snapshot must itself validate and must agree with the subject on snapshot ID, scope, protocol, evaluation asset set, and disposition.

An opaque syntactically valid SHA-256 that is absent from the authoritative store fails closed.

## 6. Authorization wrapper and non-expansion

The new entrypoint:

```text
build_research_component_execution_request_with_prerequisites
```

first requires the exact applicable-prerequisite snapshot binding to pass, then delegates to the existing canonical `build_research_component_execution_request`.

It creates no authority of its own.

At the current canonical state the delegated builder still blocks because:

```text
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
```

Therefore even a fully valid synthetic snapshot and structurally valid synthetic subject must return:

```text
STATE=BLOCKED
REASON=CURRENT_CANONICAL_PREEXECUTION_SUBJECT_NOT_AUTHORIZED
EXECUTION_PERFORMED=false
REQUEST=null
```

## 7. Explicit prohibitions

```text
MODEL_WEIGHT_ACCESS_EXPANSION=NONE
MODEL_LOAD_AUTHORITY_EXPANSION=NONE
MODEL_FORWARD_PASS_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
GENERATION_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
EVALUATION_PAYLOAD_EXECUTION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY=NONE
WINNER_SELECTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The tests use synthetic metadata only.

## 8. Qualification requirements

Before guarded merge, exact-head qualification must establish at minimum:

```text
COMPILE_CHANGED_PYTHON=PASS
FOCUSED_APPLICABLE_PREREQUISITE_SNAPSHOT_TESTS=PASS
EXISTING_RESEARCH_EXECUTION_TESTS=PASS
SPEC007_REGRESSION=PASS
FULL_REPOSITORY_REGRESSION=PASS
DIFF_WHITESPACE=PASS
MODEL_EXECUTION_DURING_QUALIFICATION=NO
TOURNAMENT_EXECUTION_DURING_QUALIFICATION=NO
```

Independent repository review remains optional by default under FD-007 unless a later exact authority requires it.

## 9. Post-hardening frontier

If this exact implementation is qualified and becomes canonical:

```text
E004_A1_A14_SNAPSHOT_CONTROL_PLANE_SUBUNIT=COMPLETE_FAIL_CLOSED_VALIDATOR_AVAILABLE
E004_A1_A14_LIVE_PASS_SNAPSHOT=ABSENT
E004_RESOURCE_ACCESS_FINANCE_SUBUNIT=INCOMPLETE_REAL_EVIDENCE_REQUIRED
E004_EXACT_SUBJECT_BINDING_SUBUNIT=INCOMPLETE
E004_A15_SUBUNIT=NOT_REACHED
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
```

The next dependency-safe transition remains an exact environment/resource/access/finance evidence design and authority reconciliation. This hardening does not create that operational evidence authority.
