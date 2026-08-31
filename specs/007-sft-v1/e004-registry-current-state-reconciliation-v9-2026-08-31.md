# E004 Registry Current-State Reconciliation V9 — 2026-08-31

**Spec:** 007 SFT V1  
**Artifact class:** append-only component current-state reconciliation  
**Canonical base:** `05c5d4840f868d782c7d36c87970e30986ed3781`  
**Authority effect:** NONE  
**Runtime-evidence execution effect:** NONE  
**Model conversion authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation:** ABSENT_NOT_AUTHORIZED  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose and authoritative relationship

Record the exact component-scoped E004 frontier after canonical PR #144 implemented the offline deterministic `SP007-RO-001` scope-binding control plane.

The authoritative relationship remains deliberately split:

```text
GLOBAL_FULL_MULTI_ROLE_E004_FRONTIER_RECORD=specs/007-sft-v1/e004-registry-current-state-reconciliation-v7-2026-08-30.md
PREVIOUS_COMPONENT_E004_FRONTIER_RECORD=specs/007-sft-v1/e004-registry-current-state-reconciliation-v8-2026-08-31.md
CURRENT_COMPONENT_E004_FRONTIER_RECORD=specs/007-sft-v1/e004-registry-current-state-reconciliation-v9-2026-08-31.md
V9_SUPERSEDES_V8_FOR_EXACT_COMPONENT_SCOPE=YES
V9_SUPERSEDES_V7_GLOBALLY=NO
```

`specs/README.md` and the existing E004 task ledger remain global/full-multi-role records unless separately reconciled. V9 governs only `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`.

## 2. Canonical implementation transition

PR #144 is canonically merged:

```text
PR144=MERGED
PR144_TITLE=feat(spec007): enforce research-only component scope
PR144_CANONICAL_BASE=123925f81b4beba5d4d1016b53e3f2a191f04ace
PR144_QUALIFIED_HEAD=9a5d141ed9ee93098bb07579fadd01dfbb6c257f
PR144_MERGE=05c5d4840f868d782c7d36c87970e30986ed3781
PR144_MERGE_TREE=0df390c90eee818a6f99ac2e9508157ced8d400c
```

The initial PR #144 head received `MATERIAL_BLOCKER=YES` because sentinel fixture IDs, gradient content-scope PASS state, and scope-binding identity were not immutable content identities. That finding was accepted and repaired before merge.

Fresh independent exact-head review on `9a5d141ed9ee93098bb07579fadd01dfbb6c257f` returned:

```text
MATERIAL_BLOCKER=NO
INITIAL_IDENTITY_BINDING_BLOCKER_CLOSED=YES
GIT_DIFF_CHECK=PASS
AST_PARSE=PASS
```

Focused reviewer-environment execution additionally observed:

```text
RECONSTRUCTED_COMPILEALL=PASS
FOCUSED_TEST_COMMAND=pytest -q tests/spec007/test_research_scope.py
FOCUSED_TEST_RESULT=15 passed in 0.11s
FULL_REPOSITORY_REGRESSION_REEXECUTED_BY_PR144_REVIEW=NO
```

The focused result is evidence only for the new research-scope logic and tests. It is not represented as a new full-repository qualification run and does not alter historical I041/I042 evidence.

## 3. Offline deterministic blocker closed

V8 identified a genuine deterministic enforcement gap. PR #144 closes that gap.

The canonical implementation now provides content-addressed records and fail-closed validators for:

```text
RESEARCH_COMPONENT_SCOPE_BINDING_CONTRACT=IMPLEMENTED
RESEARCH_COMPONENT_SCOPE_BINDING_SELF_SHA256=REQUIRED
RESEARCH_COMPONENT_SENTINEL_FIXTURE_CONTRACT=IMPLEMENTED
RESEARCH_COMPONENT_SENTINEL_FIXTURE_SELF_SHA256=REQUIRED
RESEARCH_COMPONENT_CONTENT_SCOPE_VERIFICATION_CONTRACT=IMPLEMENTED
RESEARCH_COMPONENT_CONTENT_SCOPE_VERIFICATION_SELF_SHA256=REQUIRED
RESEARCH_COMPONENT_GUARD_SNAPSHOT_CONTRACT=IMPLEMENTED
RESEARCH_COMPONENT_GUARD_SNAPSHOT_SELF_SHA256=REQUIRED
```

The scope binding freezes exact `run_manifest_id` and canonical `run_manifest_sha256`.

Each gradient-bearing record must resolve:

```text
ROLE_CLASS=LEARNER_RESEARCHER
KNOWLEDGE_PLACEMENT=DURABLE_WEIGHT_ELIGIBLE
CONTENT_SCOPE_VERIFICATION=CONTENT_ADDRESSED_AND_EXACT_RECORD_BOUND
TARGET_CAPABILITY_SET=FROZEN_NON_CLINICAL_ADMITTED_SET_ONLY
```

Each sentinel fixture must resolve by immutable content identity and remain abort/disqualify-only. The complete seven-guard set must be bound exactly once.

A future real guard snapshot must:

- be content-addressed;
- bind the exact scope-binding SHA-256;
- bind the exact RunManifest SHA-256;
- use exactly the sentinel fixture SHA-256 set frozen by that scope binding;
- report zero violations for all seven guards;
- have disposition `PASS`.

Historical/global execution authority is explicitly insufficient to authorize the successor component by itself.

## 4. What PR #144 does not create

No real execution evidence is produced by the implementation merge.

```text
REAL_RESEARCH_COMPONENT_SCOPE_BINDING_FOR_LIVE_RUN=ABSENT
REAL_RESEARCH_COMPONENT_CONTENT_SCOPE_VERIFICATIONS=ABSENT
REAL_RESEARCH_COMPONENT_SENTINEL_FIXTURE_SET_FOR_LIVE_RUN=ABSENT
REAL_RESEARCH_COMPONENT_GUARD_SNAPSHOT=ABSENT
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=NONE
SUCCESSOR_SCOPE_MODEL_EXECUTION_OCCURRED=NO
SUCCESSOR_SCOPE_TRAINING_OCCURRED=NO
```

The contracts can validate real records later; they do not fabricate those records now.

## 5. Reviewer and clinical-threshold state remains scope-separated

For the exact component scope only:

```text
COMPONENT_EXTERNAL_CLINICAL_REVIEW_REQUIRED=NO
COMPONENT_EXTERNAL_STATISTICAL_REVIEW_REQUIRED=NO
COMPONENT_T1_A2_POPULATION_THRESHOLD_REVIEW_BLOCKER_CURRENT=NO
COMPONENT_POPULATION_CLINICAL_THRESHOLDS_RECLASSIFIED_AS_PASS=NO
CLINICAL_REVIEW_EVIDENCE_CREATED=NO
```

The global/full-multi-role reviewer and clinical-threshold requirements remain unchanged under V7 and the global ledger.

## 6. Live GitHub Actions transport recheck

Fresh repository Actions inspection after PR #144 still reports `total_count=98` and the newest run remains the failed one-shot bootstrap:

```text
NEWEST_ACTIONS_RUN=33256775421
NEWEST_ACTIONS_RUN_NAME=E004 runtime evidence dispatch bootstrap
NEWEST_ACTIONS_RUN_HEAD=6aa5e7a210452fd367e41343f08abee252ef7ad9
NEWEST_ACTIONS_RUN_EVENT=push
NEWEST_ACTIONS_RUN_CONCLUSION=failure
TARGET_RUNTIME_EVIDENCE_WORKFLOW_DISPATCH_RUN_COUNT=0
AUTHORIZED_RUNTIME_EVIDENCE_RUNS_EXECUTED=0
AUTHORIZED_RUNTIME_EVIDENCE_RUNS_REMAINING=1
CONNECTED_FRESH_WORKFLOW_DISPATCH_CREATOR_AVAILABLE=NO
INSTALLABLE_WORKFLOW_DISPATCH_PLUGIN_FOUND=NO
```

The successful historical build-evidence run remains:

```text
E004_BOUNDED_BUILD_EVIDENCE_RUN=33187438094
E004_BOUNDED_BUILD_EVIDENCE_RESULT=success
AUTHORIZED_BUILD_MANUAL_RUN_ALLOWANCE_REMAINING=0
```

No bootstrap rerun, failed-job rerun, build-evidence rerun, alternate trigger workaround, or local execution substitute is authorized.

## 7. Conversion remains operationally blocked

PR #144 does not change the canonical conversion execution checklist.

The future conversion authorization still requires real operational identities including:

```text
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY
EXACT_LOCAL_SOURCE_DIRECTORY
EXACT_LOCAL_SOURCE_DIRECTORY_BASENAME
NORMALIZATION_OR_METADATA_POLICY
PYTHON_RUNTIME_IDENTITY
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256
CONVERSION_RUNTIME_EXECUTABLE_SHA256
BUILD_ENVIRONMENT_MANIFEST_SHA256
EXACT_CONVERSION_ARGV_WITHOUT_PLACEHOLDERS
NETWORK_BOUNDARY_RUNTIME_ENFORCEMENT
CREDENTIAL_STATE_RUNTIME_ATTESTATION
EXACT_STORAGE_BOUNDARY_IDENTITY
RETENTION_ENFORCEMENT_IDENTITY
EXACT_COMPUTE_RESOURCE_IDENTITY
ZERO_INCREMENTAL_SPEND_DISPOSITION
```

Those are operational evidence requirements, not repository placeholders.

```text
PERSISTENT_CONVERSION_SUBJECT_WORKSPACE=INCOMPLETE
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
```

## 8. Contamination, resources, A15, and winner remain blocked

```text
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
CONTAMINATION_EVIDENCE=INCOMPLETE
COMPONENT_SPECIFIC_GOVERNANCE_RIGHTS_RESOURCE_BINDINGS=INCOMPLETE
OTHER_E004_FINANCE_RESOURCE_EVIDENCE=INCOMPLETE_UNLESS_SEPARATELY_PROVEN
COMPONENT_A1_A14_EQUIVALENT_EXACT_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
COMPONENT_BACKBONE_WINNER=NEEDS_EVIDENCE
```

No E005 decision is reachable until actual tournament evidence exists under the exact applicable protocol and authorities.

## 9. Component E004 current state

PR #144 closes the offline scope-enforcement implementation gap but does not close E004.

```text
COMPONENT_SCOPE_POLICY_IDENTITY=PASS_CANONICAL
COMPONENT_SCOPE_OFFLINE_ENFORCEMENT=PASS_CANONICAL_IMPLEMENTED
COMPONENT_REAL_GUARD_EVIDENCE=ABSENT
COMPONENT_RUNTIME_EVIDENCE=NOT_STARTED
COMPONENT_CONVERSION_PREREQUISITES=INCOMPLETE
COMPONENT_CONTAMINATION_PREREQUISITES=INCOMPLETE
COMPONENT_RESOURCE_ACCESS_BINDINGS=INCOMPLETE
COMPONENT_SUCCESSOR_EXECUTION_AUTHORITY=NONE
COMPONENT_A15=ABSENT_NOT_AUTHORIZED
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
COMPONENT_E005_STATE=NOT_REACHED
COMPONENT_TRAINING_AUTHORITY=NONE
```

The full multi-role state remains independently blocked and unchanged.

## 10. Furthest genuinely completable frontier

All V8 repository-only implementation work identified in priority items 1–3 is now complete:

```text
V8_PRIORITY_1_COMPONENT_ACTIVATION_CONTRACT=CLOSED_BY_PR144
V8_PRIORITY_2_EXISTING_VALIDATOR_GAP_ASSESSMENT=CLOSED_GAP_CONFIRMED
V8_PRIORITY_3_MINIMAL_OFFLINE_VALIDATOR_DELTA=CLOSED_BY_PR144
```

Priority item 4 is preserved by non-action: the existing one-run runtime-evidence allowance and no-workaround transport boundary remain unchanged.

Priority item 5 is still fail-closed: separate exact authority remains required before successor model execution, model conversion, contamination execution, A15 activation, or training.

No further repository-only commit may claim progress by replacing absent runtime, model, contamination, resource, guard, or authority evidence with prose.

## 11. Claims boundary

```text
SAFE_FOR_PATIENT_USE=NO
CLINICALLY_VALIDATED=NO
CLINICAL_GRADE=NO
CLINICALLY_SUPERIOR=NO
DEPLOYMENT_READY=NO
RELEASE_READY=NO
PATIENT_BENEFIT_PROVEN=NO
SYSTEM_SAFETY_PASS=NO
TRAINING_AUTHORITY=NONE
```

## Exit evidence

This V9 reconciliation is ready for canonical merge only if fresh exact-head independent repository review confirms:

```text
PR144_IDENTITIES_MATCH_CANONICAL_GIT=YES
PR144_INITIAL_MATERIAL_FINDING_REPAIRED=YES
PR144_FINAL_MATERIAL_BLOCKER=NO
V9_SCOPE_IS_COMPONENT_ONLY=YES
V7_REMAINS_GLOBAL_FULL_MULTI_ROLE_FRONTIER=YES
OFFLINE_SCOPE_ENFORCEMENT_GAP_CLOSED_WITHOUT_REAL_EVIDENCE_FABRICATION=YES
REAL_SCOPE_BINDING_AND_GUARD_SNAPSHOT_REMAIN_ABSENT=YES
TARGET_RUNTIME_EVIDENCE_DISPATCH_COUNT_REMAINS_ZERO=YES
TARGET_RUNTIME_EVIDENCE_ALLOWANCE_REMAINS_ONE=YES
NO_RERUN_OR_TRIGGER_WORKAROUND_CREATED=YES
CONVERSION_BLOCKERS_PRESERVED=YES
CONTAMINATION_BLOCKERS_PRESERVED=YES
RESOURCE_ACCESS_A15_BLOCKERS_PRESERVED=YES
NO_SUCCESSOR_EXECUTION_AUTHORITY_CREATED=YES
NO_TRAINING_AUTHORITY_CREATED=YES
NO_FALSE_E004_CLOSE=YES
NO_FALSE_E005_ENTRY=YES
MATERIAL_BLOCKER=NO
```
