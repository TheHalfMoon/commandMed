# E004 Registry Current-State Reconciliation V32 — 2026-09-05

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical base before this reconciliation:** `6d328b9a64a420bcb43fcd08f82745fd2604d47c`  
**Predecessor:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v31-2026-09-05.md`  
**Artifact class:** deterministic current-state and dependency-frontier overlay  
**Authority effect:** only the separately recorded bounded runtime-binding evidence authorization in this same transition  
**Model execution effect:** NONE  
**A15 effect:** NONE  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Reconcile the successor frontier after:

1. canonical merge of the hardened exact-subject execution control plane;
2. canonical merge of the review-first E002 preconverted byte-integrity workflow;
3. successful real E002 byte-integrity run `33972164617` for the exact two allowlisted GGUF artifacts;
4. recovery of already-canonical real source-bundle integrity evidence from run `33183096268` for Granite PRIMARY and Qwen3-4B CONTROL;
5. identification of exact public runtime candidates that can be investigated without model execution.

This record does not claim that an executable four-candidate subject exists yet.

## 2. Canonical control-plane state after PRs #258-#260

The exact-subject lock remains intentionally closed:

```text
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
STRUCTURALLY_COMPLETE_SYNTHETIC_SUBJECT_CAN_BUILD_LIVE_REQUEST=NO
LIVE_SP007_PREEXECUTION_SUBJECT=ABSENT
```

The current frozen tournament identities remain:

```text
SCOPE_ID=SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1
PROTOCOL_ID=SP007_RO_001_NONCLINICAL_BACKBONE_TOURNAMENT_V1
PROTOCOL_SHA256=1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8
EVALUATION_ASSET_SET_SHA256=709d5f73c1599364fc184b959cbdfd199c7ec07307fef8f8091d8eafb10f5454
```

## 3. Exact candidate byte-integrity evidence now available

### Qwen3 0.6B PRIMARY

```text
CANDIDATE=Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
E002_PRECONVERTED_ARTIFACT_REPOSITORY=Antigma/Qwen3-0.6B-Base-GGUF
E002_PRECONVERTED_ARTIFACT_REVISION=f457544766bcdc72afd3514439eb3d422d4434dc
E002_PRECONVERTED_ARTIFACT_FILENAME=qwen3-0.6b-base-q4_k_m.gguf
MODEL_ARTIFACT_SHA256=218d3f063193b40008d4e63d90cf83e7dc6d33a8c6c1c647589f868a8fc74492
MODEL_ARTIFACT_BYTES=396704512
STATIC_CONTAINER_MAGIC=GGUF
BYTE_INTEGRITY=PASS_ON_RUN_33972164617
E001_LABEL=EXACT_BASE_DERIVATIVE_FEASIBILITY_ONLY_NOT_FINAL_RELEASE_BINDING
```

### Qwen3.5 0.8B PRIMARY

```text
CANDIDATE=Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
E002_PRECONVERTED_ARTIFACT_REPOSITORY=ggml-org/Qwen3.5-0.8B-Base-GGUF
E002_PRECONVERTED_ARTIFACT_REVISION=1bd44f68963429437d08bc12f465716eb31ba6e5
E002_PRECONVERTED_ARTIFACT_FILENAME=Qwen3.5-0.8B-Base-Q4_0.gguf
MODEL_ARTIFACT_SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
MODEL_ARTIFACT_BYTES=563035840
STATIC_CONTAINER_MAGIC=GGUF
BYTE_INTEGRITY=PASS_ON_RUN_33972164617
E001_LABEL=DIRECT_DIGEST_PUBLIC_METADATA
```

### Granite 350M PRIMARY source bundle

Canonical run `33183096268` already recomputed all nine selected source files, including the exact `model.safetensors` bytes and tokenizer/config surface.

```text
CANDIDATE=ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
SOURCE_WEIGHT_SHA256=a65363c0803a05c1c74e114c692c57f35b2641aeffce24d5a8ee8fad3b34dcf0
SOURCE_WEIGHT_BYTES=704786224
SELECTED_SOURCE_FILE_COUNT=9
SELECTED_SOURCE_BUNDLE_BYTES=714515562
LOCAL_INTEGRITY_MANIFEST_SHA256=67eac7cb98525612030aa608a1eb5d473e5045319ce4ce78a6aa4174f78b646a
SOURCE_BUNDLE_BYTE_INTEGRITY=PASS_ON_RUN_33183096268
PRIMARY_COMPLETE_BUNDLE_HARD_CAP_BYTES=734003200
SOURCE_SELECTED_BUNDLE_MARGIN_TO_HARD_CAP_BYTES=19487638
```

The selected source bundle fits under the frozen PRIMARY hard cap. This is size/integrity evidence, not yet an execution-bundle PASS; the exact runtime/environment route remains unbound.

### Qwen3-4B CONTROL source bundle

```text
CANDIDATE=Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
ROLE=CONTROL
WINNER_ELIGIBLE=NO
SOURCE_WEIGHT_SHARD_COUNT=3
SOURCE_WEIGHT_CONTAINER_BYTES_SUM=8044982000
SELECTED_SOURCE_FILE_COUNT=11
SELECTED_SOURCE_BUNDLE_BYTES=8056508630
LOCAL_INTEGRITY_MANIFEST_SHA256=ac831cb724268dcb54f90d9bf41c972ba25d18f7a087e56a27933f69f84b2ab8
SOURCE_BUNDLE_BYTE_INTEGRITY=PASS_ON_RUN_33183096268
PRIMARY_PACKAGE_HARD_CAP_APPLIES=NO
```

The CONTROL is exempt from the PRIMARY package cap but remains subject to all exact runtime/environment/resource/access identities.

## 4. Artifact gate disposition after new evidence

The old V31 statement that the two E002 GGUFs had provider metadata only is superseded.

```text
QWEN06_BYTE_INTEGRITY=PASS
QWEN35_BYTE_INTEGRITY=PASS
GRANITE_SELECTED_SOURCE_BYTE_INTEGRITY=PASS
CONTROL_SELECTED_SOURCE_BYTE_INTEGRITY=PASS
EXACT_FOUR_CANDIDATE_FROZEN_IDENTITY_SET=PASS
```

However:

```text
FINAL_QWEN06_RUNTIME_BINDING=INCOMPLETE
FINAL_QWEN35_RUNTIME_BINDING=INCOMPLETE
FINAL_GRANITE_RUNTIME_BINDING=INCOMPLETE
FINAL_CONTROL_RUNTIME_BINDING=INCOMPLETE
EXACT_FOUR_CANDIDATE_EXECUTION_ARTIFACT_SET=INCOMPLETE
EXECUTABLE_FORMAT_COMPATIBILITY_FOR_EXACT_FOUR_CANDIDATE_RUN=INCOMPLETE
```

Byte integrity is necessary but does not substitute for runtime compatibility or exact subject binding.

## 5. Exact runtime evidence candidates

### GGUF route candidate

An exact upstream runtime release exists for the same `llama.cpp` source revision already used by canonical E004 build/runtime evidence:

```text
LLAMA_CPP_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
LLAMA_CPP_VERSION=0.3.0
NIGHTLY_TAG=b10621
NIGHTLY_TARGET_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
UBUNTU_X64_RUNTIME_ARCHIVE=llama-b10621-bin-ubuntu-x64.tar.gz
UBUNTU_X64_RUNTIME_ARCHIVE_BYTES=16291771
UBUNTU_X64_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
```

The exact source revision statically contains both `LLM_ARCH_QWEN3` and `LLM_ARCH_QWEN35` architecture identifiers. No executable identity inside the archive has yet been recomputed by commandMed, so compatibility remains `INCOMPLETE_PENDING_AUTHORIZED_RUNTIME_EVIDENCE`.

### Safetensors route candidate

Existing canonical conversion-runtime evidence already binds an exact CPU Python dependency family including:

```text
TRANSFORMERS_VERSION=4.57.6
TORCH_RUNTIME_TARGET=2.11.0+cpu
DEPENDENCY_SET_MANIFEST_SHA256=ebfd3c49dc83c35b3ad00e0d4d8b903502a8951fd65da80186b6677007bbfd3f
```

The Transformers `v4.57.6` tag resolves to exact commit:

```text
TRANSFORMERS_TAG_TARGET_COMMIT=753d61104116eefc8ffc977327b441ee0c8d599f
```

That exact source contains Qwen3 and Granite model/configuration implementations. This supports a non-model static/import-only investigation for Granite PRIMARY and Qwen3-4B CONTROL. It does not establish model-load compatibility until an authorized runtime evidence lane proves the exact installed environment and class/config recognition without opening candidate weights.

Qwen3.5 is not assigned to this Transformers route by this reconciliation.

## 6. Runtime evidence authority now bounded separately

The Founder continuation direction is captured by:

`specs/007-sft-v1/e004-successor-runtime-binding-evidence-authorization-2026-09-05.md`

Its effect is limited to one review-first, non-model runtime-binding evidence unit.

```text
E004_SUCCESSOR_RUNTIME_BINDING_EVIDENCE_AUTHORITY=AUTHORIZED_BOUNDED
MAX_AUTHORIZED_RUNTIME_BINDING_EVIDENCE_RUNS=1
MODEL_WEIGHT_DOWNLOAD_BY_RUNTIME_EVIDENCE_LANE=PROHIBITED
MODEL_LOAD=PROHIBITED
MODEL_EXECUTION=PROHIBITED
TOURNAMENT_EXECUTION=PROHIBITED
A15_ACTIVATION=PROHIBITED
CONVERSION=PROHIBITED
TRAINING=PROHIBITED
CREDENTIAL_USE=PROHIBITED
SPEND_USD=0
```

## 7. Remaining non-A15 preflight blockers

After the evidence above, the following still require genuine exact bindings:

```text
EXACT_RUNTIME_ARCHIVE_OR_PACKAGE_INTEGRITY=INCOMPLETE_FOR_SELECTED_ROUTES
EXACT_RUNTIME_EXECUTABLE_SHA256=INCOMPLETE
EXACT_RUNTIME_SOURCE_REVISION_BINDING=PARTIAL_STATIC_EVIDENCE_ONLY
EXACT_BUILD_OR_PACKAGE_TOOLCHAIN_IDENTITY=INCOMPLETE_FOR_CURRENT_EXECUTION_SUBJECT
EXACT_TOKENIZER_OR_CONFIG_EXECUTION_BINDING=INCOMPLETE
EXACT_EXECUTION_ARGV=INCOMPLETE
EXACT_EXECUTION_PLAN_SHA256=INCOMPLETE
EXACT_ENVIRONMENT_MANIFEST_SHA256=INCOMPLETE_FOR_CURRENT_RUNNER_IMAGE
EXACT_NETWORK_DURING_EXECUTION_BINDING=INCOMPLETE
EXACT_CREDENTIAL_STATE_BINDING=INCOMPLETE
EXACT_RESOURCE_BINDING=INCOMPLETE
EXACT_ACCESS_BINDING=INCOMPLETE
ZERO_INCREMENTAL_SPEND_RESOURCE_BINDING=INCOMPLETE
A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
```

The older runtime evidence was collected on runner image `20260823.283.1`; the new E002 integrity run observed image `20260831.293.1`. Environment identities therefore may not be inherited across image drift without fresh evidence.

## 8. A15 remains separate and blocked

```text
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
GENERIC_CONTINUATION_COUNTS_AS_A15_ACTIVATION=NO
```

The new runtime-binding evidence authority does not alter this state.

## 9. Fresh successor disposition

```text
SUCCESSOR_PREFLIGHT_DISPOSITION=BLOCKED
SUCCESSOR_PASS_PREFLIGHT=NO
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
MODEL_EXECUTION_NOW=NOT_AUTHORIZED_BY_GATE_STATE
TOURNAMENT_EXECUTION_NOW=NOT_AUTHORIZED_BY_GATE_STATE
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

## 10. Next dependency-safe frontier

The next authorized unit is now exact and narrow:

1. review and qualify an inert runtime-binding evidence workflow;
2. after canonical merge, execute exactly one standard-runner evidence run under the bounded runtime-binding evidence authority;
3. bind the exact `llama.cpp` Ubuntu x64 runtime archive/files and static Qwen3/Qwen3.5 route evidence without model files;
4. bind an exact Transformers/Torch CPU environment and static/import-only Qwen3/Granite route evidence without model files;
5. canonicalize the resulting runtime/toolchain/environment evidence;
6. then recompute resource/access/finance and applicable A1-A14 successor prerequisites;
7. only after all non-A15 prerequisites genuinely pass, prepare the exact separate A15 decision surface.

No model execution is dependency-safe before steps 1-7 are complete.