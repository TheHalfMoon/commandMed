# JetBrains Handoff — commandMed Spec 005

**Purpose:** Single implementation entry point for a JetBrains coding agent after the Spec Kit planning package is reviewed/landed.

## Current planning result

```text
SPEC=005-base-model-tournament
CLARIFICATION=COMPLETE
RESEARCH=COMPLETE
PLAN=COMPLETE
REQUIREMENTS_CHECKLIST=PASS
TASKS=COMPLETE
ANALYZE=PASS_NO_CRITICAL_OR_HIGH_FINDINGS
IMPLEMENTATION_QUEUE=tasks.md
```

This means the implementation design is complete. It does **not** mean model/tournament execution is authorized.

## Required reading order

Read these files before changing code:

1. `AGENTS.md`
2. `.specify/memory/constitution.md`
3. `specs/005-base-model-tournament/spec.md`
4. `specs/005-base-model-tournament/clarification-closeout.md`
5. `specs/005-base-model-tournament/research.md`
6. `specs/005-base-model-tournament/plan.md`
7. `specs/005-base-model-tournament/data-model.md`
8. `specs/005-base-model-tournament/contracts/preconstruction-control-contract.md`
9. `specs/005-base-model-tournament/quickstart.md`
10. `specs/005-base-model-tournament/tasks.md`

Historical `session-*-q*.md` files are supporting rationale. Do not turn them into extra tasks unless `tasks.md` explicitly references them.

## Paste-ready JetBrains prompt

```text
CONTINUE commandMed — SPEC 005 IMPLEMENTATION FROM SPEC KIT TASKS

Repository:
TheHalfMoon/commandMed

Work from exact live GitHub truth. Reverify main, the active implementation branch, and all relevant heads before mutation. Live canonical GitHub truth overrides stale SHAs in planning documents.

Your implementation authority is ONLY the code/documentation work explicitly listed as unchecked tasks in:
specs/005-base-model-tournament/tasks.md

Read in this exact order before editing:
1. AGENTS.md
2. .specify/memory/constitution.md
3. specs/005-base-model-tournament/spec.md
4. specs/005-base-model-tournament/clarification-closeout.md
5. specs/005-base-model-tournament/research.md
6. specs/005-base-model-tournament/plan.md
7. specs/005-base-model-tournament/data-model.md
8. specs/005-base-model-tournament/contracts/preconstruction-control-contract.md
9. specs/005-base-model-tournament/quickstart.md
10. specs/005-base-model-tournament/tasks.md

EXECUTION MODE:
- Work one unchecked task at a time in numeric order.
- Continue automatically to the next task when the current task's focused tests pass and no STOP/AUTHORITY gate is reached.
- [P] tasks may be developed in parallel only when they edit different files and their prerequisites are satisfied.
- Use TDD for every task that has a corresponding test task: write/confirm the failing test first, then implement the smallest code that makes it pass.
- Mark a task complete only after its exact acceptance evidence exists.
- After each story phase, run the applicable focused suite.
- Before final review, run the full offline suite from quickstart.md.
- Make small coherent commits. Never force-push, rebase, reset shared history, or silently rewrite historical governance identities.

A1 SPECIAL BRANCH RULE:
- T003–T010 are a separate corrective-maintenance implementation.
- Create the A1 branch from exact live canonical main.
- Do not implement A1 on spec/005-clarify.
- Preserve data/eval/metrics.json exactly, including historical V1 digest:
  304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
- Change only the frozen A1 path budget in plan.md/tasks.md.
- Fully test/review/merge A1 and reverify canonical main before starting T011.
- If you cannot create/merge the GitHub PR from the current environment, stop at the A1 STOP gate and report the exact branch/head/tests/next required GitHub action. Do not duplicate V2 locally to bypass the gate.

TECHNICAL DEFAULTS:
- Python 3.11.
- Standard library only.
- Reuse existing commandmed canonicalization, safety, lineage and tournament logic.
- Prefer plain dictionaries + small enums/frozensets + pure functions.
- Deterministic sorted reason codes and canonical SHA-256 projections.
- Ordinary malformed parsed JSON must fail closed without crashing.
- Unknown state/vocabulary = reject/block, never permissive fallback.
- Do not introduce a generic rule engine, database, web service, plugin system or model runtime wrapper.

HARD BOUNDARIES — DO NOT CROSS:
MODEL_EXECUTION=PROHIBITED
MODEL_WEIGHT_ACCESS_OR_DOWNLOAD=PROHIBITED
MODEL_CONVERSION_OR_QUANTIZATION_EXECUTION=PROHIBITED
TRAINING=PROHIBITED
BENCHMARK_PAYLOAD_ACCESS_OR_EXECUTION=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
PROVIDER_OR_API_GENERATION=PROHIBITED
PHI_OR_RESTRICTED_DATA=PROHIBITED
GATED_TERM_ACCEPTANCE_OR_ASSET_ACCESS=PROHIBITED
DEVICE_OR_LLAMA_CPP_EXECUTION=PROHIBITED
STORAGE_PROVISIONING=PROHIBITED
PERSONNEL_CREDENTIAL_INGESTION=PROHIBITED
PAYMENT_CONTRACT_REIMBURSEMENT_OR_SPEND_EXECUTION=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
REAL_A15_CONSTRUCTION_ACTIVATION=PROHIBITED_UNTIL_SEPARATELY_AUTHORIZED
REAL_SELECTION_CASE_AUTHORING=PROHIBITED_UNTIL_A15_IS_SEPARATELY_AUTHORIZED

You MAY create synthetic/non-medical fixture dictionaries that represent gated states solely to test validators. A synthetic PASS/ACTIVE/AUTHORIZED fixture NEVER creates real authority.

SCIENTIFIC VALUES:
- Never invent missing clinical thresholds, margins, alpha/confidence/power values, sample size N, allocation, nuisance parameters, reviewer identities, runtime SHAs or contamination results.
- Implement the record schemas/validators/state machines that require those values.
- When a real required value is absent, the implementation must return BLOCKED/INCOMPLETE/STALE as specified.
- Candidate results must never be used to select or relax thresholds, N, allocation, source slices, review rules or resource gates.

SCOPE CONTROL:
- Do not broaden tasks to unrelated refactors.
- Do not change Specs 001–004 historical semantics except the exact additive A1 paths.
- Spec 002 remains safety authority.
- Spec 003 remains lineage/admission authority.
- Spec 004 remains deterministic tournament comparison/no-selection authority.
- Spec 005 adds scientific/preconstruction/access/finance/device/activation prerequisites around those inherited contracts.

VALIDATION:
Use specs/005-base-model-tournament/quickstart.md.
At minimum before implementation review run:
  python -m compileall -q src tests
  python -m unittest discover -s tests/spec005 -v
  python -m unittest discover -s tests -v

Do not claim CI PASS unless an actual GitHub Actions run exists on the exact head.
Do not claim independent-review PASS unless a fresh applicable review exists for the exact head.
Do not mark a PR Ready or merge merely because CodeRabbit/another bot is green.

PROGRESS REPORTING:
After each completed task, report:
TASK=<ID>
STATUS=COMPLETE
FILES=<exact paths>
FOCUSED_TESTS=<exact command/result>
HEAD=<exact commit SHA if committed>
NEXT_TASK=<ID>
AUTHORITY_BOUNDARY_UNCHANGED=YES

If blocked, report:
TASK=<ID>
STATUS=BLOCKED
BLOCKER=<exact missing evidence/authority/test failure>
NO_BYPASS_ATTEMPTED=YES
NEXT_REQUIRED_ACTION=<specific action>

Start with T001 now and continue until you hit the explicit A1 STOP gate or a real failing prerequisite.
```

## What “finished” means for JetBrains

JetBrains implementation is complete when:

- T001–T049 applicable code-build tasks are checked with evidence;
- A1 was landed independently before V2 consumers;
- all `tests/spec005` pass;
- inherited Specs 001–004 regressions pass;
- no prohibited side-effect mechanism was introduced;
- documentation matches implemented paths;
- the exact implementation head is ready for independent review.

It is **not** required — and is not currently authorized — to create the real Arabic selection suite, access models/benchmarks/Gold, run devices, spend money, execute the tournament or choose a winner.

## Fast navigation for a human

If you only want to follow progress, open:

```text
specs/005-base-model-tournament/tasks.md
```

That is the authoritative checklist. The first unchecked task is the next work item.