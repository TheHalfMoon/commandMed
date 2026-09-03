# E004 Aya Verified-Alias Materialization Attempt — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Route decision record:** `specs/007-sft-v1/e004-aya-content-addressed-access-route-founder-decision-2026-09-03.md`  
**Canonical route-decision merge:** `169db96c8b7a013f3dda20ed5f8da400dce0019d`  
**Artifact class:** bounded execution-attempt evidence  
**Authority effect:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Record the first bounded Aya payload materialization attempt after the exact Founder route Decision B became canonical. This attempt used the public `main` alias only as an authorized transport resolver after exact prechecks and did not change the authorized byte subject.

No payload-derived state is promoted unless actual local payload bytes are materialized and pass the canonical post-download SHA-256 check before parsing.

## 2. Exact authorized byte subject

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
```

## 3. Canonical authority at attempt time

```text
FOUNDER_AYA_ACCESS_ROUTE_DECISION=E004_AYA_ACCESS_ROUTE_DECISION_B
AYA_PUBLIC_MAIN_ALIAS_RESOLUTION_AUTHORITY=AUTHORIZED_TRANSPORT_ONLY_IF_EXACT_PIN_PRECHECK_PASSES
AYA_CONTENT_ADDRESSED_TRANSPORT_AUTHORITY=AUTHORIZED_ONLY_FOR_CANONICAL_XET_AND_SHA256_SUBJECT
AYA_BYTE_SUBJECT_EXPANSION=NONE
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
AYA_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_EXACT_PUBLIC_PIN_ONLY
AYA_PAYLOAD_MATERIALIZATION_AUTHORITY=AUTHORIZED_EPHEMERAL_EXACT_PUBLIC_PIN_ONLY
AYA_CANDIDATE_CONSTRUCTION_AUTHORITY=AUTHORIZED_NON_ADMITTING_SP007_RO_001_ONLY
AYA_PRIVACY_SCREENING_AUTHORITY=AUTHORIZED_LOCAL_DETERMINISTIC_AND_HUMAN_INSPECTION_WITH_NO_EXTERNAL_PROVIDER
AYA_RAW_PAYLOAD_REPOSITORY_PERSISTENCE_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 4. Immediate pre-download route checks

The authorized public source was rechecked immediately before requesting payload transport through the `main` alias.

Public source surfaces used for the identity precheck:

- `https://huggingface.co/datasets/CohereLabs/aya_dataset/commit/f9ea04583f02a8f86404ff6c58bf75fe637df8a2`
- `https://huggingface.co/datasets/CohereLabs/aya_dataset/blob/main/data/train-00000-of-00001.parquet`
- `https://huggingface.co/datasets/CohereLabs/aya_dataset/resolve/main/data/train-00000-of-00001.parquet`

Observed precheck state:

```text
PRECHECK_REPOSITORY=CohereLabs/aya_dataset
PRECHECK_MAIN_HEAD_OBSERVED=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
PRECHECK_MAIN_HEAD_MATCH=PASS
PRECHECK_FILE_OBSERVED=data/train-00000-of-00001.parquet
PRECHECK_FILE_MATCH=PASS
PRECHECK_XET_HASH_OBSERVED=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
PRECHECK_XET_HASH_MATCH=PASS
PRECHECK_PUBLISHED_SHA256_OBSERVED=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
PRECHECK_PUBLISHED_SHA256_MATCH=PASS
PRECHECK_PUBLIC_ACCESS=YES_OBSERVED
PRECHECK_GATED=NO_OBSERVED
PRECHECK_CREDENTIAL_REQUIRED=NO_OBSERVED
PRECHECK_INCREMENTAL_SPEND_REQUIRED=NO_OBSERVED
ROUTE_PRECHECK_RESULT=PASS
```

These observations establish route eligibility only. They are not local payload-byte verification.

## 5. Authorized alias resolution result

After the precheck passed, the exact public `resolve/main/...` route was requested only as a transport resolver. The public route resolved to signed Xet-backed transport whose content-addressed path bound to the canonical Xet subject:

```text
AUTHORIZED_ALIAS_ROUTE_REQUESTED=YES
AUTHORIZED_ALIAS_ROUTE=https://huggingface.co/datasets/CohereLabs/aya_dataset/resolve/main/data/train-00000-of-00001.parquet
RESOLVED_TRANSPORT_CLASS=SIGNED_PUBLIC_XET
RESOLVED_XET_HOST=us.aws.cdn.hf.co
RESOLVED_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
RESOLVED_XET_HASH_MATCH=PASS
SIGNED_TRANSPORT_QUERY_PERSISTED=NO
MUTABLE_MAIN_USED_AS_IDENTITY=NO
```

The transient signed query string is intentionally not persisted in canonical repository evidence.

## 6. Local byte-materialization result

The current execution environment then attempted to materialize the authorized resolved transport locally. No payload bytes were successfully received.

Observed execution-environment failures were transport-level only:

- the binary download helper could not materialize the authorized resolved object through its current safety/access boundary;
- direct local container connectivity to the resolved Xet endpoint was unavailable even when a currently published endpoint address was supplied explicitly;
- no alternate source, mirror, converted parquet, credentialed route, paid route, or provider-side processing was substituted.

```text
MATERIALIZATION_ATTEMPT_RESULT=BLOCKED_FAIL_CLOSED
MATERIALIZATION_BLOCKER=AUTHORIZED_ROUTE_RESOLVED_BUT_LOCAL_BYTE_MATERIALIZATION_UNAVAILABLE
AYA_PAYLOAD_DOWNLOAD_PERFORMED=NO
AYA_PAYLOAD_MATERIALIZED=NO
LOCAL_PAYLOAD_BYTES_RECEIVED=0
AYA_PAYLOAD_HASH_VERIFICATION_PERFORMED=NO
AYA_PAYLOAD_PARSED=NO
```

Because zero payload bytes were materialized, no local SHA-256 result exists and the parse gate remained closed exactly as required.

## 7. No parse, schema execution, screening, or candidate construction

```text
PARSE_BEFORE_POSTDOWNLOAD_SHA256_MATCH=PROHIBITED_AND_NOT_PERFORMED
AYA_SCHEMA_FROM_LOCAL_PAYLOAD_INSPECTED=NO
AYA_ORIGINAL_HUMAN_ANNOTATION_SEMANTICS_FROZEN_FROM_PAYLOAD=NO
AYA_RECORD_LEVEL_SCREENING_PERFORMED=NO
AYA_CANDIDATE_CONSTRUCTION_PERFORMED=NO
AYA_PRIVACY_SCREENING_PERFORMED=NO
AYA_HUMAN_INSPECTION_OF_RECORD_CONTENT_PERFORMED=NO
AYA_CANDIDATE_RECORD_IDENTITIES_CREATED=NO
AYA_CANDIDATE_CONTENT_IDENTITIES_CREATED=NO
REANNOTATION_EXCLUSION_EXECUTED=NO
DEMOGRAPHICS_EXCLUSION_EXECUTED=NO
USER_ID_REMOVAL_FROM_CANDIDATE_REPRESENTATION_EXECUTED=NO
SP007_RO_001_RECORD_SCOPE_FILTER_EXECUTED=NO
```

No record content was sent to an external model, AI provider, API, hosted runner, or external privacy-screening service.

## 8. Raw/transient material cleanup

The local working directory was inspected after the failed materialization attempt and contained zero files and zero payload bytes. The empty working directory was then removed.

```text
AYA_RAW_PAYLOAD_REPOSITORY_PERSISTED=NO
LOCAL_WORKSPACE_FILE_COUNT_AFTER_ATTEMPT=0
LOCAL_WORKSPACE_TOTAL_BYTES_AFTER_ATTEMPT=0
LOCAL_TRANSIENT_WORKSPACE_REMOVED=YES
RAW_OR_TRANSIENT_AYA_PAYLOAD_REMAINING=NO
```

## 9. Unauthorized substitutes rejected

```text
REFS_CONVERT_PARQUET_AUTHORITY=NONE
REFS_CONVERT_PARQUET_USED=NO
ALTERNATE_AYA_REVISION_USED=NO
ALTERNATE_AYA_FILE_USED=NO
MIRROR_OR_DERIVATIVE_USED=NO
OASST1_OR_DOLLY_FALLBACK_USED=NO
GITHUB_HOSTED_RUNNER_PAYLOAD_PROCESSING_USED=NO
EXTERNAL_PROVIDER_PII_PHI_SCREENING_USED=NO
CREDENTIAL_USE=NO
INCREMENTAL_SPEND_USD=0
```

GitHub-hosted or other external-provider payload screening was not substituted because the controlling public-data Decision B permits local deterministic/human inspection only and fails closed when external-provider use would be required.

## 10. Downstream gates remain closed

```text
DATA_ADMISSION_AUTHORITY=NONE
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_PRESENT=NO
QUARANTINE_PASS=NO
LICENSE_ADMISSION_PASS=NO
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
CONTAMINATION_EVIDENCE=INCOMPLETE
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 11. Dependency-safe continuation boundary

The route-authority blocker is resolved: Decision B is canonical and the permitted alias precheck succeeds against the exact authorized byte subject. The remaining blocker is execution-environment byte materialization.

The next payload-derived action remains:

```text
NEXT_ACTION=MATERIALIZE_THE_ALREADY_AUTHORIZED_EXACT_AYA_XET_SUBJECT_IN_A_LOCAL_EXECUTION_ENVIRONMENT_CAPABLE_OF_RECEIVING_THE_BYTES
FIRST_REQUIRED_POSTDOWNLOAD_ACTION=COMPUTE_SHA256_BEFORE_PARSING
EXPECTED_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
NEW_FOUNDER_ROUTE_DECISION_REQUIRED_FOR_SAME_EXACT_SUBJECT=NO
```

A future retry must repeat all immediate route prechecks. If any precheck no longer matches, the attempt must abort before download.

## 12. E004 effect

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

This attempt materially proves that the newly authorized transport resolver binds to the exact canonical Xet subject, but it does not create payload-derived evidence or satisfy any later gate.

## 13. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded evidence record.

Before merge, verify exact base/head/diff, correspondence to the canonical Decision B records, exact source identities, applicable status/CI checks, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
