# Spec 005 — Context / KV Envelope Research

**Lifecycle:** CLARIFY ONLY
**Evidence capture date:** 2026-08-23
**Canonical commandMed base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`
**Purpose:** read-only architecture/resource reasoning plus founder-accepted context, KV-cache, and prompt/generation budget policies for bounded clarification session 3 questions 2–4.

> This document contains public-config inspection and deterministic arithmetic only. No model weights were downloaded, no runtime was installed, no model was executed, and no benchmark payload was opened. Memory figures below are theoretical architecture-level KV estimates, not measured runtime claims.

## 1. Why context, KV, and token-budget policy must be frozen before device qualification

Context length directly changes memory use and latency. A candidate that appears to fit a 4-GB phone at 2K context may fail at 16K, while a hybrid-attention candidate can scale very differently from a conventional full-attention model.

KV-cache representation also materially changes memory pressure and can interact with runtime/backend behavior. Candidate-specific post-result KV tuning would therefore destroy comparability.

Prompt/generation allocation is likewise part of the context contract. A nominal 8K run is not comparable if one candidate receives substantially more input context while another receives more generation headroom, or if template/system tokens are silently excluded from the counted prompt budget.

Spec 005 therefore needs one candidate-neutral common context condition, one candidate-neutral primary KV-cache policy, and one candidate-neutral serialized-prompt/generation split before device evidence is allowed. The conditions must be demanding enough to represent a useful local medical assistant while remaining conservative enough not to turn the low-resource target into an architecture-specific memory contest unrelated to the frozen medical/safety floor.

## 2. Qwen3-0.6B-Base architecture observation

Official `Qwen/Qwen3-0.6B-Base` config reports:

```text
hidden_size=1024
num_hidden_layers=28
num_attention_heads=16
num_key_value_heads=8
head_dim=128
max_position_embeddings=32768
use_sliding_window=false
```

For ordinary full-attention KV storage, a simple FP16/BF16 K+V estimate is:

```text
bytes_per_token = layers * kv_heads * head_dim * 2(K+V) * 2(bytes)
                = 28 * 8 * 128 * 2 * 2
                = 114688 bytes/token
                = 112 KiB/token
```

Theoretical FP16/BF16 KV-only baselines:

```text
4K_CONTEXT  ~= 448 MiB
8K_CONTEXT  ~= 896 MiB
16K_CONTEXT ~= 1792 MiB
32K_CONTEXT ~= 3584 MiB
```

These values exclude model weights, allocator overhead, compute buffers, runtime/application memory, tokenizer/config memory, and platform overhead. Quantized KV can reduce the cache materially, but exact Q8_0 block overhead and runtime allocation behavior must be measured later under the pinned llama.cpp build; this document does not convert a nominal bit-width ratio into a runtime-memory guarantee.

## 3. Qwen3.5-0.8B-Base architecture observation

Official `Qwen/Qwen3.5-0.8B-Base` config reports:

```text
hidden_size=1024
num_hidden_layers=24
full_attention_interval=4
num_attention_heads=8
num_key_value_heads=2
head_dim=256
max_position_embeddings=262144
```

The published layer layout has one full-attention layer after every three linear-attention layers, giving six full-attention layers in the 24-layer text stack.

A simplified FP16/BF16 full-attention KV-only estimate is therefore:

```text
bytes_per_token = 6 * 2 * 256 * 2(K+V) * 2(bytes)
                = 12288 bytes/token
                = 12 KiB/token
```

Theoretical full-attention KV-only baselines:

```text
4K_CONTEXT  ~= 48 MiB
8K_CONTEXT  ~= 96 MiB
16K_CONTEXT ~= 192 MiB
32K_CONTEXT ~= 384 MiB
```

This does **not** mean total Qwen3.5 runtime memory is only those values. Its Gated DeltaNet/linear-attention recurrent state, MTP-related state, compute buffers, model weights, allocator behavior, and platform/runtime overhead remain additional memory. The calculation exists only to demonstrate why the two frontier architectures have materially different context-memory scaling.

## 4. Frozen context clarification

A `16K` hard context on every frozen 4-GB device would make Qwen3-0.6B's unquantized KV cache alone approach `1.75 GiB` before weights or runtime overhead. That would force the tournament to depend immediately on aggressive KV compression and platform-specific memory behavior.

A `4K` hard context is easier but undershoots the intended usefulness of a local longitudinal medical assistant and provides little stress differentiation.

The founder-accepted context policy is:

```text
CONTEXT_EVIDENCE_POLICY=8K_CORE_16K_STRESS
COMMON_CORE_DEVICE_CONTEXT=8192_TOKENS
LOW_RESOURCE_HARD_CONTEXT=8192_TOKENS
SECONDARY_STRESS_CONTEXT=16384_TOKENS
SECONDARY_STRESS_SCOPE=8GB_CLASS_OR_HIGHER_AND_WHERE_RUNTIME_SUPPORTS
```

Interpretation:

1. every candidate must eventually qualify at the same `8192`-token hard context on all five frozen mass-reach targets;
2. `16384`-token stress evidence is mandatory on the frozen 8-GB-class-or-higher targets where the pinned runtime supports that context; it may also be collected on lower-resource targets where it can be measured safely without changing the canonical artifact;
3. the 16K stress tier is required evidence where in scope, but its pass/fail consequence is not invented here because target-specific hard-failure semantics remain a separate pre-execution freeze;
4. no candidate receives a smaller hard context merely because its architecture uses more KV memory.

## 5. Frozen KV-cache clarification

For bounded clarification session 3 question 3, the founder accepted a conservative symmetric Q8 KV policy for primary device qualification and the mandatory stress tier:

```text
KV_CACHE_POLICY=Q8_0_SYMMETRIC_KV_CORE
HARD_QUALIFICATION_K_CACHE_TYPE=Q8_0
HARD_QUALIFICATION_V_CACHE_TYPE=Q8_0
STRESS_K_CACHE_TYPE=Q8_0
STRESS_V_CACHE_TYPE=Q8_0
ASYMMETRIC_KV_PRIMARY_QUALIFICATION=PROHIBITED
Q4_KV_PRIMARY_QUALIFICATION=NOT_FROZEN
```

Interpretation:

1. K and V cache use the same `Q8_0` type for the common 8K hard qualification condition;
2. the same symmetric `Q8_0` K/V policy applies to required 16K stress evidence where that tier is in scope;
3. a candidate may not receive F16/BF16, Q4, mixed K/V, or another KV type merely because that representation improves its observed result;
4. asymmetric K/V cache types are prohibited for the primary qualification protocol unless a future separately reviewed pre-result clarification replaces this policy for all comparable candidates;
5. Q4-class KV remains outside the frozen primary qualification protocol. It may be studied later only under separate authorization/evidence and cannot retrospectively rescue a candidate that fails the canonical Q8_0 qualification condition;
6. this policy freezes the requested cache *type semantics*, not the exact llama.cpp revision, backend implementation, allocation footprint, or measured RAM consequence. Those identities and measurements remain pre-execution gates.

## 6. Frozen prompt/generation budget clarification

For bounded clarification session 3 question 4, the founder accepted a fixed `7K` serialized-prompt / `1K` generation split for the 8K core condition while retaining the same `1K` generation allowance in the 16K stress tier:

```text
CONTEXT_BUDGET_POLICY=7K_PROMPT_1K_GENERATION
CORE_TOTAL_CONTEXT_BUDGET=8192_TOKENS
CORE_MAX_SERIALIZED_PROMPT_BUDGET=7168_TOKENS
CORE_MAX_GENERATION_BUDGET=1024_TOKENS
STRESS_TOTAL_CONTEXT_BUDGET=16384_TOKENS
STRESS_MAX_SERIALIZED_PROMPT_BUDGET=15360_TOKENS
STRESS_MAX_GENERATION_BUDGET=1024_TOKENS
SERIALIZED_PROMPT_INCLUDES_SYSTEM_AND_TEMPLATE=YES
GENERATION_BUDGET_IDENTICAL_ACROSS_CANDIDATES=YES
```

Interpretation:

1. the 8K hard qualification condition reserves at most `7168` tokens for the complete serialized input and at most `1024` tokens for generated output;
2. the 16K stress condition reserves at most `15360` tokens for the complete serialized input and the same `1024`-token generation allowance;
3. the serialized-prompt budget includes every non-generated token presented to the model under the frozen protocol, including system text, prompt/chat template material, benchmark/context material, and user/input content; no hidden template or system-token allowance exists outside the stated budget;
4. the generation allowance is identical across candidates and devices for a given tier. Early stop/EOS may produce fewer generated tokens, but unused generation allowance does not expand the serialized-prompt ceiling;
5. a candidate may not receive a different prompt/generation split merely because its tokenizer, prompt template, architecture, or observed performance makes the canonical split less favorable;
6. token accounting must later be bound to the exact tokenizer/template/runtime identities before execution so that the declared serialized-token counts are reproducible and candidate-neutral.

This freezes budget ceilings and accounting semantics only. It does not authorize benchmark access or execution and does not yet freeze batch/ubatch, cache-reuse behavior, exact runtime identities, measurement methods, or performance thresholds.

## 7. Why the frozen policies are conservative for mass reach

- `8192` hard context is materially more useful than 4K for multi-turn patient history, evidence snippets, and structured clinical context while avoiding a universal 16K hard requirement on 4-GB devices.
- Symmetric `Q8_0` KV materially reduces cache pressure relative to FP16/BF16 without making primary qualification immediately depend on more aggressive Q4 cache compression.
- A `7168`-token serialized prompt leaves substantial room for longitudinal medical context while a `1024`-token generation ceiling remains large enough for a structured, safety-conscious response without allowing output length to dominate the memory/latency condition.
- Keeping the generation allowance at `1024` in both 8K and 16K tiers makes the stress tier primarily a longer-input-context test rather than changing two variables simultaneously.
- Counting system/template tokens inside the prompt budget prevents candidate-specific serialization overhead from being hidden outside the qualification envelope.

No exact MiB saving, runtime-quality claim, or latency claim is frozen from nominal datatype or token-budget arithmetic. Actual cache bytes, peak working memory, backend offload behavior, performance, and quality/safety effects must be measured later under the exact pinned runtime and frozen protocol.

## 8. Still unresolved after context, KV, and token-budget acceptance

With `8K_CORE_16K_STRESS`, `Q8_0_SYMMETRIC_KV_CORE`, and `7K_PROMPT_1K_GENERATION` accepted, the following remain unresolved:

- exact immutable llama.cpp revision and build configuration;
- exact backend/platform wrapper identities;
- exact tokenizer/template identities and the pre-execution token-accounting implementation that enforces the frozen serialized-prompt ceilings;
- exact batch/ubatch settings;
- cache reuse/prompt-cache policy;
- measured peak RSS/working-set methodology per platform and any hard RAM threshold;
- TTFT/prefill/decode/sustained-throughput thresholds;
- thermal/energy protocol;
- OS and mobile wrapper/application versions;
- repetition, warm-up, and aggregation methodology;
- hard failure semantics beyond already frozen package/context/KV/token-budget evidence requirements.

These must be frozen before execution and may not be optimized per candidate after observing results.

## 9. Public sources

- https://huggingface.co/Qwen/Qwen3-0.6B-Base/blob/main/config.json
- https://huggingface.co/Qwen/Qwen3.5-0.8B-Base/blob/dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68/config.json
- https://huggingface.co/Qwen/Qwen3.5-0.8B-Base
- https://github.com/ggml-org/llama.cpp/tree/master

## 10. Authority boundary

```text
CONTEXT_POLICY_STATUS=FOUNDER_ACCEPTED_FROZEN_CLARIFICATION
KV_CACHE_POLICY_STATUS=FOUNDER_ACCEPTED_FROZEN_CLARIFICATION
CONTEXT_BUDGET_POLICY_STATUS=FOUNDER_ACCEPTED_FROZEN_CLARIFICATION
CLARIFICATION_SESSION_3_QUESTION_2=ACCEPTED
CLARIFICATION_SESSION_3_QUESTION_3=ACCEPTED
CLARIFICATION_SESSION_3_QUESTION_4=ACCEPTED
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PLAN_AUTHORITY=NONE
NEXT_LIFECYCLE_STEP=CLARIFY
```
