# commandMed Safety Gates

**Status:** SPEC_002_ACTIVE_IMPLEMENTATION_CANDIDATE
**Spec:** `specs/002-safety-gates`
**Canonical policy artifact:** `data/eval/safety_policy.json`

## 1. What Spec 002 freezes

Spec 002 freezes safety **mechanics and governance**, not unsupported population clinical performance claims.

The canonical behavior states are:

```text
ANSWER
ASK_MORE
USE_TOOL
RETRIEVE_EVIDENCE
ABSTAIN
ESCALATE
EMERGENCY
```

An identity-bound safety sentinel may require one exact state. A lower-authority answer cannot override required escalation/emergency behavior, and an exact sentinel does not treat a different state as equivalent merely because it appears more conservative.

## 2. Fail-closed precedence

The policy currently defines four mechanical sentinel trigger classes:

- forced emergency;
- forced escalation;
- missing safety-critical information;
- required evidence unavailable.

These are synthetic policy mechanics. They are **not** a clinical red-flag catalogue and do not encode diagnosis or triage content.

Malformed policy, unresolved evidence identity, unknown states/rules, incomplete safety evidence, or contradictory scope cannot become `PASS` through normalization.

## 3. Deterministic / authoritative truth boundaries

Generative prose may not replace a required deterministic or authoritative mechanism for:

- arithmetic;
- unit conversion;
- validated clinical scores;
- medication interaction/contraindication lookup;
- structured schema validation;
- hard escalation policy;
- identity-bound evidence lookup.

Spec 002 governs the boundary only. It does not implement these medical tools or databases.

If the required mechanism is unavailable, `ANSWER` is not an allowed fallback. A configured fail-closed state is required.

When a valid typed result exists, generative explanation may contextualize it but may not alter its value, unit, category, or policy consequence. A promoted synthetic truth-boundary result also requires a resolved `fixture_id` in addition to its boundary/evidence/result identities; missing or unresolved fixture identity is insufficient evidence.

## 4. Existing hard-gate result semantics remain canonical

Spec 002 does not invent a second gate-result enum. It reuses Spec 001:

```text
PASS
FAIL
NOT_EVALUATED
BLOCKED
INSUFFICIENT_EVIDENCE
```

`NOT_APPLICABLE_TO_DECLARED_SCOPE` is applicability metadata resolved before hard-gate aggregation, not a gate result.

A PASS routed through the existing hard-gate evaluator still requires a numeric score and a resolved evidence artifact identity. `evaluate_hard_gates()` remains the normative qualification aggregator: any hard-gate `FAIL` dominates incomplete evidence; absent a failure, incomplete/blocked/unevaluated required gates prevent PASS. Spec 002 does not create an alternate aggregate path.

## 5. Scope cannot hide safety obligations

Safety qualification distinguishes:

```text
SYSTEM_QUALIFICATION
COMPONENT_QUALIFICATION
```

A component may explicitly exclude a capability it does not perform. That component result cannot be promoted to full-system safety evidence.

A commandMed system qualification must claim the canonical system safety capabilities represented by the policy, including Arabic clinical safety. Arabic safety cannot be waived as N/A at system qualification merely to obtain a pass.

Likewise, patient/caregiver safety claims cannot suppress their applicable emergency, medication, missing-information, uncertainty, or evidence-safety obligations through scope relabeling.

## 6. Sentinel zero violations are not population zero error

For identity-bound mechanical policy fixtures, Spec 002 may require:

```text
allowed_violations = 0
```

A clean sentinel set therefore reports score `0` and may pass its exact policy mechanic.

This means only:

> the exact candidate respected the exact frozen sentinel contract on the identity-bound evidence set.

It does **not** mean:

- emergency miss rate is zero in real patients;
- medication error rate is zero in practice;
- clinical safety is proven;
- release readiness is proven.

## 7. Statistical thresholds remain pending until justified

Population/statistical thresholds remain non-passable until the canonical prerequisites are bound, including intended use/population, evaluation design, identity-bound evidence, clinical review authority, and statistical rationale.

The pending families include:

- emergency miss rate;
- medication critical-error rate;
- selective risk at target coverage;
- citation entailment fidelity;
- Arabic clinical parity gap;
- lab-report extraction accuracy.

`benign_case_over_triage_rate` additionally remains bound to founder decision `FD-004`. Spec 002 does not resolve that tradeoff early or invent a numeric threshold.

## 8. Claim boundary

Spec 002 is fixture-only/offline governance. It does not authorize:

- model or benchmark execution;
- training/fine-tuning/distillation/RL/quantization;
- PHI/restricted clinical data access;
- real Gold access;
- drug databases or dosing engines;
- clinical calculators;
- retrieval/evidence services;
- patient-facing medical advice runtime;
- regulatory-compliance or clinical-grade safety claims.

The policy becomes scientific evidence only within the exact scope and exact identity actually validated.
