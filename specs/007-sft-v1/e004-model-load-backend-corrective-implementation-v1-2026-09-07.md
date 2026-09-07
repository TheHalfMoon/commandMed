# E004 Model-Load Backend Corrective Implementation V1 — 2026-09-07

**Spec:** 007 SFT V1
**Task:** E004
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Authority:** `FOUNDER_E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION=E004_MODEL_LOAD_BACKEND_CORRECTIVE_DECISION_B`
**Authority record:** `specs/007-sft-v1/e004-model-load-backend-corrective-founder-decision-2026-09-07.md`
**Authority canonical merge:** `b32fbdc340c298ac194a3db3dce3f1f09ef84187`
**Authority canonical tree:** `be27308c00c0624af4ccf89bd03a3558ca23bff9`
**Predecessor frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v44-2026-09-07.md`
**Prior consumed corrective evidence run:** `34150708258`, attempt `1`
**Implementation state:** REVIEW_FIRST_NOT_YET_CANONICAL
**Model bytes acquired by this record/PR:** NO
**Model load performed by this record/PR:** NO
**Current authorized spend:** USD 0

## 1. Purpose

Prepare the narrow successor correction authorized by canonical backend-corrective Decision B after the consumed corrective evidence run reached `llama_model_load_from_file` for both frozen GGUF candidates but failed because the exact frozen llama.cpp runtime had no registered backend.

The successor correction does not rerun or retry any consumed workflow. It adds only path-bound dynamic backend registration from the exact already-frozen runtime directory, a zero-registration fail-closed gate, exact backend-library identity checks, and one new independently versioned post-merge evidence lane.

## 2. Exact observed predecessor failure

Consumed run `34150708258`, attempt `1`, produced the same exact runtime diagnostic for both GGUF candidates after model load was reached:

```text
llama_model_load_from_file_impl: no backends are loaded. hint: use ggml_backend_load() or ggml_backend_load_all() to load a backend before calling this function
```

Canonical predecessor state remains:

```text
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=PARTIAL_2_PASS_2_FAIL
FOUR_CANDIDATE_MODEL_LOAD_COMPATIBILITY_GATE=FAIL_NOT_PASS
PRIOR_CORRECTIVE_RUN_RERUN_AUTHORITY=NONE
PRIOR_CORRECTIVE_RUN_RETRY_AUTHORITY=NONE
```

## 3. Frozen-source correction

At exact frozen source revision:

```text
LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
```

`ggml/include/ggml-backend.h` exposes `ggml_backend_load_all_from_path` and `ggml_backend_reg_count`, while the frozen upstream simple example registers dynamic backends before model loading.

The model-load helper therefore changes only from:

```text
llama_backend_init
llama_model_default_params
llama_model_load_from_file
llama_model_free
llama_backend_free
```

to:

```text
llama_backend_init
ggml_backend_load_all_from_path
ggml_backend_reg_count
llama_model_default_params
llama_model_load_from_file
llama_model_free
llama_backend_free
```

The helper accepts the already-verified runtime library directory as an explicit second argument, registers only from that path, and returns before model load with `INCOMPLETE_BACKEND_REGISTRATION_NOT_READY` when the registered-backend count is zero.

No context creation, tokenization, decode, encode, batch execution, sampler use, prompt processing, forward pass, logits computation, inference, generation, perplexity, benchmark/evaluation payload execution, tournament execution, winner selection, A15 activation, or training is introduced.

## 4. Frozen runtime identity

No runtime substitution is introduced:

```text
LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
LLAMA_CPP_TAG=b10621
LLAMA_RUNTIME_ARCHIVE=llama-b10621-bin-ubuntu-x64.tar.gz
LLAMA_RUNTIME_ARCHIVE_BYTES=16291771
LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
LLAMA_RUNTIME_FILE_MANIFEST_SHA256=4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711
LIBLLAMA_SHA256=89869a6732162d45aa7fe5ab4b224e484c8f27f58c145e530e99dc59d8772448
LLAMA_BUILD_TOOLCHAIN_IDENTITY=GNU_11.4.0_LINUX_X86_64
```

## 5. Exact dynamic-backend identity discovery evidence

Authorized no-model static workflow run:

```text
STATIC_BACKEND_IDENTITY_DISCOVERY_WORKFLOW_RUN_ID=34153164929
STATIC_BACKEND_IDENTITY_DISCOVERY_WORKFLOW_RUN_ATTEMPT=1
STATIC_BACKEND_IDENTITY_DISCOVERY_JOB_ID=101839437634
STATIC_BACKEND_IDENTITY_DISCOVERY_CONCLUSION=SUCCESS
MODEL_BYTES_ACQUIRED=NO
MODEL_LOAD_PERFORMED=NO
MODEL_FORWARD_PASS_PERFORMED=NO
MODEL_INFERENCE_PERFORMED=NO
GENERATION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
TRAINING_PERFORMED=NO
```

The run reverified the frozen archive byte count/SHA-256, the complete frozen runtime file-manifest SHA-256, and `libllama.so.0.3.0` SHA-256 before deriving the runtime library directory.

Observed exact binding:

```text
BACKEND_LIBRARY_DIRECTORY_RELATIVE=llama-b10621
BACKEND_LIBRARY_COUNT=16
BACKEND_MANIFEST_SHA256=3875fabcb38e9bb09acb0e08f6a0ffc3f97ac4acb1434c83f5ad8b656e86ab79
```

Exact dynamic backend files, measured as resolved target bytes and SHA-256 values from the same verified archive:

| Filename | Bytes | SHA-256 |
| --- | ---: | --- |
| `libggml-base.so` | 919464 | `ebbcda9795124309a9fa492e3a7be49dbbc6b8fd7d95cde1524838f88057fcc3` |
| `libggml-cpu-alderlake.so` | 1141184 | `f1e420c6069bb3d6f310069bb3164b8a2e3895227183dc095f2d521f5d54a7e7` |
| `libggml-cpu-cannonlake.so` | 1286176 | `d7c129e27327bdbe7fe5884aa60e4a5dec9eddbf5adadd3d72f73905ab5f17ab` |
| `libggml-cpu-cascadelake.so` | 1282080 | `4e2ee9f47758426548403f75c6031baa3fc1b6c3c5d209354d947b9cf35c8c20` |
| `libggml-cpu-cooperlake.so` | 1282144 | `c706d1d1ba8804deb457f0cde14fb1cffa3f7a8e465bac0169a2c957a3f3fb4f` |
| `libggml-cpu-haswell.so` | 1141184 | `f8620357aea4dce39ccc3326626573a71c783f5dd11e49f52addb21006adbc67` |
| `libggml-cpu-icelake.so` | 1282080 | `ef2ec9d39c701e5ab9062fe5aad49d55d0a4c63b1e0eb46fbbfb5d437b6b56b8` |
| `libggml-cpu-ivybridge.so` | 1094656 | `547c9295f247cb2ba4947af75a04a5279f40479af85eadc4876282a681c3c6fd` |
| `libggml-cpu-piledriver.so` | 1090560 | `4bdbbeca90cc5b2acb32284b09b6def78546a7d897b8fead87d38a39a52035b1` |
| `libggml-cpu-sandybridge.so` | 1081248 | `9ba32dcb20048f67dc5816646edd64799048bbe2c40deaf7c2cd46a726a99e04` |
| `libggml-cpu-sapphirerapids.so` | 1548480 | `6221b414b195d1d075eb575debb93e24daf26afec7352b136146e650595d3617` |
| `libggml-cpu-skylakex.so` | 1286176 | `211269ef5a067b400c19fb10472e4f4bcecd58b724760d9e4cfa968f4c9a8cdc` |
| `libggml-cpu-sse42.so` | 882048 | `94ee365a747ce6b81d81e32981f8c1ffa05942f39c245f3e33c05300208d7355` |
| `libggml-cpu-x64.so` | 878128 | `a31a3e374f01e90ef60dbc8b654be972029107ed5f0c670bb211ed6d6821d490` |
| `libggml-cpu-zen4.so` | 1282144 | `17dde3b34a68055c2c5f9c6d63a6ca6a9f1b470fdf8869113495af6eaad24f87` |
| `libggml-rpc.so` | 159304 | `aff4f89035be449fdc46d56a7e493e9eab4b7dbf09b35b170bf7d36be3709f55` |

The implementation and evidence workflows require an exact manifest match. A filename, resolved byte-count, SHA-256, directory, count, archive, runtime-manifest, or `libllama` mismatch fails closed before model load as an incomplete runtime-identity gate.

## 6. Review-first no-model backend registration qualification

The PR static workflow:

```text
.github/workflows/e004-backend-corrective-static-qualification-v1.yml
```

is limited to:

1. exact-head binding;
2. canonical Decision-B binding;
3. exact frozen runtime archive re-verification;
4. complete frozen runtime manifest re-verification;
5. exact backend manifest verification;
6. compilation and execution of `tools/e004_backend_registration_probe.cpp` against the verified frozen runtime;
7. assertion that at least one backend is registered;
8. focused static policy tests;
9. `git diff --check`;
10. unconditional runtime-byte cleanup.

The no-model probe contains no model-load call and the static workflow has no candidate/model acquisition path.

```text
PULL_REQUEST_CANDIDATE_OR_MODEL_BYTES=PROHIBITED
PULL_REQUEST_MODEL_LOAD=PROHIBITED
MODEL_BYTES_ACQUIRED=NO
MODEL_LOAD_PERFORMED=NO
```

The exact-head no-model registration result remains a merge qualification gate; it is not an empirical model-load result and may never be promoted to model compatibility PASS.

## 7. New successor evidence workflow

A new surface is used rather than mutating or rerunning the consumed corrective workflow:

```text
BACKEND_CORRECTIVE_EVIDENCE_WORKFLOW=.github/workflows/e004-model-load-backend-corrective-evidence-v1.yml
BACKEND_CORRECTIVE_EVIDENCE_BRANCH=evidence/e004-model-load-backend-corrective-run-v1
BACKEND_CORRECTIVE_EVIDENCE_MARKER=.github/e004-model-load-backend-corrective-run-v1.txt
MAX_AUTHORIZED_BACKEND_CORRECTIVE_MODEL_LOAD_COMPATIBILITY_WORKFLOW_RUNS=1
AUTHORIZED_BACKEND_CORRECTIVE_CANDIDATE_PROBES_PER_WORKFLOW=2_EXACTLY_ONE_PER_FROZEN_GGUF_CANDIDATE
AUTOMATIC_RERUN_AUTHORITY=NONE
FAILED_RUN_RETRY_AUTHORITY=NONE
SECOND_BACKEND_CORRECTIVE_WORKFLOW_RUN_AUTHORITY=NONE
```

The workflow has only a marker-path `push` trigger on the exact evidence branch. It has no pull-request or manual/repository dispatch trigger. The marker commit must be the direct child of the canonical implementation merge and must change only the marker file.

## 8. Exact frozen successor candidate subject

Exactly two candidates are present in the successor matrix:

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd | LLAMA_CPP_GGUF | PRIMARY
Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68 | LLAMA_CPP_GGUF | PRIMARY
```

Parent identities remain:

```text
CANDIDATE_ARTIFACT_BUNDLE_SET_ID=SP007_RO_001_CANDIDATE_ARTIFACT_BUNDLE_SET_V1
CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256=ee97fe0751743cc0d3a564b8f91add3c336267f08f2da86bf125dd7333db83fd
PROTOCOL_ID=SP007_RO_001_NONCLINICAL_BACKBONE_TOURNAMENT_V1
PROTOCOL_SHA256=1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8
```

The historical Transformers PASS candidates are absent and have no rerun authority.

## 9. Empirical disposition boundary

Before invoking the model-load operation, the successor workflow verifies the exact archive, runtime manifest, `libllama`, runtime directory, and complete dynamic-backend manifest.

```text
BACKEND_LIBRARY_IDENTITY_MISMATCH=INCOMPLETE_RUNTIME_IDENTITY_GATE
BACKEND_REGISTRATION_ZERO_OR_UNAVAILABLE=INCOMPLETE_BACKEND_REGISTRATION_NOT_READY
MODEL_LOAD_EXIT_0=PASS_EXACT_MODEL_LOAD_COMPLETED
MODEL_LOAD_EXIT_137_OR_143=INCOMPLETE_RESOURCE_LIMIT_OR_TERMINATION
MODEL_LOAD_EXIT_134_OR_139=FAIL_RUNTIME_CRASH_DURING_MODEL_LOAD
OTHER_NONZERO_MODEL_LOAD_EXIT=FAIL_MODEL_LOAD_ERROR
```

The helper emits `MODEL_LOAD_REACHED=YES` immediately before `llama_model_load_from_file`. The workflow does not classify a process failure as empirical model-load FAIL unless that marker proves model load was reached.

## 10. Network, retention, resource, credential, and finance boundary

```text
SOURCE_CLASS=PUBLIC_UNGATED_EXACT_CANONICAL_BUNDLE_FILES_AND_EXACT_FROZEN_LLAMA_RUNTIME_ONLY
NETWORK_DURING_BYTE_ACQUISITION=AUTHORIZED_ONLY_FOR_EXACT_PUBLIC_SOURCE_BYTES
NETWORK_DURING_MODEL_LOAD=PROHIBITED_ENFORCED_UNSHARE_N
USER_MANAGED_CREDENTIAL_USE=PROHIBITED
FOUNDER_PERSONAL_TOKEN_USE=PROHIBITED
REPOSITORY_SECRET_USE=PROHIBITED
GATED_ASSET_ACCESS=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
PHI_ACCESS=PROHIBITED
BENCHMARK_OR_EVALUATION_PAYLOAD_ACCESS=PROHIBITED
RAW_MODEL_BYTE_ARTIFACT_UPLOAD=PROHIBITED
ACTIONS_CACHE_FOR_MODEL_BYTES=PROHIBITED
MODEL_BYTE_PERSISTENCE_AFTER_JOB=PROHIBITED
RETAINED_EVIDENCE=GITHUB_ACTIONS_LOG_METADATA_ONLY
RUNNER_CLASS=STANDARD_PUBLIC_UBUNTU_24_04_ONLY
LARGER_OR_PAID_RUNNER=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 11. Pull-request exit requirements

Before canonical merge, live exact-head evidence must establish:

```text
EXACT_HEAD_STATIC_QUALIFICATION=PASS_REQUIRED
EXACT_FROZEN_RUNTIME_ARCHIVE_REVERIFICATION=PASS_REQUIRED
EXACT_RUNTIME_FILE_MANIFEST_REVERIFICATION=PASS_REQUIRED
EXACT_BACKEND_LIBRARY_DIRECTORY_BINDING=PASS_REQUIRED
EXACT_BACKEND_LIBRARY_FILE_IDENTITY_BINDING=PASS_REQUIRED
PATH_BOUND_BACKEND_DISCOVERY=PASS_REQUIRED
ZERO_REGISTERED_BACKENDS_FAIL_CLOSED=PASS_REQUIRED
NO_MODEL_STATIC_BACKEND_REGISTRATION_PROBE=PASS_REQUIRED
LOAD_ONLY_HELPER_POLICY=PASS_REQUIRED
EXACT_TWO_GGUF_MATRIX_BINDING=PASS_REQUIRED
TRANSFORMERS_RERUN_EXCLUSION=PASS_REQUIRED
SPEC007_REGRESSION=PASS_REQUIRED
FULL_REPOSITORY_REGRESSION=PASS_REQUIRED
DIFF_WHITESPACE=PASS_REQUIRED
EXPECTED_HEAD_GUARDED_MERGE=PASS_REQUIRED
POST_MERGE_CANONICAL_REVERIFICATION=PASS_REQUIRED
```

Automated or independent review is not represented as substantive evidence unless it actually occurs. Independent repository review remains optional under FD-007.

## 12. Non-expansion and non-closure

Even if the future single successor evidence run produces two GGUF PASS outcomes, this implementation does not itself establish or authorize:

```text
RETROACTIVE_TRANSFORMERS_CLEANUP_PASS=NOT_ESTABLISHED
ORCHESTRATOR_IMPLEMENTATION_STATE=NOT_ESTABLISHED
EXACT_FUTURE_MODEL_EXECUTION_ENVIRONMENT=NOT_ESTABLISHED
EXACT_COMPUTE_RESOURCE_IDENTITY=NOT_ESTABLISHED
RESOURCE_AUTHORIZATION_BASIS=NOT_ESTABLISHED
EXPECTED_CPU_RAM_DISK_ENVELOPE=NOT_ESTABLISHED
EXPECTED_MAX_WALLCLOCK=NOT_ESTABLISHED
EXACT_ACCESS_BINDING_FOR_EXECUTION_SUBJECT=NOT_ESTABLISHED
EXACT_CREDENTIAL_STATE_BINDING=NOT_ESTABLISHED
NETWORK_DURING_TOURNAMENT_EXECUTION_BINDING=NOT_ESTABLISHED
RETENTION_BINDING_FOR_TOURNAMENT=NOT_ESTABLISHED
ZERO_INCREMENTAL_SPEND_TOURNAMENT_RESOURCE_BINDING=NOT_ESTABLISHED
A1_A14_APPLICABLE_PASS_SNAPSHOT=NOT_ESTABLISHED
A15_ACTIVATION=NOT_ESTABLISHED
TOURNAMENT_EXECUTION_AUTHORIZED_NOW=NO
WINNER_SELECTION_AUTHORIZED_NOW=NO
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
PROJECT_FINISHED=NO
```

No forward pass, inference, generation, benchmark/evaluation payload execution, tournament execution, winner selection, A15 activation, training-readiness, or project-completion claim may be inferred from this implementation or from a future load-only compatibility result.
