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

A founder clarification on 2026-08-23 establishes `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY`: the eventual commandMed release should be small enough to make installation practical on iPhones, Android phones, and low-end ordinary laptops, with the explicit product ambition of maximizing broad Hugging Face adoption. This distribution goal does not override clinical safety, provenance, licensing, or minimum-quality gates.

Spec 005 is a **baseline-only tournament**. It does not train, fine-tune, distill, align, quantization-aware-train, or otherwise optimize a candidate.

The tournament must compare candidates using the canonical evaluation, safety, provenance, and tournament contracts inherited from Specs 001–004. A winner may be selected only when the evidence is complete, comparable, license-compatible with the intended release posture, and uniquely best under the predeclared comparison strategy.

A valid outcome may be `NO_SELECTION`.

## 2. Why this spec exists

The Grand Master Plan deliberately does not preselect a backbone. Spec 005 converts that principle into a bounded evidence decision while preserving four hard truths:

1. medical and safety quality cannot be traded away merely for a smaller parameter count;
2. a technically strong candidate is not release-eligible if its lineage or license posture is incompatible with the canonical founder decision;
3. claimed device fit must be demonstrated on named device/resource classes rather than inferred from model size or vendor claims;
4. once safety, provenance, licensing, and minimum-quality gates are satisfied, deployable package size and low-resource reach are first-class product constraints rather than secondary marketing claims.

## Clarifications

### Session 2026-08-23

**Bounded session 1 — complete (5/5)**

- Q: How should Spec 005 handle the primary comparison between text-only and multimodal candidates when selecting the base backbone? → A: `COMMON_CORE_PRIMARY_RANKING` — all `PRIMARY` candidates rank only on the common text/core protocol; modality-specific capability is secondary non-ranking evidence in Spec 005.
- Q: Should all `PRIMARY` candidates in Spec 005 be base/pretrained checkpoints only, excluding instruction-tuned models from primary ranking? → A: `BASE_ONLY_PRIMARY` — only base/pretrained checkpoints may be `PRIMARY`; instruction-tuned models may be `CONTROL` or `REFERENCE_ONLY` but cannot enter primary ranking or win Spec 005.
- Q: How should Spec 005 define the `FLAGSHIP_PLUS_MODERN_MIDRANGE` device evidence boundary? → A: `NAMED_DEVICE_PLUS_RESOURCE_ENVELOPE` — use one named physical representative per tier plus a reproducible resource envelope for that tier; exact device models and numeric thresholds remain to be frozen before execution.
- Q: Should the frozen primary tournament manifest include only `PRIMARY` candidates whose admission gates are complete before manifest freeze? → A: `FULLY_ADMITTED_PRIMARY_ONLY` — only fully admitted `PRIMARY` candidates may enter the frozen primary ranking manifest; unresolved candidates remain discovery/conditional outside that manifest.
- Q: What precision/quantization policy should Spec 005 use to separate fair backbone comparison from real-device deployability evidence? → A: `DUAL_BUILD_BASELINE_AND_DEPLOYABLE` — use a frozen reference build for primary capability comparison and a separately frozen deployable quantized build for device qualification; quantify compression regression separately.

**Bounded session 2 — in progress (1/5)**

- Q: What candidate set should Spec 005 carry forward as the primary-admission shortlist before immutable revisions and exact license/lineage evidence are bound? → A: the original `FOUR_PERMISSIVE_BASE_SHORTLIST` is superseded before manifest freeze by the founder's `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY`. Admission reconciliation must add `Qwen/Qwen3.5-0.8B-Base` as the lead ultra-compact candidate while retaining the prior four artifacts as quality/device comparators until pre-execution gates can exclude them without post-result substitution.

**Founder clarification directive — does not consume an additional clarification question**

- `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY`: optimize the eventual release for extremely small download footprint and practical local use across iPhone, Android, and low-end laptops. The text/core package should be independently downloadable; optional multimodal/vision assets should not be required for the smallest common-core package when the chosen runtime permits separation. Safety, provenance, licensing, and minimum medical-quality requirements remain hard gates.

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
- a conditional candidate must not be promoted to the final release lineage merely because it scores well;
- this specification does not itself declare any named candidate fully license-compatible merely because its current public model card reports a permissive license.

### 4.2 Target device tier and distribution reach

`FD-002=FLAGSHIP_PLUS_MODERN_MIDRANGE` establishes the V1 target tier, clarification freezes `NAMED_DEVICE_PLUS_RESOURCE_ENVELOPE` as the evidence strategy, and the founder further establishes `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY`.

Therefore Spec 005 must eventually freeze:

- one named physical flagship representative plus a reproducible flagship resource envelope;
- one named physical modern-midrange representative plus a reproducible modern-midrange resource envelope;
- an additional low-resource laptop envelope representative of ordinary weak CPU/RAM hardware;
- package/download-size budget for the smallest common-core release artifact;
- peak RAM budget;
- latency/TTFT and sustained-throughput expectations appropriate to the tournament;
- energy/battery and thermal evidence requirements on phones;
- context/KV behavior relevant to the selected comparison protocol;
- whether optional modality assets are separately downloadable from the common text/core package.

The named devices, envelope values, and numeric qualification thresholds are intentionally **not frozen in clarification yet**. They must be fixed before any live execution authorization and cannot be chosen after candidate results are observed.

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
- choosing a winner from vendor claims, model-card claims, parameter count, reputation, or preference;
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
- missing, malformed, wrong-manifest, blocked, insufficient, or non-comparable evidence is `INCOMPLETE` rather than silently favorable;
- any declared candidate with incomplete required evidence forces `NO_SELECTION` before ranking;
- an exact top tie forces `NO_SELECTION`;
- no candidate ID, input order, popularity, or ad hoc tie-break may select a winner.

## 7. Comparison strategy

The comparison strategy must remain predeclared and deterministic.

Spec 005 inherits the Spec 004 strategy:

```text
COMPARISON_STRATEGY=LEXICOGRAPHIC_PREDECLARED
TIE_POLICY=NO_SELECTION_ON_TIE
```

Requirements:

- only canonical non-hard-gate metrics eligible for comparison may enter the ranking vector;
- metric direction must be explicit (`HIGHER_BETTER` or `LOWER_BETTER`);
- ranking metric order must be frozen before live evaluation;
- weighted sums are prohibited unless a future separately reviewed canonical contract explicitly replaces this rule;
- safety and lineage hard gates are not compensable by higher capability scores;
- device/resource criteria that become hard qualification gates must be frozen before execution and must not be retrofitted after results are seen;
- clarification must still decide how minimum medical-quality gates and deployable package size interact in the lexicographic ranking; the founder's distribution priority does not silently rewrite the canonical ranking order.

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
15. pre-execution evidence that the candidate has a plausible path to the frozen universal-low-resource package/RAM envelope without candidate-specific post-result threshold changes.

If any required admission field is unresolved, the candidate remains discovery-only or `CONDITIONAL` outside the frozen primary ranking manifest. It must not be inserted merely to produce `INCOMPLETE`, and it must not be removed after results are observed to rescue a selection. Candidate-set freeze occurs only after admission reconciliation is complete.

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

`ULTRA_COMPACT_FIRST_ADMISSION_SHORTLIST` supersedes the earlier four-candidate clarification shortlist before manifest freeze. This is an admission-reconciliation set, not the final frozen primary ranking manifest.

The following exact upstream artifact names are carried forward:

1. `Qwen/Qwen3.5-0.8B-Base` — **lead ultra-compact admission candidate**;
2. `Qwen/Qwen3.5-2B-Base` — compact quality comparator;
3. `mistralai/Ministral-3-3B-Base-2512` — upper-size quality/device comparator;
4. `google/gemma-4-E2B` — architecture/modality comparator subject to footprint proof;
5. `HuggingFaceTB/SmolLM3-3B-Base` — text-base quality/control comparator.

Read-only public-source verification performed during clarification observed:

- `Qwen/Qwen3.5-0.8B-Base` is an official pre-trained-only base artifact with a 0.8B language model and Apache-2.0 metadata;
- current community GGUF conversions of the corresponding 0.8B family demonstrate approximately 0.55–0.58 GB Q4-class text-model artifacts, with lower-bit artifacts below 0.5 GB; these are **size-feasibility evidence only**, not commandMed quality evidence;
- the Qwen3.5 vision projector is distributed as a separate artifact in current GGUF packaging, supporting a plausible text-only smallest-package path while preserving optional multimodal expansion;
- current Apple MLX/Swift tooling includes Qwen3.5 model support, and current MLC LLM sources include Qwen3.5 plus iOS/Android deployment paths; exact runtime qualification remains unresolved;
- `Qwen/Qwen3.5-2B-Base` currently reports Apache-2.0 and 2B language-model parameters, but representative Q4 GGUF artifacts are around 1.3–1.4 GB, materially larger than the 0.8B path;
- `mistralai/Ministral-3-3B-Base-2512` is identified by its official model card as a base pre-trained Apache-2.0 variant;
- `google/gemma-4-E2B` currently reports Apache-2.0 metadata;
- `HuggingFaceTB/SmolLM3-3B-Base` is identified by its official model card as a base model after pretraining and Apache 2.0;
- `LiquidAI/LFM2.5-2.6B-Base` remains under custom `lfm1.0` metadata and is not promoted into this shortlist.

Those observations are **discovery evidence only**. They do not satisfy the exact Spec 003 lineage contract, immutable-revision requirement, tokenizer/processor identity binding, access-status proof, contamination/quarantine proof, runtime compatibility proof, medical-quality proof, or device qualification required for `PRIMARY` admission.

Therefore:

- `Qwen/Qwen3.5-0.8B-Base` is the current **lead candidate to test for the smallest mass-distribution path**, not a selected winner;
- none of the five is yet declared fully admitted;
- none is yet present in a frozen execution manifest;
- immutable revisions/digests and neutral `candidate_id` values remain unresolved;
- exact license texts, notices, upstream code/runtime obligations, tokenizer/processor licensing, and intended-use compatibility must be bound before admission;
- pre-execution package/RAM evidence may legitimately exclude a larger candidate before live tournament execution once the universal-low-resource envelope is frozen;
- no candidate may be added after results merely because the original shortlist failed.

### Conditional discovery outside the primary shortlist

The LFM2.5 family, including `LiquidAI/LFM2.5-2.6B-Base`, remains `CONDITIONAL` discovery outside the primary-admission shortlist under canonical decision `D-007`. Its current public model metadata reports the custom `lfm1.0` license, so exact intended-use and downstream-release compatibility with `FD-001` must be proven before any promotion.

Other prior discovery items remain non-primary unless separately reconciled:

- Phi-4-mini family — control/reference consideration only where exact checkpoint status and purpose justify it;
- MedGemma family — reference/evaluation-only by default under `D-006`;
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

## 14. Device, package, and resource evidence

`NAMED_DEVICE_PLUS_RESOURCE_ENVELOPE`, `DUAL_BUILD_BASELINE_AND_DEPLOYABLE`, and `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY` are frozen as Spec 005 evidence strategies.

Each target tier must be represented by both:

1. one named physical device representative used for real device-specific evidence such as latency, sustained behavior, battery/energy, and thermals; and
2. one reproducible resource envelope describing the relevant hardware/resource boundary so conclusions are not tied solely to a single retail handset.

The future evidence plan must cover at least flagship phone, modern-midrange Android, and low-resource ordinary laptop deployment. iPhone coverage must be demonstrated through an Apple-compatible runtime/build path rather than inferred from desktop Apple Silicon results.

Each admitted `PRIMARY` candidate must also have two predeclared build roles when execution is eventually authorized:

1. a **reference build** governed by a common, frozen high-precision policy for primary common-core capability comparison; and
2. a **deployable build** governed by a common, frozen quantization/deployment policy for device qualification on the named devices and resource envelopes.

Primary capability comparison uses the reference-build evidence. Device/package qualification uses the deployable-build evidence. The deployable build must not replace the reference build in the primary capability vector, and the reference build must not be used to claim phone deployability. Quality/safety regression attributable to compression must be measured and reported separately under a frozen rule.

For mass distribution, the smallest common-core artifact should default to text-only when the selected architecture/runtime allows optional vision assets to be packaged separately. A larger optional multimodal artifact must not inflate the claimed minimum download size.

The exact reference precision, quantization format/level, conversion toolchain, runtime, build flags, architecture-specific equivalence rules, package-size ceiling, and RAM ceiling remain unresolved and must be frozen before execution. A policy may not be changed per candidate after results are observed.

Before execution authorization, clarification/planning must additionally define:

- package-byte measurement method, including tokenizer/config/runtime assets that are required for the advertised minimum installation;
- peak-memory measurement method;
- TTFT/prefill/decode/sustained-throughput measurement method;
- energy and thermal measurement method or explicit bounded proxy if a direct method is not yet feasible;
- context length and KV-cache conditions;
- repetition count, warm-up, aggregation, and failure handling;
- what constitutes a hard device/package-qualification failure versus a reported non-ranking metric;
- the minimum medical-quality floor below which a smaller artifact cannot qualify;
- the exact ranking position of deployable package size after all hard gates pass.

Parameter count and upstream marketing claims remain descriptive only. No named representative, envelope boundary, build policy, package threshold, RAM threshold, or ranking rule may be chosen after candidate results are known.

## 15. Reproducibility and exact identity

Every live result must eventually be bound to immutable evidence sufficient to prove:

- exact candidate artifact/revision;
- exact tournament manifest digest;
- exact canonical upstream identities;
- exact runtime/build configuration;
- exact benchmark/metric/safety/lineage contracts;
- exact device/resource identity where device evidence is claimed;
- exact packaged artifact identity and byte size where distribution evidence is claimed;
- exact result-set evidence artifact IDs;
- deterministic tournament report identity.

A mutable tag, model family name, `latest`, branch name, or marketplace label is not sufficient identity.

## 16. Fail-closed rules

Spec 005 must fail closed whenever evidence needed for a defensible selection is absent or contradictory.

Examples include:

- unresolved license or lineage disposition;
- required gated access not separately authorized;
- missing exact artifact identity;
- candidate not being an exact eligible base/pretrained checkpoint under `BASE_ONLY_PRIMARY`;
- candidate entering the frozen primary ranking manifest before all admission fields are resolved under `FULLY_ADMITTED_PRIMARY_ONLY`;
- incomplete safety evidence;
- benchmark or Gold quarantine violation;
- non-comparable metric vectors;
- missing required device evidence under `NAMED_DEVICE_PLUS_RESOURCE_ENVELOPE`;
- missing required reference or deployable build evidence under `DUAL_BUILD_BASELINE_AND_DEPLOYABLE`;
- unmeasured required compression regression;
- failure to satisfy a frozen universal-low-resource package/RAM hard gate;
- claiming the optional vision package as part of the minimum footprint only when advantageous to a candidate, or omitting required assets from the measured package;
- device representative, envelope boundary, build policy, package threshold, RAM threshold, or ranking-rule changes after results are observed;
- runtime or build drift without a new exact identity;
- candidate-set drift after manifest freeze;
- exact top tie.

The correct outcome in these cases is not a guessed winner; it is refusal, disqualification where canonical rules require it, or `NO_SELECTION`.

## 17. Required clarification questions

The clarification lifecycle must answer, at minimum:

1. **PARTIALLY RESOLVED / SUPERSEDED SHORTLIST:** `ULTRA_COMPACT_FIRST_ADMISSION_SHORTLIST` now carries five exact upstream artifact names, led by `Qwen/Qwen3.5-0.8B-Base`. Immutable revisions/digests, neutral candidate IDs, and the final fully admitted `PRIMARY` set remain unresolved.
2. **RESOLVED:** `BASE_ONLY_PRIMARY`; only exact base/pretrained checkpoints may be `PRIMARY`. Instruction-tuned models may be `CONTROL` or `REFERENCE_ONLY` but cannot enter primary ranking or win Spec 005.
3. What exact primary license evidence and Spec 003 lineage disposition applies to each intended use?
4. Which candidates require gated terms or access, and can they remain discovery/reference-only without accepting those terms?
5. **RESOLVED:** primary ranking uses `COMMON_CORE_PRIMARY_RANKING`; modality-specific evidence is secondary and non-ranking, with no cross-track winner in Spec 005.
6. What exact canonical benchmark/metric slices are authorized for the baseline tournament?
7. What exact safety and minimum medical-quality gates are evaluated before ranking, and how are blocked/incomplete states represented?
8. **RESOLVED POLICY:** `NAMED_DEVICE_PLUS_RESOURCE_ENVELOPE`; each target tier requires named-device evidence plus a reproducible resource envelope, now including a low-resource laptop envelope. Exact devices, envelope values, and numeric thresholds remain to be frozen before execution.
9. What exact package, peak-RAM, latency, throughput, energy, thermal, context, and KV thresholds or evidence rules implement `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY`?
10. **RESOLVED POLICY:** `DUAL_BUILD_BASELINE_AND_DEPLOYABLE`; primary capability comparison uses a frozen reference build, device qualification uses a frozen deployable quantized build, and compression regression is reported separately. Exact precision/quantization/runtime details remain to be frozen before execution.
11. What runtime/adapters are permitted on iOS, Android, and low-resource laptops, and what dependency changes would require separate review before execution?
12. What contamination/quarantine proof is required for every candidate/result path?
13. What is the exact public-benchmark access mechanism, and what payload access remains separately gated?
14. **RESOLVED POLICY:** `FULLY_ADMITTED_PRIMARY_ONLY`; unresolved/conditional candidates remain outside the frozen primary ranking manifest, and candidate-set freeze occurs only after admission reconciliation.
15. What compute/spend budget is permitted for the tournament, and which actions remain zero-spend/read-only until execution authorization?
16. What independent review and exact-head evidence must be present before any execution activation can be proposed?
17. After hard safety/provenance/license/minimum-quality gates pass, where exactly does deployable package size appear in the `LEXICOGRAPHIC_PREDECLARED` ranking order?

Bounded clarification session 1 on 2026-08-23 is complete at five accepted questions. Bounded clarification session 2 is in progress with one accepted question plus one explicit founder directive. The unresolved questions above remain active requirements and prevent the clarification lifecycle from being declared complete.

## 18. Specification acceptance criteria

A future complete clarification artifact is acceptable only when independent review confirms that it:

- defines the tournament problem without selecting a winner;
- binds the canonical predecessor identities and founder decisions;
- preserves baseline-only/no-training scope;
- distinguishes admission shortlisting from frozen admission and execution manifest membership;
- carries a genuine sub-1B base candidate through admission reconciliation rather than assuming 2B/3B is small enough;
- makes permissive release-lineage compatibility an explicit gate without asserting unverified license compatibility;
- preserves named-device evidence while explicitly covering iPhone, modern-midrange Android, and low-resource laptops;
- measures the complete minimum downloadable package honestly and separates optional modality assets only when technically valid;
- preserves Spec 004 deterministic/fail-closed comparison semantics;
- records accepted clarification decisions without contradicting unresolved gates;
- resolves all clarification requirements that materially affect candidate admission, comparability, device qualification, execution planning, and exact-head review before advancing to `PLAN`;
- grants no model, weight, benchmark payload, private Gold, provider, PHI, gated-asset, or execution authority.

Neither clarification session is a declaration that the full clarification lifecycle is complete until every material unresolved requirement is reconciled and independently reviewed.

## 19. Exit and next lifecycle step

Current working state after the founder distribution directive in bounded clarification session 2:

```text
SPEC_005_SPECIFICATION=DEFINED_CANONICALLY
CLARIFICATION_SESSION_1=5_QUESTIONS_ACCEPTED
CLARIFICATION_SESSION_2=IN_PROGRESS
CLARIFICATION_SESSION_2_QUESTIONS_ACCEPTED=1
UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY=LOCKED_BY_FOUNDER_DIRECTIVE
LEAD_ULTRA_COMPACT_ADMISSION_CANDIDATE=Qwen/Qwen3.5-0.8B-Base
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
PLAN_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
```

Clarification is explicitly authorized only within its bounded lifecycle. This session does not authorize planning, implementation, live tournament execution, model access, model-weight retrieval, benchmark payload access, winner selection, or any other later lifecycle stage.