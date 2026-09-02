# E004 Aya Content-Addressed Access Route Founder Decision Request — 2026-09-03

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Current global frontier:** `e004-registry-current-state-reconciliation-v17-2026-09-03.md`  
**Canonical base:** `87dd7c41c2dd1e4034bbd15a4415642fae41e101`  
**Artifact class:** Founder route decision request only  
**Decision owner:** Founder  
**Decision state:** ABSENT  
**Authority effect of this document:** NONE  
**Dataset payload materialized:** NO  
**Spend:** USD 0

## 1. Purpose

Resolve the execution-environment transport blocker recorded by V17 without changing the authorized Aya byte subject, dataset, file, content identities, candidate boundary, admission state, contamination state, model authority, or training authority.

Decision B from PR #189 authorizes only the exact pinned Aya subject but explicitly excludes mutable `main` as an access subject. The current execution environment cannot materialize the immutable revision URL directly. Public Hugging Face source evidence currently reports that repository `main` resolves to the same pinned repository revision and that the train file exposes the same canonical Xet hash and SHA-256.

This request therefore asks whether a strictly verified public alias may be used only as a transport resolver for the already-authorized immutable byte subject.

## 2. Existing exact byte subject remains unchanged

```text
SOURCE_REPOSITORY=CohereLabs/aya_dataset
SOURCE_REVISION=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
SOURCE_FILE=data/train-00000-of-00001.parquet
SOURCE_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
SOURCE_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
DECLARED_LICENSE=Apache-2.0
```

No other byte subject is eligible under either decision class below.

## 3. Current blocker

V17 records:

```text
MATERIALIZATION_ATTEMPT_RESULT=BLOCKED_FAIL_CLOSED
MATERIALIZATION_BLOCKER=EXACT_PIN_MATERIALIZATION_BLOCKED_BY_EXECUTION_ENVIRONMENT
AYA_PAYLOAD_DOWNLOAD_PERFORMED=NO
AYA_PAYLOAD_MATERIALIZED=NO
AYA_PAYLOAD_HASH_VERIFICATION_PERFORMED=NO
AYA_PAYLOAD_PARSED=NO
```

The blocker is not evidence that the source is unavailable. It is an execution-tool transport limitation.

## 4. Public route evidence at request time

Observed public source metadata at request time reports:

```text
OBSERVED_PUBLIC_REPOSITORY_MAIN_HEAD=f9ea045
OBSERVED_PUBLIC_MAIN_HEAD_CORRESPONDS_TO_PINNED_REVISION=YES
OBSERVED_TRAIN_FILE_XET_HASH=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
OBSERVED_TRAIN_FILE_SHA256=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
```

These are public metadata observations only. They are not local payload verification and may become stale. Any authorized route must therefore re-check identity immediately before use and verify downloaded bytes before parsing.

## 5. Decision classes

The Founder must select exactly one class after this decision surface becomes canonical.

### `E004_AYA_ACCESS_ROUTE_DECISION_A` — preserve exact immutable-route-only state

```text
FOUNDER_AYA_ACCESS_ROUTE_DECISION=E004_AYA_ACCESS_ROUTE_DECISION_A
AYA_PUBLIC_MAIN_ALIAS_RESOLUTION_AUTHORITY=NONE
AYA_CONTENT_ADDRESSED_TRANSPORT_AUTHORITY_EXPANSION=NONE
```

Effect: retain V17. Execution waits for an environment capable of directly materializing the exact immutable revision URL.

### `E004_AYA_ACCESS_ROUTE_DECISION_B` — authorize verified alias resolution for the same exact byte subject

```text
FOUNDER_AYA_ACCESS_ROUTE_DECISION=E004_AYA_ACCESS_ROUTE_DECISION_B
AYA_PUBLIC_MAIN_ALIAS_RESOLUTION_AUTHORITY=AUTHORIZED_TRANSPORT_ONLY_IF_EXACT_PIN_PRECHECK_PASSES
AYA_CONTENT_ADDRESSED_TRANSPORT_AUTHORITY=AUTHORIZED_ONLY_FOR_CANONICAL_XET_AND_SHA256_SUBJECT
AYA_BYTE_SUBJECT_EXPANSION=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Decision B changes only the permitted transport resolution path. It does not change the authorized byte subject.

## 6. Mandatory pre-download identity checks under Decision B

Before requesting any bytes through the public `main` alias, all of the following must be observed in the same bounded execution attempt:

```text
PRECHECK_REPOSITORY=CohereLabs/aya_dataset
PRECHECK_MAIN_HEAD_MUST_EQUAL=f9ea04583f02a8f86404ff6c58bf75fe637df8a2
PRECHECK_FILE_MUST_EQUAL=data/train-00000-of-00001.parquet
PRECHECK_XET_HASH_MUST_EQUAL=3a0e7a5f4bf474bb9877936ee28f8d866be5990c7d52e4f6e6ca68dbd3437082
PRECHECK_PUBLISHED_SHA256_MUST_EQUAL=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
PRECHECK_PUBLIC_ACCESS_MUST_EQUAL=YES
PRECHECK_GATED_MUST_EQUAL=NO
PRECHECK_CREDENTIAL_REQUIRED_MUST_EQUAL=NO
PRECHECK_INCREMENTAL_SPEND_REQUIRED_MUST_EQUAL=NO
```

Any mismatch aborts before download.

## 7. Mandatory post-download byte check

Even after every precheck passes, the downloaded bytes remain untrusted until locally hashed.

```text
POSTDOWNLOAD_SHA256_REQUIRED=YES
POSTDOWNLOAD_SHA256_MUST_EQUAL=51baa85043b569ba117f41516b32d1b0e4e2647fb203a08933f98a556fb1fb06
PARSE_BEFORE_POSTDOWNLOAD_SHA256_MATCH=PROHIBITED
DELETE_ON_SHA256_MISMATCH=REQUIRED
```

A successful SHA-256 equality proves only byte identity with the canonical pinned file. It does not create data admission, privacy PASS, license compatibility PASS, quarantine PASS, or contamination PASS.

## 8. Alias is transport only

Decision B, if selected, would permit `main` only as a transport resolver after the exact precheck above.

```text
MUTABLE_MAIN_AS_IDENTITY_AUTHORITY=NONE
MUTABLE_MAIN_AS_SOURCE_OF_TRUTH=PROHIBITED
MAIN_ALIAS_TRANSPORT_WITHOUT_EXACT_HEAD_MATCH=PROHIBITED
MAIN_ALIAS_TRANSPORT_WITHOUT_XET_MATCH=PROHIBITED
MAIN_ALIAS_TRANSPORT_WITHOUT_PUBLISHED_SHA256_MATCH=PROHIBITED
```

If `main` moves away from the pinned revision, this route authority becomes unusable automatically; it does not follow the new `main`.

A redirect or signed content-addressed storage URL may be followed only when it is produced by the authorized public route after all prechecks pass and the resulting downloaded bytes subsequently pass the canonical SHA-256 check.

## 9. No alternate parquet or source widening

```text
REFS_CONVERT_PARQUET_AUTHORITY=NONE
TEST_PARQUET_AUTHORITY=NONE
DEMOGRAPHICS_PAYLOAD_AUTHORITY=NONE
ALTERNATE_AYA_REVISION_AUTHORITY=NONE
ALTERNATE_AYA_FILE_AUTHORITY=NONE
MIRROR_OR_DERIVATIVE_AUTHORITY=NONE
OASST1_PAYLOAD_AUTHORITY=NONE
DOLLY_PAYLOAD_AUTHORITY=NONE
```

Matching hashes observed on an alternate path do not make that path authorized.

## 10. Existing candidate-construction boundaries remain unchanged

If the exact bytes are successfully materialized and hash-verified, the controlling Decision B from PR #189 still governs all subsequent work:

- original human annotations only after exact semantics are established;
- re-annotations excluded;
- unresolved human origin excluded fail closed;
- demographics excluded;
- `user_id` prohibited from candidate training representation;
- exact `SP007-RO-001` non-clinical learner/researcher scope enforced;
- positive patient/caregiver and clinical-professional capability content excluded;
- local deterministic PII/PHI risk screening and bounded human inspection only;
- no record content sent to an external model/provider/API;
- raw payload and transient sensitive material remain outside canonical repository source.

## 11. Still non-admitting

```text
DATA_ADMISSION_AUTHORITY=NONE
FINAL_CURRICULUM_ADMISSION_AUTHORITY=NONE
DATASET_SNAPSHOT_AUTHORITY_FROM_THIS_DECISION=NONE
QUARANTINE_PASS_AUTHORITY_FROM_THIS_DECISION=NONE
LICENSE_COMPATIBILITY_PASS_AUTHORITY_FROM_THIS_DECISION=NONE
CONTAMINATION_PASS_AUTHORITY_FROM_THIS_DECISION=NONE
```

## 12. No contamination, model, A15, or training expansion

```text
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY_EXPANSION_FROM_THIS_DECISION=NONE
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
SFT_AUTHORITY=NONE
CPT_AUTHORITY=NONE
LORA_QLORA_AUTHORITY=NONE
DISTILLATION_AUTHORITY=NONE
DPO_RL_GRPO_AUTHORITY=NONE
QAT_AUTHORITY=NONE
```

## 13. No protected, credentialed, paid, or external-AI resources

```text
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
EXTERNAL_PROVIDER_PII_PHI_SCREENING=PROHIBITED
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 14. Failure conditions

Decision B must fail closed without substitution if any condition below occurs:

```text
MAIN_HEAD_NOT_EXACT_PIN
PUBLISHED_XET_HASH_MISMATCH
PUBLISHED_SHA256_MISMATCH
ACCESS_GATED_OR_CREDENTIAL_REQUIRED
INCREMENTAL_SPEND_REQUIRED
DOWNLOAD_REDIRECT_CANNOT_BE_BOUND_TO_AUTHORIZED_ROUTE
DOWNLOADED_SHA256_MISMATCH
```

Failure does not authorize another path, file, revision, dataset, mirror, or paid route.

## 15. E004 effect

Neither decision class completes E004.

```text
E004_COMPLETE_FROM_ROUTE_DECISION=NO
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
BACKBONE_WINNER_SELECTED=NO
E005_STARTED=NO
PROJECT_FINISHED=NO
```

## 16. ChatGPT recommendation for Founder review

```text
CHATGPT_AYA_ACCESS_ROUTE_POSITION=RECOMMEND_E004_AYA_ACCESS_ROUTE_DECISION_B
RATIONALE_1=THE_BYTE_SUBJECT_DOES_NOT_CHANGE
RATIONALE_2=PRECHECK_BINDS_MAIN_TO_THE_ALREADY_PINNED_REVISION_AND_FILE_IDENTITIES
RATIONALE_3=POSTDOWNLOAD_SHA256_MUST_MATCH_BEFORE_ANY_PARSE
RATIONALE_4=THE_ROUTE_AUTOMATICALLY_FAILS_IF_MAIN_MOVES
RATIONALE_5=ALL_ADMISSION_CONTAMINATION_MODEL_A15_TRAINING_AND_SPEND_GATES_REMAIN_CLOSED
```

This recommendation is not a Founder decision.

## 17. Exact Founder response required

To preserve V17 immutable-route-only state:

```text
FOUNDER_AYA_ACCESS_ROUTE_DECISION=E004_AYA_ACCESS_ROUTE_DECISION_A
```

To authorize the verified public alias strictly as transport for the same exact byte subject:

```text
FOUNDER_AYA_ACCESS_ROUTE_DECISION=E004_AYA_ACCESS_ROUTE_DECISION_B
```

A broad continuation instruction, ordinary approval, prior public-data Decision B, or statement that all approvals are granted does not substitute for this new route-specific decision.

The operative response must occur after this decision surface is canonical and must be captured separately before the public `main` alias is used to request payload bytes.

## 18. Current state until an operative route decision is canonical

```text
FOUNDER_AYA_ACCESS_ROUTE_DECISION=ABSENT
AYA_PUBLIC_MAIN_ALIAS_RESOLUTION_AUTHORITY=NONE
AYA_CONTENT_ADDRESSED_TRANSPORT_AUTHORITY_EXPANSION=NONE
FOUNDER_PUBLIC_DATA_ACCESS_DECISION=E004_PUBLIC_DATA_ACCESS_DECISION_B
AYA_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_EXACT_PUBLIC_PIN_ONLY
AYA_PAYLOAD_MATERIALIZATION_AUTHORITY=AUTHORIZED_EPHEMERAL_EXACT_PUBLIC_PIN_ONLY
AYA_PAYLOAD_MATERIALIZED=NO
AYA_PAYLOAD_HASH_VERIFICATION_PERFORMED=NO
DATA_ADMISSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

## 19. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded decision-request artifact.

Before merge, verify exact base/head/diff, correspondence to V17 and the existing Decision B byte subject, applicable status/CI, unresolved review threads, mergeability, branch/ruleset state, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
