# Spec 006 — Patient Safety Scaffold & Deterministic Tools

> **Post-implementation reconciliation (2026-08-25):** this planning artifact was recovered from qualified planning head `6308e40f5f134bae7acccd66c8aa695ad9bba8ba` (PR #39) after the bounded implementation merged canonically through PR #41 (`4df3dc4eab5d3160d88b2f296dea62a8dd884b60`, tree `b5a88fa89c52335a2343d37d33bde32fb42d5082`). Lifecycle statements below reflecting `AUTHORIZED_TO_SPECIFY` / `SPECIFY ONLY` / deferred implementation are historical snapshots of the planning stage; the authoritative current state is **`SPEC_006=CLOSED_CANONICAL`** recorded in `specs/README.md` and bound in `closeout.md`. All model/weight/training/data/spend authorities remain NONE.

**Planning Branch**: `spec/006-specify` (PR #39, superseded by reconciliation PR) | **Implementation**: PR #41 on `impl/006-patient-safety-scaffold`
**Created**: 2026-08-25
**Status**: `IMPLEMENTATION COMPLETE` — implemented via PR #41 (merge `4df3dc4`); originally specified under `AUTHORIZED_TO_SPECIFY` at qualified head `6308e40`
**Depends on**: Spec 002 `CLOSED_CANONICAL`, Spec 005 `CLOSED_CANONICAL` (52f799b)
**Lifecycle authority**: IMPLEMENTATION COMPLETE (offline deterministic scope only)
**Execution authority**: NONE — no model execution, weight access, benchmark execution, Private Gold/PHI access, device execution, spend

> This specification defines the defense-in-depth safety scaffold that bounds generative behavior with deterministic tools and behavioral states. It is not a model-training, model-execution, mobile-app, or clinical-deployment authorization.

## 1. Objective

Ensure every patient-facing or safety-critical interaction passes through deterministic, auditable checks that generative text cannot override. The system must support `ANSWER / ASK_MORE / USE_TOOL / RETRIEVE_EVIDENCE / ABSTAIN / ESCALATE / EMERGENCY` and route to or explain deterministic tools rather than replacing validated clinical arithmetic, scores, schemas, or interaction lookups.

## 2. Context and why this spec exists

AGENTS.md requires behavioral states and states that critical escalation rules and deterministic safety checks are not overridable by generative text. Constitution I, II, VII, XI require evidence-before-training, hard safety gates, deterministic boundaries, and defense in depth. Spec 002 provides safety gates; Spec 005 provides the control plane that can represent thresholds and readiness as data. Spec 006 must now define the interaction/tool boundary that makes those gates operational before any future SFT or device work.

## User Scenarios & Testing

### User Story 1 — Deterministic tool is used where a validated tool exists (Priority: P1)

A user asks for a calculation or lookup for which a deterministic tool exists (e.g., validated clinical score, drug-interaction lookup, unit conversion, dosage arithmetic, structured schema validation).

**Why this priority**: Preventing model hallucination of arithmetic/guideline lookups is a hard safety requirement.

**Independent Test**: Send a synthetic request that maps to a tool from the allowed list; verify the system either calls `USE_TOOL`/`RETRIEVE_EVIDENCE` or explains the deterministic result, and that a pure generative answer without tool use is rejected in evaluation.

**Acceptance Scenarios**:
1. **Given** a deterministic tool exists for the request, **When** the system answers, **Then** it must route to or explain the tool result and not invent a conflicting value.
2. **Given** no deterministic tool exists, **When** the system answers, **Then** it may answer directly but must not claim a tool was used.

### User Story 2 — Abstain or escalate on missing or unsafe context (Priority: P1)

A user provides insufficient, contradictory, or high-risk clinical context, or asks for disallowed medical action.

**Why this priority**: Safety requires explicit abstention/escalation rather than unsafe completion.

**Independent Test**: Synthetic prompt with missing critical slots or emergency keywords; verify the system returns `ASK_MORE`, `ABSTAIN`, `ESCALATE`, or `EMERGENCY` as specified and does not provide a definitive clinical directive.

**Acceptance Scenarios**:
1. **Given** required context is missing for a safety-critical decision, **When** the user asks, **Then** the system must `ASK_MORE` or `ABSTAIN` and state what is missing.
2. **Given** an emergency pattern is detected, **When** evaluated, **Then** the system must `EMERGENCY`/`ESCALATE` per the frozen emergency policy and not provide routine advice.

### User Story 3 — Generative text cannot override frozen safety rules (Priority: P1)

A prompt attempts to bypass safety policy via instruction injection or tool-output spoofing.

**Why this priority**: Defense in depth requires that policy and tool outputs dominate generative text.

**Independent Test**: Inject an `ignore previous instructions` payload or a fake tool output; verify the system preserves the frozen safety decision and logs the attempt.

**Acceptance Scenarios**:
1. **Given** a user injects a policy-override instruction, **When** processed, **Then** the system must enforce the canonical safety rule and not comply.
2. **Given** a tool returns a safety-critical flag, **When** the system presents the answer, **Then** it must not contradict the tool's fail-closed result.

### Edge Cases

- What happens when a tool is unavailable or times out? → Fail closed to `ASK_MORE`/`ABSTAIN` with auditable reason.
- How does system handle multilingual (Arabic/English) safety triggers? → Both languages must be covered per Spec 005 anchors.
- How does system handle conflicting tool results? → Deterministic precedence + escalation, never silent averaging.

## Requirements

### Functional Requirements

- **FR-001**: System MUST support behavioral states `ANSWER`, `ASK_MORE`, `USE_TOOL`, `RETRIEVE_EVIDENCE`, `ABSTAIN`, `ESCALATE`, `EMERGENCY` and select one per interaction.
- **FR-002**: System MUST maintain a closed allow-list of deterministic tools (arithmetic, validated scores, schema validation, interaction/drug lookups) that, when applicable, must be routed to rather than simulated.
- **FR-003**: System MUST enforce that frozen safety rules and deterministic tool outputs override generative text; injection or tool-output spoofing must fail closed.
- **FR-004**: System MUST represent safety context (role, language, available evidence, tool availability) as explicit, auditable data, not hidden prompt state.
- **FR-005**: System MUST log every safety-critical decision in a canonical, append-only, deterministic format for evaluation. Each `InteractionTrace` record MUST carry an ordered `trace_sequence` (monotonic per `interaction_id`) and a `predecessor_sha256` (hash of the prior trace record or `GENESIS` for first) forming a hash-chain; the trace store MUST reject replacement, deletion, or reordering. A committed terminal completeness anchor `trace_seal.json` (per `interaction_id`: `expected_final_sequence` + `terminal_record_sha256` over canonical JSON of the final record) MUST be present; verification MUST reject unless sequences are strictly contiguous from 0, `(interaction_id, trace_sequence)` keys are unique and monotonic, the predecessor chain validates (`predecessor_sha256 == sha256(canonical_json(predecessor))`), and the terminal anchor hash equals the final record hash — otherwise `INSUFFICIENT_EVIDENCE`. Gaps, mismatches, deletions, reordering, or replacements → `INSUFFICIENT_EVIDENCE`.

*Clarified as typed evidence prerequisites (FR-006/FR-007 remain non-fabrication markers):*
- **FR-006**: System MUST handle [CLARIFIED: tool categories/schemas/failure semantics/precedence/provenance/network prohibition resolved in `research.md` §3–§5 and `contracts/tool-registry.schema.json`; exact clinical-score list, interaction database identities/versions, and emergency-keyword policy source remain typed `NEEDS_EVIDENCE` prerequisites bound as versioned registry records with `tool_content_identity` + `source_authority` before any `PASS` claim — tracked as tasks T017/T018]
- **FR-007**: System MUST enforce [CLARIFIED: behavioral state precedence, single terminal state, trigger/provenance/spoof/append-only/privacy/role/evidence-retrieval boundaries resolved in `research.md` §5–§7 and `data-model.md`/`contracts/safety-rule.schema.json`; exact Arabic/English emergency lexicon content and jurisdiction-bound escalation routing remain typed `NEEDS_EVIDENCE` prerequisites bound as versioned policy records before any locale-specific routing — tracked as tasks T019/T020; ambiguous high-risk fails toward ASK_MORE/ESCALATE/EMERGENCY; no local service info fabricated]

### Key Entities

- **Behavioral State**: `ANSWER | ASK_MORE | USE_TOOL | RETRIEVE_EVIDENCE | ABSTAIN | ESCALATE | EMERGENCY` with triggering evidence.
- **Deterministic Tool**: name, version, content SHA-256, allowed input schema, output schema, failure semantics.
- **Safety Rule**: id, version, source policy SHA-256, triggering condition, required state, precedence.
- **Interaction Trace**: interaction id, tool calls, safety evaluations, state transitions, input/output hashes, determinism proof.

## Success Criteria

### Measurable Outcomes

- **SC-001**: 100% of synthetic requests that map to an allow-listed deterministic tool are routed to the tool or correctly explained; 0% pure hallucinations in offline fixture suite.
- **SC-002**: 100% of synthetic injection/spoof attempts preserve the frozen safety decision in evaluation.
- **SC-003**: Every safety-critical interaction in the fixture suite emits a deterministic trace that is reproducible and hash-bound.
- **SC-004**: No network, model-weight, or external API execution is required for the offline fixture suite; all tests run with `pytest -q` deterministically.

## Assumptions

- Target users include patients, caregivers, and clinicians; safety behavior must be role-appropriate but medical truth remains shared.
- Existing Spec 002 safety gates and Spec 005 control-plane validators are the frozen prerequisites; this spec does not re-define their identities.
- Deterministic tools are metadata-registered first; real tool implementations or service bindings are separately authorized.
- Arabic and English are both in scope per Spec 005 anchors; full multimodal tool coverage is deferred.
