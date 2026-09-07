# E004 Registry Current-State Reconciliation V43 — 2026-09-07

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Predecessor:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v42-2026-09-07.md`
**Corrective Founder decision:** `specs/007-sft-v1/e004-model-load-compatibility-corrective-founder-decision-2026-09-07.md`
**Corrective Founder decision canonical merge:** `dbab184ac5c75f057963cc792b4b1472a6c64a01`
**Corrective implementation:** `specs/007-sft-v1/e004-model-load-compatibility-corrective-implementation-v1-2026-09-07.md`
**Corrective implementation PR:** #285
**Corrective implementation exact head:** `89c8cb111cecac1c64b5a42cd2313e09390d26d1`
**Corrective implementation canonical merge:** `689410e61b4338a1a18df51c98ee6c7023e1df2d`
**Canonical tree after PR #285:** `7802d33f32d7cf3ef2ac87f271ea6d5980d5e42a`
**Corrective evidence trigger head:** `031efa26c42563674f84c15604c7cdf23c61ecad`
**Corrective evidence trigger tree:** `b14fea83d207cceed54c341268a4e4165a8998fa`
**Corrective evidence workflow run:** `34150708258`, attempt `1`
**Artifact class:** deterministic append-only current-state / authority-frontier overlay
**Current authorized spend:** USD 0

## 1. Purpose

Reconcile the E004 frontier after the single authorized post-merge corrective model-load compatibility evidence run completed.

This record preserves the actual candidate-by-candidate empirical outcome. It does not rerun, retry, mutate, reinterpret, or replace either the original consumed evidence run or the corrective consumed evidence run.

## 2. Original evidence remains immutable and consumed

The original Decision-B evidence run remains historical consumed evidence:

```text
ORIGINAL_EVIDENCE_WORKFLOW_RUN_ID=34063020745
ORIGINAL_EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
ORIGINAL_MODEL_LOAD_COMPATIBILITY_EVIDENCE_RUN=CONSUMED_SINGLE_RUN_NO_RERUN_AUTHORITY
ORIGINAL_TRANSFORMERS_ROUTE_EMPIRICAL_MODEL_LOAD_COMPATIBILITY=PASS_FOR_BOTH_FROZEN_TRANSFORMERS_CANDIDATES
ORIGINAL_LLAMA_CPP_GGUF_ROUTE_EMPIRICAL_MODEL_LOAD_COMPATIBILITY=INCOMPLETE_MODEL_LOAD_NOT_REACHED_FOR_BOTH_FROZEN_GGUF_CANDIDATES
ORIGINAL_AUTOMATIC_RERUN_AUTHORITY=NONE
ORIGINAL_FAILED_RUN_RETRY_AUTHORITY=NONE
ORIGINAL_SECOND_WORKFLOW_RUN_AUTHORITY=NONE
```

The original workflow run was not rerun, retried, or mutated by the corrective lane.

## 3. Corrective implementation qualification was static and exact-head bound

PR #285 prepared the bounded two-GGUF corrective lane and repaired only the observed frozen-header staging omission by adding `ggml-alloc.h` to the header closure. The reviewed load-only helper remained unchanged.

Exact-head qualification on `89c8cb111cecac1c64b5a42cd2313e09390d26d1` established:

```text
CORRECTIVE_POLICY_TESTS=PASS_16_TESTS
SPEC007_REGRESSION=PASS_355_TESTS_50_SUBTESTS
FULL_REPOSITORY_REGRESSION=PASS_1004_TESTS_178_SUBTESTS
DIFF_WHITESPACE=PASS
PULL_REQUEST_MODEL_LOAD_PERFORMED=NO
EXPECTED_HEAD_GUARDED_MERGE=PASS
```

The corrective implementation became canonical through merge `689410e61b4338a1a18df51c98ee6c7023e1df2d`.

## 4. Exactly one corrective evidence run was created

The corrective evidence marker commit is the direct child of the canonical corrective implementation merge and changes only the canonical marker file.

```text
CORRECTIVE_EVIDENCE_BRANCH=evidence/e004-model-load-compatibility-corrective-run-v1
CORRECTIVE_EVIDENCE_TRIGGER_HEAD=031efa26c42563674f84c15604c7cdf23c61ecad
CORRECTIVE_EVIDENCE_WORKFLOW_RUN_ID=34150708258
CORRECTIVE_EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
CORRECTIVE_EVIDENCE_WORKFLOW_RUN_NUMBER=1
CORRECTIVE_EVIDENCE_WORKFLOW_EVENT=push
CORRECTIVE_EVIDENCE_WORKFLOW_OVERALL_CONCLUSION=failure
MAX_AUTHORIZED_CORRECTIVE_MODEL_LOAD_COMPATIBILITY_WORKFLOW_RUNS=1
AUTHORIZED_CORRECTIVE_CANDIDATE_PROBES_PER_WORKFLOW=2_EXACTLY_ONE_PER_FROZEN_GGUF_CANDIDATE
CORRECTIVE_AUTOMATIC_RERUN_AUTHORITY=NONE
CORRECTIVE_FAILED_RUN_RETRY_AUTHORITY=NONE
SECOND_CORRECTIVE_WORKFLOW_RUN_AUTHORITY=NONE
```

No second corrective run exists or is authorized.

## 5. Frozen corrective subject was preserved exactly

The corrective matrix contained exactly:

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd | LLAMA_CPP_GGUF | PRIMARY
Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68 | LLAMA_CPP_GGUF | PRIMARY
```

The already-PASS Transformers candidates were not rerun:

```text
TRANSFORMERS_CANDIDATE_RERUN_PERFORMED=NO
```

Parent identities remain unchanged:

```text
CANDIDATE_ARTIFACT_BUNDLE_SET_ID=SP007_RO_001_CANDIDATE_ARTIFACT_BUNDLE_SET_V1
CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256=ee97fe0751743cc0d3a564b8f91add3c336267f08f2da86bf125dd7333db83fd
PROTOCOL_ID=SP007_RO_001_NONCLINICAL_BACKBONE_TOURNAMENT_V1
PROTOCOL_SHA256=1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8
```

## 6. Corrective prerequisite repair succeeded for both GGUF candidates

For both corrective jobs, candidate acquisition and exact-byte integrity passed, the frozen llama.cpp runtime identity rebound successfully, the missing `ggml-alloc.h` dependency was present, and the unchanged load-only helper compiled successfully.

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd:
  CANDIDATE_BYTE_INTEGRITY=PASS
  CORRECTIVE_HEADER_CLOSURE_GGML_ALLOC=PASS
  LLAMA_RUNTIME_REBIND=PASS
  LOAD_ONLY_HELPER_SHA256=3e9c3e1b3db7bb7157d22bea1c8fbdb3410028960f939c364d335fab245680d4

Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68:
  CANDIDATE_BYTE_INTEGRITY=PASS
  CORRECTIVE_HEADER_CLOSURE_GGML_ALLOC=PASS
  LLAMA_RUNTIME_REBIND=PASS
  LOAD_ONLY_HELPER_SHA256=7de4ddc0e15884f56388648c6e5f0b435e83339a6933dd62858cfe32d62a7a2f
```

The different helper binary digests are recorded as observed per-job build outputs and are not promoted to a cross-job reproducibility claim.

Frozen runtime identity remained:

```text
LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
LLAMA_CPP_TAG=b10621
LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
LLAMA_RUNTIME_FILE_MANIFEST_SHA256=4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711
LIBLLAMA_SHA256=89869a6732162d45aa7fe5ab4b224e484c8f27f58c145e530e99dc59d8772448
```

## 7. Model load was reached and empirically failed for both GGUF candidates

Unlike the original run, the corrective prerequisite path completed and the reviewed load-only helper reached `llama_model_load_from_file` for both frozen GGUF candidates.

Both jobs emitted the same llama.cpp runtime diagnostic:

```text
llama_model_load_from_file_impl: no backends are loaded. hint: use ggml_backend_load() or ggml_backend_load_all() to load a backend before calling this function
```

### 7.1 Qwen/Qwen3-0.6B-Base

```text
CANDIDATE=Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
CORRECTIVE_JOB_ID=101832231080
MODEL_LOAD_REACHED=YES
EMPIRICAL_MODEL_LOAD_COMPATIBILITY=FAIL
EMPIRICAL_MODEL_LOAD_REASON_CODE=FAIL_MODEL_LOAD_ERROR
MODEL_LOAD_EXIT_CODE=2
OBSERVED_RUNTIME_DIAGNOSTIC=NO_BACKENDS_ARE_LOADED
```

### 7.2 Qwen/Qwen3.5-0.8B-Base

```text
CANDIDATE=Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
CORRECTIVE_JOB_ID=101832230804
MODEL_LOAD_REACHED=YES
EMPIRICAL_MODEL_LOAD_COMPATIBILITY=FAIL
EMPIRICAL_MODEL_LOAD_REASON_CODE=FAIL_MODEL_LOAD_ERROR
MODEL_LOAD_EXIT_CODE=2
OBSERVED_RUNTIME_DIAGNOSTIC=NO_BACKENDS_ARE_LOADED
```

The empirical classification is `FAIL`, not `INCOMPLETE_MODEL_LOAD_NOT_REACHED`, because the exact model-load operation was reached and returned a nonzero load error under the frozen disposition contract.

## 8. Four-candidate compatibility state after corrective evidence

The two original Transformers PASS results remain valid historical per-candidate evidence and were not rerun. The two corrective GGUF probes are empirical FAIL results.

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd=FAIL_MODEL_LOAD_ERROR
Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68=FAIL_MODEL_LOAD_ERROR
ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b=PASS_EXACT_MODEL_LOAD_COMPLETED
Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539=PASS_EXACT_MODEL_LOAD_COMPLETED_CONTROL_WINNER_INELIGIBLE
```

Aggregate state:

```text
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=2_PASS_2_FAIL
TRANSFORMERS_ROUTE_EMPIRICAL_MODEL_LOAD_COMPATIBILITY=PASS_FOR_BOTH_FROZEN_TRANSFORMERS_CANDIDATES
LLAMA_CPP_GGUF_ROUTE_EMPIRICAL_MODEL_LOAD_COMPATIBILITY=FAIL_FOR_BOTH_FROZEN_GGUF_CANDIDATES
RUNTIME_FORMAT_COMPATIBILITY_STATE_FOR_LIVE_SUBJECT=NOT_PASS_ALL_FOUR
SUCCESSOR_PASS_PREFLIGHT=NO
```

No aggregate workflow conclusion is substituted for the exact candidate-by-candidate evidence above.

## 9. Safety, network, retention, and finance evidence

Both corrective jobs executed model load with network disabled through `unshare -n`. The logs explicitly record no forward pass, inference, generation, benchmark/evaluation payload execution, tournament, winner selection, A15 activation, or training.

Cleanup succeeded for both jobs:

```text
NETWORK_DURING_MODEL_LOAD=PROHIBITED_ENFORCED_UNSHARE_N
TRANSFORMERS_CANDIDATE_RERUN_PERFORMED=NO
MODEL_FORWARD_PASS_PERFORMED=NO
MODEL_INFERENCE_PERFORMED=NO
GENERATION_PERFORMED=NO
BENCHMARK_EXECUTION_PERFORMED=NO
EVALUATION_PAYLOAD_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
WINNER_SELECTION_PERFORMED=NO
A15_ACTIVATION_PERFORMED=NO
TRAINING_PERFORMED=NO
MODEL_BYTE_PERSISTENCE_AFTER_JOB=NO
RAW_MODEL_BYTE_ARTIFACT_UPLOAD=NO
ACTIONS_CACHE_FOR_MODEL_BYTES=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

No protected data, gated asset, repository secret, Founder credential, paid compute, procurement, payment, or spend is evidenced by the corrective run.

## 10. Corrective authority is consumed

The exact corrective Decision-B authority has now been used by run `34150708258`, attempt `1`.

```text
CORRECTIVE_MODEL_LOAD_COMPATIBILITY_EVIDENCE_RUN=CONSUMED_SINGLE_RUN_WITH_2_FAIL_RESULT
CORRECTIVE_MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=CONSUMED
CORRECTIVE_MODEL_WEIGHT_ACQUISITION_AUTHORITY=CONSUMED
CORRECTIVE_MODEL_LOAD_AUTHORITY=CONSUMED
AUTOMATIC_RERUN_AUTHORITY=NONE
FAILED_RUN_RETRY_AUTHORITY=NONE
SECOND_CORRECTIVE_WORKFLOW_RUN_AUTHORITY=NONE
RESOURCE_ESCALATION_AUTHORITY=NONE
RUNTIME_SUBSTITUTION_AUTHORITY=NONE
CANDIDATE_SUBSTITUTION_AUTHORITY=NONE
TRANSFORMERS_CANDIDATE_RERUN_AUTHORITY=NONE
```

The failed run may not be retried or rerun under the consumed authority.

## 11. Dependency state

```text
E004_EVALUATION_ASSET_QUALIFICATION_SUBUNIT=COMPLETE
E004_RUNTIME_BINDING_EVIDENCE_SUBUNIT=COMPLETE_AUTHORITY_CONSUMED
E004_SUBJECT_METADATA_EVIDENCE_SUBUNIT=COMPLETE_AUTHORITY_CONSUMED
E004_CANDIDATE_ARTIFACT_BUNDLE_BINDING_SUBUNIT=COMPLETE
E004_LLAMA_ADAPTER_CONTROL_PLANE_SUBUNIT=COMPLETE
E004_TRANSFORMERS_ADAPTER_CONTROL_PLANE_SUBUNIT=COMPLETE
E004_EXECUTION_PLAN_ARGV_SUBUNIT=COMPLETE
E004_MODEL_LOAD_DECISION_SURFACE_SUBUNIT=COMPLETE_CANONICAL
E004_MODEL_LOAD_DECISION_CAPTURE_SUBUNIT=COMPLETE_CANONICAL_DECISION_B_CONSUMED
E004_MODEL_LOAD_COMPATIBILITY_IMPLEMENTATION_SUBUNIT=COMPLETE_CANONICAL
E004_MODEL_LOAD_COMPATIBILITY_EVIDENCE_RUN_SUBUNIT=COMPLETE_CONSUMED_SINGLE_RUN_WITH_PARTIAL_RESULT
E004_CORRECTIVE_MODEL_LOAD_DECISION_SURFACE_SUBUNIT=COMPLETE_CANONICAL
E004_CORRECTIVE_MODEL_LOAD_DECISION_CAPTURE_SUBUNIT=COMPLETE_CANONICAL_DECISION_B_CONSUMED
E004_CORRECTIVE_MODEL_LOAD_IMPLEMENTATION_SUBUNIT=COMPLETE_CANONICAL
E004_CORRECTIVE_MODEL_LOAD_EVIDENCE_RUN_SUBUNIT=COMPLETE_CONSUMED_SINGLE_RUN_WITH_2_FAIL_RESULT
E004_RUNTIME_COMPATIBILITY_SUBUNIT=INCOMPLETE_2_PASS_2_FAIL
E004_EXACT_SUBJECT_BINDING_SUBUNIT=INCOMPLETE
E004_RESOURCE_ACCESS_FINANCE_SUBUNIT=INCOMPLETE
E004_A1_A14_SNAPSHOT_SUBUNIT=INCOMPLETE
E004_A15_SUBUNIT=NOT_REACHED
E004_MODEL_EXECUTION_SUBUNIT=NOT_STARTED_NOT_AUTHORIZED_BY_GATE_STATE
E004_TOURNAMENT_EXECUTION_SUBUNIT=NOT_STARTED_NOT_AUTHORIZED_BY_GATE_STATE
E004_TASK_CHECKBOX=REMAINS_INCOMPLETE
E005_STATE=NOT_REACHED
```

## 12. Exact next lawful transition

The corrective evidence exposed a new bounded runtime prerequisite: the frozen llama.cpp load path reaches model loading but has no backend loaded before `llama_model_load_from_file`.

The consumed corrective Decision B does not authorize another workflow run, retry, runtime substitution, resource escalation, or expansion of the reviewed helper semantics to load backends.

Therefore the next lawful transition is repository-only reconciliation followed, if permitted by canonical governance, by a new explicit Founder decision surface for any further empirical backend-loading correction. No additional model-load execution may occur until a later exact post-canonical authority is independently established.

A broad continuation statement or ordinary authorization does not substitute for a future exact token if that future canonical decision surface requires one.

## 13. Non-expansion statement

The corrective result establishes no authority or readiness for:

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
```

The two Transformers model-load PASS results and two GGUF model-load FAIL results do not imply a tournament winner, A15 readiness, E005 readiness, training readiness, release readiness, or project completion.

## 14. Current disposition

```text
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v43-2026-09-07.md
CORRECTIVE_EVIDENCE_WORKFLOW_RUN_ID=34150708258
CORRECTIVE_EVIDENCE_WORKFLOW_RUN_ATTEMPT=1
CORRECTIVE_MODEL_LOAD_COMPATIBILITY_EVIDENCE_RUN=CONSUMED_SINGLE_RUN_WITH_2_FAIL_RESULT
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=2_PASS_2_FAIL
RUNTIME_FORMAT_COMPATIBILITY_STATE_FOR_LIVE_SUBJECT=NOT_PASS_ALL_FOUR
CORRECTIVE_MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=CONSUMED
CORRECTIVE_MODEL_LOAD_AUTHORITY=CONSUMED
AUTOMATIC_RERUN_AUTHORITY=NONE
FAILED_RUN_RETRY_AUTHORITY=NONE
SECOND_CORRECTIVE_WORKFLOW_RUN_AUTHORITY=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
SUCCESSOR_PREFLIGHT_DISPOSITION=BLOCKED_PENDING_NEW_EXACT_AUTHORITY_FOR_ANY_FURTHER_EMPIRICAL_MODEL_LOAD_CORRECTION
MODEL_RUNTIME_LOAD_PERFORMED=YES_TWO_TRANSFORMERS_PASS_TWO_GGUF_FAIL_LOAD_ONLY
MODEL_FORWARD_PASS_PERFORMED=NO
MODEL_INFERENCE_PERFORMED=NO
GENERATION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
TRAINING_PERFORMED=NO
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```
