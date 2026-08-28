# E004 / E002 Remaining PRIMARY Provider Metadata Reconciliation — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `a46b890e5851bcc59f809fabe399673ec2634c84`  
**Authority basis:** canonical E002 public, ungated, frozen-candidate access authority  
**Artifact class:** static public provider metadata / provenance evidence only  
**Decision B conversion-subject effect:** NONE  
**Model/source-weight download performed by this record:** NO  
**Model loading performed:** NO  
**Model conversion performed:** NO  
**Model inference performed:** NO  
**Benchmark/device execution performed:** NO  
**Training performed:** NO  
**Spend:** USD 0

This record reconciles provider metadata for the two frozen E001 PRIMARY candidates not covered by the separate `ARTIFACT_DECISION_B` Granite/Qwen3-4B conversion-subject lane:

```text
PRIMARY_1=
  Qwen/Qwen3-0.6B-Base@
  da87bfb608c14b7cf20ba1ce41287e8de496c0cd

PRIMARY_2=
  Qwen/Qwen3.5-0.8B-Base@
  dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
```

```text
THIS_RECORD_EXPANDS_ARTIFACT_DECISION_B_SCOPE=NO
THIS_RECORD_CREATES_CONVERSION_SUBJECTS=NO
THIS_RECORD_CHANGES_WINNER_ELIGIBILITY=NO
THIS_RECORD_CHANGES_TOURNAMENT_ADMISSION=NO
```

## 1. Evidence semantics

```text
PUBLIC_PROVIDER_METADATA=REMOTE_PROVIDER_REPORTED_EVIDENCE
PUBLIC_PROVIDER_LFS_OR_XET_IDENTITY=REMOTE_CONTENT_IDENTITY_EVIDENCE
PUBLIC_PROVIDER_INTEGER_BYTES=REMOTE_PROVIDER_OR_POINTER_FILE_SIZE_EVIDENCE
LOCAL_BYTE_VERIFICATION=CRYPTOGRAPHIC_HASH_OVER_LOCALLY_MATERIALIZED_BYTES
```

```text
PUBLIC_PROVIDER_METADATA_EQUALS_LOCAL_BYTE_VERIFICATION=NO
PUBLIC_PROVIDER_SHA256_EQUALS_LOCALLY_RECOMPUTED_SHA256=NO
PUBLIC_PROVIDER_INTEGER_BYTES_EQUALS_LOCAL_FILE_STAT=NO
FROZEN_REVISION_IDENTITY_EQUALS_OLDER_CLARIFICATION_REVISION=NO_UNLESS_EXACTLY_EQUAL
SAME_CONTENT_SHA256_MAKES_DISTINCT_REVISION_IDENTITIES_INTERCHANGEABLE=NO
```

A content identity may remain unchanged across repository revisions. That continuity does not erase or replace the exact frozen revision identity.

---

## 2. Qwen3-0.6B-Base PRIMARY — frozen-revision reconciliation

### 2.1 Canonical frozen identity

```text
SOURCE_REPOSITORY=Qwen/Qwen3-0.6B-Base
SOURCE_REVISION=da87bfb608c14b7cf20ba1ce41287e8de496c0cd
ROLE=PRIMARY
SOURCE_LICENSE=Apache-2.0
SOURCE_WEIGHT_FILE=model.safetensors
```

Exact frozen-revision public source:

```text
https://huggingface.co/Qwen/Qwen3-0.6B-Base/tree/da87bfb608c14b7cf20ba1ce41287e8de496c0cd
https://huggingface.co/Qwen/Qwen3-0.6B-Base/blob/da87bfb608c14b7cf20ba1ce41287e8de496c0cd/model.safetensors
```

The frozen-revision weight page reports:

```text
FROZEN_REVISION_PUBLIC_PROVIDER_WEIGHT_SHA256=cd2a512003e2f9f3cd3c32a9c3573f820bb28c940f73c57b1ddaa983d9223eba
FROZEN_REVISION_PUBLIC_PROVIDER_WEIGHT_XET_HASH=2c465b10ceca99084a7d3d8451bd593ac1ea835f3516b7ccc7279b177351021f
FROZEN_REVISION_PUBLIC_PROVIDER_DISPLAY_SIZE=1.19_GB
```

### 2.2 Historical Spec 005 revision is not the E001 frozen revision

The older clarification record:

```text
specs/005-base-model-tournament/qwen3-0.6b-exact-binding-evidence.md
```

bound:

```text
HISTORICAL_SPEC005_REVISION=d4e79cdcc24cc3dc566196f5af6ed5782c64e8f1
```

The E001 freeze later bound:

```text
E001_FROZEN_REVISION=da87bfb608c14b7cf20ba1ce41287e8de496c0cd
```

These revision identities are different and must remain visibly different.

```text
HISTORICAL_SPEC005_REVISION_EQUALS_E001_FROZEN_REVISION=NO
HISTORICAL_REVISION_MAY_SUBSTITUTE_FOR_E001_FROZEN_REVISION=NO
```

However, the weight content identity observed in the historical record is the same SHA-256/Xet identity reported at the later frozen revision:

```text
HISTORICAL_WEIGHT_SHA256=cd2a512003e2f9f3cd3c32a9c3573f820bb28c940f73c57b1ddaa983d9223eba
FROZEN_REVISION_WEIGHT_SHA256=cd2a512003e2f9f3cd3c32a9c3573f820bb28c940f73c57b1ddaa983d9223eba
WEIGHT_SHA256_CONTINUITY_ACROSS_REVISIONS=OBSERVED

HISTORICAL_WEIGHT_XET_HASH=2c465b10ceca99084a7d3d8451bd593ac1ea835f3516b7ccc7279b177351021f
FROZEN_REVISION_WEIGHT_XET_HASH=2c465b10ceca99084a7d3d8451bd593ac1ea835f3516b7ccc7279b177351021f
WEIGHT_XET_CONTINUITY_ACROSS_REVISIONS=OBSERVED
```

This is content continuity only. It is not a claim that every non-weight file stayed unchanged across the two revisions.

### 2.3 Exact remote weight byte evidence

A public Git-LFS pointer for this same SHA-256 content identity records:

```text
PUBLIC_LFS_WEIGHT_SHA256=cd2a512003e2f9f3cd3c32a9c3573f820bb28c940f73c57b1ddaa983d9223eba
PUBLIC_LFS_WEIGHT_INTEGER_BYTES=1192135096
```

Public pointer source:

```text
https://huggingface.co/Qwen/Qwen3-0.6B-Base/blame/15c1898c3109c305f9f13cd74555b04ff204dada/model.safetensors
```

The pointer is used to bind the exact remote-file byte count for the same content identity. It is not substituted as the frozen revision locator.

```text
QWEN3_0_6B_PUBLIC_PROVIDER_WEIGHT_SHA256=BOUND
QWEN3_0_6B_PUBLIC_PROVIDER_WEIGHT_XET_HASH=BOUND
QWEN3_0_6B_PUBLIC_PROVIDER_WEIGHT_INTEGER_BYTES=BOUND_BY_CONTENT_IDENTITY_POINTER_FOR_REVIEW
QWEN3_0_6B_LOCAL_WEIGHT_BYTES_MATERIALIZED=NO
QWEN3_0_6B_LOCAL_WEIGHT_SHA256_RECOMPUTED=NO
```

### 2.4 Remaining Qwen3-0.6B source-bundle evidence

The frozen revision binds repository paths for configuration/tokenizer assets, but this reconciliation does not fabricate individual local or provider content hashes for each required non-weight conversion/runtime input.

```text
QWEN3_0_6B_EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=NEEDS_EVIDENCE
QWEN3_0_6B_TOKENIZER_CONTENT_SHA256_AT_FROZEN_REVISION=NEEDS_EVIDENCE
QWEN3_0_6B_LOCAL_SOURCE_BUNDLE_INTEGRITY=INCOMPLETE
```

---

## 3. Qwen3.5-0.8B-Base PRIMARY — exact frozen-revision reconciliation

### 3.1 Canonical frozen identity

```text
SOURCE_REPOSITORY=Qwen/Qwen3.5-0.8B-Base
SOURCE_REVISION=dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
ROLE=PRIMARY
SOURCE_LICENSE=Apache-2.0
SOURCE_WEIGHT_FILE=model.safetensors-00001-of-00001.safetensors
SOURCE_INDEX_FILE=model.safetensors.index.json
```

Public exact frozen-revision sources:

```text
https://huggingface.co/Qwen/Qwen3.5-0.8B-Base/tree/dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
https://huggingface.co/Qwen/Qwen3.5-0.8B-Base/blob/dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68/model.safetensors-00001-of-00001.safetensors
https://huggingface.co/Qwen/Qwen3.5-0.8B-Base/blob/dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68/tokenizer.json
```

The existing Spec 005 clarification record already binds this exact frozen revision.

### 3.2 Weight content and exact remote bytes

```text
PUBLIC_PROVIDER_WEIGHT_SHA256=c2b1e5a17d9c1e27685d92ed9b382911ebb99955ecd89052d1721241adfbab6c
PUBLIC_PROVIDER_WEIGHT_XET_HASH=0a75fae984a2baafa5ee5b256274748f8589e950f788b1f877ec6d2da891aa67
PUBLIC_PROVIDER_WEIGHT_INTEGER_BYTES=1746942600
```

The exact byte count is exposed by the public LFS pointer for the same provider weight identity.

Public upload/pointer source:

```text
https://huggingface.co/Qwen/Qwen3.5-0.8B-Base/commit/a5fba42799b133463178a6603d0fc31ced693c5d
```

### 3.3 Index metadata remains a distinct quantity

The exact frozen-revision index records:

```text
PUBLIC_PROVIDER_INDEX_METADATA_TOTAL_SIZE=1746882752
```

```text
INDEX_METADATA_TOTAL_SIZE_EQUALS_REMOTE_WEIGHT_CONTAINER_BYTES=NO_ASSUMPTION
REMOTE_WEIGHT_CONTAINER_BYTES=1746942600
INDEX_METADATA_TOTAL_SIZE=1746882752
INDEX_MINUS_CONTAINER_BYTES=-59848
```

The index field and remote container-file byte count are not silently treated as the same semantic quantity. No defect is inferred merely from the difference.

### 3.4 Tokenizer content identity

At the exact frozen revision, the public tokenizer page reports:

```text
TOKENIZER_FILE=tokenizer.json
PUBLIC_PROVIDER_TOKENIZER_SHA256=fe000e3ed39ed12b8d2481d527d44f93c65d37e87645d2dcc80d1bf9d50d2927
PUBLIC_PROVIDER_TOKENIZER_XET_HASH=59036b7ec9c1c130de9dd3716f37308a51038389ae6fb9ba62e87c246696707a
PUBLIC_PROVIDER_TOKENIZER_INTEGER_BYTES=12807196
```

The existing Spec 005 clarification record already captured the SHA-256/Xet identity. This reconciliation adds the exact remote integer byte count to the current E002 provider-evidence view.

```text
QWEN3_5_0_8B_PUBLIC_PROVIDER_WEIGHT_SHA256=BOUND
QWEN3_5_0_8B_PUBLIC_PROVIDER_WEIGHT_XET_HASH=BOUND
QWEN3_5_0_8B_PUBLIC_PROVIDER_WEIGHT_INTEGER_BYTES=BOUND_FOR_REVIEW
QWEN3_5_0_8B_PUBLIC_PROVIDER_TOKENIZER_SHA256=BOUND
QWEN3_5_0_8B_PUBLIC_PROVIDER_TOKENIZER_XET_HASH=BOUND
QWEN3_5_0_8B_PUBLIC_PROVIDER_TOKENIZER_INTEGER_BYTES=BOUND_FOR_REVIEW
QWEN3_5_0_8B_LOCAL_SOURCE_BYTES_MATERIALIZED=NO
QWEN3_5_0_8B_LOCAL_WEIGHT_SHA256_RECOMPUTED=NO
QWEN3_5_0_8B_LOCAL_TOKENIZER_SHA256_RECOMPUTED=NO
```

### 3.5 Remaining Qwen3.5 source-bundle evidence

```text
QWEN3_5_0_8B_EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=NEEDS_EVIDENCE
QWEN3_5_0_8B_LOCAL_SOURCE_BUNDLE_INTEGRITY=INCOMPLETE
```

The tokenizer identity above does not imply that `config.json`, index, processor files, vocabulary, merges, or every future required conversion/runtime input has a complete exact hash set.

---

## 4. Relationship to PR #104 and Decision B

PR #104 canonically reconciled exact public-provider evidence for the two `ARTIFACT_DECISION_B` conversion subjects:

```text
GRANITE_PRIMARY=a50b46cef21c8a86b15f0496cb794487a78a910b
QWEN3_4B_CONTROL=906bfd4b4dc7f14ee4320094d8b41684abff8539
```

This record covers different E001 PRIMARY candidates and must not be used to widen that conversion-subject decision.

```text
ARTIFACT_DECISION_B_SCOPE_UNCHANGED=YES
QWEN3_0_6B_ADDED_TO_DECISION_B=NO
QWEN3_5_0_8B_ADDED_TO_DECISION_B=NO
CONVERSION_EXECUTION_AUTHORITY=NONE
```

## 5. No admission or downstream authority effect

```text
E002_AUTHORITY=AUTHORIZED_EXISTING_FROZEN_PUBLIC_CANDIDATES_ONLY
MODEL_WEIGHT_ACCESS_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY

PRIMARY_TOURNAMENT_ADMISSION_CHANGED_BY_THIS_RECORD=NO
BACKBONE_WINNER_SELECTED=NO
MODEL_CONVERSION_AUTHORITY=NONE
QUANTIZATION_OF_MODEL_WEIGHTS_AUTHORITY=NONE
MODEL_LOADING_AUTHORITY_EXPANSION=NONE
MODEL_INFERENCE_AUTHORITY_EXPANSION=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY_EXPANSION=NONE
BENCHMARK_EXECUTION_AUTHORITY_EXPANSION=NONE
DEVICE_QUALIFICATION_AUTHORITY_EXPANSION=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
SELECTION_SUITE_CONSTRUCTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The separate bounded GitHub Actions `llama-quantize` build-evidence allowance is unaffected:

```text
AUTHORIZED_MANUAL_BUILD_EVIDENCE_RUN_ALLOWANCE_REMAINING=1
BUILD_EXECUTION_OCCURRED_ON_GITHUB_ACTIONS_PATH=NO
BUILD_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

## 6. Required exact-head review

Fresh review must independently verify:

1. both repository/revision identities exactly match the canonical E001 frozen PRIMARY set;
2. Qwen3-0.6B frozen revision `da87bfb...` is not conflated with historical Spec 005 revision `d4e79cd...`;
3. the Qwen3-0.6B weight SHA-256/Xet values match at the E001 frozen revision and equal the historical content identity;
4. the exact remote weight byte count `1192135096` is supported for that same content identity and is not described as a local file observation;
5. Qwen3.5-0.8B weight SHA-256/Xet and remote byte count `1746942600` are exact;
6. Qwen3.5 index `metadata.total_size=1746882752` remains semantically distinct from remote container bytes;
7. Qwen3.5 tokenizer SHA-256/Xet and remote byte count `12807196` are exact at the frozen revision;
8. no incomplete non-weight hash set is promoted to complete;
9. no E002/Decision B/admission/conversion/tournament/training/spend authority is expanded;
10. the exact diff remains record-only and raw Actions on the exact head are zero.

## 7. Current lifecycle effect

```text
E002_REMAINING_PRIMARY_PROVIDER_METADATA_RECONCILIATION=PREPARED_FOR_REVIEW
QWEN3_0_6B_FROZEN_WEIGHT_PROVIDER_IDENTITY=BOUND_FOR_REVIEW
QWEN3_5_0_8B_FROZEN_WEIGHT_PROVIDER_IDENTITY=BOUND_FOR_REVIEW
QWEN3_5_0_8B_FROZEN_TOKENIZER_PROVIDER_IDENTITY=BOUND_FOR_REVIEW
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
ARTIFACT_DECISION_B_SCOPE_UNCHANGED=YES
CONVERSION_EXECUTION_AUTHORITY=NONE
BUILD_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Canonical merge of this record would close only this provider-metadata reconciliation. It would not establish local source-bundle integrity, change tournament admission, authorize conversion/model execution, or advance E004/E005.