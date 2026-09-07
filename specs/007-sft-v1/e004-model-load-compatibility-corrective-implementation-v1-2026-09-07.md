# E004 Model-Load Compatibility Corrective Implementation V1 — 2026-09-07

**Spec:** 007 SFT V1
**Task:** E004
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Authority record:** `specs/007-sft-v1/e004-model-load-compatibility-corrective-founder-decision-2026-09-07.md`
**Authority canonical merge:** `dbab184ac5c75f057963cc792b4b1472a6c64a01`
**Predecessor frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v42-2026-09-07.md`
**Artifact class:** review-first corrective implementation binding
**Current authorized spend:** USD 0

## 1. Purpose

Prepare the one authorized corrective model-load compatibility lane after the exact post-canonical Founder Decision B capture became canonical.

This implementation is limited to the two frozen GGUF candidates that did not reach model loading in the consumed original evidence run. It does not alter the candidate identities, frozen candidate bundles, llama.cpp runtime identity, load-only helper semantics, or any downstream authority.

## 2. Repository/runtime diagnosis from the consumed original run

The original Decision-B evidence run remains consumed:

```text
EVIDENCE_WORKFLOW_RUN_ID=34063020745
EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
MODEL_LOAD_COMPATIBILITY_EVIDENCE_RUN=CONSUMED_SINGLE_RUN_NO_RERUN_AUTHORITY
AUTOMATIC_RERUN_AUTHORITY=NONE
FAILED_RUN_RETRY_AUTHORITY=NONE
SECOND_WORKFLOW_RUN_AUTHORITY=NONE
```

Both frozen GGUF jobs successfully completed candidate bundle acquisition and integrity verification. Both then failed in the same pre-load runtime/helper compilation step before model loading was reached.

The exact observed compiler failure was:

```text
fatal error: ggml-alloc.h: No such file or directory
```

The frozen llama.cpp source at revision `c1d0e7a004015f23bc0233470b747b596f29b264` has `ggml/include/ggml-backend.h` directly include `ggml-alloc.h`. The original evidence workflow staged `ggml-backend.h` but omitted `ggml-alloc.h`, so the reviewed load-only helper could not compile.

This is a preparation/header-closure defect. It is not empirical model-load failure evidence.

## 3. Corrective change

The corrective implementation:

1. adds a dedicated post-merge-only corrective evidence workflow;
2. mechanically limits its matrix to exactly the two frozen GGUF candidates;
3. stages `ggml-alloc.h` from the same exact frozen llama.cpp source revision before helper compilation;
4. preserves the exact frozen runtime archive, runtime manifest, `libllama` identity, candidate bundle set, revisions, routes, and artifact hashes;
5. preserves the existing `tools/e004_model_load_probe.cpp` helper without semantic expansion;
6. freezes fail-closed empirical reason codes before execution;
7. records a pre-load prerequisite failure as `INCOMPLETE_MODEL_LOAD_NOT_REACHED_PRELOAD_PREREQUISITE_FAILED`;
8. adds a pull-request static-only qualification workflow that compiles the helper against the exact frozen llama.cpp runtime/header identity without acquiring or loading any model bytes;
9. adds static policy tests that prohibit Transformers reruns and authority expansion.

## 4. Frozen corrective subject

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
TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE
```

## 5. Frozen runtime identity

```text
LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
LLAMA_CPP_TAG=b10621
LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
LLAMA_RUNTIME_FILE_MANIFEST_SHA256=4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711
LIBLLAMA_SHA256=89869a6732162d45aa7fe5ab4b224e484c8f27f58c145e530e99dc59d8772448
LLAMA_BUILD_TOOLCHAIN_IDENTITY=GNU_11.4.0_LINUX_X86_64
```

No runtime substitution is introduced or authorized.

## 6. Review-first/static-only PR qualification

The implementation PR must not acquire candidate model bytes or load a model.

The dedicated static qualification workflow may only:

- run repository/static tests;
- download and verify the exact frozen public llama.cpp runtime archive;
- fetch the required headers from the exact frozen source revision;
- compile the reviewed load-only helper;
- verify diff whitespace;
- remove the temporary runtime/header bytes.

```text
PULL_REQUEST_MODEL_LOAD=PROHIBITED
PULL_REQUEST_MODEL_BYTE_ACQUISITION=PROHIBITED
EXACT_HEAD_STATIC_QUALIFICATION=REQUIRED
CORRECTIVE_AUTHORITY_TOKEN_BINDING=REQUIRED
DIFF_WHITESPACE=PASS_REQUIRED
EXPECTED_HEAD_GUARDED_MERGE=REQUIRED
POST_MERGE_CANONICAL_REVERIFICATION=REQUIRED
```

## 7. Corrective evidence workflow boundary

The corrective evidence workflow has no `pull_request` or `workflow_dispatch` trigger. It can run only from a dedicated evidence branch after the implementation is canonically merged and after one marker-only trigger commit binds the exact canonical implementation merge.

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

Exact reason codes frozen before execution:

```text
PASS_EXACT_MODEL_LOAD_COMPLETED
FAIL_MODEL_LOAD_ERROR
FAIL_RUNTIME_CRASH_DURING_MODEL_LOAD
INCOMPLETE_RESOURCE_LIMIT_OR_TERMINATION
INCOMPLETE_MODEL_LOAD_NOT_REACHED_PRELOAD_PREREQUISITE_FAILED
```

## 8. Non-expansion

```text
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
```

Even if both corrective GGUF candidates later receive empirical model-load PASS, no tournament, winner, A15, E005, training-readiness, or project-completion state is inferred.

## 9. Current implementation disposition before canonical merge

```text
CORRECTIVE_IMPLEMENTATION=PREPARED_REVIEW_FIRST_PENDING_EXACT_HEAD_STATIC_QUALIFICATION
CORRECTIVE_MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=AUTHORIZED_EXACT_TWO_GGUF_LOAD_ONLY_AFTER_CANONICAL_IMPLEMENTATION_AND_POST_MERGE_REVERIFICATION
CORRECTIVE_MODEL_LOAD_AUTHORITY=AUTHORIZED_EXACT_TWO_GGUF_LOAD_ONLY_AFTER_CANONICAL_IMPLEMENTATION_AND_POST_MERGE_REVERIFICATION
TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE
MODEL_FORWARD_PASS_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
GENERATION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY=NONE
WINNER_SELECTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```
