# Spec 005 — Base Model Tournament

**State:** `AUTHORIZED_TO_SPECIFY`
**Canonical starting base:** `a68d37acd713049694106e81dc134ccf4d51feb9`
**Depends on:** Spec 004 `CLOSED_CANONICAL` + canonical founder decisions `FD-001`, `FD-002`, `FD-006`
**Lifecycle authority:** CLARIFY ONLY — explicitly authorized by founder on 2026-08-23
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

Spec 005 is a **baseline-only tournament**. It does not train, fine-tune, distill, align, quantization-aware-train, or otherwise optimize a candidate.

The tournament must compare candidates using the canonical evaluation, safety, provenance, and tournament contracts inherited from Specs 001–004. A winner may be selected only when the evidence is complete, comparable, license-compatible with the intended release posture, and uniquely best under the predeclared comparison strategy.

A valid outcome may be `NO_SELECTION`.

## 2. Why this spec exists

The Grand Master Plan deliberately does not preselect a backbone. Spec 005 converts that principle into a bounded evidence decision while preserving three hard truths:

1. medical and safety quality cannot be traded away merely for a smaller parameter count;
2. a technically strong candidate is not release-eligible if its lineage or license posture is incompatible with the canonical founder decision;
3. claimed device fit must be demonstrated on named device/resource classes rather than inferred from model size or vendor claims.

## Clarifications

### Session 2026-08-23

- Q: How should Spec 005 handle the primary comparison between text-only and multimodal candidates when selecting the base backbone? → A: `COMMON_CORE_PRIMARY_RANKING` — all `PRIMARY` candidates rank only on the common text/core protocol; modality-specific capability is secondary non-ranking evidence in Spec 005.

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
- this specification does not itself declare any named candidate license-compatible.

### 4.2 Target device tier

`FD-002=FLAGSHIP_PLUS_MODERN_MIDRANGE` establishes the V1 target tier.

Therefore Spec 005 must eventually freeze:

- named device/resource classes representing flagship phones;
- named device/resource classes representing modern midrange phones;
- package/storage budget;
- peak RAM budget;
- latency/TTFT and sustained-throughput expectations appropriate to the tournament;
- energy/battery and thermal evidence requirements;
- context/KV behavior relevant to the selected comparison protocol.

Those numeric thresholds are intentionally **not frozen in the specify stage**. They must be resolved before any live execution authorization.

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
- treating this document's candidate-discovery set as an execution manifest.

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
- device/resource criteria that become hard qualification gates must be frozen before execution and must not be retrofitted after results are seen.

## 8. Candidate admission contract

Naming a candidate in planning does **not** authorize access or execution.

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
14. whether the candidate is `PRIMARY`, `CONTROL`, `CONDITIONAL`, or `REFERENCE_ONLY`.

If any required admission field is unresolved, the candidate remains discovery-only and cannot enter a live manifest.

## 9. Candidate roles

Candidate roles are semantically distinct:

### `PRIMARY`

A release-lineage candidate that is eligible, in principle, to win once exact provenance, safety, comparability, device, and execution gates are satisfied.

### `CONTROL`

A comparison anchor used to measure whether the primary candidate set actually offers value. A control is not automatically eligible to become the release backbone.

### `CONDITIONAL`

A technically relevant candidate whose exact license, intended-use, device-fit, access, or other admission condition is unresolved. It cannot become the final selected release lineage until the condition is explicitly resolved.

### `REFERENCE_ONLY`

May inform scientific context where the canonical lineage/evaluation rules permit, but cannot be selected as the release backbone under the current contract.

## 10. Planning/discovery candidate set

The existing Grand Master Plan provides the following **discovery set only**. This section records planning continuity; it is not a freeze, recommendation, admission result, or execution authority.

### Track U — compact unified/multimodal discovery

- Qwen3.5-2B Base
- Ministral 3 3B Base
- Gemma 4 E2B planning candidate, exact variant/status to be verified

### Track M — efficiency-first/modular discovery

- LFM2.5-1.2B Base
- LFM2.5-2.6B Base
- LFM2.5-VL-3B

The LFM family remains conditional under canonical decision `D-007` until exact intended-use/license compatibility is proven.

### Controls / reference discovery

- SmolLM3-3B Base
- Phi-4-mini family
- MedGemma family as reference/evaluation-only by default under `D-006`
- frontier closed or otherwise restricted/gated medical models as reference-only unless a later canonical decision and lineage disposition explicitly authorize more

Clarification must independently verify whether each named family still exists in the intended exact variant, whether it is base or instruct, its current primary license, access status, artifact identity, and whether it belongs in the final frozen candidate set.

## 11. Base vs instruction-tuned comparability

The primary scientific question is backbone selection for later commandMed adaptation. Therefore the default presumption is that `PRIMARY` candidates should be comparable base/pretrained checkpoints.

Instruction-tuned models may be useful controls or references, but must not be silently ranked as equivalent primary backbones unless clarification establishes a defensible common protocol and the scientific question explicitly permits it.

The exact rule must be frozen before execution.

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
- license/lineage fit.

This clarification-stage document does not authorize opening or executing the benchmark payloads needed to obtain those results.

## 14. Device and resource evidence

Parameter count and upstream marketing claims are descriptive only.

The future tournament must use commandMed-owned evidence on named device/resource classes and exact model builds.

Before execution authorization, clarification/planning must define:

- device representatives or reproducible resource classes;
- precision/quantization policy for baseline comparison;
- whether an unquantized reference is required in addition to deployable builds;
- package-byte measurement method;
- peak-memory measurement method;
- TTFT/prefill/decode/sustained-throughput measurement method;
- energy and thermal measurement method or explicit bounded proxy if a direct method is not yet feasible;
- context length and KV-cache conditions;
- repetition count, warm-up, aggregation, and failure handling;
- what constitutes a hard device-qualification failure versus a reported non-ranking metric.

No threshold may be chosen after candidate results are known.

## 15. Reproducibility and exact identity

Every live result must eventually be bound to immutable evidence sufficient to prove:

- exact candidate artifact/revision;
- exact tournament manifest digest;
- exact canonical upstream identities;
- exact runtime/build configuration;
- exact benchmark/metric/safety/lineage contracts;
- exact device/resource identity where device evidence is claimed;
- exact result-set evidence artifact IDs;
- deterministic tournament report identity.

A mutable tag, model family name, `latest`, branch name, or marketplace label is not sufficient identity.

## 16. Fail-closed rules

Spec 005 must fail closed whenever evidence needed for a defensible selection is absent or contradictory.

Examples include:

- unresolved license or lineage disposition;
- required gated access not separately authorized;
- missing exact artifact identity;
- incompatible candidate type under the frozen base-vs-instruct rule;
- incomplete safety evidence;
- benchmark or Gold quarantine violation;
- non-comparable metric vectors;
- missing required device evidence;
- threshold changes after results are observed;
- runtime or build drift without a new exact identity;
- candidate-set drift after manifest freeze;
- exact top tie.

The correct outcome in these cases is not a guessed winner; it is refusal, disqualification where canonical rules require it, or `NO_SELECTION`.

## 17. Required clarification questions

The clarification lifecycle must answer, at minimum:

1. What is the exact primary candidate set, with immutable upstream revisions and neutral candidate IDs?
2. Which named items are base/pretrained, instruct, control, conditional, or reference-only?
3. What exact primary license evidence and Spec 003 lineage disposition applies to each intended use?
4. Which candidates require gated terms or access, and can they remain discovery/reference-only without accepting those terms?
5. **RESOLVED:** primary ranking uses `COMMON_CORE_PRIMARY_RANKING`; modality-specific evidence is secondary and non-ranking, with no cross-track winner in Spec 005.
6. What exact canonical benchmark/metric slices are authorized for the baseline tournament?
7. What exact safety gates are evaluated before ranking, and how are blocked/incomplete states represented?
8. What exact flagship and modern-midrange device/resource representatives define `FD-002`?
9. What package, peak-RAM, latency, throughput, energy, thermal, context, and KV thresholds or evidence rules apply?
10. What precision/quantization/build policy is fair across candidates while preserving a baseline-only scientific question?
11. What runtime/adapters are permitted, and what dependency changes would require separate review before execution?
12. What contamination/quarantine proof is required for every candidate/result path?
13. What is the exact public-benchmark access mechanism, and what payload access remains separately gated?
14. What exact criteria exclude a candidate before live execution rather than producing an incomplete result later?
15. What compute/spend budget is permitted for the tournament, and which actions remain zero-spend/read-only until execution authorization?
16. What independent review and exact-head evidence must be present before any execution activation can be proposed?

## 18. Specification acceptance criteria

This specify-stage artifact is complete only when independent review confirms that it:

- defines the tournament problem without selecting a winner;
- binds the canonical predecessor identities and founder decisions;
- preserves baseline-only/no-training scope;
- distinguishes planning discovery from frozen admission;
- makes permissive release-lineage compatibility an explicit gate without asserting unverified license compatibility;
- preserves flagship + modern-midrange device intent without inventing unsupported numeric thresholds;
- preserves Spec 004 deterministic/fail-closed comparison semantics;
- enumerates the unresolved questions that clarification must resolve;
- grants no model, weight, benchmark payload, private Gold, provider, PHI, gated-asset, or execution authority.

## 19. Exit and next lifecycle step

Successful canonical merge of this specification means only:

```text
SPEC_005_SPECIFICATION=DEFINED_CANONICALLY
NEXT_LIFECYCLE_STEP=CLARIFY
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
```

Clarification is now explicitly authorized by the founder for this bounded session. This does not authorize planning, implementation, live tournament execution, model access, model-weight retrieval, benchmark payload access, or winner selection.