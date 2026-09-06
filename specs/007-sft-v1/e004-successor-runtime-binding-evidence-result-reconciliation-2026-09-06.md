# E004 Successor Runtime-Binding Evidence Result Reconciliation — 2026-09-06

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical base before this result:** `6a86bbc4a52adac3846a1eef97f89cb170fe202b`  
**Controlling authority:** `specs/007-sft-v1/e004-successor-runtime-binding-evidence-authorization-2026-09-05.md`  
**Workflow:** `.github/workflows/e004-successor-runtime-binding-evidence-v3.yml`  
**Artifact class:** append-only runtime/toolchain/environment evidence result reconciliation  
**Authority effect:** NONE  
**Model execution authority effect:** NONE  
**Tournament execution authority effect:** NONE  
**A15 authority effect:** NONE  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose and claim boundary

Capture only the deterministic, non-sensitive evidence actually emitted by the single bounded successor runtime-binding evidence run authorized on 2026-09-05.

This record is based on the live GitHub Actions run metadata, job metadata, decoded retained job logs, the canonical workflow bytes, and the live workflow-artifact listing. It does not infer evidence that the run did not emit and it does not reinterpret successful job status as model-load, tournament, resource, access, A15, or execution-subject PASS.

The runtime evidence lane remained non-model throughout:

```text
MODEL_WEIGHT_DOWNLOAD_BY_RUNTIME_EVIDENCE_LANE=PROHIBITED
MODEL_LOAD=PROHIBITED
MODEL_EXECUTION=PROHIBITED
TOURNAMENT_EXECUTION=PROHIBITED
A15_ACTIVATION=PROHIBITED
CONVERSION=PROHIBITED
TRAINING=PROHIBITED
CREDENTIAL_USE=PROHIBITED
ARTIFACT_UPLOAD=PROHIBITED
PAID_OR_LARGER_RUNNER=PROHIBITED
SPEND_USD=0
```

## 2. One-run authority consumption

The controlling authorization allowed exactly one runtime-binding evidence run and no rerun by default. The authorized run was created and completed successfully.

```text
E004_SUCCESSOR_RUNTIME_BINDING_EVIDENCE_AUTHORITY=AUTHORIZED_BOUNDED
MAX_AUTHORIZED_RUNTIME_BINDING_EVIDENCE_RUNS=1
RUNTIME_BINDING_EVIDENCE_RUNS_CONSUMED=1
RUNTIME_BINDING_EVIDENCE_RUNS_REMAINING=0
RERUN_AUTHORITY=NONE_BY_DEFAULT
FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
SECOND_RUNTIME_BINDING_EVIDENCE_RUN_AUTHORITY=NONE
```

No later continuation wording reopens this consumed allowance.

## 3. Exact run and job identity

```text
RUN_ID=33974098680
RUN_NUMBER=2
RUN_ATTEMPT=1
RUN_EVENT=push
RUN_HEAD_BRANCH=evidence/e004-successor-runtime-binding-run-v1
RUN_HEAD_SHA=f5f5fbdcafa82d11bc0ddeb3dc641c729cf9fc79
RUN_HEAD_TREE=ed5ba0e2f76d736460e68f33b2c8f90215ca6a52
RUN_STATUS=completed
RUN_CONCLUSION=success
RUN_STARTED_AT=2026-09-05T15:12:43Z
RUN_UPDATED_AT=2026-09-05T15:13:40Z

LLAMA_RUNTIME_JOB_ID=101327644627
LLAMA_RUNTIME_JOB_NAME=llama-runtime-evidence
LLAMA_RUNTIME_JOB_CONCLUSION=success

TRANSFORMERS_RUNTIME_JOB_ID=101327644698
TRANSFORMERS_RUNTIME_JOB_NAME=transformers-runtime-evidence
TRANSFORMERS_RUNTIME_JOB_CONCLUSION=success

STATIC_QUALIFICATION_PUSH_JOB_ID=101327645478
STATIC_QUALIFICATION_PUSH_JOB_NAME=static-qualification
STATIC_QUALIFICATION_PUSH_JOB_CONCLUSION=skipped

WORKFLOW_ARTIFACT_COUNT=0
WORKFLOW_ARTIFACTS=[]
```

The skipped static-qualification job is expected on the push event; that job is the pull-request-only qualification lane. The two runtime-evidence jobs are the authorized push-only lanes.

## 4. Shared runner-image evidence

Both runtime jobs reported the same GitHub-hosted runner software/image family:

```text
RUNNER_VERSION=2.337.0
HOSTED_COMPUTE_AGENT_VERSION=20260828.587
HOSTED_COMPUTE_AGENT_COMMIT=abac92662cab4cc7352de4f9f9d2e2419aad9c29
RUNNER_OS=Linux
RUNNER_ARCH=X64
IMAGE_OS=ubuntu24
IMAGE_VERSION=20260831.293.1
OPERATING_SYSTEM=Ubuntu_24.04.4_LTS
```

The individual hosted agents were provisioned in different Azure regions, so region is not treated as one shared execution identity:

```text
LLAMA_RUNTIME_AZURE_REGION=eastus2
TRANSFORMERS_RUNTIME_AZURE_REGION=centralus
```

This runner evidence does not by itself create the later `execution_environment_id`, resource binding, or access binding required by the live SP007 pre-execution subject.

## 5. Exact llama.cpp runtime evidence

The llama runtime job acquired and verified the exact public upstream release archive bound by the authorization:

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
```

Non-model introspection of that exact executable completed in an offline network namespace and emitted:

```text
LLAMA_CLI_VERSION=0.3.0-dev_build_10621_commit_c1d0e7a00
LLAMA_CLI_BUILD_TOOLCHAIN=GNU_11.4.0_for_Linux_x86_64
LLAMA_CLI_NON_MODEL_INTROSPECTION=PASS_OFFLINE_NAMESPACE
```

The exact source-revision architecture header also emitted:

```text
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

These values directly establish exact public runtime archive/file/executable identity and static architecture support for the authorized GGUF route investigation. They do not establish candidate model-load compatibility because no candidate model file was opened.

## 6. Exact Transformers/Torch dependency-closure evidence

The Transformers runtime job staged the exact public Python dependency closure using public PyPI and PyTorch indexes only. The retained log emitted:

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

The dependency-set manifest differs from earlier historical runtime-evidence observations and is intentionally recorded as the fresh identity emitted by this run rather than inherited from an older runner state.

## 7. Exact offline installed-environment and import evidence

After acquisition, installation and static/import-only inspection ran in a default-deny network namespace. The retained log emitted:

```text
PYTHON_RUNTIME_PATH=/usr/bin/python3.12
PYTHON_RUNTIME_VERSION=Python_3.12.3
PYTHON_RUNTIME_SHA256=a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223
INSTALLED_ENVIRONMENT_MANIFEST_SHA256=54517b34077e193c9bc019e8a2b232d3c9b6d6a85c4c6df13bcd38aa2b66c384
PHASE_B_NETWORK=DEFAULT_DENY_NETWORK_NAMESPACE_FOR_INSTALL_AND_IMPORT
CREDENTIAL_USE_PERFORMED=NO
ARTIFACT_UPLOAD_PERFORMED=NO
MODEL_LOAD_PERFORMED=NO
MODEL_EXECUTION_PERFORMED=NO
SPEND_USD=0
```

Exact imported module identities were:

```text
TRANSFORMERS_MODULE_SHA256=aa8cb54da488cf43ba37b9955bb6c0d84d2000db0306f6a5f1c20b6842482d04
TORCH_MODULE_SHA256=0387d8b811b289287479c8bfdf4e1dac3a71b246f938d82da1331cf2dc8bf001
QWEN3_CONFIG_MODULE_SHA256=27863e9718fdbc899f2d0e567621e4d3d36d8dc500c1d54b49dba4242d08d2bd
QWEN3_MODELING_MODULE_SHA256=4b95c371fd26d40c69083dab36ac1eafd8cf82b415a0bb827275097c5ad2305b
GRANITE_CONFIG_MODULE_SHA256=535090da0bd3606c7be77517d2de4839f70b9658a40d4ec9ba98fb365397dc39
GRANITE_MODELING_MODULE_SHA256=920678d503bcb6795ba46c1b9579c28aad208a3ff0b73e7e02754e7cd9e3c19c
```

The import-only mapping assertions emitted:

```text
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
```

This directly closes static/import-only runtime recognition for Qwen3 and Granite under the exact installed environment. It does not establish candidate weight loading, tensor materialization, inference, or generation compatibility because those actions were prohibited and did not occur.

## 8. Negative-operation evidence

Across the bounded runtime-evidence lane, the logs and artifact endpoint establish only the following negative-operation facts:

```text
MODEL_FILE_OPENED_BY_LLAMA_RUNTIME=NO
MODEL_WEIGHT_FILE_OPENED_BY_TRANSFORMERS_RUNTIME=NO
MODEL_OBJECT_INSTANTIATED=NO
MODEL_LOAD_PERFORMED=NO
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
A15_ACTIVATION_PERFORMED=NO
CONVERSION_PERFORMED=NO
TRAINING_PERFORMED=NO
CREDENTIAL_USE_PERFORMED=NO
ARTIFACT_UPLOAD_PERFORMED=NO
WORKFLOW_ARTIFACT_COUNT=0
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
SPEND_USD=0
```

`PRIVATE_GOLD_ACCESSED=NO` and `PHI_ACCESSED=NO` follow the controlling workflow/authority boundary and the absence of any such input surface in the runtime-evidence jobs; this record does not expose or reproduce any protected material.

## 9. Directly closed evidence fields

The run directly supports these narrow evidence dispositions:

```text
LLAMA_RUNTIME_ARCHIVE_INTEGRITY=PASS
LLAMA_RUNTIME_FILE_MANIFEST_IDENTITY=PASS
LLAMA_RUNTIME_EXECUTABLE_IDENTITY=PASS
LLAMA_RUNTIME_SOURCE_REVISION_BINDING=PASS
LLAMA_QWEN3_STATIC_ARCHITECTURE_SUPPORT=PASS
LLAMA_QWEN35_STATIC_ARCHITECTURE_SUPPORT=PASS
TRANSFORMERS_DEPENDENCY_CLOSURE_IDENTITY=PASS
TRANSFORMERS_PYTHON_RUNTIME_IDENTITY=PASS
TRANSFORMERS_INSTALLED_ENVIRONMENT_MANIFEST_IDENTITY=PASS
TRANSFORMERS_QWEN3_STATIC_IMPORT_COMPATIBILITY=PASS
TRANSFORMERS_GRANITE_STATIC_IMPORT_COMPATIBILITY=PASS
RUNTIME_EVIDENCE_CREDENTIAL_BOUNDARY=PASS_NO_CREDENTIAL_USE
RUNTIME_EVIDENCE_ARTIFACT_UPLOAD_BOUNDARY=PASS_NO_UPLOAD
RUNTIME_EVIDENCE_SPEND_BOUNDARY=PASS_USD_0
```

These are evidence-field dispositions only. They are not equivalent to a complete live candidate runtime binding or a PASS pre-execution subject.

## 10. Fields not closed by this run

The following live-subject requirements remain unresolved because this evidence lane did not directly prove them:

```text
LIVE_FOUR_CANDIDATE_COMPLETE_BUNDLE_BINDINGS=INCOMPLETE
LIVE_FOUR_CANDIDATE_TOKENIZER_CONFIG_BINDINGS=INCOMPLETE
LIVE_FOUR_CANDIDATE_EXECUTION_ARGV=INCOMPLETE
LIVE_FOUR_CANDIDATE_EXECUTION_PLAN_SHA256=INCOMPLETE
LIVE_EXECUTION_ENVIRONMENT_BINDING=INCOMPLETE
LIVE_RESOURCE_BINDING=INCOMPLETE
LIVE_ACCESS_BINDING=INCOMPLETE
ZERO_INCREMENTAL_SPEND_EXECUTION_RESOURCE_BINDING=INCOMPLETE
A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
```

For the safetensors route, `STATIC_IMPORT_ONLY_COMPATIBILITY=PASS` must not be rewritten as model-load compatibility. For the GGUF route, static architecture support and non-model executable introspection must not be rewritten as successful candidate-file loading.

## 11. Successor disposition

```text
RUNTIME_BINDING_EVIDENCE_RESULT=PASS_WITH_NARROW_DIRECT_FIELDS_ONLY
RUNTIME_BINDING_EVIDENCE_AUTHORITY_CONSUMED=YES
RUNTIME_BINDING_EVIDENCE_RERUN_AUTHORITY=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
MODEL_EXECUTION_NOW=NOT_AUTHORIZED_BY_GATE_STATE
TOURNAMENT_EXECUTION_NOW=NOT_AUTHORIZED_BY_GATE_STATE
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_PERFORMED=NO
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

The next dependency-safe work is to reconcile the newly proven runtime fields into the exact four-candidate pre-execution dependency graph and determine which remaining subject-component bindings can be constructed deterministically from already-canonical evidence without model execution or new authority.