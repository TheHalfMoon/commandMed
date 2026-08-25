# Plan — Spec 006 Patient Safety Scaffold & Deterministic Tools

> **Post-implementation reconciliation (2026-08-25):** this planning artifact was recovered from qualified planning head `6308e40f5f134bae7acccd66c8aa695ad9bba8ba` (PR #39) after the bounded implementation merged canonically through PR #41 (`4df3dc4eab5d3160d88b2f296dea62a8dd884b60`, tree `b5a88fa89c52335a2343d37d33bde32fb42d5082`). Lifecycle statements below reflecting `AUTHORIZED_TO_SPECIFY` / `SPECIFY ONLY` / deferred implementation are historical snapshots of the planning stage; the authoritative current state is **`SPEC_006=CLOSED_CANONICAL`** recorded in `specs/README.md` and bound in `closeout.md`. All model/weight/training/data/spend authorities remain NONE.

**Branch:** `spec/006-specify` | **Base:** `52f799b` | **Status:** planning qualified at `6308e40`; implementation canonical via PR #41 (`4df3dc4`)
**Execution authority:** NONE | **No model/weight/benchmark/Private Gold/PHI/device/spend**

## 1. Summary

Compose Spec 002 `CLOSED_CANONICAL` safety gates and Spec 005 `CLOSED_CANONICAL` control-plane validators into a minimal, offline-fixture, deterministic interaction scaffold. Freeze — [historical planning objective, satisfied and now implemented via PR #41] — the tool registry contract, safety-rule precedence, fail-closed semantics, multilingual emergency handling architecture, and auditable trace contract before any implementation. All real clinical-score versions, drug-lookup DB identities, and jurisdiction-bound emergency routing remain typed evidence prerequisites.

## 2. Technical context

- Language: Python 3.11+ (project stdlib baseline), standard library only for scaffold validators.
- Reuse: `eval_contract/canonical.py` (canonical JSON + SHA-256), `eval_contract/safety.py` (state/trigger/capability vocab), `eval_contract/validate.py` (`evaluate_hard_gates`), Spec 005 `spec005/*` validator patterns (pure, deterministic, fail-closed).
- Constraints: Offline fixtures only; `NETWORK_REQUIRED=false`; no model weights; no PHI in fixtures or traces; `implementation_authority=NONE`.
- File identity of the V1 metric catalog must be preserved (`304c980c…`); Spec 006 must not mutate it.

## 3. Constitution check

- Preamble/Gating: frozen evaluation before optimization (I) — scaffold provides frozen fixture protocol before any SFT.
- Safety hard gate (II): noncompensable failures, defense in depth — emergency/escalation/tool/evidence rules are zero-tolerance, fail-closed.
- Provenance (III): every tool/policy/trace record has version + content SHA-256 + source authority.
- Resource (IV): not applicable at scaffold layer (no device claim here).
- Universal roles (V): patient/caregiver/professional share medical truth; behavior adapts via explicit `safety_context`.
- Hybrid multimodal (VI): evidence contract (`CLAIM`/`EVIDENCE`/… ) respected; tool outputs are evidence, not prose.
- Deterministic boundary (VII): `REQUIRED_DETERMINISTIC`/`REQUIRED_AUTHORITATIVE` task classes enforced; prose cannot override validated results.
- Holdout quarantine (VIII): fixtures are synthetic/offline; no Gold/PHI access.
- Reproducibility (IX): canonical JSON + SHA-256 + determinism proof (replay ≡ same state).
- Capability preservation (X): scaffold validators must not degrade general/Arabic/tool-use checks; separate slice.
- Defense in depth (XI): `model reasoning → deterministic checks → evidence/tools → abstain/escalate` chain made operable.
- Claims integrity (XII): no clinical efficacy claim from scaffold alone.
- Minimal mechanism (XIII): smallest registry/policy/trace records that satisfy the bounded spec.
- Bounded authority (XIV): [historical planning note] the roadmap did not authorize implementation; the later founder authorization (PR #40) and merged implementation (PR #41) supply that authority canonically.

No constitution amendment is required.

## 4. Architecture (smallest deterministic implementation planned)

```text
specs/006-patient-safety-scaffold/
  spec.md, research.md, plan.md, data-model.md, quickstart.md,
  contracts/{tool-registry.schema.json, safety-rule.schema.json, interaction-trace.schema.json},
  checklists/requirements.md, tasks.md, analysis.md

Implemented layout (created canonically via PR #41):
  src/commandmed/spec006/
    __init__.py, registry.py, policy.py, trace.py, scaffold.py, canonical.py (re-exports)
  tests/spec006/
    test_registry.py, test_policy.py, test_trace.py, test_scaffold.py + fixtures/
  data/spec006/
    fixtures/*.json (synthetic offline only)
```

Core validators (intended):

- `registry.validate_tool_record` / `validate_registry` — closed allow-list, input/output JSON Schemas, SHA-256, freshness, network-false (`const NONE`), authority NONE; registry bundle identity validated via projection omitting `registry_sha256`.
- `policy.validate_safety_rule` / `validate_policy_bundle` / `evaluate_precedence` — frozen precedence order (Sec. 5 of research.md), exact-equality for EMERGENCY/ESCALATE, conflict → ABSTAIN with `BLOCKED_SAFETY_STATE` reason, injection/spoof → fail-closed, `minItems:1` + unique-precedence + trigger-coverage validation in planned `spec006.policy` bundle validator, bundle identity via projection omitting `policy_sha256`, reason codes.
- [RECONCILED TO IMPLEMENTED APIS] `trace.validate_trace(record)` / `append_trace(previous, partial)` / offline set check `validate_trace_set(traces, seal, interaction_id)` + `validate_seal(seal)` + `validate_manifest(manifest)` + trusted-tree entrypoint `validate_trace_set_trusted(trusted_commit_oid, interaction_id, ...)` — canonical, deterministic, append-only, hash-bound, privacy-safe (no raw PHI), determinism proof (5 equalities + replayed true), cross-artifact `interaction_id` equality (manifest == seal == every trace == requested), contiguous sequence + predecessor chain + state_before continuity (`0 ⇒ null`, `>0 ⇒ predecessor.state_after`) + terminal seal + seal-immutability via trusted commit OID → tree → canonical manifest/seal/trace bytes read from trusted tree through manifest-bound `seal_path`/`trace_set_path` (confined to fixtures/, no traversal, trace set as ordered JSON array). Validator MUST validate OID per object format (40/64 hex), resolve commit to tree, read `specs/006-patient-safety-scaffold/fixtures/fixture-manifest.json` from trusted tree at canonical path, require caller bytes byte-identical, require seal at `seal_path` and trace array at `trace_set_path` to be read exclusively from same trusted tree per manifest entry and to have matching interaction_id, and keep `manifest_identity_sha256` separate from the out-of-band trust anchor (FR-005).
- `scaffold.evaluate_interaction` — composes registry + policy + trace into `ANSWER|ASK_MORE|USE_TOOL|RETRIEVE_EVIDENCE|ABSTAIN|ESCALATE|EMERGENCY` with exactly one terminal state.

Anticipated tests (fixture-first, TDD-friendly):

- tool routing vs hallucination,
- missing-slot → ASK_MORE/ABSTAIN,
- emergency/escalation sentinel preservation,
- injection/spoof preservation,
- tool unavailable/timeout → fail-closed with reason,
- conflicting tool results → conflict reason + escalation,
- Arabic/English emergency triggers (lexical + semantic pattern, ambiguous → escalate),
- trace reproducibility and PHI minimization.

## 5. Data model

See `data-model.md`. Entities: `BehavioralState`, `DeterministicTool`, `SafetyRule`, `InteractionTrace`, plus supporting `SafetyContext`, `TriggerRecord`, `ToolCallRecord`. Synced to JSON Schemas in `contracts/`.

## 6. Contracts

- `contracts/tool-registry.schema.json` — one record per tool; bundle hashed as registry identity (projection omitting `registry_sha256`).
- `contracts/safety-rule.schema.json` — one record per rule; bundle hashed as policy identity (projection omitting `policy_sha256`).
- `contracts/interaction-trace.schema.json` — one trace per synthetic interaction; hash-bound and replay-verifiable (replayed const true + 5 equalities via semantic validator).
- `contracts/trace-seal.schema.json` — one terminal anchor per `interaction_id`; `expected_final_sequence` + `terminal_record_sha256` over canonical JSON of final record.
- `contracts/fixture-manifest.schema.json` — immutable manifest describing committed seals (manifest_version + entries + manifest_identity_sha256 projection); trusted git commit OID is supplied out-of-band to verifier, not stored inside manifest; anchors seal immutability for offline fixtures.

All contracts are JSON Schema draft 2020-12. Validation uses standard-library only (`json` + typed validators in `src/commandmed/spec006/`; no vendored `jsonschema` dependency); no network fetch of meta-schemas. Conformance is proven by committed negative/positive fixture tests for every keyword used across the five schemas (`required`, `type`, `enum`, `const`, `pattern`, `minLength`, `minItems`, `maximum`, `minimum`, `uniqueItems`, `additionalProperties`, `properties`, `items`, `$ref`, `$defs`, `allOf`, `if`/`then`/`else`). Stdlib validators enforce nested constraints; `properties`/`items`/`$ref` coverage is proven by fixtures that would fail if nested `additionalProperties:false` or `$ref` resolution were ignored. Bundle-identity fixtures prove `registry_sha256`/`policy_sha256` are computed over the projection omitting the hash field itself (negative fixture where hash includes itself or mismatches projection → fail). Determinism-proof fixtures prove `replayed=true` and semantic validator enforces `replay_input_sha256==input_identity_sha256`, `replay_context_identity_sha256==context_identity_sha256`, `replay_policy_identity_sha256==policy_identity_sha256`, `replay_tool_registry_identity_sha256==tool_registry_identity_sha256`, and `replay_output_state==state_after`; negative fixtures for `replayed=false` and each of the five mismatches must be rejected. Trace-seal fixtures prove contiguous 0..expected_final_sequence, unique (interaction_id, trace_sequence), predecessor chain validation, `state_before` continuity (`0 ⇒ null`, `>0 ⇒ predecessor.state_after`), and terminal_record_sha256 equality; negative fixtures for missing seal, gap, duplicate, reordered, truncated, predecessor mismatch, state-continuity violation (genesis non-null, adjacent mismatch), and terminal hash mismatch must yield INSUFFICIENT_EVIDENCE. Seal-immutability fixtures prove append-only ledger anchoring via fixture-manifest: verification is supplied a trusted commit OID out-of-band, validates OID per object format, resolves commit→tree, reads `fixture-manifest.json` from that trusted tree at canonical path, and must reject unless caller manifest bytes are byte-identical to trusted-tree bytes, `manifest_identity_sha256` matches recomputed projection, and seal/trace artifacts are read from same trusted tree with seal hash matching manifest entry; full trace-set replacement + seal replacement + manifest replacement in a different committed tree, manifest bytes not from trusted tree, seal/trace not from trusted tree, duplicate interaction_id, and manifest_identity_sha256 absent/mismatch must be rejected as INSUFFICIENT_EVIDENCE (untrusted-commit/manifest-mismatch/seal-replaced/wrong-tree).

## 7. Verification plan

- `python3 -m compileall -q src tests` PASS
- `pytest -q` — expected on canonical main: **627 passed + 128 subtests** (513 inherited baseline + spec006 suite); re-run at every material commit of the reconciliation branch and recorded in PR #42 review evidence (docs-only commits do not change these counts)
- `git diff --check` PASS
- [HISTORICAL PLANNING CHECK] `audit: git diff --name-status` confirmed no implementation existed in the planning PR. Post-implementation reconciliation re-proves the inverse: IMPLEMENTATION_DELETION=NONE against canonical PR #41 content.
- Independent exact-head review requested at meaningful heads; CodeRabbit Draft skip is NOT a pass.

## 8. Risks & mitigations

- Clinical truth drift if scores/DBs are hard-coded as prose → mitigated by registry identity + version + freshness, fail-closed on stale/missing.
- Fragile keyword-only emergency detection → mitigated by frozen policy with lexical + semantic frozen patterns + ambiguous-case escalation.
- PHI leakage via traces → mitigated by hash-only identities + structured `safety_context` + no raw text logging.
- Locale-specific emergency info fabrication → mitigated by generic escalation until jurisdiction-bound routing is sourced/versioned.
- Overengineering a plugin framework → mitigated by Ponytail: few typed records + pure validators, no services/queues.

## 9. Out of scope (explicit)

- Real drug-database/assessment implementation or service binding (metadata only here).
- Model execution, training, weight access, benchmark or Private Gold execution, PHI access, device execution, spend.
- Fabricating local emergency phone numbers/addresses without jurisdiction-bound source.
- Redesigning Spec 002 states or Spec 005 control plane.

## 10. Lifecycle note

Reconciled lifecycle: the `AUTHORIZED_TO_START` gate was granted via founder authorization recorded in PR #40 (merge `18d26f7`), after which implementation was executed and merged via PR #41. This plan text is historical planning evidence; the authoritative registry state lives in `specs/README.md`.
