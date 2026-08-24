# Spec 005 — Base Model Tournament Tasks

**Status:** `REPAIRED_COMPLETE_READY_FOR_ANALYZE`
**Execution model:** TDD, offline, deterministic, Python 3.11 standard library.

> JetBrains should execute **one unchecked task at a time in numeric order** unless `[P]` explicitly permits parallel work. Do not treat historical clarification files as additional task queues.

## Non-negotiable authority boundary

These tasks build validators, state machines, metadata contracts and synthetic fixture tests only.

```text
MODEL_EXECUTION=PROHIBITED
MODEL_WEIGHT_ACCESS=PROHIBITED
BENCHMARK_PAYLOAD_ACCESS_OR_EXECUTION=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
PROVIDER_GENERATION=PROHIBITED
PHI_OR_RESTRICTED_DATA=PROHIBITED
DEVICE_EXECUTION=PROHIBITED
SPEND_OR_PAYMENT_EXECUTION=PROHIBITED
A15_REAL_CONSTRUCTION_ACTIVATION=PROHIBITED_UNTIL_SEPARATELY_AUTHORIZED
CURRENT_AUTHORIZED_SPEND_USD=0
```

Synthetic fixtures may represent otherwise-gated states solely to test validation logic; fixture validity never creates real authority.

---

## Phase 1 — Setup and Branch Discipline

**Goal:** Start from exact live GitHub truth and preserve Spec Kit / repository boundaries.

- [ ] T001 Read `AGENTS.md`, `.specify/memory/constitution.md`, `specs/005-base-model-tournament/spec.md`, `specs/005-base-model-tournament/clarification-closeout.md`, `specs/005-base-model-tournament/plan.md`, and `specs/005-base-model-tournament/contracts/preconstruction-control-contract.md` before editing implementation files.
- [ ] T002 Verify live canonical `main` and create a dedicated A1 corrective-maintenance branch from that exact head before editing `data/eval/metrics-v2.json`; do not implement A1 on `spec/005-clarify` and do not rebase/force-push.

---

## Phase 2 — US1: Additive Metrics V2 Without Breaking V1

**Story goal:** Add the minimum versioned metric/evidence-role capability needed by Spec 005 while preserving historical V1 evaluation/tournament identities.

**Independent test criterion:** V2 validates and is explicitly bound by V2 consumers; V1 metrics bytes/digest and V1 tournament behavior remain unchanged; V1↔V2 fallback/fall-forward mismatches fail closed.

> **Branch rule:** T003–T010 belong to the dedicated A1 corrective-maintenance branch/PR only.

- [ ] T003 [P] [US1] Write failing V2 catalog/role/unknown-vocabulary/canonicalization tests in `tests/eval_contract/test_metrics_v2.py`.
- [ ] T004 [P] [US1] Write failing V1/V2 tournament identity, path/SHA/version mismatch, fall-forward and fallback tests in `tests/test_tournament_metrics_v2_identity.py`.
- [ ] T005 [US1] Add the additive `commandmed-metrics-catalog` schema version `2.0` artifact with evidence-role records in `data/eval/metrics-v2.json` while leaving `data/eval/metrics.json` unchanged.
- [ ] T006 [P] [US1] Add minimal V2 model types/projections while preserving V1 parsing semantics in `src/commandmed/eval_contract/model.py` and `src/commandmed/eval_contract/canonical.py`.
- [ ] T007 [US1] Implement fail-closed V2 catalog/evidence-role validation and public exports in `src/commandmed/eval_contract/validate.py` and `src/commandmed/eval_contract/__init__.py`.
- [ ] T008 [US1] Add explicit versioned metrics identity binding to V2 tournament consumers without changing V1 behavior in `src/commandmed/tournament.py`.
- [ ] T009 [P] [US1] Document the additive V1→V2 corrective maintenance and immutable V1 guarantee in `docs/evaluation/tournament-harness.md` and `specs/001-eval-charter/corrective-maintenance-metrics-v2.md`.
- [ ] T010 [US1] Run the focused/full offline verification defined in `specs/005-base-model-tournament/quickstart.md`, prove V1 digest `304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a` remains unchanged, obtain exact-head review, merge A1, and reverify canonical `main` before T011.

### STOP GATE A1

Do **not** start T011 until A1 is merged to canonical `main` and the resulting main SHA/tree plus V2 artifact identity are reverified. Stop rather than implementing a local duplicate metric contract.

---

## Phase 3 — Foundational Spec 005 Scaffolding

**Goal:** Create the bounded standard-library package and canonical policy contracts after A1 is canonical.

- [ ] T011 [P] Create side-effect-free public package exports in `src/commandmed/spec005/__init__.py`.
- [ ] T012 [P] Create the fixture-test package marker in `tests/spec005/__init__.py`.
- [ ] T013 [P] Add seven-lane/A2/A3+A4 closed scientific-selection vocabularies and invariants to `data/spec005/selection_quality_contract.json`.
- [ ] T014 [P] Add closed A5–A13 preconstruction/governance vocabularies and invariants, with no case payload, to `data/spec005/preconstruction_contract.json`.
- [ ] T015 [P] Add the frozen five-target/context/KV/batch/memory/timing/thermal/energy/package/failure policy metadata to `data/spec005/device_qualification_contract.json`.

---

## Phase 4 — US2: Scientific Quality, Threshold and Statistical Design

**Story goal:** Make the seven-lane quality floor and A2 + atomic A3/A4 scientific evidence machine-verifiable without inventing thresholds or sample sizes.

**Independent test criterion:** All required lanes/metric roles/strata are explicit; exact threshold/margin/N/allocation records are required for PASS where applicable; missing review/evidence values block; candidate-specific/post-result changes and unpaired Arabic parity shortcuts are rejected.

- [ ] T016 [P] [US2] Write failing seven-lane quality, metric-role, threshold/margin, estimand, sample-size/allocation, paired-Arabic, dependency and post-result-mutation tests in `tests/spec005/test_science.py`.
- [ ] T017 [US2] Implement `selection_quality_contract.json` closed-shape validation and metrics-v2 evidence-role mapping in `src/commandmed/spec005/science.py`.
- [ ] T018 [US2] Implement A2 threshold/margin-policy validation with metric/estimand/direction/scope, clinical/statistical evidence, qualified-review and conflict bindings in `src/commandmed/spec005/science.py`; never default an unresolved threshold.
- [ ] T019 [US2] Implement atomic A3+A4 statistical-design/allocation validation and `evaluate_scientific_selection_readiness()` in `src/commandmed/spec005/science.py`, including candidate-neutral nuisance assumptions, paired/root-case dependency, multiplicity declaration and fail-closed missing N/allocation.

---

## Phase 5 — US3: Preconstruction Evidence and Source Governance

**Story goal:** Compute fail-closed preconstruction readiness from identity-bound A5/A6/A8/A9/A10/A11/A12 evidence without creating selection cases.

**Independent test criterion:** Synthetic valid metadata can satisfy local governance checks; missing/unknown/stale/Gold-derived/PHI/unresolved-rights/materially-mutated evidence blocks deterministically; no case text is accepted; scientific US2 readiness cannot be bypassed.

- [ ] T020 [P] [US3] Write failing contract/source-route/metadata/review/contamination/change-control/preconstruction-snapshot tests in `tests/spec005/test_preconstruction.py`.
- [ ] T021 [US3] Implement closed contract and common metadata-shape validation in `src/commandmed/spec005/preconstruction.py` using `data/spec005/preconstruction_contract.json`.
- [ ] T022 [US3] Implement A5/A6/A10 rights, privacy, exact source-route, parent-lineage, translation/derivation and prohibited-source validation in `src/commandmed/spec005/preconstruction.py`.
- [ ] T023 [US3] Implement A8/A9 metadata-only root/pair/review binding rules, including author/reviewer separation and no embedded clinical/Gold payload, in `src/commandmed/spec005/preconstruction.py`.
- [ ] T024 [US3] Implement A11 contamination-plan identity readiness and A12 material-change/new-identity rules without executing contamination scans in `src/commandmed/spec005/preconstruction.py`.
- [ ] T025 [US3] Implement dependency/staleness-aware `evaluate_preconstruction_snapshot()` in `src/commandmed/spec005/preconstruction.py`, requiring US2 scientific readiness and outputting only `NOT_READY_TO_CONSTRUCT` or `READY_FOR_SEPARATE_ACTIVATION_NOT_AUTHORIZED` before a real A15 record.

---

## Phase 6 — US4: Personnel Governance

**Story goal:** Validate opaque personnel qualification, Gold/result exposure, independence, assignment and A7 handshake records without storing credentials or assigning real people.

**Independent test criterion:** Eligibility is role/scope-specific; self-verification, unresolved conflicts, incompatible Gold/result exposure, stale evidence and independence collisions fail closed; assignment never auto-grants access.

- [ ] T026 [P] [US4] Write failing identity/eligibility/conflict/Gold-exposure/assignment/independence/transition/bootstrap-handshake tests in `tests/spec005/test_personnel.py`.
- [ ] T027 [US4] Implement opaque identity, qualification-evidence, conflict and Gold-exposure record validation/state evaluation in `src/commandmed/spec005/personnel.py`.
- [ ] T028 [US4] Implement role-scoped eligibility plus `PROPOSED/ACTIVE/SUSPENDED/REVOKED/EXPIRED` assignment validation and independence collision checks in `src/commandmed/spec005/personnel.py`.
- [ ] T029 [US4] Implement stale-evidence propagation, same-suite result-exposure restrictions, bootstrap/steady-state readiness and A7 handshake signals in `src/commandmed/spec005/personnel.py`.

---

## Phase 7 — US5: Payload and Candidate-Result Access Firewall

**Story goal:** Validate A13 access metadata and the one-way result firewall without provisioning storage or granting real access.

**Independent test criterion:** Default deny; Zone 1/2/3 and Private-Gold boundaries remain separate; A7 deny/revoke/stale signals override grants; active content roles cannot receive same-suite result access and result-exposed actors cannot silently return to result-blind content roles.

- [ ] T030 [P] [US5] Write failing zone/default-deny/grant/revoke/result-firewall/export/audit-record tests in `tests/spec005/test_access.py`.
- [ ] T031 [US5] Implement the three-zone metadata policy, resource-zone validation and default-deny semantics in `src/commandmed/spec005/access.py`.
- [ ] T032 [US5] Implement A7→A13 grant-consideration/deny/revoke/revalidation handshake, result-role incompatibilities, export restrictions and append-only audit-record validation in `src/commandmed/spec005/access.py`.

---

## Phase 8 — US6: Spend and Engagement Governance

**Story goal:** Compute A14 requirement/authorization readiness without selecting vendors, creating contracts, accessing payment instruments or spending money.

**Independent test criterion:** `$0`, silence, free tiers and assumed volunteers do not establish PASS; required workload gaps are explicit; self-approval/conflicted approval fails; only current `ACTIVE` authorizations cover prospective commitments; material changes require new identities; stale upstream evidence invalidates PASS.

- [ ] T033 [P] [US6] Write failing workload/capacity/requirement, approval-conflict, lifecycle, material-amendment, pass-mode and staleness tests in `tests/spec005/test_finance.py`.
- [ ] T034 [US6] Implement A14 workload/resource manifest validation and `NOT_REQUIRED/REQUIRED/BLOCKED_UNKNOWN_OR_INCOMPLETE` requirement evaluation in `src/commandmed/spec005/finance.py`.
- [ ] T035 [US6] Implement authorization identity, segregation-of-financial-duties, payee/vendor conflict and lifecycle transition validation in `src/commandmed/spec005/finance.py`.
- [ ] T036 [US6] Implement `A14_NOT_REQUIRED_PASS` / `A14_AUTHORIZED_PASS` evidence evaluation with cap/period/scope/state coverage and staleness/revalidation in `src/commandmed/spec005/finance.py`.

---

## Phase 9 — US7: Construction Activation, Device Protocol and Tournament Manifest

**Story goal:** Validate frozen device/runtime metadata and exact A15/Spec 005 manifest prerequisites without performing construction, model, benchmark or device execution.

**Independent test criterion:** Device metadata validation reflects the frozen protocol; synthetic activation fixtures require complete exact prerequisite identities including US2 scientific records; missing/stale/unauthorized evidence prevents a Spec 004 projection; complete synthetic fixtures prove validator compatibility without creating real authority.

- [ ] T037 [P] [US7] Write failing five-target/context/KV/batch/run-count/memory/timing/thermal/energy/package/runtime-identity/failure-semantics tests in `tests/spec005/test_device.py`.
- [ ] T038 [US7] Implement metadata-only device qualification contract/evidence validation and fail-closed preflight in `src/commandmed/spec005/device.py` using `data/spec005/device_qualification_contract.json`.
- [ ] T039 [P] [US7] Write failing A15 prerequisite-snapshot, scientific-record, stale/mismatched gate, bounded-scope and synthetic-authority tests in `tests/spec005/test_activation.py`.
- [ ] T040 [US7] Implement immutable A15 activation-record validation/readiness without creating a canonical activation or external side effect in `src/commandmed/spec005/activation.py`.
- [ ] T041 [P] [US7] Write failing Spec 005 manifest/admission/metrics-v2/seven-lane/scientific-design/device/activation/Private-Gold/no-projection tests in `tests/spec005/test_manifest.py`.
- [ ] T042 [US7] Implement Spec 005 manifest validation/preflight and the fail-closed Spec 004-compatible projection adapter in `src/commandmed/spec005/manifest.py`.
- [ ] T043 [US7] Document the implemented scientific/preconstruction control plane, inherited Spec 002/003/004 boundaries and explicit non-execution scope in `docs/evaluation/base-model-tournament.md`.

---

## Phase 10 — Polish, Regression and Review Readiness

**Goal:** Prove the code is deterministic, bounded and ready for independent implementation review; do not perform live tournament execution.

- [ ] T044 [P] Run Python syntax compilation for `src/commandmed/spec005/`, `src/commandmed/eval_contract/`, `tests/spec005/`, and A1 tests using `specs/005-base-model-tournament/quickstart.md`.
- [ ] T045 [P] Run the complete focused Spec 005 fixture suite under `tests/spec005/` and repair only in-scope failures without weakening requirements.
- [ ] T046 Run the full offline repository `unittest` suite from `tests/` and preserve all Specs 001–004 regression identities/behavior.
- [ ] T047 Audit `src/commandmed/spec005/`, `data/spec005/`, and `tests/spec005/` for network/provider/model/device/payment/storage side effects, prohibited payload fields and unapproved third-party dependencies; remove any such mechanism rather than testing it live.
- [ ] T048 Reconcile implemented paths and validation commands with `specs/005-base-model-tournament/plan.md`, `specs/005-base-model-tournament/data-model.md`, `specs/005-base-model-tournament/contracts/preconstruction-control-contract.md`, and `specs/005-base-model-tournament/quickstart.md` without expanding scope.
- [ ] T049 Obtain fresh independent review on the exact implementation head and append only actual local/CI/review evidence to an `Implementation Evidence` section in `docs/evaluation/base-model-tournament.md`; do not claim CI PASS if no Actions run exists and do not mark Ready/merge until the governed Spec 005 implementation exit gate is separately satisfied.

---

## Dependencies

```text
T001 -> T002
T002 -> T003..T010
T010 (A1 merged + main reverified) -> T011..T015
T011..T015 -> US2..US7
US2 -> US3
US3 -> US4
US4 -> US5
US2 + US3 + US4 -> US6
US2 + US3 + US4 + US5 + US6 + device contract -> US7
US1..US7 -> T044..T049
```

A15 real construction activation is **not** a dependency JetBrains should satisfy itself; JetBrains only implements its validator. A real activation requires separate founder authorization after real prerequisite PASS evidence exists.

## Parallel Opportunities

- T003 and T004 can proceed in parallel.
- T006 and T009 can proceed in parallel after the V2 shape is stable.
- T011–T015 can proceed in parallel after A1 canonical merge.
- Test authoring for US2–US7 can proceed in parallel where files do not overlap.
- Device tests/implementation can proceed in parallel with personnel/finance because they meet only at final snapshot/manifest integration.

## Implementation Strategy

### MVP build target

The first independently valuable implementation increment is **US1 + US2 + US3**:

1. additive metrics-v2 with V1 preservation;
2. explicit scientific quality/threshold/statistical design validation;
3. deterministic preconstruction/source/provenance/change-control validation.

This yields a complete machine-verifiable scientific + governance readiness layer without touching real model/data execution.

### Incremental delivery

1. Land A1 independently.
2. Land foundational Spec 005 contracts.
3. Add scientific selection validation.
4. Add preconstruction source/provenance governance.
5. Add personnel + access.
6. Add finance.
7. Add device/activation/manifest integration.
8. Run full regression and exact-head review.

Do not combine later execution (case construction, model/benchmark/device runs, spending) into these tasks merely because validators exist.

## Task summary

```text
TOTAL_TASKS=49
SETUP=2
US1=8
FOUNDATIONAL=5
US2=4
US3=6
US4=4
US5=3
US6=4
US7=7
POLISH=6
```

All tasks use the required Spec Kit checkbox + ID + optional `[P]` + story-label format and name concrete repository paths.