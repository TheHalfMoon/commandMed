# Spec 005 — Canonical Safety and Medical-Quality Floor Evidence

**Lifecycle:** CLARIFY ONLY
**Evidence capture date:** 2026-08-23
**Canonical commandMed base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`

> This artifact reads canonical Spec 001/002 contracts only. It does not execute benchmarks, open private Gold payloads, run models, invent clinical thresholds, or authorize execution.

## 1. Canonical identities

```text
METRICS_IDENTITY=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
SAFETY_POLICY_IDENTITY=79a12414fe68fc08efb43070f3eede36976f2e0dc0ece7f4eed4bbcc5496d14f
BENCHMARKS_IDENTITY=7f58edba1ac179cbf24cb2d5c902e2ef947024bfd1c6eacdbef1a609b00f64a7
GOLD_PROTOCOLS_IDENTITY=40c89702469d759f4dc893aff6bc6fdb7e300f9cb2d8f19f2b3e0dbd78200666
QUARANTINE_IDENTITY=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
```

Canonical files inspected:

- `data/eval/metrics.json`
- `data/eval/safety_policy.json`
- `data/eval/benchmarks.json`

## 2. Canonical hard-gate metrics relevant to Spec 005

The metric registry marks these metrics as hard gates:

| Metric | Direction | Core meaning | Threshold state in metric registry |
|---|---|---|---|
| `emergency_miss_rate` | LOWER_BETTER | missed emergency / false reassurance | `DEFINED_NOT_YET_THRESHOLD_FROZEN` |
| `medication_critical_error_rate` | LOWER_BETTER | critical dosing / interaction / contraindication errors | `DEFINED_NOT_YET_THRESHOLD_FROZEN` |
| `selective_risk_at_target_coverage` | LOWER_BETTER | accepted-answer risk with abstention option | `DEFINED_NOT_YET_THRESHOLD_FROZEN` |
| `citation_entailment_fidelity` | HIGHER_BETTER | factual clinical claim support by evidence | `DEFINED_NOT_YET_THRESHOLD_FROZEN` |
| `arabic_clinical_parity_gap` | LOWER_BETTER | Arabic-English clinical capability gap | `DEFINED_NOT_YET_THRESHOLD_FROZEN` |
| `lab_report_field_extraction_accuracy` | HIGHER_BETTER | structured lab extraction correctness | `DEFINED_NOT_YET_THRESHOLD_FROZEN` |

Resource metrics such as `installed_package_bytes` and `peak_inference_ram` are canonical metrics but are not marked hard gates in the metric registry. Spec 005 separately freezes the `700 MiB` package ceiling as a tournament qualification boundary; that Spec 005 rule does not rewrite the canonical metric registry's `is_hard_gate` field.

## 3. Spec 002 gate semantics already frozen

Canonical safety policy `commandmed-safety-policy-v1` distinguishes sentinel mechanics from population/statistical thresholds.

### 3.1 Frozen zero-violation sentinel mechanics

The following gate contracts already have a deterministic sentinel pass/fail rule:

```text
emergency-sentinel-policy-gate-v1:
  metric=emergency_miss_rate
  threshold_class=FROZEN_SENTINEL_ZERO_VIOLATIONS
  pass=ZERO_VIOLATIONS
  fail=ANY_VIOLATION

medication-sentinel-policy-gate-v1:
  metric=medication_critical_error_rate
  threshold_class=FROZEN_SENTINEL_ZERO_VIOLATIONS
  pass=ZERO_VIOLATIONS
  fail=ANY_VIOLATION

citation-evidence-sentinel-gate-v1:
  metric=citation_entailment_fidelity
  threshold_class=FROZEN_SENTINEL_ZERO_VIOLATIONS
  pass=ZERO_VIOLATIONS
  fail=ANY_VIOLATION
```

These sentinel contracts are non-compensable. A smaller model/package cannot offset an exact sentinel violation.

### 3.2 Statistical/clinical gates explicitly not passable yet

The following gates are canonically `PENDING_CLINICAL_EVIDENCE` with `NO_PASS_UNTIL_FROZEN` or equivalent pending semantics:

```text
selective-risk-statistical-gate-v1
arabic-clinical-parity-statistical-gate-v1
lab-extraction-statistical-gate-v1
```

The canonical policy requires, before statistical threshold freeze:

```text
INTENDED_USE_AND_POPULATION
EVALUATION_DESIGN
IDENTITY_BOUND_EVIDENCE
CLINICAL_REVIEW_AUTHORITY
STATISTICAL_RATIONALE
SAMPLE_SIZE_OR_POWER_RATIONALE
```

For relevant metrics, `pass_allowed=false` while those requirements remain unresolved.

Therefore **Spec 005 clarification must not invent numeric thresholds merely to enable a tournament selection**.

## 4. Consequence for `QUALITY_FLOOR_THEN_SIZE_FIRST`

The founder-approved `QUALITY_FLOOR_THEN_SIZE_FIRST` rule remains valid, but the phrase “quality floor” cannot be reduced to an arbitrary MedQA score or a model-card benchmark.

A candidate is not fully safety-qualified merely because it:

- is smaller;
- has strong public benchmark scores;
- passes MedQA;
- matches a medical reference model on one metric;
- passes the three zero-violation sentinel mechanics while statistical hard gates remain unfrozen.

Spec 005 must preserve two distinct evidence layers:

1. **Frozen sentinel qualification** — exact zero-violation rules can be evaluated once execution is separately authorized.
2. **Pending clinical/statistical hard gates** — no canonical PASS exists until the required clinical/statistical threshold-freeze evidence exists.

## 5. Canonical public benchmark inventory usable for later development planning

The benchmark registry already contains verified public development assets, including:

```text
healthbench_consensus
  source_revision=40ee1968852fc57f625934251ac22be47077a8fb
  access=PUBLIC
  license=MIT
  contamination_sensitivity=HIGH

healthbench_core
  source_revision=40ee1968852fc57f625934251ac22be47077a8fb
  access=PUBLIC
  license=MIT
  contamination_sensitivity=HIGH

healthbench_hard
  source_revision=40ee1968852fc57f625934251ac22be47077a8fb
  access=PUBLIC
  license=MIT
  contamination_sensitivity=HIGH

healthbench_professional
  source_revision=349962fd46dd02343a0d8a606491baf59154ea1a
  access=PUBLIC
  license=MIT
  contamination_sensitivity=HIGH
```

This registry inspection does not authorize opening or executing those payloads. Their high contamination sensitivity also means any later use must respect the canonical quarantine contract.

Family records such as MedHELM and MedAbstain are reference-only/component-specific at the family level and are not automatically executable benchmark assets.

## 6. Medical knowledge is useful but not itself the safety floor

Canonical non-hard metric `medqa_usmle_accuracy` may support capability comparison, but it is explicitly not a hard gate. Thus Spec 005 must not define “medical enough” as a single MCQ threshold alone.

The eventual medical-quality qualification must be evidence-backed and consistent with the canonical role/language/safety contracts. In particular, commandMed's product ambitions require attention to:

- patient/caregiver safety;
- clinical-professional behavior;
- uncertainty/abstention;
- evidence-grounded clinical responses;
- Arabic-English parity;
- appropriate deterministic/authoritative truth boundaries.

## 7. Implication for current ultra-compact candidates

### Qwen3-0.6B-Base and Qwen3.5-0.8B-Base

Both can remain `PRIMARY` admission candidates on size/license/base-status evidence. Neither may be called selected or medically qualified until the canonical hard-gate evidence is complete.

### SmolLM2-360M

Its official English-primary limitation is particularly material because `arabic_clinical_parity_gap` is a canonical hard gate whose statistical threshold remains pending. Extremely small size does not justify assuming Arabic qualification.

### Apertus and Gemma 3 270M

Their rights/access conditions independently prevent clean `PRIMARY` admission while unresolved, before medical qualification is even considered.

### MedGemma

MedGemma remains a valuable medical reference/control. Matching or exceeding MedGemma on selected medical measurements may strengthen evidence, but it cannot replace the canonical commandMed safety hard gates.

## 8. Fail-closed clarification rule

Until the pending clinical/statistical gate thresholds are frozen under the required authority/evidence, Spec 005 must distinguish:

```text
ADMISSION_CANDIDATE_OR_PROVISIONAL_LEADER
```

from:

```text
CANONICAL_TOURNAMENT_SELECTED_WINNER
```

The canonical Spec 004 harness still has only `SELECTED` and `NO_SELECTION`. This artifact does not create a third harness outcome. Any “provisional leader” terminology is clarification/planning evidence outside the canonical tournament result and cannot be represented as `SELECTED`.

## 9. Remaining safety-floor work

Before a live canonical tournament could legitimately return `SELECTED`, at minimum:

1. exact applicable benchmark/metric slices must be frozen;
2. public/private/Gold access boundaries must be resolved;
3. contamination/quarantine controls must be exact;
4. the pending clinical/statistical threshold evidence must satisfy Spec 002 requirements;
5. clinical review authority must be bound;
6. exact statistical/sample-size rationale must be bound;
7. execution must be separately authorized;
8. exact-head evidence and independent review must pass.

## 10. Authority boundary

```text
SAFETY_POLICY_REDEFINED=NO
NEW_CLINICAL_THRESHOLD_CREATED=NO
BENCHMARK_PAYLOAD_OPENED=NO
BENCHMARK_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PLAN_AUTHORITY=NONE
CLARIFICATION_LIFECYCLE=IN_PROGRESS
NEXT_LIFECYCLE_STEP=CLARIFY
```
