# E004 Successor Runtime-Binding Evidence Result — 2026-09-06

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Evidence authority:** `E004_SUCCESSOR_RUNTIME_BINDING_EVIDENCE_AUTHORITY=AUTHORIZED_BOUNDED`  
**Authority record:** `specs/007-sft-v1/e004-successor-runtime-binding-evidence-authorization-2026-09-05.md`  
**Canonical workflow merge:** `6a86bbc4a52adac3846a1eef97f89cb170fe202b`  
**Canonical workflow:** `.github/workflows/e004-successor-runtime-binding-evidence-v3.yml`  
**Authority effect of this record:** NONE beyond recording already-observed evidence and consumed bounded-run state  
**Model execution effect:** NONE  
**Tournament execution effect:** NONE  
**A15 effect:** NONE  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Canonically capture the exact non-model runtime/toolchain/static-compatibility evidence emitted by the single authorized successor runtime-binding evidence run. This record does not infer any value that was not observed in the GitHub Actions run or already bound by canonical repository authority.

No model artifact was opened by either runtime evidence job. No model object was instantiated from candidate weights. No model was loaded or executed. No tournament or evaluation payload was executed. No credential was used. No artifact was uploaded. No spend was incurred.

## 2. Exact authorized run identity

```text
WORKFLOW_RUN_ID=33974098680
WORKFLOW_NAME=E004 successor runtime binding evidence V3
EVENT=push
RUN_NUMBER=2
RUN_ATTEMPT=1
RUN_STATUS=completed
RUN_CONCLUSION=success
RUN_HEAD_BRANCH=evidence/e004-successor-runtime-binding-run-v1
RUN_HEAD_SHA=f5f5fbdcafa82d11bc0ddeb3dc641c729cf9fc79
RUN_HEAD_TREE=ed5ba0e2f76d736460e68f33b2c8f90215ca6a52
RUN_STARTED_AT=2026-09-05T15:12:43Z
RUN_UPDATED_AT=2026-09-05T15:13:40Z
WORKFLOW_ARTIFACT_COUNT=0
```

The evidence trigger commit contains only `.github/e004-successor-runtime-binding-run-v1.txt` and explicitly preserves the no-model/no-spend boundary.

## 3. Bounded run authority is consumed

The canonical authorization permits exactly one runtime-binding evidence run and grants no rerun authority by default. The run above is that one execution.

```text
MAX_AUTHORIZED_RUNTIME_BINDING_EVIDENCE_RUNS=1
AUTHORIZED_RUNTIME_BINDING_EVIDENCE_RUNS_EXECUTED=1
AUTHORIZED_RUNTIME_BINDING_EVIDENCE_RUNS_REMAINING=0
RUNTIME_BINDING_EVIDENCE_AUTHORITY_STATE=CONSUMED_EXACTLY_ONCE
RERUN_AUTHORITY=NONE_BY_DEFAULT
FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
RUNTIME_BINDING_EVIDENCE_RERUN_AUTHORIZED_NOW=NO
```

No rerun is permitted by this record.

## 4. Job dispositions

```text
LLAMA_RUNTIME_JOB_ID=101327644627
LLAMA_RUNTIME_JOB_NAME=llama-runtime-evidence
LLAMA_RUNTIME_JOB_CONCLUSION=success

TRANSFORMERS_RUNTIME_JOB_ID=101327644698
TRANSFORMERS_RUNTIME_JOB_NAME=transformers-runtime-evidence
TRANSFORMERS_RUNTIME_JOB_CONCLUSION=success

STATIC_QUALIFICATION_PUSH_JOB_ID=101327645478
STATIC_QUALIFICATION_PUSH_JOB_NAME=static-qualification
STATIC_QUALIFICATION_PUSH_JOB_CONCLUSION=skipped
```

The static qualification job is expected to be inert on the push evidence path. Its skipped conclusion is not represented as substantive review or as an independent scientific PASS.

## 5. llama.cpp runtime evidence

The llama job observed the standard GitHub-hosted `ubuntu-24.04` runner image `20260831.293.1`, Linux x64, Ubuntu 24.04.4 LTS. The exact runtime evidence emitted by the job is:

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
LLAMA_CLI_VERSION=0.3.0-dev_BUILD_10621_COMMIT_c1d0e7a00
LLAMA_CLI_BUILD_TOOLCHAIN=GNU_11.4.0_LINUX_X86_64
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

This establishes exact archive/file/executable identities, exact source revision binding, non-model executable introspection, and static Qwen3/Qwen3.5 architecture support for this investigated llama.cpp route. It does not claim that either exact E002 GGUF model artifact was opened or successfully loaded.

## 6. Transformers/Torch runtime evidence

The Transformers job observed the standard GitHub-hosted `ubuntu-24.04` runner image `20260831.293.1`, Linux x64, Ubuntu 24.04.4 LTS. Its acquisition phase used only the public PyPI and PyTorch package indexes, with credential variables unset. The exact dependency evidence emitted by the job is:

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

The job then installed only from the staged local wheelhouse and performed import/static recognition inside a default-deny network namespace. The exact runtime/environment evidence emitted by the job is:

```text
PYTHON_RUNTIME_PATH=/usr/bin/python3.12
PYTHON_RUNTIME_VERSION=Python 3.12.3
PYTHON_RUNTIME_SHA256=a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223
INSTALLED_ENVIRONMENT_MANIFEST_SHA256=54517b34077e193c9bc019e8a2b232d3c9b6d6a85c4c6df13bcd38aa2b66c384
PHASE_B_NETWORK=DEFAULT_DENY_NETWORK_NAMESPACE_FOR_INSTALL_AND_IMPORT
```

The exact imported-module identities and mapping results are:

```text
TRANSFORMERS_MODULE_SHA256=aa8cb54da488cf43ba37b9955bb6c0d84d2000db0306f6a5f1c20b6842482d04
TORCH_MODULE_SHA256=0387d8b811b289287479c8bfdf4e1dac3a71b246f938d82da1331cf2dc8bf001
QWEN3_CONFIG_MODULE_SHA256=27863e9718fdbc899f2d0e567621e4d3d36d8dc500c1d54b49dba4242d08d2bd
QWEN3_MODELING_MODULE_SHA256=4b95c371fd26d40c69083dab36ac1eafd8cf82b415a0bb827275097c5ad2305b
GRANITE_CONFIG_MODULE_SHA256=535090da0bd3606c7be77517d2de4839f70b9658a40d4ec9ba98fb365397dc39
GRANITE_MODELING_MODULE_SHA256=920678d503bcb6795ba46c1b9579c28aad208a3ff0b73e7e02754e7cd9e3c19c
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
CREDENTIAL_USE_PERFORMED=NO
ARTIFACT_UPLOAD_PERFORMED=NO
SPEND_USD=0
```

This establishes exact dependency/Python/installed-environment/module identities and static/import-only Qwen3/Granite recognition for the investigated Transformers route. It does not claim that the exact Granite or Qwen3-4B candidate weight files were opened or loaded.

## 7. Directly closed evidence fields

Only fields directly supported by the run are closed here:

```text
LLAMA_RUNTIME_ARCHIVE_BYTE_INTEGRITY=PASS
LLAMA_RUNTIME_FILE_MANIFEST_IDENTITY=PASS
LLAMA_RUNTIME_EXECUTABLE_IDENTITY=PASS
LLAMA_RUNTIME_SOURCE_REVISION_BINDING=PASS
LLAMA_NON_MODEL_INTROSPECTION=PASS
LLAMA_STATIC_QWEN3_ROUTE_SUPPORT=PASS
LLAMA_STATIC_QWEN35_ROUTE_SUPPORT=PASS

TRANSFORMERS_DEPENDENCY_CLOSURE_IDENTITY=PASS
TRANSFORMERS_PYTHON_RUNTIME_IDENTITY=PASS
TRANSFORMERS_INSTALLED_ENVIRONMENT_MANIFEST_IDENTITY=PASS
TRANSFORMERS_RUNTIME_SOURCE_REVISION_BINDING=PASS
TRANSFORMERS_STATIC_QWEN3_ROUTE_SUPPORT=PASS
TRANSFORMERS_STATIC_GRANITE_ROUTE_SUPPORT=PASS

RUNTIME_EVIDENCE_LANE_MODEL_WEIGHT_ACCESS=NO
RUNTIME_EVIDENCE_LANE_MODEL_LOAD=NO
RUNTIME_EVIDENCE_LANE_MODEL_EXECUTION=NO
RUNTIME_EVIDENCE_LANE_CREDENTIAL_USE=NO
RUNTIME_EVIDENCE_LANE_ARTIFACT_UPLOAD=NO
RUNTIME_EVIDENCE_LANE_SPEND_USD=0
```

## 8. Fields not closed by this evidence lane

The canonical authority explicitly forbids treating this successful evidence run as a substitute for separately required exact subject gates. The following remain unresolved unless separate canonical evidence already or later proves them for the exact future execution subject:

```text
EXACT_FOUR_CANDIDATE_RUNTIME_FORMAT_COMPATIBILITY=INCOMPLETE
EXACT_PER_CANDIDATE_TOKENIZER_OR_CONFIG_EXECUTION_BINDING=INCOMPLETE
EXACT_FINAL_EXECUTION_ENTRYPOINT_AND_ARGV=INCOMPLETE
EXACT_EXECUTION_PLAN_SHA256=INCOMPLETE
EXACT_FUTURE_EXECUTION_ENVIRONMENT_MANIFEST_SHA256=INCOMPLETE
EXACT_NETWORK_DURING_MODEL_EXECUTION_BINDING=INCOMPLETE
EXACT_CREDENTIAL_STATE_FOR_MODEL_EXECUTION_BINDING=INCOMPLETE
EXACT_RESOURCE_BINDING=INCOMPLETE
EXACT_ACCESS_BINDING_FOR_EXECUTION_SUBJECT=INCOMPLETE
ZERO_INCREMENTAL_SPEND_TOURNAMENT_RESOURCE_BINDING=INCOMPLETE
A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
```

Static architecture/class recognition is not represented as successful loading of any candidate artifact. Evidence from the runtime lane is reusable only under exact identity compatibility; future runner-image or package drift requires fresh reconciliation and cannot consume this exhausted one-run authority by inference.

## 9. Explicit non-actions

```text
MODEL_CONVERSION_PERFORMED=NO
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_PERFORMED=NO
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
GATED_ASSET_ACCESSED=NO
CREDENTIAL_USE_PERFORMED=NO
PROCUREMENT_PERFORMED=NO
PAYMENT_PERFORMED=NO
SPEND_USD=0
```

## 10. Next-state rule

This record must be consumed by a fresh successor-frontier reconciliation. That reconciliation may promote only directly evidenced runtime/toolchain/static-support fields. It must preserve the exact-subject lock and fail closed on every unresolved resource/access/environment/argv/tokenizer/config/A1-A14/A15 prerequisite.
