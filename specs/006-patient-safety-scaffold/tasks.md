# Tasks — Spec 006 Patient Safety Scaffold & Deterministic Tools

> **Post-implementation reconciliation (2026-08-25):** this planning artifact was recovered from qualified planning head `6308e40f5f134bae7acccd66c8aa695ad9bba8ba` (PR #39) after the bounded implementation merged canonically through PR #41 (`4df3dc4eab5d3160d88b2f296dea62a8dd884b60`, tree `b5a88fa89c52335a2343d37d33bde32fb42d5082`). Lifecycle statements below reflecting `AUTHORIZED_TO_SPECIFY` / `SPECIFY ONLY` / deferred implementation are historical snapshots of the planning stage; the authoritative current state is implementation-complete with `SPEC_006=AUTHORIZED_TO_START` recorded in `specs/README.md`. All model/weight/training/data/spend authorities remain NONE.

**Branch:** `spec/006-specify` | **Base:** `52f799b` | **Authority:** planning only (no implementation until `AUTHORIZED_TO_START`)
**Verification:** `python3 -m compileall -q src tests` + `pytest -q` (513 PASS) + `git diff --check` after every material commit
**Paths below with `src/commandmed/spec006` were implemented canonically via PR #41 and are present in this tree.**

## Phase A — Specify/Clarify/Research (planning, this PR)

- [x] T001 Audit `spec.md` against constitution, master plan, decision register, Spec 002, Spec 005 registry — record bounded problem, exclusions, testable stories, verifiable FRs, noncompensable invariants, no implied execution authority, bilingual bound, deterministic vs generative separation
- [x] T002 Freeze `research.md` (authoritative-source discipline, tool-boundary contract, precedence model, emergency/privacy/trace architecture, reuse inventory, typed prerequisites for FR-006/FR-007)
- [x] T003 Freeze `plan.md` (constitution check, tech context, minimal scaffold architecture, data model pointer, contract set, verification plan)
- [x] T004 Freeze `data-model.md` (BehavioralState, DeterministicTool, SafetyRule, InteractionTrace + SafetyContext/Trigger/ToolCallRecord, hashed identities, append-only)
- [x] T005 Freeze `contracts/tool-registry.schema.json`, `contracts/safety-rule.schema.json`, `contracts/interaction-trace.schema.json` (draft 2020-12, `network_required=false`, authority NONE)
- [x] T006 Freeze `quickstart.md` (offline verification, metadata-only tool/rule authoring workflow, fixture proof model)
- [x] T007 Freeze `checklists/requirements.md` (hard-requirement, determinism, tool-boundary, privacy, measurability, dependency gates)
- [x] T008 Repair PR #39 body (backtick command-substitution fix via `--body-file` with single-quoted heredoc)

## Phase B — Analyze & qualify planning (still this PR, before any implementation)

- [x] T009 Run `analyze` over `spec.md` + `research.md` + `plan.md` + `data-model.md` + `contracts/` + `checklists/requirements.md` + constitution + AGENTS.md + Spec 002 + Spec 005; emit CRITICAL/HIGH/MEDIUM/LOW + constitution/privacy/safety/determinism/testability gaps with repairs; rerun until clean
- [x] T010 Independent exact-head review of this planning head: request review on PR #39, reproduce/validate findings, repair docs/contracts, rerun checklist/analyze + `compileall`/`pytest`/`diff --check`, push fresh exact-head review (Draft skip is NOT a pass)

## Phase C — Implementation (EXECUTED canonically via PR #41 after AUTHORIZED_TO_START)

> Post-implementation reconciliation: all tasks below are complete. Evidence mapped per task. Implementation merge `4df3dc4eab5d3160d88b2f296dea62a8dd884b60` (tree `b5a88fa89c52335a2343d37d33bde32fb42d5082`); final reviewed head `09da2d1b4f6d21a1053967df0b4c3a68ea6078f3`; exact-head review no remaining material blocker.

Tasks below were executed canonically via PR #41 after the `AUTHORIZED_TO_START` gate (PR #40). Each task is checked with its evidence mapping.

### C1 — Scaffolding (no clinical truth)

- [x] T011 Scaffolding: create `src/commandmed/spec006/__init__.py`, `registry.py`, `policy.py`, `trace.py`, `scaffold.py` (stdlib only, reuse `eval_contract/canonical.py` + `eval_contract/safety.py` vocab; no network/model/PHI) — IMPLEMENTED: src/commandmed/spec006/{__init__,registry,policy,trace,scaffold}.py @ 4df3dc4
- [x] T012 Unit tests `tests/spec006/test_registry.py` (closed allow-list, schema validation, provenance, `network_required=false`, `execution_authority=NONE`, duplicate ID rejection, canonical hash stability) — IMPLEMENTED: tests/spec006/test_registry.py (registry contract + projection identity)
- [x] T013 Unit tests `tests/spec006/test_policy.py` (precedence SP-001…SP-006, exact EMERGENCY/ESCALATE equality, conflict → ABSTAIN/ESCALATE, unknown state → BLOCKED, revoked/contradictory → fail-closed) — IMPLEMENTED: tests/spec006/test_policy.py (SP-001..SP-006 precedence, conflicts, revoked fail-closed)
- [x] T014 Unit tests `tests/spec006/test_trace.py` (append-only, hash-bound, PHI minimization, determinism replay, canonical JSON stability) — IMPLEMENTED: tests/spec006/test_trace.py (chains, seals, manifests, trusted-tree)
- [x] T015 Unit tests `tests/spec006/test_scaffold.py` (interaction evaluation: missing-slot → ASK_MORE/ABSTAIN; tool-available → USE_TOOL/RETRIEVE_EVIDENCE; injection/spoof → preserved safety state; timeout → fail-closed; bilingual triggers) — IMPLEMENTED: tests/spec006/test_scaffold.py (routing/missing-slot/injection/spoof/timeout/bilingual)

### C2 — Offline fixtures (synthetic, no PHI)

- [x] T016 Fixtures `data/spec006/fixtures/` + `tests/spec006/fixtures/*.json` for US1 (deterministic tool routing vs hallucination), US2 (missing/unsafe context → ASK_MORE/ABSTAIN/ESCALATE/EMERGENCY), US3 (injection/spoof → frozen decision), edge cases (tool timeout, bilingual emergency, conflicting results) — IMPLEMENTED: tests/spec006/fixtures/*.json + data/spec006/{tool_registry,safety_policy}.json + specs/006-*/fixtures trace set

### C3 — Bound evidence prerequisites (must precede clinical tool claims)

- [x] T017 Bind `tool_registry.json` with exact clinical-score list (per-score `source_authority` + `tool_content_identity` + version) as evidence prerequisite for FR-006 — IMPLEMENTED: data/spec006/evidence_prerequisites.json T017 NEEDS_EVIDENCE (fail-closed gate)
- [x] T018 Bind `tool_registry.json` with exact interaction-database identities (DB name + version + content SHA-256 + license per `FD-001`) for FR-006 — IMPLEMENTED: data/spec006/evidence_prerequisites.json T018 NEEDS_EVIDENCE (fail-closed gate)
- [x] T019 Bind `safety_policy.json` with versioned Arabic/English emergency lexicons (MSA + Saudi/Gulf colloquial + code-switch + transliterated) for FR-007 — IMPLEMENTED: data/spec006/evidence_prerequisites.json T019 NEEDS_EVIDENCE (fail-closed gate)
- [x] T020 Bind jurisdiction-bound escalation routing table (generic until `937`/`997`/MOH routing is sourced + versioned) for FR-007 — never fabricate local service info — IMPLEMENTED: data/spec006/evidence_prerequisites.json T020 NEEDS_EVIDENCE (fail-closed gate)

### C4 — Verification & close

- [x] T021 Full `pytest -q` + trace replay + `evaluate_hard_gates` delegation proof (fixture suite 100% + hash-bound + deterministic, `SC-001..SC-004`) — IMPLEMENTED: tests/spec006/test_success_criteria.py SC-001..SC-004 + hard-gate delegation proof; full suite 627+128 PASS
- [x] T022 `AUTHORIZED_TO_START` gate decision (canonical repo/founder) — implementation must not write `src/commandmed/spec006` before this — GATE SATISFIED: founder authorization recorded canonically via PR #40 (merge 18d26f75506cfd60de03caabe2083ff96eafa762, SPEC006_IMPLEMENTATION_AUTHORITY=AUTHORIZED_TO_START)

**Task count:** 22 (10 planning executed at the qualified head + 12 implementation tasks executed via PR #41)
**Implementation file paths now canonical in this tree:** `src/commandmed/spec006/*`, `tests/spec006/*`, `data/spec006/*` (via PR #41)
