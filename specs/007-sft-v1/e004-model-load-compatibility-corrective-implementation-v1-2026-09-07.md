# E004 Model-Load Compatibility Corrective Implementation V1 — 2026-09-07

**Spec:** 007 SFT V1
**Task:** E004
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Corrective authority:** `FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION=E004_MODEL_LOAD_COMPATIBILITY_CORRECTIVE_DECISION_B`
**Corrective authority record:** `specs/007-sft-v1/e004-model-load-compatibility-corrective-founder-decision-2026-09-07.md`
**Corrective authority canonical merge:** `dbab184ac5c75f057963cc792b4b1472a6c64a01`
**Corrective authority canonical tree:** `2bc0bbfd77aac98f75cf285b7595ba71465e4313`
**Predecessor frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v42-2026-09-07.md`
**Original consumed evidence run:** `34063020745`, attempt `1`
**Implementation state:** REVIEW_FIRST_NOT_YET_CANONICAL
**Model load performed by this record/PR:** NO
**Current authorized spend:** USD 0

## 1. Purpose

Prepare the exact review-first corrective implementation authorized by the canonical corrective Founder Decision B after the original model-load compatibility evidence run established two Transformers PASS outcomes and two GGUF `INCOMPLETE_MODEL_LOAD_NOT_REACHED` outcomes.

This implementation does not rerun, retry, mutate, or reinterpret the consumed original workflow run. It does not perform model loading on pull request and does not expand authority beyond the exact two frozen GGUF candidates.

## 2. Observed pre-load failure being corrected

Read-only inspection of the original run `34063020745` established the same prerequisite failure for both frozen GGUF candidates after exact candidate acquisition/integrity had passed and before model load was reached:

```text
.../ggml-backend.h:4:10: fatal error: ggml-alloc.h: No such file or directory
    4 | #include "ggml-alloc.h"
      |          ^~~~~~~~~~~~~~
compilation terminated.
```

Affected original jobs:

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
ORIGINAL_JOB_ID=101566822624
ORIGINAL_MODEL_LOAD_REACHED=NO
ORIGINAL_DISPOSITION=INCOMPLETE_MODEL_LOAD_NOT_REACHED

Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
ORIGINAL_JOB_ID=101566822550
ORIGINAL_MODEL_LOAD_REACHED=NO
ORIGINAL_DISPOSITION=INCOMPLETE_MODEL_LOAD_NOT_REACHED
```

At frozen llama.cpp revision `c1d0e7a004015f23bc0233470b747b596f29b264`, `ggml-backend.h` directly includes `ggml-alloc.h`, and `ggml-alloc.h` directly includes `ggml.h`. The original evidence workflow staged `ggml-backend.h` but omitted `ggml-alloc.h`.

The corrective implementation therefore repairs only the observed header-staging closure. The reviewed load-only helper is unchanged.

## 3. Corrective implementation surfaces

```text
CORRECTIVE_EVIDENCE_WORKFLOW=.github/workflows/e004-model-load-compatibility-corrective-evidence-v1.yml
UNCHANGED_LOAD_ONLY_HELPER=tools/e004_model_load_probe.cpp
STATIC_POLICY_TEST=tests/spec007/test_e004_model_load_compatibility_policy.py
STATIC_QUALIFICATION_WORKFLOW=.github/workflows/e004-research-component-tournament-control-plane-v1.yml
```

The original evidence workflow remains unchanged as historical consumed evidence:

```text
ORIGINAL_EVIDENCE_WORKFLOW=.github/workflows/e004-model-load-compatibility-evidence-v1.yml
ORIGINAL_EVIDENCE_WORKFLOW_RUN_ID=34063020745
ORIGINAL_EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
ORIGINAL_EVIDENCE_WORKFLOW_MUTATION=NONE
ORIGINAL_EVIDENCE_WORKFLOW_RERUN=PROHIBITED
```

## 4. Exact frozen corrective subject

The corrective workflow contains exactly two matrix records:

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd | LLAMA_CPP_GGUF | PRIMARY
Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68 | LLAMA_CPP_GGUF | PRIMARY
```

The already-PASS Transformers candidates do not appear in the corrective matrix and have no corrective rerun authority.

Parent identities remain:

```text
CANDIDATE_ARTIFACT_BUNDLE_SET_ID=SP007_RO_001_CANDIDATE_ARTIFACT_BUNDLE_SET_V1
CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256=ee97fe0751743cc0d3a564b8f91add3c336267f08f2da86bf125dd7333db83fd
PROTOCOL_ID=SP007_RO_001_NONCLINICAL_BACKBONE_TOURNAMENT_V1
PROTOCOL_SHA256=1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8
```

## 5. Frozen runtime identity and bounded staging correction

No runtime substitution is introduced:

```text
LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
LLAMA_CPP_TAG=b10621
LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
LLAMA_RUNTIME_FILE_MANIFEST_SHA256=4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711
LIBLLAMA_SHA256=89869a6732162d45aa7fe5ab4b224e484c8f27f58c145e530e99dc59d8772448
```

The exact staged header set is:

```text
include/llama.h
ggml/include/ggml.h
ggml/include/ggml-cpu.h
ggml/include/ggml-backend.h
ggml/include/ggml-alloc.h
ggml/include/ggml-opt.h
ggml/include/gguf.h
```

The corrective workflow explicitly verifies that the staged `ggml-backend.h` contains `#include "ggml-alloc.h"` and that the missing dependency is present before compiling the unchanged helper.

No candidate identity, candidate bundle, GGUF model artifact, runtime archive, library identity, runtime route, or helper semantic operation is changed.

## 6. Load-only helper boundary remains unchanged

The existing helper remains limited to:

```text
llama_backend_init
llama_model_default_params
llama_model_load_from_file
llama_model_free
llama_backend_free
```

No context creation, decode, encode, batch, sampler, prompt, forward pass, logits computation, generation, perplexity, benchmark/evaluation payload, tournament, winner selection, A15 activation, or training operation is introduced.

## 7. Review-first and trigger boundary

The corrective evidence workflow has no `pull_request`, `workflow_dispatch`, or `repository_dispatch` trigger. Pull-request qualification is static-only.

The only future evidence trigger is:

```text
EVENT=push
BRANCH=evidence/e004-model-load-compatibility-corrective-run-v1
MARKER=.github/e004-model-load-compatibility-corrective-run-v1.txt
MAX_AUTHORIZED_CORRECTIVE_MODEL_LOAD_COMPATIBILITY_WORKFLOW_RUNS=1
AUTHORIZED_CORRECTIVE_CANDIDATE_PROBES_PER_WORKFLOW=2_EXACTLY_ONE_PER_FROZEN_GGUF_CANDIDATE
AUTOMATIC_RERUN_AUTHORITY=NONE
FAILED_RUN_RETRY_AUTHORITY=NONE
SECOND_CORRECTIVE_WORKFLOW_RUN_AUTHORITY=NONE
```

The marker commit must be the direct child of the canonical corrective implementation merge and must be the only file changed in the trigger commit. The workflow binds:

```text
CORRECTIVE_DECISION_CANONICAL_MERGE=dbab184ac5c75f057963cc792b4b1472a6c64a01
CORRECTIVE_AUTHORITY_PREDECESSOR_MAIN=531435907e9dd45163933a99ade1bc6b6194220a
ORIGINAL_EVIDENCE_WORKFLOW_RUN_ID=34063020745
CORRECTIVE_IMPLEMENTATION_CANONICAL_MERGE=<direct parent of marker commit>
```

Every corrective candidate job requires `github.run_attempt == 1`.

## 8. Candidate acquisition and model-load boundary

Each corrective job validates the canonical candidate-bundle set, selects exactly one frozen GGUF candidate/revision, requires `artifact_format=GGUF`, requires `candidate_role=PRIMARY`, requires exactly one `MODEL_WEIGHT`, acquires only the exact canonical public/ungated bundle files, and validates every canonical byte count and SHA-256 before runtime use.

Network access is permitted only during exact public byte acquisition and frozen runtime/header staging. The actual model-load process is executed under a separate Linux network namespace using `unshare -n`.

```text
NETWORK_DURING_MODEL_LOAD=PROHIBITED_ENFORCED_UNSHARE_N
USER_MANAGED_CREDENTIAL_USE=PROHIBITED
FOUNDER_PERSONAL_TOKEN_USE=PROHIBITED
REPOSITORY_SECRET_USE=PROHIBITED
GATED_ASSET_ACCESS=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
PHI_ACCESS=PROHIBITED
BENCHMARK_OR_EVALUATION_PAYLOAD_ACCESS=PROHIBITED
```

## 9. Frozen empirical disposition contract

Successful completion of the exact load-only helper after all identity/integrity/build gates yields only:

```text
EMPIRICAL_MODEL_LOAD_COMPATIBILITY=PASS
EMPIRICAL_MODEL_LOAD_REASON_CODE=PASS_EXACT_MODEL_LOAD_COMPLETED
```

Load-process nonzero outcomes are classified as:

```text
EXIT_137_OR_143=INCOMPLETE_RESOURCE_LIMIT_OR_TERMINATION
EXIT_134_OR_139=FAIL_RUNTIME_CRASH_DURING_MODEL_LOAD
OTHER_NONZERO_LOAD_EXIT=FAIL_MODEL_LOAD_ERROR
```

Any authority, marker, acquisition, integrity, runtime identity, header staging, helper build, infrastructure, or policy failure before model load fails closed and must not be represented as empirical model-load PASS or empirical model-load FAIL.

## 10. Retention, resource, and finance boundary

```text
RUNNER_CLASS=STANDARD_PUBLIC_UBUNTU_24_04_ONLY
LARGER_OR_PAID_RUNNER=PROHIBITED
RESOURCE_ESCALATION_AUTHORITY=NONE
RAW_MODEL_BYTE_ARTIFACT_UPLOAD=PROHIBITED
ACTIONS_CACHE_FOR_MODEL_BYTES=PROHIBITED
MODEL_BYTE_PERSISTENCE_AFTER_JOB=PROHIBITED
RETAINED_EVIDENCE=GITHUB_ACTIONS_LOG_METADATA_ONLY
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

Every corrective matrix job has unconditional cleanup of candidate bytes, runtime bytes, staged headers, helper binary, and local manifests.

## 11. Pull-request qualification requirements

Before canonical merge, the corrective implementation must genuinely satisfy:

```text
PULL_REQUEST_MODEL_LOAD=PROHIBITED
EXACT_HEAD_STATIC_QUALIFICATION=PASS_REQUIRED
CORRECTIVE_AUTHORITY_TOKEN_BINDING=PASS_REQUIRED
EXACT_TWO_GGUF_MATRIX_BINDING=PASS_REQUIRED
TRANSFORMERS_RERUN_EXCLUSION=PASS_REQUIRED
FROZEN_RUNTIME_IDENTITY_BINDING=PASS_REQUIRED
OBSERVED_HEADER_CLOSURE_CORRECTION=PASS_REQUIRED
LOAD_ONLY_HELPER_POLICY=PASS_REQUIRED
NO_RETENTION_OR_PAID_COMPUTE_PATH=PASS_REQUIRED
DIFF_WHITESPACE=PASS_REQUIRED
EXPECTED_HEAD_GUARDED_MERGE=PASS_REQUIRED
POST_MERGE_CANONICAL_REVERIFICATION=PASS_REQUIRED
```

No model bytes are acquired and no model is loaded by static pull-request qualification.

Independent repository review remains optional by default under FD-007 unless later bounded governance explicitly changes that requirement.

## 12. Non-expansion and non-closure

Even if both future corrective probes empirically PASS, this implementation and that evidence do not establish or authorize forward pass, inference, generation, benchmark/evaluation payload execution, tournament execution, winner selection, A15 activation, E005 progression, or training.

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
PROJECT_FINISHED=NO
```
