# commandMed Constitution

**Version:** 0.1.0
**Ratified:** 2026-08-21
**Status:** CANONICAL PLANNING CONSTITUTION

## Preamble

commandMed exists to investigate how much trustworthy Health & Medical Intelligence can be compressed into an efficient, privacy-oriented system that can serve ordinary people and healthcare professionals. The project values scientific validity over leaderboard theater and clinical safety over convenience.

## I. Evidence Before Training

No training, adaptation, distillation, preference optimization, reinforcement learning, or compression experiment may define its own success criteria.

A frozen evaluation contract must exist before an optimization run begins. It must define primary metrics, safety hard gates, relevant holdouts, accepted comparison rules, and failure conditions.

Public benchmark wins alone cannot authorize release claims.

## II. Clinical Safety Is a Hard Gate

Critical failures cannot be averaged away by high mean scores.

At minimum, independent safety strata must cover where applicable:

- missed emergencies and false reassurance;
- inappropriate emergency escalation;
- medication/dose errors;
- allergies and interactions;
- renal/hepatic considerations;
- pregnancy and pediatric safety;
- critical omissions;
- unsupported certainty;
- unsafe tool routing;
- failure to abstain or ask for missing information.

Any safety-critical threshold must be frozen before the evaluation used to judge it.

## III. Provenance, Licensing, and Data Lineage

Every data/model/evidence asset used for research must be traceable.

Required metadata includes where applicable:

- source identifier and canonical location;
- version/revision and retrieval time;
- license and allowed use;
- redistribution/modification/commercial constraints;
- PHI/privacy classification and de-identification status;
- cryptographic content identity;
- split assignment;
- contamination/benchmark-overlap status;
- synthetic/teacher provenance;
- verification state.

Unclear rights are a blocker, not an invitation to assume permission.

## IV. Smallness Is Measured in Resources

The project does not define "small" solely by parameter count.

Claims must be grounded in named devices and report at least:

- installed/package bytes;
- peak RAM;
- context/KV memory behavior;
- time to first token;
- prefill and decode performance;
- sustained performance;
- energy/battery impact;
- thermal behavior;
- quality and safety after compression.

## V. Universal Roles, Shared Medical Truth

Patients, caregivers, clinical professionals, learners, and researchers are first-class users of the research program.

Training behavior may be grouped into a small number of classes, but role-specific evaluation remains mandatory. The underlying medical facts must not change to flatter a role; communication, detail, permitted actions, and escalation behavior may adapt.

Patient-facing usefulness is not proven by professional benchmark scores.

## VI. Hybrid Multimodal Medical Intelligence

commandMed is a multimodal system, not necessarily a single monolithic neural network.

Specialized perception/signal modules are allowed and preferred when they improve verifiability, safety, resource use, or modality fidelity.

All modalities should converge on a shared evidence contract capable of representing:

- `CLAIM`
- `EVIDENCE`
- `SOURCE_PROVENANCE`
- `CONFIDENCE`
- `UNCERTAINTY`
- `CONTRADICTION`
- `MISSING_INFORMATION`
- `ABSTENTION`
- `RECOMMENDED_NEXT_EVIDENCE`

A model accepting an image, waveform, or volume is not evidence that the modality is mature.

## VII. Deterministic Truth Boundaries

When a task has a reliable deterministic or authoritative mechanism, generative inference must not silently replace it.

Examples include:

- arithmetic and unit conversion;
- validated clinical scores;
- schema/profile validation;
- structured field validation;
- drug/interaction database lookup;
- source/evidence retrieval;
- policy or hard escalation rules.

The model may select a tool and explain verified output, but safety-critical deterministic results are not overridable by prose.

## VIII. Holdout Quarantine and Anti-Contamination

Private evaluation material is separated from optimization.

Private Gold content must not enter:

- continued pretraining;
- SFT;
- teacher generation;
- distillation;
- DPO/RL;
- prompt optimization;
- hyperparameter tuning;
- checkpoint selection;
- backbone/model selection.

Access, identities, and any permitted scoring events must be auditable.

## IX. Reproducibility and Identity-Bound Evidence

Promoted research outputs must be reproducible from canonical inputs/configuration and bound to exact identities/hashes.

Runtime metadata must not silently change scientific identity. Seeds, dataset revisions, model revisions, environment assumptions, and evaluation configuration must be captured where relevant.

## X. Capability Preservation

Medical specialization is not allowed to hide catastrophic loss of general competence.

After material optimization stages, evaluate regression in:

- general reasoning;
- instruction following;
- English;
- Arabic;
- tool use;
- uncertainty behavior;
- safety.

The thresholds must be defined before the run being judged.

## XI. Patient Safety Uses Defense in Depth

A small model is never presumed safe enough to own all patient-critical decisions.

Patient-facing architecture must combine, where appropriate:

- active information acquisition;
- deterministic red-flag/escalation rules;
- deterministic tools;
- calibrated model reasoning;
- evidence retrieval;
- explicit abstention;
- human escalation.

The generative model may propose; non-overridable safety mechanisms may dispose.

## XII. Claims Integrity

Terms such as `best`, `SOTA`, `record-breaking`, `clinical-grade`, `safe`, and `superior` require evidence matching the breadth of the claim.

No release may infer:

- real-world patient benefit from MCQ accuracy;
- human+AI benefit from model-only testing;
- multimodal competence from input acceptance;
- medical equivalence from quantized general benchmarks;
- truth from teacher consensus;
- deployment feasibility from parameter count.

## XIII. Minimal Mechanism, Maximum Assurance

Ponytail/YAGNI applies to implementation complexity, not assurance guarantees.

Use the minimum mechanism needed by the active bounded spec, while preserving validation, security, privacy, provenance, reproducibility, tests, failure handling, auditability, and independent review.

## XIV. Bounded Spec Authority

The roadmap is not execution authority.

Work proceeds through dependency-ordered bounded Spec Kit specifications. Each spec must define scope, exclusions, dependencies, acceptance criteria, evidence, and exit state.

Later phases may not start merely because their intended design is described.

## Amendment rule

A constitutional principle may change only through an explicit documented decision that states:

- the current rule;
- proposed replacement;
- evidence/reason;
- affected specs and prior evidence;
- whether previously collected results remain comparable.

Silent constitutional drift is prohibited.
