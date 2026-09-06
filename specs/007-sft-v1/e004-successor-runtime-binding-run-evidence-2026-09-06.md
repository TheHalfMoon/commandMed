# E004 Successor Runtime-Binding Run Evidence — 2026-09-06

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Authority record:** `specs/007-sft-v1/e004-successor-runtime-binding-evidence-authorization-2026-09-05.md`  
**Canonical workflow merge:** `6a86bbc4a52adac3846a1eef97f89cb170fe202b`  
**Workflow path:** `.github/workflows/e004-successor-runtime-binding-evidence-v3.yml`  
**Execution branch:** `evidence/e004-successor-runtime-binding-run-v1`  
**Execution marker head:** `f5f5fbdcafa82d11bc0ddeb3dc641c729cf9fc79`  
**Execution marker tree:** `ed5ba0e2f76d736460e68f33b2c8f90215ca6a52`  
**Workflow run:** `33974098680`  
**Run attempt:** `1`  
**Run event:** `push`  
**Run conclusion:** `success`  
**Model load performed:** NO  
**Model execution performed:** NO  
**Tournament execution performed:** NO  
**Model conversion performed:** NO  
**A15 activation performed:** NO  
**Credential use performed:** NO  
**Artifact upload performed:** NO  
**Training performed:** NO  
**Spend:** USD 0

## 1. Purpose and authority boundary

This record canonically captures the deterministic non-model runtime-binding evidence emitted by the single authorized successor runtime-binding evidence run. It closes only fields directly proven by the retained GitHub Actions logs.

It does not authorize or claim candidate weight loading, inference, tournament execution, resource measurement with a model, conversion, quantization, A15 activation, winner selection, training, credential/gated/private-data access, procurement, payment, or spend.

```text
MAX_AUTHORIZED_RUNTIME_BINDING_EVIDENCE_RUNS=1
OBSERVED_AUTHORIZED_RUNTIME_BINDING_EVIDENCE_RUNS=1
REMAINING_AUTHORIZED_RUNTIME_BINDING_EVIDENCE_RUNS=0
RERUN_AUTHORITY=NONE_BY_DEFAULT
MODEL_WEIGHT_OPEN_BY_RUNTIME=NO
MODEL_LOAD_PERFORMED=NO
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
A15_ACTIVATION_PERFORMED=NO
CREDENTIAL_USE_PERFORMED=NO
ARTIFACT_UPLOAD_PERFORMED=NO
SPEND_USD=0
```

The arithmetic disposition above records consumption of the one-run budget without rewriting or broadening the historical authorization record.

## 2. Exact run and job identity

```text
RUN_ID=33974098680
RUN_NUMBER=2
RUN_ATTEMPT=1
RUN_EVENT=push
RUN_BRANCH=evidence/e004-successor-runtime-binding-run-v1
RUN_HEAD_SHA=f5f5fbdcafa82d11bc0ddeb3dc641c729cf9fc79
RUN_HEAD_TREE=ed5ba0e2f76d736460e68f33b2c8f90215ca6a52
RUN_CONCLUSION=success
RUN_STARTED_AT=2026-09-05T15:12:43Z
RUN_UPDATED_AT=2026-09-05T15:13:40Z
LLAMA_RUNTIME_JOB_ID=101327644627
LLAMA_RUNTIME_JOB_CONCLUSION=success
TRANSFORMERS_RUNTIME_JOB_ID=101327644698
TRANSFORMERS_RUNTIME_JOB_CONCLUSION=success
STATIC_QUALIFICATION_PUSH_JOB_ID=101327645478
STATIC_QUALIFICATION_PUSH_JOB_CONCLUSION=skipped
WORKFLOW_ARTIFACT_COUNT=0
```

Both runtime jobs used the standard GitHub-hosted `ubuntu-24.04` image family observed as:

```text
RUNNER_VERSION=2.337.0
RUNNER_OS=Linux
RUNNER_ARCH=X64
RUNNER_IMAGE=ubuntu-24.04
RUNNER_IMAGE_VERSION=20260831.293.1
OPERATING_SYSTEM=Ubuntu_24.04.4_LTS
```

No Actions artifact was retained by the run.

## 3. Exact llama.cpp runtime evidence

The successful `llama-runtime-evidence` job emitted:

```text
LLAMA_CPP_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
LLAMA_CPP_TAG=b10621
RUNTIME_ARCHIVE=llama-b10621-bin-ubuntu-x64.tar.gz
RUNTIME_ARCHIVE_BYTES=16291771
RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
ARCHIVE_LIST_SHA256=ab66a01367012608d57404d71ece042ec5ba67e8511feb260cd96196e86f82d9
RUNTIME_FILE_COUNT=50
RUNTIME_SYMLINK_COUNT=10
RUNTIME_FILE_MANIFEST_SHA256=4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711
LLAMA_CLI_RELATIVE_PATH=llama-b10621/llama-cli
LLAMA_CLI_BYTES=1418312
LLAMA_CLI_SHA256=f0034d9e6959f6c32b40cbb5326f41ccdbac21b77feb27a6f32c0a7465c9ebf7
LLAMA_CLI_NON_MODEL_INTROSPECTION=PASS_OFFLINE_NAMESPACE
LLAMA_CLI_VERSION=0.3.0-dev_build_10621_commit_c1d0e7a00
LLAMA_CLI_BUILD_TOOLCHAIN=GNU_11.4.0_Linux_x86_64
LLAMA_ARCH_HEADER_SHA256=404d6e73de04156ff771dc557cda99c112583d2ddccda3b63ddb159f319fbecf
STATIC_QWEN3_ARCHITECTURE_IDENTIFIER=PASS
STATIC_QWEN35_ARCHITECTURE_IDENTIFIER=PASS
MODEL_FILE_OPENED=NO
MODEL_LOAD_PERFORMED=NO
MODEL_EXECUTION_PERFORMED=NO
CREDENTIAL_USE_PERFORMED=NO
ARTIFACT_UPLOAD_PERFORMED=NO
SPEND_USD=0
```

This proves the exact public archive/file/executable identity and non-model offline introspection of the selected llama.cpp route, plus static architecture identifiers for Qwen3 and Qwen3.5. It does not prove that either frozen GGUF candidate has been opened or executed by this runtime.

## 4. Exact Transformers/Torch dependency evidence

The successful `transformers-runtime-evidence` job emitted the exact dependency-closure identity:

```text
TRANSFORMERS_VERSION=4.57.6
TRANSFORMERS_COMMIT=753d61104116eefc8ffc977327b441ee0c8d599f
TORCH_RUNTIME_TARGET=2.11.0+cpu
DEPENDENCY_ARTIFACT_COUNT=27
DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
PIP_DOWNLOAD_LOG_SHA256=275b237f4640e568ab051a694ded1194bb88f50131b2ac265d7fd8402a6fcc97
PHASE_A_NETWORK=PUBLIC_PYPI_AND_PYTORCH_INDEXES_ONLY
PHASE_A_CREDENTIAL_USE=NO
```

The dependency set is intentionally bound to this run rather than inheriting the older `ebfd3c49...` closure from a different evidence run/image.

## 5. Exact installed Python environment and static/import-only compatibility

The offline install/import phase emitted:

```text
PYTHON_RUNTIME_PATH=/usr/bin/python3.12
PYTHON_RUNTIME_VERSION=Python_3.12.3
PYTHON_RUNTIME_SHA256=a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223
INSTALLED_ENVIRONMENT_MANIFEST_SHA256=54517b34077e193c9bc019e8a2b232d3c9b6d6a85c4c6df13bcd38aa2b66c384
TRANSFORMERS_MODULE_SHA256=aa8cb54da488cf43ba37b9955bb6c0d84d2000db0306f6a5f1c20b6842482d04
TORCH_MODULE_SHA256=0387d8b811b289287479c8bfdf4e1dac3a71b246f938d82da1331cf2dc8bf001
QWEN3_CONFIG_MODULE_SHA256=27863e9718fdbc899f2d0e567621e4d3d36d8dc500c1d54b49dba4242d08d2bd
QWEN3_MODELING_MODULE_SHA256=4b95c371fd26d40c69083dab36ac1eafd8cf82b415a0bb827275097c5ad2305b
GRANITE_CONFIG_MODULE_SHA256=535090da0bd3606c7be77517d2de4839f70b9658a40d4ec9ba98fb365397dc39
GRANITE_MODELING_MODULE_SHA256=920678d503bcb6795ba46c1b9579c28aad208a3ff0b73e7e02754e7cd9e3c19c
TRANSFORMERS_VERSION=4.57.6
TRANSFORMERS_TAG_TARGET_COMMIT=753d61104116eefc8ffc977327b441ee0c8d599f
TORCH_VERSION=2.11.0+cpu
QWEN3_CONFIG_MAPPING=PASS
QWEN3_CAUSAL_LM_MAPPING=PASS
GRANITE_CONFIG_MAPPING=PASS
GRANITE_CAUSAL_LM_MAPPING=PASS
STATIC_IMPORT_ONLY_COMPATIBILITY=PASS
MODEL_OBJECT_INSTANTIATED=NO
MODEL_WEIGHT_FILE_OPENED=NO
MODEL_LOAD_PERFORMED=NO
MODEL_EXECUTION_PERFORMED=NO
PHASE_B_NETWORK=DEFAULT_DENY_NETWORK_NAMESPACE_FOR_INSTALL_AND_IMPORT
CREDENTIAL_USE_PERFORMED=NO
ARTIFACT_UPLOAD_PERFORMED=NO
SPEND_USD=0
```

This proves that the exact installed Transformers/Torch environment recognizes the required Qwen3 and Granite configuration/model mappings under an offline network namespace. It does not construct a candidate model object and does not establish candidate-weight execution compatibility by inference.

## 6. Negative evidence and retention boundary

```text
MODEL_OBJECT_INSTANTIATED=NO
MODEL_WEIGHT_FILE_OPENED=NO
MODEL_LOAD_PERFORMED=NO
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_CONVERSION_PERFORMED=NO
A15_ACTIVATION_PERFORMED=NO
WINNER_SELECTION_PERFORMED=NO
TRAINING_PERFORMED=NO
CREDENTIAL_USE_PERFORMED=NO
ARTIFACT_UPLOAD_PERFORMED=NO
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
PAID_OR_LARGER_RUNNER_USED=NO
SPEND_USD=0
RETENTION=GITHUB_ACTIONS_LOGS_ONLY
```

## 7. Exact current interpretation

The run directly closes the selected runtime archive/package/executable and static/import-only support evidence it emitted. It does not automatically close the complete four-candidate execution subject.

```text
LLAMA_CPP_RUNTIME_ARCHIVE_IDENTITY=PASS_ON_RUN_33974098680
LLAMA_CPP_RUNTIME_EXECUTABLE_IDENTITY=PASS_ON_RUN_33974098680
LLAMA_CPP_QWEN3_STATIC_SUPPORT=PASS_ON_RUN_33974098680
LLAMA_CPP_QWEN35_STATIC_SUPPORT=PASS_ON_RUN_33974098680
TRANSFORMERS_DEPENDENCY_CLOSURE_IDENTITY=PASS_ON_RUN_33974098680
TRANSFORMERS_INSTALLED_ENVIRONMENT_IDENTITY=PASS_ON_RUN_33974098680
TRANSFORMERS_QWEN3_STATIC_IMPORT_MAPPING=PASS_ON_RUN_33974098680
TRANSFORMERS_GRANITE_STATIC_IMPORT_MAPPING=PASS_ON_RUN_33974098680
EXACT_FOUR_CANDIDATE_RUNTIME_BINDINGS=INCOMPLETE
EXACT_FOUR_CANDIDATE_EXECUTION_ARTIFACT_SET=INCOMPLETE
EXACT_FOUR_CANDIDATE_TOKENIZER_CONFIG_BINDINGS=INCOMPLETE
EXACT_FOUR_CANDIDATE_EXECUTION_PLANS=INCOMPLETE
EXACT_RESOURCE_BINDING=INCOMPLETE
EXACT_ACCESS_BINDING=INCOMPLETE
A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
SUCCESSOR_PASS_PREFLIGHT=NO
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_PERFORMED=NO
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

A later reconciliation must combine this evidence with the exact frozen candidate artifact/bundle/config evidence, resource/access/finance evidence, applicable A1-A14 gates, and the still-separate A15 gate before any live execution subject can be authorized.