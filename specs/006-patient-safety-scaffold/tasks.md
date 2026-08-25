# Tasks — Spec 006 Patient Safety Scaffold & Deterministic Tools

**Branch:** `spec/006-specify` | **Base:** `52f799b` | **Authority:** planning only (no implementation until `AUTHORIZED_TO_START`)
**Verification:** `python3 -m compileall -q src tests` + `pytest -q` (513 PASS) + `git diff --check` after every material commit
**Paths below with `src/commandmed/spec006` are intended implementation targets referenced by planning docs only — do NOT create them in this planning PR.**

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

## Phase C — Implementation (deferred, requires SEPARATE `AUTHORIZED_TO_START`)

Tasks below are **planned, not executed** in this PR. They are dependency-ordered, small, fixture-first, TDD-friendly.

### C1 — Scaffolding (no clinical truth)

- [ ] T011 Scaffolding: create `src/commandmed/spec006/__init__.py`, `registry.py`, `policy.py`, `trace.py`, `scaffold.py` (stdlib only, reuse `eval_contract/canonical.py` + `eval_contract/safety.py` vocab; no network/model/PHI)
- [ ] T012 Unit tests `tests/spec006/test_registry.py` (closed allow-list, schema validation, provenance, `network_required=false`, `execution_authority=NONE`, duplicate ID rejection, canonical hash stability)
- [ ] T013 Unit tests `tests/spec006/test_policy.py` (precedence SP-001…SP-006, exact EMERGENCY/ESCALATE equality, conflict → ABSTAIN/ESCALATE, unknown state → BLOCKED, revoked/contradictory → fail-closed)
- [ ] T014 Unit tests `tests/spec006/test_trace.py` (append-only, hash-bound, PHI minimization, determinism replay, canonical JSON stability)
- [ ] T015 Unit tests `tests/spec006/test_scaffold.py` (interaction evaluation: missing-slot → ASK_MORE/ABSTAIN; tool-available → USE_TOOL/RETRIEVE_EVIDENCE; injection/spoof → preserved safety state; timeout → fail-closed; bilingual triggers)

### C2 — Offline fixtures (synthetic, no PHI)

- [ ] T016 Fixtures `data/spec006/fixtures/` + `tests/spec006/fixtures/*.json` for US1 (deterministic tool routing vs hallucination), US2 (missing/unsafe context → ASK_MORE/ABSTAIN/ESCALATE/EMERGENCY), US3 (injection/spoof → frozen decision), edge cases (tool timeout, bilingual emergency, conflicting results)

### C3 — Bound evidence prerequisites (must precede clinical tool claims)

- [ ] T017 Bind `tool_registry.json` with exact clinical-score list (per-score `source_authority` + `tool_content_identity` + version) as evidence prerequisite for FR-006
- [ ] T018 Bind `tool_registry.json` with exact interaction-database identities (DB name + version + content SHA-256 + license per `FD-001`) for FR-006
- [ ] T019 Bind `safety_policy.json` with versioned Arabic/English emergency lexicons (MSA + Saudi/Gulf colloquial + code-switch + transliterated) for FR-007
- [ ] T020 Bind jurisdiction-bound escalation routing table (generic until `937`/`997`/MOH routing is sourced + versioned) for FR-007 — never fabricate local service info

### C4 — Verification & close

- [ ] T021 Full `pytest -q` + trace replay + `evaluate_hard_gates` delegation proof (fixture suite 100% + hash-bound + deterministic, `SC-001..SC-004`)
- [ ] T022 `AUTHORIZED_TO_START` gate decision (canonical repo/founder) — implementation must not write `src/commandmed/spec006` before this

**Task count:** 22 (10 planning executed + 12 deferred implementation prerequisites)
**Implementation file paths referenced but not created in planning PR:** `src/commandmed/spec006/*`, `tests/spec006/*`, `data/spec006/*`
