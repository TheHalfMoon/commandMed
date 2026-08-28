# E004 Registry Current-State Reconciliation — 2026-08-28

**Spec:** 007 SFT V1  
**Artifact class:** append-only current-state reconciliation  
**Canonical base at branch creation:** `a6b81a5dc78b75d7b9d25fdaa7df6fe77d6eecb2`  
**Canonical base tree:** `29d921b06e037d65e5a11541f0cf28394d5962f0`  
**Authority effect:** NONE  
**Execution effect:** NONE  
**Spend:** USD 0

## Purpose

Reconcile one stale current-state interpretation in the Spec 007 registry summary after canonical PRs #111 and #112.

The `specs/README.md` Spec 007 row remains historical/canonical repository text and is not rewritten by this record. Its current-state phrase that the remaining E004 blockers include a separately gated artifact prerequisite predates the canonical Decision B preparation/evidence reconciliation now recorded by PR #111 and the task-ledger reconciliation now recorded by PR #112.

This record supersedes only that stale **current-state interpretation**. It does not rewrite history, change lifecycle state, close E004, advance E005, or create any execution authority.

```text
HISTORICAL_REGISTRY_TEXT_PRESERVED=YES
CURRENT_STATE_INTERPRETATION_RECONCILED=YES
LIFECYCLE_STATE_CHANGED=NO
AUTHORITY_EXPANDED=NO
EXECUTION_PERFORMED=NO
```

## Canonical carrier chain

```text
PR111=docs(e004): reconcile live Decision B subject state
PR111_QUALIFIED_HEAD=717931e35de07f43895d777b8d2d49c7e1066061
PR111_MERGE=711627203905d84c9af7f1984f5b1922b7dacc51

PR112=docs(e004): reconcile task ledger frontier
PR112_QUALIFIED_HEAD=b6a913d165e4fba4ec9b3c50327e4ab747cab133
PR112_MERGE=a6b81a5dc78b75d7b9d25fdaa7df6fe77d6eecb2
PR112_MERGE_TREE=29d921b06e037d65e5a11541f0cf28394d5962f0
```

PR #112 preserves the E004 checkbox as unchecked and `BLOCKED_PREFLIGHT`. Its exact-head CodeRabbit review accepted the ledger reconciliation with no downstream authority expansion and `MATERIAL_BLOCKER=NO`.

## Current artifact/preparation truth

Canonical `ARTIFACT_DECISION_B` already provides bounded preparation authority for exactly these two conversion subjects:

```text
PRIMARY=ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
CONTROL=Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
CONTROL_WINNER_ELIGIBLE=NO
```

Canonical provider/static preparation now includes:

```text
PROVIDER_SOURCE_WEIGHT_IDENTITIES=BOUND
PROVIDER_INTEGER_SOURCE_WEIGHT_BYTES=BOUND
PROVIDER_SELECTED_NON_WEIGHT_INPUT_SURFACE=BOUND_AFTER_CORRECTION
NORMALIZATION_OR_METADATA_POLICY=CANONICAL_STATIC_POLICY_DEFINED
CONVERTER_RUNTIME_DEPENDENCY_SOURCE_MANIFESTS=BOUND
CONVERSION_EXECUTION_BOUNDARY_POLICY=CANONICAL_DESIGN_PREPARED
```

Therefore, a generic statement that E004 is currently blocked because separate artifact preparation authority is absent is stale.

This does **not** mean artifact execution readiness exists.

## Remaining Decision B local and operational blockers

The following remain unresolved and fail closed:

```text
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
LOCAL_SOURCE_DIRECTORY_BASENAME_ATTESTATION=NEEDS_EVIDENCE
PYTHON_RUNTIME_IDENTITY=NEEDS_EVIDENCE
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256=NEEDS_EVIDENCE
DEPENDENCY_PACKAGE_HASH_SET=NEEDS_EVIDENCE
BUILD_ENVIRONMENT_MANIFEST_SHA256=NEEDS_EVIDENCE
EXACT_CONVERSION_ARGV_WITHOUT_PLACEHOLDERS=NEEDS_EVIDENCE
EXACT_LOCAL_OUTPUT_DIRECTORY=NEEDS_EVIDENCE
NETWORK_BOUNDARY=NEEDS_OPERATIONAL_EVIDENCE
CREDENTIAL_STATE=NEEDS_OPERATIONAL_EVIDENCE
STORAGE_AND_RETENTION_POLICY=NEEDS_OPERATIONAL_EVIDENCE
EXACT_COMPUTE_RESOURCE_IDENTITY=NEEDS_EVIDENCE
ZERO_INCREMENTAL_SPEND_DISPOSITION=NEEDS_EVIDENCE
```

Public/provider metadata is not commandMed-local byte verification, and static design is not operational PASS.

## Build-evidence lane

The separately bounded `llama-quantize` build-evidence lane remains canonical:

```text
E004_CONVERSION_TOOLCHAIN_BUILD_AUTHORITY=AUTHORIZED_BOUNDED
CONVERTER_BUILD_EXECUTION_AUTHORITY=AUTHORIZED_EXACT_LLAMA_CPP_REVISION_BUILD_EVIDENCE_ONLY
LIVE_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
LIVE_WORKFLOW_GIT_BLOB_SHA1=710cb4e6ecf1b34e93d3dfa3d59e24c3d60d1d79
LIVE_WORKFLOW_SHA256=836175ee057e2a6802b47db00766119d54c2034b63c8487f138dc125285f226b
TRIGGER=workflow_dispatch_only
AUTHORIZED_MANUAL_RUN_EXECUTED=NO
AUTHORIZED_MANUAL_RUN_ALLOWANCE_REMAINING=1
BUILD_EXECUTION_OCCURRED_ON_GITHUB_ACTIONS_PATH=NO
BUILD_PASS=NO
```

The connected execution surface does not currently expose an operation to initiate a new `workflow_dispatch`. Re-running historical `push` failures is not an authorized substitute for the exact manual trigger.

## Independent E004 blockers unchanged

The non-artifact branches remain unresolved independently:

```text
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
QUALIFIED_CLINICAL_STATISTICAL_REVIEW=INCOMPLETE
REAL_GOVERNANCE_OPERATIONAL_EVIDENCE=INCOMPLETE
REAL_PERSONNEL_ACCESS_FINANCE_EVIDENCE=INCOMPLETE
REAL_A1_TO_A14_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
BACKBONE_WINNER=NEEDS_EVIDENCE
```

Repository review or generic continuation approval cannot impersonate qualified clinical/statistical review, real personnel/access/finance evidence, or a separately bound A15 activation decision.

## Authority boundary

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
MODEL_CONVERSION_AUTHORITY=NONE
QUANTIZATION_OF_MODEL_WEIGHTS_AUTHORITY=NONE
MODEL_LOADING_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY_EXPANSION=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

No statement in this record converts preparation authority into execution authority.

## Dependency-safe frontier after this reconciliation

The next genuinely eligible work remains limited to actions that already have exact authority and are possible on the active execution surface:

1. E002-bounded non-executing acquisition and local integrity evidence for exact frozen public artifacts, when an execution environment with working public-provider network access is available;
2. the single already-authorized manual build-evidence `workflow_dispatch`, only when the connected surface can initiate that exact trigger and all canonical pre-run conditions still pass;
3. repository-only append-only reconciliation when newer canonical evidence makes a current-state statement stale.

The following are not authorized by this record or by generic continuation approval:

- model conversion or model-weight quantization;
- model loading or inference beyond existing separately bounded authority;
- contamination assessment execution without its separate authority;
- training or optimization;
- Private Gold or PHI access;
- credentialed/gated access;
- procurement or spend.

## Current state

```text
CANONICAL_MAIN_AT_CAPTURE=a6b81a5dc78b75d7b9d25fdaa7df6fe77d6eecb2
CANONICAL_TREE_AT_CAPTURE=29d921b06e037d65e5a11541f0cf28394d5962f0
OPEN_PRS_AT_CAPTURE=0
ACTIONS_RUNS_ON_CANONICAL_HEAD_AT_CAPTURE=0

REGISTRY_STALE_ARTIFACT_BLOCKER_INTERPRETATION=SUPERSEDED_BY_PR111_PR112_CURRENT_STATE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BUILD_PASS=NO
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```
