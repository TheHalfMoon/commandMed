# E004 Aya-43 Curriculum Construction Evidence V1 — 2026-09-04

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Artifact class:** post-merge deterministic evidence reconciliation  
**Authority effect:** NONE  
**Execution effect:** NONE  
**Training authority:** NONE  
**Spend authority:** NONE

## 1. Authority and exact subject

The bounded construction was authorized only by the canonical Founder decision:

`specs/007-sft-v1/e004-final-curriculum-admission-founder-decision-2026-09-04.md`

```text
FOUNDER_FINAL_CURRICULUM_ADMISSION_DECISION=E004_FINAL_CURRICULUM_ADMISSION_DECISION_B
FINAL_CURRICULUM_ADMISSION_AUTHORITY=AUTHORIZED_EXACT_AYA_43_SP007_RESEARCH_COMPONENT_ONLY
FINAL_CURRICULUM_RECORD_COUNT=43
FINAL_CURRICULUM_RECORD_ID_SET_SHA256=417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4
CURRICULUM_RECORD_CONSTRUCTION_AUTHORITY=AUTHORIZED_EXACT_AYA_43_HASH_BOUND_METADATA_ONLY
CONTENT_SCOPE_VERIFICATION_AUTHORITY=AUTHORIZED_EXACT_AYA_43_ONLY
```

The construction method is `AYA_43_HASH_BOUND_CURRICULUM_CONSTRUCTION_V1`.

## 2. Source and qualification identities

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
CANDIDATE_COUNT=135
CANDIDATE_MANIFEST_CANONICAL_SHA256=dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99
SPEC003_CORRECTED_DIRECT_DIGEST_RESULTS_SHA256=a8807085864707ae88966f7a925bfd2a7fd05a0e683d70893a46d3b6d5dbdce4
SPEC003_ELIGIBLE_COUNT=43
SPEC003_BLOCKED_COUNT=92
SPEC003_VALIDATION_ERROR_COUNT=0
ELIGIBLE_RECORD_ID_SET_SHA256=417a1b6afbedf1aa72a31e9f06478526fe0f73f0d3bd3338b2d633b23eda8ee4
```

Only the exact 43 eligible identities were admitted. The blocked 92 remain prohibited from downstream admission.

## 3. Persisted repository-safe result

PR #234 persisted the exact repository-safe construction result and merged as:

```text
PR_NUMBER=234
PR_FINAL_HEAD=8611c90bed7283338e9286b7751e1117421b8bed
PR_MERGE_COMMIT=2d4b51c8e076284902e178b0fb1fb46ba4e93d37
AYA_43_CURRICULUM_RECORD_COUNT=43
AYA_43_CONTENT_SCOPE_VERIFICATION_COUNT=43
AYA_43_BUNDLE_SHA256=f12f70a754e39d395c4d5999fcae1d6718640b1a97931fd9f48321469b87be03
IMPLEMENTATION_SHA256=4ae39d9742d04c126587712baa51ef13ae4a507ff404fac0e961743f5704386a
METHOD_SHA256=73083f055c5ce779b5845b50870f96b625c2fb2c48b5820b39802224d4beb9bc
```

The persistence representation contains hashes, categorical metadata, contract-valid `CurriculumRecord` objects, content-scope verification objects, aggregate counts, and immutable identities only.

## 4. Exact-head qualification

GitHub Actions run `33864457065`, job `100996009504`, explicitly checked out PR #234 exact head `8611c90bed7283338e9286b7751e1117421b8bed` and completed successfully.

The exact-head job reconstructed all persisted parts, required the exact content-addressed persistence identities, invoked the canonical validator, and reported:

```text
RECONSTRUCTED_ENTRY_COUNT=43
RECONSTRUCTED_BUNDLE_SHA256=f12f70a754e39d395c4d5999fcae1d6718640b1a97931fd9f48321469b87be03
PERSISTED_RAW_AYA_TEXT=ABSENT
PERSISTED_USER_ID=ABSENT
VALIDATION=PASS
IMPLEMENTATION_SHA256=4ae39d9742d04c126587712baa51ef13ae4a507ff404fac0e961743f5704386a
METHOD_SHA256=73083f055c5ce779b5845b50870f96b625c2fb2c48b5820b39802224d4beb9bc
```

Six focused synthetic constructor tests also passed on the same exact head. No favorable model, tournament, clinical, or training result is inferred from this validation.

## 5. Persistence repair audit trail

Two earlier PR-head workflow runs failed closed while the repository-safe bundle was being transported into GitHub persistence:

```text
RUN_33863952713=PERSISTENCE_WRAPPER_IDENTITY_FAILURE
RUN_33864065388=PACKED_GZIP_SHA256_MISMATCH
```

Those failures were not accepted as new semantic identities. The large text wrapper was replaced with six bounded Base64 chunks. Final CI required the original exact semantic identities:

```text
CONCATENATED_BASE64_LENGTH=10188
PACKED_GZIP_SHA256=928c69fecd957477ac931cd9464184e1f9455bd359f30258112158a6f8308139
PACKED_DECODED_JSON_SHA256=ac0001440b55dd5469fe57ccbc367b530fc175bbaf7aceb3c1c5d11786eff5f5
FULL_RECONSTRUCTED_BUNDLE_SHA256=f12f70a754e39d395c4d5999fcae1d6718640b1a97931fd9f48321469b87be03
```

## 6. Raw/transient cleanup

Local construction completed without raw-text output and local raw/transient Aya and PyArrow material was removed with zero target paths remaining.

PR #233 merged as `3be92cecb8657abb4ba9bfb8886d0008479a924c`. Cleanup run `33862996747`, job `100991457807`, completed successfully and deleted the exact transient Aya replay artifact and PyArrow tooling artifact. The originating replay and tooling runs subsequently exposed zero artifacts.

```text
RAW_AYA_TEXT_REPOSITORY_PERSISTED=NO
AYA_USER_ID_READ_OR_PERSISTED=NO
REMOTE_MODEL_OR_AI_RECORD_PROCESSING=NO
TRANSIENT_LOCAL_TARGET_PATHS_REMAINING=0
TRANSIENT_REMOTE_REPLAY_ARTIFACTS_REMAINING=0
TRANSIENT_REMOTE_TOOLING_ARTIFACTS_REMAINING=0
```

## 7. Review and merge qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is optional by default. PR #234 had no submitted substantive review and none is claimed. Qodo reported its billing pause and CodeRabbit reported that automatic review was skipped. There were no inline review threads.

Before merge, live state was verified as exact-head CI successful, mergeable/clean, `main` unprotected, repository rulesets empty, and the base unchanged. PR #234 was merged with an exact expected-head guard.

## 8. Authority boundary after this evidence

This evidence closes only the exact Aya-43 curriculum-construction and content-scope-verification substep. It does not complete E004 and does not create any later authority.

```text
DATASET_SNAPSHOT_AUTHORITY=NONE
DATASET_SNAPSHOT_PRESENT=NO
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER_SELECTED=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

The dependency-safe component order in `e004-research-component-execution-preflight-blocker-packet-2026-09-02.md` now has concrete evidence for items 1 and 2 for the exact Aya-43 component subject. Item 3 is the exact seven sentinel-fixture identity freeze. Item 4 is DatasetSnapshot plus quarantine-verification freezing, which remains outside the current DatasetSnapshot authority.