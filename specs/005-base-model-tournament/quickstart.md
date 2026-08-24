# Spec 005 — Implementation Quickstart

**Audience:** JetBrains coding agent / reviewer.
**Purpose:** Validate implementation increments without crossing model, payload, device, Gold, PHI, provider or spend boundaries.

## 1. Read first

Before implementation, read in order:

1. `AGENTS.md`
2. `.specify/memory/constitution.md`
3. `specs/005-base-model-tournament/spec.md`
4. `specs/005-base-model-tournament/clarification-closeout.md`
5. `specs/005-base-model-tournament/research.md`
6. `specs/005-base-model-tournament/plan.md`
7. `specs/005-base-model-tournament/data-model.md`
8. `specs/005-base-model-tournament/contracts/preconstruction-control-contract.md`
9. `specs/005-base-model-tournament/tasks.md`

Use `tasks.md` as the implementation queue. Historical clarification files are rationale/evidence only.

## 2. Environment expectations

- Python 3.11.
- Standard library only unless a later task explicitly documents a separately approved dependency.
- No network required for validation.
- No model or benchmark payload required.

Do not install model/runtime/provider dependencies merely to satisfy Spec 005 planning-stage tests.

## 3. A1 corrective-maintenance gate

A1 is first and is intentionally separate from the Spec 005 implementation branch.

Before implementing Spec 005 consumers:

```text
1. verify live canonical main;
2. create a dedicated A1 corrective-maintenance branch from that exact main;
3. change only the frozen A1 path budget;
4. preserve data/eval/metrics.json V1 identity;
5. run focused + full offline tests;
6. obtain exact-head review;
7. merge A1 through the normal guarded process;
8. verify resulting canonical main;
9. only then start/reconcile the Spec 005 implementation branch.
```

Expected invariant:

```text
V1_METRICS_SHA256=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
```

## 4. Focused validation after A1

```text
python -m compileall -q src tests
python -m unittest tests.eval_contract.test_metrics_v2 -v
python -m unittest tests.test_tournament_metrics_v2_identity -v
python -m unittest discover -s tests -v
```

Expected outcome: all tests pass with no V1 identity drift. A missing CI workflow is not reported as CI PASS.

## 5. Focused Spec 005 validation

After the Spec 005 package is implemented:

```text
python -m compileall -q src tests
python -m unittest tests.spec005.test_preconstruction -v
python -m unittest tests.spec005.test_personnel -v
python -m unittest tests.spec005.test_access -v
python -m unittest tests.spec005.test_finance -v
python -m unittest tests.spec005.test_device -v
python -m unittest tests.spec005.test_activation -v
python -m unittest tests.spec005.test_manifest -v
python -m unittest discover -s tests/spec005 -v
python -m unittest discover -s tests -v
```

## 6. Required validation scenarios

### Scenario A — missing prerequisite stays blocked

Provide synthetic metadata with one required gate absent/stale.

Expected:

```text
PRECONSTRUCTION=NOT_READY_TO_CONSTRUCT
NO_AUTOMATIC_ACTIVATION
NO_SPEC004_EXECUTABLE_PROJECTION
```

### Scenario B — Private Gold cannot become selection source

Create a synthetic source-route/lineage fixture that tries to use Private Gold as a parent or `CHECKPOINT_SELECTION` source.

Expected: deterministic prohibited/blocked result.

### Scenario C — personnel eligibility does not grant access

Create synthetic `ELIGIBLE` + `ACTIVE` assignment records without an A13 grant.

Expected: assignment may be valid, real access remains absent. `ALLOW_GRANT_CONSIDERATION` is not access authorization.

### Scenario D — Gold/result exposure invalidates incompatible roles

Create synthetic records with actual Private-Gold case exposure or same-suite candidate-result exposure for a content role.

Expected: content-role eligibility blocked/ineligible and A13 revoke/deny signal where applicable.

### Scenario E — finance `$0` is not silent PASS

Use an incomplete requirement manifest with no active authorization.

Expected: blocked/unknown, not `A14_NOT_REQUIRED_PASS` merely because spend is zero.

### Scenario F — authorization material change requires new identity

Attempt synthetic cap increase/period extension/vendor substitution on an existing authorization identity.

Expected: reject in-place material amendment; require a superseding authorization identity.

### Scenario G — device contract validates metadata without executing device

Validate synthetic complete/incomplete run metadata against the frozen five-target protocol.

Expected: deterministic PASS/BLOCKED/HARD_FAIL/INCOMPLETE semantics as appropriate, with no subprocess/runtime execution.

### Scenario H — synthetic activation proves validator only

Validate a synthetic fully satisfied A1–A14 fixture and an activation record.

Expected: validator can return a fixture-valid state. The test must explicitly assert that fixture validity does not create canonical real-world construction authority.

### Scenario I — Spec 004 projection fails closed

Attempt to build the Spec 004 projection with missing metrics-v2 identity, stale prerequisite snapshot, incomplete device evidence, Private-Gold selection source, or missing required threshold identity.

Expected: no executable projection.

## 7. Forbidden quickstart actions

Do NOT add commands that:

- download or load a model;
- run inference;
- download/access benchmark case payloads;
- access Private Gold;
- invoke provider APIs;
- execute llama.cpp/device qualification;
- accept gated terms;
- provision storage/services;
- read credentials/payment instruments;
- make payments or contracts;
- use PHI/restricted data.

Those are later separately authorized execution activities, not implementation validation.

## 8. Phase completion rule

After each task: run its smallest focused test.

After each story phase: run all `tests/spec005` tests relevant to that phase plus inherited regression tests touched by the phase.

Before implementation PR review:

```text
python -m compileall -q src tests
python -m unittest discover -s tests -v
```

Then obtain fresh independent exact-head review. Do not mark Ready/merge merely because a bot status is green.