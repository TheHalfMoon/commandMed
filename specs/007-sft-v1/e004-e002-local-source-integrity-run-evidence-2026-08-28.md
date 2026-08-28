# E004 / E002 Local Source Integrity Run Evidence — 2026-08-28

**Spec:** 007 SFT V1  
**E002 purpose:** bounded non-executing public source acquisition and local integrity verification  
**E004 relationship:** Decision B source-subject evidence only  
**Canonical workflow merge:** `dd85e9e22de0dccf0043c8905be1c2d9fb5f68a4`  
**Qualified workflow head:** `cb05e8ec48d0b0c3ea209402ca3632d1340a3fbd`  
**Execution marker head:** `d4404ee56c7b2fb1018650c5c05e9dc3eb5b59b2`  
**Workflow run:** `33183096268`  
**Run attempt:** `1`  
**Event:** `push`  
**Run conclusion:** `success`  
**Model load performed:** NO  
**Model conversion performed:** NO  
**Model inference performed:** NO  
**Benchmark access performed:** NO  
**Artifact upload performed:** NO  
**Training performed:** NO  
**Credential use performed:** NO  
**Reviewer outreach performed:** NO  
**Spend:** USD 0

## 1. Purpose and authority boundary

This record captures real execution evidence for the exact non-executing acquisition/integrity work already authorized by canonical E002 for the frozen public/ungated source subjects used by Decision B preparation.

It does not grant or exercise model conversion, quantization, inference, benchmark/device execution, contamination assessment, A15 activation, training, credential, Private Gold, PHI, provider-generation, personnel, engagement, procurement, payment, or spend authority.

```text
E002_AUTHORITY_USED=AUTHORIZED_FROZEN_PUBLIC_SOURCE_ACQUISITION_AND_INTEGRITY_ONLY
E003_TOURNAMENT_EXECUTION_AUTHORITY_USED=NO
E004_MODEL_EXECUTION_OCCURRED=NO
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The run is also independent of the separately authorized E004 `llama-quantize` build-evidence lane. No `workflow_dispatch` run was created or consumed.

```text
E004_BUILD_EVIDENCE_ALLOWANCE_CONSUMED_BY_THIS_RUN=NO
AUTHORIZED_BUILD_WORKFLOW_TRIGGER=workflow_dispatch_only
WORKFLOW_DISPATCH_RUN_COUNT_AFTER_E002_RUN=0
AUTHORIZED_BUILD_MANUAL_RUN_EXECUTED=NO
AUTHORIZED_BUILD_MANUAL_RUN_ALLOWANCE_REMAINING=1
BUILD_PASS=NO
```

## 2. Workflow qualification and execution identity

The executable workflow was added only after a review-first qualification cycle.

```text
WORKFLOW_PATH=.github/workflows/e002-public-source-integrity-evidence.yml
QUALIFIED_WORKFLOW_HEAD=cb05e8ec48d0b0c3ea209402ca3632d1340a3fbd
WORKFLOW_CANONICAL_MERGE=dd85e9e22de0dccf0043c8905be1c2d9fb5f68a4
WORKFLOW_CANONICAL_TREE=389d235ac072f6a094db49ceada13e3490daca96
EXECUTION_BRANCH=evidence/e002-source-integrity-run-v1
EXECUTION_MARKER_PATH=.github/e002-source-integrity-run-v1.txt
EXECUTION_MARKER_HEAD=d4404ee56c7b2fb1018650c5c05e9dc3eb5b59b2
RUN_ID=33183096268
RUN_NUMBER=1
RUN_ATTEMPT=1
RUN_EVENT=push
RUN_CONCLUSION=success
```

The qualified workflow exact-head review reported:

```text
WORKFLOW_INERT_BEFORE_REVIEWED_MERGE=YES
E002_SCOPE_VALID=YES
BUILD_EVIDENCE_ALLOWANCE_ISOLATED=YES
ALL_PROVIDER_IDENTITIES_MATCH_CANONICAL=YES
NO_CREDENTIAL_USE=YES
NO_MODEL_OR_CONVERTER_EXECUTION=YES
NO_BENCHMARK_OR_TRAINING_EXECUTION=YES
NO_ARTIFACT_CACHE_OR_REPOSITORY_WRITE=YES
FAIL_CLOSED_DOWNLOAD_AND_INTEGRITY=YES
YAML_BASH_VALID=YES
EPHEMERAL_PASS_SCOPE_VALID=YES
NO_DOWNSTREAM_AUTHORITY_EXPANSION=YES
MATERIAL_BLOCKER=NO
```

No run existed on the qualified workflow head before canonical merge.

## 3. GitHub-hosted runner evidence

Both jobs ran on the standard public `ubuntu-24.04` class and reported:

```text
RUNNER_VERSION=2.336.0
HOSTED_COMPUTE_AGENT_VERSION=20260819.586
HOSTED_COMPUTE_AGENT_COMMIT=3cc4a88dfa507ef76119ad1bb3eccc6378bb2b76
RUNNER_OS=Linux
RUNNER_ARCH=X64
IMAGE_OS=ubuntu24
IMAGE_VERSION=20260823.283.1
OPERATING_SYSTEM=Ubuntu_24.04.4_LTS
AZURE_REGION=westcentralus
```

The runner image identity matches the previously canonical static runner-image evidence for `ImageVersion=20260823.283.1`; this run now supplies runtime evidence for the acquisition/hash lane only.

The jobs explicitly unset and fail-closed on the following credential variables before acquisition:

```text
HF_TOKEN=UNSET
HUGGING_FACE_HUB_TOKEN=UNSET
GH_TOKEN=UNSET
GITHUB_TOKEN=UNSET_INSIDE_ACQUISITION_SCRIPT
CREDENTIAL_USE_OCCURRED=NO
```

GitHub's job bootstrap reports only the platform's metadata-read token permission. The acquisition shell itself unsets the token variables and performs direct public HTTPS downloads without authorization headers or provider credentials.

## 4. Granite PRIMARY local integrity evidence

```text
JOB_NAME=granite-integrity
JOB_ID=98889052166
JOB_CONCLUSION=success
SUBJECT=E004-CONVERT-GRANITE-350M-Q4_K_M-V1
ROLE=PRIMARY
SOURCE_REPOSITORY=ibm-granite/granite-4.0-350m-base
SOURCE_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
LOCAL_SOURCE_DIRECTORY_BASENAME=granite-4.0-350m-base
LOCAL_SELECTED_FILE_COUNT=9
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=PASS_ON_EPHEMERAL_RUNNER
LOCAL_INTEGRITY_MANIFEST_SHA256=67eac7cb98525612030aa608a1eb5d473e5045319ce4ce78a6aa4174f78b646a
```

The runner downloaded every exact selected file to a temporary `.part` path, recomputed integer byte size and SHA-256, required equality with the canonical provider-bound values, and only then promoted the file into the ephemeral source directory.

| Local file | Recomputed bytes | Recomputed SHA-256 |
|---|---:|---|
| `README.md` | `26418` | `e0786791023161d3f6dbc7e20a4efb278a1ef09a6a0abb9599bdba2e47a89378` |
| `config.json` | `1764` | `089690e22b9eafadcdd385afa5b6f3ea2446674ff5398c71df23be059d7c795d` |
| `generation_config.json` | `147` | `7c04cb9d2ba771f7528fba5a7104999cdaf7566d02b5fbd58472829f62716177` |
| `merges.txt` | `916646` | `b6fe424e334903f7fb84d3a106d9730455f4744b9fe3c21ee136d97a00e72502` |
| `model.safetensors` | `704786224` | `a65363c0803a05c1c74e114c692c57f35b2641aeffce24d5a8ee8fad3b34dcf0` |
| `special_tokens_map.json` | `579` | `c08676c49fd7969a3130f72be6d4bf34da66aa484a6e21dffe359893a1bd5f2e` |
| `tokenizer.json` | `7153421` | `e2bad66439538cb4d5a7580680932432ed9ece9d3b8577e675512bdf11599253` |
| `tokenizer_config.json` | `17659` | `a5ec5daab12ba090a90f3dd169c8f9c275557013a87b9c1258dc7cb497a35c86` |
| `vocab.json` | `1612704` | `8af71076de8b0b626eed0f4c984faf0a7c062479164b2a31308a948524d4f69c` |

The job also required exactly nine regular files and no symlinks before emitting its PASS state.

```text
GRANITE_LOCAL_SOURCE_WEIGHT_BYTES_MATERIALIZED_DURING_RUN=YES
GRANITE_LOCAL_SOURCE_WEIGHT_SHA256_RECOMPUTED=YES
GRANITE_LOCAL_INTEGER_SOURCE_WEIGHT_BYTES=704786224
GRANITE_LOCAL_SELECTED_NON_WEIGHT_SHA256_SET=RECOMPUTED_AND_MATCHED
GRANITE_LOCAL_SOURCE_DIRECTORY_BASENAME_ATTESTED=YES
GRANITE_EPHEMERAL_LOCAL_INTEGRITY=PASS
```

## 5. Qwen3-4B CONTROL local integrity evidence

```text
JOB_NAME=qwen-control-integrity
JOB_ID=98889051893
JOB_CONCLUSION=success
SUBJECT=E004-CONVERT-QWEN3-4B-CONTROL-Q4_K_M-V1
ROLE=CONTROL
WINNER_ELIGIBLE=NO
SOURCE_REPOSITORY=Qwen/Qwen3-4B-Base
SOURCE_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
LOCAL_SOURCE_DIRECTORY_BASENAME=Qwen3-4B-Base
LOCAL_SELECTED_FILE_COUNT=11
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=PASS_ON_EPHEMERAL_RUNNER
LOCAL_INTEGRITY_MANIFEST_SHA256=ac831cb724268dcb54f90d9bf41c972ba25d18f7a087e56a27933f69f84b2ab8
```

The runner used the same fail-closed acquisition/integrity procedure for all three frozen weight shards and the exact selected non-weight surface.

| Local file | Recomputed bytes | Recomputed SHA-256 |
|---|---:|---|
| `README.md` | `2937` | `9fd20ab531a1dc75ae18fcde658dd69d04173fdb93311091c38a7098e3d4b4a1` |
| `config.json` | `727` | `304b2545a258d35620f1d4bf46940c0471d9baa00715ff8e77f84c2fca5057c1` |
| `generation_config.json` | `138` | `8c970692323e3ea0e9b8b0a4dca79388d31226e41f83c9fd6014804280ebf6e8` |
| `merges.txt` | `1671853` | `8831e4f1a044471340f7c0a83d7bd71306a5b867e95fd870f74d0c5308a904d5` |
| `model-00001-of-00003.safetensors` | `3957900840` | `4c807e2503d68ae373d508689d00a41f4b33f33c2536da97ab81a20caddc1241` |
| `model-00002-of-00003.safetensors` | `3987450520` | `f4707585548b2fc75a6b1d732e8465c62040a8699903c32850781beeb9b27826` |
| `model-00003-of-00003.safetensors` | `99630640` | `c7b1aa8fb672de2e00423c99876926022e50b18d4f0d140670788510a27f9965` |
| `model.safetensors.index.json` | `32819` | `d6c42883a895dfef5b0080ed2116a1bcd764f558406b98923d675978a1abf29c` |
| `tokenizer.json` | `7031645` | `c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539` |
| `tokenizer_config.json` | `9678` | `3c04ed3ca964ea2f6b2b5faf0dc4d31aec1cb1e8b4bcf63f402d295046b422b5` |
| `vocab.json` | `2776833` | `ca10d7e9fb3ed18575dd1e277a2579c16d108e32f27439684afa0e10b1440910` |

The job required exactly eleven regular files and no symlinks before emitting PASS.

```text
QWEN_LOCAL_SOURCE_WEIGHT_BYTES_MATERIALIZED_DURING_RUN=YES
QWEN_LOCAL_SOURCE_WEIGHT_SHA256_PER_SHARD=RECOMPUTED_AND_MATCHED
QWEN_LOCAL_INTEGER_SOURCE_WEIGHT_BYTES_PER_SHARD=3957900840,3987450520,99630640
QWEN_LOCAL_WEIGHT_CONTAINER_BYTES_SUM=8044982000
QWEN_LOCAL_SELECTED_NON_WEIGHT_SHA256_SET=RECOMPUTED_AND_MATCHED
QWEN_LOCAL_SOURCE_DIRECTORY_BASENAME_ATTESTED=YES
QWEN_EPHEMERAL_LOCAL_INTEGRITY=PASS
```

No assumption is made that the model index metadata `total_size` equals the physical container-byte sum.

## 6. Run-wide negative evidence

Both jobs completed successfully with the workflow's fail-closed prohibitions in force.

```text
MODEL_LOAD_OCCURRED=NO
MODEL_CONVERSION_OCCURRED=NO
MODEL_INFERENCE_OCCURRED=NO
BENCHMARK_ACCESS_OCCURRED=NO
DEVICE_QUALIFICATION_OCCURRED=NO
ARTIFACT_UPLOAD_OCCURRED=NO
WORKFLOW_ARTIFACT_COUNT=0
CACHE_UPLOAD_OCCURRED=NO
REPOSITORY_WRITE_FROM_RUN_OCCURRED=NO
CREDENTIAL_USE_OCCURRED=NO
TRAINING_OCCURRED=NO
REVIEWER_OUTREACH_OCCURRED=NO
PRIVATE_GOLD_ACCESS_OCCURRED=NO
PHI_ACCESS_OCCURRED=NO
PROVIDER_GENERATION_OCCURRED=NO
PROCUREMENT_OCCURRED=NO
PAYMENT_OCCURRED=NO
SPEND_USD=0
```

The GitHub Actions artifacts endpoint for run `33183096268` returned an empty artifact list.

## 7. What this evidence supersedes

Earlier current-state records correctly stated that no commandMed-local source bytes had been materialized or cryptographically recomputed at their capture time. Run `33183096268` now creates later real evidence that exact frozen bytes were materialized and recomputed in commandMed's governed GitHub Actions execution context.

For **evidence existence**, these stale current-state fields are superseded:

```text
GRANITE_LOCAL_SOURCE_WEIGHT_SHA256_RECOMPUTED=YES_ON_RUN_33183096268
GRANITE_LOCAL_INTEGER_SOURCE_WEIGHT_BYTES=704786224_ON_RUN_33183096268
QWEN_LOCAL_SOURCE_WEIGHT_SHA256_PER_SHARD=RECOMPUTED_AND_MATCHED_ON_RUN_33183096268
QWEN_LOCAL_INTEGER_SOURCE_WEIGHT_BYTES_PER_SHARD=RECOMPUTED_ON_RUN_33183096268
LOCAL_SELECTED_NON_WEIGHT_INPUT_SHA256_SET=RECOMPUTED_AND_MATCHED_ON_RUN_33183096268
LOCAL_SOURCE_DIRECTORY_BASENAME_ATTESTATION=PASS_ON_RUN_33183096268
LOCAL_SOURCE_BUNDLE_BYTE_INTEGRITY=PASS_EPHEMERAL_EVIDENCE_ON_RUN_33183096268
```

This does **not** mean the bytes remain available after the hosted runners are destroyed.

## 8. Persistent execution-subject gaps remain

The acquisition/integrity run used ephemeral GitHub-hosted runner storage and intentionally uploaded no source artifacts. Therefore it does not establish a persistent conversion workspace or a future conversion-time path.

```text
PERSISTENT_LOCAL_SOURCE_BUNDLE_PRESENT=NO
PERSISTENT_EXACT_LOCAL_SOURCE_DIRECTORY=NEEDS_EVIDENCE
FUTURE_CONVERSION_TIME_SOURCE_PATH=NEEDS_EVIDENCE
EXACT_LOCAL_OUTPUT_DIRECTORY=NEEDS_EVIDENCE
```

No conversion runtime was created or installed by this lane. The following remain unresolved:

```text
PYTHON_RUNTIME_IDENTITY_FOR_CONVERSION=NEEDS_EVIDENCE
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256=NEEDS_EVIDENCE
DEPENDENCY_PACKAGE_HASH_SET=NEEDS_EVIDENCE
CONVERSION_RUNTIME_EXECUTABLE_OR_INTERPRETER_IDENTITY=NEEDS_EVIDENCE
LLAMA_QUANTIZE_EXECUTABLE_SHA256=NEEDS_EVIDENCE
BUILD_ENVIRONMENT_MANIFEST_SHA256=NEEDS_EVIDENCE
EXACT_CONVERSION_ARGV_WITHOUT_PLACEHOLDERS=NEEDS_EVIDENCE
NETWORK_DISABLEMENT_OR_NAMESPACE_ENFORCEMENT_IDENTITY=NEEDS_EVIDENCE
CREDENTIAL_SCAN_OR_ENVIRONMENT_ATTESTATION_IDENTITY_FOR_CONVERSION=NEEDS_EVIDENCE
EXACT_STORAGE_BOUNDARY_IDENTITY=NEEDS_EVIDENCE
FILESYSTEM_OR_VOLUME_IDENTITY=NEEDS_EVIDENCE
ACCESS_CONTROL_OR_PROCESS_ISOLATION_IDENTITY=NEEDS_EVIDENCE
RETENTION_ENFORCEMENT_IDENTITY=NEEDS_EVIDENCE
EXACT_COMPUTE_RESOURCE_IDENTITY_FOR_CONVERSION=NEEDS_EVIDENCE
EXPECTED_CPU_RAM_DISK_ENVELOPE_FOR_CONVERSION=NEEDS_EVIDENCE
EXPECTED_MAX_WALLCLOCK_FOR_CONVERSION=NEEDS_EVIDENCE
ZERO_INCREMENTAL_SPEND_DISPOSITION_FOR_CONVERSION=NEEDS_EVIDENCE
```

Exact runtime/dependency/environment creation or execution requires then-current authority that actually permits it. This record grants none.

## 9. Scientific/governance and A15 blockers are unchanged

```text
T1_A2=INCOMPLETE_REAL_EVIDENCE_NUMERIC_POLICY_AND_QUALIFIED_REVIEW
D34_A3_A4=BLOCKED_BY_T1
G1_A5_REAL_GATE_PASS=NO
G2_A6_REAL_GATE_PASS=NO
G3_A8_REAL_GATE_PASS=NO
G4_A12_REAL_GATE_PASS=NO
REAL_PERSONNEL_ACCESS_FINANCE_EVIDENCE=INCOMPLETE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
REAL_A1_TO_A14_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
```

Repository/AI review cannot impersonate these real scientific, governance, personnel, access, finance, contamination, or activation requirements.

## 10. Current bounded conclusion

Run `33183096268` materially advances the Decision B preparation frontier by replacing provider-only/static integrity with real commandMed-governed ephemeral local recomputation evidence for both exact frozen source subjects.

It does not close E004 and does not make E005 reachable.

```text
E002_PUBLIC_SOURCE_ACQUISITION_PATH=EXECUTED_SUCCESSFULLY
DECISION_B_EPHEMERAL_LOCAL_BYTE_INTEGRITY=PASS
GRANITE_EPHEMERAL_LOCAL_BYTE_INTEGRITY=PASS
QWEN_CONTROL_EPHEMERAL_LOCAL_BYTE_INTEGRITY=PASS
PERSISTENT_CONVERSION_SOURCE_WORKSPACE=ABSENT
MODEL_CONVERSION_AUTHORITY=NONE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The next dependency-safe work must not recreate this acquisition evidence. It may only advance another already-authorized and actually executable branch, or append-only reconcile current-state records to this later evidence.

## 11. Direct evidence locators

```text
WORKFLOW_PR=121
WORKFLOW_MERGE=dd85e9e22de0dccf0043c8905be1c2d9fb5f68a4
EXECUTION_MARKER_HEAD=d4404ee56c7b2fb1018650c5c05e9dc3eb5b59b2
RUN_URL=https://github.com/TheHalfMoon/commandMed/actions/runs/33183096268
GRANITE_JOB_URL=https://github.com/TheHalfMoon/commandMed/actions/runs/33183096268/job/98889052166
QWEN_JOB_URL=https://github.com/TheHalfMoon/commandMed/actions/runs/33183096268/job/98889051893
```
