# Spec 000 — Program Charter

**State:** CLOSED_CANONICAL
**State effectiveness:** effective only when the dedicated closure-only PR containing this state transition is merged into canonical `main`
**Execution authority:** governance/documentation only
**Canonical planning package:** `b0398f2fe514bd3ccd339908d739aef61055f929`
**Closeout evidence:** `specs/000-program-charter/closeout.md`

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

All 12 criteria are evidenced as `PASS` in `specs/000-program-charter/closeout.md`, bound to canonical planning merge `b0398f2fe514bd3ccd339908d739aef61055f929` and exact artifact blob identities.

## Canonical closeout protocol

The planning package remained `CANONICAL_PLANNING` until it existed on canonical `main`. The dedicated closure-only PR then:

1. recorded the exact planning-package merge commit SHA;
2. verified every required artifact on that exact canonical main;
3. recorded exact artifact blob identities;
4. changed this header to `CLOSED_CANONICAL`;
5. changed the Spec 000 registry row to `CLOSED_CANONICAL`;
6. authorized Spec 001 T001 only after this closure PR itself becomes canonical;
7. performed no Spec Kit bootstrap, model/data work, or Spec 001 implementation.

The closure PR cannot pre-record its own future merge SHA. Its own canonical identity is the GitHub merge record produced at merge time and is verified against live `main` immediately afterward, as defined in the closeout evidence. No recursive third PR is required solely to restate that canonical GitHub merge identity.

## Exit state

`CLOSED_CANONICAL` is effective only once this closure-only state transition is merged into canonical `main` and that resulting main SHA is verified.

After effective closure:

- Spec 001 **T001 only** is `AUTHORIZED_TO_START`.
- Spec 001 T002–T010 remain blocked until T001 passes its bootstrap-reconciliation and analysis acceptance criteria.
- Spec 002+ remain not started/blocked.
- Model execution authority remains NONE.
- Training authority remains NONE.
