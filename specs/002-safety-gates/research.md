# Spec 002 Research — Safety-Gate Design Evidence

**Spec:** `002-safety-gates`
**Research date:** 2026-08-22
**Purpose:** bounded design evidence only; not regulatory advice and not a claim of compliance

## 1. Research question

What external primary guidance supports commandMed's safety-gate architecture, and what does that guidance **not** justify?

Spec 002 needs enough evidence to design fail-closed safety semantics without inventing clinical performance numbers.

## 2. Primary sources reviewed

### R-001 — WHO: Ethics and governance of artificial intelligence for health

Canonical source:
`https://www.who.int/publications/i/item/9789240029200`

Related WHO summary:
`https://www.who.int/news/item/28-06-2021-who-issues-first-global-report-on-ai-in-health-and-six-guiding-principles-for-its-design-and-use`

Relevant design support:

- human autonomy and control over health-care decisions;
- promotion of human well-being and safety;
- safety, accuracy and efficacy for well-defined uses;
- transparency/explainability;
- responsibility/accountability;
- continuing assessment during use.

What it does **not** establish for commandMed:

- a universal numeric acceptable emergency miss rate;
- a universal medication-error threshold;
- a release threshold for any specific commandMed role/modality;
- a claim that commandMed is clinically validated or compliant.

### R-002 — WHO: Guidance on large multi-modal models for health

Canonical source:
`https://www.who.int/publications/i/item/9789240084759`

Relevant design support:

- health LMMs require governance proportional to risks and intended use;
- general-purpose capability does not itself prove safe health performance;
- safety/governance concerns apply across development and deployment.

What it does **not** establish:

- commandMed-specific threshold values;
- modality maturity from input acceptance;
- permission to substitute a generative model for deterministic clinical mechanisms.

### R-003 — FDA: Clinical Decision Support Software, Final Guidance (January 2026)

Canonical source:
`https://www.fda.gov/regulatory-information/search-fda-guidance-documents/clinical-decision-support-software`

FDA policy navigator context:
`https://www.fda.gov/medical-devices/digital-health-center-excellence/step-6-software-function-intended-provide-clinical-decision-support`

Relevant design support:

- intended user and patient population matter;
- required input information, relevance and data-quality expectations should be identifiable;
- knowns/unknowns and the basis for recommendations should be reviewable where independent review is expected;
- automation level and time-criticality affect the risk that users over-rely on automated recommendations.

What it does **not** establish:

- that commandMed is or is not a regulated medical device;
- a universal commandMed emergency/medication threshold;
- that clinician review alone is sufficient for patient-facing use;
- permission to claim regulatory compliance.

### R-004 — NIST AI RMF 1.0 / Generative AI Profile (NIST AI 600-1)

Canonical sources:
`https://www.nist.gov/itl/ai-risk-management-framework`
`https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence`

Relevant design support:

- explicit risk management across the lifecycle;
- validity/reliability and safety are trustworthiness concerns that should be measured and managed;
- generative-AI-specific risks require structured governance rather than average quality alone.

What it does **not** establish:

- medical clinical thresholds;
- a medical-device regulatory classification;
- commandMed release readiness.

### R-005 — FDA: AI-enabled device lifecycle guidance status

Current FDA digital-health guidance index:
`https://www.fda.gov/medical-devices/digital-health-center-excellence/guidances-digital-health-content`

Current state observed on 2026-08-22:

- January 2026 Clinical Decision Support Software guidance is Final;
- August 2025 Predetermined Change Control Plan guidance for AI-enabled device software functions is Final;
- January 2025 broad AI-enabled device lifecycle/marketing submission recommendations remain identified as Draft on FDA's guidance page.

Design implication:

Use final/current guidance where possible and label draft material as draft. Do not silently treat a draft regulatory document as a binding implementation requirement.

## 3. Derived design decisions for Spec 002

The following are evidence-informed **project governance choices**, not quoted regulatory requirements.

### RD-001 — Separate policy invariants from statistical clinical thresholds

A deterministic policy violation can be zero-tolerance without claiming that real-world clinical error probability is zero.

Therefore Spec 002 may freeze `0 allowed violations` for identity-bound sentinel/policy invariants while leaving population-level rate thresholds pending until clinical/statistical evidence exists.

### RD-002 — Time-critical forced states must be non-overridable

Where a later identity-bound safety policy marks an exact fixture/state as requiring emergency or escalation handling, lower-authority prose cannot override that decision.

Spec 002 validates the precedence mechanism only; it does not author the medical red-flag catalogue.

### RD-003 — Required inputs/knowns/unknowns are part of safety state

If safety-critical information is explicitly required and missing, ordinary `ANSWER` cannot be the default. A configured safe state such as `ASK_MORE`, `ABSTAIN`, `ESCALATE`, or `EMERGENCY` is required.

### RD-004 — Deterministic/authoritative truth remains external to generative prose

Arithmetic, unit conversion, validated clinical scores, authoritative interaction/contraindication lookup, schema validation, hard escalation policy, and identity-bound evidence lookup remain truth-boundary classes where generative substitution is prohibited by default.

### RD-005 — Applicability must be claims-bound

A required gate may be `NOT_APPLICABLE` only when the corresponding capability is explicitly outside the declared scope. A system may not claim Arabic, lab/document, patient, or other capability while suppressing its required gate as not applicable.

## 4. Threshold evidence conclusion

The reviewed primary guidance supports rigorous, risk-based and transparent safety evaluation. It does **not** provide a scientifically defensible universal value for:

- `emergency_miss_rate`;
- `medication_critical_error_rate`;
- `selective_risk_at_target_coverage`;
- `citation_entailment_fidelity`;
- `arabic_clinical_parity_gap`;
- `lab_report_field_extraction_accuracy`;
- `benign_case_over_triage_rate`.

Therefore Spec 002 must not invent numeric population thresholds merely to mark planning complete.

Before any such statistical threshold becomes frozen, the threshold record must bind at minimum the intended use/population, metric definition, evidence source, clinical/statistical rationale, reviewer/owner authority, and canonical revision.

FD-004 remains specifically required for the benign over-triage product/ethics tradeoff when the patient release gate is actually due.

## 5. Regulatory-scope disclaimer

This research record does not determine whether any future commandMed product is a medical device, CDS, wellness product, research software, or another regulated category in any jurisdiction. Product classification and legal/regulatory strategy require separate qualified review when intended use, claims, users, deployment and jurisdiction are concrete.
