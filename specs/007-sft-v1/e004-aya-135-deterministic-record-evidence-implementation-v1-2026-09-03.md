# E004 Aya 135 Deterministic Record Evidence Implementation V1 — 2026-09-03

**Spec:** 007 SFT V1
**Task:** E004
**Method:** `AYA_135_LOCAL_DETERMINISTIC_RECORD_EVIDENCE_V1`
**Authority:** `FD-008` / `REMOVE_MANDATORY_AYA_135_LOCAL_HUMAN_REVIEW_GATE`
**Artifact class:** implementation qualification binding
**Current authorized spend:** USD 0

## 1. Purpose

Bind the exact deterministic Aya 135 record-evidence implementation to actual exact-head repository qualification evidence without claiming that any real Aya record evidence has been executed.

## 2. Exact implementation identity

```text
METHOD_ID=AYA_135_LOCAL_DETERMINISTIC_RECORD_EVIDENCE_V1
IMPLEMENTATION_PATH=scripts/e004_aya_135_deterministic_record_evidence_v1.py
IMPLEMENTATION_SHA256=0f6d9d7953da5a69716061f25939977671dd17b3d65445f9c74874b8ecc14ffc
```

The implementation identity above was emitted by the qualification job from the exact implementation file checked out at the qualified head.

## 3. Qualification evidence

```text
QUALIFICATION_HEAD=aaf1c468778a5701a87bfbbcf902c35199cffdf2
QUALIFICATION_RUN=33799760942
QUALIFICATION_JOB=100796072806
EXACT_HEAD_BINDING=PASS
COMPILEALL=PASS
FOCUSED_SYNTHETIC_TESTS=13_PASS
GIT_DIFF_CHECK=PASS
RAW_AYA_PAYLOAD_IN_REPOSITORY_CHECKOUT=ABSENT
```

The focused tests cover deterministic privacy classification, embedded-source-risk classification, record-level rights mapping, scope verification, fail-closed task-family behavior, no `user_id` access in candidate replay, absence of network-client imports, and the repository-safe categorical output contract.

## 4. Execution boundary remains unchanged

```text
REAL_AYA_RECORD_EVIDENCE_EXECUTED=NO
RAW_AYA_RECORD_CONTENT_INSPECTED_BY_CI=NO
RAW_AYA_RECORD_CONTENT_PERSISTED=NO
USER_ID_READ=NO
EXTERNAL_AI_OR_MODEL_USED=NO
EXTERNAL_PROVIDER_USED=NO
REMOTE_RECORD_SCREENING_EXECUTED=NO
```

The CI workflow qualifies implementation behavior only against synthetic fixtures and repository structure. It does not receive or parse the Aya parquet payload.

## 5. Data-admission state

```text
DATA_ADMISSION_AUTHORITY=AUTHORIZED_EXACT_AYA_135_SPEC003_EVALUATOR_ONLY
DATA_ADMISSION_STATE=BLOCKED
CURRENT_AYA_DATA_FRONTIER=REQUIRED_LOCAL_EXECUTION_OF_FROZEN_DETERMINISTIC_RECORD_EVIDENCE_ON_EXACT_VERIFIED_PAYLOAD
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
```

A real result may be promoted only after local execution of this exact implementation on the exact verified Aya payload and exact canonical candidate manifest. Any material change to the deterministic classification rules requires a new method version and new implementation identity.

## 6. No authority expansion

This implementation qualification creates no authority for remote Aya parsing, remote privacy/rights screening, final curriculum admission, DatasetSnapshot construction, model conversion, model inference, tournament execution, A15 activation, training, credentials, protected-data access, paid compute, procurement/payment, spend, clinical qualification, release claims, or project completion.
