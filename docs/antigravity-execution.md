# Antigravity Execution Guide

**Status:** CANONICAL OPERATOR GUIDE
**Primary integration:** GitHub Spec Kit `agy` skills

This guide tells Google Antigravity how to execute commandMed without converting the roadmap into uncontrolled implementation.

## 1. Bootstrap principle

Spec Kit may install its scripts/templates/skills, but it must not silently overwrite commandMed's canonical planning authority.

Canonical planning files include at least:

- `AGENTS.md`
- `.specify/memory/constitution.md`
- `docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md`
- `docs/decision-register.md`
- `specs/README.md`
- active bounded spec files

## 2. Recommended pinned Spec Kit bootstrap

At the planning snapshot date, use a pinned known release rather than an unbounded moving main branch. Verify the release before execution.

From the repository branch that contains this plan:

```bash
uvx --from git+https://github.com/github/spec-kit.git@v0.15.1 specify init --here --force --integration agy --script py
```

Why `--force`: the repository is no longer empty. This flag permits initialization into the directory; it is NOT permission to accept arbitrary overwrites.

## 3. Safe initialization protocol

Before running Spec Kit initialization:

```bash
git status --short
git rev-parse HEAD
git ls-files -s AGENTS.md .specify/memory/constitution.md docs specs
```

After initialization:

```bash
git status --short
git diff -- AGENTS.md .specify/memory/constitution.md docs specs .agents .specify
```

Then reconcile deliberately:

- preserve commandMed `AGENTS.md` requirements;
- preserve the commandMed constitution;
- preserve canonical master-plan/decision/spec files;
- keep valid Spec Kit-generated skills/templates/scripts needed for `agy` integration;
- do not delete safety/provenance language because a generated template is shorter;
- do not accept unexpected generated files without understanding why they exist.

If initialization cannot be reconciled without destroying canonical planning content, stop and report the conflict rather than improvising.

## 4. Ponytail use

Read `.agents/skills/ponytail/SKILL.md` before planning implementation.

Ponytail reduces accidental architecture. It does not reduce assurance.

In early specs, reject unnecessary:

- vector databases;
- orchestration frameworks;
- plugin frameworks;
- service meshes;
- queues/workers;
- databases for small static registries;
- model-serving SDKs before inference is authorized;
- cloud resources before a requirement needs them.

## 5. Spec Kit execution lifecycle

For one bounded spec only:

1. Read constitution and active spec.
2. Run/perform `specify` only if the active spec is not already canonical.
3. `clarify` unresolved ambiguities that affect acceptance.
4. `plan` the smallest implementation satisfying the spec.
5. Build a requirement checklist.
6. Generate bounded tasks.
7. Run `analyze` against constitution/spec/plan/tasks.
8. If material inconsistency exists: STOP; repair the planning artifacts first.
9. Implement only the authorized tasks.
10. Run required validation.
11. Produce an evidence/closeout report.
12. Do not start the next spec until the current exit state is explicitly proven.

A roadmap dependency becoming visible is not authorization to execute it.

## 6. First Antigravity assignment

The first executable implementation assignment is **Spec 001 — Evaluation Charter**.

Use this prompt after the Spec Kit integration has been safely initialized:

```text
COMMANDMED — EXECUTE SPEC 001 ONLY

Repository: TheHalfMoon/commandMed

Read, in order:
1. AGENTS.md
2. .specify/memory/constitution.md
3. docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md
4. docs/decision-register.md
5. specs/README.md
6. specs/001-eval-charter/spec.md
7. specs/001-eval-charter/plan.md
8. specs/001-eval-charter/tasks.md
9. specs/001-eval-charter/checklists/requirements.md
10. .agents/skills/ponytail/SKILL.md

Use the installed GitHub Spec Kit Antigravity skills (`agy`).
Use Ponytail throughout: implement the minimum mechanism required by Spec 001.

Before implementation:
- verify exact git branch and HEAD;
- inspect the working tree;
- run the Spec Kit analysis step against constitution/spec/plan/tasks;
- if material contradictions remain, do not implement; report them.

Hard scope:
- execute ONLY Spec 001;
- fixture-only/local deterministic work;
- no model downloads;
- no model weights;
- no model inference;
- no training/fine-tuning/CPT/distillation/DPO/GRPO/RL/QAT;
- no PHI;
- no restricted dataset content;
- no third-party judge/model API calls;
- no Gold case content;
- no patient-facing medical claims.

Target outcome:
Build the minimal evaluation-governance foundation specified by Spec 001:
- verified benchmark registry contract;
- metrics and hard-gate catalog;
- private-Gold metadata/protocol contract;
- quarantine/contamination rules;
- deterministic canonical serialization/digests;
- fixture-only validation/tests;
- closeout evidence.

Do not add frameworks, databases, services, vector stores, model SDKs, or cloud infrastructure unless the active spec proves they are necessary. Prefer Python 3.11 standard library for the minimal deterministic implementation if implementation is authorized by the final plan.

At completion report:
- exact HEAD;
- exact changed paths;
- tests/validation run and results;
- deterministic artifact hashes;
- every acceptance criterion with PASS/FAIL evidence;
- unresolved risks;
- explicit statement that Spec 002+ remain NOT STARTED.

Do not start Spec 002.
```

## 7. Git behavior for Antigravity

- Never force-push.
- Never rewrite shared history.
- Never use destructive cleanup to make the working tree look clean.
- Do not commit unrelated changes.
- Keep one bounded spec per implementation branch/PR unless the active governance explicitly permits another layout.
- Treat exact HEAD and changed-path identity as scientific evidence.

## 8. Stop conditions

Stop rather than improvise if any of the following occurs:

- canonical planning files conflict materially;
- a benchmark cannot be verified against a primary/current source;
- a license or data-use right is unclear for an executable action;
- a task requires model inference/training not authorized by the spec;
- a Gold/private boundary would be crossed;
- implementation would weaken a safety/provenance guarantee;
- tests cannot establish deterministic identity required by the spec;
- scope expansion would be needed to proceed.

A safe STOP with precise evidence is a successful outcome.
