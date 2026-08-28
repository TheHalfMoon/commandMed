# E004 Registry Current-State Reconciliation V3 — 2026-08-28

**Spec:** 007 SFT V1  
**Artifact class:** append-only current-state reconciliation  
**Canonical base:** `20a3c5fb731155af339ce270af3128b010114378`  
**Canonical base tree:** `965d6473326702ea0e4a686c15b7c0d3ff23bd37`  
**Authority effect:** NONE  
**Execution effect:** NONE  
**Spend:** USD 0

## Purpose

Reconcile the live Spec 007 / E004 frontier after canonical PR #121 established a reviewed E002 public-source integrity workflow and canonical PR #122 recorded successful execution evidence from run `33183096268`.

Earlier current-state records remain immutable historical evidence. This V3 record supersedes only stale **current-state interpretation** that said no connected E002 acquisition path was available or that commandMed-local source-byte integrity had never been recomputed.

```text
HISTORICAL_RECORDS_PRESERVED=YES
V1_V2_REGISTRY_RECONCILIATIONS_PRESERVED=YES
PR117_PR118_PR119_HISTORY_PRESERVED=YES
PR121_PR122_EVIDENCE_NOW_CONTROLLING_FOR_LOCAL_INTEGRITY=YES
AUTHORITY_EXPANDED=NO
REAL_E004_GATE_PASS_CREATED=NO
```

## Canonical evidence chain added after V2

```text
PR121=ci(e002): add bounded public source integrity evidence lane
PR121_QUALIFIED_HEAD=cb05e8ec48d0b0c3ea209402ca3632d1340a3fbd
PR121_MERGE=dd85e9e22de0dccf0043c8905be1c2d9fb5f68a4
PR121_MERGE_TREE=389d235ac072f6a094db49ceada13e3490daca96

E002_EXECUTION_BRANCH=evidence/e002-source-integrity-run-v1
E002_EXECUTION_MARKER_HEAD=d4404ee56c7b2fb1018650c5c05e9dc3eb5b59b2
E002_WORKFLOW_RUN=33183096268
E002_WORKFLOW_RUN_ATTEMPT=1
E002_WORKFLOW_RUN_EVENT=push
E002_WORKFLOW_RUN_CONCLUSION=success

PR122=docs(e002): record exact local source integrity run evidence
PR122_QUALIFIED_HEAD=871b88667f4846e8b3146399d484a97e38236af5
PR122_MERGE=20a3c5fb731155af339ce270af3128b010114378
PR122_MERGE_TREE=965d6473326702ea0e4a686c15b7c0d3ff23bd37
```

The PR #122 exact-head review independently verified the run, both job manifests, all local rows against canonical provider identities, correct ephemeral-local scope, zero artifacts, the unconsumed separate build-dispatch allowance, no false gate closure, and no downstream authority expansion.

## E002 local source acquisition/integrity — blocker partially resolved

The old current-state statement that no connected acquisition route existed is no longer current.

A reviewed GitHub Actions path successfully acquired and cryptographically recomputed the exact selected source bundles within existing E002 authority.

```text
E002_PUBLIC_SOURCE_ACQUISITION_PATH=EXECUTED_SUCCESSFULLY
RUN_ID=33183096268
RUN_CONCLUSION=success
WORKFLOW_ARTIFACT_COUNT=0
```

### Granite PRIMARY

```text
GRANITE_JOB_ID=98889052166
GRANITE_JOB_CONCLUSION=success
GRANITE_LOCAL_SELECTED_FILE_COUNT=9
GRANITE_LOCAL_SOURCE_DIRECTORY_BASENAME=granite-4.0-350m-base
GRANITE_LOCAL_INTEGRITY_MANIFEST_SHA256=67eac7cb98525612030aa608a1eb5d473e5045319ce4ce78a6aa4174f78b646a
GRANITE_LOCAL_SOURCE_WEIGHT_SHA256_RECOMPUTED=YES_ON_RUN_33183096268
GRANITE_LOCAL_INTEGER_SOURCE_WEIGHT_BYTES=704786224_ON_RUN_33183096268
GRANITE_LOCAL_SELECTED_NON_WEIGHT_SHA256_SET=RECOMPUTED_AND_MATCHED_ON_RUN_33183096268
```

### Qwen3-4B CONTROL

```text
QWEN_CONTROL_JOB_ID=98889051893
QWEN_CONTROL_JOB_CONCLUSION=success
QWEN_CONTROL_LOCAL_SELECTED_FILE_COUNT=11
QWEN_CONTROL_LOCAL_SOURCE_DIRECTORY_BASENAME=Qwen3-4B-Base
QWEN_CONTROL_LOCAL_INTEGRITY_MANIFEST_SHA256=ac831cb724268dcb54f90d9bf41c972ba25d18f7a087e56a27933f69f84b2ab8
QWEN_LOCAL_SOURCE_WEIGHT_SHA256_PER_SHARD=RECOMPUTED_AND_MATCHED_ON_RUN_33183096268
QWEN_LOCAL_INTEGER_SOURCE_WEIGHT_BYTES_PER_SHARD=3957900840,3987450520,99630640
QWEN_LOCAL_SELECTED_NON_WEIGHT_SHA256_SET=RECOMPUTED_AND_MATCHED_ON_RUN_33183096268
```

Current evidence interpretation is therefore:

```text
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=PASS_EPHEMERAL_EVIDENCE_ON_RUN_33183096268
LOCAL_SELECTED_NON_WEIGHT_INPUT_SHA256_SET=RECOMPUTED_AND_MATCHED_ON_RUN_33183096268
LOCAL_SOURCE_DIRECTORY_BASENAME_ATTESTATION=PASS_ON_RUN_33183096268
```

The old generic interpretation:

```text
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
LOCAL_SELECTED_NON_WEIGHT_INPUT_SHA256_SET=NEEDS_EVIDENCE
LOCAL_SOURCE_DIRECTORY_BASENAME_ATTESTATION=NEEDS_EVIDENCE
```

is superseded only for **evidence existence on run `33183096268`**.

## Ephemeral evidence is not a persistent conversion workspace

The source bytes were held only on ephemeral GitHub-hosted runners. The workflow uploaded no artifacts and intentionally did not retain model bytes.

```text
PERSISTENT_LOCAL_SOURCE_BUNDLE_PRESENT=NO
PERSISTENT_EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
FUTURE_CONVERSION_TIME_SOURCE_PATH=NEEDS_EVIDENCE
EXACT_LOCAL_OUTPUT_DIRECTORY=NEEDS_EVIDENCE
```

Therefore no placeholder-bearing future conversion argv can become executable merely because integrity was proven on an earlier ephemeral runner.

```text
EXACT_CONVERSION_ARGV_WITHOUT_PLACEHOLDERS=NEEDS_EVIDENCE
CONVERSION_EXECUTION_AUTHORITY=NONE
MODEL_CONVERSION_EXECUTION_OCCURRED=NO
```

## Runtime/dependency/environment frontier remains blocked

The E002 integrity workflow did not install or execute the pinned converter/runtime stack.

Current unresolved execution-environment evidence remains:

```text
PYTHON_RUNTIME_IDENTITY_FOR_CONVERSION=NEEDS_EVIDENCE
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256=NEEDS_EVIDENCE
DEPENDENCY_PACKAGE_HASH_SET=NEEDS_EVIDENCE
CONVERSION_RUNTIME_EXECUTABLE_OR_INTERPRETER_IDENTITY=NEEDS_EVIDENCE
LLAMA_QUANTIZE_EXECUTABLE_SHA256=NEEDS_EVIDENCE
BUILD_ENVIRONMENT_MANIFEST_SHA256=NEEDS_EVIDENCE
NETWORK_DISABLEMENT_OR_NAMESPACE_ENFORCEMENT_IDENTITY=NEEDS_EVIDENCE
CREDENTIAL_SCAN_OR_ENVIRONMENT_ATTESTATION_IDENTITY_FOR_CONVERSION=NEEDS_EVIDENCE
EXACT_STORAGE_BOUNDARY_IDENTITY=NEEDS_EVIDENCE
FILESYSTEM_OR_VOLUME_IDENTITY=NEEDS_EVIDENCE
ACCESS_CONTROL_OR_PROCESS_ISOLATION_IDENTITY=NEEDS_EVIDENCE
RETENTION_ENFORCEMENT_IDENTITY=NEEDS_EVIDENCE
EXACT_COMPUTE_RESOURCE_IDENTITY_FOR_CONVERSION=NEEDS_EVIDENCE
EXPECTED_CPU_RAM_DISK_ENVELOPE_FOR_CONVERSION=NEEDS_EVIDENCE
EXPECTED_MAX_WALLCLOCK_FOR_CONVERSION=NEEDS_EVIDENCE
ZERO_INCREMENTAL_SPEND_DISPOSITION_FOR_CONVERSION=NEEDS_EVIDENCE
```

The canonical Decision B reconciliation explicitly requires then-current authority that actually permits runtime/dependency/environment creation or execution before that work may start. Successful E002 byte acquisition does not create such authority.

## Build-evidence lane remains separate and unconsumed

The successful E002 push-triggered integrity run does not satisfy or consume the separately bounded E004 `llama-quantize` build-evidence allowance.

Latest direct recheck after the E002 run:

```text
WORKFLOW_DISPATCH_RUN_COUNT=0
AUTHORIZED_BUILD_MANUAL_RUN_EXECUTED=NO
AUTHORIZED_BUILD_MANUAL_RUN_ALLOWANCE_REMAINING=1
AUTHORIZED_BUILD_MANUAL_RUN_TRIGGER=workflow_dispatch_only
BUILD_EXECUTION_OCCURRED_ON_GITHUB_ACTIONS_PATH=NO
BUILD_PASS=NO
```

The connected GitHub tool surface still exposes no fresh `workflow_dispatch` initiation action. Push-triggered E002 integrity evidence is not an authorized substitute for the build-only lane.

## Scientific/governance frontier unchanged

```text
T1_A2=INCOMPLETE_REAL_EVIDENCE_NUMERIC_POLICY_AND_QUALIFIED_REVIEW
D34_A3_A4=BLOCKED_BY_T1
G1_A5_REAL_GATE_PASS=NO
G2_A6_REAL_GATE_PASS=NO
G3_A8_REAL_GATE_PASS=NO
G4_A12_REAL_GATE_PASS=NO
REAL_PERSONNEL_ACCESS_FINANCE_EVIDENCE=INCOMPLETE
REAL_A1_TO_A14_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
```

Repository/AI review cannot impersonate qualified clinical/statistical review, independent governance/privacy/rights evidence, real personnel/access/finance evidence, or A15 activation.

The current no-outreach boundary remains fully active.

## Contamination ordering unchanged

```text
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION=NOT_STARTED
A11_ORDERING_PRESERVED=YES
D34_H1_I1_F1_J1_A15_DEPENDENCY_ORDER_PRESERVED=YES
```

No contamination assessment is authorized or implied by source-byte integrity evidence.

## Current E004 frontier after PR #122

The prior `NO_ELIGIBLE_REAL_GATE_TRANSITION_AVAILABLE_ON_CURRENT_SURFACE=YES` statement from before the E002 lane existed has been superseded by the successful acquisition/integrity transition itself.

That transition is now complete. The newly remaining frontier again has no executable transition on the currently connected surface under current authority because:

1. persistent conversion-workspace and conversion runtime/dependency/environment work requires authority not currently granted;
2. the already-authorized build-only lane requires a fresh `workflow_dispatch` action not exposed by the connected GitHub tool surface;
3. T1/A2 and G1-G4 require real human scientific/governance evidence that repository/AI review cannot impersonate, while external outreach is currently prohibited;
4. A11 contamination authority is absent;
5. a real A1-A14 snapshot and separate A15 activation remain absent.

```text
LATEST_REAL_TRANSITION=E002_EPHEMERAL_LOCAL_SOURCE_INTEGRITY_PASS
LATEST_REAL_TRANSITION_RUN=33183096268
FURTHEST_CURRENT_STATE=E004_BLOCKED_PREFLIGHT_AFTER_LOCAL_INTEGRITY_PASS
NO_FURTHER_ELIGIBLE_REAL_GATE_TRANSITION_AVAILABLE_ON_CURRENT_SURFACE=YES
```

This is a current-surface statement, not a permanent project impossibility.

## Current authoritative state

```text
SPEC007_LIFECYCLE=AUTHORIZED_TO_START
E001=CLOSED_CANONICAL
E002=CLOSED_CANONICAL
E003=CLOSED_CANONICAL
E002_EPHEMERAL_LOCAL_INTEGRITY_EVIDENCE=PASS
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Any older current-state statement that lists absence of local byte recomputation or absence of any connected E002 acquisition route as a current blocker must now be interpreted through canonical PR #122 and this later V3 reconciliation.

## Dependency-safe next work

Under current authority and connected tooling, ordinary work may only proceed if one of the following becomes genuinely executable:

1. the already-authorized exact build-evidence manual run becomes triggerable through a real fresh `workflow_dispatch` action while all pre-run conditions still pass;
2. separately bounded authority is canonically granted for an exact runtime/dependency/environment preparation action that is actually executable without smuggling conversion authority;
3. real scientific/governance/personnel/access/finance evidence becomes available through a path permitted by then-current governance;
4. contamination/A15 authority becomes separately canonical only in correct dependency order;
5. append-only reconciliation is required by newer canonical evidence.

Generic continuation approval does not create any separately gated authority above.

## Capture state

```text
CANONICAL_MAIN_AT_CAPTURE=20a3c5fb731155af339ce270af3128b010114378
CANONICAL_TREE_AT_CAPTURE=965d6473326702ea0e4a686c15b7c0d3ff23bd37
E002_INTEGRITY_RUN=33183096268
E002_INTEGRITY_RUN_CONCLUSION=success
GRANITE_INTEGRITY_JOB=98889052166_success
QWEN_CONTROL_INTEGRITY_JOB=98889051893_success
WORKFLOW_ARTIFACT_COUNT=0
WORKFLOW_DISPATCH_RUN_COUNT=0

REGISTRY_CURRENT_STATE=RECONCILED_V3_AFTER_PR121_PR122
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BUILD_PASS=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```
