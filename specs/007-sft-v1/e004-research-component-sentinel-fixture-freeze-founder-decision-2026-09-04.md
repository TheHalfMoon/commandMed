# E004 Research-Component Sentinel Fixture Freeze Founder Decision — 2026-09-04

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical decision-request merge:** `b607594d02073d17ad0f8ccb81041eb89eb7522c`  
**Canonical base for this decision record:** `f85c04b9213cf1dace10f6c6df5ed49de61ad790`  
**Decision owner:** Founder  
**Decision class:** `E004_SENTINEL_FIXTURE_FREEZE_DECISION_B`  
**Decision state:** SELECTED  
**Sentinel construction performed by this decision record:** NO  
**Sentinel execution performed by this decision record:** NO  
**DatasetSnapshot created by this decision record:** NO  
**Training performed:** NO  
**Current authorized spend:** USD 0

## 1. Operative Founder decision

After the canonical decision surface was merged, the Founder supplied the exact required decision text:

```text
FOUNDER_SENTINEL_FIXTURE_FREEZE_DECISION=E004_SENTINEL_FIXTURE_FREEZE_DECISION_B
```

This is the exact Decision B token defined by:

`specs/007-sft-v1/e004-research-component-sentinel-fixture-freeze-founder-decision-request-2026-09-04.md`

Therefore the exact bounded authority becomes:

```text
FOUNDER_SENTINEL_FIXTURE_FREEZE_DECISION=E004_SENTINEL_FIXTURE_FREEZE_DECISION_B
SENTINEL_FIXTURE_CONSTRUCTION_AUTHORITY=AUTHORIZED_EXACT_PREDECLARED_SP007_RO_001_SENTINEL_7_ONLY
SENTINEL_FIXTURE_FREEZE_AUTHORITY=AUTHORIZED_EXACT_PREDECLARED_SP007_RO_001_SENTINEL_7_ONLY
SENTINEL_FIXTURE_RECORD_COUNT=7
SENTINEL_FIXTURE_SET_SHA256=5a2bd28b391010c9575c99654899cd442fea8d94cbb4176045b654c940fa2fd3
SENTINEL_FIXTURE_SHA256_SET_SHA256=b65b36689cf2006bad8b446536d50ccd3f3440a4b244c044a1b26409aea0fef2
SENTINEL_FIXTURE_SCOPE_ID=SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1
SENTINEL_OPTIMIZATION_FEEDBACK_ALLOWED=false
SENTINEL_EXECUTION_AUTHORITY_EXPANSION=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 2. Exact authorized subject

This authority is limited to the seven records predeclared verbatim in the canonical decision-request artifact. No prompt, fixture ID, guard ID, expected action, optimization-feedback flag, fixture hash, record count, set hash, or scope substitution is permitted.

```text
SENTINEL_RECORD_IDS=SP007-RO-001-SENTINEL-001,SP007-RO-001-SENTINEL-002,SP007-RO-001-SENTINEL-003,SP007-RO-001-SENTINEL-004,SP007-RO-001-SENTINEL-005,SP007-RO-001-SENTINEL-006,SP007-RO-001-SENTINEL-007
SENTINEL_REQUIRED_GUARD_COUNT=7
SENTINEL_CANDIDATE_SET_SHA256=5a2bd28b391010c9575c99654899cd442fea8d94cbb4176045b654c940fa2fd3
SENTINEL_CANDIDATE_FIXTURE_SHA256_SET_SHA256=b65b36689cf2006bad8b446536d50ccd3f3440a4b244c044a1b26409aea0fef2
```

## 3. Construction and freeze authority

Decision B authorizes only repository-safe construction, schema/validator verification, and canonical freezing of exactly the seven predeclared records.

The construction must fail closed on any mismatch in:

- fixture content;
- fixture ID;
- guard ID;
- expected action;
- optimization-feedback flag;
- per-record `fixture_sha256`;
- set-level SHA-256 identities;
- required guard coverage;
- scope ID;
- schema or validator result.

No replacement or alternate fixture is authorized.

## 4. Execution and optimization boundary

Decision B does not authorize model inference or create guard PASS evidence.

```text
SENTINEL_MODEL_INFERENCE_PERFORMED=NO
SENTINEL_GUARD_SNAPSHOT_PRESENT=NO
SENTINEL_GUARD_PASS_CREATED=NO
MODEL_EXECUTION_AUTHORITY_EXPANSION=NONE
TOURNAMENT_EXECUTION_AUTHORITY_EXPANSION=NONE
TRAINING_AUTHORITY=NONE
CAN_RANK_CHECKPOINTS=NO
CAN_TUNE_RECIPE=NO
CAN_CHANGE_HYPERPARAMETERS=NO
CAN_CREATE_PREFERRED_EARLY_STOPPING=NO
CAN_BECOME_GRADIENT_TARGET=NO
CAN_BECOME_HIDDEN_CLINICAL_DEVELOPMENT_SET=NO
```

## 5. DatasetSnapshot remains separately blocked

```text
DATASET_SNAPSHOT_AUTHORITY=NONE
DATASET_SNAPSHOT_PRESENT=NO
QUARANTINE_VERIFICATION_IDENTITY_FOR_DATASET_SNAPSHOT=ABSENT
```

An exact sentinel freeze cannot be used to infer DatasetSnapshot authority.

## 6. Model, access, training, and spend boundaries

```text
MODEL_WINNER_SELECTED=NO
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
USER_MANAGED_CREDENTIAL_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 7. E004 effect

```text
SENTINEL_FREEZE_DECISION_CAPTURED=YES
EXACT_SENTINEL_7_CONSTRUCTION_REACHABLE=YES
EXACT_SENTINEL_7_FREEZE_REACHABLE=YES
DATASET_SNAPSHOT_REACHABLE=NO_PENDING_SEPARATE_AUTHORITY
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER_SELECTED=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

Decision B opens only component dependency 3. It does not authorize dependency 4 or any later runtime, model-selection, conversion, training, credential, procurement, payment, or spend unit.

## 8. Relationship to generic continuation approval

The exact Founder token above is the sole source of the new sentinel construction/freeze authority. Generic continuation instructions remain project intent but do not expand this authority.

## 9. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is optional by default for this bounded Founder-decision capture artifact.

Before merge, verify exact base/head/diff, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, exact Decision B correspondence with the canonical decision surface, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
