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

Registry bundle: `tool_registry.json` (`list[DeterministicTool]` + `registry_version` + `registry_sha256`). Canonical bundle identity `registry_sha256 = sha256(canonical_json({registry_version, tools}))` computed over the canonical JSON projection that omits the `registry_sha256` field itself (deterministic sorted-key serialization per `eval_contract/canonical.py`). Validators must recompute by omitting `registry_sha256` and comparing; fixtures must include a negative case where `registry_sha256` does not match the projection.

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

Policy bundle: `safety_policy.json` (`list[SafetyRule]` + `policy_version` + `policy_sha256`). Canonical bundle identity `policy_sha256 = sha256(canonical_json({policy_version, rules}))` computed over the canonical JSON projection that omits the `policy_sha256` field itself. Validators must recompute by omitting `policy_sha256` and comparing; fixtures must include a negative case where `policy_sha256` does not match the projection.

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
| `policy_identity_sha256` | `str` | yes | `safety_policy.json` projection hash (per §1.3, omitting `policy_sha256`) |
| `tool_registry_identity_sha256` | `str` | yes | `tool_registry.json` projection hash (per §1.2, omitting `registry_sha256`) |
| `state_before` | `BehavioralState` or `null` | yes | null for initial; otherwise prior terminal state |
| `state_after` | `BehavioralState` | yes | exactly one terminal state |
| `trigger_record_ids` | `list[str]` | yes | rule/trigger IDs that fired |
| `tool_call_record_ids` | `list[str]` | yes | may be empty; ordered |
| `output_identity_sha256` | `str` | yes | hash of canonical output/utterance |
| `failure_reason_codes` | `list[str]` | yes | may be empty |
| `safety_context` | `SafetyContext` | yes | embedded auditable context (no raw PHI) |
| `tool_calls` | `list[ToolCallRecord]` | yes | ordered, hash-bound |
| `determinism_proof` | `object` | yes | `{replayed: const true, replay_input_sha256 == input_identity_sha256, replay_context_identity_sha256 == context_identity_sha256, replay_policy_identity_sha256 == policy_identity_sha256, replay_tool_registry_identity_sha256 == tool_registry_identity_sha256, replay_output_state == state_after}` — JSON Schema enforces `replayed=true` and typed fields; semantic validator must enforce all five equalities (see contracts) |

### 1.5 TraceSeal (terminal completeness anchor)

Per `interaction_id`, one `trace_seal.json` anchoring the complete trace set. Verification consumes the full set plus the seal.

| Field | Type | Required | Notes |
|---|---|---|---|
| `interaction_id` | `str` (uuid) | yes | matches sealed InteractionTrace set |
| `seal_version` | `str` | yes | seal schema version |
| `expected_final_sequence` | `int` | yes | expected max `trace_sequence`; verification rejects unless contiguous 0..expected_final_sequence |
| `terminal_record_sha256` | `str` (hex sha256) | yes | `sha256(canonical_json(final InteractionTrace record))` where `trace_sequence == expected_final_sequence` |

Manifest-bound artifact resolution: each manifest entry binds `seal_path` and `trace_set_path` as canonical relative paths confined to `specs/006-patient-safety-scaffold/fixtures/` (no traversal, normalized). `trace_set_path` points to an ordered JSON array of `InteractionTrace` records for that `interaction_id` at that path in the trusted tree; representation is explicitly ordered. Validator MUST NOT scan directories — it MUST load seal and trace set only through the manifest-bound paths in the resolved trusted tree.

Validation rule (FR-005): verification `validate_trace_set(trusted_commit_oid, interaction_id)` MUST reject unless sequences are strictly contiguous from 0, `(interaction_id, trace_sequence)` keys are unique and monotonic, `predecessor_sha256 == sha256(canonical_json(predecessor))` chain validates, `state_before` continuity holds (`trace_sequence==0 ⇒ state_before==null`; `trace_sequence>0 ⇒ state_before == predecessor.state_after`), and `terminal_record_sha256` equals recomputed hash of final record — otherwise `INSUFFICIENT_EVIDENCE`. Missing seal, gap, duplicate, reordered, predecessor mismatch, state-continuity violation, or terminal hash mismatch → `INSUFFICIENT_EVIDENCE`.

Seal immutability (anti-replacement): trace store is append-only; each `(interaction_id, trace_seal)` is written once and its ledger position is immutable. Offline fixture suite anchors seals in a committed `fixture-manifest.json` at `specs/006-patient-safety-scaffold/fixtures/fixture-manifest.json` (see `contracts/fixture-manifest.schema.json`) whose content identity is `manifest_identity_sha256` (projection omitting itself). The trusted git commit OID is supplied out-of-band to the verifier per repository object format (sha1=40 hex, sha256=64 hex) and is NOT stored inside the manifest it authenticates. Verification MUST be supplied `trusted_commit_oid` out-of-band, validate OID format per object format, resolve it to its tree, read `fixture-manifest.json` from that trusted tree at canonical path, and MUST reject unless (a) the bytes of the caller-supplied manifest are byte-identical to the bytes read from the trusted tree, (b) the seal file's `sha256(canonical_json(seal))` at `seal_path` in trusted tree matches the manifest entry `seal_canonical_sha256` for that `interaction_id`, (c) the trace set at `trace_set_path` in trusted tree is loaded and its final record hash/sequence match the seal and manifest entry, and (d) seal/trace bytes are exclusively from that trusted tree (caller-supplied artifacts not on manifest-bound paths are ignored/rejected). The `manifest_identity_sha256` is a separate projection hash, not a substitute for the out-of-band commit OID. A later commit that replaces trace set + seal + manifest together yields a different commit OID and therefore fails step (a) → `INSUFFICIENT_EVIDENCE` (untrusted-commit / manifest-mismatch). Each `interaction_id` MUST appear exactly once in manifest entries with unique manifest-bound paths (semantic validator must reject duplicate interaction_id or duplicate seal/trace paths even if entries differ byte-wise; `uniqueItems` alone is insufficient). Negative fixtures must cover missing path, traversal path, missing trusted-tree artifact, seal outside manifest-bound path, trace outside manifest-bound path, wrong OID, manifest bytes not from trusted tree, seal/trace not from trusted tree, duplicate interaction_id, duplicate paths, and manifest_identity_sha256 mismatch.

### 1.6 Supporting structs

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

Schemas live at `specs/006-patient-safety-scaffold/contracts/{tool-registry,safety-rule,interaction-trace,trace-seal,fixture-manifest}.schema.json` and are the normative validators (draft 2020-12). Python validators re-export standard-library checks and canonical hashing. Trace-set validation (contiguous sequence + predecessor chain + state continuity + terminal seal + manifest-bound seal immutability) is a semantic validator over the set plus `TraceSeal` plus `FixtureManifest` with trusted commit hash supplied out-of-band, not a single-record JSON Schema check.

## 5. What is NOT in this model

- Real drug databases, live clinical-score engines, FHIR servers, retrieval indices, or network clients — deferred to `AUTHORIZED_TO_START`.
- Any training/inference/numeric threshold for population rates — those remain `PENDING_*` governance classes per Spec 002 §8.
