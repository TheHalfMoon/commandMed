# Requirements Checklist — Spec 006 Patient Safety Scaffold

**Branch:** `spec/006-specify` | **Base:** `52f799b` | **Authority:** planning only

Legend: `[x]` pass, `[ ]` fail/blocked, `[~]` partial/needs evidence (typed prerequisite, not silent pass)

## Hard requirements

- [x] FR-001 behavioral states `ANSWER|ASK_MORE|USE_TOOL|RETRIEVE_EVIDENCE|ABSTAIN|ESCALATE|EMERGENCY` with exactly one terminal state — modelled in `data-model.md` + schemas + `research.md` §5
- [x] FR-002 closed deterministic tool allow-list (`REQUIRED_DETERMINISTIC`/`REQUIRED_AUTHORITATIVE` boundary) — `contracts/tool-registry.schema.json` + `research.md` §3/§4
- [x] FR-003 frozen policy + deterministic output overrides generative text; injection/spoof fail-closed — `research.md` §5/§6 + `contracts/safety-rule.schema.json` + provider/reason codes; modeled as `INJECTION_ATTEMPT_SUPPRESSED`, `SPOOFED_TOOL_RESULT_REJECTED`
- [x] FR-004 auditable safety context (role, language, evidence, availability) as explicit data — `data-model.md` `SafetyContext`; not hidden prompt state
- [x] FR-005 canonical append-only deterministic trace (state, triggers, tool calls, hashes) — `contracts/interaction-trace.schema.json` + `data-model.md` §1.4
- [~] FR-006 exact clinical-score list, interaction DB identities, emergency-keyword policy source — typed evidence prerequisites per `research.md` §9; checklist records as `NEEDS_EVIDENCE`, not fabricated
- [~] FR-007 exact Arabic/English emergency lexicon + escalation routing — typed evidence prerequisites per `research.md` §9; jurisdiction-bound routing sourced before any locale-specific service info is emitted
- [x] No ambiguity remains in hard requirements that can be resolved from existing canonical governance — all resolvable items frozen; remainder typed as prerequisites with explicit evidence kind

## Determinism & safety

- [x] Precedence order derived from Spec 002 SP-001…SP-006, not invented clinical severity ranking (`research.md` §5)
- [x] Conflicting equal-precedence triggers → fail-closed `ABSTAIN/ESCALATE` + `CONFLICTING_SAFETY_OUTCOMES`
- [x] Generative text cannot lower deterministic safety state
- [x] Tool unavailable/timeout → fail-closed `ASK_MORE`/`ABSTAIN`/`ESCALATE` with auditable reason
- [x] Spoofed tool result rejected via provenance (`tool_content_identity` mismatch → `SPOOFED_TOOL_RESULT_REJECTED`)
- [x] Injection payload does not override frozen policy (`INJECTION_ATTEMPT_SUPPRESSED`)
- [x] Emergency not reduced to fragile single-keyword list; lexicon is versioned signal + frozen policy remains authoritative; ambiguous high-risk → `ASK_MORE`/`ESCALATE`/`EMERGENCY` per policy
- [x] Locale-specific emergency info never fabricated; generic escalation until jurisdiction-bound source/version

## Tool boundary

- [x] Minimal Ponytail registry (typed record, no framework/services/queues)
- [x] Every registry entry has `TOOL_ID, TOOL_VERSION, TOOL_CONTENT_IDENTITY, TOOL_CLASS, INPUT_SCHEMA, OUTPUT_SCHEMA, SOURCE_AUTHORITY, FAILURE_SEMANTICS, APPLICABLE_WHEN, PROHIBITED_WHEN, FRESHNESS_POLICY, RESULT_PROVENANCE_REQUIRED, NETWORK_REQUIRED=false, EXECUTION_AUTHORITY`
- [x] Real DB/service binding deferred to `AUTHORIZED_TO_START`; planning stage is metadata + validation only

## Privacy & audit

- [x] No raw PHI in trace store; hashes + structured reason codes only
- [x] Append-only = no mutation of prior trace records
- [x] Determinism proof: replay with same input/context/policy/registry → same `state_after`
- [x] Multilingual: Arabic (MSA + Saudi/Gulf colloquial + code-switch + transliterated drug names) and English both in scope per Grand Master Plan §13; lexicons versioned per language

## Measurability

- [x] SC-001..SC-004 are measurable over offline fixture suite (`pytest -q`, `100%`, `reproducible`, `no network/weights`)
- [x] Every FR has acceptance evidence via fixtures + validators before `IMPLEMENTATION`
- [x] Exclusions explicit (no model/PHI/device/spend; no clinical threshold fabrication; no Spec 002 redefinition)

## Dependency & authority

- [x] Spec 002 semantics preserved and composed, not redefined
- [x] Spec 005 validators reused (canonical JSON, SHA-256, fail-closed, `evaluate_hard_gates` delegation)
- [x] `AUTHORIZED_TO_START` explicitly remains `NOT_GRANTED`; no implementation source created in this planning PR
- [x] No hidden external runtime dependency assumed for fixture suite

## Overall

- [x] No unresolved critical/high contradiction remains that is resolvable without external typed evidence — remainder is `UNRESOLVED_EXTERNAL_EVIDENCE` (clinical-score list, DB identities, jurisdiction routing) tracked as prerequisites, not hidden gaps
