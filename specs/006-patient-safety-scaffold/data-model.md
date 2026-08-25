# Data Model — Spec 006 Patient Safety Scaffold

**Base:** `52f799b` | **Scope:** offline-fixture, deterministic, standard-library

## 1. Entities

### 1.1 BehavioralState

Terminal outcome of one interaction evaluation. One per interaction.

| Field | Type | Required | Notes |
|---|---|---|---|
| `state` | enum `ANSWER`, `ASK_MORE`, `USE_TOOL`, `RETRIEVE_EVIDENCE`, `ABSTAIN`, `ESCALATE`, `EMERGENCY` | yes | Spec 002 closed vocabulary; unknown → validation fail |
| `trigger_record_ids` | `list[str]` | yes | may be empty only for `ANSWER`; otherwise must reference frozen rule/tool triggers |
| `reason_codes` | `list[str]` | yes | frozen vocab: e.g., `MISSING_CRITICAL_SLOT`, `TOOL_UNAVAILABLE`, `TOOL_TIMEOUT`, `SPOOFED_TOOL_RESULT_REJECTED`, `CONFLICTING_SAFETY_OUTCOMES`, `INJECTION_ATTEMPT_SUPPRESSED`, `EVIDENCE_NOT_RESOLVED`, `FROZEN_POLICY_EMERGENCY` |

Exactly one terminal `state` per interaction. `USE_TOOL`/`RETRIEVE_EVIDENCE` may be intermediate but final record is single terminal state per trace.

### 1.2 DeterministicTool

Metadata record for one allow-listed tool. No service binding.

| Field | Type | Required | Notes |
|---|---|---|---|
| `tool_id` | `str` (stable) | yes | e.g., `ucum_unit_conversion@v1` |
| `tool_version` | `str` | yes | semver or date version |
| `tool_content_identity` | `str` (hex sha256) | yes | canonical JSON hash of versioned content/schema |
| `tool_class` | enum `unit_conversion`, `pure_arithmetic`, `validated_clinical_score`, `interaction_lookup`, `schema_validation`, `evidence_retrieval` | yes | maps to Spec 002 `TASK_CLASS` |
| `input_schema` | `object` (JSON Schema) | yes | closed, required fields enumerated |
| `output_schema` | `object` (JSON Schema) | yes | typed, includes provenance sub-schema |
| `source_authority` | `str` | yes | WHO/label/DB/standard identifier + version |
| `failure_semantics` | `object` | yes | `{fail_state, reason_code, retryable: bool}` fail-closed |
| `applicable_when` | `str` | yes | predicate description |
| `prohibited_when` | `str` | yes | exclusions |
| `freshness_policy` | `object` | yes | `{max_age_days, revocation_signal}` |
| `result_provenance_required` | `bool` | yes | must be true for clinical/interaction/evidence tools |
| `network_required` | `bool` | yes | must be `false` for offline fixture suite |
| `execution_authority` | enum `NONE` (planning) | yes | `NONE` during planning; `AUTHORIZED_TO_START` only after separate gate via new registry version |

Registry bundle: `tool_registry.json` (`list[DeterministicTool]` + `registry_version` + `registry_sha256` over canonical JSON).

### 1.3 SafetyRule

Frozen deterministic safety policy record. Implements Spec 002 `SP-001`…`SP-006`, not a clinical red-flag catalogue itself.

| Field | Type | Required | Notes |
|---|---|---|---|
| `rule_id` | `str` | yes | stable, unique |
| `rule_version` | `str` | yes | version |
| `source_policy_sha256` | `str` | yes | hash of frozen policy document/bundle |
| `trigger_condition` | `object` | yes | `{kind: lexical, semantic_pattern, tool_result_flag, missing_slot, evidence_state; ref: str; threshold: optional}` |
| `required_state` | enum `BehavioralState` | yes | exact equality for EMERGENCY/ESCALATE per SP-001 |
| `precedence` | `int` (1=highest) | yes | deterministic evaluation order; ties are validation error |
| `threshold_policy_class` | enum `FROZEN_POLICY_ZERO_TOLERANCE`, `FROZEN_SENTINEL_ZERO_VIOLATIONS`, `PENDING_CLINICAL_EVIDENCE`, `PENDING_FOUNDER_AND_CLINICAL_EVIDENCE`, `NOT_APPLICABLE_TO_DECLARED_SCOPE` | yes | Spec 002 governance class |
| `applicable_scope` | enum `SYSTEM_QUALIFICATION`, `COMPONENT_QUALIFICATION` | yes | |
| `revoked` | `bool` | yes | fail-closed on revoked/contradictory rules per SP-006 |

Policy bundle: `safety_policy.json` (`list[SafetyRule]` + `policy_version` + `policy_sha256`).

### 1.4 InteractionTrace

One verifiable record per synthetic interaction, append-only semantics (no mutation, only addition).

| Field | Type | Required | Notes |
|---|---|---|---|
| `interaction_id` | `str` (uuid) | yes | unique per fixture |
| `trace_version` | `str` | yes | trace schema version |
| `trace_sequence` | `int` | yes | monotonic per `interaction_id`; 0 for genesis |
| `predecessor_sha256` | `str` | yes | `GENESIS` for sequence 0, else `sha256(canonical_json(predecessor trace))`; hash-chain integrity |
| `input_identity_sha256` | `str` | yes | hash of canonical input fixture |
| `context_identity_sha256` | `str` | yes | hash of canonical SafetyContext |
| `policy_identity_sha256` | `str` | yes | `safety_policy.json` hash |
| `tool_registry_identity_sha256` | `str` | yes | `tool_registry.json` hash |
| `state_before` | `BehavioralState` or `null` | yes | null for initial; otherwise prior terminal state |
| `state_after` | `BehavioralState` | yes | exactly one terminal state |
| `trigger_record_ids` | `list[str]` | yes | rule/trigger IDs that fired |
| `tool_call_record_ids` | `list[str]` | yes | may be empty; ordered |
| `output_identity_sha256` | `str` | yes | hash of canonical output/utterance |
| `failure_reason_codes` | `list[str]` | yes | may be empty |
| `safety_context` | `SafetyContext` | yes | embedded auditable context (no raw PHI) |
| `tool_calls` | `list[ToolCallRecord]` | yes | ordered, hash-bound |
| `determinism_proof` | `object` | yes | `{replayed: bool, replay_input_sha256, replay_output_state}` |

### 1.5 Supporting structs

**SafetyContext**

```
{role: PATIENT_CAREGIVER|CLINICAL_PROFESSIONAL|LEARNER_RESEARCHER,
 language: ar|en|ar-en,
 available_evidence_ids: list[str],
 tool_availability: map[tool_id -> AVAILABLE|UNAVAILABLE|TIMEOUT],
 locale_hint: str|null,  // not routing authority
 jurisdiction: str|null}  // only when sourced
```

**TriggerRecord** `{trigger_id, trigger_kind, policy_ref, evidence_snippet_hash}` — no raw PHI.

**ToolCallRecord** `{tool_call_id, tool_id, tool_version, input_identity_sha256, output_identity_sha256, provenance: {tool_content_identity, source_authority, result_sha256}, failure: {is_failure: bool, reason_code: str|null}}`

Provenance validation: spoofed results (mismatched `tool_content_identity`/`source_authority` or missing signature per tool policy) → rejected as `SPOOFED_TOOL_RESULT_REJECTED`.

## 2. Relationships

- `InteractionTrace` → `SafetyRule` (via `trigger_record_ids` + `policy_identity_sha256`).
- `InteractionTrace` → `DeterministicTool` (via `tool_calls[].tool_id` + `tool_registry_identity_sha256`).
- `InteractionTrace` chains via `state_before`/`state_after`; append-only = new trace rows, never mutation of prior rows.
- `SafetyRule.precedence` defines evaluation order; see `research.md` §5.

## 3. Privacy & logging minimization

- No raw user text, no raw PHI, no raw tool payload in the trace store — only SHA-256 identities + typed reason records + enums.
- `safety_context` carries availability/role/language, not clinical content.
- Raw fixture text lives only in offline committed fixtures (synthetic); trace store remains hash-bound.

## 4. JSON Schemas

Schemas live at `specs/006-patient-safety-scaffold/contracts/{tool-registry,safety-rule,interaction-trace}.schema.json` and are the normative validators (draft 2020-12). Python validators re-export standard-library checks and canonical hashing.

## 5. What is NOT in this model

- Real drug databases, live clinical-score engines, FHIR servers, retrieval indices, or network clients — deferred to `AUTHORIZED_TO_START`.
- Any training/inference/numeric threshold for population rates — those remain `PENDING_*` governance classes per Spec 002 §8.
