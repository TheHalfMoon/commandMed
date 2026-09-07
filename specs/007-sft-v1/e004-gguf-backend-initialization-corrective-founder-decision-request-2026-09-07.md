# E004 GGUF Backend-Initialization Corrective Founder Decision Request — 2026-09-07

**Spec:** 007 SFT V1
**Task:** E004
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Canonical empirical reconciliation:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v43-2026-09-07.md`
**Canonical empirical reconciliation merge:** `7e490d0c174e7c96854ee196a9e2ca401da5d2d9`
**Canonical empirical reconciliation tree:** `48b31bde037a81c82986ea82676b72dba1c5e08b`
**Prior corrective Founder decision:** `FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION=E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION_B_CONSUMED`
**Prior corrective evidence run:** `34150708258`, attempt `1`, consumed
**Artifact class:** Founder decision request only
**Authority effect of this request before an exact post-canonical Founder token:** NONE
**Current authorized spend:** USD 0

## 1. Decision question

The first corrective E004 GGUF model-load compatibility workflow run is consumed. It successfully removed the previously observed missing-header/helper-build prerequisite failure, reached the actual network-disabled llama.cpp model-load call for both frozen GGUF candidates, and produced the same empirical load error for both candidates:

```text
llama_model_load_from_file_impl: no backends are loaded. hint: use ggml_backend_load() or ggml_backend_load_all() to load a backend before calling this function
```

Both frozen GGUF candidates therefore have canonical empirical disposition:

```text
EMPIRICAL_MODEL_LOAD_COMPATIBILITY=FAIL
EMPIRICAL_MODEL_LOAD_REASON_CODE=FAIL_MODEL_LOAD_ERROR
MODEL_LOAD_EXIT_CODE=2
```

No rerun, retry, or second workflow run remains authorized by the consumed prior corrective decision.

Repository-only diagnosis now identifies a bounded backend-discovery/initialization defect that can be repaired without changing candidate identities, model bytes, candidate bundles, llama.cpp source revision, frozen runtime archive, runtime route, runner class, or the load-only scientific question. That diagnosis is not empirical PASS and creates no execution authority.

The Founder must now choose whether to preserve the current `PARTIAL_2_PASS_2_FAIL` state or authorize exactly one new post-merge, zero-spend, load-only backend-initialization corrective evidence workflow run limited to the same two frozen GGUF candidates.

## 2. Current canonical empirical state

```text
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v43-2026-09-07.md
ORIGINAL_EVIDENCE_WORKFLOW_RUN_ID=34063020745
ORIGINAL_EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
ORIGINAL_MODEL_LOAD_COMPATIBILITY_EVIDENCE_RUN=CONSUMED_SINGLE_RUN_NO_RERUN_AUTHORITY
FIRST_CORRECTIVE_EVIDENCE_WORKFLOW_RUN_ID=34150708258
FIRST_CORRECTIVE_EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
FIRST_CORRECTIVE_EVIDENCE_WORKFLOW_RUN_CONCLUSION=failure
FIRST_CORRECTIVE_MODEL_LOAD_COMPATIBILITY_EVIDENCE_RUN=CONSUMED_SINGLE_RUN_WITH_2_GGUF_EMPIRICAL_FAIL
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=PARTIAL_2_PASS_2_FAIL
RUNTIME_FORMAT_COMPATIBILITY_STATE_FOR_LIVE_SUBJECT=NOT_PASS_ALL_FOUR
FOUR_CANDIDATE_MODEL_LOAD_COMPATIBILITY_GATE=FAIL_NOT_PASS
```

The two already-PASS Transformers candidates retain only their original consumed-run evidence and must not be rerun.

## 3. Exact frozen corrective subject

Any future backend-initialization corrective run under Decision B is limited to exactly:

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd | LLAMA_CPP_GGUF | PRIMARY
Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68 | LLAMA_CPP_GGUF | PRIMARY
```

Frozen candidate artifact identities remain:

```text
QWEN3_0_6B_MODEL_ARTIFACT_SHA256=218d3f063193b40008d4e63d90cf83e7dc6d33a8c6c1c647589f868a8fc74492
QWEN3_0_6B_MODEL_ARTIFACT_BYTES=396704512
QWEN3_0_6B_CANDIDATE_BUNDLE_SHA256=8b207e94ad7c5937dceced686603294ae5f150022ac2b355fee9997a408fc415
QWEN3_0_6B_TOKENIZER_CONFIG_SHA256=3c04ed3ca964ea2f6b2b5faf0dc4d31aec1cb1e8b4bcf63f402d295046b422b5
QWEN3_5_0_8B_MODEL_ARTIFACT_SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
QWEN3_5_0_8B_MODEL_ARTIFACT_BYTES=563035840
QWEN3_5_0_8B_CANDIDATE_BUNDLE_SHA256=682ef5c8fb914feb5346d5153e26b83e6bb3bb834aa1313cba240b61c0657592
QWEN3_5_0_8B_TOKENIZER_CONFIG_SHA256=e611fbccc7c29ef3b1cafb1cb7ea548d189968632901d678fd62be68c47885de
```

Parent identities remain frozen:

```text
CANDIDATE_ARTIFACT_BUNDLE_SET_ID=SP007_RO_001_CANDIDATE_ARTIFACT_BUNDLE_SET_V1
CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256=ee97fe0751743cc0d3a564b8f91add3c336267f08f2da86bf125dd7333db83fd
PROTOCOL_ID=SP007_RO_001_NONCLINICAL_BACKBONE_TOURNAMENT_V1
PROTOCOL_SHA256=1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8
```

No candidate, revision, role, artifact, bundle, protocol, or runtime route substitution is permitted.

## 4. Frozen llama.cpp runtime identity

Any implementation under Decision B must preserve exactly:

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

The upstream `b10621` release binds the Ubuntu x64 CPU asset to the same frozen source revision and exact archive SHA-256 above.

## 5. Repository-only backend diagnosis

No model was loaded and no model bytes were acquired for this diagnosis.

At the exact frozen llama.cpp source revision, `ggml/include/ggml-backend.h` declares:

```text
GGML_API ggml_backend_reg_t ggml_backend_load(const char * path);
GGML_API void ggml_backend_load_all(void);
GGML_API void ggml_backend_load_all_from_path(const char * dir_path);
```

At the same exact revision, `ggml/src/ggml-backend-reg.cpp` establishes:

```text
ggml_backend_load_all() -> ggml_backend_load_all_from_path(nullptr)
```

When no explicit path is supplied, the dynamic-backend loader searches the executable directory and current working directory, plus any compiled `GGML_BACKEND_DIR`. When an explicit `dir_path` is supplied, that directory is the dynamic-backend search path. The loader attempts the CPU backend among its known dynamic backends.

At the same exact revision, upstream `examples/simple/simple.cpp` calls:

```text
ggml_backend_load_all();
llama_model_load_from_file(...);
```

The exact `b10621` Ubuntu CPU release workflow builds with:

```text
GGML_BACKEND_DL=ON
GGML_NATIVE=OFF
GGML_CPU_ALL_VARIANTS=ON
CMAKE_INSTALL_RPATH=$ORIGIN
```

and packages the complete `build/bin` directory into the frozen Ubuntu x64 CPU archive.

The first corrective commandMed workflow, however, compiled its reviewed helper at a separate root path while retaining the frozen runtime libraries under the extracted runtime directory. Its linker `rpath`/`rpath-link` bound normal shared-library resolution to the frozen `libllama` directory, but the helper did not call a dynamic-backend discovery API before `llama_model_load_from_file`. The empirical runtime therefore reported that no backend had been loaded.

The minimum bounded corrective mechanism is consequently an explicit dynamic-backend discovery/initialization step, bound to the exact already-verified frozen runtime-library directory, before the existing model-load call. Static diagnosis does not establish that a future model-load call will PASS.

```text
BACKEND_INITIALIZATION_DIAGNOSIS=STATIC_HIGH_CONFIDENCE_NOT_EMPIRICAL_PASS
OBSERVED_RUNTIME_ERROR=NO_BACKENDS_LOADED
FROZEN_RUNTIME_DYNAMIC_BACKEND_BUILD=YES
MODEL_LOAD_RETRY_AUTHORITY_FROM_DIAGNOSIS=NONE
```

## 6. Founder decision classes

### `E004_GGUF_BACKEND_INITIALIZATION_CORRECTIVE_DECISION_A` — preserve current empirical failure state

Exact operative token:

```text
FOUNDER_E004_GGUF_BACKEND_INITIALIZATION_CORRECTIVE_DECISION=E004_GGUF_BACKEND_INITIALIZATION_CORRECTIVE_DECISION_A
```

Effect only after this request is canonical and the exact token is separately captured canonically:

```text
GGUF_BACKEND_INITIALIZATION_CORRECTIVE_IMPLEMENTATION_AUTHORITY=NONE
GGUF_BACKEND_INITIALIZATION_CORRECTIVE_MODEL_WEIGHT_ACQUISITION_AUTHORITY=NONE
GGUF_BACKEND_INITIALIZATION_CORRECTIVE_MODEL_LOAD_AUTHORITY=NONE
GGUF_BACKEND_INITIALIZATION_CORRECTIVE_EVIDENCE_WORKFLOW_RUN_AUTHORITY=NONE
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=PARTIAL_2_PASS_2_FAIL
FOUR_CANDIDATE_MODEL_LOAD_COMPATIBILITY_GATE=FAIL_NOT_PASS
```

### `E004_GGUF_BACKEND_INITIALIZATION_CORRECTIVE_DECISION_B` — authorize one exact backend-initialization corrective load-only run

Exact operative token:

```text
FOUNDER_E004_GGUF_BACKEND_INITIALIZATION_CORRECTIVE_DECISION=E004_GGUF_BACKEND_INITIALIZATION_CORRECTIVE_DECISION_B
```

Effect only after this request is canonical and the exact token is separately captured canonically:

```text
GGUF_BACKEND_INITIALIZATION_CORRECTIVE_IMPLEMENTATION_AUTHORITY=AUTHORIZED_REVIEW_FIRST_STATIC_ONLY
GGUF_BACKEND_INITIALIZATION_CORRECTIVE_MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=AUTHORIZED_EXACT_TWO_GGUF_LOAD_ONLY
GGUF_BACKEND_INITIALIZATION_CORRECTIVE_MODEL_WEIGHT_ACQUISITION_AUTHORITY=AUTHORIZED_EXACT_TWO_PUBLIC_UNGATED_CANONICAL_GGUF_BUNDLES_ONLY
GGUF_BACKEND_INITIALIZATION_CORRECTIVE_MODEL_LOAD_AUTHORITY=AUTHORIZED_EXACT_TWO_GGUF_LOAD_ONLY
GGUF_BACKEND_INITIALIZATION_CORRECTIVE_EVIDENCE_WORKFLOW_RUN_AUTHORITY=AUTHORIZED_SINGLE_NEW_POST_MERGE_RUN
TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE
MODEL_FORWARD_PASS_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
GENERATION_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
EVALUATION_PAYLOAD_EXECUTION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY=NONE
WINNER_SELECTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

This is a new, separately bounded Founder decision. It does not revive, modify, rerun, or extend either consumed workflow run `34063020745` or `34150708258`.

## 7. Exact implementation boundary under Decision B

Decision B authorizes implementation preparation only after the exact token is captured in a separate canonical Founder decision record.

The implementation may only:

1. preserve the exact two frozen GGUF candidate identities and frozen candidate bundles;
2. preserve the exact frozen llama.cpp source/runtime/archive/library identities;
3. preserve the existing load-only scientific question;
4. add the minimum explicit dynamic-backend discovery/initialization binding required by the exact frozen runtime before `llama_model_load_from_file`;
5. bind backend discovery to the exact verified runtime library directory rather than broad or mutable system search paths;
6. prove statically that at least one backend registration must exist before the helper proceeds to the model-load call, while failing closed if backend discovery does not establish that condition;
7. preserve network-disabled model loading;
8. preserve exact candidate-byte and runtime-byte integrity gates;
9. preserve unconditional cleanup and zero-retention behavior;
10. add or strengthen static policy tests for all of the above;
11. create a dedicated post-merge-only evidence workflow mechanically limited to the exact two frozen GGUF candidates;
12. execute exactly one new evidence workflow run only after exact-head qualification, expected-head guarded merge, and post-merge canonical reverification.

Permitted backend APIs are limited to the exact frozen-revision dynamic-backend registration surface necessary to make a CPU backend available before model loading, such as `ggml_backend_load_all_from_path` or a more narrowly bound exact-path `ggml_backend_load` implementation if static review proves that it is strictly narrower and uses only the already-verified frozen runtime bytes.

The implementation must not create a context or invoke any compute/evaluation primitive.

## 8. Prohibited implementation and execution expansion

```text
CANDIDATE_CHANGE=PROHIBITED
CANDIDATE_REVISION_CHANGE=PROHIBITED
MODEL_ARTIFACT_IDENTITY_CHANGE=PROHIBITED
CANDIDATE_BUNDLE_CHANGE=PROHIBITED
PROTOCOL_CHANGE=PROHIBITED
RUNTIME_REVISION_CHANGE=PROHIBITED
RUNTIME_ARCHIVE_CHANGE=PROHIBITED
RUNTIME_LIBRARY_IDENTITY_CHANGE=PROHIBITED
RUNTIME_ROUTE_CHANGE=PROHIBITED
SYSTEM_BACKEND_FALLBACK=PROHIBITED
MUTABLE_SYSTEM_LIBRARY_DISCOVERY=PROHIBITED
TRANSFORMERS_CANDIDATE_RERUN=PROHIBITED
PULL_REQUEST_MODEL_LOAD=PROHIBITED
MANUAL_WORKFLOW_DISPATCH_MODEL_LOAD=PROHIBITED
PAID_OR_LARGER_RUNNER_USE=PROHIBITED
RESOURCE_ESCALATION=PROHIBITED
USER_MANAGED_CREDENTIAL_USE=PROHIBITED
FOUNDER_PERSONAL_TOKEN_USE=PROHIBITED
REPOSITORY_SECRET_USE=PROHIBITED
GATED_ASSET_ACCESS=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
PHI_ACCESS=PROHIBITED
BENCHMARK_OR_EVALUATION_PAYLOAD_ACCESS=PROHIBITED
MODEL_FORWARD_PASS=PROHIBITED
MODEL_INFERENCE=PROHIBITED
GENERATION=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
EVALUATION_PAYLOAD_EXECUTION=PROHIBITED
TOURNAMENT_EXECUTION=PROHIBITED
WINNER_SELECTION=PROHIBITED
A15_ACTIVATION=PROHIBITED
TRAINING=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
SPEND=PROHIBITED
```

## 9. One-new-run boundary under Decision B

If Decision B is selected and canonically captured:

```text
MAX_AUTHORIZED_GGUF_BACKEND_INITIALIZATION_CORRECTIVE_WORKFLOW_RUNS=1
AUTHORIZED_GGUF_BACKEND_INITIALIZATION_CORRECTIVE_CANDIDATE_PROBES_PER_WORKFLOW=2_EXACTLY_ONE_PER_FROZEN_GGUF_CANDIDATE
AUTOMATIC_RERUN_AUTHORITY=NONE
FAILED_RUN_RETRY_AUTHORITY=NONE
SECOND_GGUF_BACKEND_INITIALIZATION_CORRECTIVE_WORKFLOW_RUN_AUTHORITY=NONE
RESOURCE_ESCALATION_AUTHORITY=NONE
RUNTIME_SUBSTITUTION_AUTHORITY=NONE
CANDIDATE_SUBSTITUTION_AUTHORITY=NONE
TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE
```

The two prior workflow runs remain consumed and immutable:

```text
ORIGINAL_EVIDENCE_WORKFLOW_RUN_ID=34063020745
ORIGINAL_EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
FIRST_CORRECTIVE_EVIDENCE_WORKFLOW_RUN_ID=34150708258
FIRST_CORRECTIVE_EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
PRIOR_WORKFLOW_RERUN_AUTHORITY=NONE
PRIOR_WORKFLOW_RETRY_AUTHORITY=NONE
```

Ordinary byte-transport retries remain restricted to the same exact public source URL/revision/path before the canonical SHA-256 gate and are not workflow reruns.

## 10. Acquisition, network, credential, retention, resource, and finance boundary

```text
SOURCE_CLASS=PUBLIC_UNGATED_EXACT_CANONICAL_BUNDLE_FILES_ONLY
NETWORK_DURING_BYTE_ACQUISITION=AUTHORIZED_ONLY_FOR_EXACT_PUBLIC_SOURCE_BYTES
NETWORK_DURING_FROZEN_RUNTIME_ACQUISITION=AUTHORIZED_ONLY_FOR_EXACT_FROZEN_RUNTIME_BYTES
NETWORK_DURING_MODEL_LOAD=PROHIBITED
USER_MANAGED_CREDENTIAL_USE=PROHIBITED
FOUNDER_PERSONAL_TOKEN_USE=PROHIBITED
REPOSITORY_SECRET_USE=PROHIBITED
GATED_ASSET_ACCESS=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
PHI_ACCESS=PROHIBITED
BENCHMARK_OR_EVALUATION_PAYLOAD_ACCESS=PROHIBITED
RAW_MODEL_BYTE_ARTIFACT_UPLOAD=PROHIBITED
RAW_RUNTIME_BYTE_ARTIFACT_UPLOAD=PROHIBITED
ACTIONS_CACHE_FOR_MODEL_OR_RUNTIME_BYTES=PROHIBITED
MODEL_BYTE_PERSISTENCE_AFTER_JOB=PROHIBITED
RUNTIME_BYTE_PERSISTENCE_AFTER_JOB=PROHIBITED
RETAINED_EVIDENCE=GITHUB_ACTIONS_LOG_METADATA_ONLY
RUNNER_CLASS=STANDARD_PUBLIC_UBUNTU_24_04_ONLY
LARGER_OR_PAID_RUNNER=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 11. Empirical disposition boundary

A future exact GGUF candidate may receive model-load compatibility PASS only if:

1. all exact candidate artifact, bundle, runtime archive, runtime file-manifest, and library identity gates pass;
2. backend discovery is bound only to the exact verified frozen runtime library directory;
3. at least one backend is registered before model loading;
4. network is disabled for the load process;
5. `llama_model_load_from_file` completes successfully;
6. no context, decode, encode, sampler, forward pass, inference, generation, benchmark/evaluation payload, tournament, winner selection, A15 activation, or training operation occurs;
7. cleanup succeeds and no model/runtime bytes are retained or uploaded.

A failure before `llama_model_load_from_file` is reached remains `INCOMPLETE_MODEL_LOAD_NOT_REACHED` with a frozen prerequisite reason code. A nonzero return/crash after the model-load function is reached remains empirical FAIL under a frozen load-error reason code. Static diagnosis may never be promoted to empirical PASS.

## 12. Review-first and post-merge boundary

Before any new evidence trigger exists, a future corrective implementation PR must genuinely satisfy:

```text
PULL_REQUEST_MODEL_LOAD=PROHIBITED
REVIEW_FIRST_WORKFLOW_PREPARATION=REQUIRED
EXACT_HEAD_STATIC_QUALIFICATION=REQUIRED
NEW_CORRECTIVE_AUTHORITY_TOKEN_BINDING=REQUIRED
EXACT_TWO_GGUF_MATRIX_BINDING=REQUIRED
TRANSFORMERS_RERUN_EXCLUSION=REQUIRED
FROZEN_RUNTIME_IDENTITY_BINDING=REQUIRED
EXACT_RUNTIME_BACKEND_DIRECTORY_BINDING=REQUIRED
LOAD_ONLY_HELPER_POLICY=REQUIRED
NO_CONTEXT_OR_COMPUTE_API_POLICY=REQUIRED
ZERO_RETENTION_POLICY=REQUIRED
ZERO_SPEND_POLICY=REQUIRED
DIFF_WHITESPACE=PASS_REQUIRED
EXPECTED_HEAD_GUARDED_MERGE=REQUIRED
POST_MERGE_CANONICAL_REVERIFICATION=REQUIRED
```

Independent repository review remains optional by default under FD-007 unless later bounded authority explicitly requires it for this named task. A skipped or unavailable automated review must not be represented as substantive independent review evidence.

## 13. Non-expansion statement

Even if a future separately authorized backend-initialization corrective run produced PASS for both GGUF candidates, it would establish only the exact load-only model/runtime compatibility result for those candidates. It would not establish or activate:

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
```

## 14. Exact post-canonical selection requirement

This request creates no implementation, model-acquisition, model-load, or evidence-run authority by itself.

The previously supplied and consumed token:

```text
FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION=E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION_B
```

cannot be reused, reinterpreted, or expanded into this new decision.

Any broad continuation statement, ordinary authorization, generic permission, or `go ahead` supplied before this new decision surface becomes canonical is context only and cannot substitute for either exact new decision token.

After this request is canonically merged, the Founder must supply exactly one of:

```text
FOUNDER_E004_GGUF_BACKEND_INITIALIZATION_CORRECTIVE_DECISION=E004_GGUF_BACKEND_INITIALIZATION_CORRECTIVE_DECISION_A
```

or

```text
FOUNDER_E004_GGUF_BACKEND_INITIALIZATION_CORRECTIVE_DECISION=E004_GGUF_BACKEND_INITIALIZATION_CORRECTIVE_DECISION_B
```

The selected token must then be captured in a separate canonical Founder decision record before any implementation is treated as execution-authorized.

## 15. Current disposition before selection

```text
GGUF_BACKEND_INITIALIZATION_CORRECTIVE_DECISION_SURFACE=NOT_YET_CANONICAL
POST_CANONICAL_EXACT_GGUF_BACKEND_INITIALIZATION_FOUNDER_DECISION_TOKEN=ABSENT
FOUNDER_E004_GGUF_BACKEND_INITIALIZATION_CORRECTIVE_DECISION=ABSENT
GGUF_BACKEND_INITIALIZATION_CORRECTIVE_IMPLEMENTATION_AUTHORITY=NONE
GGUF_BACKEND_INITIALIZATION_CORRECTIVE_MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=NONE
GGUF_BACKEND_INITIALIZATION_CORRECTIVE_MODEL_WEIGHT_ACQUISITION_AUTHORITY=NONE
GGUF_BACKEND_INITIALIZATION_CORRECTIVE_MODEL_LOAD_AUTHORITY=NONE
GGUF_BACKEND_INITIALIZATION_CORRECTIVE_EVIDENCE_WORKFLOW_RUN_AUTHORITY=NONE
TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE
MODEL_FORWARD_PASS_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
GENERATION_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
EVALUATION_PAYLOAD_EXECUTION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY=NONE
WINNER_SELECTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```
