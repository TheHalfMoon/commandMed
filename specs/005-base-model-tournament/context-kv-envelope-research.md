# Spec 005 — Context / KV Envelope Research

**Lifecycle:** CLARIFY ONLY
**Evidence capture date:** 2026-08-23
**Canonical commandMed base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`
**Purpose:** read-only architecture/resource reasoning for the next bounded clarification decision.

> This document contains public-config inspection and deterministic arithmetic only. No model weights were downloaded, no runtime was installed, no model was executed, and no benchmark payload was opened. Memory figures below are theoretical architecture-level KV estimates, not measured runtime claims.

## 1. Why context must be frozen before device qualification

Context length directly changes memory use and latency. A candidate that appears to fit a 4-GB phone at 2K context may fail at 16K, while a hybrid-attention candidate can scale very differently from a conventional full-attention model.

Spec 005 therefore needs one candidate-neutral common context condition before device evidence is allowed. The condition must be demanding enough to represent a useful local medical assistant but conservative enough not to turn the low-resource target into an architecture-specific memory contest unrelated to the frozen medical/safety floor.

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

These values exclude model weights, allocator overhead, compute buffers, runtime/application memory, tokenizer/config memory, and platform overhead. Quantized KV can reduce the cache materially, but the exact block format and runtime overhead must be measured later under the pinned llama.cpp build; this document does not convert a theoretical bit-width ratio into a runtime guarantee.

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

## 4. Clarification consequence

A `16K` hard context on every frozen 4-GB device would make Qwen3-0.6B's unquantized KV cache alone approach `1.75 GiB` before weights or runtime overhead. That would force the tournament to depend immediately on aggressive KV quantization and platform-specific memory behavior.

A `4K` hard context is easier but undershoots the intended usefulness of a local longitudinal medical assistant and provides little stress differentiation.

The balanced pre-execution recommendation is therefore:

```text
CONTEXT_EVIDENCE_POLICY=8K_CORE_16K_STRESS
COMMON_CORE_DEVICE_CONTEXT=8192_TOKENS
LOW_RESOURCE_HARD_CONTEXT=8192_TOKENS
SECONDARY_STRESS_CONTEXT=16384_TOKENS
SECONDARY_STRESS_SCOPE=8GB_CLASS_OR_HIGHER_AND_WHERE_RUNTIME_SUPPORTS
```

Interpretation:

1. every candidate must eventually qualify at the same `8192`-token context on all five frozen mass-reach targets;
2. `16384` tokens is secondary stress evidence on the 8-GB-class or higher targets and on any lower-resource target where it can be measured safely without changing the canonical artifact;
3. failure of the optional 16K stress run on a 4-GB target does not by itself disqualify a candidate unless a later pre-execution policy explicitly makes 16K mandatory there;
4. no candidate receives a smaller hard context merely because its architecture uses more KV memory;
5. exact KV cache type remains a separate pre-execution freeze and must be identical or scientifically justified across candidates; candidate-specific post-result KV tuning is prohibited.

## 5. Why 8K is the recommended common hard context

- It is materially more useful than 4K for multi-turn patient history, evidence snippets, and structured clinical context.
- It keeps the conventional Qwen3-0.6B theoretical FP16/BF16 KV baseline below 1 GiB, leaving a plausible path to the current `<=2 GiB` peak-working-RAM engineering target once deployable KV compression and actual runtime evidence are considered.
- It does not grant Qwen3.5 an architecture-specific advantage by choosing an arbitrarily huge context solely because its hybrid attention scales more cheaply.
- It remains far below the upstream maximum context of either frontier model, so the tournament measures commandMed's mass-reach operating point rather than vendor maximum-context claims.
- It supports a clean 16K secondary stress tier without changing the hard qualification contract after results are observed.

## 6. Still unresolved after context acceptance

Even if `8K_CORE_16K_STRESS` is accepted, the following remain unresolved:

- exact llama.cpp revision;
- exact KV cache type(s) and quantization;
- whether K and V cache use identical types;
- exact batch/ubatch settings;
- prompt and generation token split inside the 8K condition;
- cache reuse/prompt-cache policy;
- measured peak RSS/working-set methodology per platform;
- TTFT/prefill/decode/sustained-throughput thresholds;
- thermal/energy protocol;
- OS and mobile wrapper/application versions;
- hard failure semantics beyond the frozen package ceiling.

These must be frozen before execution and may not be optimized per candidate after observing results.

## 7. Public sources

- https://huggingface.co/Qwen/Qwen3-0.6B-Base/blob/main/config.json
- https://huggingface.co/Qwen/Qwen3.5-0.8B-Base/blob/dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68/config.json
- https://huggingface.co/Qwen/Qwen3.5-0.8B-Base

## 8. Authority boundary

```text
CONTEXT_POLICY_STATUS=RESEARCH_RECOMMENDATION_PENDING_FOUNDER_CLARIFICATION
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PLAN_AUTHORITY=NONE
NEXT_LIFECYCLE_STEP=CLARIFY
```
