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

## 2. Immutable Spec Kit bootstrap

The bootstrap itself is **Spec 001 T001**. It is not a prerequisite that occurs outside bounded execution authority.

The reviewed Spec Kit source identity for the v0.15.1 planning baseline is:

```text
SPEC_KIT_RELEASE=v0.15.1
SPEC_KIT_COMMIT=489a3d51d152fa160d88d86781a924e99c4af832
```

The commit above is the GitHub `github/spec-kit` release commit that sets version `0.15.1`. T001 must re-verify that exact commit identity before executing it. A movable tag name alone is not sufficient execution evidence.

After Spec 000 is `CLOSED_CANONICAL`, start Spec 001 on a dedicated branch created from the exact canonical main that closed Spec 000. T001 may then run the immutable-source initialization command in uvx's isolated tool environment:

```bash
uvx --from git+https://github.com/github/spec-kit.git@489a3d51d152fa160d88d86781a924e99c4af832 specify init --here --force --integration agy --script py
```

`--force` is required because the repository is non-empty. It is **not** permission to trust overwrites.

Before accepting the generated diff, T001 must record bootstrap evidence including at least:

- commandMed pre-bootstrap HEAD;
- Spec Kit commit SHA above;
- `specify version` output from the same immutable source;
- `uv --version`;
- Python version;
- resolved package/dependency evidence available from the execution environment/logs;
- exact files changed by initialization;
- confirmation that the pre-bootstrap commandMed commit remains a rollback/checkpoint identity.

If the execution environment cannot provide enough dependency-resolution evidence to make the bootstrap reviewable, perform the bootstrap in a scratch clone/worktree at the same commandMed HEAD and treat its generated files as untrusted inputs to be copied/reconciled deliberately. Do not weaken reproducibility just to save a bootstrap step.

T002–T010 remain blocked until T001 safely reconciles generated changes and planning analysis reports no material contradiction.

## 3. Safe T001 initialization protocol

Before running Spec Kit initialization:

```bash
git status --short
git rev-parse HEAD
git ls-files -s AGENTS.md .specify/memory/constitution.md docs specs
```

The worktree must be clean/known and the exact pre-bootstrap commit must be recorded before `--force` is used.

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
- do not accept unexpected generated files without understanding why they exist;
- do not allow the bootstrap to change project authority merely because a generated file has a canonical-looking name.

T001 must then run the planning consistency analysis required by `specs/001-eval-charter/tasks.md`.

If initialization cannot be reconciled without destroying canonical planning content, dependency/source identity cannot be evidenced, or analysis finds an unresolved material contradiction, stop and report the conflict rather than improvising. T002–T010 stay blocked.

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
2. Reconcile the Spec Kit bootstrap if the active spec explicitly owns that task.
3. Run/perform `specify` only if the active spec is not already canonical.
4. `clarify` unresolved ambiguities that affect acceptance.
5. `plan` the smallest implementation satisfying the spec.
6. Build a requirement checklist.
7. Generate bounded tasks.
8. Run `analyze` against constitution/spec/plan/tasks.
9. If material inconsistency exists: STOP; repair the planning artifacts first.
10. Implement only the authorized tasks.
11. Run required validation.
12. Produce an evidence/closeout report.
13. Do not start the next spec until the current exit state is explicitly proven.

A roadmap dependency becoming visible is not authorization to execute it.

## 6. First Antigravity assignment

The first executable assignment after Spec 000 is `CLOSED_CANONICAL` is **Spec 001 — Evaluation Charter**, beginning with **T001 only**.

Use this prompt on a dedicated Spec 001 branch created from the exact canonical main that closed Spec 000:

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

Use Ponytail throughout: implement the minimum mechanism required by Spec 001.

Authority sequence:
- verify that Spec 000 is CLOSED_CANONICAL on the exact main used as this branch base;
- execute T001 first using the immutable Spec Kit source commit 489a3d51d152fa160d88d86781a924e99c4af832;
- safely initialize/reconcile the GitHub Spec Kit Antigravity integration (`agy`), record bootstrap source/environment evidence, and run the required planning analysis;
- DO NOT start T002–T010 unless T001 acceptance passes and analysis reports no unresolved material contradiction;
- if T001 fails, stop and report exact evidence.

Before any implementation beyond T001:
- verify exact git branch and HEAD;
- inspect the working tree and bootstrap diff;
- preserve commandMed canonical planning authority;
- confirm T001 acceptance;
- confirm Spec Kit analysis is clean enough to proceed.

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

Target outcome after T001 unlocks the remaining tasks:
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
