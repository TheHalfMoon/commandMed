# E004 Aya 135 Local Human Review Boundary — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Authority:** `E004_AYA_135_QUALIFICATION_ADMISSION_DECISION_B`  
**State:** REQUIRED HUMAN EVIDENCE BOUNDARY  
**Current authorized spend:** USD 0

## 1. Exact subject

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
FILTER_ID=AYA_SP007_RO_001_CANDIDATE_FILTER_V1
CANDIDATE_COUNT=135
CANDIDATE_MANIFEST_CANONICAL_SHA256=dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99
```

No candidate-set widening or substitution is permitted.

## 2. Why human review remains required

The deterministic construction pass excluded obvious privacy-pattern hits, but canonical governance explicitly states that deterministic screening does not become final privacy clearance. The same governance also states that dataset-level Apache-2.0 evidence does not automatically prove that every embedded or quoted third-party passage is independently cleared for the exact optimization use.

Therefore final record-level privacy and embedded-source-risk evidence requires bounded local human inspection.

```text
HUMAN_INSPECTION_UNAVAILABLE_IMPLIES_PASS=NO
PRIVACY_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
RIGHTS_UNRESOLVED_CAN_PRODUCE_ELIGIBLE=NO
```

## 3. Review implementation

```text
REVIEW_SCRIPT=scripts/e004_aya_135_human_review_v2.py
REVIEW_SCRIPT_SHA256=a1d0fc68f14783bc7aa8b0d4f35f6b7bec590b93db2c7c89f9acccce34bec4de
REVIEW_METHOD_ID=AYA_135_LOCAL_HUMAN_PRIVACY_EMBEDDED_SOURCE_REVIEW_V2
```

Replay-only validation recovered exactly 135/135 candidate identities without printing raw text or collecting any human disposition.

The script:

- requires an interactive local TTY;
- reads only `inputs`, `targets`, `language_code`, and `annotation_type` from the exact verified Aya payload;
- never reads or persists `user_id`;
- performs no network request;
- sends no record content to GitHub, an AI model, an API, or any external provider;
- displays one exact candidate at a time to the local human reviewer;
- writes only candidate/content hashes and categorical review outcomes;
- persists no raw prompt or target text.

## 4. Required human dispositions

For every exact candidate, the human reviewer records:

```text
PRIVACY_STATE=NO_PHI_KNOWN | RESTRICTED_OR_PHI | UNRESOLVED
EMBEDDED_SOURCE_RISK_STATE=NO_EMBEDDED_SOURCE_RISK_OBSERVED | EMBEDDED_SOURCE_RISK_PRESENT | UNRESOLVED
SCOPE_VERIFICATION=PASS | FAIL | UNRESOLVED
```

No default PASS is permitted.

Dataset-level rights evidence remains bound to the pinned Aya README, which declares Apache-2.0 and train/finetune/evaluate use. Record-level `RIGHTS_STATE=SUPPORTED` may be supplied to the Spec 003 evaluator only when the record-level human evidence does not leave embedded-source rights materially unresolved. This is evidence evaluation, not legal advice.

## 5. Fail-closed post-review mapping

```text
PRIVACY_STATE=RESTRICTED_OR_PHI -> RECORD_NOT_ELIGIBLE_FOR_TRAINING
PRIVACY_STATE=UNRESOLVED -> SPEC003_PRIVACY_UNRESOLVED
EMBEDDED_SOURCE_RISK_STATE=EMBEDDED_SOURCE_RISK_PRESENT -> RIGHTS_NOT_AUTOMATICALLY_SUPPORTED
EMBEDDED_SOURCE_RISK_STATE=UNRESOLVED -> SPEC003_RIGHTS_UNRESOLVED
SCOPE_VERIFICATION=FAIL -> RECORD_EXCLUDED_FROM_SP007_RO_001
SCOPE_VERIFICATION=UNRESOLVED -> RECORD_EXCLUDED_OR_BLOCKED_FAIL_CLOSED
```

Only complete evidence may be supplied to the canonical Spec 003 evaluator. Caller-controlled `ELIGIBLE` remains prohibited.

## 6. Execution example

```bash
python scripts/e004_aya_135_human_review_v2.py \
  --aya-parquet /secure/transient/aya-train.parquet \
  --candidate-manifest /secure/transient/candidate-manifest.json \
  --out /secure/transient/e004-aya-135-human-review-v2.json \
  --reviewer-id local-human-reviewer
```

The review must be performed by a real human who is locally viewing the exact candidate text. An AI assistant, remote model, external semantic judge, or unattended automation cannot substitute for this evidence.

## 7. Current state

```text
HUMAN_REVIEW_EXECUTED=NO
RECORD_LEVEL_RIGHTS_STATE=UNRESOLVED
PRIVACY_STATE=UNRESOLVED
DATA_ADMISSION_STATE=BLOCKED
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```
