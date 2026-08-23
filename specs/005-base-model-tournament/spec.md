# Spec 005 — Base Model Tournament

**Canonical state at branch base:** `AUTHORIZED_TO_SPECIFY`
**Canonical starting base:** `a68d37acd713049694106e81dc134ccf4d51feb9`
**Depends on:** Spec 004 `CLOSED_CANONICAL` + canonical founder decisions `FD-001`, `FD-002`, `FD-006`
**Working lifecycle:** CLARIFY — explicitly authorized by founder on 2026-08-23
**Training authority:** NONE
**Model execution authority:** NONE
**Model-weight access authority:** NONE
**Benchmark-payload execution authority:** NONE
**Private Gold access authority:** NONE
**Provider/API generation authority:** NONE
**PHI/restricted-data access authority:** NONE
**Gated-asset access authority:** NONE

> This specification defines the bounded problem and the gates that later lifecycle stages must resolve. It is not an execution manifest, model-access authorization, candidate freeze, benchmark-access authorization, or permission to accept gated terms.

## 1. Objective

Select the strongest release-compatible **base/backbone candidate evidence** for commandMed under a frozen, safety-capped, provenance-aware, resource-aware tournament.

A founder clarification on 2026-08-23 establishes `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY`: the eventual commandMed release should be small enough to make installation practical on iPhones, Android phones, and low-end ordinary laptops, with the explicit product ambition of maximizing broad Hugging Face adoption. The founder further sets `GLOBAL_HEALTH_AI_CATEGORY_LEADERSHIP` as a product ambition: commandMed should compete to become the most downloaded, most adopted, and most discussed open health-AI model on Hugging Face. These are adoption objectives, not scientific claims or ranking metrics, and they never override clinical safety, provenance, licensing, or minimum-quality gates.

Spec 005 is a **baseline-only tournament**. It does not train, fine-tune, distill, align, quantization-aware-train, or otherwise optimize a candidate.

The tournament must compare candidates using the canonical evaluation, safety, provenance, and tournament contracts inherited from Specs 001–004. A winner may be selected only when the evidence is complete, comparable, license-compatible with the intended release posture, and uniquely best under the predeclared comparison strategy.

A valid outcome may be `NO_SELECTION`.

## 2. Why this spec exists

The Grand Master Plan deliberately does not preselect a backbone. Spec 005 converts that principle into a bounded evidence decision while preserving four hard truths:

1. medical and safety quality cannot be traded away merely for a smaller parameter count;
2. a technically strong candidate is not release-eligible if its lineage or license posture is incompatible with the canonical founder decision;
3. claimed device fit must be demonstrated on named device/resource classes rather than inferred from model size or vendor claims;
4. once safety, provenance, licensing, and minimum-quality gates are satisfied, deployable package size and low-resource reach are first-class product constraints rather than secondary marketing claims.

Popularity, download counts, likes, social discussion, stars, or vendor reputation must not enter the scientific tournament ranking vector. Adoption success is measured after release under a separate product KPI framework.

## Clarifications

### Session 2026-08-23

**Bounded session 1 — complete (5/5)**

- Q: How should Spec 005 handle the primary comparison between text-only and multimodal candidates when selecting the base backbone? → A: `COMMON_CORE_PRIMARY_RANKING` — all `PRIMARY` candidates rank only on the common text/core protocol; modality-specific capability is secondary non-ranking evidence in Spec 005.
- Q: Should all `PRIMARY` candidates in Spec 005 be base/pretrained checkpoints only, excluding instruction-tuned models from primary ranking? → A: `BASE_ONLY_PRIMARY` — only base/pretrained checkpoints may be `PRIMARY`; instruction-tuned models may be `CONTROL` or `REFERENCE_ONLY` but cannot enter primary ranking or win Spec 005.
- Q: How should Spec 005 define the `FLAGSHIP_PLUS_MODERN_MIDRANGE` device evidence boundary? → A: `NAMED_DEVICE_PLUS_RESOURCE_ENVELOPE` — use one named physical representative per tier plus a reproducible resource envelope for that tier; exact device models and numeric thresholds remain to be frozen before execution.
- Q: Should the frozen primary tournament manifest include only `PRIMARY` candidates whose admission gates are complete before manifest freeze? → A: `FULLY_ADMITTED_PRIMARY_ONLY` — only fully admitted `PRIMARY` candidates may enter the frozen primary ranking manifest; unresolved candidates remain discovery/conditional outside that manifest.
- Q: What precision/quantization policy should Spec 005 use to separate fair backbone comparison from real-device deployability evidence? → A: `DUAL_BUILD_BASELINE_AND_DEPLOYABLE` — use a frozen reference build for primary capability comparison and a separately frozen deployable quantized build for device qualification; quantify compression regression separately.

**Bounded session 2 — complete (5/5)**

- Q: What candidate set should Spec 005 carry forward as the primary-admission shortlist before immutable revisions and exact license/lineage evidence are bound? → A: the original `FOUR_PERMISSIVE_BASE_SHORTLIST` is superseded before manifest freeze by the founder's `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY`. Subsequent read-only reconciliation now carries `Qwen/Qwen3-0.6B-Base` and `Qwen/Qwen3.5-0.8B-Base` as the current ultra-compact `PRIMARY` admission frontier; `swiss-ai/Apertus-v1.1-0.5B` remains a `CONDITIONAL` ultra-compact size comparator because its official model-card metadata includes an additional gated Acceptable Use Policy/terms-acceptance flow. Larger artifacts remain quality/device comparators until frozen pre-execution gates determine eligibility.
- Q: After hard safety, provenance, licensing, and minimum medical-quality gates pass, where should deployable package size appear in the frozen ranking order? → A: `QUALITY_FLOOR_THEN_SIZE_FIRST` — all hard gates and the frozen minimum medical-quality floor are evaluated first; among candidates that pass them, complete deployable package bytes are the first ranking metric (`LOWER_BETTER`), followed only by predeclared secondary capability/performance/resource metrics.
- Q: What mass-distribution envelope should the smallest commandMed Core release target? → A: `SUB_700MB_MASS_REACH` — the complete minimum text/core Hugging Face bundle has a hard ceiling of `700 MiB`; the engineering target is `<=600 MiB`; `<=500 MiB` is a stretch target only if the same safety and minimum medical-quality gates still pass. Peak working RAM has an engineering target of `<=2 GiB` at the later-frozen short-context condition, and qualification evidence must include a 4-GB-class phone/resource envelope rather than relying only on flagship devices.
- Q: What runtime/artifact strategy should be canonical for the smallest mass-distribution release across phones and weak laptops? → A: `GGUF_LLAMA_CPP_CANONICAL` — the minimum-distribution artifact is canonical GGUF with compatibility bound to an immutable reviewed llama.cpp revision/toolchain before execution; MLX, MLC, Core ML, or other native/accelerated derivatives may be published as optional optimized derivatives but do not replace the canonical minimum GGUF artifact or alter its package-size ranking evidence.
- Q: What quantization policy should be canonical for commandMed Core V1? → A: `Q4_FLOOR_SMALLEST_PASSING` — evaluate a frozen deployable ladder from higher-quality Q5/Q4-class candidates down through Q4-class (`Q5_K_M`, `Q4_K_M`, `Q4_K_S`, `IQ4_XS`, or exact architecture-equivalent variants frozen before execution). For each backbone, the canonical deployable release is the smallest allowed artifact that still passes every safety, minimum medical-quality, compression-regression, package/RAM, runtime, and device hard gate. Sub-4-bit Q3/IQ3/Q2 artifacts are excluded from the V1 `PRIMARY` canonical release even if smaller.

**Bounded session 3 — complete (5/5)**

- Q: Which named device/resource targets must Spec 005 represent before any live tournament can be authorized? → A: `MASS_REACH_FIVE_TARGET_SET` — require Apple iPhone 17 Pro 12 GB as the flagship Apple anchor, Apple iPhone 13 4 GB as the Apple low-resource anchor, Samsung Galaxy A56 5G 8 GB as the modern-midrange Android anchor, Samsung Galaxy A16 5G 4 GB as the low-resource Android anchor, and an Intel Processor N100 + 8 GB x86-64 weak-laptop envelope. This freezes the target set only; OS/runtime revisions, context/KV conditions, performance thresholds, thermal/energy protocol, and hard-failure semantics remain unresolved and must be frozen pre-execution.
- Q: What context length must be the common hard qualification condition on all five mass-reach targets? → A: `8K_CORE_16K_STRESS` — require `8192` tokens as the candidate-neutral hard context on all five frozen targets; require `16384`-token secondary stress evidence on 8-GB-class-or-higher targets where the pinned runtime supports that context. Exact KV cache types/quantization, batch/ubatch settings, prompt/generation split, cache policy, peak-RAM measurement, latency/throughput thresholds, thermals, energy, OS/runtime revisions, and target-specific hard-failure semantics remain unresolved and must be frozen before execution.
- Q: What KV-cache representation must be canonical for primary device qualification and required stress evidence? → A: `Q8_0_SYMMETRIC_KV_CORE` — use `Q8_0` for both K and V cache in the common 8K hard qualification condition and required 16K stress tier. Asymmetric K/V cache types are prohibited for primary qualification, and Q4-class KV is not frozen as a primary qualification path. Exact runtime revision/backend identities, batch/ubatch settings, prompt/generation split, cache reuse policy, measured peak-RAM method, performance thresholds, thermals, energy, and target-specific hard-failure semantics remain unresolved.
- Q: How must the frozen 8K and 16K context budgets be divided between serialized prompt/input and generated output? → A: `7K_PROMPT_1K_GENERATION` — cap the 8K hard condition at `7168` serialized-prompt tokens plus `1024` generation tokens, and the 16K stress condition at `15360` serialized-prompt tokens plus the same `1024` generation tokens. The serialized-prompt budget includes system text and prompt/chat-template tokens as well as benchmark/context/user material; unused generation allowance does not expand the prompt ceiling. Generation budget is identical across candidates. Exact tokenizer/template/runtime identities and the reproducible token-accounting implementation remain pre-execution gates, along with batch/ubatch, cache reuse, RAM/performance measurement, thermals, energy, OS/runtime revisions, and target-specific hard-failure semantics.
- Q: What prompt-processing batch and cache-reuse profile must measured device qualification use? → A: `B512_U128_COLD_NO_REUSE` — use logical batch `512` and physical ubatch `128` for measured qualification and required stress runs; prohibit prompt-cache, session-state, prefix-cache, or equivalent cross-run/precomputed prompt-state reuse; apply the same batch profile across comparable candidates and all frozen device targets. This freezes a comparability profile, not a measured performance claim. Exact runtime/backend identities, peak-RAM methodology, latency/throughput thresholds, thermal/energy protocol, OS/runtime revisions, repetition/warm-up/aggregation rules, and target-specific hard-failure semantics remain unresolved.

**Bounded session 4 — in progress (1/5)**

- Q: How must the canonical llama.cpp runtime identity be bound across iOS, Android, and x86-64 device qualification? → A: `PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST` — require one exact immutable llama.cpp core commit across all comparable candidates and all five frozen targets; prohibit mutable `master`/`main`/`latest` identities and candidate-specific or post-result runtime revision substitution; require a platform build manifest that binds the shared core commit, compiler/toolchain, relevant build flags/backend choices, target architecture/ABI, wrapper/application identity where applicable, and produced runtime/build artifact identity when available. This freezes the identity method only; the exact core commit SHA and concrete platform build values remain unresolved pre-execution evidence requirements.

**Founder clarification directives — do not consume additional clarification questions**

- `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY`: optimize the eventual release for extremely small download footprint and practical local use across iPhone, Android, and low-end laptops. The text/core package should be independently downloadable; optional multimodal/vision assets should not be required for the smallest common-core package when the chosen runtime permits separation. Safety, provenance, licensing, and minimum medical-quality requirements remain hard gates.
- `GLOBAL_HEALTH_AI_CATEGORY_LEADERSHIP`: optimize product packaging, documentation, discoverability, interoperability, demos, and community usability so commandMed can compete for category-leading Hugging Face downloads and mindshare. This is an aspirational product objective to be measured with post-release KPIs; it is not evidence that commandMed is already category-leading and does not alter scientific/safety qualification.

## 3. Canonical authority and inherited identities

This specification inherits the following canonical identities without redefining their semantics:

```text
BENCHMARKS_IDENTITY=7f58edba1ac179cbf24cb2d5c902e2ef947024bfd1c6eacdbef1a609b00f64a7
GOLD_PROTOCOLS_IDENTITY=40c89702469d759f4dc893aff6bc6fdb7e300f9cb2d8f19f2b3e0dbd78200666
METRICS_IDENTITY=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
QUARANTINE_IDENTITY=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
SAFETY_POLICY_IDENTITY=79a12414fe68fc08efb43070f3eede36976f2e0dc0ece7f4eed4bbcc5496d14f
LINEAGE_CONTRACT_IDENTITY=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962
```

Spec 004 tournament-harness implementation evidence:

```text
SPEC004_IMPLEMENTATION_MERGE=9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d
SPEC004_IMPLEMENTATION_TREE=7e37fa626f825ee25271e0bf21a627a2e64e49da
SPEC004_FINAL_REVIEWED_HEAD=cf6158ea4193aa7db895607c6fac5a3a1442f708
SPEC004_CLOSURE_MERGE=3dc705a1de09347f3574b305afb1bfaa6d46ecff
```

Canonical Spec 005 entry decision merge:

```text
SPEC005_ENTRY_DECISION_MERGE=a68d37acd713049694106e81dc134ccf4d51feb9
FD-001=OPEN_WEIGHTS_PERMISSIVE_DOWNSTREAM_USE
FD-002=FLAGSHIP_PLUS_MODERN_MIDRANGE
FD-006=NOT_INVOKED
```

No later lifecycle document may silently substitute different upstream identities.

## 4. Founder-decision consequences

### 4.1 Release/licensing posture

`FD-001=OPEN_WEIGHTS_PERMISSIVE_DOWNSTREAM_USE` means the intended release lineage should preserve permissive downstream use where the complete lineage legally permits it.

Therefore:

- permissive licensing is an admission and final-selection concern, not a cosmetic metadata field;
- exact base-model, dataset, tokenizer, code, adapter, teacher/output, and derivative obligations must be proven before irreversible use or final selection;
- custom or restrictive candidates may remain research/conditional candidates only when their exact intended-use compatibility is unresolved;
- a candidate whose model card combines permissive license metadata with additional gated/AUP terms remains `CONDITIONAL` until the exact intended-use rights and access posture are reconciled; license metadata alone must not be widened into `SUPPORTED` rights;
- a conditional candidate must not be promoted to the final release lineage merely because it scores well or is smaller;
- this specification does not itself declare any named candidate fully license-compatible merely because its current public model card reports a permissive license.

### 4.2 Target device tier and distribution reach

`FD-002=FLAGSHIP_PLUS_MODERN_MIDRANGE` establishes the V1 target tier, clarification freezes `NAMED_DEVICE_PLUS_RESOURCE_ENVELOPE` as the evidence strategy, the founder further establishes `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY` plus `SUB_700MB_MASS_REACH`, bounded clarification session 3 freezes `MASS_REACH_FIVE_TARGET_SET`, `8K_CORE_16K_STRESS`, `Q8_0_SYMMETRIC_KV_CORE`, `7K_PROMPT_1K_GENERATION`, and `B512_U128_COLD_NO_REUSE`, and bounded clarification session 4 freezes `PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST` as the runtime identity policy.

The frozen mass-reach package, target, context, KV, token-budget, prompt-processing, and runtime-identity policy is:

```text
MINIMUM_TEXT_CORE_BUNDLE_HARD_CEILING=700_MiB
MINIMUM_TEXT_CORE_BUNDLE_ENGINEERING_TARGET=600_MiB_OR_LESS
MINIMUM_TEXT_CORE_BUNDLE_STRETCH_TARGET=500_MiB_OR_LESS_IF_ALL_HARD_GATES_STILL_PASS
PEAK_WORKING_RAM_ENGINEERING_TARGET=2_GiB_OR_LESS_AT_FROZEN_SHORT_CONTEXT
LOW_RESOURCE_PHONE_EVIDENCE=4_GB_CLASS_REQUIRED
DEVICE_EVIDENCE_POLICY=MASS_REACH_FIVE_TARGET_SET
FLAGSHIP_REPRESENTATIVE=Apple_iPhone_17_Pro_12GB
APPLE_LOW_RESOURCE_REPRESENTATIVE=Apple_iPhone_13_4GB
MODERN_MIDRANGE_ANDROID_REPRESENTATIVE=Samsung_Galaxy_A56_5G_8GB
LOW_RESOURCE_ANDROID_REPRESENTATIVE=Samsung_Galaxy_A16_5G_4GB
LOW_RESOURCE_LAPTOP_ENVELOPE=Intel_N100_8GB_x86_64
CONTEXT_EVIDENCE_POLICY=8K_CORE_16K_STRESS
COMMON_CORE_DEVICE_CONTEXT=8192_TOKENS
LOW_RESOURCE_HARD_CONTEXT=8192_TOKENS
SECONDARY_STRESS_CONTEXT=16384_TOKENS
SECONDARY_STRESS_SCOPE=8GB_CLASS_OR_HIGHER_AND_WHERE_RUNTIME_SUPPORTS
KV_CACHE_POLICY=Q8_0_SYMMETRIC_KV_CORE
HARD_QUALIFICATION_K_CACHE_TYPE=Q8_0
HARD_QUALIFICATION_V_CACHE_TYPE=Q8_0
STRESS_K_CACHE_TYPE=Q8_0
STRESS_V_CACHE_TYPE=Q8_0
ASYMMETRIC_KV_PRIMARY_QUALIFICATION=PROHIBITED
Q4_KV_PRIMARY_QUALIFICATION=NOT_FROZEN
CONTEXT_BUDGET_POLICY=7K_PROMPT_1K_GENERATION
CORE_TOTAL_CONTEXT_BUDGET=8192_TOKENS
CORE_MAX_SERIALIZED_PROMPT_BUDGET=7168_TOKENS
CORE_MAX_GENERATION_BUDGET=1024_TOKENS
STRESS_TOTAL_CONTEXT_BUDGET=16384_TOKENS
STRESS_MAX_SERIALIZED_PROMPT_BUDGET=15360_TOKENS
STRESS_MAX_GENERATION_BUDGET=1024_TOKENS
SERIALIZED_PROMPT_INCLUDES_SYSTEM_AND_TEMPLATE=YES
GENERATION_BUDGET_IDENTICAL_ACROSS_CANDIDATES=YES
PROMPT_PROCESSING_POLICY=B512_U128_COLD_NO_REUSE
LOGICAL_BATCH_SIZE=512
PHYSICAL_UBATCH_SIZE=128
PROMPT_CACHE_REUSE_FOR_MEASURED_RUNS=PROHIBITED
SESSION_STATE_REUSE_FOR_MEASURED_RUNS=PROHIBITED
PREFIX_CACHE_REUSE_FOR_MEASURED_RUNS=PROHIBITED
BATCH_PROFILE_IDENTICAL_ACROSS_CANDIDATES=YES
BATCH_PROFILE_IDENTICAL_ACROSS_DEVICE_TARGETS=YES
RUNTIME_IDENTITY_POLICY=PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST
LLAMA_CPP_CORE_REVISION=IMMUTABLE_COMMIT_REQUIRED
MUTABLE_MASTER_OR_LATEST=PROHIBITED
SAME_CORE_REVISION_ACROSS_ALL_TARGETS=REQUIRED
PLATFORM_BUILD_MANIFEST=REQUIRED
COMPILER_AND_BUILD_FLAGS_PINNED=REQUIRED
PLATFORM_WRAPPER_IDENTITY_PINNED=REQUIRED
CANDIDATE_SPECIFIC_RUNTIME_REVISION=PROHIBITED
POST_RESULT_RUNTIME_SUBSTITUTION=PROHIBITED
```

Spec 005 must eventually bind execution evidence for every frozen target without silently weakening the resource class after candidate results are observed. A physical-device substitution is permissible only through a separately reviewed pre-result clarification that preserves the same or stricter resource class and records the reason and new exact identity.

Every candidate must eventually qualify at the same `8192`-token hard context on all five frozen targets using symmetric `Q8_0` K/V cache, the same `7168` serialized-prompt / `1024` generation ceiling, and the same cold `512/128` prompt-processing profile with no cross-run or precomputed prompt-state reuse. The `16384`-token tier is required secondary stress evidence on 8-GB-class-or-higher targets where the pinned runtime supports it and uses the same symmetric Q8_0 policy, `15360` serialized-prompt / `1024` generation ceiling, and cold `512/128` prompt-processing profile. The serialized-prompt budget includes system and template tokens; unused generation allowance cannot expand the prompt ceiling. The stress-result consequence remains separate from the hard 8K qualification condition until target-specific hard-failure semantics are frozen pre-execution.

All comparable device evidence must use one exact immutable llama.cpp core commit. Platform-specific builds may differ only where required by iOS, Android, or x86-64 toolchains, and every such path must carry a reproducible exact build manifest. The exact core SHA and concrete platform build values are not selected by this policy and remain unresolved pre-execution evidence requirements.

The `700 MiB` package ceiling is a hard qualification boundary. The `<=600 MiB` and `<=500 MiB` values are engineering and stretch targets, not substitutes for the hard safety/medical-quality gates. The `<=2 GiB` peak working RAM value remains an engineering target; exact measurement methodology and any hard RAM threshold are unresolved and must not be misreported as proven runtime guarantees before execution evidence exists.

The target set, common context policy, primary KV-cache type policy, prompt/generation budget policy, prompt-processing batch/cache-reuse policy, and runtime identity method are now frozen, but the exact llama.cpp commit value, exact OS/build versions, compiler/toolchain versions, build flags/backends, platform wrapper/application identities, produced runtime artifact identities, tokenizer/template identities and token-accounting implementation, latency/TTFT/throughput thresholds, peak-RAM hard threshold and measurement method, energy/battery and thermal protocol, repetition/warm-up/aggregation methodology, and target-specific hard-failure semantics remain intentionally unresolved. They must be fixed before live execution authorization and cannot be chosen after candidate results are observed.

### 4.3 Donor-origin restrictions

`FD-006=NOT_INVOKED` means commandMed does not automatically inherit model-origin restrictions from other projects.

Candidate eligibility is governed only by commandMed's own canonical evaluation, provenance, safety, licensing, device, and authorization contracts unless a later explicit founder decision changes this rule.

## 5. Non-goals and prohibited actions

The following are outside this clarification-stage authority:

- downloading, cloning, pulling, caching, or otherwise obtaining model weights;
- accepting gated model terms, gated dataset terms, or access requests;
- logging in to model providers or model hubs for gated access;
- running inference, generation, embeddings, reranking, scoring, or model-backed preprocessing;
- reading or executing benchmark payloads for tournament measurement;
- reading private Gold payloads;
- sending prompts or samples to provider APIs;
- training, SFT, LoRA/QLoRA, CPT, distillation, DPO, RLVR, QAT, or any other optimization;
- installing or changing runtime/model dependencies merely to prepare execution;
- creating hidden caches, credentials, secrets, tokens, provider sessions, or model-serving endpoints;
- choosing a winner from vendor claims, model-card claims, parameter count, reputation, preference, downloads, likes, or social attention;
- treating this document's candidate-admission shortlist as an execution manifest.

## 6. Tournament outcome contract

Spec 005 must produce evidence that can be consumed by the canonical Spec 004 harness without changing the harness comparison semantics.

Allowed tournament outcomes remain:

```text
SELECTED
NO_SELECTION
```

A candidate may participate in ranking only if its result is complete and qualified under the canonical contracts.

At minimum:

- lineage `PROHIBITED` is disqualifying;
- prohibited/reference-only use under the exact lineage contract is disqualifying for final selection;
- safety hard-gate failure is disqualifying;
- failure of the frozen minimum medical-quality floor is disqualifying for size-first ranking eligibility;
- failure of the `700 MiB` complete minimum text/core bundle ceiling is disqualifying for `PRIMARY` size-first ranking eligibility;
- missing, malformed, wrong-manifest, blocked, insufficient, or non-comparable evidence is `INCOMPLETE` rather than silently favorable;
- any declared candidate with incomplete required evidence forces `NO_SELECTION` before ranking;
- an exact top tie under the complete predeclared ranking vector forces `NO_SELECTION`;
- no candidate ID, input order, popularity, or ad hoc tie-break may select a winner.

## 7. Comparison strategy

The comparison strategy must remain predeclared and deterministic.

Spec 005 inherits the Spec 004 strategy:

```text
COMPARISON_STRATEGY=LEXICOGRAPHIC_PREDECLARED
TIE_POLICY=NO_SELECTION_ON_TIE
SIZE_PRIORITY=QUALITY_FLOOR_THEN_SIZE_FIRST
```

`QUALITY_FLOOR_THEN_SIZE_FIRST` means ranking occurs in two logically separate phases:

1. **qualification phase** — provenance/lineage, licensing, safety, minimum medical-quality, candidate identity, comparability, the `700 MiB` minimum-package ceiling, and all other frozen device/package hard gates must pass; a smaller model cannot compensate for failure of any hard gate;
2. **ranking phase** — among fully qualified candidates only, complete deployable package bytes are the first comparison metric with direction `LOWER_BETTER`; only then are the remaining predeclared secondary metrics compared lexicographically.

Requirements:

- only canonical non-hard-gate metrics eligible for comparison may enter the ranking vector;
- metric direction must be explicit (`HIGHER_BETTER` or `LOWER_BETTER`);
- ranking metric order must be frozen before live evaluation;
- the first ranking metric after qualification is complete deployable package bytes, measured under one frozen package-accounting rule;
- weighted sums are prohibited unless a future separately reviewed canonical contract explicitly replaces this rule;
- safety, lineage, licensing, and minimum medical-quality hard gates are not compensable by a smaller package or higher capability score;
- device/resource criteria that become hard qualification gates must be frozen before execution and must not be retrofitted after results are seen;
- the package metric must include every artifact required for the advertised minimum common-core installation; optional modality assets may be excluded only when they are genuinely optional and separately downloadable for every candidate under the frozen rule;
- adoption metrics such as Hugging Face downloads, likes, trends, social mentions, stars, or community buzz are product KPIs only and cannot enter the tournament ranking vector.

## 8. Candidate admission contract

`FULLY_ADMITTED_PRIMARY_ONLY` is frozen for the future primary ranking manifest.

Naming a candidate in clarification or planning does **not** authorize access or execution. A candidate may enter the frozen primary ranking manifest only after every required admission field is resolved and the candidate is classified `PRIMARY` under the frozen rules.

Before a candidate can enter a future frozen execution manifest, clarification/planning must bind all of the following:

1. canonical neutral `candidate_id`;
2. exact upstream organization/repository identity;
3. exact model artifact or variant identity;
4. immutable revision/commit/digest or equivalent exact-head record;
5. exact tokenizer/processor identity when distinct;
6. architecture/modalities needed to determine comparability;
7. declared base/pretrained vs instruction-tuned status;
8. complete license identifier and primary license evidence;
9. Spec 003 lineage disposition for the intended tournament use;
10. gated/access status without accepting new terms merely to discover it;
11. runtime compatibility evidence required to construct an authorized execution plan;
12. expected device/resource evidence class;
13. contamination/quarantine disposition where applicable;
14. whether the candidate is `PRIMARY`, `CONTROL`, `CONDITIONAL`, or `REFERENCE_ONLY`;
15. pre-execution evidence that the candidate has a plausible path to the frozen `700 MiB` package ceiling and low-resource RAM/device envelope without candidate-specific post-result threshold changes;
16. whether the exact candidate architecture can produce a canonical GGUF artifact compatible with the future pinned llama.cpp toolchain without candidate-specific exceptions that destroy comparability;
17. whether the candidate has at least one allowed Q5/Q4-class deployable quantization path under `Q4_FLOOR_SMALLEST_PASSING`; sub-4-bit-only feasibility is insufficient for V1 `PRIMARY` admission.

If any required admission field is unresolved, the candidate remains discovery-only or `CONDITIONAL` outside the frozen primary ranking manifest. It must not be inserted merely to produce `INCOMPLETE`, and it must not be removed after results are observed to rescue a selection. Candidate-set freeze occurs only after admission reconciliation is complete.

Under the canonical Spec 003 lineage contract, `rights_state=CONDITIONAL` or `UNRESOLVED` cannot yield `ELIGIBLE`. An exact-use model record may become eligible only after source verification, exact artifact binding for non-reference use, supported rights with evidence, privacy resolution where required, and any use-specific contamination requirements are satisfied. Spec 005 does not self-assert those evaluator-owned outputs.

## 9. Candidate roles

Candidate roles are semantically distinct:

### `PRIMARY`

A release-lineage candidate that is eligible, in principle, to win once exact provenance, safety, comparability, device, and execution gates are satisfied. Under `BASE_ONLY_PRIMARY`, the candidate must be an exact base/pretrained checkpoint; instruction-tuned checkpoints are not eligible for this role. Under `FULLY_ADMITTED_PRIMARY_ONLY`, all admission fields must be resolved before it can enter the frozen primary ranking manifest.

### `CONTROL`

A comparison anchor used to measure whether the primary candidate set actually offers value. A control is not automatically eligible to become the release backbone. An instruction-tuned model may be used as a control only under a separately frozen, scientifically valid non-primary protocol.

### `CONDITIONAL`

A technically relevant candidate whose exact license, intended-use, device-fit, access, or other admission condition is unresolved. It cannot become the final selected release lineage until the condition is explicitly resolved, and it cannot enter the frozen primary ranking manifest while conditional.

### `REFERENCE_ONLY`

May inform scientific context where the canonical lineage/evaluation rules permit, but cannot be selected as the release backbone under the current contract. Instruction-tuned models may be reference-only where scientifically useful and otherwise authorized.

## 10. Ultra-compact-first candidate admission shortlist

`ULTRA_COMPACT_FIRST_ADMISSION_SHORTLIST` is an admission-reconciliation set, not the final frozen primary ranking manifest. Read-only factual reconciliation may add or reclassify a candidate before manifest freeze; no post-result candidate substitution is permitted.

### Tier A — ultra-compact admission frontier

1. `Qwen/Qwen3-0.6B-Base` — `PRIMARY` admission-frontier candidate; exact official base Q8_0 GGUF feasibility is below the `700 MiB` ceiling, but an equal-method Q5/Q4 deployable path and all other admission gates remain unresolved;
2. `Qwen/Qwen3.5-0.8B-Base` — `PRIMARY` admission-frontier candidate; exact-base Q4_0 feasibility is below the `700 MiB` ceiling, with all remaining admission gates still unresolved;
3. `swiss-ai/Apertus-v1.1-0.5B` — `CONDITIONAL` ultra-compact package-size comparator, excluded from the future frozen `PRIMARY` manifest unless its additional gated Acceptable Use Policy/terms and exact intended-use rights are separately reconciled and authorized.

### Tier B — larger quality/device comparators

4. `Qwen/Qwen3.5-2B-Base` — compact quality comparator;
5. `mistralai/Ministral-3-3B-Base-2512` — upper-size quality/device comparator;
6. `google/gemma-4-E2B` — architecture/modality comparator subject to footprint proof;
7. `HuggingFaceTB/SmolLM3-3B-Base` — text-base quality/control comparator.

Read-only public-source verification performed during clarification observed:

- `Qwen/Qwen3-0.6B-Base` is an official base/pretrained artifact under Apache-2.0 at observed immutable revision `d4e79cdcc24cc3dc566196f5af6ed5782c64e8f1`; public metadata exposes upstream weight SHA-256 `cd2a512003e2f9f3cd3c32a9c3573f820bb28c940f73c57b1ddaa983d9223eba` without requiring weight download;
- official `ggml-org/Qwen3-0.6B-Base-GGUF` evidence exposes exact-base `Qwen3-0.6B-Base-Q8_0.gguf` at approximately `639 MB`, SHA-256 `ebb25a17e79b1f43834410fb711ac3dc985364eb875b45914181f55b9993f2d0`, demonstrating that even Q8_0 fits the frozen package ceiling; exact-base Q5/Q4 evidence was not observed in that repository and must not be inferred from post-trained Qwen3-0.6B artifacts;
- `Qwen/Qwen3.5-0.8B-Base` is an official pre-trained-only base artifact with a 0.8B language model and Apache-2.0 metadata; current read-only public inspection has not identified an equivalent gated terms-acceptance flow for this repository;
- an exact-base `ggml-org/Qwen3.5-0.8B-Base-GGUF` conversion exposes `Qwen3.5-0.8B-Base-Q4_0.gguf` at approximately `563 MB` with published SHA-256 `0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d`, demonstrating exact-base GGUF size feasibility below the 700 MiB ceiling; this is not commandMed quality/device evidence and is not the future canonical commandMed conversion;
- the captured 0.6B Q8_0 and 0.8B Q4_0 package numbers are **not apples-to-apples** and cannot rank candidates; equal-method build evidence is required before package-size comparison;
- `HuggingFaceTB/SmolLM2-360M` is an Apache-2.0 base with public exact-base Q4_K_M feasibility around `271 MB`, but its official card states that the model primarily understands and generates English; because `arabic_clinical_parity_gap` is a canonical hard gate, it remains an ultra-small control/conditional comparator rather than being promoted on size alone;
- `swiss-ai/Apertus-v1.1-0.5B` is an official base text-generation artifact whose metadata reports Apache-2.0 and whose model card describes a highly efficient 0.5–4B family for constrained hardware, but the official metadata also contains an `extra_gated_prompt` for the Apertus LLM Acceptable Use Policy plus an explicit terms-acceptance field; therefore Apache-2.0 metadata alone does not establish supported rights or ungated access for commandMed's intended uses;
- a current community conversion of `swiss-ai/Apertus-v1.1-0.5B` demonstrates a llama.cpp-compatible `Q4_K_M` GGUF of approximately `306 MB`; this is **size/runtime-feasibility evidence only** and does not remove upstream access/rights conditions;
- Apertus 0.5B is not a medical-specialized model, so its small size cannot substitute for the same frozen medical-quality and safety gates that would apply if it ever became fully admitted;
- `google/gemma-3-270m` is a very small pretrained artifact, but its current access path uses gated terms and the Gemma custom license; it remains `CONDITIONAL` with no gated-access authority;
- `Qwen/Qwen3.5-2B-Base` currently reports Apache-2.0 and 2B language-model parameters, but representative Q4 GGUF artifacts are materially larger than the frozen 700 MiB ceiling;
- `mistralai/Ministral-3-3B-Base-2512` is identified by its official model card as a base pre-trained Apache-2.0 variant;
- `google/gemma-4-E2B` currently reports Apache-2.0 metadata;
- `HuggingFaceTB/SmolLM3-3B-Base` is identified by its official model card as a base model after pretraining and Apache 2.0;
- `LiquidAI/LFM2.5-2.6B-Base` remains under custom `lfm1.0` metadata and is not promoted into this shortlist.

Those observations are **discovery evidence only**. They do not satisfy the exact Spec 003 lineage contract, immutable-revision requirement, tokenizer/processor identity binding, access-status proof, contamination/quarantine proof, runtime compatibility proof, medical-quality proof, or device qualification required for `PRIMARY` admission.

Therefore:

- Qwen3 0.6B and Qwen3.5 0.8B form the current ultra-compact `PRIMARY` admission frontier; neither is yet fully admitted or selected;
- the 0.6B/0.8B captured package values cannot rank them because the observed quantizations differ;
- Apertus 0.5B remains useful as a strong package-size feasibility comparator, but its gated AUP/terms make its exact intended-use rights `CONDITIONAL` for commandMed until separately reconciled; it must stay outside the future frozen `PRIMARY` manifest under `FULLY_ADMITTED_PRIMARY_ONLY` while conditional;
- SmolLM2 360M remains a useful ultra-small control/conditional comparator but cannot bypass the Arabic clinical hard gate merely because it is smaller;
- none of the candidates is yet declared fully admitted;
- none is yet present in a frozen execution manifest;
- immutable revisions/digests and neutral `candidate_id` values remain unresolved as final frozen identities where not already captured as read-only evidence;
- exact license texts, notices, upstream code/runtime obligations, tokenizer/processor licensing, and intended-use compatibility must be bound before admission;
- pre-execution package/RAM/runtime evidence may legitimately exclude a larger or incompatible candidate before live tournament execution once all remaining universal-low-resource and runtime details are frozen;
- no candidate may be added after results merely because the frozen candidate set failed.

### Medical reference/control continuity — MedGemma

MedGemma remains scientifically important but is not a current V1 `PRIMARY` mass-distribution candidate under this contract:

- `google/medgemma-1.5-4b-it` is currently available only as a 4B multimodal instruction-tuned variant and therefore is ineligible under `BASE_ONLY_PRIMARY`;
- `google/medgemma-4b-pt` is a genuine pretrained medical base checkpoint, but access requires acceptance of Health AI Developer Foundations terms and therefore is not equivalent to the intended Apache-2.0-style permissive admission posture;
- current community GGUF evidence for MedGemma 4B places Q4-class text-model artifacts at roughly 2.4–2.6 GB and even Q2 around 1.8 GB, before optional multimodal projector assets, so the 4B base cannot satisfy the frozen `700 MiB` V1 primary package ceiling;
- canonical decision `D-006` already places the MedGemma family in reference/evaluation-only status by default.

Accordingly, `google/medgemma-4b-pt` should be carried forward as an explicit **medical quality reference/control candidate** when its access and evaluation are separately authorized. It is a model commandMed should aim to meet or exceed on relevant medical dimensions, but it cannot win the current V1 mass-distribution backbone tournament unless a later canonical decision changes the frozen role/device/license contract.

### Conditional discovery outside the primary shortlist

The LFM2.5 family, including `LiquidAI/LFM2.5-2.6B-Base`, remains `CONDITIONAL` discovery outside the primary-admission shortlist under canonical decision `D-007`. Its current public model metadata reports the custom `lfm1.0` license, so exact intended-use and downstream-release compatibility with `FD-001` must be proven before any promotion.

Other prior discovery items remain non-primary unless separately reconciled:

- Apertus v1.1 0.5B — conditional ultra-compact size comparator while its additional gated AUP/terms remain unresolved for commandMed's intended uses;
- SmolLM2 360M — ultra-small control/conditional comparator because English-primary upstream scope cannot substitute for Arabic clinical qualification;
- Gemma 3 270M — conditional gated/custom-license ultra-small comparator;
- Phi-4-mini family — control/reference consideration only where exact checkpoint status and purpose justify it;
- MedGemma family — explicit medical reference/control, reference/evaluation-only by default under `D-006`;
- frontier closed, restricted, or gated medical models — reference-only unless a later canonical decision and lineage disposition explicitly authorize more.

No shortlist decision authorizes model access, gated-term acceptance, weight retrieval, benchmark execution, or winner selection.

## 11. Base vs instruction-tuned comparability

`BASE_ONLY_PRIMARY` is frozen for Spec 005.

Only exact base/pretrained checkpoints are eligible for the `PRIMARY` role and the primary ranking vector. Instruction-tuned, chat, aligned, or other post-pretraining checkpoints cannot enter the primary ranking and cannot be selected as the Spec 005 backbone winner.

Instruction-tuned models may be admitted only as `CONTROL` or `REFERENCE_ONLY` where their separate scientific purpose, evidence contract, and access are explicitly authorized. Their scores cannot be mixed into the `PRIMARY` ranking vector, break a primary tie, compensate for weaker base-model evidence, or create an exception to the base-only rule.

If a model family has no exact eligible base/pretrained checkpoint that satisfies the frozen admission contract, that family remains outside the `PRIMARY` candidate set rather than substituting an instruction-tuned checkpoint.

## 12. Modality comparability

`COMMON_CORE_PRIMARY_RANKING` is frozen for Spec 005.

All `PRIMARY` candidates rank only on a common text/core protocol whose dimensions are valid across every admitted primary candidate. Native multimodal capability must not alter the primary ranking vector in Spec 005.

Modality-specific evidence may be collected only if separately authorized and scientifically comparable, and must be reported as **secondary non-ranking evidence** for this spec. It cannot break a tie, compensate for a weaker common-core score, or create a cross-track winner.

A later multimodal spec may evaluate modality-specific capabilities under its own frozen contract. No post-result comparability rule may be invented to favor a candidate.

## 13. Evaluation evidence requirements

Before live execution, the evaluation plan must bind exact authorized subsets/slices of the canonical Spec 001 benchmark and metric contracts.

At minimum, the eventual plan must preserve evidence across relevant dimensions such as:

- core medical knowledge and reasoning;
- patient conversational behavior where the baseline protocol can validly test it;
- uncertainty/abstention;
- safety hard gates;
- Arabic and English capability;
- general-capability preservation potential where measurable without training;
- document/multimodal evidence as secondary non-ranking evidence only where separately authorized and comparable;
- resource/device evidence;
- package/download footprint and runtime reach across the frozen low-resource envelopes;
- license/lineage fit.

This clarification-stage document does not authorize opening or executing the benchmark payloads needed to obtain those results.

## 14. Device, package, runtime, quantization, and resource evidence

`NAMED_DEVICE_PLUS_RESOURCE_ENVELOPE`, `MASS_REACH_FIVE_TARGET_SET`, `8K_CORE_16K_STRESS`, `Q8_0_SYMMETRIC_KV_CORE`, `7K_PROMPT_1K_GENERATION`, `B512_U128_COLD_NO_REUSE`, `PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST`, `DUAL_BUILD_BASELINE_AND_DEPLOYABLE`, `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY`, `QUALITY_FLOOR_THEN_SIZE_FIRST`, `SUB_700MB_MASS_REACH`, `GGUF_LLAMA_CPP_CANONICAL`, and `Q4_FLOOR_SMALLEST_PASSING` are frozen as Spec 005 evidence strategies.

The minimum text/core package and device envelope is:

```text
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_HARD_CEILING=700_MiB
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_ENGINEERING_TARGET=600_MiB_OR_LESS
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_STRETCH_TARGET=500_MiB_OR_LESS_IF_HARD_GATES_PASS
PEAK_WORKING_RAM_ENGINEERING_TARGET=2_GiB_OR_LESS_AT_FROZEN_SHORT_CONTEXT
LOW_RESOURCE_PHONE_TEST_ENVELOPE=4_GB_CLASS
CANONICAL_MINIMUM_DISTRIBUTION_ARTIFACT=GGUF
CANONICAL_RUNTIME_FAMILY=LLAMA_CPP
V1_PRIMARY_QUANTIZATION_POLICY=Q4_FLOOR_SMALLEST_PASSING
SUB4BIT_PRIMARY_CANONICAL_RELEASE=PROHIBITED
DEVICE_EVIDENCE_POLICY=MASS_REACH_FIVE_TARGET_SET
FLAGSHIP_REPRESENTATIVE=Apple_iPhone_17_Pro_12GB
APPLE_LOW_RESOURCE_REPRESENTATIVE=Apple_iPhone_13_4GB
MODERN_MIDRANGE_ANDROID_REPRESENTATIVE=Samsung_Galaxy_A56_5G_8GB
LOW_RESOURCE_ANDROID_REPRESENTATIVE=Samsung_Galaxy_A16_5G_4GB
LOW_RESOURCE_LAPTOP_ENVELOPE=Intel_N100_8GB_x86_64
CONTEXT_EVIDENCE_POLICY=8K_CORE_16K_STRESS
COMMON_CORE_DEVICE_CONTEXT=8192_TOKENS
LOW_RESOURCE_HARD_CONTEXT=8192_TOKENS
SECONDARY_STRESS_CONTEXT=16384_TOKENS
SECONDARY_STRESS_SCOPE=8GB_CLASS_OR_HIGHER_AND_WHERE_RUNTIME_SUPPORTS
KV_CACHE_POLICY=Q8_0_SYMMETRIC_KV_CORE
HARD_QUALIFICATION_K_CACHE_TYPE=Q8_0
HARD_QUALIFICATION_V_CACHE_TYPE=Q8_0
STRESS_K_CACHE_TYPE=Q8_0
STRESS_V_CACHE_TYPE=Q8_0
ASYMMETRIC_KV_PRIMARY_QUALIFICATION=PROHIBITED
Q4_KV_PRIMARY_QUALIFICATION=NOT_FROZEN
CONTEXT_BUDGET_POLICY=7K_PROMPT_1K_GENERATION
CORE_TOTAL_CONTEXT_BUDGET=8192_TOKENS
CORE_MAX_SERIALIZED_PROMPT_BUDGET=7168_TOKENS
CORE_MAX_GENERATION_BUDGET=1024_TOKENS
STRESS_TOTAL_CONTEXT_BUDGET=16384_TOKENS
STRESS_MAX_SERIALIZED_PROMPT_BUDGET=15360_TOKENS
STRESS_MAX_GENERATION_BUDGET=1024_TOKENS
SERIALIZED_PROMPT_INCLUDES_SYSTEM_AND_TEMPLATE=YES
GENERATION_BUDGET_IDENTICAL_ACROSS_CANDIDATES=YES
PROMPT_PROCESSING_POLICY=B512_U128_COLD_NO_REUSE
LOGICAL_BATCH_SIZE=512
PHYSICAL_UBATCH_SIZE=128
PROMPT_CACHE_REUSE_FOR_MEASURED_RUNS=PROHIBITED
SESSION_STATE_REUSE_FOR_MEASURED_RUNS=PROHIBITED
PREFIX_CACHE_REUSE_FOR_MEASURED_RUNS=PROHIBITED
BATCH_PROFILE_IDENTICAL_ACROSS_CANDIDATES=YES
BATCH_PROFILE_IDENTICAL_ACROSS_DEVICE_TARGETS=YES
RUNTIME_IDENTITY_POLICY=PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST
LLAMA_CPP_CORE_REVISION=IMMUTABLE_COMMIT_REQUIRED
MUTABLE_MASTER_OR_LATEST=PROHIBITED
SAME_CORE_REVISION_ACROSS_ALL_TARGETS=REQUIRED
PLATFORM_BUILD_MANIFEST=REQUIRED
COMPILER_AND_BUILD_FLAGS_PINNED=REQUIRED
PLATFORM_WRAPPER_IDENTITY_PINNED=REQUIRED
CANDIDATE_SPECIFIC_RUNTIME_REVISION=PROHIBITED
POST_RESULT_RUNTIME_SUBSTITUTION=PROHIBITED
```

### 14.1 Canonical mass-distribution artifact/runtime

`GGUF_LLAMA_CPP_CANONICAL` means:

- the canonical minimum text/core Hugging Face release artifact is GGUF;
- the conversion procedure, GGUF metadata expectations, and llama.cpp compatibility must be bound to immutable reviewed toolchain/revision identities before any execution or release qualification;
- the exact canonical GGUF artifact identity is the artifact whose bytes enter the `QUALITY_FLOOR_THEN_SIZE_FIRST` package-size evidence;
- the same canonical artifact should be usable across ordinary desktop/laptop and mobile-compatible llama.cpp paths wherever the target platform/runtime supports it; platform-specific wrappers must not silently produce a scientifically different model artifact;
- MLX, MLC, Core ML, native mobile packages, or other optimized derivatives may be released later as optional acceleration/convenience artifacts, but they are secondary derivatives and cannot replace the canonical GGUF artifact for minimum-download claims or primary size ranking;
- an optional derivative that materially changes weights, quantization, tokenizer behavior, prompt semantics, or evaluation-relevant outputs requires its own exact identity and evidence and cannot inherit canonical GGUF claims automatically;
- no llama.cpp installation, dependency mutation, model conversion, runtime execution, mobile build, or weight access is authorized by this clarification decision.

### 14.2 V1 canonical quantization policy

`Q4_FLOOR_SMALLEST_PASSING` means:

- the future deployable quantization ladder must be frozen before any candidate results are observed;
- the intended ladder begins with Q5/Q4-class GGUF variants such as `Q5_K_M`, `Q4_K_M`, `Q4_K_S`, and `IQ4_XS`, or exact architecture-equivalent variants proven comparable and frozen before execution;
- each candidate's canonical deployable artifact is the **smallest allowed ladder member** that passes every frozen safety, minimum medical-quality, compression-regression, `700 MiB` package, RAM, runtime, and device gate;
- a candidate does not gain an exception merely because a lower-bit representation is the only way it can satisfy the size ceiling;
- Q3/IQ3/Q2 and other sub-4-bit variants are not eligible as the V1 `PRIMARY` canonical release, even if they are useful experimental artifacts later;
- the exact order, tool flags, imatrix/calibration policy if any, metadata, and architecture-specific equivalence mapping must be frozen before execution and applied without post-result candidate-specific tuning.

### 14.3 Immutable runtime identity policy

`PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST` means:

- one exact immutable llama.cpp core commit SHA must be selected and reviewed before any runtime/device execution authorization;
- that same core commit must govern every comparable candidate and all five frozen target paths;
- mutable `master`, `main`, `latest`, unpinned package versions, or unbound marketplace/application builds are not sufficient execution identity;
- platform-specific compilation is allowed only through exact build manifests that bind the shared core commit, compiler/toolchain identity, relevant build flags/options, backend/acceleration selection, target architecture/ABI, wrapper/application identity where applicable, and produced runtime/build artifact identity when available;
- candidate-specific or target-specific core revision substitution is prohibited, including a substitution intended to rescue compatibility or performance after results are known;
- the exact selected core SHA and concrete build-manifest values remain unresolved until separately reviewed pre-execution evidence is captured;
- the previously inspected llama.cpp revision `70adb1b4cea5ee39f867792c78dc59320921eda7` is interface evidence only and is not canonicalized by this policy.

The complete minimum bundle measurement must include model weights plus every tokenizer, config, model-side runtime metadata, and other artifact required for the advertised minimum text/core installation. A general-purpose application/runtime binary may be reported separately only under a single frozen accounting rule applied identically to every candidate. Optional vision or other modality assets may be excluded from the minimum package only when they are genuinely optional and separately downloadable under the same policy for all candidates.

Every frozen target must be represented by named physical-device evidence where the target is a named device and by its corresponding reproducible resource description. The weak-laptop target is intentionally an exact CPU/RAM/ISA envelope; a retail laptop SKU may be added pre-execution if required without weakening that envelope.

The future evidence plan must cover all five frozen targets: iPhone 17 Pro 12 GB, iPhone 13 4 GB, Galaxy A56 5G 8 GB, Galaxy A16 5G 4 GB, and Intel N100 + 8 GB x86-64. Every target must use the common `8192`-token hard qualification context with symmetric `Q8_0` K/V cache, the fixed `7168` serialized-prompt / `1024` generation ceiling, logical batch `512`, physical ubatch `128`, no prompt/session/prefix cache reuse for the measured run, and the same immutable llama.cpp core revision under its platform build manifest. The `16384`-token secondary stress tier is required on the iPhone 17 Pro 12 GB, Galaxy A56 5G 8 GB, and Intel N100 + 8 GB x86-64 targets where the pinned runtime supports that context, and must use the same symmetric `Q8_0` K/V cache, `15360` serialized-prompt / `1024` generation ceiling, `512/128` prompt-processing profile, cold/no-reuse semantics, and same shared core revision. It may be collected on lower-resource targets where safe and comparable, but no candidate may receive a reduced 8K hard context, a different KV-cache type, a different prompt/generation allocation, a different batch profile, reused prompt state, or a different core runtime revision because its memory scaling, tokenizer, template overhead, compatibility, or observed prefill performance is less favorable. iPhone coverage must be demonstrated through an Apple-compatible llama.cpp-compatible runtime/application path using the canonical GGUF identity or an explicitly proven equivalent path; it must not be inferred from desktop Apple Silicon results. Android and low-resource laptop coverage likewise require platform-specific execution evidence once separately authorized.

Each admitted `PRIMARY` candidate must also have two predeclared build roles when execution is eventually authorized:

1. a **reference build** governed by a common, frozen high-precision policy for primary common-core capability comparison; and
2. a **deployable build** governed by the canonical GGUF and `Q4_FLOOR_SMALLEST_PASSING` policy for device qualification on the named devices and resource envelopes.

The reference build supplies the evidence used to evaluate the frozen minimum medical-quality floor and other reference-quality requirements. Device/package qualification and the size-first ranking metric use the canonical deployable GGUF build. The deployable build must not replace the reference build for reference-quality claims, and the reference build must not be used to claim phone deployability. Quality/safety regression attributable to compression must be measured and reported separately under a frozen rule; if compression pushes the deployable build below a required hard gate, that candidate is not qualified for size-first ranking.

The exact reference precision, conversion toolchain revision, selected llama.cpp core commit SHA, concrete platform build manifests, architecture-specific equivalence rules, tokenizer/template identities and token-accounting implementation, latency/throughput/energy/thermal thresholds, peak-RAM hard threshold/measurement method, and minimum medical-quality threshold remain unresolved and must be frozen before execution. A policy may not be changed per candidate after results are observed.

Before execution authorization, clarification/planning must additionally define:

- exact package-byte measurement procedure and exclusions;
- exact immutable llama.cpp core commit and GGUF conversion-toolchain identities;
- exact platform build manifests for every required execution path, including compiler/toolchain, relevant flags/backend choices, target ABI, wrapper/application identity where applicable, and produced runtime artifact identity when available;
- exact final Q5/Q4 ladder order, conversion flags, and any calibration/imatrix inputs and quarantine rules;
- verification that the pinned runtime/backend implements the frozen symmetric `Q8_0` K/V cache semantics consistently across all required platform paths;
- exact tokenizer/template identities and a reproducible token-accounting implementation that counts all system/template/context/input tokens inside the frozen serialized-prompt ceilings;
- verification that the pinned runtime/backend implements logical batch `512`, physical ubatch `128`, and the cold/no-reuse prompt-processing semantics consistently across all required platform paths;
- peak-memory measurement method and any hard RAM threshold;
- TTFT/prefill/decode/sustained-throughput measurement method and thresholds;
- energy and thermal measurement method or explicit bounded proxy if direct measurement is not feasible;
- repetition count, warm-up, aggregation, and failure handling, with any warm-up prohibited from preloading or reusing measured prompt state;
- what constitutes a hard device/runtime qualification failure beyond the already frozen `700 MiB` package ceiling, `8192`-token common hard context, symmetric Q8_0 primary KV policy, frozen prompt/generation ceilings, cold `512/128` prompt-processing profile, and immutable shared-core runtime identity policy;
- how mandatory 16K stress evidence is interpreted where in scope without retroactively changing the 8K hard qualification rule;
- the minimum medical-quality floor below which a smaller artifact cannot qualify;
- the secondary metric order used only after complete deployable package bytes tie.

Parameter count and upstream marketing claims remain descriptive only. No target substitution, context reduction, KV-cache substitution, prompt/generation reallocation, batch/ubatch substitution, prompt-state reuse, runtime-core substitution, remaining envelope boundary, quantization rule, RAM hard threshold, medical-quality threshold, or secondary ranking rule may be chosen after candidate results are known.

## 15. Reproducibility and exact identity

Every live result must eventually be bound to immutable evidence sufficient to prove:

- exact candidate artifact/revision;
- exact tournament manifest digest;
- exact canonical upstream identities;
- exact reference-build identity;
- exact canonical GGUF deployable artifact identity and quantization type;
- exact conversion-toolchain identity and shared llama.cpp core commit SHA;
- exact per-platform runtime build manifest and produced runtime/build artifact identity where available;
- exact benchmark/metric/safety/lineage contracts;
- exact device/resource identity where device evidence is claimed;
- exact context/KV/token-budget configuration used for each device result, including symmetric Q8_0 K/V identity and serialized-prompt/generation ceilings for primary qualification;
- exact tokenizer/template identities and serialized-token accounting record;
- exact logical batch `512`, physical ubatch `128`, and evidence that no prohibited prompt/session/prefix state was reused in the measured run;
- exact packaged artifact identity and byte size where distribution evidence is claimed;
- exact result-set evidence artifact IDs;
- deterministic tournament report identity.

A mutable tag, model family name, `latest`, branch name, mutable runtime branch, marketplace label, or unpinned runtime version is not sufficient identity.

## 16. Fail-closed rules

Spec 005 must fail closed whenever evidence needed for a defensible selection is absent or contradictory.

Examples include:

- unresolved license or lineage disposition;
- model-card license metadata accompanied by additional gated/AUP terms whose intended-use compatibility has not been resolved;
- required gated access not separately authorized;
- missing exact artifact identity;
- candidate not being an exact eligible base/pretrained checkpoint under `BASE_ONLY_PRIMARY`;
- candidate entering the frozen primary ranking manifest before all admission fields are resolved under `FULLY_ADMITTED_PRIMARY_ONLY`;
- incomplete safety evidence;
- failure of the frozen minimum medical-quality floor;
- benchmark or Gold quarantine violation;
- non-comparable metric vectors;
- complete minimum text/core bundle exceeding `700 MiB` under the frozen accounting rule;
- inability to construct a canonical comparable GGUF artifact under the frozen toolchain/runtime contract;
- inability to satisfy V1 gates using an allowed Q5/Q4-class artifact under `Q4_FLOOR_SMALLEST_PASSING`;
- using Q3/IQ3/Q2 or another sub-4-bit artifact as the V1 `PRIMARY` canonical release;
- missing required evidence for any target in `MASS_REACH_FIVE_TARGET_SET` once device execution is separately authorized;
- failure to apply the same `8192`-token hard qualification context to every frozen mass-reach target;
- failure to use symmetric `Q8_0` K/V cache for primary qualification or required stress evidence;
- use of asymmetric K/V cache types in the primary qualification protocol;
- use of Q4-class or candidate-specific KV cache as a retrospective rescue path for primary qualification;
- exceeding the frozen `7168` serialized-prompt or `1024` generation ceiling in the 8K hard condition;
- exceeding the frozen `15360` serialized-prompt or `1024` generation ceiling in the 16K stress condition;
- excluding system/template tokens or other model-visible non-generated tokens from serialized-prompt accounting;
- candidate-specific prompt/generation reallocation or allowing unused generation headroom to expand the prompt ceiling;
- failure to use logical batch `512` and physical ubatch `128` for measured primary qualification or required stress evidence;
- prompt-cache, session-state, prefix-cache, or equivalent cross-run/precomputed prompt-state reuse in a measured qualification run;
- candidate- or target-specific batch/ubatch tuning after results are observed;
- use of mutable `master`/`main`/`latest` or another non-immutable runtime identity for measured evidence;
- different llama.cpp core revisions across comparable candidates or frozen target paths;
- missing or insufficient platform build manifest for a measured target path;
- candidate-specific or post-result runtime core substitution intended to rescue compatibility/performance;
- pooling evidence from different runtime-core revisions as if it shared one exact runtime identity;
- missing required `16384`-token stress evidence on an 8-GB-class-or-higher target where the pinned runtime supports it;
- post-result reduction or candidate-specific adjustment of the frozen 8K hard context, Q8_0 KV policy, prompt/generation budget, cold `512/128` prompt-processing profile, or shared runtime identity policy;
- post-result substitution of a frozen named device/resource target or weakening of its resource class;
- missing required reference or deployable build evidence under `DUAL_BUILD_BASELINE_AND_DEPLOYABLE`;
- unmeasured required compression regression;
- incomplete or candidate-specific package accounting that would make the size metric non-comparable;
- omitting required assets from the measured minimum package or inconsistently excluding optional modality assets;
- substituting an MLX/MLC/Core ML/native derivative for the canonical GGUF evidence without a separately frozen equivalence contract;
- envelope boundary, runtime, build policy, KV policy, token-budget policy, prompt-processing policy, quantization policy, package threshold, RAM threshold, medical-quality threshold, or ranking-rule changes after results are observed;
- runtime or build drift without a new exact identity;
- candidate-set drift after manifest freeze;
- exact top tie under the complete predeclared ranking vector.

The correct outcome in these cases is not a guessed winner; it is refusal, disqualification where canonical rules require it, or `NO_SELECTION`.

## 17. Required clarification questions

The clarification lifecycle must answer, at minimum:

1. **PARTIALLY RESOLVED / RECONCILED FRONTIER:** `Qwen/Qwen3-0.6B-Base` and `Qwen/Qwen3.5-0.8B-Base` form the current ultra-compact `PRIMARY` admission frontier. The 0.6B exact-base Q8_0 feasibility artifact is ~639 MB and the 0.8B exact-base Q4_0 artifact is ~563 MB, but those values are not comparable because quantization differs. `swiss-ai/Apertus-v1.1-0.5B` remains a smaller `CONDITIONAL` comparator because of its additional gated AUP/terms. Immutable frozen candidate IDs and the final fully admitted `PRIMARY` set remain unresolved.
2. **RESOLVED:** `BASE_ONLY_PRIMARY`; only exact base/pretrained checkpoints may be `PRIMARY`. Instruction-tuned models may be `CONTROL` or `REFERENCE_ONLY` but cannot enter primary ranking or win Spec 005.
3. **PARTIALLY RESOLVED:** Qwen currently presents the cleaner public Apache-2.0/base path, but exact component-level rights evidence and Spec 003 dispositions for development evaluation, modification/derivation, redistribution, and any later training use remain to be computed from exact records. Apertus rights remain `CONDITIONAL` pending reconciliation of its gated AUP/terms with `FD-001` and the intended uses.
4. **PARTIALLY RESOLVED:** Apertus, Gemma 3 270M, and MedGemma require gated terms/access; no acceptance is authorized. The two Qwen frontier repositories have no equivalent gate identified in current read-only inspection. Any newly discovered gating changes must fail closed.
5. **RESOLVED:** primary ranking uses `COMMON_CORE_PRIMARY_RANKING`; modality-specific evidence is secondary and non-ranking, with no cross-track winner in Spec 005.
6. What exact canonical benchmark/metric slices are authorized for the baseline tournament?
7. **PARTIALLY RESOLVED / CANONICAL FLOOR PRESERVED:** zero-violation sentinel rules apply where already frozen by Spec 002, while selective risk, Arabic clinical parity, and lab extraction remain `NO_PASS_UNTIL_FROZEN` pending the canonical clinical/statistical evidence requirements. Exact statistical thresholds remain unresolved and must not be invented from candidate results.
8. **RESOLVED TARGET SET + CONTEXT + KV + TOKEN-BUDGET + PROMPT-PROCESSING + RUNTIME-IDENTITY POLICY / DETAILS PENDING:** `MASS_REACH_FIVE_TARGET_SET` freezes iPhone 17 Pro 12 GB, iPhone 13 4 GB, Galaxy A56 5G 8 GB, Galaxy A16 5G 4 GB, and Intel N100 + 8 GB x86-64 as required evidence targets. `8K_CORE_16K_STRESS` freezes `8192` tokens as the hard qualification context on all five, with required `16384`-token secondary stress evidence on 8-GB-class-or-higher targets where the pinned runtime supports it. `Q8_0_SYMMETRIC_KV_CORE` freezes symmetric `Q8_0` K/V cache for both tiers and prohibits asymmetric primary KV. `7K_PROMPT_1K_GENERATION` freezes `7168+1024` for core and `15360+1024` for stress, counts system/template tokens inside the serialized-prompt budget, and preserves the same generation allowance across candidates. `B512_U128_COLD_NO_REUSE` freezes logical batch `512`, physical ubatch `128`, and prohibits prompt/session/prefix state reuse for measured runs across all comparable candidates and frozen targets. `PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST` freezes one immutable llama.cpp core revision across all target paths and requires exact per-platform build manifests while prohibiting mutable/candidate-specific/post-result runtime substitution. The exact selected core SHA, concrete build manifests, tokenizer/template accounting implementation, performance/thermal/energy thresholds, peak-memory measurement, repetition/warm-up/aggregation rules, and target-specific hard-failure semantics remain unresolved.
9. **PARTIALLY RESOLVED:** `SUB_700MB_MASS_REACH` freezes a `700 MiB` hard ceiling for the complete minimum text/core bundle, `<=600 MiB` engineering target, `<=500 MiB` stretch target if hard gates pass, `<=2 GiB` peak-working-RAM engineering target at the now-frozen common 8K/Q8_0/7K+1K/512+128 cold condition, and 4-GB-class phone/resource evidence. Exact RAM hard gate/measurement method, latency, throughput, energy, and thermal rules remain unresolved.
10. **RESOLVED POLICY:** `DUAL_BUILD_BASELINE_AND_DEPLOYABLE` plus `Q4_FLOOR_SMALLEST_PASSING`; primary capability comparison uses a frozen reference build, while the canonical deployable GGUF is the smallest allowed Q5/Q4-class artifact that passes every hard gate. Sub-4-bit artifacts are excluded from the V1 `PRIMARY` canonical release. Exact reference precision and frozen conversion/calibration details remain pending.
11. **RESOLVED RUNTIME IDENTITY POLICY / VALUES PENDING:** `GGUF_LLAMA_CPP_CANONICAL` plus `PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST`; GGUF + llama.cpp is the canonical mass-distribution artifact/runtime family, one immutable core commit must be shared across all target paths, and platform-specific builds must be exact-manifest-bound. MLX/MLC/Core ML/native builds remain optional derivatives. The exact core commit SHA, conversion revision, compiler/toolchain versions, build/backend flags, wrapper/application identities, and produced runtime artifact identities remain to be frozen before execution.
12. What contamination/quarantine proof is required for every candidate/result path, including whether `MODIFICATION_OR_DERIVATION` contamination state may legitimately be `NOT_APPLICABLE` for exact model-weight quantization under the Spec 003 contract?
13. What is the exact public-benchmark access mechanism, and what payload access remains separately gated?
14. **RESOLVED POLICY:** `FULLY_ADMITTED_PRIMARY_ONLY`; unresolved/conditional candidates remain outside the frozen primary ranking manifest, and candidate-set freeze occurs only after admission reconciliation.
15. What compute/spend budget is permitted for the tournament, and which actions remain zero-spend/read-only until execution authorization?
16. What independent review and exact-head evidence must be present before any execution activation can be proposed?
17. **RESOLVED:** `QUALITY_FLOOR_THEN_SIZE_FIRST`; after all hard gates and the frozen minimum medical-quality floor pass, complete deployable package bytes are the first lexicographic ranking metric with `LOWER_BETTER`.

Bounded clarification session 1 on 2026-08-23 is complete at five accepted questions. Bounded clarification session 2 is complete at five accepted questions plus two explicit founder directives. Bounded clarification session 3 is complete at five accepted questions. Bounded clarification session 4 is in progress at one accepted question. The unresolved factual/evidence requirements above remain active and prevent the overall clarification lifecycle from being declared complete or advancing to `PLAN`.

## 18. Specification acceptance criteria

A future complete clarification artifact is acceptable only when independent review confirms that it:

- defines the tournament problem without selecting a winner;
- binds the canonical predecessor identities and founder decisions;
- preserves baseline-only/no-training scope;
- distinguishes admission shortlisting from frozen admission and execution manifest membership;
- carries Qwen3 0.6B and Qwen3.5 0.8B as the current ultra-compact primary-admission frontier without claiming that unlike quantization artifacts are directly comparable;
- preserves Apertus 0.5B as a conditional size comparator rather than laundering its gated AUP/terms into permissive eligibility;
- preserves SmolLM2 360M as an ultra-small control/conditional comparator without allowing English-primary upstream scope to bypass the Arabic clinical hard gate;
- makes permissive release-lineage compatibility an explicit gate without asserting unverified license compatibility;
- preserves MedGemma 4B PT as a medical reference/control rather than incorrectly forcing it into a V1 mass-distribution role it cannot satisfy under the current package/access contract;
- freezes `MASS_REACH_FIVE_TARGET_SET` while keeping execution/performance thresholds separately unresolved until pre-execution evidence design;
- requires evidence for iPhone 17 Pro 12 GB, iPhone 13 4 GB, Galaxy A56 5G 8 GB, Galaxy A16 5G 4 GB, and Intel N100 + 8 GB x86-64 without post-result target weakening;
- freezes `8K_CORE_16K_STRESS`, requiring an `8192`-token hard qualification context on all five targets and `16384`-token secondary stress evidence on 8-GB-class-or-higher targets where the pinned runtime supports it;
- freezes `Q8_0_SYMMETRIC_KV_CORE`, requiring symmetric `Q8_0` K/V cache for primary hard qualification and required stress evidence, prohibiting asymmetric primary KV, while keeping runtime/backend identity and measured memory/performance effects separately unresolved until pre-execution qualification;
- freezes `7K_PROMPT_1K_GENERATION`, requiring `7168` serialized-prompt + `1024` generation tokens for the 8K hard condition and `15360` + `1024` for the 16K stress condition, with system/template tokens counted inside the prompt ceiling and no candidate-specific reallocation;
- freezes `B512_U128_COLD_NO_REUSE`, requiring logical batch `512`, physical ubatch `128`, and no prompt/session/prefix cache reuse for measured qualification/stress runs, identically across comparable candidates and frozen targets;
- freezes `PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST`, requiring one immutable llama.cpp core commit across all comparable candidates/targets, exact platform build manifests, and no mutable/candidate-specific/post-result runtime substitution while keeping the exact core SHA/build values unresolved until separately reviewed pre-execution binding;
- enforces the `700 MiB` complete minimum text/core bundle ceiling under one honest, candidate-neutral accounting rule;
- treats `<=600 MiB`, `<=500 MiB`, and `<=2 GiB` as engineering/stretch targets exactly as frozen, without converting them into retrospective hard gates;
- uses canonical GGUF + immutable llama.cpp compatibility as the minimum mass-distribution path, with optional optimized derivatives kept semantically and evidentially separate;
- enforces `Q4_FLOOR_SMALLEST_PASSING` and prohibits a sub-4-bit V1 primary release from winning merely because it is smaller;
- applies `QUALITY_FLOOR_THEN_SIZE_FIRST` only after all non-compensable safety/provenance/license/minimum-medical-quality gates pass;
- keeps Hugging Face adoption/category-leadership KPIs outside the scientific ranking and claims boundary;
- preserves Spec 004 deterministic/fail-closed comparison semantics;
- records accepted clarification decisions without contradicting unresolved gates;
- resolves all clarification requirements that materially affect candidate admission, comparability, device qualification, execution planning, and exact-head review before advancing to `PLAN`;
- grants no model, weight, benchmark payload, private Gold, provider, PHI, gated-asset, runtime-execution, or tournament-execution authority.

No bounded clarification session is a declaration that the full clarification lifecycle is complete until every material unresolved requirement is reconciled and independently reviewed.

## 19. Exit and next lifecycle step

Current working state after bounded session 3 completion and `PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST` acceptance in bounded session 4 question 1:

```text
SPEC_005_SPECIFICATION=DEFINED_CANONICALLY
CLARIFICATION_SESSION_1=5_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_2=5_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_2_STATUS=COMPLETE_BOUNDED_SESSION
CLARIFICATION_SESSION_3=5_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_3_STATUS=COMPLETE_BOUNDED_SESSION
CLARIFICATION_SESSION_4=1_QUESTION_ACCEPTED
CLARIFICATION_SESSION_4_STATUS=IN_PROGRESS
UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY=LOCKED_BY_FOUNDER_DIRECTIVE
GLOBAL_HEALTH_AI_CATEGORY_LEADERSHIP=PRODUCT_AMBITION
PRIMARY_ADMISSION_FRONTIER=Qwen/Qwen3-0.6B-Base,Qwen/Qwen3.5-0.8B-Base
ULTRA_COMPACT_SIZE_LEADER_CONDITIONAL_CANDIDATE=swiss-ai/Apertus-v1.1-0.5B
APERTUS_GATED_AUP_TERMS=UNRESOLVED_CONDITIONAL
MEDICAL_REFERENCE_CONTROL=google/medgemma-4b-pt
SIZE_PRIORITY=QUALITY_FLOOR_THEN_SIZE_FIRST
MASS_REACH_PACKAGE_POLICY=SUB_700MB_MASS_REACH
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_HARD_CEILING=700_MiB
CANONICAL_MINIMUM_DISTRIBUTION_ARTIFACT=GGUF
CANONICAL_RUNTIME_FAMILY=LLAMA_CPP
V1_PRIMARY_QUANTIZATION_POLICY=Q4_FLOOR_SMALLEST_PASSING
SUB4BIT_PRIMARY_CANONICAL_RELEASE=PROHIBITED
DEVICE_EVIDENCE_POLICY=MASS_REACH_FIVE_TARGET_SET
FLAGSHIP_REPRESENTATIVE=Apple_iPhone_17_Pro_12GB
APPLE_LOW_RESOURCE_REPRESENTATIVE=Apple_iPhone_13_4GB
MODERN_MIDRANGE_ANDROID_REPRESENTATIVE=Samsung_Galaxy_A56_5G_8GB
LOW_RESOURCE_ANDROID_REPRESENTATIVE=Samsung_Galaxy_A16_5G_4GB
LOW_RESOURCE_LAPTOP_ENVELOPE=Intel_N100_8GB_x86_64
CONTEXT_EVIDENCE_POLICY=8K_CORE_16K_STRESS
COMMON_CORE_DEVICE_CONTEXT=8192_TOKENS
LOW_RESOURCE_HARD_CONTEXT=8192_TOKENS
SECONDARY_STRESS_CONTEXT=16384_TOKENS
SECONDARY_STRESS_SCOPE=8GB_CLASS_OR_HIGHER_AND_WHERE_RUNTIME_SUPPORTS
KV_CACHE_POLICY=Q8_0_SYMMETRIC_KV_CORE
HARD_QUALIFICATION_K_CACHE_TYPE=Q8_0
HARD_QUALIFICATION_V_CACHE_TYPE=Q8_0
STRESS_K_CACHE_TYPE=Q8_0
STRESS_V_CACHE_TYPE=Q8_0
ASYMMETRIC_KV_PRIMARY_QUALIFICATION=PROHIBITED
Q4_KV_PRIMARY_QUALIFICATION=NOT_FROZEN
CONTEXT_BUDGET_POLICY=7K_PROMPT_1K_GENERATION
CORE_TOTAL_CONTEXT_BUDGET=8192_TOKENS
CORE_MAX_SERIALIZED_PROMPT_BUDGET=7168_TOKENS
CORE_MAX_GENERATION_BUDGET=1024_TOKENS
STRESS_TOTAL_CONTEXT_BUDGET=16384_TOKENS
STRESS_MAX_SERIALIZED_PROMPT_BUDGET=15360_TOKENS
STRESS_MAX_GENERATION_BUDGET=1024_TOKENS
SERIALIZED_PROMPT_INCLUDES_SYSTEM_AND_TEMPLATE=YES
GENERATION_BUDGET_IDENTICAL_ACROSS_CANDIDATES=YES
PROMPT_PROCESSING_POLICY=B512_U128_COLD_NO_REUSE
LOGICAL_BATCH_SIZE=512
PHYSICAL_UBATCH_SIZE=128
PROMPT_CACHE_REUSE_FOR_MEASURED_RUNS=PROHIBITED
SESSION_STATE_REUSE_FOR_MEASURED_RUNS=PROHIBITED
PREFIX_CACHE_REUSE_FOR_MEASURED_RUNS=PROHIBITED
BATCH_PROFILE_IDENTICAL_ACROSS_CANDIDATES=YES
BATCH_PROFILE_IDENTICAL_ACROSS_DEVICE_TARGETS=YES
RUNTIME_IDENTITY_POLICY=PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST
LLAMA_CPP_CORE_REVISION=IMMUTABLE_COMMIT_REQUIRED
EXACT_LLAMA_CPP_CORE_SHA=UNRESOLVED_VALUE
MUTABLE_MASTER_OR_LATEST=PROHIBITED
SAME_CORE_REVISION_ACROSS_ALL_TARGETS=REQUIRED
PLATFORM_BUILD_MANIFEST=REQUIRED
COMPILER_AND_BUILD_FLAGS_PINNED=REQUIRED
PLATFORM_WRAPPER_IDENTITY_PINNED=REQUIRED
CANDIDATE_SPECIFIC_RUNTIME_REVISION=PROHIBITED
POST_RESULT_RUNTIME_SUBSTITUTION=PROHIBITED
PLAN_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
```

Acceptance of the runtime-identity method does **not** select a concrete llama.cpp execution commit and does **not** complete the full clarification lifecycle. Remaining factual/evidence requirements must be reconciled and independently reviewed before a transition to `PLAN` can be proposed.

Clarification is explicitly authorized only within its bounded lifecycle. This session does not authorize planning, implementation, live tournament execution, model access, model-weight retrieval, benchmark payload access, runtime execution, winner selection, or any other later lifecycle stage.
