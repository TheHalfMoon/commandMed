# E004 Model-Load Compatibility Corrective Founder Decision Request — 2026-09-07

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Canonical evidence reconciliation:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v41-2026-09-07.md`
**Canonical evidence reconciliation merge:** `2737cdb605e95f4e4322a9661e82cb19fd18e8f0`
**Artifact class:** Founder decision request only
**Authority effect of this request before an exact post-canonical Founder token:** NONE
**Current authorized spend:** USD 0

## 1. Decision question

The single Decision-B model-load compatibility evidence run has been consumed. It produced empirical load-only PASS evidence for both frozen Transformers candidates, while both frozen GGUF candidates did not reach model load because their llama.cpp runtime/helper-build prerequisite step failed.

No rerun or second run remains authorized by the consumed Decision B.

The Founder must now choose whether to preserve the current incomplete state or authorize exactly one corrective, zero-spend, post-merge evidence run limited to the two frozen GGUF candidates that never reached model load.

## 2. Current canonical evidence state

```text
PR280_IMPLEMENTATION_MERGE=a1455770c0bdfdf935b9150c508df8306c385096
EVIDENCE_TRIGGER_HEAD=cc0e63058f701430137f213aa22c59a1fb987e8d
EVIDENCE_WORKFLOW_RUN_ID=34063020745
EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
EVIDENCE_WORKFLOW_OVERALL_CONCLUSION=failure
MODEL_LOAD_COMPATIBILITY_EVIDENCE_RUN=CONSUMED_SINGLE_RUN_NO_RERUN_AUTHORITY
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=PARTIAL_2_PASS_2_INCOMPLETE
RUNTIME_FORMAT_COMPATIBILITY_STATE_FOR_LIVE_SUBJECT=NOT_PASS_ALL_FOUR
```

Observed candidate state:

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd=INCOMPLETE_MODEL_LOAD_NOT_REACHED
Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68=INCOMPLETE_MODEL_LOAD_NOT_REACHED
ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b=PASS_EXACT_MODEL_LOAD_COMPLETED
Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539=PASS_EXACT_MODEL_LOAD_COMPLETED_CONTROL_WINNER_INELIGIBLE
```

The two successful Transformers jobs subsequently had cleanup-step failures. That cleanup truth is preserved by V41 and is not retroactively converted to PASS by either decision below.

## 3. Frozen corrective subject

A corrective run under Decision B, if selected after this request is canonical and captured by a separate canonical decision record, is limited to exactly these two already-frozen GGUF candidates:

### 3.1 Qwen/Qwen3-0.6B-Base

```text
CANDIDATE_ID=Qwen/Qwen3-0.6B-Base
CANDIDATE_REVISION=da87bfb608c14b7cf20ba1ce41287e8de496c0cd
ROLE=PRIMARY
RUNTIME_ROUTE=LLAMA_CPP_GGUF
MODEL_ARTIFACT_SHA256=218d3f063193b40008d4e63d90cf83e7dc6d33a8c6c1c647589f868a8fc74492
MODEL_ARTIFACT_BYTES=396704512
CANDIDATE_BUNDLE_SHA256=8b207e94ad7c5937dceced686603294ae5f150022ac2b355fee9997a408fc415
TOKENIZER_CONFIG_SHA256=3c04ed3ca964ea2f6b2b5faf0dc4d31aec1cb1e8b4bcf63f402d295046b422b5
```

### 3.2 Qwen/Qwen3.5-0.8B-Base

```text
CANDIDATE_ID=Qwen/Qwen3.5-0.8B-Base
CANDIDATE_REVISION=dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
ROLE=PRIMARY
RUNTIME_ROUTE=LLAMA_CPP_GGUF
MODEL_ARTIFACT_SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
MODEL_ARTIFACT_BYTES=563035840
CANDIDATE_BUNDLE_SHA256=682ef5c8fb914feb5346d5153e26b83e6bb3bb834aa1313cba240b61c0657592
TOKENIZER_CONFIG_SHA256=e611fbccc7c29ef3b1cafb1cb7ea548d189968632901d678fd62be68c47885de
```

Parent identities remain frozen:

```text
CANDIDATE_ARTIFACT_BUNDLE_SET_ID=SP007_RO_001_CANDIDATE_ARTIFACT_BUNDLE_SET_V1
CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256=ee97fe0751743cc0d3a564b8f91add3c336267f08f2da86bf125dd7333db83fd
PROTOCOL_ID=SP007_RO_001_NONCLINICAL_BACKBONE_TOURNAMENT_V1
PROTOCOL_SHA256=1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8
```

No other candidate may execute in a corrective run.

## 4. Frozen llama.cpp runtime identity

The corrective implementation may repair only the preparation/staging required to use the same frozen runtime identity. It may not substitute a different llama.cpp revision, runtime archive, library identity, candidate format, or runtime route.

```text
LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
LLAMA_CPP_TAG=b10621
LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
LLAMA_RUNTIME_FILE_MANIFEST_SHA256=4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711
LIBLLAMA_SHA256=89869a6732162d45aa7fe5ab4b224e484c8f27f58c145e530e99dc59d8772448
LLAMA_BUILD_TOOLCHAIN_IDENTITY=GNU_11.4.0_LINUX_X86_64
```

The reviewed load-only helper semantics remain restricted to model construction/loading and free/backend teardown. No context creation, decode, encode, sampler, prompt, token generation, perplexity, benchmark, evaluation, or training operation may be introduced.

## 5. Founder decision classes

### `E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION_A` — preserve no-retry state

Exact operative token:

```text
FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION=E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION_A
```

Effect after canonical capture:

```text
CORRECTIVE_MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=NONE
CORRECTIVE_MODEL_WEIGHT_ACQUISITION_AUTHORITY=NONE
CORRECTIVE_MODEL_LOAD_AUTHORITY=NONE
SECOND_COMPATIBILITY_WORKFLOW_RUN_AUTHORITY=NONE
```

The two GGUF candidates remain empirically incomplete and the four-candidate compatibility gate remains not PASS.

### `E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION_B` — authorize one exact two-GGUF corrective run

Exact operative token:

```text
FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION=E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION_B
```

Effect only after this request is canonical and the exact token is separately captured canonically:

```text
CORRECTIVE_MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=AUTHORIZED_EXACT_TWO_GGUF_LOAD_ONLY
CORRECTIVE_MODEL_WEIGHT_ACQUISITION_AUTHORITY=AUTHORIZED_EXACT_TWO_PUBLIC_UNGATED_CANONICAL_GGUF_BUNDLES_ONLY
CORRECTIVE_MODEL_LOAD_AUTHORITY=AUTHORIZED_EXACT_TWO_GGUF_LOAD_ONLY
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

## 6. Corrective implementation boundary under Decision B

Decision B authorizes preparation of a review-first corrective implementation only after the exact decision token is canonically captured.

The implementation may:

1. diagnose the failed GGUF prerequisite path using repository-safe evidence;
2. repair only the header/source/runtime staging or build wiring required for the reviewed load-only helper to compile against the exact frozen llama.cpp runtime identity;
3. harden cleanup behavior for the corrective GGUF jobs;
4. add or strengthen static policy tests for the exact corrective workflow;
5. create a dedicated post-merge-only corrective workflow limited mechanically to the two frozen GGUF candidates;
6. perform exactly one corrective evidence workflow run after exact-head qualification, guarded merge, and post-merge canonical reverification.

The following remain prohibited:

```text
CANDIDATE_REVISION_CHANGE=PROHIBITED
MODEL_ARTIFACT_IDENTITY_CHANGE=PROHIBITED
RUNTIME_REVISION_CHANGE=PROHIBITED
RUNTIME_ROUTE_CHANGE=PROHIBITED
TRANSFORMERS_CANDIDATE_RERUN=PROHIBITED
PULL_REQUEST_MODEL_LOAD=PROHIBITED
MANUAL_WORKFLOW_DISPATCH_MODEL_LOAD=PROHIBITED
PAID_OR_LARGER_RUNNER_USE=PROHIBITED
USER_OR_REPOSITORY_CREDENTIAL_USE=PROHIBITED
GATED_ASSET_ACCESS=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
PHI_ACCESS=PROHIBITED
MODEL_FORWARD_PASS=PROHIBITED
MODEL_INFERENCE=PROHIBITED
GENERATION=PROHIBITED
BENCHMARK_OR_EVALUATION_PAYLOAD_EXECUTION=PROHIBITED
TOURNAMENT_EXECUTION=PROHIBITED
WINNER_SELECTION=PROHIBITED
A15_ACTIVATION=PROHIBITED
TRAINING=PROHIBITED
```

## 7. Corrective one-run boundary

If Decision B is selected and captured:

```text
MAX_AUTHORIZED_CORRECTIVE_MODEL_LOAD_COMPATIBILITY_WORKFLOW_RUNS=1
AUTHORIZED_CORRECTIVE_CANDIDATE_PROBES_PER_WORKFLOW=2_EXACTLY_ONE_PER_FROZEN_GGUF_CANDIDATE
AUTOMATIC_RERUN_AUTHORITY=NONE
FAILED_RUN_RETRY_AUTHORITY=NONE
RESOURCE_ESCALATION_AUTHORITY=NONE
RUNTIME_SUBSTITUTION_AUTHORITY=NONE
CANDIDATE_SUBSTITUTION_AUTHORITY=NONE
TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE
```

Ordinary byte-transport retries remain restricted to the same exact public source URL/revision/path before the canonical SHA-256 gate. They are not workflow reruns and do not permit source substitution.

## 8. Acquisition, network, credentials, retention, resource, and finance boundary

```text
SOURCE_CLASS=PUBLIC_UNGATED_EXACT_CANONICAL_BUNDLE_FILES_ONLY
NETWORK_DURING_BYTE_ACQUISITION=AUTHORIZED_ONLY_FOR_EXACT_PUBLIC_SOURCE_BYTES
NETWORK_DURING_MODEL_LOAD=PROHIBITED
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

If either exact GGUF candidate cannot complete model loading within this exact resource/runtime envelope, the corrective run must fail closed. No resource escalation or third run is implied.

## 9. Empirical disposition boundary

The corrective implementation must freeze exact reason codes before execution. A GGUF candidate may receive empirical PASS only when all exact artifact/runtime/integrity gates pass and the network-disabled load-only model process completes successfully without context execution, forward pass, inference, generation, benchmark/evaluation payload, tournament, or training.

A prerequisite/helper-build failure before model load remains `INCOMPLETE_MODEL_LOAD_NOT_REACHED`; it must not be mislabeled as empirical model-load FAIL.

Static compatibility reasoning may never be promoted to empirical PASS.

## 10. Review-first and post-merge boundary

Before a corrective evidence trigger exists, the corrective implementation PR must genuinely satisfy:

```text
PULL_REQUEST_MODEL_LOAD=PROHIBITED
REVIEW_FIRST_WORKFLOW_PREPARATION=REQUIRED
EXACT_HEAD_STATIC_QUALIFICATION=REQUIRED
CORRECTIVE_AUTHORITY_TOKEN_BINDING=REQUIRED
DIFF_WHITESPACE=PASS_REQUIRED
EXPECTED_HEAD_GUARDED_MERGE=REQUIRED
POST_MERGE_CANONICAL_REVERIFICATION=REQUIRED
```

Independent repository review remains optional by default under FD-007. A skipped automated review status may not be represented as substantive independent review evidence.

## 11. Non-expansion statement

Even if both corrective GGUF probes later PASS, this decision does not establish or activate:

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
TRAINING_AUTHORITY=NONE
```

## 12. Exact post-canonical selection requirement

This request creates no corrective execution authority by itself.

Any broad continuation statement, generic approval, ordinary authorization, or `go ahead` supplied before this decision surface becomes canonical is context only and cannot substitute for either exact decision token.

After this request is canonically merged, the Founder must supply exactly one of:

```text
FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION=E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION_A
```

or

```text
FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION=E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION_B
```

The selected token must be captured in a separate canonical Founder decision record before any corrective implementation is treated as execution-authorized.

## 13. Current disposition before selection

```text
CORRECTIVE_MODEL_LOAD_DECISION_SURFACE=NOT_YET_CANONICAL
POST_CANONICAL_EXACT_CORRECTIVE_FOUNDER_DECISION_TOKEN=ABSENT
FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION=ABSENT
CORRECTIVE_MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=NONE
CORRECTIVE_MODEL_WEIGHT_ACQUISITION_AUTHORITY=NONE
CORRECTIVE_MODEL_LOAD_AUTHORITY=NONE
TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE
MODEL_FORWARD_PASS_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
GENERATION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY=NONE
WINNER_SELECTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```
