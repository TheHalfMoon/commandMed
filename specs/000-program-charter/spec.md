# Spec 000 — Program Charter

**State:** CANONICAL_PLANNING
**Execution authority:** governance/documentation only

## Purpose

Establish commandMed's mission, constitutional rules, planning evidence, bounded-spec roadmap, and execution constraints before model or data work begins.

## Goals

- Define the Health & Medical Intelligence mission.
- Make patient, caregiver, professional, learner, and researcher use cases first-class.
- Establish evaluation-before-training authority.
- Establish clinical-safety, provenance, holdout, reproducibility, claims, and resource-measurement principles.
- Establish the hybrid multimodal architecture direction without prematurely selecting a model.
- Record unresolved founder decisions separately from evidence-resolvable experiments.
- Establish Spec Kit + Antigravity + Ponytail execution discipline.

## In scope

- repository planning documents;
- constitution;
- agent rules;
- Grand Master Plan;
- decision register;
- spec registry;
- first bounded executable spec definition.

## Out of scope

- source-code implementation;
- model/dataset downloads;
- inference;
- training or adaptation;
- evaluation against real models;
- PHI/restricted data;
- Gold case construction;
- cloud resources;
- product UI.

## Required artifacts

- `README.md`
- `AGENTS.md`
- `.specify/memory/constitution.md`
- `.agents/skills/ponytail/SKILL.md`
- `docs/research/2026-08-21-final-reconciliation.md`
- `docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md`
- `docs/decision-register.md`
- `docs/antigravity-execution.md`
- `specs/README.md`
- `specs/001-eval-charter/*`

## Acceptance criteria

1. Mission and success hierarchy are explicit.
2. No-training authority is explicit.
3. Safety hard-gate principle is explicit.
4. Data/model lineage rules are explicit.
5. Private Gold quarantine is explicit.
6. Resource-based smallness is explicit.
7. Three behavioral training classes and role-specific evaluation are explicit.
8. Hybrid multimodal principle is explicit.
9. License-sensitive model defaults are explicit.
10. Spec-of-specs dependencies are explicit.
11. Ponytail safety carve-outs are explicit.
12. Spec 001 is bounded and does not authorize model execution.

## Exit state

`CLOSED_CANONICAL` only after these artifacts are reviewed and merged as the canonical planning baseline.

Closing Spec 000 authorizes planning/execution of Spec 001 only. It does not authorize Spec 002+, model inference, or training.
