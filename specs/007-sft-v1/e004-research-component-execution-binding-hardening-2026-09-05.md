# E004 Research-Component Execution Binding Hardening — 2026-09-05

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Canonical base at branch creation:** `f70b54c426f448d38a93c8eca95da23f2ad3bb08`
**Artifact class:** fail-closed corrective-maintenance reconciliation
**Authority source:** canonical E004 CM-3 corrective-maintenance authorization
**Execution effect:** NONE
**Training authority:** NONE
**Current authorized spend:** USD 0

## 1. Finding

PR #258 canonically introduced the missing successor-specific pre-execution envelope, but post-merge adversarial inspection found two material control-plane gaps that must be repaired before any operational evidence may be treated as execution-ready.

First, the envelope accepted caller-supplied favorable state strings for A15/resource/access and could therefore construct `READY_FOR_EXTERNAL_EXECUTOR` for a structurally complete synthetic subject. That is not a valid live authority transition. CM-3 requires caller-owned PASS to be non-authoritative.

Second, the frozen `RESOURCE_EFFICIENCY` evaluation asset declares `RESOURCE_MEASUREMENT_RECORD_V1`, but the repository had no validator for those result records. The tournament evidence pack carried opaque `resource_result_ids` without verifying the exact frozen eight-probe measurement subject.

```text
PR258_CANONICALITY=PRESERVED
PR258_IMPLEMENTATION_REQUIRES_FAIL_CLOSED_HARDENING=YES
CALLER_OWNED_PASS_MAY_AUTHORIZE_EXECUTION=NO
RESOURCE_RESULT_IDS_WITHOUT_RESULT_VALIDATION=INSUFFICIENT
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
```

## 2. Exact-subject execution lock

`src/commandmed/spec007/research_execution.py` now separates structural completeness from live execution authority.

```text
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
STRUCTURALLY_COMPLETE_SYNTHETIC_SUBJECT_CAN_BUILD_LIVE_REQUEST=NO
LIVE_REQUEST_REQUIRES_EXACT_CANONICAL_SUBJECT_SHA256=YES
```

Until a later canonical gate-closing transition binds one exact fully qualified subject SHA-256, `build_research_component_execution_request()` returns:

```text
STATE=BLOCKED
REASON=CURRENT_CANONICAL_PREEXECUTION_SUBJECT_NOT_AUTHORIZED
EXECUTION_PERFORMED=false
REQUEST=null
```

A future subject authorization must be a new canonical repository transition after every applicable prerequisite, including the applicable A1-A14-equivalent snapshot and separately authorized A15 activation, is genuinely PASS.

## 3. Candidate executable-bundle hardening

Every frozen candidate runtime binding now additionally requires:

```text
complete_bundle_sha256
complete_bundle_bytes
runtime_artifact_sha256
build_toolchain_identity
execution_plan_sha256
```

The existing exact runtime executable, runtime source revision, tokenizer/config, argv, access, format-compatibility, and model-artifact identities remain required.

For PRIMARY candidates, the canonical E001 mass-reach package hard cap remains noncompensable:

```text
PRIMARY_COMPLETE_BUNDLE_HARD_CAP_BYTES=734003200
```

The CONTROL remains exempt from the PRIMARY package cap but not from exact identity requirements.

This hardening does not import the legacy five-target Spec 005 device measurement protocol into `SP007-RO-001`. The frozen research-component `RESOURCE_EFFICIENCY` asset has its own exact measurement protocol and remains controlling for this successor scope.

## 4. Successor resource measurement evidence

The exact canonical resource asset remains:

```text
RESOURCE_ASSET_ID=SP007-RO-001-EVAL-RESOURCE-EFFICIENCY-V1
RESOURCE_ASSET_SHA256=a1ddea12b740886643fc396c62553b1ab954404090d16db499a57e933056a200
SCORING_METHOD=RESOURCE_MEASUREMENT_RECORD_V1
FROZEN_PROBE_COUNT=8
WARMUP_RUNS_PER_PROBE=1
MEASURED_RUNS_PER_PROBE=3
```

Each measured run must record exactly:

```text
MODEL_ARTIFACT_BYTES
PEAK_RSS_BYTES
TIME_TO_FIRST_TOKEN_MS
DECODE_TOKENS_PER_SECOND
WALL_CLOCK_MS
```

The new resource-result validator binds every record to:

- the exact pre-execution subject SHA-256;
- one exact frozen candidate and revision;
- the exact resource asset identity;
- the exact execution environment identity;
- all eight frozen probe identities;
- one warmup and exactly three measured records per probe;
- the candidate model-artifact byte identity from the exact execution subject;
- a canonical self SHA-256.

No threshold PASS or winner is created by recording measurements.

## 5. Composed execution-evidence bundle

The new composed validator requires all of the following to agree:

```text
EXACT_PREEXECUTION_SUBJECT=VALID
EXACT_FROZEN_PROTOCOL_IDENTITY=MATCH
TOURNAMENT_EVIDENCE_PACK=VALID
EXECUTION_ENVIRONMENT_IDENTITY=MATCH
EXECUTION_AUTHORITY_IDENTITY=MATCH
RESOURCE_RESULT_STORE=EXACTLY_REFERENCED_RECORDS_ONLY
ONE_RESOURCE_RESULT_PER_CANDIDATE=REQUIRED
RESOURCE_EFFICIENCY_VALUE_IDENTITY=RESOURCE_RESULT_SHA256
RESOURCE_EFFICIENCY_EVALUATOR_ID=SP007_RO_001_RESOURCE_MEASUREMENT_EVALUATOR_V1
```

Opaque, missing, extra, cross-candidate, cross-environment, or unbound resource records fail closed.

## 6. Additional pre-execution invariants

The subject now explicitly requires:

```text
A1_A14_APPLICABLE_STATE=PASS
A15_STATE=AUTHORIZED_TO_CONSTRUCT
A15_AUTHORIZATION_DECISION_ID=REQUIRED
NETWORK_DURING_EXECUTION=false
AUTHORIZED_SPEND_USD=0
CREDENTIALS_USED=false
GATED_ASSETS_USED=false
PRIVATE_GOLD_USED=false
PHI_USED=false
WINNER_SELECTION_PERFORMED=false
```

These structural fields do not themselves create authority. The exact-subject execution lock remains the final repository-level protection against caller-owned favorable values.

## 7. Current live state remains blocked

```text
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
LIVE_SP007_PREEXECUTION_SUBJECT=ABSENT
LIVE_FOUR_CANDIDATE_COMPLETE_BUNDLE_BINDINGS=INCOMPLETE
LIVE_FOUR_CANDIDATE_RUNTIME_BINDINGS=INCOMPLETE
LIVE_RESOURCE_BINDING=INCOMPLETE
LIVE_ACCESS_BINDING=INCOMPLETE
A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
SUCCESSOR_PASS_PREFLIGHT=NO
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_PERFORMED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 8. Qualification

Before merge, require exact-head qualification through the existing E004 research-component workflow, including compile, focused tournament and pre-execution tests, Spec 007 regression, full repository regression, and diff-whitespace verification.

Independent repository review remains optional by default under FD-007. Service silence, billing exhaustion, or skipped bot review is not substantive review PASS.
