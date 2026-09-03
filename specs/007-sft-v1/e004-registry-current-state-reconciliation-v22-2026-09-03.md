# E004 Registry Current-State Reconciliation V22 — 2026-09-03

**Spec:** 007 SFT V1
**Task:** E004
**Artifact class:** append-only current-state reconciliation
**Canonical base before this result package:** `58480543b2d2ae706c33033ecad8bb021cf06ce4`
**Exact component scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Founder decisions preserved:** FD-007, FD-008, exact Aya qualification Decision B, exact Aya transport Decision B
**Current authorized spend:** USD 0

## 1. Purpose and supersession

Reconcile the E004 current view after the FD-008 successor method was implemented, qualified, merged through PR #222, and then executed locally against the exact verified Aya 135 subject without human review, external AI/model processing, external provider screening, or raw-text repository persistence.

```text
PREVIOUS_CURRENT_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v21-2026-09-03.md
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v22-2026-09-03.md
V22_SUPERSEDES_V21_FOR_PROSPECTIVE_CURRENT_STATE=YES
HISTORICAL_EVIDENCE_REWRITTEN=NO
```

V22 records actual evidence that did not exist at V21. It does not retroactively alter V20/V21 historical statements.

## 2. Canonical deterministic method implementation

PR #222 merged the frozen FD-008 successor implementation into `main`.

```text
PR=222
MERGE_SHA=58480543b2d2ae706c33033ecad8bb021cf06ce4
METHOD_ID=AYA_135_LOCAL_DETERMINISTIC_RECORD_EVIDENCE_V1
IMPLEMENTATION_PATH=scripts/e004_aya_135_deterministic_record_evidence_v1.py
IMPLEMENTATION_GIT_BLOB_SHA=8b69861d613a0c4acdda6911ab782b890ce2d174
IMPLEMENTATION_SHA256=0f6d9d7953da5a69716061f25939977671dd17b3d65445f9c74874b8ecc14ffc
FINAL_PACKAGE_CI_RUN=33799999429
FINAL_PACKAGE_CI_JOB=100796906772
FINAL_PACKAGE_CI_RESULT=PASS
FOCUSED_SYNTHETIC_TEST_COUNT=13
```

The implementation does not compute `ELIGIBLE`; it produces only exact identities plus categorical rights/privacy/scope evidence.

## 3. Exact Aya subject replayed

The previously canonical GitHub Actions transport artifact remained live and was materialized into the local execution environment. Before parsing, the artifact ZIP and extracted Parquet were verified against their exact identities.

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SIZE=137195800
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
TRANSPORT_RUN_ID=33774671767
TRANSPORT_ARTIFACT_ID=9901059828
TRANSPORT_ARTIFACT_DIGEST=sha256:400a54e6c0c777a151318558a4eb76028a83e01e216dbd097f0a445c45420417
LOCAL_SOURCE_SHA256_VERIFICATION=PASS
RAW_AYA_TEXT_EMITTED=NO
USER_ID_READ=NO
```

## 4. Exact tooling replay

The canonical CPython 3.13 tooling artifact was also materialized and verified before local installation with no index and no dependency substitution.

```text
TOOL=pyarrow
TOOL_VERSION=25.0.1
WHEEL=pyarrow-25.0.1-cp313-cp313-manylinux_2_28_x86_64.whl
WHEEL_SHA256=0befcf816e45a1af33ac775a9970b749e4868a230c7372f0ae5e932bee27039f
TOOLING_RUN_ID=33775229990
TOOLING_ARTIFACT_ID=9901289574
TOOLING_ARTIFACT_DIGEST=sha256:2af8ef97c8facbb61fe3729817df03a735be1f3e5bfe0e8eeea2e42d9907300f
TOOLING_IDENTITY_VERIFICATION=PASS
```

## 5. Candidate replay result

The canonical candidate-pass script was reconstructed from the current repository and verified before execution.

```text
CANDIDATE_SCRIPT_GIT_BLOB_SHA=82bc50ba7e5f9903ddaa5a136b69f79504252208
CANDIDATE_SCRIPT_SHA256=12ecee629f5558bb347ad0f14ff75cea9f3b00d90030ad19513d4e87bd566f8f
CANDIDATE_COUNT=135
CANDIDATE_MANIFEST_CANONICAL_SHA256=dc341eef6589cf5c41cbf886f679d7d345f6fb47069e290377c2504c2f5adb99
CANDIDATE_MANIFEST_FILE_SHA256=bbc7188613f242b428b4ac4cad0297c9dfb31403f6fab146a1a8491a106b2d6e
CANDIDATE_RECORD_ID_SET_SHA256=d50c128704e66ff401db534d289b398b4b5e2ce5700f4b8ac0e6d26cbda9de83
CANDIDATE_CONTENT_SHA256_SET_SHA256=ed6d37362b9fef0180f48af2a60c5eada85d64c9bf7c1ed7f12f07f2dbe5ba64
LANGUAGE_ARB_COUNT=47
LANGUAGE_ENG_COUNT=88
USER_ID_READ=FALSE
HUMAN_INSPECTION_PERFORMED=FALSE
```

The replay exactly reproduced the fixed canonical candidate subject.

## 6. Actual deterministic record-evidence result

The frozen V1 method then classified the exact 135 records locally. Repository-safe per-record categorical evidence is captured in `e004-aya-135-deterministic-record-evidence-result-v1.json`.

```text
DETERMINISTIC_RECORD_EVIDENCE_OUTPUT_SHA256=129688b220a75773a7709c656a2aa313f2aed770541dc62a39b3351848beb07d
PRIVACY_NO_PHI_KNOWN=118
PRIVACY_UNRESOLVED=17
PRIVACY_RESTRICTED_OR_PHI=0
RECORD_LEVEL_RIGHTS_SUPPORTED=43
RECORD_LEVEL_RIGHTS_UNRESOLVED=92
EMBEDDED_SOURCE_RISK_PRESENT=0
SCOPE_PASS=135
SCOPE_FAIL=0
SCOPE_UNRESOLVED=0
EXTERNAL_AI_OR_MODEL_USED=FALSE
EXTERNAL_PROVIDER_USED=FALSE
NETWORK_ACCESS_PERFORMED_BY_METHOD=FALSE
RAW_TEXT_PERSISTED=FALSE
```

`NO_PHI_KNOWN` and `SUPPORTED` are bounded statements under the frozen deterministic method and canonical dataset-level evidence. They are not universal legal or privacy proofs.

## 7. Canonical Spec 003 evaluator replay

The exact Spec 003 evaluator source package created by the canonical V2 transport was materialized and verified. The lineage contract validated with zero contract errors.

```text
SPEC003_EVALUATOR_SOURCE_COMMIT=7fa0b8d4baee9e6ef5f2a0ca30aaf0bd8199c6fc
SPEC003_EVALUATOR_SOURCE_RUN_ID=33776122190
SPEC003_EVALUATOR_SOURCE_ARTIFACT_ID=9901629369
SPEC003_EVALUATOR_SOURCE_ARTIFACT_DIGEST=sha256:5ac4f7390d88aa85fda30ba6706faf5612538dbf93c6f8dd2cdaebb9289a4688
SPEC003_LINEAGE_CONTRACT_SHA256=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962
SPEC003_CONTRACT_VALIDATION=PASS
```

For each exact candidate, the evaluator input used the fixed candidate record identity as `asset_id`, its exact `content_sha256` as `DIRECT_DIGEST`, the canonical pinned Aya source and revision, `DECLARED_USE=TRAINING_OR_ADAPTATION`, `PURPOSE=TRAIN`, `ORIGIN_TYPE=ORIGINAL`, `QUARANTINE_STATE=NOT_QUARANTINED`, the frozen deterministic rights/privacy dispositions, and the previously canonical `ASSESSED_CLEAN` contamination disposition. Scope PASS was required before evaluation. No caller-controlled admission field was supplied.

## 8. Actual Spec 003 admission result

The canonical evaluator processed all 135 exact candidates with zero validation errors.

```text
SPEC003_CANDIDATE_COUNT=135
SPEC003_ELIGIBLE_COUNT=43
SPEC003_BLOCKED_COUNT=92
SPEC003_VALIDATION_ERROR_COUNT=0
SPEC003_RIGHTS_UNRESOLVED_REASON_COUNT=92
SPEC003_PRIVACY_UNRESOLVED_REASON_COUNT=17
SPEC003_POST_DETERMINISTIC_RESULTS_SHA256=3e7e4f15a913ca5e72c091aee4dda563f48037ed6fd67a3781fef1ade71d21ef
CALLER_CONTROLLED_ELIGIBLE_STATE=FALSE
```

The state intersection is exact:

```text
RIGHTS_SUPPORTED_AND_PRIVACY_NO_PHI_KNOWN=43
RIGHTS_UNRESOLVED_AND_PRIVACY_NO_PHI_KNOWN=75
RIGHTS_UNRESOLVED_AND_PRIVACY_UNRESOLVED=17
```

Therefore the evaluator, not the caller, computed exactly 43 records `ELIGIBLE`; the remaining 92 stay fail-closed `BLOCKED`.

## 9. What this resolves and what it does not

The V21 Aya-135 record-evidence frontier is now complete for the frozen V1 method and exact candidate set.

```text
AYA_135_HUMAN_REVIEW_REQUIRED=NO
AYA_135_DETERMINISTIC_RECORD_EVIDENCE_EXECUTED=YES
AYA_135_SPEC003_EVALUATION_EXECUTED=YES
AYA_135_EXACT_ELIGIBLE_RECORD_COUNT=43
AYA_135_EXACT_BLOCKED_RECORD_COUNT=92
AYA_135_DATA_QUALIFICATION_EDGE_RESOLVED=YES_FOR_FROZEN_V1_EVIDENCE
```

This does not authorize or perform final SFT curriculum admission. The canonical Founder decision remains explicit:

```text
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The 92 blocked records are not silently discarded into a PASS lane, and the 43 eligible records do not create authority beyond the exact Spec 003 evaluator disposition.

## 10. Local cleanup completed

After safe hashes and categorical outcomes were captured, the raw/transient local material no longer needed for execution was removed.

```text
LOCAL_RAW_AYA_PARQUET_REMAINING=NO
LOCAL_AYA_TRANSPORT_ZIP_REMAINING=NO
LOCAL_PYARROW_WHEEL_REMAINING=NO
LOCAL_TOOLING_ARTIFACT_ZIP_REMAINING=NO
LOCAL_SPEC003_SOURCE_ARTIFACT_ZIP_REMAINING=NO
```

Repository-safe hash/categorical result material may remain only as needed for canonical evidence and verification.

## 11. Remote artifact cleanup obligation

The three one-day transport artifacts have served their bounded materialization purpose and must not be treated as persistent storage.

```text
AYA_TRANSPORT_ARTIFACT_ID=9901059828
PYARROW_TOOLING_ARTIFACT_ID=9901289574
SPEC003_EVALUATOR_SOURCE_ARTIFACT_ID=9901629369
REMOTE_ARTIFACT_CLEANUP_REQUIRED=YES
```

This result package includes a one-shot exact-ID cleanup workflow. Remote cleanup is not claimed complete until the post-merge workflow returns PASS and the artifacts no longer resolve.

## 12. Current E004 frontier after data qualification

The newly resolved Aya edge does not fabricate the exact research-component execution subject that earlier component reconciliation V12 recorded as absent. The remaining dependency-correct frontier returns to those concrete operational bindings.

```text
COMPONENT_REAL_GUARD_EVIDENCE=ABSENT
COMPONENT_SPECIFIC_EXECUTION_SUBJECT_RUNTIME_BINDING=ABSENT
COMPONENT_EXACT_RUN_MANIFEST=ABSENT
COMPONENT_CONVERSION_PREREQUISITES=INCOMPLETE
COMPONENT_RESOURCE_ACCESS_BINDINGS=INCOMPLETE
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
COMPONENT_A1_A14_EQUIVALENT_EXACT_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
E005_STATE=NOT_REACHED
E005_REACHABLE=NO
TRAINING_AUTHORITY=NONE
PROJECT_FINISHED=NO
```

The next work must satisfy the exact component execution-subject/resource/guard prerequisites and any separately applicable authority before model conversion or tournament execution. No generic continuation approval is interpreted as model-conversion, A15, credential, protected-data, or training authority.

## 13. Repository qualification

Under FD-007, independent repository review is optional by default. Before merge, verify the exact base/head/diff, result-file identities, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, and expected-head guard. The remote cleanup workflow must then be verified from its actual post-merge run before claiming remote artifact deletion complete.
