# E004 Decision B Live Subject Reconciliation — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `827222e1871637f684ea038ec8cda5111f98fd2f`  
**Artifact class:** append-only current-state reconciliation  
**Authority effect:** NONE  
**Model/source-weight local materialization performed:** NO  
**Package installation performed:** NO  
**Converter/model/benchmark/device execution performed:** NO  
**Training performed:** NO  
**Spend:** USD 0

This record reconciles the two canonical `ARTIFACT_DECISION_B` conversion subjects after the provider-provenance, selected-input, runtime-dependency, execution-boundary, and normalization-policy chain became canonical. Earlier records remain immutable historical evidence. This record supersedes only stale **current-state interpretation** where a field that was previously unresolved has since become bound at the provider/static-policy layer.

It deliberately distinguishes remote/provider or static-source evidence from local execution-authoritative evidence. A provider-side hash, byte count, object identity, or static policy does not become a locally recomputed integrity result, installed runtime identity, or conversion PASS by transcription.

```text
HISTORICAL_RECORDS_PRESERVED=YES
THIS_RECORD_SUPERSEDES_STALE_CURRENT_STATE_INTERPRETATION_ONLY=YES
REAL_EXECUTION_GATE_PASS_CREATED=NO
AUTHORITY_EXPANDED=NO
```

## 1. Canonical subject and carrier chain

The Decision B subject set remains exactly:

```text
SUBJECT_1=E004-CONVERT-GRANITE-350M-Q4_K_M-V1
SUBJECT_1_ROLE=PRIMARY
SUBJECT_1_SOURCE=ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b

SUBJECT_2=E004-CONVERT-QWEN3-4B-CONTROL-Q4_K_M-V1
SUBJECT_2_ROLE=CONTROL
SUBJECT_2_SOURCE=Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
SUBJECT_2_WINNER_ELIGIBLE=NO
```

Relevant canonical carrier merges now include:

```text
PR104_PROVIDER_WEIGHT_METADATA_MERGE=a46b890e5851bcc59f809fabe399673ec2634c84
PR106_SELECTED_NON_WEIGHT_INPUT_SURFACE_MERGE=39f8e8a1793376cde7d6b8a0213e9e7f9b9b1a46
PR107_METADATA_INPUT_CORRECTION_MERGE=6a74b8284d9fc26342ce6c90aad5417dc3bcafb9
PR108_RUNTIME_DEPENDENCY_RECONCILIATION_MERGE=6d98428b3ea9b68b4e662e8f55d0a01d35432f9a
PR109_EXECUTION_BOUNDARY_PREPARATION_MERGE=2f820acb3e524bdc8e763e20a8e8a57f2b2009ba
PR110_NORMALIZATION_METADATA_POLICY_MERGE=827222e1871637f684ea038ec8cda5111f98fd2f
```

No carrier above grants model conversion authority.

## 2. Source-weight provider evidence — now bound remotely

The older live-frontier overlay still described exact integer source-weight bytes as unresolved. That is no longer current **for provider-side evidence**.

### Granite PRIMARY

Canonical PR #104 binds exact frozen-revision provider evidence:

```text
GRANITE_PROVIDER_WEIGHT_FILE=model.safetensors
GRANITE_PROVIDER_WEIGHT_SHA256=a65363c0803a05c1c74e114c692c57f35b2641aeffce24d5a8ee8fad3b34dcf0
GRANITE_PROVIDER_WEIGHT_XET_HASH=ad623156f038ecd3f840ab101a5e3a7e465bce27b2201348c2d8e786d9c54043
GRANITE_PROVIDER_INTEGER_SOURCE_WEIGHT_BYTES=704786224
GRANITE_PROVIDER_WEIGHT_IDENTITY_STATE=BOUND
```

### Qwen3-4B CONTROL

Canonical PR #104 binds all three exact frozen-revision provider shard identities and integer sizes:

```text
QWEN_PROVIDER_SHARD_1_SHA256=4c807e2503d68ae373d508689d00a41f4b33f33c2536da97ab81a20caddc1241
QWEN_PROVIDER_SHARD_1_INTEGER_BYTES=3957900840
QWEN_PROVIDER_SHARD_1_XET_HASH=5ce2c21cd6643568258b5f339a1069bd27bc74f4e10db9732bd0795fd67f2c0e

QWEN_PROVIDER_SHARD_2_SHA256=f4707585548b2fc75a6b1d732e8465c62040a8699903c32850781beeb9b27826
QWEN_PROVIDER_SHARD_2_INTEGER_BYTES=3987450520
QWEN_PROVIDER_SHARD_2_XET_HASH=06334f44342b0ca51d6a936fd4ddc69b6bef1a52aef8e2887531207afd724ca7

QWEN_PROVIDER_SHARD_3_SHA256=c7b1aa8fb672de2e00423c99876926022e50b18d4f0d140670788510a27f9965
QWEN_PROVIDER_SHARD_3_INTEGER_BYTES=99630640
QWEN_PROVIDER_SHARD_3_XET_HASH=91ccda833766cc1b12e03e1126e75fe5a968f51ae0854c7e90335ab9b0491217

QWEN_PROVIDER_WEIGHT_CONTAINER_BYTES_SUM=8044982000
QWEN_PROVIDER_INDEX_METADATA_TOTAL_SIZE=8045591552
QWEN_PROVIDER_INDEX_TOTAL_SIZE_EQUALS_CONTAINER_BYTES=NO_ASSUMPTION
QWEN_PROVIDER_WEIGHT_IDENTITY_STATE=BOUND
```

Therefore the stale generic interpretation:

```text
EXACT_INTEGER_SOURCE_WEIGHT_BYTES=NEEDS_EVIDENCE
EXACT_INTEGER_SOURCE_WEIGHT_BYTES_PER_QWEN_SHARD=NEEDS_EVIDENCE
```

is superseded only as follows:

```text
PROVIDER_INTEGER_SOURCE_WEIGHT_BYTES=BOUND
PROVIDER_INTEGER_SOURCE_WEIGHT_BYTES_PER_QWEN_SHARD=BOUND
LOCAL_INTEGER_SOURCE_WEIGHT_BYTES=NEEDS_EVIDENCE
LOCAL_INTEGER_SOURCE_WEIGHT_BYTES_PER_QWEN_SHARD=NEEDS_EVIDENCE
```

Provider evidence remains distinct from local byte verification.

## 3. Selected non-weight provider input surface — bound and corrected

PR #106 bound provider raw SHA-256, integer byte counts, and provider Git object identities for the selected non-weight inputs it classified from the pinned converter path. PR #107 then corrected the selected metadata surface after exact source inspection showed additional metadata reads and the source-directory basename semantic dependency.

The correction binds these additional frozen-provider rows:

```text
GRANITE_README_BYTES=26418
GRANITE_README_SHA256=e0786791023161d3f6dbc7e20a4efb278a1ef09a6a0abb9599bdba2e47a89378
GRANITE_README_PROVIDER_GIT_OID=9b8c0ebb687792889ff8cf9d862302138320cf08

GRANITE_GENERATION_CONFIG_BYTES=147
GRANITE_GENERATION_CONFIG_SHA256=7c04cb9d2ba771f7528fba5a7104999cdaf7566d02b5fbd58472829f62716177
GRANITE_GENERATION_CONFIG_PROVIDER_GIT_OID=2eed7ca2d26ec1a753b8800e0bae20c824e8b015

QWEN_GENERATION_CONFIG_BYTES=138
QWEN_GENERATION_CONFIG_SHA256=8c970692323e3ea0e9b8b0a4dca79388d31226e41f83c9fd6014804280ebf6e8
QWEN_GENERATION_CONFIG_PROVIDER_GIT_OID=cbbb3133034e192527e5321b4c679154e4819ab8
```

The exact-head independent review of PR #107 also established:

```text
METADATA_CALL_CHAIN_VERIFIED=YES
DIRECTORY_BASENAME_IS_SEMANTIC_INPUT=YES
ADDITIONAL_MISSING_SELECTED_METADATA_INPUT=NONE
```

Current provider/static interpretation is therefore:

```text
SELECTED_NON_WEIGHT_PROVIDER_INPUT_SURFACE=BOUND_AFTER_PR106_PR107_CORRECTION
PROVIDER_SELECTED_NON_WEIGHT_RAW_HASH_SET=BOUND
PROVIDER_MODEL_INDEX_RAW_SHA256=BOUND_WHERE_APPLICABLE
SOURCE_DIRECTORY_BASENAME_SEMANTIC_REQUIREMENT=BOUND
LOCAL_SELECTED_NON_WEIGHT_RAW_HASH_SET=NEEDS_EVIDENCE
LOCAL_SOURCE_DIRECTORY_BASENAME_ATTESTATION=NEEDS_EVIDENCE
```

## 4. Normalization / metadata policy — static policy is now canonical

PR #110 canonically defines the Decision B normalization/metadata policy against pinned `ggml-org/llama.cpp@c1d0e7a004015f23bc0233470b747b596f29b264`.

Current policy state:

```text
NORMALIZATION_OR_METADATA_POLICY=CANONICAL_STATIC_POLICY_DEFINED
SOURCE_FILE_PREPROCESSING_BY_COMMANDMED=PROHIBITED
SOURCE_METADATA_REWRITE_BY_COMMANDMED=PROHIBITED
TOKENIZER_FILE_REWRITE_BY_COMMANDMED=PROHIBITED
CONFIG_REWRITE_BY_COMMANDMED=PROHIBITED
MODEL_CARD_REWRITE_BY_COMMANDMED=PROHIBITED
GENERATION_CONFIG_REWRITE_BY_COMMANDMED=PROHIBITED
WEIGHT_FILE_REWRITE_BY_COMMANDMED=PROHIBITED
SOURCE_SHARD_REPACKING_BY_COMMANDMED=PROHIBITED
SOURCE_FILENAME_RENAMING_AFTER_SUBJECT_FREEZE=PROHIBITED
SOURCE_DIRECTORY_BASENAME_MUTATION_AFTER_SUBJECT_FREEZE=PROHIBITED
METADATA_OVERRIDE_FILE_SELECTED=NO
MODEL_NAME_OVERRIDE_SELECTED=NO
REMOTE_HF_MODE_SELECTED=NO
TRUST_REMOTE_CODE=FALSE_REQUIRED
```

Pinned converter-internal parsing/normalization may occur only as the converter's own in-memory behavior if conversion is separately authorized. commandMed may not pre-edit source bytes to emulate it.

Runtime/tensor-derived output metadata remains execution-derived:

```text
POST_CONVERSION_METADATA_ATTESTATION=REQUIRED_IF_EXECUTION_IS_LATER_AUTHORIZED
POST_CONVERSION_METADATA_ATTESTATION_STATE=NOT_REACHED
```

Static policy definition is not conversion execution evidence.

## 5. Runtime dependency surface — source manifests bound, execution lock absent

PR #108 canonically binds the pinned upstream runtime/dependency manifests and the local `gguf-py` selection rule.

```text
CONVERTER_RUNTIME_DEPENDENCY_SOURCE_MANIFESTS=BOUND
LOCAL_GGUF_SOURCE_MODE=REQUIRED
NO_LOCAL_GGUF_MUST_BE_UNSET=YES
EXTERNAL_GGUF_CODE_AS_SELECTED_RUNTIME=PROHIBITED
UPSTREAM_FULLY_RESOLVED_DEPENDENCY_LOCK_PRESENT=NO
```

The following remain real execution-environment evidence gaps:

```text
PYTHON_RUNTIME_IDENTITY=NEEDS_EVIDENCE
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256=NEEDS_EVIDENCE
DEPENDENCY_PACKAGE_HASH_SET=NEEDS_EVIDENCE
CONVERSION_RUNTIME_EXECUTABLE_OR_INTERPRETER_IDENTITY=NEEDS_EVIDENCE
BUILD_ENVIRONMENT_MANIFEST_SHA256=NEEDS_EVIDENCE
```

No package installation or runtime-environment creation is performed by this reconciliation.

## 6. Conversion execution boundary — design prepared, operational binding incomplete

PR #109 canonically defines the conversion-specific fail-closed design boundaries:

```text
PHASE_B_NETWORK_POLICY=DEFAULT_DENY
CONVERSION_CREDENTIAL_POLICY=NONE
CONVERSION_STORAGE_ZONE_POLICY=DESIGN_PREPARED
CONVERSION_RETENTION_POLICY=DESIGN_PREPARED_WITH_EXACT_DURATION_UNRESOLVED
CONVERSION_LOGGING_POLICY=DESIGN_PREPARED
EXPECTED_INCREMENTAL_SPEND_USD=0
```

The design does not establish operational PASS. Current required operational evidence includes:

```text
NETWORK_DISABLEMENT_OR_NAMESPACE_ENFORCEMENT_IDENTITY=NEEDS_EVIDENCE
CREDENTIAL_SCAN_OR_ENVIRONMENT_ATTESTATION_IDENTITY=NEEDS_EVIDENCE
EXACT_STORAGE_BOUNDARY_IDENTITY=NEEDS_EVIDENCE
FILESYSTEM_OR_VOLUME_IDENTITY=NEEDS_EVIDENCE
ACCESS_CONTROL_OR_PROCESS_ISOLATION_IDENTITY=NEEDS_EVIDENCE
RETENTION_ENFORCEMENT_IDENTITY=NEEDS_EVIDENCE
EXACT_COMPUTE_RESOURCE_IDENTITY=NEEDS_EVIDENCE
RESOURCE_AUTHORIZATION_BASIS=NEEDS_EVIDENCE
EXPECTED_CPU_RAM_DISK_ENVELOPE=NEEDS_EVIDENCE
EXPECTED_MAX_WALLCLOCK=NEEDS_EVIDENCE
ZERO_INCREMENTAL_SPEND_DISPOSITION=NEEDS_EVIDENCE
```

## 7. Local source-bundle integrity remains the principal Decision B subject blocker

Nothing in PRs #104, #106, #107, #108, #109, or #110 creates commandMed-local source materialization or local cryptographic verification.

Current local subject state remains:

```text
GRANITE_LOCAL_SOURCE_WEIGHT_BYTES_MATERIALIZED=NO
GRANITE_LOCAL_SOURCE_WEIGHT_SHA256_RECOMPUTED=NO
GRANITE_LOCAL_INTEGER_SOURCE_WEIGHT_BYTES=NEEDS_EVIDENCE

QWEN_LOCAL_SOURCE_WEIGHT_BYTES_MATERIALIZED=NO
QWEN_LOCAL_SOURCE_WEIGHT_SHA256_PER_SHARD=NEEDS_EVIDENCE
QWEN_LOCAL_INTEGER_SOURCE_WEIGHT_BYTES_PER_SHARD=NEEDS_EVIDENCE

LOCAL_SELECTED_NON_WEIGHT_INPUT_BYTES_MATERIALIZED=NO
LOCAL_SELECTED_NON_WEIGHT_INPUT_SHA256_SET=NEEDS_EVIDENCE
EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
LOCAL_SOURCE_DIRECTORY_BASENAME_ATTESTATION=NEEDS_EVIDENCE
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
```

Canonical E002 may authorize bounded non-executing acquisition/integrity work only within its exact frozen public scope. This reconciliation performs none of that acquisition itself.

## 8. Exact execution argv remains operationally unresolved

The static policy now rules out unselected modes and overrides, but exact future argv cannot truthfully be frozen with real local paths while the local source and runtime identities are absent.

```text
CONVERSION_ARGV_POLICY_CONSTRAINTS=CANONICAL_PREPARED
EXACT_CONVERSION_ARGV_WITHOUT_PLACEHOLDERS=NEEDS_EVIDENCE
EXACT_LOCAL_OUTPUT_DIRECTORY=NEEDS_EVIDENCE
```

No placeholder path is promoted to execution authority.

## 9. Build-evidence lane remains separate

The bounded `llama-quantize` build-evidence authority remains canonical and separate from model conversion authority.

The canonical GitHub Actions workflow remains manual-only and its single conditional manual allowance remains unconsumed. The connected execution surface still has no authorized operation to initiate a new `workflow_dispatch` run.

```text
E004_CONVERSION_TOOLCHAIN_BUILD_AUTHORITY=AUTHORIZED_BOUNDED
CONVERTER_BUILD_EXECUTION_AUTHORITY=AUTHORIZED_EXACT_LLAMA_CPP_REVISION_BUILD_EVIDENCE_ONLY
GITHUB_BUILD_EVIDENCE_WORKFLOW=CANONICAL_PROMOTED_VERIFIED
GITHUB_BUILD_EVIDENCE_DISPATCH=BLOCKED_CONNECTED_EXECUTION_TOOLING
AUTHORIZED_MANUAL_RUN_EXECUTED=NO
AUTHORIZED_MANUAL_RUN_ALLOWANCE_REMAINING=1
AUTHORIZED_MANUAL_RUN_TRIGGER=workflow_dispatch_only
BUILD_EXECUTION_OCCURRED_ON_GITHUB_ACTIONS_PATH=NO
BUILD_PASS=NO
```

A successful build-evidence run, if later possible under exact authority, would not grant model conversion authority.

## 10. Downstream scientific/governance blockers are unchanged

This subject reconciliation does not alter the independent E004 scientific, governance, contamination, or A15 branches.

```text
T1_A2=INCOMPLETE_REAL_EVIDENCE_NUMERIC_POLICY_AND_QUALIFIED_REVIEW
D34_A3_A4=BLOCKED_BY_T1
G1_G2_G3_G4=REAL_GOVERNANCE_OPERATIONAL_EVIDENCE_INCOMPLETE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
REAL_A1_TO_A14_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
BACKBONE_WINNER=NEEDS_EVIDENCE
```

Repository or AI review cannot impersonate qualified clinical/statistical review, real personnel/access evidence, or explicit A15 activation.

## 11. Current dependency-safe frontier

After this reconciliation, ordinary repository work must not recreate already-bound provider/static evidence. The remaining Decision B subject gaps are predominantly local/operational.

Potentially eligible work under an already-existing exact authority must remain separately justified before mutation or execution. In particular:

1. E002-bounded non-executing local acquisition/integrity evidence for the exact frozen public Decision B source subjects, if the active connected/runtime surface can perform it within E002 constraints;
2. exact runtime/dependency/environment evidence only under a then-current authority that actually permits environment creation or execution;
3. the already-authorized single build-evidence workflow run only if the connected surface exposes an authorized manual dispatch action and all exact pre-run conditions still pass;
4. append-only reconciliation when newer canonical evidence supersedes a stale current-state statement.

Generic continuation approval does not authorize model conversion, benchmark/device execution, contamination assessment, human-review impersonation, training, credentials, procurement, or spend.

## 12. Current state

```text
CANONICAL_BASE_AT_CAPTURE=827222e1871637f684ea038ec8cda5111f98fd2f

PROVIDER_SOURCE_WEIGHT_IDENTITIES=BOUND
PROVIDER_INTEGER_SOURCE_WEIGHT_BYTES=BOUND
PROVIDER_SELECTED_NON_WEIGHT_INPUT_SURFACE=BOUND_AFTER_CORRECTION
NORMALIZATION_OR_METADATA_POLICY=CANONICAL_STATIC_POLICY_DEFINED
CONVERTER_RUNTIME_DEPENDENCY_SOURCE_MANIFESTS=BOUND
CONVERSION_EXECUTION_BOUNDARY_POLICY=CANONICAL_DESIGN_PREPARED

LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=INCOMPLETE
EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
PYTHON_RUNTIME_IDENTITY=NEEDS_EVIDENCE
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256=NEEDS_EVIDENCE
EXACT_CONVERSION_ARGV_WITHOUT_PLACEHOLDERS=NEEDS_EVIDENCE
NETWORK_BOUNDARY=NEEDS_OPERATIONAL_EVIDENCE
CREDENTIAL_STATE=NEEDS_OPERATIONAL_EVIDENCE
STORAGE_AND_RETENTION_POLICY=NEEDS_OPERATIONAL_EVIDENCE
EXPECTED_ZERO_SPEND_RESOURCE_ENVELOPE=DESIGN_PREPARED_OPERATIONAL_BINDING_INCOMPLETE

MODEL_CONVERSION_AUTHORITY=NONE
MODEL_LOADING_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0

BUILD_EXECUTION_OCCURRED=NO
BUILD_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
```

No task checkbox, workflow, executable, source-model byte, benchmark payload, device state, credential, personnel assignment, procurement, or spend state is changed by this record.
