# E004 Aya 135 Local Transient Cleanup Evidence V2 — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** exact Aya 135 qualification pass  
**Authority effect:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Record local cleanup after the machine-executable portion of the exact Aya 135 qualification pass reached the non-delegable human-review boundary.

The local AI execution environment cannot satisfy the required real-human privacy, embedded-source-risk, and scope inspection. Retaining raw/transient payload material after all currently machine-authorized evidence had been canonically persisted would therefore have served no remaining executable unit in this session.

## 2. Machine-executable work completed before cleanup

```text
AYA_SOURCE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
CANDIDATE_COUNT=135
CANDIDATE_MANIFEST_CANONICAL_SHA256=dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99
CONTAMINATION_METHOD_ID=AYA_135_PUBLIC_CANONICAL_TEXT_13_TOKEN_EXACT_V1
CONTAMINATION_UNIVERSE_CANONICAL_SHA256=e473b2607b28467f3bd055fb34a1e1092fc15f87558185e989d8e4c483c0e98e
CONTAMINATION_ASSESSED_CLEAN=135
CONTAMINATION_OVERLAP_OR_HIGH_RISK=0
SPEC003_POST_CONTAMINATION_BLOCKED=135
SPEC003_POST_CONTAMINATION_VALIDATION_ERRORS=0
HUMAN_REVIEW_EXECUTED=NO
```

Repository-safe evidence was canonically bound by PR #218 before cleanup.

## 3. Local material removed

The cleanup removed local material classes used only for the bounded pass, including:

- the exact transient Aya Parquet payload;
- the local candidate manifest and local pass outputs;
- all nine materialized public comparison payloads and their transport manifest;
- downloaded GitHub Actions artifact ZIPs for Aya replay, comparison transport, exact PyArrow tooling, and Spec 003 evaluator source;
- the local PyArrow wheel and offline installation environment;
- the local exact Spec 003 evaluator source package;
- local contamination result files after their repository-safe identities/counts were persisted;
- local Spec 003 evaluation outputs after their repository-safe identities/counts were persisted;
- hypothetical/noncanonical rights-supported evaluator outputs that were never promoted as evidence;
- local working copies of the human-review implementation and qualification documents after their exact repository versions were canonicalized.

## 4. Observed cleanup counts

```text
PRE_CLEANUP_FILE_COUNT=914
PRE_CLEANUP_BYTES=779130083
POST_CLEANUP_REMAINING_TARGET_PATH_COUNT=0
LOCAL_RAW_AYA_PAYLOAD_REMAINING=NO
LOCAL_COMPARISON_PAYLOAD_REMAINING=NO
LOCAL_PYARROW_TOOLING_ENVIRONMENT_REMAINING=NO
LOCAL_SPEC003_SOURCE_PACKAGE_REMAINING=NO
LOCAL_HYPOTHETICAL_RIGHTS_PASS_OUTPUT_REMAINING=NO
```

The post-cleanup check searched the bounded local filename/path families created for this E004 pass and found no remaining target path.

## 5. Remote-artifact boundary

GitHub Actions runner-local cleanup succeeded in the relevant transport workflows. This local cleanup record does **not** claim deletion of GitHub-hosted artifacts for which no authorized deletion tool was available in the execution environment.

Those transport artifacts were configured with one-day retention. Their existence until expiration does not change the local cleanup result and does not create new data-processing authority.

```text
REMOTE_ARTIFACT_DELETION_CLAIMED=NO
RUNNER_LOCAL_CLEANUP_PREVIOUSLY_VERIFIED=YES
LOCAL_TRANSIENT_CLEANUP_COMPLETE=YES
```

## 6. Remaining evidence boundary

The exact human-review method is canonical at:

```text
scripts/e004_aya_135_human_review_v2.py
```

A future real-human review requires fresh exact payload materialization under the already-canonical exact-subject replay boundaries. No stale local raw payload is retained as a shortcut around those checks.

## 7. Authority exclusions

```text
HUMAN_REVIEW_EXECUTED=NO
RECORD_LEVEL_RIGHTS_STATE=UNRESOLVED
PRIVACY_STATE=UNRESOLVED
DATA_ADMISSION_STATE=BLOCKED
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```
