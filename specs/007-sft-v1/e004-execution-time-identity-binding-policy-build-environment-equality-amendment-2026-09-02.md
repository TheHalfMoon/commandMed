# E004 Execution-Time Identity Binding Policy — Build-Environment Equality Amendment — 2026-09-02

**Spec:** 007 SFT V1  
**Canonical base:** `071cf1ca92f7f1d7d4cea3c0bccd478f4208e2c1`  
**Amends:** `specs/007-sft-v1/e004-execution-time-identity-binding-policy-disposition-2026-09-02.md`  
**Amendment scope:** Section 5 double-build equality gate and corresponding failure/review semantics only  
**Artifact class:** non-executing bounded policy amendment  
**Model conversion authority:** NONE  
**Conversion execution authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation:** ABSENT_NOT_AUTHORIZED  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Close the post-merge review gap identified after PR #172: the canonical execution-time identity-binding policy requires each pre-model build to record `build_environment_manifest_sha256`, but its noncompensable double-build gate did not separately state that the two recorded build-environment manifest identities must be equal.

That omission could allow two builds with equal binaries and other listed evidence to pass even when their recorded build-environment manifests differ. This amendment closes only that gap.

This document performs no build, workflow execution, model/source-weight access, conversion, quantization, inference, benchmark execution, contamination assessment, A15 activation, training, credential use, protected-data access, upload, procurement, payment, or spend.

## 2. Controlling amendment

The canonical policy's Section 5 requirement that each build record:

```text
build_environment_manifest_sha256
```

is hereby paired with the following mandatory, noncompensable equality gate:

```text
DOUBLE_BUILD_BUILD_ENVIRONMENT_MANIFEST_EQUAL=YES_REQUIRED
```

For avoidance of doubt, the complete minimum double-build equality gate is now interpreted as:

```text
DOUBLE_BUILD_FULL_FILE_SHA256_EQUAL=YES_REQUIRED
DOUBLE_BUILD_INTEGER_BYTES_EQUAL=YES_REQUIRED
DOUBLE_BUILD_ELF_BUILD_ID_EQUAL=YES_REQUIRED_IF_PRESENT
DOUBLE_BUILD_CMAKE_CACHE_EQUAL=YES_REQUIRED
DOUBLE_BUILD_COMPILE_COMMANDS_EQUAL=YES_REQUIRED
DOUBLE_BUILD_GENERATED_BUILD_INFO_EQUAL=YES_REQUIRED
DOUBLE_BUILD_BUILD_ENVIRONMENT_MANIFEST_EQUAL=YES_REQUIRED
DOUBLE_BUILD_SECURITY_BOUNDARY_EQUAL=YES_REQUIRED
DOUBLE_BUILD_BUILD_MANIFEST_EQUAL=YES_REQUIRED
```

No listed equality check is compensable by another check.

## 3. Failure semantics

A mismatch in the recorded build-environment manifest identity is terminal for that exact execution attempt before any model/source-weight byte may be opened:

```text
DOUBLE_BUILD_BUILD_ENVIRONMENT_MANIFEST_MISMATCH_DISPOSITION=ABORT_BEFORE_MODEL_BYTES
AUTOMATIC_RETRY_AFTER_BUILD_ENVIRONMENT_MANIFEST_MISMATCH=PROHIBITED
ALTERNATE_ENVIRONMENT_AFTER_MISMATCH=PROHIBITED
```

Any retry or changed execution subject requires separate canonical authority. This amendment creates no such authority.

The canonical policy's existing broader fail-closed semantics remain unchanged and continue to apply.

## 4. Policy composition

This amendment is controlling where Section 5 of the canonical execution-time identity-binding policy is silent about equality of `build_environment_manifest_sha256` between the two required builds.

All other provisions of the canonical policy remain unchanged, including:

```text
REBUILD_MISMATCH_CAUSE=NEEDS_EVIDENCE
HISTORICAL_BINARY_EQUIVALENCE_CLAIM=PROHIBITED
HISTORICAL_REPAIRED_HASH_RECONSTRUCTION=NOT_REPRODUCED
FUTURE_CONVERSION_TOOL_IDENTITY_MODE=SAME_SUBJECT_DOUBLE_BUILD_THEN_BIND
FIRST_MODEL_BYTE_READ_BEFORE_TOOL_BINDING=PROHIBITED
CONVERSION_BEFORE_TOOL_BINDING=PROHIBITED
AUTOMATIC_RETRY_AFTER_DOUBLE_BUILD_MISMATCH=PROHIBITED
EXECUTION_TIME_BINARY_CROSS_RUN_REUSE=PROHIBITED_BY_THIS_POLICY
RUN_MANIFEST_CLOSED_SCHEMA_WIDENED_BY_THIS_POLICY=NO
RUN_MANIFEST_VALIDATOR_WIDENED_BY_THIS_POLICY=NO
```

This amendment does not alter the existing Decision B normalization/metadata policy.

## 5. Authority boundary

Even after qualified canonical merge:

```text
MODEL_SOURCE_WEIGHT_ACQUISITION_AUTHORITY=UNCHANGED_BY_THIS_AMENDMENT
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0

E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

No execution may be inferred from this amendment.

## 6. Independent review and merge gate

This amendment has no canonical effect until a fresh independent exact-head repository/governance review verifies the complete one-file diff against canonical `main` and concludes that no material correctness, evidence-integrity, reproducibility, security, integration, or authority-boundary blocker remains.

The reviewer must verify at least:

```text
EXACT_CANONICAL_BASE_MATCHES_MAIN=YES
POST_MERGE_PR172_REVIEW_GAP_IDENTIFIED_EXACTLY=YES
BUILD_ENVIRONMENT_MANIFEST_RECORDED_BY_CANONICAL_POLICY=YES
DOUBLE_BUILD_BUILD_ENVIRONMENT_MANIFEST_EQUALITY_EXPLICIT=YES
BUILD_ENVIRONMENT_MANIFEST_MISMATCH_FAILS_CLOSED_BEFORE_MODEL_BYTES=YES
AUTOMATIC_RETRY_AUTHORITY_CREATED=NO
OTHER_DOUBLE_BUILD_EQUALITY_GATES_PRESERVED=YES
RUN_MANIFEST_SCHEMA_OR_VALIDATOR_WIDENED=NO
NORMALIZATION_METADATA_POLICY_PRESERVED=YES
CONVERSION_EXECUTION_AUTHORITY_CREATED=NO
CONTAMINATION_AUTHORITY_CREATED=NO
A15_AUTHORITY_CREATED=NO
TRAINING_AUTHORITY_CREATED=NO
SPEND_AUTHORITY_CREATED=NO
E004_REMAINS_INCOMPLETE=YES
E005_REMAINS_NOT_REACHED=YES
PROJECT_FINISHED_REMAINS_NO=YES
MATERIAL_BLOCKER=NO
```

Any `MATERIAL_BLOCKER=YES` finding must be resolved on a new exact head and independently re-reviewed before merge. Self-review is not sufficient.

## 7. Explicit exclusions

This amendment does not authorize or perform:

- a rerun of any historical or diagnostic workflow;
- a second rebuild-reproducibility diagnostic;
- binary-difference localization execution;
- model/source-weight download, loading, conversion, quantization, or inference;
- benchmark or device execution;
- contamination assessment;
- A15 activation;
- training or gradient updates;
- Private Gold, PHI, restricted, or gated asset access;
- credentials or provider generation;
- artifact upload or persistent binary promotion;
- external clinical/statistical reviewer outreach;
- paid or larger runner use;
- procurement, payment, or spend;
- clinical, deployment, release, superiority, SOTA, or safety claims.
