# Spec 002 Tasks — Safety Gates

**Spec:** `002-safety-gates`
**Status:** PLANNED / NOT YET IMPLEMENTED
**Canonical start base:** `cc02b0d99d67e5a720502953c99307c8b991720d`

No task below authorizes model execution, benchmark execution, PHI/restricted-data access, or training.

## Dependency graph

```text
T001 planning/research reconciliation
  ↓
T002 analysis / contradiction gate
  ↓
T003 safety-policy data contract
  ├─→ T004 forced-state / gate evaluation
  ├─→ T005 deterministic truth-boundary validation
  └─→ T006 threshold/applicability governance
          ↓
T007 canonical identity integration
          ↓
T008 fixture-only tests
          ↓
T009 reviewer documentation / status reconciliation
          ↓
T010 exact-head validation + closeout candidate
```

## T001 — Reconcile Spec 002 planning and external design evidence

**Goal:** create the bounded Spec 002 spec/research/plan/tasks/checklist from canonical main.

**Required evidence:**

- exact canonical base recorded;
- Spec 001 `CLOSED_CANONICAL` verified;
- Constitution/GMP/decision register/Spec 001 metrics reviewed;
- WHO/FDA/NIST primary design sources recorded with limitations;
- no unsupported clinical numeric threshold introduced.

**Exit:** planning artifacts exist and are internally coherent enough to analyze.

## T002 — Run planning consistency analysis

**Depends on:** T001

**Goal:** determine whether implementation would violate any canonical authority or duplicate Spec 001.

**Must answer:**

- no conflict with hard-gate dominance;
- no hidden gate weakening through `NOT_APPLICABLE`;
- no invented population clinical thresholds;
- FD-004 remains pending and not prematurely decided;
- no clinical tool/red-flag implementation scope creep;
- stdlib/offline path remains sufficient;
- no Spec 003/004 implementation leakage.

**Exit:** `analysis.md` reports `PASS_TO_IMPLEMENT` or explicit blockers. Any material blocker stops T003+.

## T003 — Implement canonical safety-policy contract

**Depends on:** T002=PASS_TO_IMPLEMENT

**Goal:** add the smallest declarative/validated policy representation.

**Target artifacts:**

- `data/eval/safety_policy.json`;
- `src/commandmed/eval_contract/safety.py`;
- minimal shared exports/enums only if required.

**Required invariants:**

- closed behavior/mechanism/task/threshold vocabularies;
- stable IDs;
- duplicate/malformed data rejected;
- no executable code in policy data;
- no third-party dependency.

## T004 — Implement forced-state and safety-gate fixture evaluation

**Depends on:** T003

**Goal:** prove non-overridable safety mechanics with synthetic policy fixtures.

**Required cases:**

- required `EMERGENCY` cannot become lower-authority outcome;
- required `ESCALATE` cannot become ordinary answer/tool/evidence state;
- exact required state + complete evidence may pass;
- missing evidence cannot pass;
- malformed/contradictory fixture fails closed.

**Prohibition:** do not author medical red-flag content or call a model.

## T005 — Implement deterministic/authoritative truth-boundary validation

**Depends on:** T003

**Goal:** enforce contract-level prohibition on generative substitution.

**Minimum task classes:**

- arithmetic;
- unit conversion;
- validated clinical score;
- medication interaction/contraindication lookup;
- structured schema validation;
- hard escalation policy;
- identity-bound evidence lookup.

**Required cases:**

- `generative_substitution=PROHIBITED` enforced;
- required mechanism unavailable + fallback `ANSWER` rejected;
- missing result identity cannot pass;
- altered typed deterministic result fails.

**Prohibition:** no actual clinical calculator, medication database, FHIR engine, or retrieval system.

## T006 — Implement threshold and applicability governance

**Depends on:** T003

**Goal:** make unsupported threshold/gate weakening impossible.

**Required behavior:**

- accept policy/sentinel zero-violation invariants;
- prohibit promotion of sentinel pass to population-rate claim;
- require `pass_allowed=false` for pending clinical thresholds;
- reject unsupported frozen statistical threshold records;
- bind over-triage pending state to `FD-004`;
- allow N/A only when the corresponding capability is explicitly out of scope;
- reject N/A while capability is claimed.

## T007 — Integrate canonical identity

**Depends on:** T003–T006

**Goal:** reuse Spec 001 semantic canonicalization for the safety-policy artifact.

**Required tests:**

- representation-only reorder equivalence where fields are defined set-like;
- semantic mutation changes digest;
- invalid policy is never promoted as a valid canonical policy identity.

**Prohibition:** do not create a second serializer/hash framework.

## T008 — Complete fixture-only test suite

**Depends on:** T004–T007

**Goal:** prove all safety policy requirements offline.

**Required command:**

```bash
python -m unittest discover -s tests -p "test_*.py"
```

**Exit:** focused Spec 002 tests pass and all prior Spec 001 tests remain green.

No benchmark/model/Gold case content may be needed by the tests.

## T009 — Write reviewer-facing safety documentation and reconcile status

**Depends on:** T008

**Goal:** make the policy human-reviewable without building UI/generator complexity.

**Target:**

- `docs/evaluation/safety-gates.md`;
- minimal factual updates to stale evaluation/spec status wording;
- `specs/README.md` reflects Spec 002 active candidate only; Spec 003 remains blocked/unactivated.

**Required clarity:**

- sentinel zero violations != zero real-world error;
- statistical thresholds remain pending until evidence prerequisites are met;
- FD-004 is not resolved by Spec 002;
- closure gives no model/training authority.

## T010 — Produce exact-head qualification and closeout candidate

**Depends on:** T008–T009

**Goal:** create auditable implementation-candidate evidence without self-referential SHA claims.

**Required evidence:**

- starting canonical base;
- exact candidate head in PR/review metadata;
- exact changed paths/tree identity;
- focused and full-suite test results;
- `git diff --check` equivalent/exact-head hygiene evidence;
- semantic SHA-256 for `data/eval/safety_policy.json`;
- acceptance matrix;
- unresolved clinical/founder threshold list;
- explicit activity/authority attestation.

**State after T010 pass:**

```text
SPEC_002=CLOSEOUT_CANDIDATE_NOT_CANONICAL
PR=READY_FOR_EXTERNAL_REVIEW_ELIGIBLE
SPEC_003_IMPLEMENTATION=NOT_AUTHORIZED
MODEL_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
```

Implementation merge still does not make Spec 002 `CLOSED_CANONICAL`; a dedicated closure-only PR remains required.
