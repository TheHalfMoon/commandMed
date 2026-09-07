# E004 Model-Load Compatibility Corrective Founder Decision — 2026-09-07

**Spec:** 007 SFT V1
**Task:** E004
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Canonical corrective decision request:** `specs/007-sft-v1/e004-model-load-compatibility-corrective-founder-decision-request-2026-09-07.md`
**Corrective decision-request PR:** #282
**Corrective decision-request canonical merge:** `7a3689a9c831396720c1771977466f3be030a2f3`
**Predecessor frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v42-2026-09-07.md`
**Canonical predecessor main:** `531435907e9dd45163933a99ade1bc6b6194220a`
**Canonical predecessor tree:** `6435dabc6bad3a15a0fa61d73515c3e77b86285d`
**Artifact class:** Founder decision capture
**Decision owner:** Founder
**Decision state before canonical merge:** CAPTURED_PENDING_CANONICAL_MERGE
**Current authorized spend:** USD 0

## 1. Exact post-canonical Founder token

After PR #282 and V42 made the corrective decision surface canonical, the Founder supplied exactly:

```text
FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION=E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION_B
```

Exact token SHA-256:

```text
FOUNDER_CORRECTIVE_DECISION_TOKEN_SHA256=2088779db1ee35f0f09a45bf1966484d22880c0df8715b32266ef997f7942434
```

This is the operative post-canonical corrective Decision B token required by V42. It is not inferred from any earlier broad continuation statement or ordinary approval.

## 2. Decision effect after canonical merge

Once this decision record is canonically merged, and only while every exact constraint in the canonical corrective decision request remains satisfied:

```text
FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION=E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION_B
CORRECTIVE_MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=AUTHORIZED_EXACT_TWO_GGUF_LOAD_ONLY
CORRECTIVE_MODEL_WEIGHT_ACQUISITION_AUTHORITY=AUTHORIZED_EXACT_TWO_PUBLIC_UNGATED_CANONICAL_GGUF_BUNDLES_ONLY
CORRECTIVE_MODEL_LOAD_AUTHORITY=AUTHORIZED_EXACT_TWO_GGUF_LOAD_ONLY
CORRECTIVE_IMPLEMENTATION_PREPARATION_AUTHORITY=AUTHORIZED_REVIEW_FIRST_STATIC_ONLY
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

This decision authorizes only preparation of a review-first corrective implementation, exact-head static qualification, expected-head guarded merge, post-merge canonical reverification, and exactly one post-merge corrective load-only evidence workflow run limited to the two frozen GGUF candidates below.

## 3. Frozen corrective candidate subject

The authorized corrective subject is exactly:

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd | LLAMA_CPP_GGUF | PRIMARY
Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68 | LLAMA_CPP_GGUF | PRIMARY
```

Exact frozen artifact identities remain:

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

No candidate, revision, model artifact, bundle, tokenizer/config identity, role, runtime route, or parent identity may be substituted.

The two already-PASS Transformers candidates are outside this corrective authority and must not be rerun.

## 4. Frozen llama.cpp runtime identity

The corrective implementation may repair only the preparation, staging, or build wiring necessary to use the same frozen runtime identity:

```text
LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
LLAMA_CPP_TAG=b10621
LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
LLAMA_RUNTIME_FILE_MANIFEST_SHA256=4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711
LIBLLAMA_SHA256=89869a6732162d45aa7fe5ab4b224e484c8f27f58c145e530e99dc59d8772448
LLAMA_BUILD_TOOLCHAIN_IDENTITY=GNU_11.4.0_LINUX_X86_64
```

Runtime revision, runtime archive identity, library identity, candidate format, and runtime route substitutions are prohibited.

## 5. Exact corrective implementation boundary

The corrective implementation may only:

1. diagnose the previously observed GGUF prerequisite/helper-build failure using repository-safe evidence;
2. repair the header/source/runtime staging or build wiring required for the existing reviewed load-only helper to compile against the exact frozen llama.cpp runtime identity;
3. harden cleanup behavior for the corrective GGUF jobs;
4. add or strengthen static policy tests for the exact corrective workflow;
5. add a dedicated post-merge-only corrective workflow mechanically limited to exactly the two frozen GGUF candidates;
6. preserve fail-closed reason-code handling when model load is not reached.

The helper semantics remain restricted to model construction/loading and free/backend teardown. No context creation, decode, encode, sampler, prompt, forward pass, logits computation, token generation, perplexity, benchmark, evaluation payload, tournament, winner selection, A15 activation, or training operation may be introduced.

## 6. Corrective one-run boundary

```text
MAX_AUTHORIZED_CORRECTIVE_MODEL_LOAD_COMPATIBILITY_WORKFLOW_RUNS=1
AUTHORIZED_CORRECTIVE_CANDIDATE_PROBES_PER_WORKFLOW=2_EXACTLY_ONE_PER_FROZEN_GGUF_CANDIDATE
AUTOMATIC_RERUN_AUTHORITY=NONE
FAILED_RUN_RETRY_AUTHORITY=NONE
SECOND_CORRECTIVE_WORKFLOW_RUN_AUTHORITY=NONE
RESOURCE_ESCALATION_AUTHORITY=NONE
RUNTIME_SUBSTITUTION_AUTHORITY=NONE
CANDIDATE_SUBSTITUTION_AUTHORITY=NONE
TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE
```

The original Decision-B evidence run remains consumed and must not be rerun, retried, or mutated:

```text
EVIDENCE_WORKFLOW_RUN_ID=34063020745
EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
MODEL_LOAD_COMPATIBILITY_EVIDENCE_RUN=CONSUMED_SINGLE_RUN_NO_RERUN_AUTHORITY
```

Ordinary byte-transport retries remain limited to the same exact public source URL/revision/path before the canonical SHA-256 gate. They are not workflow reruns and do not authorize source substitution.

## 7. Acquisition, network, credential, retention, resource, and finance boundary

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

If either exact GGUF candidate cannot complete model loading within this exact resource/runtime envelope, the corrective run must fail closed. No resource escalation, runtime substitution, candidate substitution, retry workflow, or third run is implied.

## 8. Review-first and post-merge boundary

Before the single corrective evidence run:

```text
PULL_REQUEST_MODEL_LOAD=PROHIBITED
REVIEW_FIRST_WORKFLOW_PREPARATION=REQUIRED
EXACT_HEAD_STATIC_QUALIFICATION=REQUIRED
CORRECTIVE_AUTHORITY_TOKEN_BINDING=REQUIRED
DIFF_WHITESPACE=PASS_REQUIRED
EXPECTED_HEAD_GUARDED_MERGE=REQUIRED
POST_MERGE_CANONICAL_REVERIFICATION=REQUIRED
```

No candidate bytes may be acquired and no model may be loaded from the decision-capture PR or the corrective implementation PR.

Independent repository review remains optional by default under FD-007 unless a later bounded authority explicitly requires it for this task. A skipped or unavailable automated review must not be represented as substantive independent review evidence.

## 9. Empirical disposition boundary

A GGUF candidate may receive empirical model-load compatibility PASS only when all exact artifact/runtime/integrity gates pass and the network-disabled load-only model process completes successfully without context execution, forward pass, inference, generation, benchmark/evaluation payload, tournament, winner selection, A15 activation, or training.

A prerequisite/helper-build failure before model load remains `INCOMPLETE_MODEL_LOAD_NOT_REACHED`; it must not be mislabeled as empirical model-load FAIL.

Static compatibility reasoning may never be promoted to empirical PASS.

## 10. Non-expansion statement

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
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
```

No tournament, winner, A15, E005, training-readiness, or project-completion claim may be inferred from this decision or from a future corrective load-only PASS.

## 11. Current disposition before canonical merge

```text
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v42-2026-09-07.md
FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION=E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION_B
POST_CANONICAL_EXACT_CORRECTIVE_FOUNDER_DECISION_TOKEN=CAPTURED_PENDING_CANONICAL_MERGE
CORRECTIVE_MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=PENDING_CANONICAL_DECISION_CAPTURE
CORRECTIVE_MODEL_WEIGHT_ACQUISITION_AUTHORITY=NONE_UNTIL_CANONICAL_MERGE
CORRECTIVE_MODEL_LOAD_AUTHORITY=NONE_UNTIL_CANONICAL_MERGE
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

After canonical merge, live authority must be reverified before any corrective implementation is prepared or treated as execution-authorized.
