# Spec 002 Analysis — Planning Consistency Gate

**Spec:** `002-safety-gates`
**Analyzed canonical base:** `cc02b0d99d67e5a720502953c99307c8b991720d`
**Analyzed planning branch lineage:** through `82870d90e56611cff48fb71d7e5d19da417478fd`, with the applicability repair committed immediately before this analysis record
**Analysis date:** 2026-08-22

## 1. Inputs inspected

Canonical authority/evidence:

- `.specify/memory/constitution.md`
- `docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md`
- `docs/decision-register.md`
- `specs/README.md`
- `specs/001-eval-charter/spec.md`
- `specs/001-eval-charter/closeout.md`
- `data/eval/metrics.json`
- `docs/evaluation/metrics-and-gates.md`
- `src/commandmed/eval_contract/model.py`
- `src/commandmed/eval_contract/validate.py`
- `src/commandmed/eval_contract/canonical.py`

Spec 002 planning artifacts:

- `spec.md`
- `research.md`
- `plan.md`
- `tasks.md`
- `checklists/requirements.md`

External primary design evidence is bounded in `research.md` and is not treated as regulatory compliance authority.

## 2. Analysis findings

### A-001 — Spec authority and dependency

**Verdict: PASS**

Canonical main closes Spec 001 and authorizes Spec 002 alone to start. Spec 003 implementation remains unactivated. Spec 002 contains no authority for model execution, benchmark execution, PHI/restricted data, real Gold cases, or training.

### A-002 — Hard-gate result vocabulary mismatch

**Initial finding: MATERIAL — REPAIRED BEFORE IMPLEMENTATION**

The first Spec 002 draft described `NOT_APPLICABLE` as a gate-result state. Canonical Spec 001 code does not define that result:

```text
GateEvaluationState =
PASS | FAIL | NOT_EVALUATED | BLOCKED | INSUFFICIENT_EVIDENCE
```

`NOT_APPLICABLE` exists in threshold/applicability semantics (`ThresholdState.NOT_APPLICABLE`), not `GateEvaluationState`.

**Repair:** Spec 002 now reuses the existing gate-result vocabulary exactly and resolves applicability before aggregation. No second gate-result enum is authorized.

### A-003 — N/A scope could hide required system capability

**Initial finding: MATERIAL — REPAIRED BEFORE IMPLEMENTATION**

A generic "capability out of scope" rule could let a narrow component evaluation be misreported as full commandMed safety evidence, or let Arabic be suppressed despite the canonical project baseline making Arabic a first-class research language.

**Repair:**

- applicability distinguishes `SYSTEM_QUALIFICATION` from `COMPONENT_QUALIFICATION`;
- component-scoped PASS cannot be promoted to system PASS;
- `arabic_clinical_parity_gap` cannot be N/A for commandMed system qualification;
- patient/caregiver safety claims cannot suppress applicable emergency/medication/missing-info/evidence gates through scope relabeling.

### A-004 — Existing hard-gate evaluator can be reused

**Verdict: PASS WITH IMPLEMENTATION REQUIREMENT**

Canonical `evaluate_hard_gates()` already fails closed for:

- absent/empty hard-gate catalog;
- malformed metric records;
- missing results;
- malformed result objects;
- invalid result statuses;
- PASS lacking a numeric score;
- PASS lacking a resolved `evidence_artifact_id`.

Therefore Spec 002 does not need a replacement hard-gate aggregator.

When a Spec 002 sentinel result is routed into this evaluator, the sentinel adapter must use:

```text
score = numeric violation count (0 for a clean sentinel set)
evidence_artifact_id = resolved identity of the exact sentinel evidence artifact
status = existing GateEvaluationState value
```

A zero violation count is evidence about the exact policy fixture set only; it is not a population clinical error estimate.

### A-005 — Threshold-state compatibility

**Verdict: PASS**

Spec 001 `ThresholdState` remains:

```text
DEFINED_NOT_YET_THRESHOLD_FROZEN
FROZEN
NOT_APPLICABLE
```

Spec 002's threshold-policy classes are separate governance metadata that explain *why/how* a threshold may be frozen or remain pending. They do not silently replace or broaden the existing metric enum.

No `metrics.json` threshold needs to be changed merely to implement Spec 002 policy mechanics.

### A-006 — Population clinical thresholds

**Verdict: PASS / INTENTIONALLY PENDING**

The Constitution requires safety-critical thresholds to be frozen before the evaluation that judges them. It does not require unsupported numbers to be invented before their evidence exists.

Spec 002 therefore freezes only policy/sentinel mechanics that can be defended now and records population clinical thresholds as non-passable pending prerequisites.

This is compatible with the roadmap because model/candidate execution remains unauthorized in Spec 002. Any later evaluation that depends on a pending statistical threshold cannot receive a threshold PASS until the threshold is frozen with the required evidence.

### A-007 — FD-004 timing

**Verdict: PASS**

The decision register states FD-004 is needed before patient release-gate freeze, not before Spec 002 planning.

Spec 002 does not ask the founder to choose an over-triage value now. It only records that `benign_case_over_triage_rate` is `PENDING_FOUNDER_AND_CLINICAL_EVIDENCE` and non-passable as a frozen release threshold until FD-004 is actually due and resolved.

### A-008 — Deterministic truth boundary does not implement clinical tools

**Verdict: PASS**

The planned contract defines task/mechanism classes and fallback behavior only. It explicitly excludes:

- clinical red-flag content;
- drug/interaction databases;
- dose engines;
- clinical-score implementations;
- FHIR engines;
- retrieval/evidence services.

Those belong to later bounded specs.

### A-009 — Canonical identity reuse

**Verdict: PASS WITH SMALL EXTENSION**

The existing semantic canonicalizer is sufficient. Spec 002 may require only explicit additions for new set-like field names and stable record IDs such as:

```text
rule_id
boundary_id
gate_id
```

and set-like arrays such as:

```text
behavior_states
prohibited_lower_states
required_result_identity_fields
allowed_unavailable_fallback_states
required_before_freeze
```

No second serializer/hash implementation is justified.

Unique-ID validation remains mandatory before promoting a policy digest as canonical evidence.

### A-010 — External guidance overreach

**Verdict: PASS**

WHO/FDA/NIST evidence is used only to support general safety design principles. The spec explicitly refuses to derive universal commandMed clinical error thresholds or regulatory-compliance claims from those sources.

### A-011 — Privacy/security/dependency surface

**Verdict: PASS**

The planned implementation is declarative JSON + Python stdlib validation/evaluation + synthetic fixtures. It needs no credentials, network access, dynamic code execution, patient data, restricted clinical content, new service, database, ML framework, or third-party dependency.

### A-012 — Future-spec leakage

**Verdict: PASS**

No Spec 003 data-lineage implementation, Spec 004 tournament harness, model selection, or runtime patient-safety implementation is authorized by the task graph.

## 3. Remaining non-blocking facts

These remain intentionally unresolved and must stay visible at implementation closeout:

1. population-level emergency miss threshold;
2. population-level medication critical-error threshold;
3. selective-risk target/coverage threshold;
4. citation entailment percentage threshold;
5. Arabic parity statistical threshold;
6. lab/document extraction statistical threshold;
7. benign over-triage threshold and FD-004 product posture.

Their unresolved state is not permission to evaluate them as PASS.

## 4. Implementation constraints derived from analysis

T003+ implementation must preserve all of the following:

```text
REUSE_EXISTING_GATE_RESULT_ENUM=YES
REUSE_EXISTING_HARD_GATE_AGGREGATOR=YES
NOT_APPLICABLE_AS_GATE_RESULT=NO
COMPONENT_PASS_PROMOTABLE_TO_SYSTEM_PASS=NO
SYSTEM_ARABIC_GATE_NA=NO
SENTINEL_ZERO_VIOLATIONS_IS_POPULATION_ZERO_ERROR=NO
PENDING_CLINICAL_THRESHOLD_PASS_ALLOWED=NO
FD_004_RESOLVED_IN_SPEC_002=NO
NEW_THIRD_PARTY_DEPENDENCY=NO
NETWORK_RUNTIME=NO
MODEL_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEC_003_IMPLEMENTATION=NOT_AUTHORIZED
```

## 5. Analyze verdict

The two material planning contradictions found during analysis were repaired before implementation:

1. gate-result/applicability vocabulary mismatch;
2. component/system applicability loophole.

No remaining material contradiction blocks the bounded fixture-only implementation.

```text
SPEC_002_ANALYZE=PASS_TO_IMPLEMENT
T003_T009=AUTHORIZED_WITHIN_SPEC_002_BOUNDS
T010=CANDIDATE_CLOSEOUT_ONLY_AFTER_EXACT_HEAD_VALIDATION
SPEC_003_IMPLEMENTATION=NOT_AUTHORIZED
MODEL_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
```
