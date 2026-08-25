# Spec 005 — Base Model Tournament
> **Post-implementation reconciliation — 2026-08-25**
> **Canonical implementation:** `5e35cd423c54ce743b9b305287971a97eeeb7a64` (PR #36 merged, tree `5b823d20fd1106669e1b79af4d301d15c5e4e8dd`)
> **Historical note:** State `AUTHORIZED_TO_SPECIFY` and planning-branch `spec/005-clarify` below are pre-implementation. The deterministic control plane (A1–A15 validators, synthetic fixtures) is now canonical on `main`. Lifecycle text below is preserved as historical evidence; see tasks.md reconciliation and this branch for post-implementation truth. No model/benchmark/Private Gold/PHI/device/spend execution authority is granted by this reconciliation.



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

**Bounded session 4 — complete (5/5)**

- Q: How must the canonical llama.cpp runtime identity be bound across iOS, Android, and x86-64 device qualification? → A: `PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST` — require one exact immutable llama.cpp core commit across all comparable candidates and all five frozen targets; prohibit mutable `master`/`main`/`latest` identities and candidate-specific or post-result runtime revision substitution; require a platform build manifest that binds the shared core commit, compiler/toolchain, relevant build flags/backend choices, target architecture/ABI, wrapper/application identity where applicable, and produced runtime/build artifact identity when available. This freezes the identity method only; the exact core commit SHA and concrete platform build values remain unresolved pre-execution evidence requirements.
- Q: How must peak memory be measured across the frozen iOS, Android, and x86-64 qualification paths? → A: `PLATFORM_NATIVE_PEAK_MEMORY` — use iOS physical-footprint peak, Android time-resolved RSS peak with total PSS as secondary context, and Linux cgroup-v2 `memory.peak` for the full required qualification process set. Record pre-model-load baseline, absolute peak bytes, and peak delta; treat OS memory termination as a hard failure; prohibit mixing the unlike raw platform-native memory metrics into a cross-platform ranking metric.
- Q: What absolute RAM hard ceiling must the common 8K Core qualification satisfy? → A: `2G_CORE_HARD_CAP` — every frozen target must remain at or below an absolute platform-native peak of `2 GiB` (`2147483648` bytes) for the full required qualification process set under the common 8K condition. Absolute peak is the hard-gate input; baseline delta is diagnostic only; OS/LMK/OOM memory termination is a hard failure. Required 16K stress evidence still records peak memory and fails on OS memory termination, but no additional absolute 16K RAM ceiling is frozen by this question.
- Q: How must performance timing be decomposed so cold-start cost and ready-state model performance remain separately comparable? → A: `COMPONENT_TIMING_COLD_AND_READY` — record cold-start-to-first-token and model-load time, plus ready-state TTFT, prefill tokens/second, decode tokens/second, and end-to-end response time. Use identical timing boundaries across candidates and targets; exclude model load from ready-state TTFT while including model load in cold-start-to-first-token; prohibit prompt/session/prefix-cache reuse and candidate-specific timing boundaries. This freezes the component timing measurement policy only. Performance hard thresholds remain unresolved and must be frozen before execution.
- Q: What repetition, warm-up, aggregation, and failed-run handling policy must measured performance qualification use? → A: `FIVE_FRESH_RUNS_MEDIAN_WITH_WORST_CASE` — require five measured runs per candidate/target/condition; each measured run starts from a fresh process, includes a fresh model load, and contains exactly one measured request after load; use no non-measured warm-up requests; retain all raw runs, record the median of five as the primary aggregate and the worst-case run separately; retain failed or terminated runs as failures, prohibit replacement or post-hoc exclusion, prohibit candidate- or target-specific run counts, and record thermal state before each run. This freezes repetition and aggregation semantics only. Thermal cooldown policy and numeric performance hard thresholds remain unresolved.

**Bounded session 5 — complete (5/5)**

- Q: What thermal-readiness policy must govern the five measured runs so candidates are not compared from materially different throttling states? → A: `PLATFORM_NATIVE_THERMAL_READY_GATE` — record platform-native thermal state before and after every measured run; require a platform-native thermal-ready determination before a measured run may start; prohibit starting while known active throttling is present; require the thermal signal identity to be pinned before execution; use cooldown as needed until thermal-ready rather than treating a fixed sleep as proof of readiness; predeclare run order; prohibit candidate-specific thermal exceptions and post-result thermal-rule changes; record thermal termination or OS throttling events. This freezes the thermal-readiness method only. Exact platform signal mappings/ready thresholds and numeric performance hard thresholds remain unresolved.
- Q: What energy-measurement policy must govern measured runs across iOS, Android, and the low-resource laptop path? → A: `PLATFORM_NATIVE_ENERGY_PER_RUN` — require an energy record for every measured run over the full cold-run window; record pre-run baseline, post-run record, and energy delta where supported; pin the energy signal and tool/meter identity before execution; require the same method within a target across all candidates; prohibit candidate-specific or post-result energy-method changes; preserve raw unit semantics and uncertainty where available; prohibit cross-platform raw-energy ranking and compare raw energy only within the same target using the same method. Missing or failed energy capture is `EVIDENCE_INCOMPLETE`, and failed-run energy evidence is retained. This freezes the energy-measurement method only; exact tools/meters and calibration/uncertainty details remain unresolved, while Q3 separately freezes the V1 qualification role.
- Q: What qualification role should energy evidence have in V1 once per-run measurement is required? → A: `ENERGY_REQUIRED_EVIDENCE_NO_V1_ABSOLUTE_HARD_GATE` — energy evidence remains required and missing energy evidence is `INCOMPLETE`, but V1 has no absolute raw-energy hard ceiling and raw energy values cannot directly disqualify a candidate. Same-target/same-method energy comparison is allowed; cross-platform raw-energy comparison remains prohibited. Energy may enter secondary ranking only if that role is predeclared and limited to same-target/same-method evidence. Energy cannot compensate for safety, quality, package, or Core-memory hard-gate failure. Candidate-specific or post-result energy thresholds are prohibited, and any future energy hard gate requires separate canonical evidence before results are observed. Numeric performance hard thresholds remain unresolved.
- Q: What candidate-neutral device/runtime failure semantics must be frozen before numeric performance thresholds so five-run aggregation cannot be retrofitted after failures are observed? → A: `UNIVERSAL_FATAL_FAILURES_AND_FAIL_CLOSED_EVIDENCE` — classify runtime initialization failure, canonical artifact load failure, inability of a correctly configured candidate/runtime to execute the required Core condition, process crash/abnormal termination, OS non-memory forced termination, measured-request noncompletion, and known unauthorized runtime/backend/artifact fallback as `HARD_FAIL`. Missing or malformed required measurement evidence, an unprovable runtime/artifact identity, or a wrong/unprovable run configuration is `INCOMPLETE` rather than a candidate failure. Mid-run thermal throttling is recorded but is not an automatic hard failure unless it produces an independently frozen fatal event. Any hard-fail run makes its candidate/target/condition `HARD_FAIL`; any incomplete run makes the condition `INCOMPLETE`; a valid median-of-five requires five complete numeric runs and partial-median substitution is prohibited. Failure-signal identities and the noncompletion watchdog must be pinned before execution, while the exact watchdog timeout and numeric performance hard thresholds remain unresolved. Candidate-specific failure exceptions and post-result failure-rule changes are prohibited.
- Q: What performance-threshold policy must be frozen before execution without inventing candidate-result-derived latency or throughput numbers? → A: `PREDECLARED_TARGET_USABILITY_PERFORMANCE_GATES` — performance hard gates are required before execution, but exact numeric values remain unresolved until supported by documented candidate-independent usability evidence. Cold-start-to-first-token, ready-state TTFT, and decode tokens/second must receive hard gates; prefill throughput, model-load time, and end-to-end response time remain recorded/secondary unless separately frozen as hard gates. Thresholds are identical across candidates on the same target; target-specific thresholds are allowed only when predeclared and justified before candidate results. Candidate-specific thresholds, candidate-result-derived thresholds, post-result threshold changes, and post-result target-specific relaxation are prohibited. Median-of-five is the primary threshold aggregate, worst-case evidence remains mandatory, and `HARD_FAIL`/`INCOMPLETE` runs cannot be inserted into or removed from a numeric aggregate to rescue qualification.

**Bounded session 6 — in progress (4/5)**

- Q: What benchmark/metric scope may be carried forward toward the future baseline tournament without silently turning public or reference assets into selectable execution data? → A: `CANONICAL_PUBLIC_SLICE_MANIFEST_ONLY` — only canonical Spec 001 benchmark records that are verified, public, development-scoped, and sufficiently artifact-bound may be considered for a future executable baseline slice manifest. The current public-development registry scope is `healthbench_core`, `healthbench_consensus`, `healthbench_hard`, `healthbench_professional`, `medxpertqa`, and `pubmedqa`; this is a metadata scope, not payload-access or execution authorization and not by itself a selectable ranking manifest. Any future executable manifest must bind exact benchmark ID, artifact/split identity, quarantine purpose, allowed metric IDs/directions, and selection eligibility before execution. Public canonical test splits remain external-evaluation-only and cannot select a model. `medxpertqa` multimodal slices remain secondary non-ranking evidence under `COMMON_CORE_PRIMARY_RANKING`; its text dev split may become selectable only through an explicit pre-execution `DEV`/`CHECKPOINT_SELECTION` mapping. HealthBench and PubMedQA do not become selectable merely because their registry records are `PUBLIC` + `DEVELOPMENT`; their exact selection-purpose mapping remains unresolved. `REFERENCE_ONLY`, mixed/unbound, unresolved-license, gated, private, and private-Gold assets remain outside executable selection scope unless separately reconciled and authorized. Candidate-specific slice selection and post-result slice addition/removal are prohibited. This clarification authorizes read-only registry/metadata inspection only; benchmark payload access/execution remains unauthorized.
- Q: What quarantine-purpose semantics must each future benchmark slice satisfy so development, model-selection, and external-evaluation evidence cannot be relabeled after candidate results? → A: `PREDECLARED_QUARANTINE_PURPOSE_PER_SLICE` — every executable slice must have exactly one canonical purpose frozen before payload access or execution. Baseline purposes are `DEV`, `CHECKPOINT_SELECTION`, and `PUBLIC_EXTERNAL_EVAL`; selection use requires the canonical source class to permit it and `can_select_model=true`. Public canonical test splits remain `PUBLIC_EXTERNAL_EVAL` and cannot select a model. Private Gold remains `PRIVATE_GOLD_ONLY`, cannot select or train, and is not authorized here. `REFERENCE_ONLY`, unbound, or unresolved-purpose assets are not executable. The same slice-purpose mapping must apply across candidates; candidate-specific mapping, post-result remapping, or promotion of external-evaluation evidence into selection evidence is prohibited. Exact purpose mappings for MedXpertQA text dev, HealthBench, and PubMedQA remain unresolved. Benchmark payload access/execution remains unauthorized.
- Q: What access preconditions must a future public benchmark payload satisfy before any payload bytes may be obtained, cached, or executed? → A: `METADATA_FIRST_EXACT_ARTIFACT_BINDING_BEFORE_ACCESS` — read-only public-source metadata inspection remains allowed, but payload access requires separate explicit authorization plus an exact artifact/split identity, immutable source revision or equivalent immutable digest, resolved license/access class, a frozen canonical quarantine purpose, and a contamination disposition. Mutable `latest`/unpinned or otherwise unbound payload access is prohibited. Gated, private, and Private Gold payloads remain inaccessible without separate authority; external-submission-only ground truth does not become local Gold. Local payload cache/copy creation is not authorized by this clarification. Any later access mechanism must preserve canonical artifact identity, must not substitute a post-access artifact or candidate-specific payload version, and an access failure or identity mismatch fails closed as `INCOMPLETE`. Benchmark payload access and execution authorities remain `NONE`.
- Q: What contamination proof must govern clean-required uses, including whether exact model-weight quantization may use `NOT_APPLICABLE` under Spec 003? → A: `USE_CLASS_SPECIFIC_FAIL_CLOSED_CONTAMINATION_BINDING` — preserve the canonical Spec 003 rule that `MODIFICATION_OR_DERIVATION`, `TEACHER_OR_SYNTHETIC_GENERATION`, and `TRAINING_OR_ADAPTATION` are clean-contamination-required uses. For such uses, only `ASSESSED_CLEAN` or evidence-backed `NOT_APPLICABLE` can satisfy the contamination gate; `NOT_APPLICABLE` is valid only when the exact path is proven truly outside the contamination condition and cannot be self-asserted. Exact model-weight quantization may use `NOT_APPLICABLE` only for a proven weight-only, data-free transform bound to exact source-weight identity, exact transform/toolchain identity, and frozen transform flags, with no calibration/imatrix, benchmark/Gold, training/dev, teacher, or provider-output payload input. Any quantization using calibration, imatrix, or other data requires contamination assessment instead. Pending/not-assessed contamination blocks clean-required use; known overlap/high-risk contamination prohibits it. Candidate-specific contamination exceptions and post-result reclassification are prohibited. Exact per-candidate/per-slice dispositions remain pending; no weight, conversion, benchmark-payload, or Gold authority is granted.

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

`FD-002=FLAGSHIP_PLUS_MODERN_MIDRANGE` establishes the V1 target tier, clarification freezes `NAMED_DEVICE_PLUS_RESOURCE_ENVELOPE` as the evidence strategy, the founder further establishes `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY` plus `SUB_700MB_MASS_REACH`, bounded clarification session 3 freezes `MASS_REACH_FIVE_TARGET_SET`, `8K_CORE_16K_STRESS`, `Q8_0_SYMMETRIC_KV_CORE`, `7K_PROMPT_1K_GENERATION`, and `B512_U128_COLD_NO_REUSE`, bounded clarification session 4 freezes `PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST`, `PLATFORM_NATIVE_PEAK_MEMORY`, `2G_CORE_HARD_CAP`, `COMPONENT_TIMING_COLD_AND_READY`, and `FIVE_FRESH_RUNS_MEDIAN_WITH_WORST_CASE`, and bounded clarification session 5 questions 1–5 freeze `PLATFORM_NATIVE_THERMAL_READY_GATE`, `PLATFORM_NATIVE_ENERGY_PER_RUN`, `ENERGY_REQUIRED_EVIDENCE_NO_V1_ABSOLUTE_HARD_GATE`, `UNIVERSAL_FATAL_FAILURES_AND_FAIL_CLOSED_EVIDENCE`, and `PREDECLARED_TARGET_USABILITY_PERFORMANCE_GATES` as thermal/energy/runtime/performance qualification policies.

The frozen mass-reach package, target, context, KV, token-budget, prompt-processing, runtime-identity, memory-measurement, 8K Core memory-gate, timing, repetition/aggregation, thermal-readiness, energy-measurement, V1 energy-qualification, device/runtime failure, and performance-threshold policy is:

```text
MINIMUM_TEXT_CORE_BUNDLE_HARD_CEILING=700_MiB
MINIMUM_TEXT_CORE_BUNDLE_ENGINEERING_TARGET=600_MiB_OR_LESS
MINIMUM_TEXT_CORE_BUNDLE_STRETCH_TARGET=500_MiB_OR_LESS_IF_ALL_HARD_GATES_STILL_PASS
PEAK_WORKING_RAM_ENGINEERING_TARGET=2_GiB_OR_LESS_AT_FROZEN_SHORT_CONTEXT
CORE_8K_MEMORY_GATE=2G_CORE_HARD_CAP
CORE_8K_PEAK_MEMORY_HARD_CEILING=2_GiB
CORE_8K_PEAK_MEMORY_HARD_CEILING_BYTES=2147483648
CORE_8K_HARD_CEILING_APPLIES_TO_ALL_FIVE_TARGETS=YES
CORE_8K_HARD_CEILING_USES_PLATFORM_NATIVE_PRIMARY_METRIC=YES
CORE_8K_MEMORY_TERMINATION=HARD_FAIL
CORE_8K_PEAK_DELTA=DIAGNOSTIC_ONLY
CORE_8K_ABSOLUTE_PEAK=HARD_GATE_INPUT
STRESS_16K_PEAK_MEMORY=RECORDED
STRESS_16K_OS_MEMORY_TERMINATION=HARD_FAIL
STRESS_16K_ABSOLUTE_RAM_HARD_CEILING=NOT_FROZEN
CANDIDATE_SPECIFIC_RAM_EXCEPTION=PROHIBITED
POST_RESULT_RAM_CEILING_CHANGE=PROHIBITED
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
MEMORY_MEASUREMENT_POLICY=PLATFORM_NATIVE_PEAK_MEMORY
IOS_PRIMARY_PEAK_METRIC=LEDGER_PHYS_FOOTPRINT_PEAK
IOS_OS_MEMORY_TERMINATION=HARD_FAIL
ANDROID_PRIMARY_PEAK_METRIC=RSS_TRACE_PEAK
ANDROID_SECONDARY_MEMORY_METRIC=TOTAL_PSS
ANDROID_LMK_OR_OOM_TERMINATION=HARD_FAIL
LINUX_PRIMARY_PEAK_METRIC=CGROUP_V2_MEMORY_PEAK
LINUX_OOM_TERMINATION=HARD_FAIL
FULL_QUALIFICATION_PROCESS_SET_ACCOUNTED=YES
MEASUREMENT_WINDOW=FULL_COLD_QUALIFICATION_RUN
BASELINE_BEFORE_MODEL_LOAD=RECORDED
PEAK_ABSOLUTE_BYTES=RECORDED
PEAK_DELTA_FROM_BASELINE=RECORDED
CROSS_PLATFORM_RAW_METRIC_RANKING=PROHIBITED
PERFORMANCE_MEASUREMENT_POLICY=COMPONENT_TIMING_COLD_AND_READY
COLD_START_TO_FIRST_TOKEN=RECORDED
MODEL_LOAD_TIME=RECORDED
READY_STATE_TTFT=RECORDED
PREFILL_TOKENS_PER_SECOND=RECORDED
DECODE_TOKENS_PER_SECOND=RECORDED
END_TO_END_RESPONSE_TIME=RECORDED
TIMING_BOUNDARIES_IDENTICAL_ACROSS_CANDIDATES=YES
TIMING_BOUNDARIES_IDENTICAL_ACROSS_TARGETS=YES
MODEL_LOAD_TIME_EXCLUDED_FROM_READY_STATE_TTFT=YES
COLD_START_TO_FIRST_TOKEN_INCLUDES_MODEL_LOAD=YES
PROMPT_SESSION_PREFIX_CACHE_REUSE=PROHIBITED
CANDIDATE_SPECIFIC_TIMING_BOUNDARIES=PROHIBITED
PERFORMANCE_REPETITION_POLICY=FIVE_FRESH_RUNS_MEDIAN_WITH_WORST_CASE
MEASURED_RUNS_PER_CANDIDATE_TARGET_CONDITION=5
EACH_MEASURED_RUN_STARTS_FROM_FRESH_PROCESS=YES
EACH_MEASURED_RUN_INCLUDES_FRESH_MODEL_LOAD=YES
MEASURED_REQUESTS_PER_FRESH_LOAD=1
NON_MEASURED_WARMUP_REQUESTS=0
PRIMARY_AGGREGATION=MEDIAN_OF_FIVE
WORST_CASE_RUN=RECORDED
ALL_RAW_RUNS=RETAINED
FAILED_OR_TERMINATED_RUNS=RETAINED_AS_FAILURE
FAILED_RUN_REPLACEMENT=PROHIBITED
POST_HOC_RUN_EXCLUSION=PROHIBITED
CANDIDATE_SPECIFIC_RUN_COUNT=PROHIBITED
TARGET_SPECIFIC_RUN_COUNT=PROHIBITED
THERMAL_CONTROL_POLICY=PLATFORM_NATIVE_THERMAL_READY_GATE
THERMAL_STATE_BEFORE_EACH_RUN=RECORDED
THERMAL_STATE_AFTER_EACH_RUN=RECORDED
MEASURED_RUN_START_REQUIRES_THERMAL_READY=YES
KNOWN_ACTIVE_THROTTLING_AT_RUN_START=PROHIBITED
THERMAL_READINESS_USES_PLATFORM_NATIVE_SIGNAL=YES
THERMAL_SIGNAL_IDENTITY_MUST_BE_PINNED=YES
IOS_THERMAL_STATE=PLATFORM_NATIVE_RECORDED
ANDROID_THERMAL_STATUS=PLATFORM_NATIVE_RECORDED
LAPTOP_CPU_THERMAL_TELEMETRY=RECORDED
COOLDOWN_BETWEEN_RUNS=AS_NEEDED_UNTIL_THERMAL_READY
FIXED_SLEEP_AS_THERMAL_PROOF=PROHIBITED
RUN_ORDER_PREDECLARED=REQUIRED
CANDIDATE_SPECIFIC_THERMAL_EXCEPTION=PROHIBITED
POST_RESULT_THERMAL_RULE_CHANGE=PROHIBITED
THERMAL_TERMINATION_OR_OS_THROTTLING_EVENT=RECORDED
EXACT_PLATFORM_THERMAL_READY_THRESHOLDS=NOT_YET_FROZEN
ENERGY_MEASUREMENT_POLICY=PLATFORM_NATIVE_ENERGY_PER_RUN
ENERGY_MEASUREMENT_REQUIRED_FOR_EACH_MEASURED_RUN=YES
ENERGY_WINDOW_MATCHES_FULL_COLD_RUN=YES
PRE_RUN_ENERGY_BASELINE=RECORDED
POST_RUN_ENERGY_RECORD=RECORDED
RUN_ENERGY_DELTA=RECORDED_WHERE_SUPPORTED
ENERGY_SIGNAL_IDENTITY_MUST_BE_PINNED=YES
ENERGY_TOOL_OR_METER_IDENTITY_MUST_BE_PINNED=YES
SAME_ENERGY_METHOD_WITHIN_TARGET_ACROSS_CANDIDATES=REQUIRED
CANDIDATE_SPECIFIC_ENERGY_METHOD=PROHIBITED
POST_RESULT_ENERGY_METHOD_CHANGE=PROHIBITED
IOS_ENERGY_EVIDENCE=PLATFORM_NATIVE_OR_PREDECLARED_VALIDATED_METER
ANDROID_ENERGY_EVIDENCE=PLATFORM_NATIVE_OR_PREDECLARED_VALIDATED_METER
LAPTOP_ENERGY_EVIDENCE=PLATFORM_NATIVE_OR_PREDECLARED_VALIDATED_METER
RAW_ENERGY_UNIT_AND_SEMANTICS=RECORDED
ENERGY_MEASUREMENT_UNCERTAINTY=RECORDED_WHERE_AVAILABLE
CROSS_PLATFORM_RAW_ENERGY_RANKING=PROHIBITED
ENERGY_COMPARISON_SCOPE=SAME_TARGET_SAME_METHOD_ONLY
FAILED_OR_MISSING_ENERGY_CAPTURE=EVIDENCE_INCOMPLETE
FAILED_RUN_ENERGY_RECORD_RETAINED=YES
ENERGY_QUALIFICATION_POLICY=ENERGY_REQUIRED_EVIDENCE_NO_V1_ABSOLUTE_HARD_GATE
ENERGY_EVIDENCE_REQUIRED=YES
MISSING_ENERGY_EVIDENCE=INCOMPLETE
V1_ABSOLUTE_ENERGY_HARD_CEILING=NONE
ENERGY_HARD_DISQUALIFICATION_BY_RAW_VALUE=PROHIBITED
SAME_TARGET_ENERGY_COMPARISON=ALLOWED
CROSS_PLATFORM_RAW_ENERGY_COMPARISON=PROHIBITED
ENERGY_MAY_ENTER_SECONDARY_RANKING=ONLY_IF_PREDECLARED
ENERGY_SECONDARY_RANKING_SCOPE=SAME_TARGET_SAME_METHOD_ONLY
ENERGY_CANNOT_COMPENSATE_FOR_SAFETY_FAILURE=YES
ENERGY_CANNOT_COMPENSATE_FOR_QUALITY_FAILURE=YES
ENERGY_CANNOT_COMPENSATE_FOR_PACKAGE_FAILURE=YES
ENERGY_CANNOT_COMPENSATE_FOR_CORE_MEMORY_FAILURE=YES
POST_RESULT_ENERGY_THRESHOLD_CREATION=PROHIBITED
CANDIDATE_SPECIFIC_ENERGY_THRESHOLD=PROHIBITED
FUTURE_ENERGY_HARD_GATE_REQUIRES_SEPARATE_CANONICAL_EVIDENCE=YES
DEVICE_RUNTIME_FAILURE_POLICY=UNIVERSAL_FATAL_FAILURES_AND_FAIL_CLOSED_EVIDENCE
RUNTIME_INITIALIZATION_FAILURE=HARD_FAIL
CANONICAL_ARTIFACT_LOAD_FAILURE=HARD_FAIL
REQUIRED_CORE_CONDITION_EXECUTION_FAILURE=HARD_FAIL
PROCESS_CRASH_OR_ABNORMAL_TERMINATION=HARD_FAIL
OS_NON_MEMORY_FORCED_TERMINATION=HARD_FAIL
MEASURED_REQUEST_NONCOMPLETION=HARD_FAIL
UNAUTHORIZED_RUNTIME_BACKEND_OR_ARTIFACT_FALLBACK=HARD_FAIL
MISSING_REQUIRED_MEASUREMENT_EVIDENCE=INCOMPLETE
MALFORMED_REQUIRED_MEASUREMENT_EVIDENCE=INCOMPLETE
UNPROVABLE_RUNTIME_OR_ARTIFACT_IDENTITY=INCOMPLETE
WRONG_OR_UNPROVABLE_RUN_CONFIGURATION=INCOMPLETE
MID_RUN_THERMAL_THROTTLING=RECORDED_NOT_AUTOMATIC_HARD_FAIL
FIVE_RUN_SET_WITH_ANY_HARD_FAIL=HARD_FAIL
FIVE_RUN_SET_WITH_ANY_INCOMPLETE_RUN=INCOMPLETE
MEDIAN_OF_FIVE_REQUIRES_FIVE_COMPLETE_NUMERIC_RUNS=YES
PARTIAL_MEDIAN_SUBSTITUTION=PROHIBITED
TARGET_NATIVE_FAILURE_SIGNAL_IDENTITY=PINNED_BEFORE_EXECUTION
NONCOMPLETION_DETECTION_WATCHDOG=PREEXECUTION_REQUIRED
EXACT_WATCHDOG_TIMEOUT=NOT_YET_FROZEN
CANDIDATE_SPECIFIC_FAILURE_EXCEPTION=PROHIBITED
POST_RESULT_FAILURE_RULE_CHANGE=PROHIBITED
PERFORMANCE_THRESHOLD_POLICY=PREDECLARED_TARGET_USABILITY_PERFORMANCE_GATES
PERFORMANCE_HARD_GATES_REQUIRED_BEFORE_EXECUTION=YES
EXACT_NUMERIC_PERFORMANCE_THRESHOLDS=NOT_YET_FROZEN
PERFORMANCE_HARD_THRESHOLDS=NOT_YET_FROZEN
THRESHOLDS_MUST_BE_FROZEN_BEFORE_CANDIDATE_RESULTS=YES
THRESHOLD_EVIDENCE_BASIS_MUST_BE_DOCUMENTED=YES
SAME_TARGET_THRESHOLDS_IDENTICAL_ACROSS_CANDIDATES=YES
CANDIDATE_SPECIFIC_PERFORMANCE_THRESHOLD=PROHIBITED
POST_RESULT_PERFORMANCE_THRESHOLD_CHANGE=PROHIBITED
TARGET_SPECIFIC_THRESHOLDS=ALLOWED_WHEN_PREDECLARED_AND_JUSTIFIED
TARGET_SPECIFIC_THRESHOLD_RELAXATION_AFTER_RESULTS=PROHIBITED
COLD_START_TO_FIRST_TOKEN_HARD_GATE=REQUIRED
READY_STATE_TTFT_HARD_GATE=REQUIRED
DECODE_TOKENS_PER_SECOND_HARD_GATE=REQUIRED
PREFILL_TOKENS_PER_SECOND=RECORDED_AND_SECONDARY_UNLESS_SEPARATELY_FROZEN
MODEL_LOAD_TIME=RECORDED_COMPONENT
END_TO_END_RESPONSE_TIME=RECORDED_AND_SECONDARY_UNLESS_SEPARATELY_FROZEN
PRIMARY_THRESHOLD_AGGREGATE=MEDIAN_OF_FIVE
WORST_CASE_RUN=MANDATORY_GUARDRAIL_EVIDENCE
HARD_FAIL_OR_INCOMPLETE_RUN_CANNOT_ENTER_NUMERIC_AGGREGATE=YES
PERFORMANCE_THRESHOLD_SOURCE=CANDIDATE_INDEPENDENT_USABILITY_EVIDENCE_REQUIRED
CANDIDATE_RESULT_DERIVED_THRESHOLD=PROHIBITED
PERFORMANCE_CAN_NEVER_COMPENSATE_FOR_SAFETY_FAILURE=YES
PERFORMANCE_CAN_NEVER_COMPENSATE_FOR_QUALITY_FAILURE=YES
PERFORMANCE_CAN_NEVER_COMPENSATE_FOR_PACKAGE_FAILURE=YES
PERFORMANCE_CAN_NEVER_COMPENSATE_FOR_CORE_MEMORY_FAILURE=YES
PERFORMANCE_CAN_NEVER_COMPENSATE_FOR_RUNTIME_HARD_FAIL=YES
```

Spec 005 must eventually bind execution evidence for every frozen target without silently weakening the resource class after candidate results are observed. A physical-device substitution is permissible only through a separately reviewed pre-result clarification that preserves the same or stricter resource class and records the reason and new exact identity.

Every candidate must eventually qualify at the same `8192`-token hard context on all five frozen targets using symmetric `Q8_0` K/V cache, the same `7168` serialized-prompt / `1024` generation ceiling, and the same cold `512/128` prompt-processing profile with no cross-run or precomputed prompt-state reuse. The absolute platform-native peak for the full required qualification process set must not exceed `2 GiB` on any of those five 8K Core target runs. The `16384`-token tier is required secondary stress evidence on 8-GB-class-or-higher targets where the pinned runtime supports it and uses the same symmetric Q8_0 policy, `15360` serialized-prompt / `1024` generation ceiling, and cold `512/128` prompt-processing profile. The 16K tier records peak memory and fails on OS memory termination, but no absolute 16K RAM ceiling is frozen here. The serialized-prompt budget includes system and template tokens; unused generation allowance cannot expand the prompt ceiling.

All comparable device evidence must use one exact immutable llama.cpp core commit. Platform-specific builds may differ only where required by iOS, Android, or x86-64 toolchains, and every such path must carry a reproducible exact build manifest. The exact core SHA and concrete platform build values are not selected by this policy and remain unresolved pre-execution evidence requirements.

Peak-memory evidence must use the frozen platform-native method across the full required qualification process set: iOS physical-footprint peak, Android time-resolved RSS peak with total PSS as secondary context, and Linux cgroup-v2 `memory.peak`. The pre-load baseline, absolute peak, and delta are all recorded. OS memory termination is a hard failure. A Windows weak-laptop path requires a separately reviewed Windows-native measurement binding before execution; Linux cgroup evidence must not be silently reused as Windows evidence.

Performance evidence must preserve both cold-start cost and ready-state execution behavior. `COLD_START_TO_FIRST_TOKEN` includes model load; `READY_STATE_TTFT` excludes model load. Model load time, ready-state TTFT, prefill throughput, decode throughput, and end-to-end response time must be recorded with identical timing boundaries across comparable candidates and frozen targets. Prompt/session/prefix-cache reuse is prohibited for measured timing, and no candidate may receive a custom timing boundary. Each candidate/target/condition uses exactly five measured fresh-process runs, each with a fresh load and one measured request, no non-measured warm-up requests, median-of-five primary aggregation, worst-case recording, all raw runs retained, and failed/terminated runs retained as failures without replacement or post-hoc exclusion. Under `UNIVERSAL_FATAL_FAILURES_AND_FAIL_CLOSED_EVIDENCE`, the median-of-five is valid only when all five runs complete with the required numeric evidence; any hard-fail run makes the condition `HARD_FAIL`, and any incomplete run makes the condition `INCOMPLETE`. Under `PREDECLARED_TARGET_USABILITY_PERFORMANCE_GATES`, numeric hard-gate values must be supported by documented candidate-independent usability evidence and frozen before candidate results; thresholds must be identical across candidates within a target, while target-specific values are permitted only when predeclared and justified. Candidate-specific thresholds, candidate-result-derived thresholds, post-result threshold changes, and post-result target-specific relaxation are prohibited. Each run records platform-native thermal state before and after execution; a measured run may start only after the frozen platform-native signal determines thermal readiness, and known active throttling at run start is prohibited. Cooldown is as-needed until readiness rather than a fixed-sleep proof. Exact numeric performance thresholds, the exact noncompletion watchdog timeout, and exact platform thermal-ready signal mappings/thresholds remain unresolved and must be frozen before execution.

Energy evidence is required for every measured run over the full cold-run window. Each target must use one pinned platform-native or predeclared validated meter/tool method consistently across all candidates; pre-run baseline, post-run record, raw unit semantics, and run delta where supported must be retained. Candidate-specific or post-result method changes are prohibited. Raw energy values may be compared only within the same target using the same method; cross-platform raw-energy ranking is prohibited. V1 intentionally has no absolute raw-energy hard ceiling, so raw energy values do not directly disqualify a candidate. Energy may enter secondary ranking only through a predeclared same-target/same-method rule. Exact tool/meter identities and calibration/uncertainty details remain unresolved pre-execution requirements; any future energy hard gate requires separate canonical evidence before results are observed.

Runtime/device failure classification is candidate-neutral and precedes numeric performance thresholding. A correctly configured required run that cannot initialize the runtime, load the canonical artifact, execute the frozen Core condition, complete the measured request normally, or remain alive without crash/OS non-memory forced termination is a hard qualification failure. A known silent or explicit fallback to an unauthorized runtime, backend, or artifact is also a hard failure because the run no longer tests the frozen contract. By contrast, missing or malformed telemetry, an unprovable identity, or a wrong/unprovable run configuration makes the evidence `INCOMPLETE`; it must not be relabeled as a favorable result or as a candidate failure. Mid-run thermal throttling is retained as evidence and may affect measured performance, but is not itself an automatic hard failure unless it causes another frozen fatal event. Exact platform failure-signal identities and an operational noncompletion watchdog must be pinned before execution; the exact watchdog timeout remains unresolved and is separate from numeric performance pass/fail thresholds.

The `700 MiB` package ceiling and `2 GiB` absolute peak ceiling for the common 8K Core qualification condition are hard qualification boundaries. The `<=600 MiB` and `<=500 MiB` package values remain engineering and stretch targets. The 16K stress tier does not inherit the 2 GiB absolute ceiling; its memory peak is recorded and OS memory termination remains a hard failure.

The target set, common context policy, primary KV-cache type policy, prompt/generation budget policy, prompt-processing batch/cache-reuse policy, runtime identity method, memory measurement method, 8K Core `2 GiB` hard memory gate, component timing measurement policy, five-run repetition/aggregation policy, platform-native thermal-readiness method, per-run energy-measurement method, V1 energy-qualification role, universal device/runtime failure semantics, and performance-threshold derivation policy are now frozen. Exact numeric performance thresholds remain intentionally unresolved: they require a documented candidate-independent usability basis and must be frozen before candidate results or execution. The exact llama.cpp commit value, exact OS/build versions, compiler/toolchain versions, build flags/backends, platform wrapper/application identities, produced runtime artifact identities, tokenizer/template identities and token-accounting implementation, exact memory instrumentation/tool invocation and sampling cadence where applicable, any 16K stress absolute RAM ceiling, exact timing instrumentation, exact platform thermal signal identities/mappings and ready thresholds, exact energy signal/tool/meter identities, calibration/uncertainty details, exact target-native failure signal identities, and exact noncompletion watchdog timeout also remain unresolved. They must be fixed before live execution authorization and cannot be chosen after candidate results are observed. Any future energy hard gate is outside the frozen V1 policy and requires separate canonical evidence before results.

### 4.3 Donor-origin restrictions

`FD-006=NOT_INVOKED` means commandMed does not automatically inherit model-origin restrictions from other projects.

Candidate eligibility is governed only by commandMed's own canonical evaluation, provenance, safety, licensing, device, and authorization contracts unless a later explicit founder decision changes this rule.

## 5. Non-goals and prohibited actions

The following are outside this clarification-stage authority:

- downloading, cloning, pulling, caching, or otherwise obtaining model weights;
- accepting gated model terms, gated dataset terms, or access requests;
- logging in to model providers or model hubs for gated access;
- running inference, generation, embeddings, reranking, scoring, or model-backed preprocessing;
- reading, downloading, caching, copying, or executing benchmark payloads for tournament measurement;
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
- failure of the `2 GiB` absolute platform-native peak-memory hard ceiling on any frozen 8K Core target is disqualifying for `PRIMARY` mass-reach qualification;
- a frozen universal device/runtime `HARD_FAIL` is disqualifying for the affected candidate/target/condition;
- failure of a frozen numeric performance hard gate, once its candidate-independent value is separately bound before execution, is disqualifying for the affected candidate/target/condition;
- missing, malformed, wrong-manifest, blocked, insufficient, or non-comparable evidence is `INCOMPLETE` rather than silently favorable;
- any declared candidate with incomplete required evidence forces `NO_SELECTION` before ranking;
- a valid five-run numeric aggregate requires five complete numeric runs; a hard-fail run or incomplete run cannot be replaced or omitted to manufacture a median;
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

1. **qualification phase** — provenance/lineage, licensing, safety, minimum medical-quality, candidate identity, comparability, the `700 MiB` minimum-package ceiling, the `2 GiB` 8K Core memory ceiling, universal device/runtime hard-failure semantics, frozen performance hard gates once their candidate-independent values are bound, and all other frozen device/package hard gates must pass; a smaller model cannot compensate for failure of any hard gate;
2. **ranking phase** — among fully qualified candidates only, complete deployable package bytes are the first comparison metric with direction `LOWER_BETTER`; only then are the remaining predeclared secondary metrics compared lexicographically.

Requirements:

- only canonical non-hard-gate metrics eligible for comparison may enter the ranking vector;
- metric direction must be explicit (`HIGHER_BETTER` or `LOWER_BETTER`);
- ranking metric order must be frozen before live evaluation;
- the first ranking metric after qualification is complete deployable package bytes, measured under one frozen package-accounting rule;
- weighted sums are prohibited unless a future separately reviewed canonical contract explicitly replaces this rule;
- safety, lineage, licensing, minimum medical-quality, package, frozen 8K Core memory, universal runtime/device, and frozen performance hard gates are not compensable by a smaller package or higher capability score;
- device/resource criteria that become hard qualification gates must be frozen before execution and must not be retrofitted after results are seen;
- performance threshold values must come from candidate-independent usability evidence, not from candidate results;
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
15. pre-execution evidence that the candidate has a plausible path to the frozen `700 MiB` package ceiling and `2 GiB` 8K Core memory/device envelope without candidate-specific post-result threshold changes;
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

This clarification-stage document does not authorize opening, downloading, caching, copying, or executing the benchmark payloads needed to obtain those results.

### 13.1 Canonical public slice manifest policy

`CANONICAL_PUBLIC_SLICE_MANIFEST_ONLY` freezes the admissible source boundary for the future baseline evaluation manifest without granting payload access:

```text
BASELINE_EVALUATION_SCOPE_POLICY=CANONICAL_PUBLIC_SLICE_MANIFEST_ONLY
CANONICAL_REGISTRY_SOURCE=SPEC001_BENCHMARKS_IDENTITY
PUBLIC_DEVELOPMENT_SCOPE_IDS=healthbench_core,healthbench_consensus,healthbench_hard,healthbench_professional,medxpertqa,pubmedqa
EVALUATION_SLICE_MANIFEST_REQUIRED=YES
EXACT_PRIMARY_SELECTION_SLICE_MANIFEST=NOT_YET_FROZEN
MANIFEST_MUST_BE_FROZEN_BEFORE_EXECUTION=YES
ONLY_CANONICAL_SPEC001_METRICS_ALLOWED=YES
ONLY_EXPLICITLY_AUTHORIZED_SLICES_ALLOWED=YES
PRIMARY_CANDIDATES_USE_IDENTICAL_SLICE_MANIFEST=YES
CANDIDATE_SPECIFIC_SLICE_SELECTION=PROHIBITED
POST_RESULT_SLICE_ADDITION_OR_REMOVAL=PROHIBITED
PUBLIC_BENCHMARK_METADATA_INSPECTION=ALLOWED_READ_ONLY
PUBLIC_BENCHMARK_PAYLOAD_ACCESS=NOT_AUTHORIZED_YET
PUBLIC_BENCHMARK_PAYLOAD_EXECUTION=NOT_AUTHORIZED_YET
PRIVATE_GOLD_ACCESS=PROHIBITED
GATED_BENCHMARK_ACCESS=PROHIBITED_WITHOUT_SEPARATE_AUTHORIZATION
REFERENCE_ONLY_BENCHMARK_EXECUTION=PROHIBITED
UNBOUND_EXECUTABLE_ARTIFACT=PROHIBITED
PUBLIC_CANONICAL_TEST_SPLITS_CAN_SELECT_MODEL=NO
MEDXPERTQA_TEXT_DEV_SELECTION_ELIGIBILITY=FUTURE_MANIFEST_AND_CHECKPOINT_SELECTION_BINDING_REQUIRED
MEDXPERTQA_TEXT_TEST_ROLE=PUBLIC_EXTERNAL_EVAL_ONLY
MEDXPERTQA_MM_ROLE=SECONDARY_NON_RANKING_IF_SEPARATELY_AUTHORIZED
HEALTHBENCH_AND_PUBMEDQA_SELECTION_PURPOSE=NOT_YET_FROZEN
SAFETY_HARD_GATE_SLICES=PRESERVED_FROM_CANONICAL_SPEC002
ARABIC_CLINICAL_PARITY_REQUIREMENT=PRESERVED
SELECTIVE_RISK_REQUIREMENT=PRESERVED
LAB_EXTRACTION_REQUIREMENT=PRESERVED
UNFROZEN_CLINICAL_STATISTICAL_THRESHOLDS=NO_PASS_UNTIL_FROZEN
BENCHMARK_CONTAMINATION_AND_QUARANTINE_POLICY=MUST_BE_BOUND_BEFORE_EXECUTION
EXACT_EXECUTION_PAYLOAD_MANIFEST=NOT_YET_AUTHORIZED
```

The six listed IDs are the current canonical registry records that are both `PUBLIC` and `DEVELOPMENT`; they define the **metadata eligibility envelope**, not an execution set. `REFERENCE_ONLY`, mixed-component, unresolved, gated, or private assets cannot be laundered into execution by appearing in a literature review or public catalog. A benchmark's `PUBLIC`/`DEVELOPMENT` registry status also does not by itself prove that its exact artifact may select the tournament winner: the future manifest must bind each slice to the canonical quarantine purpose. Public canonical test splits remain `PUBLIC_EXTERNAL_EVAL` and cannot select a model. MedXpertQA `Text/dev.jsonl` is the only currently named dev slice in the registry whose future selection use can be considered, and even that requires a pre-execution `DEV`/`CHECKPOINT_SELECTION` binding; `Text/test.jsonl` remains external-evaluation-only, while `MM/dev.jsonl`, `MM/test.jsonl`, and images remain modality-specific secondary non-ranking evidence if separately authorized. HealthBench and PubMedQA selection-purpose mappings remain unresolved rather than being inferred from their `DEVELOPMENT` labels.

All six canonical hard-gate metric identities from the inherited Spec 001/002 catalog remain preserved: `emergency_miss_rate`, `medication_critical_error_rate`, `selective_risk_at_target_coverage`, `citation_entailment_fidelity`, `arabic_clinical_parity_gap`, and `lab_report_field_extraction_accuracy`. This policy does not invent missing population/statistical thresholds, does not make Private Gold selectable, and does not claim that every hard gate is currently evaluable from public slices. Where an inherited hard gate cannot yet be evaluated under authorized evidence, the result remains non-passable until its separate evidence/threshold requirements are canonically satisfied.

### 13.2 Predeclared quarantine purpose per slice

`PREDECLARED_QUARANTINE_PURPOSE_PER_SLICE` freezes the purpose-classification rule for every future executable benchmark slice before payload access or execution:

```text
BENCHMARK_PURPOSE_POLICY=PREDECLARED_QUARANTINE_PURPOSE_PER_SLICE
EVERY_EXECUTABLE_SLICE_REQUIRES_ONE_CANONICAL_PURPOSE=YES
PURPOSE_MUST_BE_FROZEN_BEFORE_PAYLOAD_ACCESS_OR_EXECUTION=YES
ALLOWED_PURPOSES=DEV,CHECKPOINT_SELECTION,PUBLIC_EXTERNAL_EVAL
CHECKPOINT_SELECTION_REQUIRES_CAN_SELECT_MODEL_TRUE=YES
CHECKPOINT_SELECTION_SOURCE_CLASS_MUST_BE_CANONICALLY_ALLOWED=YES
PUBLIC_CANONICAL_TEST_SPLIT_PURPOSE=PUBLIC_EXTERNAL_EVAL
PUBLIC_CANONICAL_TEST_SPLIT_CAN_SELECT_MODEL=NO
PRIVATE_GOLD_PURPOSE=PRIVATE_GOLD_ONLY
PRIVATE_GOLD_CAN_SELECT_MODEL=NO
PRIVATE_GOLD_CAN_TRAIN=NO
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
REFERENCE_ONLY_ASSET_EXECUTION=PROHIBITED
UNBOUND_COMPONENT_EXECUTION=PROHIBITED
UNRESOLVED_PURPOSE=NOT_EXECUTABLE
SAME_SLICE_PURPOSE_ACROSS_CANDIDATES=REQUIRED
CANDIDATE_SPECIFIC_PURPOSE_MAPPING=PROHIBITED
POST_RESULT_PURPOSE_REMAPPING=PROHIBITED
DEV_TO_EXTERNAL_EVAL_PROMOTION_AFTER_RESULTS=PROHIBITED
EXTERNAL_EVAL_TO_SELECTION_PROMOTION_AFTER_RESULTS=PROHIBITED
MEDXPERTQA_TEXT_TEST_PURPOSE=PUBLIC_EXTERNAL_EVAL
MEDXPERTQA_MM_PURPOSE=SECONDARY_NON_RANKING_IF_SEPARATELY_AUTHORIZED
MEDXPERTQA_TEXT_DEV_PURPOSE=NOT_YET_FROZEN
HEALTHBENCH_PURPOSE_MAPPING=NOT_YET_FROZEN
PUBMEDQA_PURPOSE_MAPPING=NOT_YET_FROZEN
PURPOSE_AMBIGUITY=FAIL_CLOSED_NOT_EXECUTABLE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
```

A future executable slice must have one and only one canonical quarantine purpose in the execution manifest. `CHECKPOINT_SELECTION` is permitted only where the inherited quarantine contract explicitly allows the source class to select and `can_select_model=true`; a public label or development label alone is insufficient. Public canonical test splits remain `PUBLIC_EXTERNAL_EVAL`, so their results cannot select a candidate or be promoted into selection evidence. Private Gold remains governed by its separate `PRIVATE_GOLD` purpose, cannot select or train, and remains inaccessible under this clarification authority. `REFERENCE_ONLY`, unbound, and unresolved-purpose assets remain non-executable.

Purpose mapping is a candidate-neutral property of the slice, not a per-candidate tuning knob. The same exact slice must retain the same canonical purpose across every comparable candidate. Candidate-specific mapping, post-result remapping, or promoting an external-evaluation result into selection evidence after observing candidate performance is prohibited. MedXpertQA `Text/test.jsonl` is frozen as `PUBLIC_EXTERNAL_EVAL`; its multimodal assets remain secondary non-ranking if separately authorized. MedXpertQA text dev, HealthBench, and PubMedQA exact purpose mappings remain unresolved rather than being inferred. This policy grants no benchmark payload access or execution authority.

### 13.3 Metadata-first exact-artifact access gate

`METADATA_FIRST_EXACT_ARTIFACT_BINDING_BEFORE_ACCESS` freezes the preconditions that must be satisfied before any future benchmark payload bytes may be obtained, cached, copied, or executed:

```text
PUBLIC_BENCHMARK_ACCESS_POLICY=METADATA_FIRST_EXACT_ARTIFACT_BINDING_BEFORE_ACCESS
PUBLIC_SOURCE_METADATA_INSPECTION=ALLOWED_READ_ONLY
PAYLOAD_ACCESS_REQUIRES_EXPLICIT_SEPARATE_AUTHORIZATION=YES
PAYLOAD_ACCESS_REQUIRES_EXACT_ARTIFACT_IDENTITY=YES
PAYLOAD_ACCESS_REQUIRES_IMMUTABLE_SOURCE_REVISION=YES
PAYLOAD_ACCESS_REQUIRES_LICENSE_AND_ACCESS_CLASS_RESOLVED=YES
PAYLOAD_ACCESS_REQUIRES_QUARANTINE_PURPOSE_FROZEN=YES
PAYLOAD_ACCESS_REQUIRES_CONTAMINATION_DISPOSITION=YES
MUTABLE_LATEST_OR_UNPINNED_PAYLOAD=PROHIBITED
UNBOUND_PAYLOAD_ACCESS=PROHIBITED
GATED_PAYLOAD_ACCESS=PROHIBITED_WITHOUT_SEPARATE_AUTHORIZATION
PRIVATE_PAYLOAD_ACCESS=PROHIBITED_WITHOUT_SEPARATE_AUTHORIZATION
PRIVATE_GOLD_ACCESS=PROHIBITED
EXTERNAL_SUBMISSION_ONLY_GROUND_TRUTH=NO_LOCAL_GOLD_ACCESS
LOCAL_PAYLOAD_CACHE_OR_COPY_CREATION=NOT_AUTHORIZED_YET
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
ACCESS_MECHANISM_MUST_PRESERVE_CANONICAL_ARTIFACT_IDENTITY=YES
POST_ACCESS_ARTIFACT_SUBSTITUTION=PROHIBITED
CANDIDATE_SPECIFIC_PAYLOAD_VERSION=PROHIBITED
ACCESS_FAILURE_OR_IDENTITY_MISMATCH=FAIL_CLOSED_INCOMPLETE
```

Read-only metadata inspection may identify repositories, filenames, revisions, digests, licenses, access classes, split roles, or transport mechanisms without obtaining benchmark payload bytes. That metadata inspection does not itself authorize download, cloning, local copy/cache creation, API retrieval of payload contents, or execution. A future payload-access authorization may be proposed only after the exact artifact/split identity, immutable source revision or equivalent digest, license/access class, canonical quarantine purpose, and contamination disposition are all bound.

The eventual access mechanism may differ by benchmark, but it must preserve the frozen canonical artifact identity and cannot silently follow a mutable `latest`, branch head, changing remote object, or candidate-specific version. Gated/private assets require their own separate authority; Private Gold remains prohibited. Where evaluation uses an external submission service whose ground truth is not distributed, that service does not create local Gold access. Any access failure, missing immutable identity, or identity mismatch is `INCOMPLETE` and cannot be repaired by substituting a different payload after results are observed. This policy does not select concrete per-benchmark transport URLs or authorize any benchmark bytes to be obtained.

### 13.4 Use-class-specific fail-closed contamination binding

`USE_CLASS_SPECIFIC_FAIL_CLOSED_CONTAMINATION_BINDING` freezes the Spec 005 interpretation of the canonical Spec 003 contamination gate without self-asserting any candidate-specific result:

```text
CONTAMINATION_PROOF_POLICY=USE_CLASS_SPECIFIC_FAIL_CLOSED_CONTAMINATION_BINDING
CONTAMINATION_DISPOSITION_REQUIRED_BEFORE_PAYLOAD_ACCESS=YES
CONTAMINATION_DISPOSITION_REQUIRED_BEFORE_CANDIDATE_EXECUTION=YES
SPEC003_CLEAN_CONTAMINATION_REQUIRED_USES=MODIFICATION_OR_DERIVATION,TEACHER_OR_SYNTHETIC_GENERATION,TRAINING_OR_ADAPTATION
MODIFICATION_OR_DERIVATION_REQUIRES_CLEAN_CONTAMINATION=YES
CLEAN_CONTAMINATION_ELIGIBLE_STATES=ASSESSED_CLEAN,NOT_APPLICABLE
NOT_APPLICABLE_REQUIRES_EXPLICIT_EVIDENCE=YES
NOT_APPLICABLE_REQUIRES_TRULY_OUTSIDE_CONTAMINATION_CONDITION=YES
SELF_ASSERTED_NOT_APPLICABLE=PROHIBITED
EXACT_MODEL_WEIGHT_QUANTIZATION_NOT_APPLICABLE=CONDITIONALLY_ALLOWED_ONLY_FOR_WEIGHT_ONLY_DATA_FREE_TRANSFORM
WEIGHT_ONLY_DATA_FREE_QUANTIZATION_REQUIRES_EXACT_SOURCE_WEIGHT_IDENTITY=YES
WEIGHT_ONLY_DATA_FREE_QUANTIZATION_REQUIRES_EXACT_TRANSFORM_TOOLCHAIN_IDENTITY=YES
WEIGHT_ONLY_DATA_FREE_QUANTIZATION_REQUIRES_FROZEN_TRANSFORM_FLAGS=YES
WEIGHT_ONLY_DATA_FREE_QUANTIZATION_REQUIRES_NO_CALIBRATION_DATA=YES
WEIGHT_ONLY_DATA_FREE_QUANTIZATION_REQUIRES_NO_IMATRIX_DATA=YES
WEIGHT_ONLY_DATA_FREE_QUANTIZATION_REQUIRES_NO_BENCHMARK_OR_GOLD_INPUT=YES
WEIGHT_ONLY_DATA_FREE_QUANTIZATION_REQUIRES_NO_TRAINING_OR_DEV_PAYLOAD_INPUT=YES
WEIGHT_ONLY_DATA_FREE_QUANTIZATION_REQUIRES_NO_TEACHER_OR_PROVIDER_OUTPUT=YES
QUANTIZATION_WITH_CALIBRATION_OR_IMATRIX_OR_DATA=CONTAMINATION_ASSESSMENT_REQUIRED
QUANTIZATION_WITH_UNRESOLVED_INPUT_PROVENANCE=NOT_ELIGIBLE_FAIL_CLOSED
EVALUATION_PAYLOAD_CONTAMINATION_DISPOSITION_REQUIRED=YES
CANDIDATE_DERIVATION_CONTAMINATION_DISPOSITION_REQUIRED=YES
CONTAMINATION_EVIDENCE_OR_RATIONALE_IDENTITY_REQUIRED=YES
KNOWN_OVERLAP_OR_HIGH_RISK=PROHIBITED_FOR_CLEAN_REQUIRED_USE
PENDING_OR_NOT_ASSESSED=BLOCKED_FOR_CLEAN_REQUIRED_USE
PUBLIC_EXTERNAL_EVAL_TO_SELECTION_REUSE=PROHIBITED
PRIVATE_GOLD_CONTAMINATION_BOUNDARY=PRESERVED
CANDIDATE_SPECIFIC_CONTAMINATION_EXCEPTION=PROHIBITED
POST_RESULT_CONTAMINATION_RECLASSIFICATION=PROHIBITED
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
```

The canonical Spec 003 evaluator treats `MODIFICATION_OR_DERIVATION` as a clean-contamination-required use and accepts only `ASSESSED_CLEAN` or `NOT_APPLICABLE` at that gate. Its planning contract restricts `NOT_APPLICABLE` to an explicit case that is truly outside the contamination condition. Spec 005 therefore does not equate quantization with `NOT_APPLICABLE` automatically.

For a future exact model-weight quantization, `NOT_APPLICABLE` may be proposed only when evidence proves a weight-only/data-free transform: exact source weights, exact transform/toolchain, and frozen flags are bound, and no calibration set, imatrix data, benchmark/Gold payload, training/dev payload, teacher output, provider output, or equivalent external data influences the transform. If any such data participates, the path requires an exact contamination assessment and cannot use the data-free `NOT_APPLICABLE` route. Missing provenance, `PENDING`, `NOT_ASSESSED`, or contradictory contamination evidence fails closed. Known overlap/high risk prohibits a clean-required use. This policy freezes semantics only; it computes no candidate-specific contamination disposition and authorizes no model weights, conversion, benchmark payload, Private Gold, or execution.

## 14. Device, package, runtime, quantization, and resource evidence

`NAMED_DEVICE_PLUS_RESOURCE_ENVELOPE`, `MASS_REACH_FIVE_TARGET_SET`, `8K_CORE_16K_STRESS`, `Q8_0_SYMMETRIC_KV_CORE`, `7K_PROMPT_1K_GENERATION`, `B512_U128_COLD_NO_REUSE`, `PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST`, `PLATFORM_NATIVE_PEAK_MEMORY`, `2G_CORE_HARD_CAP`, `COMPONENT_TIMING_COLD_AND_READY`, `FIVE_FRESH_RUNS_MEDIAN_WITH_WORST_CASE`, `PLATFORM_NATIVE_THERMAL_READY_GATE`, `PLATFORM_NATIVE_ENERGY_PER_RUN`, `ENERGY_REQUIRED_EVIDENCE_NO_V1_ABSOLUTE_HARD_GATE`, `UNIVERSAL_FATAL_FAILURES_AND_FAIL_CLOSED_EVIDENCE`, `PREDECLARED_TARGET_USABILITY_PERFORMANCE_GATES`, `DUAL_BUILD_BASELINE_AND_DEPLOYABLE`, `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY`, `QUALITY_FLOOR_THEN_SIZE_FIRST`, `SUB_700MB_MASS_REACH`, `GGUF_LLAMA_CPP_CANONICAL`, and `Q4_FLOOR_SMALLEST_PASSING` are frozen as Spec 005 evidence strategies.

The minimum text/core package and device envelope is:

```text
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_HARD_CEILING=700_MiB
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_ENGINEERING_TARGET=600_MiB_OR_LESS
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_STRETCH_TARGET=500_MiB_OR_LESS_IF_HARD_GATES_PASS
PEAK_WORKING_RAM_ENGINEERING_TARGET=2_GiB_OR_LESS_AT_FROZEN_SHORT_CONTEXT
CORE_8K_MEMORY_GATE=2G_CORE_HARD_CAP
CORE_8K_PEAK_MEMORY_HARD_CEILING=2_GiB
CORE_8K_PEAK_MEMORY_HARD_CEILING_BYTES=2147483648
CORE_8K_HARD_CEILING_APPLIES_TO_ALL_FIVE_TARGETS=YES
CORE_8K_HARD_CEILING_USES_PLATFORM_NATIVE_PRIMARY_METRIC=YES
CORE_8K_MEMORY_TERMINATION=HARD_FAIL
CORE_8K_PEAK_DELTA=DIAGNOSTIC_ONLY
CORE_8K_ABSOLUTE_PEAK=HARD_GATE_INPUT
STRESS_16K_PEAK_MEMORY=RECORDED
STRESS_16K_OS_MEMORY_TERMINATION=HARD_FAIL
STRESS_16K_ABSOLUTE_RAM_HARD_CEILING=NOT_FROZEN
CANDIDATE_SPECIFIC_RAM_EXCEPTION=PROHIBITED
POST_RESULT_RAM_CEILING_CHANGE=PROHIBITED
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
MEMORY_MEASUREMENT_POLICY=PLATFORM_NATIVE_PEAK_MEMORY
IOS_PRIMARY_PEAK_METRIC=LEDGER_PHYS_FOOTPRINT_PEAK
IOS_OS_MEMORY_TERMINATION=HARD_FAIL
ANDROID_PRIMARY_PEAK_METRIC=RSS_TRACE_PEAK
ANDROID_SECONDARY_MEMORY_METRIC=TOTAL_PSS
ANDROID_LMK_OR_OOM_TERMINATION=HARD_FAIL
LINUX_PRIMARY_PEAK_METRIC=CGROUP_V2_MEMORY_PEAK
LINUX_OOM_TERMINATION=HARD_FAIL
FULL_QUALIFICATION_PROCESS_SET_ACCOUNTED=YES
MEASUREMENT_WINDOW=FULL_COLD_QUALIFICATION_RUN
BASELINE_BEFORE_MODEL_LOAD=RECORDED
PEAK_ABSOLUTE_BYTES=RECORDED
PEAK_DELTA_FROM_BASELINE=RECORDED
CROSS_PLATFORM_RAW_METRIC_RANKING=PROHIBITED
PERFORMANCE_MEASUREMENT_POLICY=COMPONENT_TIMING_COLD_AND_READY
COLD_START_TO_FIRST_TOKEN=RECORDED
MODEL_LOAD_TIME=RECORDED
READY_STATE_TTFT=RECORDED
PREFILL_TOKENS_PER_SECOND=RECORDED
DECODE_TOKENS_PER_SECOND=RECORDED
END_TO_END_RESPONSE_TIME=RECORDED
TIMING_BOUNDARIES_IDENTICAL_ACROSS_CANDIDATES=YES
TIMING_BOUNDARIES_IDENTICAL_ACROSS_TARGETS=YES
MODEL_LOAD_TIME_EXCLUDED_FROM_READY_STATE_TTFT=YES
COLD_START_TO_FIRST_TOKEN_INCLUDES_MODEL_LOAD=YES
PROMPT_SESSION_PREFIX_CACHE_REUSE=PROHIBITED
CANDIDATE_SPECIFIC_TIMING_BOUNDARIES=PROHIBITED
PERFORMANCE_REPETITION_POLICY=FIVE_FRESH_RUNS_MEDIAN_WITH_WORST_CASE
MEASURED_RUNS_PER_CANDIDATE_TARGET_CONDITION=5
EACH_MEASURED_RUN_STARTS_FROM_FRESH_PROCESS=YES
EACH_MEASURED_RUN_INCLUDES_FRESH_MODEL_LOAD=YES
MEASURED_REQUESTS_PER_FRESH_LOAD=1
NON_MEASURED_WARMUP_REQUESTS=0
PRIMARY_AGGREGATION=MEDIAN_OF_FIVE
WORST_CASE_RUN=RECORDED
ALL_RAW_RUNS=RETAINED
FAILED_OR_TERMINATED_RUNS=RETAINED_AS_FAILURE
FAILED_RUN_REPLACEMENT=PROHIBITED
POST_HOC_RUN_EXCLUSION=PROHIBITED
CANDIDATE_SPECIFIC_RUN_COUNT=PROHIBITED
TARGET_SPECIFIC_RUN_COUNT=PROHIBITED
THERMAL_CONTROL_POLICY=PLATFORM_NATIVE_THERMAL_READY_GATE
THERMAL_STATE_BEFORE_EACH_RUN=RECORDED
THERMAL_STATE_AFTER_EACH_RUN=RECORDED
MEASURED_RUN_START_REQUIRES_THERMAL_READY=YES
KNOWN_ACTIVE_THROTTLING_AT_RUN_START=PROHIBITED
THERMAL_READINESS_USES_PLATFORM_NATIVE_SIGNAL=YES
THERMAL_SIGNAL_IDENTITY_MUST_BE_PINNED=YES
IOS_THERMAL_STATE=PLATFORM_NATIVE_RECORDED
ANDROID_THERMAL_STATUS=PLATFORM_NATIVE_RECORDED
LAPTOP_CPU_THERMAL_TELEMETRY=RECORDED
COOLDOWN_BETWEEN_RUNS=AS_NEEDED_UNTIL_THERMAL_READY
FIXED_SLEEP_AS_THERMAL_PROOF=PROHIBITED
RUN_ORDER_PREDECLARED=REQUIRED
CANDIDATE_SPECIFIC_THERMAL_EXCEPTION=PROHIBITED
POST_RESULT_THERMAL_RULE_CHANGE=PROHIBITED
THERMAL_TERMINATION_OR_OS_THROTTLING_EVENT=RECORDED
EXACT_PLATFORM_THERMAL_READY_THRESHOLDS=NOT_YET_FROZEN
ENERGY_MEASUREMENT_POLICY=PLATFORM_NATIVE_ENERGY_PER_RUN
ENERGY_MEASUREMENT_REQUIRED_FOR_EACH_MEASURED_RUN=YES
ENERGY_WINDOW_MATCHES_FULL_COLD_RUN=YES
PRE_RUN_ENERGY_BASELINE=RECORDED
POST_RUN_ENERGY_RECORD=RECORDED
RUN_ENERGY_DELTA=RECORDED_WHERE_SUPPORTED
ENERGY_SIGNAL_IDENTITY_MUST_BE_PINNED=YES
ENERGY_TOOL_OR_METER_IDENTITY_MUST_BE_PINNED=YES
SAME_ENERGY_METHOD_WITHIN_TARGET_ACROSS_CANDIDATES=REQUIRED
CANDIDATE_SPECIFIC_ENERGY_METHOD=PROHIBITED
POST_RESULT_ENERGY_METHOD_CHANGE=PROHIBITED
IOS_ENERGY_EVIDENCE=PLATFORM_NATIVE_OR_PREDECLARED_VALIDATED_METER
ANDROID_ENERGY_EVIDENCE=PLATFORM_NATIVE_OR_PREDECLARED_VALIDATED_METER
LAPTOP_ENERGY_EVIDENCE=PLATFORM_NATIVE_OR_PREDECLARED_VALIDATED_METER
RAW_ENERGY_UNIT_AND_SEMANTICS=RECORDED
ENERGY_MEASUREMENT_UNCERTAINTY=RECORDED_WHERE_AVAILABLE
CROSS_PLATFORM_RAW_ENERGY_RANKING=PROHIBITED
ENERGY_COMPARISON_SCOPE=SAME_TARGET_SAME_METHOD_ONLY
FAILED_OR_MISSING_ENERGY_CAPTURE=EVIDENCE_INCOMPLETE
FAILED_RUN_ENERGY_RECORD_RETAINED=YES
ENERGY_QUALIFICATION_POLICY=ENERGY_REQUIRED_EVIDENCE_NO_V1_ABSOLUTE_HARD_GATE
ENERGY_EVIDENCE_REQUIRED=YES
MISSING_ENERGY_EVIDENCE=INCOMPLETE
V1_ABSOLUTE_ENERGY_HARD_CEILING=NONE
ENERGY_HARD_DISQUALIFICATION_BY_RAW_VALUE=PROHIBITED
SAME_TARGET_ENERGY_COMPARISON=ALLOWED
CROSS_PLATFORM_RAW_ENERGY_COMPARISON=PROHIBITED
ENERGY_MAY_ENTER_SECONDARY_RANKING=ONLY_IF_PREDECLARED
ENERGY_SECONDARY_RANKING_SCOPE=SAME_TARGET_SAME_METHOD_ONLY
ENERGY_CANNOT_COMPENSATE_FOR_SAFETY_FAILURE=YES
ENERGY_CANNOT_COMPENSATE_FOR_QUALITY_FAILURE=YES
ENERGY_CANNOT_COMPENSATE_FOR_PACKAGE_FAILURE=YES
ENERGY_CANNOT_COMPENSATE_FOR_CORE_MEMORY_FAILURE=YES
POST_RESULT_ENERGY_THRESHOLD_CREATION=PROHIBITED
CANDIDATE_SPECIFIC_ENERGY_THRESHOLD=PROHIBITED
FUTURE_ENERGY_HARD_GATE_REQUIRES_SEPARATE_CANONICAL_EVIDENCE=YES
DEVICE_RUNTIME_FAILURE_POLICY=UNIVERSAL_FATAL_FAILURES_AND_FAIL_CLOSED_EVIDENCE
RUNTIME_INITIALIZATION_FAILURE=HARD_FAIL
CANONICAL_ARTIFACT_LOAD_FAILURE=HARD_FAIL
REQUIRED_CORE_CONDITION_EXECUTION_FAILURE=HARD_FAIL
PROCESS_CRASH_OR_ABNORMAL_TERMINATION=HARD_FAIL
OS_NON_MEMORY_FORCED_TERMINATION=HARD_FAIL
MEASURED_REQUEST_NONCOMPLETION=HARD_FAIL
UNAUTHORIZED_RUNTIME_BACKEND_OR_ARTIFACT_FALLBACK=HARD_FAIL
MISSING_REQUIRED_MEASUREMENT_EVIDENCE=INCOMPLETE
MALFORMED_REQUIRED_MEASUREMENT_EVIDENCE=INCOMPLETE
UNPROVABLE_RUNTIME_OR_ARTIFACT_IDENTITY=INCOMPLETE
WRONG_OR_UNPROVABLE_RUN_CONFIGURATION=INCOMPLETE
MID_RUN_THERMAL_THROTTLING=RECORDED_NOT_AUTOMATIC_HARD_FAIL
FIVE_RUN_SET_WITH_ANY_HARD_FAIL=HARD_FAIL
FIVE_RUN_SET_WITH_ANY_INCOMPLETE_RUN=INCOMPLETE
MEDIAN_OF_FIVE_REQUIRES_FIVE_COMPLETE_NUMERIC_RUNS=YES
PARTIAL_MEDIAN_SUBSTITUTION=PROHIBITED
TARGET_NATIVE_FAILURE_SIGNAL_IDENTITY=PINNED_BEFORE_EXECUTION
NONCOMPLETION_DETECTION_WATCHDOG=PREEXECUTION_REQUIRED
EXACT_WATCHDOG_TIMEOUT=NOT_YET_FROZEN
CANDIDATE_SPECIFIC_FAILURE_EXCEPTION=PROHIBITED
POST_RESULT_FAILURE_RULE_CHANGE=PROHIBITED
PERFORMANCE_THRESHOLD_POLICY=PREDECLARED_TARGET_USABILITY_PERFORMANCE_GATES
PERFORMANCE_HARD_GATES_REQUIRED_BEFORE_EXECUTION=YES
EXACT_NUMERIC_PERFORMANCE_THRESHOLDS=NOT_YET_FROZEN
PERFORMANCE_HARD_THRESHOLDS=NOT_YET_FROZEN
THRESHOLDS_MUST_BE_FROZEN_BEFORE_CANDIDATE_RESULTS=YES
THRESHOLD_EVIDENCE_BASIS_MUST_BE_DOCUMENTED=YES
SAME_TARGET_THRESHOLDS_IDENTICAL_ACROSS_CANDIDATES=YES
CANDIDATE_SPECIFIC_PERFORMANCE_THRESHOLD=PROHIBITED
POST_RESULT_PERFORMANCE_THRESHOLD_CHANGE=PROHIBITED
TARGET_SPECIFIC_THRESHOLDS=ALLOWED_WHEN_PREDECLARED_AND_JUSTIFIED
TARGET_SPECIFIC_THRESHOLD_RELAXATION_AFTER_RESULTS=PROHIBITED
COLD_START_TO_FIRST_TOKEN_HARD_GATE=REQUIRED
READY_STATE_TTFT_HARD_GATE=REQUIRED
DECODE_TOKENS_PER_SECOND_HARD_GATE=REQUIRED
PREFILL_TOKENS_PER_SECOND=RECORDED_AND_SECONDARY_UNLESS_SEPARATELY_FROZEN
MODEL_LOAD_TIME=RECORDED_COMPONENT
END_TO_END_RESPONSE_TIME=RECORDED_AND_SECONDARY_UNLESS_SEPARATELY_FROZEN
PRIMARY_THRESHOLD_AGGREGATE=MEDIAN_OF_FIVE
WORST_CASE_RUN=MANDATORY_GUARDRAIL_EVIDENCE
HARD_FAIL_OR_INCOMPLETE_RUN_CANNOT_ENTER_NUMERIC_AGGREGATE=YES
PERFORMANCE_THRESHOLD_SOURCE=CANDIDATE_INDEPENDENT_USABILITY_EVIDENCE_REQUIRED
CANDIDATE_RESULT_DERIVED_THRESHOLD=PROHIBITED
PERFORMANCE_CAN_NEVER_COMPENSATE_FOR_SAFETY_FAILURE=YES
PERFORMANCE_CAN_NEVER_COMPENSATE_FOR_QUALITY_FAILURE=YES
PERFORMANCE_CAN_NEVER_COMPENSATE_FOR_PACKAGE_FAILURE=YES
PERFORMANCE_CAN_NEVER_COMPENSATE_FOR_CORE_MEMORY_FAILURE=YES
PERFORMANCE_CAN_NEVER_COMPENSATE_FOR_RUNTIME_HARD_FAIL=YES
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
- each candidate's canonical deployable artifact is the **smallest allowed ladder member** that passes every frozen safety, minimum medical-quality, compression-regression, `700 MiB` package, `2 GiB` 8K Core memory, runtime, and device gate;
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

### 14.4 Platform-native peak-memory measurement policy

`PLATFORM_NATIVE_PEAK_MEMORY` means:

- iOS qualification records physical-footprint peak as its primary peak-memory metric and treats OS memory-pressure termination during the measured run as a hard failure;
- Android qualification records a time-resolved RSS peak as the primary peak metric and total PSS as secondary memory context; LMK/OOM termination is a hard failure;
- the Linux x86-64 qualification path uses a dedicated cgroup v2 boundary covering the full required qualification process set and records `memory.peak`; OOM termination is a hard failure;
- if the weak-laptop path executes on Windows instead of Linux, a separately reviewed pre-execution Windows-native peak-working-set/accounting method must be bound rather than reusing Linux cgroup semantics;
- the measurement window is the full cold qualification run and records a pre-model-load baseline, absolute peak bytes, and peak delta from baseline;
- helper/runtime/wrapper processes required to deliver the tested local inference path must be included in the accounted process set and cannot be omitted to improve the reported number;
- platform-native raw memory numbers are qualification/resource evidence and may not be mixed into a cross-platform scientific ranking metric because their accounting semantics differ.

This policy freezes the measurement family and required records, not the exact sampling cadence/tool invocation or concrete OS/runtime build.

### 14.5 8K Core RAM hard gate

`2G_CORE_HARD_CAP` means:

- every measured common 8K Core qualification run on every frozen target must have an absolute platform-native peak of no more than `2 GiB` (`2147483648` bytes) for the full required qualification process set;
- the absolute platform-native peak is the hard-gate input; the recorded peak delta from baseline is diagnostic only and cannot rescue a run above the absolute ceiling;
- OS/LMK/OOM memory termination is a hard failure even when the last captured sample is below the numerical ceiling;
- the same `2 GiB` ceiling applies to all five targets, including 8 GB and 12 GB devices. A target with more installed RAM does not receive a higher Core ceiling;
- candidate-specific or target-specific RAM exceptions are prohibited, and the ceiling cannot be raised after candidate outcomes are known;
- the required 16K stress tier records platform-native peak memory and fails on OS memory termination, but `STRESS_16K_ABSOLUTE_RAM_HARD_CEILING=NOT_FROZEN` remains explicit.

This hard gate is specific to the mass-reach 8K Core condition and does not authorize execution.

### 14.6 Component timing policy

`COMPONENT_TIMING_COLD_AND_READY` means:

- `COLD_START_TO_FIRST_TOKEN` is recorded from the frozen cold-start boundary through first generated token and includes model-load time;
- `MODEL_LOAD_TIME` is recorded separately so load cost is not hidden inside a single end-to-end latency number;
- `READY_STATE_TTFT` is recorded from the frozen ready-state request boundary to first generated token and explicitly excludes model-load time;
- prefill throughput, decode throughput, and end-to-end response time are recorded separately;
- timing boundaries must be identical across comparable candidates and frozen targets;
- prompt-cache, session-state, prefix-cache, or equivalent reused prompt state is prohibited for measured timing;
- candidate-specific timing boundaries or post-result timing-boundary substitutions are prohibited;
- this policy does not freeze numeric performance pass/fail thresholds.

This policy freezes decomposition and comparability boundaries only. Exact instrumentation, thermal signal mappings, exact energy instrumentation identities, exact target-native failure signals, and the noncompletion watchdog identity/value remain unresolved pre-execution requirements. Exact numeric performance hard-gate values remain unresolved and are governed by the separately frozen candidate-independent threshold policy; V1 has no absolute raw-energy hard gate.

### 14.7 Five-fresh-run repetition and aggregation policy

`FIVE_FRESH_RUNS_MEDIAN_WITH_WORST_CASE` means:

- each candidate/target/condition requires exactly five measured runs;
- every measured run starts from a fresh process and includes a fresh model load;
- each fresh load contains exactly one measured request;
- no non-measured warm-up requests are permitted;
- the median of five is the primary aggregate, while the worst-case run is also recorded;
- all five raw run records are retained;
- a failed or terminated run remains a failure and must not be replaced;
- post-hoc run exclusion is prohibited;
- candidate-specific and target-specific run counts are prohibited;
- prompt/session/prefix-cache reuse remains prohibited;
- thermal state is recorded before and after each run under the separately frozen thermal-readiness policy;
- energy evidence is retained per measured run under the separately frozen energy policy;
- under the frozen universal failure policy, a hard-fail run makes the candidate/target/condition `HARD_FAIL`, an incomplete run makes it `INCOMPLETE`, and the median-of-five exists only when all five runs have complete required numeric evidence;
- partial-median substitution or calculating a median from fewer than five completed numeric runs is prohibited;
- under the frozen performance-threshold policy, the valid median-of-five is the primary threshold aggregate and the worst-case run is mandatory guardrail evidence;
- exact numeric performance hard-gate values remain unresolved until frozen from candidate-independent evidence before execution.

This policy freezes run count, fresh-process semantics, warm-up prohibition, aggregation, raw-run retention, failed-run handling, and the relationship between run disposition and aggregation. It does not authorize execution.

### 14.8 Platform-native thermal readiness gate

`PLATFORM_NATIVE_THERMAL_READY_GATE` means:

- platform-native thermal state/status is recorded immediately before and after every measured run;
- a measured run may start only when the frozen platform-native signal determines the target is thermal-ready;
- known active throttling at measured-run start is prohibited;
- the exact platform-native signal identity used for readiness must be pinned before execution;
- iOS uses a pinned platform-native thermal-state signal, Android uses a pinned platform-native thermal-status signal, and the laptop path records pinned CPU/platform thermal telemetry appropriate to its exact OS/runtime path;
- cooldown between measured runs is as long as needed to re-enter the frozen thermal-ready state;
- a fixed sleep interval alone is not proof of thermal readiness;
- run order must be predeclared before candidate results are observed;
- candidate-specific thermal exceptions and post-result thermal-rule changes are prohibited;
- thermal termination or OS/runtime throttling events are recorded and retained with the run evidence;
- mid-run thermal throttling is recorded and is not by itself an automatic `HARD_FAIL`; if it produces a crash, forced termination, or another frozen fatal event, that fatal event controls the run disposition;
- this policy does not yet freeze the exact per-platform ready-state mapping/numeric thresholds or numeric performance pass/fail values.

This policy freezes the readiness method and anti-throttling comparability rule only. Exact thermal signal identities and mapping/threshold details remain unresolved pre-execution requirements. It does not authorize device or model execution.

### 14.9 Platform-native energy-per-run policy

`PLATFORM_NATIVE_ENERGY_PER_RUN` means:

- an energy measurement record is required for every measured run;
- the energy measurement window matches the full cold qualification run;
- a pre-run energy baseline and post-run energy record are retained, with run energy delta recorded where the selected method supports it;
- the exact energy signal and tool/meter identity must be pinned before execution;
- within each target, the same energy method must be used across all comparable candidates;
- candidate-specific energy methods and post-result energy-method changes are prohibited;
- iOS, Android, and laptop evidence may use a platform-native signal or a predeclared validated external meter appropriate to that target, but its exact identity and semantics must be frozen before execution;
- raw unit and accounting semantics are retained with every energy record;
- measurement uncertainty is recorded where the selected tool/meter exposes it;
- raw energy values may be compared only within the same target using the same method;
- cross-platform raw-energy ranking is prohibited because platform accounting and meter semantics may differ;
- failed or missing energy capture makes the required energy evidence `INCOMPLETE` rather than silently favorable;
- failed-run energy records, when captured, are retained with the failed-run evidence;
- V1 does not impose an absolute raw-energy hard ceiling; any future energy hard gate requires separate canonical evidence before results are observed.

This policy freezes the per-run measurement scope and candidate-neutral comparison method only. Exact platform signals, tool/meter identities, and calibration/uncertainty procedures remain unresolved pre-execution requirements. It does not authorize device or model execution.

### 14.10 V1 energy qualification role

`ENERGY_REQUIRED_EVIDENCE_NO_V1_ABSOLUTE_HARD_GATE` means:

- energy evidence remains required for every measured run, and missing required energy evidence remains `INCOMPLETE`;
- `V1_ABSOLUTE_ENERGY_HARD_CEILING=NONE`;
- raw energy magnitude cannot itself hard-disqualify a V1 candidate;
- same-target energy comparison is allowed only under the frozen same-method rule;
- cross-platform raw-energy comparison remains prohibited;
- energy may enter the secondary ranking vector only if that role and direction are predeclared before live results, and only within same-target/same-method evidence;
- energy cannot compensate for safety, minimum medical-quality, package, or 8K Core memory hard-gate failure;
- candidate-specific energy thresholds and post-result energy-threshold creation are prohibited;
- a future energy hard gate requires a separate canonical evidence basis and decision before candidate results are observed;
- this policy does not freeze numeric performance pass/fail values.

This policy freezes V1's qualification role for energy: mandatory evidence, no absolute raw-value hard gate, and tightly bounded optional secondary comparison. It does not authorize execution or determine the unresolved secondary ranking order.

### 14.11 Universal device/runtime failure semantics

`UNIVERSAL_FATAL_FAILURES_AND_FAIL_CLOSED_EVIDENCE` means:

- `RUNTIME_INITIALIZATION_FAILURE=HARD_FAIL` when the correctly configured pinned runtime cannot initialize for the candidate on the required target;
- `CANONICAL_ARTIFACT_LOAD_FAILURE=HARD_FAIL` when the exact canonical candidate artifact cannot be loaded by the required pinned target path;
- `REQUIRED_CORE_CONDITION_EXECUTION_FAILURE=HARD_FAIL` when a correctly configured candidate/runtime cannot execute the frozen required Core condition;
- `PROCESS_CRASH_OR_ABNORMAL_TERMINATION=HARD_FAIL`;
- `OS_NON_MEMORY_FORCED_TERMINATION=HARD_FAIL`; existing platform memory-termination rules remain independently hard-fail as already frozen;
- `MEASURED_REQUEST_NONCOMPLETION=HARD_FAIL` once noncompletion is established by the separately pinned operational watchdog or by an explicit runtime/OS failure signal;
- `UNAUTHORIZED_RUNTIME_BACKEND_OR_ARTIFACT_FALLBACK=HARD_FAIL` when evidence proves that measured execution silently or explicitly substituted a runtime, backend, or artifact outside the frozen manifest;
- missing required measurement evidence is `INCOMPLETE`, not a candidate hard failure;
- malformed required measurement evidence is `INCOMPLETE`;
- an unprovable runtime/artifact identity is `INCOMPLETE`; this is distinct from a positively identified unauthorized fallback, which is `HARD_FAIL`;
- a wrong or unprovable run configuration is `INCOMPLETE` unless the candidate/runtime itself rejects the correctly configured required condition, which is `HARD_FAIL`;
- mid-run thermal throttling is recorded and retained but is not automatically `HARD_FAIL`; any resulting crash, forced termination, or noncompletion is classified by the corresponding frozen fatal rule;
- any hard-fail run in the frozen five-run set makes that candidate/target/condition `HARD_FAIL`;
- any incomplete run in the frozen five-run set makes that candidate/target/condition `INCOMPLETE`;
- a valid `MEDIAN_OF_FIVE` requires five complete numeric run records; replacing, dropping, or numerically imputing a failed/incomplete run is prohibited;
- target-native failure-signal identities and the noncompletion-detection watchdog must be pinned before execution;
- the exact watchdog timeout is not frozen by this question and must be fixed before execution without being changed per candidate or after results;
- candidate-specific failure exceptions and post-result failure-rule changes are prohibited;
- these binary failure semantics are independent of, and must precede, numeric performance pass/fail thresholds.

This policy freezes the candidate-neutral distinction between demonstrated fatal runtime/device failure and insufficient evidence. It does not invent a latency/throughput threshold, does not authorize execution, and does not convert missing telemetry into a candidate failure.

### 14.12 Predeclared target-usability performance gates

`PREDECLARED_TARGET_USABILITY_PERFORMANCE_GATES` means:

- performance hard gates are required before any live tournament/device execution may be authorized, but this question deliberately does not invent their exact numeric values;
- exact numeric thresholds must be supported by documented candidate-independent usability evidence and frozen before candidate results are observed;
- `COLD_START_TO_FIRST_TOKEN`, `READY_STATE_TTFT`, and `DECODE_TOKENS_PER_SECOND` must each receive a numeric hard gate before execution;
- `PREFILL_TOKENS_PER_SECOND` is recorded and secondary unless a later pre-result canonical decision separately promotes it to a hard gate;
- `MODEL_LOAD_TIME` remains a recorded component so cold-start decomposition remains auditable;
- `END_TO_END_RESPONSE_TIME` is recorded and secondary unless a later pre-result canonical decision separately promotes it to a hard gate;
- the same target uses identical threshold values across all comparable candidates;
- target-specific threshold values are allowed only when predeclared and justified by candidate-independent target/usability evidence before candidate results;
- candidate-specific performance thresholds are prohibited;
- candidate-result-derived thresholds are prohibited;
- post-result threshold changes and post-result target-specific threshold relaxation are prohibited;
- the primary numeric threshold aggregate is the valid median of five complete numeric runs under `FIVE_FRESH_RUNS_MEDIAN_WITH_WORST_CASE`;
- the worst-case run remains mandatory guardrail evidence and cannot be omitted merely because the median passes;
- `HARD_FAIL` and `INCOMPLETE` runs do not become favorable numeric values and cannot be dropped, replaced, or imputed to manufacture a passing aggregate;
- performance cannot compensate for failure of safety, minimum medical-quality, package, 8K Core memory, or universal runtime/device hard gates;
- the exact noncompletion watchdog timeout remains a separate unresolved pre-execution value and is not itself defined by this threshold policy.

This policy freezes how performance gates must be derived, scoped, and protected against result-driven manipulation. It does not freeze the numeric values themselves and does not authorize execution.

The complete minimum bundle measurement must include model weights plus every tokenizer, config, model-side runtime metadata, and other artifact required for the advertised minimum text/core installation. A general-purpose application/runtime binary may be reported separately only under a single frozen accounting rule applied identically to every candidate. Optional vision or other modality assets may be excluded from the minimum package only when they are genuinely optional and separately downloadable under the same policy for all candidates.

Every frozen target must be represented by named physical-device evidence where the target is a named device and by its corresponding reproducible resource description. The weak-laptop target is intentionally an exact CPU/RAM/ISA envelope; a retail laptop SKU may be added pre-execution if required without weakening that envelope.

The future evidence plan must cover all five frozen targets: iPhone 17 Pro 12 GB, iPhone 13 4 GB, Galaxy A56 5G 8 GB, Galaxy A16 5G 4 GB, and Intel N100 + 8 GB x86-64. Every target must use the common `8192`-token hard qualification context with symmetric `Q8_0` K/V cache, the fixed `7168` serialized-prompt / `1024` generation ceiling, logical batch `512`, physical ubatch `128`, no prompt/session/prefix cache reuse for the measured run, the same immutable llama.cpp core revision under its platform build manifest, the frozen platform-native peak-memory method, the `2 GiB` absolute Core peak ceiling, the frozen component timing decomposition, the five-fresh-run repetition/aggregation policy, the platform-native thermal-ready gate before each measured run with thermal state recorded before and after, per-run energy evidence using one pinned method within each target across all candidates, the universal device/runtime failure semantics, and the predeclared target-usability performance-gate policy. Energy is required evidence but has no V1 absolute raw-energy hard ceiling. Exact performance-gate values remain unresolved until separately bound from candidate-independent evidence before execution. The `16384`-token secondary stress tier is required on the iPhone 17 Pro 12 GB, Galaxy A56 5G 8 GB, and Intel N100 + 8 GB x86-64 targets where the pinned runtime supports that context, and must use the same symmetric `Q8_0` K/V cache, `15360` serialized-prompt / `1024` generation ceiling, `512/128` prompt-processing profile, cold/no-reuse semantics, shared core revision, memory measurement policy, timing-boundary policy, five-run policy, thermal-ready rule, per-run energy policy, universal failure semantics, and threshold-policy semantics. The 16K tier records peak memory and fails on OS memory termination but has no separately frozen absolute RAM ceiling. It may be collected on lower-resource targets where safe and comparable, but no candidate may receive a reduced 8K hard context, a different KV-cache type, a different prompt/generation allocation, a different batch profile, reused prompt state, a different core runtime revision, a different memory-accounting method, a higher 8K Core RAM ceiling, candidate-specific timing boundaries, a different measured-run count, a thermal-readiness exception, a candidate-specific energy method, a candidate-specific energy threshold, a candidate-specific failure exception, or a candidate-specific performance threshold because its memory scaling, tokenizer, template overhead, compatibility, observed prefill performance, throttling behavior, energy behavior, runtime stability, or measured latency/throughput is less favorable. iPhone coverage must be demonstrated through an Apple-compatible llama.cpp-compatible runtime/application path using the canonical GGUF identity or an explicitly proven equivalent path; it must not be inferred from desktop Apple Silicon results. Android and low-resource laptop coverage likewise require platform-specific execution evidence once separately authorized.

Each admitted `PRIMARY` candidate must also have two predeclared build roles when execution is eventually authorized:

1. a **reference build** governed by a common, frozen high-precision policy for primary common-core capability comparison; and
2. a **deployable build** governed by the canonical GGUF and `Q4_FLOOR_SMALLEST_PASSING` policy for device qualification on the named devices and resource envelopes.

The reference build supplies the evidence used to evaluate the frozen minimum medical-quality floor and other reference-quality requirements. Device/package qualification and the size-first ranking metric use the canonical deployable GGUF build. The deployable build must not replace the reference build for reference-quality claims, and the reference build must not be used to claim phone deployability. Quality/safety regression attributable to compression must be measured and reported separately under a frozen rule; if compression pushes the deployable build below a required hard gate, that candidate is not qualified for size-first ranking.

The exact reference precision, conversion toolchain revision, selected llama.cpp core commit SHA, concrete platform build manifests, architecture-specific equivalence rules, tokenizer/template identities and token-accounting implementation, exact memory instrumentation/tool invocation and sampling cadence where applicable, any 16K stress absolute RAM ceiling, exact timing instrumentation, exact numeric performance thresholds, exact platform thermal signal identities/mappings/ready thresholds, exact energy signal/tool/meter identities, calibration/uncertainty procedures, exact target-native failure-signal identities, exact noncompletion watchdog timeout, and minimum medical-quality threshold remain unresolved and must be frozen before execution. A policy may not be changed per candidate after results are observed. Any future energy hard gate is outside the frozen V1 policy and requires separate canonical evidence before results.

Before execution authorization, clarification/planning must additionally define:

- exact package-byte measurement procedure and exclusions;
- exact immutable llama.cpp core commit and GGUF conversion-toolchain identities;
- exact platform build manifests for every required execution path, including compiler/toolchain, relevant flags/backend choices, target ABI, wrapper/application identity where applicable, and produced runtime artifact identity when available;
- exact final Q5/Q4 ladder order, conversion flags, and any calibration/imatrix inputs and quarantine rules;
- verification that the pinned runtime/backend implements the frozen symmetric `Q8_0` K/V cache semantics consistently across all required platform paths;
- exact tokenizer/template identities and a reproducible token-accounting implementation that counts all system/template/context/input tokens inside the frozen serialized-prompt ceilings;
- verification that the pinned runtime/backend implements logical batch `512`, physical ubatch `128`, and the cold/no-reuse prompt-processing semantics consistently across all required platform paths;
- exact platform memory instrumentation/tool invocation and sampling cadence where applicable, consistent with `PLATFORM_NATIVE_PEAK_MEMORY` and the absolute `2 GiB` 8K Core gate;
- whether the required 16K stress tier should receive an additional absolute RAM ceiling or remain governed only by peak recording and OS-termination failure semantics;
- exact timing instrumentation and event definitions consistent with `COMPONENT_TIMING_COLD_AND_READY`;
- the candidate-independent usability evidence basis and exact predeclared numeric hard-gate values for cold-start-to-first-token, ready-state TTFT, and decode throughput, plus any separately justified promotion of prefill throughput or end-to-end response time to a hard gate, consistent with `PREDECLARED_TARGET_USABILITY_PERFORMANCE_GATES`;
- exact platform-native thermal signal identities, readiness mappings/thresholds, sampling/recording method, and evidence format consistent with `PLATFORM_NATIVE_THERMAL_READY_GATE`;
- exact energy signal/tool/meter identities, calibration/uncertainty procedure, raw-unit semantics, and evidence format consistent with `PLATFORM_NATIVE_ENERGY_PER_RUN`; V1 has no absolute raw-energy hard ceiling, and any future energy hard-gate proposal requires a separate canonical evidence basis and decision before results;
- exact target-native failure-signal identities and the exact candidate-neutral noncompletion watchdog timeout/evidence format consistent with `UNIVERSAL_FATAL_FAILURES_AND_FAIL_CLOSED_EVIDENCE`;
- exact per-slice canonical quarantine purpose and selection eligibility, including proof that the mapping is frozen before payload access/execution and identical across comparable candidates, consistent with `PREDECLARED_QUARANTINE_PURPOSE_PER_SLICE`;
- exact per-benchmark payload access route/transport identity, immutable source revision or digest, license/access-class proof, contamination disposition, and any later separate payload-access authorization identity, consistent with `METADATA_FIRST_EXACT_ARTIFACT_BINDING_BEFORE_ACCESS`;
- exact contamination evidence/disposition for every clean-required candidate derivation and future benchmark payload, including proof for any `NOT_APPLICABLE` claim that the path is truly outside the contamination condition; for quantization, proof that any `NOT_APPLICABLE` path is weight-only/data-free with exact source-weight/toolchain/flags and no calibration/imatrix/benchmark/Gold/training/dev/teacher/provider payload input, consistent with `USE_CLASS_SPECIFIC_FAIL_CLOSED_CONTAMINATION_BINDING`;
- how mandatory 16K stress evidence is interpreted where in scope without retroactively changing the 8K hard qualification rule;
- the minimum medical-quality floor below which a smaller artifact cannot qualify;
- the secondary metric order used only after complete deployable package bytes tie, including whether energy is included under its same-target/same-method restriction.

Parameter count and upstream marketing claims remain descriptive only. No target substitution, context reduction, KV-cache substitution, prompt/generation reallocation, batch/ubatch substitution, prompt-state reuse, runtime-core substitution, memory-accounting substitution, 8K Core RAM-ceiling increase, candidate-specific timing-boundary substitution, measured-run-count substitution, failed-run replacement, post-hoc run exclusion, partial-median substitution, thermal-readiness exception, fixed-sleep substitution for thermal proof, post-result thermal-rule change, candidate-specific energy-method substitution, post-result energy-method change, candidate-specific energy-threshold creation, post-result energy-threshold creation, cross-platform raw-energy ranking substitution, raw-energy hard disqualification in V1, candidate-specific failure exception, post-result failure-rule change, candidate-specific performance threshold, candidate-result-derived performance threshold, post-result performance-threshold change, post-result target-specific performance-threshold relaxation, benchmark-purpose remapping, candidate-specific benchmark-purpose mapping, external-evaluation-to-selection promotion, mutable/unpinned benchmark-payload substitution, post-access payload substitution, candidate-specific payload-version substitution, self-asserted contamination `NOT_APPLICABLE`, candidate-specific contamination exception, post-result contamination reclassification, data-assisted quantization presented as data-free `NOT_APPLICABLE`, remaining envelope boundary, quantization rule, medical-quality threshold, or secondary ranking rule may be chosen after candidate results are known.

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
- exact frozen benchmark slice manifest identity, per-slice canonical quarantine purpose/selection eligibility, proof that every purpose was frozen before payload access/execution, and proof that every comparable primary candidate used the identical authorized slice set and purpose mapping;
- exact benchmark payload artifact/split identity, immutable source revision or digest, resolved license/access class, contamination disposition, payload-access authorization identity, access route/transport identity, and proof that the accessed bytes preserve the canonical artifact identity;
- proof that no candidate-specific payload version or post-access artifact substitution was used;
- exact contamination evidence/rationale identity for every required disposition, including proof of `ASSESSED_CLEAN` or evidence-backed `NOT_APPLICABLE` where a clean-required use applies;
- for any quantization/derivation using `NOT_APPLICABLE`, exact proof of weight-only/data-free transformation: exact source-weight identity, transform/toolchain identity, frozen flags, and absence of calibration/imatrix/benchmark/Gold/training/dev/teacher/provider payload inputs;
- exact device/resource identity where device evidence is claimed;
- exact context/KV/token-budget configuration used for each device result, including symmetric Q8_0 K/V identity and serialized-prompt/generation ceilings for primary qualification;
- exact tokenizer/template identities and serialized-token accounting record;
- exact logical batch `512`, physical ubatch `128`, and evidence that no prohibited prompt/session/prefix state was reused in the measured run;
- exact platform-native memory measurement identity/configuration, accounted process set, pre-load baseline, absolute peak bytes, peak delta, and any OS memory-termination event;
- explicit proof that each 8K Core result is at or below `2147483648` absolute peak bytes under its frozen platform-native primary metric;
- exact timing-boundary identity and component records for cold-start-to-first-token, model load, ready-state TTFT, prefill throughput, decode throughput, and end-to-end response time;
- exact candidate-independent performance-threshold evidence artifact/decision identity and exact target-specific threshold values, including proof that the same target thresholds apply identically across candidates and were frozen before candidate results;
- exact five-run raw records per candidate/target/condition, run index/order, fresh-process/fresh-load evidence, failed/terminated/incomplete-run disposition, proof that any numeric median uses five complete runs, median-of-five primary aggregate where valid, and worst-case run record;
- exact platform-native thermal signal identity/configuration, pre-run and post-run thermal states, thermal-ready determination, cooldown/readiness evidence, and any thermal termination or throttling event;
- exact energy signal/tool/meter identity/configuration for each target, pre-run baseline, post-run record, run delta where supported, raw unit/accounting semantics, measurement uncertainty where available, and failed/missing-capture disposition for every measured run;
- explicit V1 energy-qualification record binding `V1_ABSOLUTE_ENERGY_HARD_CEILING=NONE`, any predeclared secondary-ranking use, and proof that no candidate-specific or post-result energy threshold was applied;
- exact target-native failure-signal identity/configuration, runtime/artifact/backend identity proof, run-configuration proof, noncompletion-watchdog identity/value, and final `HARD_FAIL`/`INCOMPLETE`/complete disposition for every measured run;
- exact packaged artifact identity and byte size where distribution evidence is claimed;
- exact result-set evidence artifact IDs;
- deterministic tournament report identity.

A mutable tag, model family name, `latest`, branch name, mutable runtime branch, mutable benchmark revision, marketplace label, or unpinned runtime/payload version is not sufficient identity.

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
- adding a benchmark/slice to execution outside the frozen canonical slice manifest;
- using different benchmark/slice manifests for comparable primary candidates;
- candidate-specific benchmark/slice selection;
- adding, removing, or reclassifying a benchmark slice after candidate results are observed;
- using a public canonical test split to select the winner despite `PUBLIC_EXTERNAL_EVAL.can_select_model=false`;
- executing a `REFERENCE_ONLY`, mixed/unbound component, unresolved-license, gated, private, or private-Gold asset without separate canonical reconciliation and authorization;
- treating registry/metadata inspection as benchmark payload access or execution authority;
- treating a `PUBLIC` + `DEVELOPMENT` registry label as proof of `CHECKPOINT_SELECTION` eligibility without an explicit quarantine-purpose mapping;
- attempting to execute a slice whose canonical quarantine purpose is missing, ambiguous, or unresolved;
- assigning `CHECKPOINT_SELECTION` to a slice whose canonical source class has `can_select_model=false`;
- using candidate-specific purpose mappings for the same slice;
- remapping a slice purpose after candidate results are observed;
- promoting a `PUBLIC_EXTERNAL_EVAL` slice or result into model-selection evidence after results are observed;
- relabeling `DEV`, `CHECKPOINT_SELECTION`, or `PUBLIC_EXTERNAL_EVAL` after results to rescue a selection;
- obtaining, downloading, copying, caching, or API-retrieving benchmark payload bytes before a separate explicit payload-access authorization;
- accessing a payload without exact artifact/split identity, immutable source revision or digest, resolved license/access class, frozen quarantine purpose, and contamination disposition;
- accessing a mutable `latest`, unpinned branch head, changing remote object, or otherwise unbound payload;
- accessing gated/private payload bytes without separate authorization or accessing Private Gold under this clarification authority;
- treating external-submission-only ground truth as locally accessible Gold;
- creating a local payload cache or copy under the current no-access authority;
- using a candidate-specific benchmark payload version;
- substituting a different benchmark artifact after access or after candidate results are observed;
- treating an access failure or benchmark identity mismatch as permission to use a substitute rather than `INCOMPLETE`;
- missing a required contamination disposition before benchmark-payload access or candidate execution;
- treating `PENDING`, `NOT_ASSESSED`, `OVERLAP_OR_HIGH_RISK`, or contradictory contamination evidence as clean for a Spec 003 clean-required use;
- self-asserting `NOT_APPLICABLE` without evidence that the exact path is truly outside the contamination condition;
- assigning `NOT_APPLICABLE` to model-weight quantization that uses calibration, imatrix, benchmark/Gold, training/dev, teacher/provider output, or any other external data input;
- claiming data-free quantization `NOT_APPLICABLE` without exact source-weight identity, exact transform/toolchain identity, frozen transform flags, and evidence of absent external data inputs;
- granting a candidate-specific contamination exception;
- reclassifying contamination after candidate results are observed;
- non-comparable metric vectors;
- complete minimum text/core bundle exceeding `700 MiB` under the frozen accounting rule;
- absolute platform-native peak memory exceeding `2147483648` bytes during any frozen 8K Core target qualification run;
- using baseline-subtracted peak delta instead of absolute peak to evade the `2 GiB` 8K Core hard gate;
- candidate-specific, target-specific, or post-result increase of the frozen `2 GiB` Core ceiling;
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
- failure to use the frozen platform-native memory metric family for a measured target path;
- omission of required helper/runtime/wrapper processes from the memory-accounted qualification process set;
- missing pre-load baseline, absolute peak, or peak-delta record where the frozen memory policy requires them;
- iOS memory-pressure termination, Android LMK/OOM termination, or Linux cgroup OOM termination during a measured qualification or required stress run;
- substituting a lower-looking platform memory metric or baseline-subtracted value as if it were the frozen absolute peak evidence;
- mixing unlike iOS/Android/Linux raw memory values into a cross-platform ranking metric;
- missing required timing components under `COMPONENT_TIMING_COLD_AND_READY`;
- including model-load time inside ready-state TTFT or excluding model-load time from cold-start-to-first-token contrary to the frozen timing policy;
- candidate-specific, target-specific, or post-result timing-boundary changes;
- prompt/session/prefix-cache reuse that makes a measured timing result non-cold or non-comparable;
- using fewer or more than five measured runs for any candidate/target/condition;
- starting a measured run from a reused process or omitting the required fresh model load;
- using a non-measured warm-up request before a measured request;
- replacing a failed or terminated measured run;
- excluding a measured run post hoc from the retained raw set or primary aggregate;
- failing to retain all raw runs, record the median-of-five primary aggregate where valid, or record the worst-case run;
- calculating or reporting a median-of-five from fewer than five complete required numeric run records;
- candidate-specific or target-specific measured-run counts;
- missing the required platform-native thermal-state record before or after a measured run;
- starting a measured run when the frozen platform-native readiness signal does not establish thermal-ready state or while known active throttling is present;
- using a fixed sleep interval as the only proof of thermal readiness;
- using an unpinned or candidate-specific thermal signal/readiness rule;
- granting a candidate-specific thermal exception or changing the thermal-readiness rule after results are known;
- failing to retain a thermal termination or OS/runtime throttling event with the affected run evidence;
- missing required energy capture for a measured run;
- using an unpinned or candidate-specific energy signal/tool/meter method;
- changing the target energy method after candidate results are known;
- comparing raw energy values across unlike targets/methods as if they were one scientific ranking metric;
- omitting raw energy unit/accounting semantics or a required failed/missing-capture disposition;
- discarding a failed-run energy record that was captured;
- applying an absolute raw-energy value as a V1 hard-disqualification threshold;
- creating or applying a candidate-specific energy threshold;
- creating an energy threshold after candidate results are observed;
- allowing favorable energy evidence to compensate for safety, minimum medical-quality, package, or 8K Core memory hard-gate failure;
- entering energy into secondary ranking without a predeclared same-target/same-method rule;
- runtime initialization failure on a correctly configured required target path;
- canonical artifact load failure on a correctly configured required target path;
- inability of a correctly configured candidate/runtime to execute the frozen required Core condition;
- process crash, abnormal termination, or OS non-memory forced termination during a measured run;
- measured-request noncompletion once established by the frozen operational watchdog or explicit runtime/OS failure evidence;
- known unauthorized runtime/backend/artifact fallback during a measured run;
- treating missing/malformed telemetry, an unprovable runtime/artifact identity, or a wrong/unprovable run configuration as a favorable result rather than `INCOMPLETE`;
- treating missing evidence as a candidate hard failure when the actual runtime outcome cannot be proven;
- allowing a hard-fail run or incomplete run to be replaced, dropped, or numerically imputed to preserve a five-run aggregate;
- granting a candidate-specific runtime/device failure exception or changing failure semantics after results are known;
- execution beginning before numeric hard-gate values for cold-start-to-first-token, ready-state TTFT, and decode throughput are frozen from documented candidate-independent usability evidence;
- creating or applying a candidate-specific performance threshold;
- deriving a performance threshold from observed candidate results;
- changing a performance threshold after candidate results are observed;
- relaxing a target-specific performance threshold after candidate results are observed;
- applying different performance thresholds to comparable candidates on the same target;
- treating a hard-fail or incomplete run as a synthetic numeric value, or omitting it, to manufacture a passing median;
- allowing favorable performance to compensate for safety, minimum medical-quality, package, 8K Core memory, or universal runtime/device hard-gate failure;
- missing required `16384`-token stress evidence on an 8-GB-class-or-higher target where the pinned runtime supports it;
- post-result reduction or candidate-specific adjustment of the frozen 8K hard context, Q8_0 KV policy, prompt/generation budget, cold `512/128` prompt-processing profile, shared runtime identity policy, platform-native memory measurement policy, `2 GiB` 8K Core memory ceiling, component timing policy, five-run repetition policy, thermal-readiness policy, energy-measurement policy, V1 energy-qualification policy, universal device/runtime failure policy, or performance-threshold policy;
- post-result substitution of a frozen named device/resource target or weakening of its resource class;
- missing required reference or deployable build evidence under `DUAL_BUILD_BASELINE_AND_DEPLOYABLE`;
- unmeasured required compression regression;
- incomplete or candidate-specific package accounting that would make the size metric non-comparable;
- omitting required assets from the measured minimum package or inconsistently excluding optional modality assets;
- substituting an MLX/MLC/Core ML/native derivative for the canonical GGUF evidence without a separately frozen equivalence contract;
- envelope boundary, runtime, build policy, KV policy, token-budget policy, prompt-processing policy, memory-measurement policy, timing policy, repetition/aggregation policy, thermal-readiness policy, energy-measurement policy, V1 energy-qualification policy, universal device/runtime failure policy, performance-threshold policy, quantization policy, package threshold, Core RAM threshold, medical-quality threshold, benchmark-slice policy, benchmark-purpose policy, benchmark-access policy, contamination-proof policy, or ranking-rule changes after results are observed;
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
6. **PARTIALLY RESOLVED / PUBLIC-DEVELOPMENT METADATA SCOPE + MANIFEST + PURPOSE POLICIES FROZEN / EXACT PRIMARY SELECTION MANIFEST AND NAMED PURPOSE MAPPINGS PENDING:** `CANONICAL_PUBLIC_SLICE_MANIFEST_ONLY` limits future executable baseline scope to explicit canonical Spec 001 records/slices, while `PREDECLARED_QUARANTINE_PURPOSE_PER_SLICE` requires one canonical purpose per executable slice before payload access/execution and preserves `can_select_model` semantics. The current `PUBLIC` + `DEVELOPMENT` registry envelope is `healthbench_core`, `healthbench_consensus`, `healthbench_hard`, `healthbench_professional`, `medxpertqa`, and `pubmedqa`, but this metadata envelope is not itself an execution or winner-selection manifest. Public canonical test splits are `PUBLIC_EXTERNAL_EVAL` and cannot select a model. Candidate-specific purpose mapping and post-result purpose remapping/promotion are prohibited. MedXpertQA text test is external-eval only; its multimodal slices remain secondary non-ranking if separately authorized. MedXpertQA text dev, HealthBench, and PubMedQA exact purpose mappings remain unresolved. Any future primary-selection manifest must bind exact benchmark/artifact/split identity, purpose, metric IDs/directions, contamination/quarantine disposition, and selection eligibility before payload access/execution. Benchmark payload access/execution and Private Gold remain unauthorized.
7. **PARTIALLY RESOLVED / CANONICAL FLOOR PRESERVED:** zero-violation sentinel rules apply where already frozen by Spec 002, while selective risk, Arabic clinical parity, and lab extraction remain `NO_PASS_UNTIL_FROZEN` pending the canonical clinical/statistical evidence requirements. Exact statistical thresholds remain unresolved and must not be invented from candidate results.
8. **RESOLVED TARGET SET + CONTEXT + KV + TOKEN-BUDGET + PROMPT-PROCESSING + RUNTIME-IDENTITY + MEMORY + TIMING + REPETITION + THERMAL-READINESS + ENERGY-MEASUREMENT + V1 ENERGY-QUALIFICATION + UNIVERSAL FAILURE + PERFORMANCE-THRESHOLD POLICY / VALUES PENDING:** `MASS_REACH_FIVE_TARGET_SET` freezes iPhone 17 Pro 12 GB, iPhone 13 4 GB, Galaxy A56 5G 8 GB, Galaxy A16 5G 4 GB, and Intel N100 + 8 GB x86-64 as required evidence targets. `8K_CORE_16K_STRESS`, `Q8_0_SYMMETRIC_KV_CORE`, `7K_PROMPT_1K_GENERATION`, and `B512_U128_COLD_NO_REUSE` freeze the common Core/stress comparability condition. `PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST` freezes one immutable llama.cpp core revision across target paths. `PLATFORM_NATIVE_PEAK_MEMORY` freezes the platform-native memory measurement family and full-process-set accounting. `2G_CORE_HARD_CAP` freezes an absolute `2 GiB` peak-memory hard ceiling for the common 8K Core condition on all five targets. `COMPONENT_TIMING_COLD_AND_READY` freezes cold-vs-ready timing decomposition and common timing boundaries. `FIVE_FRESH_RUNS_MEDIAN_WITH_WORST_CASE` freezes five fresh-process measured runs, zero warm-ups, median-of-five primary aggregation, worst-case recording, raw-run retention, and failed-run no-replacement semantics. `PLATFORM_NATIVE_THERMAL_READY_GATE` freezes platform-native pre/post thermal-state recording, a thermal-ready start gate, as-needed cooldown, no fixed-sleep proof, predeclared run order, and no candidate-specific/post-result thermal exceptions. `PLATFORM_NATIVE_ENERGY_PER_RUN` freezes one per-run energy-evidence method within each target across candidates, full-cold-run measurement scope, raw unit semantics, no candidate-specific/post-result method changes, and no cross-platform raw-energy ranking. `ENERGY_REQUIRED_EVIDENCE_NO_V1_ABSOLUTE_HARD_GATE` freezes energy as required evidence without an absolute raw-value V1 hard gate and permits only predeclared same-target/same-method secondary comparison. `UNIVERSAL_FATAL_FAILURES_AND_FAIL_CLOSED_EVIDENCE` freezes candidate-neutral runtime/device fatal events vs `INCOMPLETE` evidence semantics, requires five complete numeric runs for a median-of-five, and prohibits candidate-specific/post-result failure-rule changes. `PREDECLARED_TARGET_USABILITY_PERFORMANCE_GATES` freezes candidate-independent pre-result threshold derivation, requires future hard gates for cold-start-to-first-token, ready-state TTFT, and decode throughput, and prohibits candidate-specific/result-derived/post-result threshold manipulation. The exact selected core SHA, concrete build manifests, tokenizer/template accounting implementation, exact memory/timing instrumentation details, exact numeric performance thresholds, exact thermal signal identities/mappings/ready thresholds, exact energy signal/tool/meter identities, calibration/uncertainty details, exact target-native failure-signal identities, exact noncompletion watchdog timeout, and any separate 16K absolute RAM ceiling remain unresolved.
9. **RESOLVED CORE RAM GATE + PERFORMANCE/REPETITION/THERMAL/ENERGY + UNIVERSAL FAILURE + PERFORMANCE-THRESHOLD POLICY / NUMERIC VALUES PENDING:** `SUB_700MB_MASS_REACH` freezes the `700 MiB` hard package ceiling and `2G_CORE_HARD_CAP` turns the prior `<=2 GiB` 8K engineering target into an absolute platform-native hard qualification ceiling on all five Core target runs. `PLATFORM_NATIVE_PEAK_MEMORY` defines how peak memory is measured. `COMPONENT_TIMING_COLD_AND_READY` defines how cold-start and ready-state performance components are recorded, `FIVE_FRESH_RUNS_MEDIAN_WITH_WORST_CASE` defines repeated-run and aggregation semantics, `PLATFORM_NATIVE_THERMAL_READY_GATE` requires each measured run to begin from a frozen platform-native thermal-ready state, `PLATFORM_NATIVE_ENERGY_PER_RUN` requires energy evidence for every measured run under one candidate-neutral method per target, `ENERGY_REQUIRED_EVIDENCE_NO_V1_ABSOLUTE_HARD_GATE` establishes that V1 does not use an absolute raw-energy hard ceiling, `UNIVERSAL_FATAL_FAILURES_AND_FAIL_CLOSED_EVIDENCE` freezes what makes a measured run fatal versus merely evidentially incomplete, and `PREDECLARED_TARGET_USABILITY_PERFORMANCE_GATES` freezes how candidate-independent performance hard gates must be selected before execution. The required 16K stress tier records peak memory and fails on OS memory termination but has no separately frozen absolute RAM ceiling. Exact sampling/tool invocation, timing instrumentation, numeric performance values, thermal signal mappings/thresholds, energy tool/meter identities, calibration/uncertainty details, target-native failure-signal identities, and watchdog timeout remain unresolved.
10. **RESOLVED POLICY:** `DUAL_BUILD_BASELINE_AND_DEPLOYABLE` plus `Q4_FLOOR_SMALLEST_PASSING`; primary capability comparison uses a frozen reference build, while the canonical deployable GGUF is the smallest allowed Q5/Q4-class artifact that passes every hard gate. Sub-4-bit artifacts are excluded from the V1 `PRIMARY` canonical release. Exact reference precision and frozen conversion/calibration details remain pending.
11. **RESOLVED RUNTIME IDENTITY POLICY / VALUES PENDING:** `GGUF_LLAMA_CPP_CANONICAL` plus `PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST`; GGUF + llama.cpp is the canonical mass-distribution artifact/runtime family, one immutable core commit must be shared across all target paths, and platform-specific builds must be exact-manifest-bound. MLX/MLC/Core ML/native builds remain optional derivatives. The exact core commit SHA, conversion revision, compiler/toolchain versions, build/backend flags, wrapper/application identities, and produced runtime artifact identities remain to be frozen before execution.
12. **RESOLVED POLICY / EXACT PER-ASSET DISPOSITIONS PENDING:** `USE_CLASS_SPECIFIC_FAIL_CLOSED_CONTAMINATION_BINDING` preserves the canonical Spec 003 rule that `MODIFICATION_OR_DERIVATION`, `TEACHER_OR_SYNTHETIC_GENERATION`, and `TRAINING_OR_ADAPTATION` are clean-contamination-required uses. For such a use, only `ASSESSED_CLEAN` or explicit evidence-backed `NOT_APPLICABLE` may contribute to eligibility; `NOT_APPLICABLE` is permitted only when the asset/path is truly outside the contamination condition and cannot be self-asserted. Exact model-weight quantization may use `NOT_APPLICABLE` only for a proven weight-only/data-free transform bound to exact source-weight identity, transform/toolchain identity, and frozen flags, with no calibration/imatrix/benchmark/Gold/training/dev/teacher/provider payload input. A quantization using any such data requires contamination assessment instead. Pending/not-assessed contamination blocks clean-required use; known overlap/high risk prohibits it. Candidate-specific exceptions and post-result contamination reclassification are prohibited. Exact candidate/slice records and dispositions remain to be computed from exact evidence before access/execution; no payload/weight/conversion authority is granted.
13. **PARTIALLY RESOLVED / ACCESS PRECONDITIONS FROZEN / EXACT PER-BENCHMARK ROUTES + ACCESS AUTHORITY PENDING:** `METADATA_FIRST_EXACT_ARTIFACT_BINDING_BEFORE_ACCESS` allows read-only public metadata inspection but requires separate explicit authorization before any benchmark payload bytes are obtained, cached, copied, or executed. Any future access must bind exact artifact/split identity, immutable revision/digest, resolved license/access class, frozen quarantine purpose, contamination disposition, and an identity-preserving access route. Mutable/unpinned payloads, candidate-specific payload versions, post-access substitution, unauthorized gated/private access, and local Private Gold are prohibited. External-submission-only ground truth does not become local Gold. Access failures or identity mismatches fail closed as `INCOMPLETE`. Exact artifact-specific transport routes and any payload-access authorization remain unresolved; current benchmark payload access/execution authorities remain `NONE`.
14. **RESOLVED POLICY:** `FULLY_ADMITTED_PRIMARY_ONLY`; unresolved/conditional candidates remain outside the frozen primary ranking manifest, and candidate-set freeze occurs only after admission reconciliation.
15. What compute/spend budget is permitted for the tournament, and which actions remain zero-spend/read-only until execution authorization?
16. What independent review and exact-head evidence must be present before any execution activation can be proposed?
17. **RESOLVED:** `QUALITY_FLOOR_THEN_SIZE_FIRST`; after all hard gates and the frozen minimum medical-quality floor pass, complete deployable package bytes are the first lexicographic ranking metric with `LOWER_BETTER`.

Bounded clarification session 1 on 2026-08-23 is complete at five accepted questions. Bounded clarification session 2 is complete at five accepted questions plus two explicit founder directives. Bounded clarification session 3 is complete at five accepted questions. Bounded clarification session 4 is complete at five accepted questions. Bounded clarification session 5 is complete at five accepted questions. Bounded clarification session 6 is in progress at four accepted questions. Completion of any bounded session does **not** complete the overall clarification lifecycle. The unresolved factual/evidence requirements above remain active and prevent the overall clarification lifecycle from being declared complete or advancing to `PLAN`.

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
- freezes `CANONICAL_PUBLIC_SLICE_MANIFEST_ONLY` as the future benchmark-source boundary, preserves the six current `PUBLIC` + `DEVELOPMENT` registry IDs as a metadata eligibility envelope without pretending they are already a selectable execution manifest, forbids public canonical test splits from selecting the winner, keeps reference/mixed-unbound/gated/private/Gold assets fail-closed, and keeps exact primary-selection purpose/slice mapping separately unresolved until pre-execution binding;
- freezes `PREDECLARED_QUARANTINE_PURPOSE_PER_SLICE`, requiring one candidate-neutral canonical purpose per executable slice before payload access/execution, requiring `can_select_model=true` for selection use, keeping public canonical test splits external-eval-only, prohibiting candidate-specific/post-result purpose remapping or promotion, and keeping unresolved-purpose assets non-executable while exact MedXpertQA text-dev/HealthBench/PubMedQA mappings remain pending;
- freezes `METADATA_FIRST_EXACT_ARTIFACT_BINDING_BEFORE_ACCESS`, permitting metadata-only inspection while requiring separate authorization plus exact immutable artifact identity, resolved license/access class, frozen purpose, contamination disposition, and identity-preserving access before any payload bytes may be obtained; prohibits mutable/unbound, candidate-specific, substituted, unauthorized gated/private, or local Private Gold payload access while keeping concrete per-benchmark routes and access authority unresolved;
- freezes `USE_CLASS_SPECIFIC_FAIL_CLOSED_CONTAMINATION_BINDING`, preserving Spec 003 clean-required uses and allowing `NOT_APPLICABLE` only with explicit evidence that the path is truly outside the contamination condition; permits it for model-weight quantization only when the transform is proven weight-only/data-free with exact source/toolchain/flags and no calibration/imatrix/benchmark/Gold/training/dev/teacher/provider payload input, otherwise requiring contamination assessment; prohibits self-asserted N/A, candidate-specific exceptions, and post-result reclassification while keeping exact per-asset dispositions pending;
- freezes `MASS_REACH_FIVE_TARGET_SET` while keeping exact execution/performance threshold values separately unresolved until supported by candidate-independent pre-execution evidence;
- requires evidence for iPhone 17 Pro 12 GB, iPhone 13 4 GB, Galaxy A56 5G 8 GB, Galaxy A16 5G 4 GB, and Intel N100 + 8 GB x86-64 without post-result target weakening;
- freezes `8K_CORE_16K_STRESS`, requiring an `8192`-token hard qualification context on all five targets and `16384`-token secondary stress evidence on 8-GB-class-or-higher targets where the pinned runtime supports it;
- freezes `Q8_0_SYMMETRIC_KV_CORE`, requiring symmetric `Q8_0` K/V cache for primary hard qualification and required stress evidence, prohibiting asymmetric primary KV, while keeping runtime/backend identity and measured memory/performance effects separately unresolved until pre-execution qualification;
- freezes `7K_PROMPT_1K_GENERATION`, requiring `7168` serialized-prompt + `1024` generation tokens for the 8K hard condition and `15360` + `1024` for the 16K stress condition, with system/template tokens counted inside the prompt ceiling and no candidate-specific reallocation;
- freezes `B512_U128_COLD_NO_REUSE`, requiring logical batch `512`, physical ubatch `128`, and no prompt/session/prefix cache reuse for measured qualification/stress runs, identically across comparable candidates and frozen targets;
- freezes `PINNED_CORE_COMMIT_PLATFORM_BUILD_MANIFEST`, requiring one immutable llama.cpp core commit across all comparable candidates/targets, exact platform build manifests, and no mutable/candidate-specific/post-result runtime substitution while keeping the exact core SHA/build values unresolved until separately reviewed pre-execution binding;
- freezes `PLATFORM_NATIVE_PEAK_MEMORY`, requiring platform-native peak metrics, full qualification-process-set accounting, baseline/absolute/delta records, OS memory-termination hard failures, and no cross-platform raw-memory ranking;
- freezes `2G_CORE_HARD_CAP`, requiring absolute platform-native peak memory `<=2 GiB` on every frozen 8K Core target, using absolute peak rather than baseline delta as the hard-gate input, while keeping any separate 16K absolute ceiling unresolved;
- freezes `COMPONENT_TIMING_COLD_AND_READY`, requiring cold-start-to-first-token and model-load records plus ready-state TTFT, prefill throughput, decode throughput, and end-to-end response-time records under identical candidate-neutral timing boundaries;
- freezes `FIVE_FRESH_RUNS_MEDIAN_WITH_WORST_CASE`, requiring exactly five fresh-process/fresh-load measured runs per candidate/target/condition, one measured request per load, zero non-measured warm-ups, median-of-five primary aggregation, worst-case recording, retention of all raw runs and failed runs, and no replacement/post-hoc exclusion;
- freezes `PLATFORM_NATIVE_THERMAL_READY_GATE`, requiring platform-native pre/post thermal-state records, a thermal-ready start gate, no known active throttling at run start, pinned signal identity before execution, as-needed cooldown rather than fixed-sleep proof, predeclared run order, and no candidate-specific/post-result thermal exceptions, while keeping exact platform ready thresholds unresolved;
- freezes `PLATFORM_NATIVE_ENERGY_PER_RUN`, requiring per-run full-cold-window energy evidence under one pinned method within each target across candidates, raw unit/accounting semantics, uncertainty where available, no candidate-specific/post-result method change, `INCOMPLETE` on missing required energy capture, and no cross-platform raw-energy ranking, while keeping exact tool/meter identities and calibration details unresolved;
- freezes `ENERGY_REQUIRED_EVIDENCE_NO_V1_ABSOLUTE_HARD_GATE`, requiring energy evidence while setting no absolute raw-energy hard ceiling in V1, prohibiting raw-energy hard disqualification and candidate-specific/post-result energy thresholds, allowing only predeclared same-target/same-method secondary ranking, and requiring separate canonical evidence for any future energy hard gate;
- freezes `UNIVERSAL_FATAL_FAILURES_AND_FAIL_CLOSED_EVIDENCE`, classifying demonstrated runtime initialization/load/Core-execution/crash/forced-termination/noncompletion/unauthorized-fallback events as `HARD_FAIL`, classifying missing/malformed/unprovable evidence as `INCOMPLETE`, requiring any hard-fail or incomplete run to control the five-run condition disposition, prohibiting partial medians, and keeping exact failure-signal identities/watchdog timeout unresolved until pre-execution binding;
- freezes `PREDECLARED_TARGET_USABILITY_PERFORMANCE_GATES`, requiring candidate-independent documented pre-result evidence for numeric hard-gate values, future hard gates for cold-start-to-first-token/ready-state TTFT/decode throughput, identical same-target thresholds across candidates, no candidate-specific/result-derived/post-result threshold manipulation, median-of-five primary threshold aggregation, and mandatory worst-case guardrail evidence while keeping the exact numeric values unresolved;
- enforces the `700 MiB` complete minimum text/core bundle ceiling under one honest, candidate-neutral accounting rule;
- treats `<=600 MiB` and `<=500 MiB` as engineering/stretch package targets while treating the previously targeted `<=2 GiB` value as a now-frozen hard gate only for the common 8K Core condition;
- uses canonical GGUF + immutable llama.cpp compatibility as the minimum mass-distribution path, with optional optimized derivatives kept semantically and evidentially separate;
- enforces `Q4_FLOOR_SMALLEST_PASSING` and prohibits a sub-4-bit V1 primary release from winning merely because it is smaller;
- applies `QUALITY_FLOOR_THEN_SIZE_FIRST` only after all non-compensable safety/provenance/license/minimum-medical-quality/package/Core-memory/runtime-device/performance hard gates pass;
- keeps Hugging Face adoption/category-leadership KPIs outside the scientific ranking and claims boundary;
- preserves Spec 004 deterministic/fail-closed comparison semantics;
- records accepted clarification decisions without contradicting unresolved gates;
- resolves all clarification requirements that materially affect candidate admission, comparability, device qualification, execution planning, and exact-head review before advancing to `PLAN`;
- grants no model, weight, benchmark payload, private Gold, provider, PHI, gated-asset, runtime-execution, or tournament-execution authority.

No bounded clarification session is a declaration that the full clarification lifecycle is complete until every material unresolved requirement is reconciled and independently reviewed.

## 19. Exit and next lifecycle step

Current working state after bounded session 5 completion and bounded session 6 questions 1–4 acceptance of `CANONICAL_PUBLIC_SLICE_MANIFEST_ONLY`, `PREDECLARED_QUARANTINE_PURPOSE_PER_SLICE`, `METADATA_FIRST_EXACT_ARTIFACT_BINDING_BEFORE_ACCESS`, and `USE_CLASS_SPECIFIC_FAIL_CLOSED_CONTAMINATION_BINDING`:

```text
SPEC_005_SPECIFICATION=DEFINED_CANONICALLY
CLARIFICATION_SESSION_1=5_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_2=5_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_2_STATUS=COMPLETE_BOUNDED_SESSION
CLARIFICATION_SESSION_3=5_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_3_STATUS=COMPLETE_BOUNDED_SESSION
CLARIFICATION_SESSION_4=5_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_4_STATUS=COMPLETE_BOUNDED_SESSION
CLARIFICATION_SESSION_5=5_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_5_STATUS=COMPLETE_BOUNDED_SESSION
CLARIFICATION_SESSION_6=4_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_6_STATUS=IN_PROGRESS
BASELINE_EVALUATION_SCOPE_POLICY=CANONICAL_PUBLIC_SLICE_MANIFEST_ONLY
PUBLIC_DEVELOPMENT_SCOPE_IDS=healthbench_core,healthbench_consensus,healthbench_hard,healthbench_professional,medxpertqa,pubmedqa
EVALUATION_SLICE_MANIFEST_REQUIRED=YES
EXACT_PRIMARY_SELECTION_SLICE_MANIFEST=NOT_YET_FROZEN
BENCHMARK_PURPOSE_POLICY=PREDECLARED_QUARANTINE_PURPOSE_PER_SLICE
EVERY_EXECUTABLE_SLICE_REQUIRES_ONE_CANONICAL_PURPOSE=YES
PURPOSE_MUST_BE_FROZEN_BEFORE_PAYLOAD_ACCESS_OR_EXECUTION=YES
ALLOWED_PURPOSES=DEV,CHECKPOINT_SELECTION,PUBLIC_EXTERNAL_EVAL
CHECKPOINT_SELECTION_REQUIRES_CAN_SELECT_MODEL_TRUE=YES
PUBLIC_CANONICAL_TEST_SPLIT_PURPOSE=PUBLIC_EXTERNAL_EVAL
PUBLIC_CANONICAL_TEST_SPLIT_CAN_SELECT_MODEL=NO
SAME_SLICE_PURPOSE_ACROSS_CANDIDATES=REQUIRED
CANDIDATE_SPECIFIC_PURPOSE_MAPPING=PROHIBITED
POST_RESULT_PURPOSE_REMAPPING=PROHIBITED
MEDXPERTQA_TEXT_DEV_PURPOSE=NOT_YET_FROZEN
HEALTHBENCH_PURPOSE_MAPPING=NOT_YET_FROZEN
PUBMEDQA_PURPOSE_MAPPING=NOT_YET_FROZEN
PURPOSE_AMBIGUITY=FAIL_CLOSED_NOT_EXECUTABLE
PUBLIC_BENCHMARK_ACCESS_POLICY=METADATA_FIRST_EXACT_ARTIFACT_BINDING_BEFORE_ACCESS
PUBLIC_SOURCE_METADATA_INSPECTION=ALLOWED_READ_ONLY
PAYLOAD_ACCESS_REQUIRES_EXPLICIT_SEPARATE_AUTHORIZATION=YES
PAYLOAD_ACCESS_REQUIRES_EXACT_ARTIFACT_IDENTITY=YES
PAYLOAD_ACCESS_REQUIRES_IMMUTABLE_SOURCE_REVISION=YES
PAYLOAD_ACCESS_REQUIRES_LICENSE_AND_ACCESS_CLASS_RESOLVED=YES
PAYLOAD_ACCESS_REQUIRES_QUARANTINE_PURPOSE_FROZEN=YES
PAYLOAD_ACCESS_REQUIRES_CONTAMINATION_DISPOSITION=YES
MUTABLE_LATEST_OR_UNPINNED_PAYLOAD=PROHIBITED
UNBOUND_PAYLOAD_ACCESS=PROHIBITED
GATED_PAYLOAD_ACCESS=PROHIBITED_WITHOUT_SEPARATE_AUTHORIZATION
PRIVATE_PAYLOAD_ACCESS=PROHIBITED_WITHOUT_SEPARATE_AUTHORIZATION
EXTERNAL_SUBMISSION_ONLY_GROUND_TRUTH=NO_LOCAL_GOLD_ACCESS
LOCAL_PAYLOAD_CACHE_OR_COPY_CREATION=NOT_AUTHORIZED_YET
ACCESS_MECHANISM_MUST_PRESERVE_CANONICAL_ARTIFACT_IDENTITY=YES
POST_ACCESS_ARTIFACT_SUBSTITUTION=PROHIBITED
CANDIDATE_SPECIFIC_PAYLOAD_VERSION=PROHIBITED
ACCESS_FAILURE_OR_IDENTITY_MISMATCH=FAIL_CLOSED_INCOMPLETE
CONTAMINATION_PROOF_POLICY=USE_CLASS_SPECIFIC_FAIL_CLOSED_CONTAMINATION_BINDING
CONTAMINATION_DISPOSITION_REQUIRED_BEFORE_PAYLOAD_ACCESS=YES
CONTAMINATION_DISPOSITION_REQUIRED_BEFORE_CANDIDATE_EXECUTION=YES
SPEC003_CLEAN_CONTAMINATION_REQUIRED_USES=MODIFICATION_OR_DERIVATION,TEACHER_OR_SYNTHETIC_GENERATION,TRAINING_OR_ADAPTATION
MODIFICATION_OR_DERIVATION_REQUIRES_CLEAN_CONTAMINATION=YES
CLEAN_CONTAMINATION_ELIGIBLE_STATES=ASSESSED_CLEAN,NOT_APPLICABLE
NOT_APPLICABLE_REQUIRES_EXPLICIT_EVIDENCE=YES
NOT_APPLICABLE_REQUIRES_TRULY_OUTSIDE_CONTAMINATION_CONDITION=YES
SELF_ASSERTED_NOT_APPLICABLE=PROHIBITED
EXACT_MODEL_WEIGHT_QUANTIZATION_NOT_APPLICABLE=CONDITIONALLY_ALLOWED_ONLY_FOR_WEIGHT_ONLY_DATA_FREE_TRANSFORM
WEIGHT_ONLY_DATA_FREE_QUANTIZATION_REQUIRES_NO_CALIBRATION_DATA=YES
WEIGHT_ONLY_DATA_FREE_QUANTIZATION_REQUIRES_NO_IMATRIX_DATA=YES
WEIGHT_ONLY_DATA_FREE_QUANTIZATION_REQUIRES_NO_BENCHMARK_OR_GOLD_INPUT=YES
WEIGHT_ONLY_DATA_FREE_QUANTIZATION_REQUIRES_NO_TRAINING_OR_DEV_PAYLOAD_INPUT=YES
WEIGHT_ONLY_DATA_FREE_QUANTIZATION_REQUIRES_NO_TEACHER_OR_PROVIDER_OUTPUT=YES
QUANTIZATION_WITH_CALIBRATION_OR_IMATRIX_OR_DATA=CONTAMINATION_ASSESSMENT_REQUIRED
CANDIDATE_SPECIFIC_CONTAMINATION_EXCEPTION=PROHIBITED
POST_RESULT_CONTAMINATION_RECLASSIFICATION=PROHIBITED
PUBLIC_BENCHMARK_PAYLOAD_ACCESS=NOT_AUTHORIZED_YET
PUBLIC_BENCHMARK_PAYLOAD_EXECUTION=NOT_AUTHORIZED_YET
PRIVATE_GOLD_ACCESS=PROHIBITED
REFERENCE_ONLY_BENCHMARK_EXECUTION=PROHIBITED
UNBOUND_EXECUTABLE_ARTIFACT=PROHIBITED
UNFROZEN_CLINICAL_STATISTICAL_THRESHOLDS=NO_PASS_UNTIL_FROZEN
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
MEMORY_MEASUREMENT_POLICY=PLATFORM_NATIVE_PEAK_MEMORY
IOS_PRIMARY_PEAK_METRIC=LEDGER_PHYS_FOOTPRINT_PEAK
IOS_OS_MEMORY_TERMINATION=HARD_FAIL
ANDROID_PRIMARY_PEAK_METRIC=RSS_TRACE_PEAK
ANDROID_SECONDARY_MEMORY_METRIC=TOTAL_PSS
ANDROID_LMK_OR_OOM_TERMINATION=HARD_FAIL
LINUX_PRIMARY_PEAK_METRIC=CGROUP_V2_MEMORY_PEAK
LINUX_OOM_TERMINATION=HARD_FAIL
FULL_QUALIFICATION_PROCESS_SET_ACCOUNTED=YES
MEASUREMENT_WINDOW=FULL_COLD_QUALIFICATION_RUN
BASELINE_BEFORE_MODEL_LOAD=RECORDED
PEAK_ABSOLUTE_BYTES=RECORDED
PEAK_DELTA_FROM_BASELINE=RECORDED
CORE_8K_MEMORY_GATE=2G_CORE_HARD_CAP
CORE_8K_PEAK_MEMORY_HARD_CEILING=2_GiB
CORE_8K_PEAK_MEMORY_HARD_CEILING_BYTES=2147483648
CORE_8K_HARD_CEILING_APPLIES_TO_ALL_FIVE_TARGETS=YES
CORE_8K_HARD_CEILING_USES_PLATFORM_NATIVE_PRIMARY_METRIC=YES
CORE_8K_MEMORY_TERMINATION=HARD_FAIL
CORE_8K_PEAK_DELTA=DIAGNOSTIC_ONLY
CORE_8K_ABSOLUTE_PEAK=HARD_GATE_INPUT
STRESS_16K_PEAK_MEMORY=RECORDED
STRESS_16K_OS_MEMORY_TERMINATION=HARD_FAIL
STRESS_16K_ABSOLUTE_RAM_HARD_CEILING=NOT_FROZEN
CANDIDATE_SPECIFIC_RAM_EXCEPTION=PROHIBITED
POST_RESULT_RAM_CEILING_CHANGE=PROHIBITED
CROSS_PLATFORM_RAW_METRIC_RANKING=PROHIBITED
PERFORMANCE_MEASUREMENT_POLICY=COMPONENT_TIMING_COLD_AND_READY
COLD_START_TO_FIRST_TOKEN=RECORDED
MODEL_LOAD_TIME=RECORDED
READY_STATE_TTFT=RECORDED
PREFILL_TOKENS_PER_SECOND=RECORDED
DECODE_TOKENS_PER_SECOND=RECORDED
END_TO_END_RESPONSE_TIME=RECORDED
TIMING_BOUNDARIES_IDENTICAL_ACROSS_CANDIDATES=YES
TIMING_BOUNDARIES_IDENTICAL_ACROSS_TARGETS=YES
MODEL_LOAD_TIME_EXCLUDED_FROM_READY_STATE_TTFT=YES
COLD_START_TO_FIRST_TOKEN_INCLUDES_MODEL_LOAD=YES
PROMPT_SESSION_PREFIX_CACHE_REUSE=PROHIBITED
CANDIDATE_SPECIFIC_TIMING_BOUNDARIES=PROHIBITED
PERFORMANCE_REPETITION_POLICY=FIVE_FRESH_RUNS_MEDIAN_WITH_WORST_CASE
MEASURED_RUNS_PER_CANDIDATE_TARGET_CONDITION=5
EACH_MEASURED_RUN_STARTS_FROM_FRESH_PROCESS=YES
EACH_MEASURED_RUN_INCLUDES_FRESH_MODEL_LOAD=YES
MEASURED_REQUESTS_PER_FRESH_LOAD=1
NON_MEASURED_WARMUP_REQUESTS=0
PRIMARY_AGGREGATION=MEDIAN_OF_FIVE
WORST_CASE_RUN=RECORDED
ALL_RAW_RUNS=RETAINED
FAILED_OR_TERMINATED_RUNS=RETAINED_AS_FAILURE
FAILED_RUN_REPLACEMENT=PROHIBITED
POST_HOC_RUN_EXCLUSION=PROHIBITED
CANDIDATE_SPECIFIC_RUN_COUNT=PROHIBITED
TARGET_SPECIFIC_RUN_COUNT=PROHIBITED
THERMAL_CONTROL_POLICY=PLATFORM_NATIVE_THERMAL_READY_GATE
THERMAL_STATE_BEFORE_EACH_RUN=RECORDED
THERMAL_STATE_AFTER_EACH_RUN=RECORDED
MEASURED_RUN_START_REQUIRES_THERMAL_READY=YES
KNOWN_ACTIVE_THROTTLING_AT_RUN_START=PROHIBITED
THERMAL_READINESS_USES_PLATFORM_NATIVE_SIGNAL=YES
THERMAL_SIGNAL_IDENTITY_MUST_BE_PINNED=YES
IOS_THERMAL_STATE=PLATFORM_NATIVE_RECORDED
ANDROID_THERMAL_STATUS=PLATFORM_NATIVE_RECORDED
LAPTOP_CPU_THERMAL_TELEMETRY=RECORDED
COOLDOWN_BETWEEN_RUNS=AS_NEEDED_UNTIL_THERMAL_READY
FIXED_SLEEP_AS_THERMAL_PROOF=PROHIBITED
RUN_ORDER_PREDECLARED=REQUIRED
CANDIDATE_SPECIFIC_THERMAL_EXCEPTION=PROHIBITED
POST_RESULT_THERMAL_RULE_CHANGE=PROHIBITED
THERMAL_TERMINATION_OR_OS_THROTTLING_EVENT=RECORDED
EXACT_PLATFORM_THERMAL_READY_THRESHOLDS=NOT_YET_FROZEN
ENERGY_MEASUREMENT_POLICY=PLATFORM_NATIVE_ENERGY_PER_RUN
ENERGY_MEASUREMENT_REQUIRED_FOR_EACH_MEASURED_RUN=YES
ENERGY_WINDOW_MATCHES_FULL_COLD_RUN=YES
PRE_RUN_ENERGY_BASELINE=RECORDED
POST_RUN_ENERGY_RECORD=RECORDED
RUN_ENERGY_DELTA=RECORDED_WHERE_SUPPORTED
ENERGY_SIGNAL_IDENTITY_MUST_BE_PINNED=YES
ENERGY_TOOL_OR_METER_IDENTITY_MUST_BE_PINNED=YES
SAME_ENERGY_METHOD_WITHIN_TARGET_ACROSS_CANDIDATES=REQUIRED
CANDIDATE_SPECIFIC_ENERGY_METHOD=PROHIBITED
POST_RESULT_ENERGY_METHOD_CHANGE=PROHIBITED
IOS_ENERGY_EVIDENCE=PLATFORM_NATIVE_OR_PREDECLARED_VALIDATED_METER
ANDROID_ENERGY_EVIDENCE=PLATFORM_NATIVE_OR_PREDECLARED_VALIDATED_METER
LAPTOP_ENERGY_EVIDENCE=PLATFORM_NATIVE_OR_PREDECLARED_VALIDATED_METER
RAW_ENERGY_UNIT_AND_SEMANTICS=RECORDED
ENERGY_MEASUREMENT_UNCERTAINTY=RECORDED_WHERE_AVAILABLE
CROSS_PLATFORM_RAW_ENERGY_RANKING=PROHIBITED
ENERGY_COMPARISON_SCOPE=SAME_TARGET_SAME_METHOD_ONLY
FAILED_OR_MISSING_ENERGY_CAPTURE=EVIDENCE_INCOMPLETE
FAILED_RUN_ENERGY_RECORD_RETAINED=YES
ENERGY_QUALIFICATION_POLICY=ENERGY_REQUIRED_EVIDENCE_NO_V1_ABSOLUTE_HARD_GATE
ENERGY_EVIDENCE_REQUIRED=YES
MISSING_ENERGY_EVIDENCE=INCOMPLETE
V1_ABSOLUTE_ENERGY_HARD_CEILING=NONE
ENERGY_HARD_DISQUALIFICATION_BY_RAW_VALUE=PROHIBITED
SAME_TARGET_ENERGY_COMPARISON=ALLOWED
CROSS_PLATFORM_RAW_ENERGY_COMPARISON=PROHIBITED
ENERGY_MAY_ENTER_SECONDARY_RANKING=ONLY_IF_PREDECLARED
ENERGY_SECONDARY_RANKING_SCOPE=SAME_TARGET_SAME_METHOD_ONLY
ENERGY_CANNOT_COMPENSATE_FOR_SAFETY_FAILURE=YES
ENERGY_CANNOT_COMPENSATE_FOR_QUALITY_FAILURE=YES
ENERGY_CANNOT_COMPENSATE_FOR_PACKAGE_FAILURE=YES
ENERGY_CANNOT_COMPENSATE_FOR_CORE_MEMORY_FAILURE=YES
POST_RESULT_ENERGY_THRESHOLD_CREATION=PROHIBITED
CANDIDATE_SPECIFIC_ENERGY_THRESHOLD=PROHIBITED
FUTURE_ENERGY_HARD_GATE_REQUIRES_SEPARATE_CANONICAL_EVIDENCE=YES
DEVICE_RUNTIME_FAILURE_POLICY=UNIVERSAL_FATAL_FAILURES_AND_FAIL_CLOSED_EVIDENCE
RUNTIME_INITIALIZATION_FAILURE=HARD_FAIL
CANONICAL_ARTIFACT_LOAD_FAILURE=HARD_FAIL
REQUIRED_CORE_CONDITION_EXECUTION_FAILURE=HARD_FAIL
PROCESS_CRASH_OR_ABNORMAL_TERMINATION=HARD_FAIL
OS_NON_MEMORY_FORCED_TERMINATION=HARD_FAIL
MEASURED_REQUEST_NONCOMPLETION=HARD_FAIL
UNAUTHORIZED_RUNTIME_BACKEND_OR_ARTIFACT_FALLBACK=HARD_FAIL
MISSING_REQUIRED_MEASUREMENT_EVIDENCE=INCOMPLETE
MALFORMED_REQUIRED_MEASUREMENT_EVIDENCE=INCOMPLETE
UNPROVABLE_RUNTIME_OR_ARTIFACT_IDENTITY=INCOMPLETE
WRONG_OR_UNPROVABLE_RUN_CONFIGURATION=INCOMPLETE
MID_RUN_THERMAL_THROTTLING=RECORDED_NOT_AUTOMATIC_HARD_FAIL
FIVE_RUN_SET_WITH_ANY_HARD_FAIL=HARD_FAIL
FIVE_RUN_SET_WITH_ANY_INCOMPLETE_RUN=INCOMPLETE
MEDIAN_OF_FIVE_REQUIRES_FIVE_COMPLETE_NUMERIC_RUNS=YES
PARTIAL_MEDIAN_SUBSTITUTION=PROHIBITED
TARGET_NATIVE_FAILURE_SIGNAL_IDENTITY=PINNED_BEFORE_EXECUTION
NONCOMPLETION_DETECTION_WATCHDOG=PREEXECUTION_REQUIRED
EXACT_WATCHDOG_TIMEOUT=NOT_YET_FROZEN
CANDIDATE_SPECIFIC_FAILURE_EXCEPTION=PROHIBITED
POST_RESULT_FAILURE_RULE_CHANGE=PROHIBITED
PERFORMANCE_THRESHOLD_POLICY=PREDECLARED_TARGET_USABILITY_PERFORMANCE_GATES
PERFORMANCE_HARD_GATES_REQUIRED_BEFORE_EXECUTION=YES
EXACT_NUMERIC_PERFORMANCE_THRESHOLDS=NOT_YET_FROZEN
PERFORMANCE_HARD_THRESHOLDS=NOT_YET_FROZEN
THRESHOLDS_MUST_BE_FROZEN_BEFORE_CANDIDATE_RESULTS=YES
THRESHOLD_EVIDENCE_BASIS_MUST_BE_DOCUMENTED
SAME_TARGET_THRESHOLDS_IDENTICAL_ACROSS_CANDIDATES=YES
CANDIDATE_SPECIFIC_PERFORMANCE_THRESHOLD=PROHIBITED
POST_RESULT_PERFORMANCE_THRESHOLD_CHANGE=PROHIBITED
TARGET_SPECIFIC_THRESHOLDS=ALLOWED_WHEN_PREDECLARED_AND_JUSTIFIED
TARGET_SPECIFIC_THRESHOLD_RELAXATION_AFTER_RESULTS=PROHIBITED
COLD_START_TO_FIRST_TOKEN_HARD_GATE=REQUIRED
READY_STATE_TTFT_HARD_GATE=REQUIRED
DECODE_TOKENS_PER_SECOND_HARD_GATE=REQUIRED
PREFILL_TOKENS_PER_SECOND=RECORDED_AND_SECONDARY_UNLESS_SEPARATELY_FROZEN
MODEL_LOAD_TIME=RECORDED_COMPONENT
END_TO_END_RESPONSE_TIME=RECORDED_AND_SECONDARY_UNLESS_SEPARATELY_FROZEN
PRIMARY_THRESHOLD_AGGREGATE=MEDIAN_OF_FIVE
WORST_CASE_RUN=MANDATORY_GUARDRAIL_EVIDENCE
HARD_FAIL_OR_INCOMPLETE_RUN_CANNOT_ENTER_NUMERIC_AGGREGATE=YES
PERFORMANCE_THRESHOLD_SOURCE=CANDIDATE_INDEPENDENT_USABILITY_EVIDENCE_REQUIRED
CANDIDATE_RESULT_DERIVED_THRESHOLD=PROHIBITED
PERFORMANCE_CAN_NEVER_COMPENSATE_FOR_SAFETY_FAILURE=YES
PERFORMANCE_CAN_NEVER_COMPENSATE_FOR_QUALITY_FAILURE=YES
PERFORMANCE_CAN_NEVER_COMPENSATE_FOR_PACKAGE_FAILURE=YES
PERFORMANCE_CAN_NEVER_COMPENSATE_FOR_CORE_MEMORY_FAILURE=YES
PERFORMANCE_CAN_NEVER_COMPENSATE_FOR_RUNTIME_HARD_FAIL=YES
PLAN_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
```

Acceptance of `USE_CLASS_SPECIFIC_FAIL_CLOSED_CONTAMINATION_BINDING` advances bounded clarification session 6 to four accepted questions but does **not** compute or freeze exact per-candidate/per-slice contamination records, does **not** authorize model-weight access or conversion, does **not** authorize benchmark payload access, local cache/copy creation, or execution, does **not** authorize Private Gold or gated/private benchmark access, does **not** freeze the exact primary-selection slice manifest or unresolved purpose mappings, does **not** freeze the remaining clinical/statistical thresholds, and does **not** complete the full clarification lifecycle. Remaining factual/evidence requirements must be reconciled and independently reviewed before a transition to `PLAN` can be proposed.

Clarification is explicitly authorized only within its bounded lifecycle. This session does not authorize planning, implementation, live tournament execution, model access, model-weight retrieval, model conversion, benchmark payload access, runtime execution, winner selection, or any other later lifecycle stage.