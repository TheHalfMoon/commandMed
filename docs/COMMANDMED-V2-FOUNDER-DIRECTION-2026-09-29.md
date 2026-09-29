# CommandMed v2 Founder Research Direction

**Date:** 2026-09-29  
**Status:** PROPOSED CANONICAL PLANNING DIRECTION  
**Execution authority created:** NONE  
**Training authority created:** NONE  
**Spend authority created:** NONE  

## Decision V2-FD-001 — Primary single-checkpoint research target

**Founder direction:** `SINGLE_CHECKPOINT_PRIMARY_RESEARCH_TARGET`

CommandMed v2 shall investigate a single model/checkpoint that unifies:

1. Qwen-family autoregressive medical language and multimodal reasoning;
2. a Qwen-derived Jev/System-One-style one-pass typed decision capability;
3. a Qwen-Image-derived visual generation/editing path.

The primary research design must not be an application-level ensemble of three independently served foundation models.

This decision supersedes `DF-003 — One checkpoint vs multiple release tiers` as a **prospective research-direction question**. It does not pre-prove that a single checkpoint will succeed, fit every deployment tier, or be the final commercial release artifact.

### Scientific interpretation

The founder has selected the hypothesis to test, not its outcome.

A negative result remains acceptable. If rigorous evidence demonstrates that the single-checkpoint target causes unacceptable capability, calibration, safety, rights, efficiency, or reproducibility failures, the project must report that result and may propose a later founder decision to narrow or replace the target.

## Decision V2-FD-002 — No separate uncertainty model

**Founder direction:** `INTRINSIC_DECISION_PROBABILITY_NOT_SEPARATE_UNCERTAINTY_MODEL`

CommandMed v2 should not add a separately served uncertainty model merely to estimate confidence.

Instead:

- typed decision probabilities are native outputs of the decision head;
- probability quality is evaluated directly with proper scoring and calibration/selective metrics;
- unsupported certainty is a failure, not a design goal;
- safety policies may still require asking for information, abstaining, or escalating when evidence is insufficient.

This direction changes architecture, not the constitutional requirement to detect unsupported certainty or preserve safety-critical failure handling.

## Decision V2-FD-003 — Paper is a primary project output

**Founder direction:** `PAPER_FIRST_RESEARCH_DISCIPLINE`

A publication-quality research paper is a primary deliverable of CommandMed v2.

Consequences:

- novelty is evaluated before expensive optimization;
- primary hypotheses and metrics are frozen before confirmatory experiments;
- strong recent merging and unified-medical-model baselines are mandatory;
- negative results and failed hypotheses are retained;
- test contamination and repeated test access are tracked explicitly;
- paper claims are narrower than or equal to the evidence;
- publication pressure does not create training, spend, data, or model-execution authority.

## Decision V2-FD-004 — Heterogeneous fusion, not naive tensor averaging

**Founder direction:** `HETEROGENEOUS_CAPABILITY_FUSION_RESEARCH`

CommandMed v2 may use conventional weight-space merging only where architecture and parameter correspondence make it scientifically valid.

The project must not pretend that a causal language model, a typed decision head, and a diffusion/flow generator can be combined by naive averaging of unrelated tensors.

The prospective method therefore separates:

- compatible Qwen expert/task-vector merging;
- decision-head transplantation/integration;
- hidden-state/representation alignment;
- image semantic-encoder replacement;
- joint stabilization;
- later consolidation/compression when justified.

`Heterogeneous Capability Fusion (HCF)` is a working method name, not yet a proven contribution.

## Decision V2-FD-005 — Qwen3.8 and Qwen-Image are preferred research donors, not pre-proven winners

**Founder direction:** `QWEN_FAMILY_PRIMARY_RESEARCH_LINEAGE`

The current preferred research lineage is:

- `Qwen/Qwen3.8-27B` for the shared semantic backbone;
- Qwen-family Jev/System-One alternatives such as Kev/decider as decision references/donors;
- `QwenLM/Qwen-Image-2.1` as the frontier visual-generation research donor where exact terms permit.

This selection is a research direction and architecture constraint. It does not erase the requirement to freeze exact revisions, verify licenses, establish comparability, or reject a donor if the evidence or rights fail.

Qwen-Image-2.1's research-license posture must remain explicit. No CommandMed-owned Apache-2.0 statement is allowed to imply that third-party model weights or derivatives have been relicensed.

## Relationship to prior canonical decisions

Historical decisions and closed specs remain evidence.

This v2 direction does not retroactively invalidate:

- evaluation-before-training;
- deterministic clinical truth boundaries;
- holdout quarantine;
- exact provenance and licensing;
- safety hard gates;
- Arabic/English evaluation;
- resource accounting;
- existing Spec 000–007 historical closure/execution records.

Where older planning language preferred or allowed multiple specialist neural modules, v2 changes the **primary hypothesis** to a single-checkpoint neural model. Deterministic authoritative tools remain external by design and do not violate the single-model research target.

## Prospective authority rule

After this document is canonical, it authorizes only planning alignment.

It does **not** authorize:

```text
MODEL_WEIGHT_DOWNLOAD=NO
MODEL_WEIGHT_LOAD=NO
MODEL_INFERENCE=NO
MODEL_MERGE_EXECUTION=NO
MODEL_CONVERSION=NO
TRAINING=NO
BENCHMARK_PAYLOAD_EXECUTION=NO
PRIVATE_GOLD_ACCESS=NO
PHI_ACCESS=NO
PAID_COMPUTE=NO
SPEND=NO
```

Any later execution must be granted by a dedicated bounded spec after the evaluation, rights, resource, and scientific prerequisites are satisfied.
