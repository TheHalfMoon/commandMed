# E004 Successor Execution-Adapter Control Plane V1 — 2026-09-06

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Canonical predecessor frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v36-2026-09-06.md`
**Canonical base at branch creation:** `eca82cd0d837d07cf6b56da1de55241f03d93a98`
**Authority basis:** bounded E004 corrective-maintenance authorization, CM-3
**Artifact class:** non-executing execution-adapter control plane
**Execution effect:** NONE
**A15 effect:** NONE
**Training authority:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

V36 correctly left exact runtime argv and execution-plan identity incomplete. During the dependency-safe attempt to bind those values, the frozen evaluation semantics exposed a material adapter gap: one singular generation argv cannot truthfully represent the complete `SP007-RO-001` tournament.

The frozen evaluation set contains:

```text
MULTIPLE_CHOICE_CONDITIONAL_LIKELIHOOD_ASSET_COUNT=6
RESOURCE_MEASUREMENT_PROTOCOL_ASSET_COUNT=1
RESOURCE_PROBE_COUNT=8
RESOURCE_WARMUP_RUNS_PER_PROBE=1
RESOURCE_MEASURED_RUNS_PER_PROBE=3
RESOURCE_TOTAL_INVOCATIONS_PER_CANDIDATE=32
```

Therefore this control-plane unit binds only the already-evidenced `llama.cpp` route to the actual frozen evaluator semantics before any full four-candidate execution plan is claimed.

## 2. Authority boundary

CM-3 permits a minimal identity-bound E004 execution envelope/adapter and requires its qualification to remain synthetic/non-medical and non-executing.

This unit performs or authorizes none of the following:

```text
MODEL_LOAD=NO
MODEL_EXECUTION=NO
TOURNAMENT_EXECUTION=NO
PHYSICAL_DEVICE_EXECUTION=NO
MODEL_DOWNLOAD=NO
NETWORK_MODEL_ACCESS=NO
MODEL_CONVERSION=NO
A15_ACTIVATION=NO
TRAINING=NO
CREDENTIAL_USE=NO
PRIVATE_GOLD_ACCESS=NO
PHI_ACCESS=NO
PROCUREMENT=NO
PAYMENT=NO
SPEND_USD=0
```

It does not change `CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE`.

## 3. Exact pinned llama.cpp route

Existing canonical runtime evidence already binds:

```text
LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
LLAMA_BUILD_TOOLCHAIN_IDENTITY=GNU_11.4.0_LINUX_X86_64
LLAMA_CLI_EXECUTABLE_SHA256=f0034d9e6959f6c32b40cbb5326f41ccdbac21b77feb27a6f32c0a7465c9ebf7
LLAMA_PERPLEXITY_EXECUTABLE_SHA256=1c06240ed8594fd377d655aef2dab0865431e3e779c06638474c96b38e6d74a0
```

The exact pinned source implements `llama-perplexity --multiple-choice`. Its multiple-choice evaluator forms each candidate sequence as the question plus one answer, computes continuation log probabilities, normalizes by the evaluated token count, and selects the maximum normalized score. That is the required core semantics for the frozen `NORMALIZED_CONDITIONAL_LOG_LIKELIHOOD_ARGMAX` assets.

This static source-semantic match does **not** establish empirical model-load compatibility.

## 4. Frozen multiple-choice binary adapter

`src/commandmed/spec007/e004_execution_adapter.py` deterministically serializes each of the six frozen 12-case multiple-choice assets into the exact record layout consumed by the pinned `llama-perplexity` implementation:

```text
uint32 task_count
uint32 absolute_task_offsets[task_count]
for each task:
  uint32 question_utf8_bytes
  byte question[question_utf8_bytes]
  uint32 mc1_answer_count
  repeated mc1 answer strings using the same uint32-length UTF-8 encoding
  int32 mc1_labels[mc1_answer_count]
  uint32 mc2_answer_count=0
```

The previously observed runtime family is Linux x86_64. The adapter therefore names this byte contract explicitly:

```text
INPUT_FORMAT=LLAMA_CPP_MULTIPLE_CHOICE_LE32_V1
```

The serializer is deterministic, and every resulting payload receives a raw-byte SHA-256 before it may be referenced by a later execution plan.

No generated binary payload is committed by this unit.

## 5. Exact llama multiple-choice argv projection

For each frozen multiple-choice asset, the adapter projects one command vector with an exact local model path and exact generated payload path supplied by the later environment binding:

```text
llama-perplexity
--model <exact-local-model-path>
--file <exact-local-payload-path>
--multiple-choice
--multiple-choice-tasks 12
--ctx-size 512
--offline
```

`--ctx-size 512` makes the pinned runtime's own default explicit for reproducibility. `--offline` is part of the exact pinned runtime and prevents network access by the runtime.

The adapter creates no filesystem path authority. The final local paths remain subject to the later exact environment/resource/access binding.

## 6. Exact llama resource-probe invocation projection

The resource asset has eight frozen probes. Every probe requires one warmup and three measured runs, so the adapter expands it to exactly 32 invocation records per candidate.

Each invocation projects:

```text
llama-cli
--model <exact-local-model-path>
--prompt <exact-frozen-probe-input-text>
--n-predict 8
--temp 0
--seed 1
--ctx-size 512
--no-conversation
--no-display-prompt
--offline
```

The greedy temperature and fixed seed are adapter reproducibility controls, not scientific thresholds and not a new ranking criterion. The frozen prompt, `max_new_tokens=8`, warmup count, measured-run count, and required resource measurements remain unchanged.

The later resource evidence must still measure and validate the exact canonical fields required by `RESOURCE_MEASUREMENT_RECORD_V1`; this unit records no measurement.

## 7. Candidate coverage in this unit

The static runtime evidence assigned the two exact GGUF candidates to the pinned llama.cpp route:

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
```

For those two candidates only, the adapter can now deterministically construct a seven-operation non-executing manifest containing:

- six `MULTIPLE_CHOICE_SCORE` operations, each with one `llama-perplexity` invocation;
- one `RESOURCE_MEASUREMENT` operation containing all 32 `llama-cli` invocations;
- exact frozen protocol and evaluation-set identities;
- exact pinned runtime archive/source/toolchain identities;
- canonical adapter self-identity;
- `execution_performed=false` and `authorized_spend_usd=0`.

This is an adapter manifest, not the final live pre-execution subject and not a claim of runtime compatibility.

## 8. Deliberately unresolved Transformers route

The Granite PRIMARY and Qwen3-4B CONTROL remain assigned by existing static evidence to the exact Transformers/PyTorch runtime family, but the repository does not yet have an equivalently bound scoring/resource adapter that implements the frozen conditional-likelihood and resource semantics under that runtime.

Therefore:

```text
QWEN06_LLAMA_ADAPTER_STATIC_BINDING=READY_FOR_QUALIFICATION
QWEN35_LLAMA_ADAPTER_STATIC_BINDING=READY_FOR_QUALIFICATION
GRANITE_TRANSFORMERS_ADAPTER_STATIC_BINDING=INCOMPLETE
CONTROL_TRANSFORMERS_ADAPTER_STATIC_BINDING=INCOMPLETE
EXACT_FOUR_CANDIDATE_RUNTIME_ARGV=INCOMPLETE
EXACT_FOUR_CANDIDATE_EXECUTION_PLAN_SHA256=INCOMPLETE
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=INCOMPLETE
```

No synthetic hash or favorable state may fill those gaps.

## 9. Qualification requirements

Before this unit may merge, exact-head CI must prove at minimum:

```text
CM3_AUTHORITY_BINDING=PASS
COMPILE_CHANGED_ADAPTER_SURFACE=PASS
FOCUSED_E004_ADAPTER_TESTS=PASS
FOCUSED_CANDIDATE_BUNDLE_TESTS=PASS
FOCUSED_TOURNAMENT_TESTS=PASS
FOCUSED_PREEXECUTION_TESTS=PASS
SPEC007_REGRESSION=PASS
FULL_REPOSITORY_REGRESSION=PASS
DIFF_WHITESPACE=PASS
NO_REAL_MODEL_OR_RUNTIME_EXECUTION_DURING_QUALIFICATION=PASS_BY_WORKFLOW_SCOPE
```

Independent repository review remains optional by default under FD-007. No absent or skipped review may be described as substantive review PASS.

## 10. Successor frontier if qualification and canonical merge succeed

This unit may close only the llama-route adapter semantic subunit. It must not close the four-candidate execution-plan or live-subject gate.

The next dependency-safe sequence is:

1. implement and qualify a non-executing Transformers/PyTorch adapter for the exact Granite PRIMARY and Qwen3-4B CONTROL runtime family, matching the same frozen conditional-likelihood and resource semantics;
2. compose all four candidate adapter projections into deterministic per-candidate execution-plan identities without model execution;
3. separately establish runtime-format/model-load compatibility from genuine authorized evidence; static adapter correctness is insufficient;
4. continue V36's exact environment/resource/network/access/credential/retention/wallclock/zero-spend binding;
5. only after those non-A15 prerequisites pass may A1-A14 and later A15 proceed in canonical order.
