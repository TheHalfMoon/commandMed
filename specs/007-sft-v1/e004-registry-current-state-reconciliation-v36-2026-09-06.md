# E004 Registry Current-State Reconciliation V36 — 2026-09-06

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Predecessor:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v35-2026-09-06.md`
**Candidate-bundle binding:** `specs/007-sft-v1/e004-successor-candidate-artifact-bundle-binding-v1-2026-09-06.md`
**Candidate-bundle set:** `specs/007-sft-v1/e004-successor-candidate-artifact-bundle-set-v1.json`
**Qualified PR:** #269
**Qualified exact head:** `0c4f11119b56cf55570b657e6091916050428905`
**Qualification run:** `34047859045`
**Qualification job:** `101526040276`
**Canonical merge:** `1be1690aa0b178ae1a0985407bacfdef1be73c6c`
**Canonical tree:** `bdb03821e3363ffeaf79133620c5d1090153fb1f`
**Artifact class:** deterministic append-only current-state / dependency-frontier overlay
**Authority effect:** none; no execution, A15, winner-selection, training, credential, or spend authority
**Current authorized spend:** USD 0

## 1. Purpose

Consume the qualified canonical candidate-artifact bundle binding introduced by PR #269 and recompute the exact successor frontier without promoting artifact identity into runtime compatibility or execution authority.

## 2. Exact-head qualification evidence

The E004 research-component control-plane workflow checked out exact PR head `0c4f11119b56cf55570b657e6091916050428905` and completed successfully on run `34047859045`, job `101526040276`.

Observed qualification:

```text
EXACT_HEAD_CHECKOUT=PASS
AUTHORITY_BIND=PASS
COMPILE_CHANGED_PYTHON=PASS
FOCUSED_CANDIDATE_BUNDLE_TESTS=17_PASS
FOCUSED_TOURNAMENT_TESTS=22_PASS
FOCUSED_PREEXECUTION_TESTS=16_PASS
FOCUSED_SNAPSHOT_REPAIR_TESTS=3_PASS
SPEC007_REGRESSION=308_PASS_PLUS_50_SUBTESTS_PASS
FULL_REPOSITORY_REGRESSION=957_PASS_PLUS_178_SUBTESTS_PASS
DIFF_WHITESPACE=PASS
WORKFLOW_CONCLUSION=SUCCESS
```

Runner observations were Ubuntu 24.04.4 / `ubuntu-24.04`, image version `20260831.293.1`, runner version `2.337.0`.

No submitted repository review or review thread existed on PR #269. Under FD-007, independent repository review is optional by default; no review PASS is claimed.

## 3. Newly closed deterministic artifact fields

The canonical bundle-set identity is:

```text
CANDIDATE_ARTIFACT_BUNDLE_SET_ID=SP007_RO_001_CANDIDATE_ARTIFACT_BUNDLE_SET_V1
CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256=ee97fe0751743cc0d3a564b8f91add3c336267f08f2da86bf125dd7333db83fd
COMPLETE_BUNDLE_SEMANTICS=CANONICAL_FILE_MANIFEST_SHA256_V1
```

Per candidate:

```text
QWEN06_COMPLETE_BUNDLE_SHA256=8b207e94ad7c5937dceced686603294ae5f150022ac2b355fee9997a408fc415
QWEN06_COMPLETE_BUNDLE_BYTES=408195248
QWEN06_PRIMARY_HARD_CAP_MARGIN_BYTES=325807952

QWEN35_COMPLETE_BUNDLE_SHA256=682ef5c8fb914feb5346d5153e26b83e6bb3bb834aa1313cba240b61c0657592
QWEN35_COMPLETE_BUNDLE_BYTES=585938673
QWEN35_PRIMARY_HARD_CAP_MARGIN_BYTES=148064527

GRANITE_COMPLETE_BUNDLE_SHA256=90c8061eefbe53328a9eb217d1163941a16387d5a078dc789dbccb159c0b41db
GRANITE_COMPLETE_BUNDLE_BYTES=714515562
GRANITE_PRIMARY_HARD_CAP_MARGIN_BYTES=19487638

CONTROL_COMPLETE_BUNDLE_SHA256=9d4e39cdff26b357a698371b4096167a7b70f07975d016460e4b7996399170b9
CONTROL_COMPLETE_BUNDLE_BYTES=8056508630
CONTROL_PRIMARY_HARD_CAP_APPLIES=NO
```

The CONTROL's three safetensors weight shards are bound by a canonical weight-shard manifest rather than a fabricated single-file digest:

```text
CONTROL_MODEL_ARTIFACT_IDENTITY_KIND=CANONICAL_WEIGHT_SHARD_MANIFEST_SHA256_V1
CONTROL_MODEL_ARTIFACT_SHA256=d7daa1f7a5f70276b29b71838f8e2c830a61f06b4e70c04de0987bd8c5b4a397
CONTROL_MODEL_ARTIFACT_BYTES=8044982000
```

Therefore:

```text
EXACT_COMPLETE_BUNDLE_SHA256_PER_CANDIDATE=PASS_BOUND
EXACT_COMPLETE_BUNDLE_BYTES_PER_CANDIDATE=PASS_BOUND
EXACT_CONTROL_COMPOSITE_MODEL_ARTIFACT_IDENTITY=PASS_BOUND
LIVE_FOUR_CANDIDATE_ARTIFACT_BUNDLE_BINDINGS=COMPLETE
```

The older E002 local-integrity manifest hashes remain valid evidence under their original manifest semantics and are not replaced or asserted equal to the new canonical file-manifest identities.

## 4. Runtime compatibility remains fail closed

The candidate bundle binding contains no runtime-compatibility field and creates no empirical model-load evidence.

```text
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=INCOMPLETE
RUNTIME_FORMAT_COMPATIBILITY_STATE_FOR_LIVE_SUBJECT=NOT_YET_PASS
LIVE_FOUR_CANDIDATE_RUNTIME_BINDINGS=INCOMPLETE
MODEL_RUNTIME_LOAD_PERFORMED=NO
```

Static runtime-family support from V33 remains evidence-only and must not be promoted to empirical compatibility PASS.

## 5. Execution-plan and argv fields remain unresolved

```text
EXACT_EXECUTION_PLAN_SHA256_PER_CANDIDATE=INCOMPLETE
EXACT_RUNTIME_ARGV_PER_CANDIDATE=INCOMPLETE
```

The next unit may define these only as deterministic non-executing control-plane identities against the already-bound runtime families. It must not execute a runtime or model merely to fill the fields.

## 6. Environment, resource, access, and finance remain fail closed

```text
EXACT_FUTURE_MODEL_EXECUTION_ENVIRONMENT=INCOMPLETE
EXACT_ENVIRONMENT_MANIFEST_SHA256=INCOMPLETE
EXACT_COMPUTE_RESOURCE_IDENTITY=INCOMPLETE
RESOURCE_AUTHORIZATION_BASIS=INCOMPLETE
EXPECTED_CPU_RAM_DISK_ENVELOPE=INCOMPLETE
EXPECTED_MAX_WALLCLOCK=INCOMPLETE
EXACT_ACCESS_BINDING_FOR_EXECUTION_SUBJECT=INCOMPLETE
EXACT_CREDENTIAL_STATE_BINDING=INCOMPLETE
NETWORK_DURING_EXECUTION_BINDING=INCOMPLETE
ZERO_INCREMENTAL_SPEND_TOURNAMENT_RESOURCE_BINDING=INCOMPLETE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 7. A1-A14, A15, and exact-subject lock remain ordered

```text
A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
A15_IS_SOLE_REMAINING_BLOCKER=NO
GENERIC_GO_AHEAD_COUNTS_AS_A15_ACTIVATION=NO
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
LIVE_SP007_PREEXECUTION_SUBJECT=ABSENT
SUCCESSOR_PASS_PREFLIGHT=NO
MODEL_EXECUTION_NOW=NOT_AUTHORIZED_BY_GATE_STATE
TOURNAMENT_EXECUTION_NOW=NOT_AUTHORIZED_BY_GATE_STATE
```

## 8. Task-ledger interpretation

```text
E004_TASK_CHECKBOX=REMAINS_INCOMPLETE
E004_EVALUATION_ASSET_QUALIFICATION_SUBUNIT=COMPLETE
E004_RUNTIME_BINDING_EVIDENCE_SUBUNIT=COMPLETE_AUTHORITY_CONSUMED
E004_SUBJECT_METADATA_EVIDENCE_SUBUNIT=COMPLETE_AUTHORITY_CONSUMED
E004_CANDIDATE_ARTIFACT_BUNDLE_BINDING_SUBUNIT=COMPLETE
E004_EXECUTION_PLAN_ARGV_SUBUNIT=INCOMPLETE
E004_RUNTIME_COMPATIBILITY_SUBUNIT=INCOMPLETE
E004_EXACT_SUBJECT_BINDING_SUBUNIT=INCOMPLETE
E004_RESOURCE_ACCESS_FINANCE_SUBUNIT=INCOMPLETE
E004_A1_A14_SNAPSHOT_SUBUNIT=INCOMPLETE
E004_A15_SUBUNIT=NOT_REACHED_AS_SOLE_BLOCKER
E004_MODEL_EXECUTION_SUBUNIT=NOT_STARTED_NOT_AUTHORIZED_BY_GATE_STATE
E004_TOURNAMENT_EXECUTION_SUBUNIT=NOT_STARTED_NOT_AUTHORIZED_BY_GATE_STATE
E005_STATE=NOT_REACHED
```

## 9. Next dependency-safe frontier

Continue in the V35 dependency order:

1. define exact per-candidate runtime argv and deterministic execution-plan identities against the already-bound runtime families without executing any model or runtime;
2. separately close compatibility facts that static evidence cannot establish; do not infer model-load PASS;
3. bind exact future environment, compute/resource, network, access/credential, retention, wallclock, and zero-incremental-spend identities;
4. construct and qualify the applicable A1-A14 snapshot only from genuine evidence;
5. only after all earlier applicable prerequisites pass may a separate explicit A15 decision surface be prepared;
6. only after A15 and the full exact subject pass may a non-`NONE` `CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256` permit the first model call.

This ordering creates no implicit authority to execute a missing step.

## 10. Current disposition

```text
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v36-2026-09-06.md
SUCCESSOR_PREFLIGHT_DISPOSITION=BLOCKED
SUCCESSOR_PASS_PREFLIGHT=NO
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
MODEL_RUNTIME_LOAD_PERFORMED=NO
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
TRAINING_PERFORMED=NO
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```
