# E004 Research-Component Sentinel Fixture Freeze Evidence V1 — 2026-09-04

**Spec:** 007 SFT V1
**Task:** E004
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Evidence class:** repository-safe deterministic freeze qualification
**Founder decision:** `E004_SENTINEL_FIXTURE_FREEZE_DECISION_B`
**PR:** #240
**Qualified implementation head:** `6e044d35d81998c71c8cc2335ae4607c1fe4a99d`
**Workflow run:** `33869622710`
**Workflow job:** `101012255948`
**Model inference performed:** NO
**Guard PASS created:** NO
**DatasetSnapshot created:** NO
**Training performed:** NO
**Authorized spend:** USD 0

## 1. Exact authority

```text
FOUNDER_SENTINEL_FIXTURE_FREEZE_DECISION=E004_SENTINEL_FIXTURE_FREEZE_DECISION_B
SENTINEL_FIXTURE_CONSTRUCTION_AUTHORITY=AUTHORIZED_EXACT_PREDECLARED_SP007_RO_001_SENTINEL_7_ONLY
SENTINEL_FIXTURE_FREEZE_AUTHORITY=AUTHORIZED_EXACT_PREDECLARED_SP007_RO_001_SENTINEL_7_ONLY
SENTINEL_FIXTURE_RECORD_COUNT=7
SENTINEL_FIXTURE_SET_SHA256=5a2bd28b391010c9575c99654899cd442fea8d94cbb4176045b654c940fa2fd3
SENTINEL_FIXTURE_SHA256_SET_SHA256=b65b36689cf2006bad8b446536d50ccd3f3440a4b244c044a1b26409aea0fef2
DATASET_SNAPSHOT_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

No alternate prompt, fixture, guard, expected action, hash, count, or scope is admitted.

## 2. Frozen subject

The implementation persists the exact seven-record subject at `specs/007-sft-v1/e004-research-component-sentinel-fixture-set-v1.json` and adds a deterministic offline verifier, five fail-closed tests, and an exact-head qualification workflow. The fixtures are synthetic, non-PHI guard evidence only and cannot become optimization feedback or gradient targets.

## 3. Exact-head qualification

Run `33869622710`, job `101012255948`, bound exact head:

```text
HEAD_SHA=6e044d35d81998c71c8cc2335ae4607c1fe4a99d
EXACT_HEAD_BINDING=PASS
FOUNDER_AUTHORITY_BOUNDARY=PASS
COMPILE=PASS
FOCUSED_FAIL_CLOSED_TESTS=5/5 PASS
SENTINEL_FIXTURE_SCHEMA_VALIDATION=PASS
NON_EXECUTION_BOUNDARY_ASSERTION=PASS
DIFF_CHECK=PASS
```

The tests prove fail-closed rejection for prompt mutation, replacement fixture identity, enabling optimization feedback, and missing required guard.

## 4. Exact identity result

```text
SENTINEL_FIXTURE_RECORD_COUNT=7
SENTINEL_FIXTURE_SET_SHA256=5a2bd28b391010c9575c99654899cd442fea8d94cbb4176045b654c940fa2fd3
SENTINEL_FIXTURE_SHA256_SET_SHA256=b65b36689cf2006bad8b446536d50ccd3f3440a4b244c044a1b26409aea0fef2
SENTINEL_FIXTURE_SCHEMA_VALIDATION=PASS
```

These identities exactly match the Founder-authorized subject. No replacement fixture was selected.

## 5. Non-execution boundary

```text
SENTINEL_MODEL_INFERENCE_PERFORMED=NO
SENTINEL_GUARD_PASS_CREATED=NO
DATASET_SNAPSHOT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

This evidence proves deterministic construction/freeze qualification only. It does not prove model behavior and creates no guard snapshot or PASS.

```text
CAN_RANK_CHECKPOINTS=NO
CAN_TUNE_RECIPE=NO
CAN_CHANGE_HYPERPARAMETERS=NO
CAN_CREATE_PREFERRED_EARLY_STOPPING=NO
CAN_BECOME_GRADIENT_TARGET=NO
CAN_BECOME_HIDDEN_CLINICAL_DEVELOPMENT_SET=NO
```

## 6. Dependency effect

Component dependency item 3 is evidenced on the qualified implementation head. Dependency item 4 remains blocked:

```text
DATASET_SNAPSHOT_AUTHORITY=NONE
DATASET_SNAPSHOT_PRESENT=NO
QUARANTINE_VERIFICATION_IDENTITY_FOR_DATASET_SNAPSHOT=ABSENT
```

E004 remains incomplete and fail-closed before runtime preflight.

## 7. Final-head qualification rule

Run `33869622710` qualifies implementation head `6e044d35d81998c71c8cc2335ae4607c1fe4a99d` only. Adding this evidence changes the PR head, so the final PR head MUST receive a fresh exact-head workflow run before merge. No success is inferred across heads.
