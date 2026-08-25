# Analyze — Spec 006 Patient Safety Scaffold

**Analyzed head:** planning PR #39 (base `52f799b`)
**Artifacts:** `spec.md`, `research.md`, `plan.md`, `data-model.md`, `contracts/*.schema.json`, `quickstart.md`, `checklists/requirements.md`, `tasks.md` + constitution + AGENTS.md + Spec 002 `CLOSED_CANONICAL` + Spec 005 `CLOSED_CANONICAL`
**Authority:** planning only

## Verdict

```
CRITICAL=0
HIGH=0
MEDIUM=0
LOW=2
CONSTITUTION_VIOLATIONS=0
MATERIAL_COVERAGE_GAPS=0
AMBIGUITIES=0
DUPLICATE_ARCHITECTURE=0
OVERDESIGN=0
UNAUTHORIZED_EXECUTION_SURFACE=0
PRIVACY_GAPS=0
SAFETY_GAPS=0
DETERMINISM_GAPS=0
TESTABILITY_GAPS=0
RESULT=PASS (planning)
```

## Checks

- Constitution I/VII/XI: scaffold provides frozen fixture protocol + deterministic boundary + defense-in-depth before any SFT — satisfied without amendment.
- Spec 002: states SP-001…SP-006, TASK_CLASSES, BEHAVIOR_STATES, threshold governance, and `evaluate_hard_gates` delegation preserved; no redefinition, no second aggregator. Tool classes in `research.md` map 1:1 to Spec 002 `TASK_CLASS`.
- Spec 005: `canonical_json_dumps`/`compute_canonical_sha256`, fail-closed validator patterns, identity/hash conventions, lifecycle `AUTHORIZED_TO_START` gate reused. V1 metric catalog SHA `304c980c…` untouched.
- FR-001…FR-005: bounded, verifiable via offline fixtures (`SC-001..SC-004`); FR-006/FR-007 remain as typed `NEEDS_EVIDENCE` prerequisites, not fabrications — tracked in `tasks.md` T017…T020 and `checklists/requirements.md`.
- FR-006/FR-007 clarification: deterministic tool categories/schemas, version/identity, input/output schemas, failure semantics, Arabic/English emergency handling, lexical vs semantic trigger boundary, escalation routing/locale boundary, state precedence (single terminal state, allowed/forbidden transitions), timeout/conflict/provenance/spoof/canonicalization/append-only/privacy/role distinction/evidence-retrieval/unit-conversion/dosage/score boundaries, network prohibition — all resolved from repository truth in `research.md` §5–§9 or recorded as typed `NEEDS_EVIDENCE` (not invented).
- Emergency design rule: frozen deterministic policy authoritative, lexicon as signal, generative text cannot lower state, ambiguous high-risk escalates, no fabricated locale service info — satisfied (`research.md` §6, `data-model.md` `SafetyContext`).
- Deterministic tool boundary: minimal registry contract with `TOOL_ID/VERSION/CONTENT_IDENTITY/CLASS/INPUT_SCHEMA/OUTPUT_SCHEMA/SOURCE_AUTHORITY/FAILURE_SEMANTICS/APPLICABLE_WHEN/PROHIBITED_WHEN/FRESHNESS_POLICY/RESULT_PROVENANCE_REQUIRED/NETWORK_REQUIRED/EXECUTION_AUTHORITY` — no plugin framework, Ponytail-compliant.
- Trace/audit: privacy-safe minimum fields (hashes + reason codes + determinism proof), no raw PHI, append-only — satisfied (`research.md` §7, `data-model.md` §1.4).
- Plan: repeats must check thresholds via existing mechanisms (not invent do it again).
- Checklist: all hard requirements, deterministic/safety/privacy/measurability/dependency gates pass or typed prerequisite.
- Tasks: small, dependency-ordered, fixture-first, explicit file paths, authority boundaries, tests before/with implementation; planning vs deferred implementation cleanly split per instruction.

## Low findings (informational, not blocking)

- L01 — Real unit/dosage arithmetic coverage is best proven by fixtures once implementation exists; planning validators cannot alone prove arithmetic correctness — mitigated by deferred T015/T016 fixture-first tasks.
- L02 — External authoritative source versions (e.g., which interaction DB) will require founder/license selection before `AUTHORIZED_TO_START`; planning correctly leaves them as evidence prerequisites rather than fabricating — no action now.

## No critical/high contradiction remains.

Repair loop not required. Next gate remains `SPEC006_IMPLEMENTATION_AUTHORITY=AUTHORIZED_TO_START` (separate canonical authorization).
