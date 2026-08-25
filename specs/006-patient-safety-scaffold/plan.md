# Plan — Spec 006 Patient Safety Scaffold & Deterministic Tools

**Branch:** `spec/006-specify` | **Base:** `52f799b` | **Status:** `AUTHORIZED_TO_SPECIFY` (planning only)
**Execution authority:** NONE | **No model/weight/benchmark/Private Gold/PHI/device/spend**

## 1. Summary

Compose Spec 002 `CLOSED_CANONICAL` safety gates and Spec 005 `CLOSED_CANONICAL` control-plane validators into a minimal, offline-fixture, deterministic interaction scaffold. Freeze the tool registry contract, safety-rule precedence, fail-closed semantics, multilingual emergency handling architecture, and auditable trace contract before any implementation. All real clinical-score versions, drug-lookup DB identities, and jurisdiction-bound emergency routing remain typed evidence prerequisites.

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
- Bounded authority (XIV): roadmap does not authorize implementation.

No constitution amendment is required.

## 4. Architecture (smallest deterministic implementation planned)

```
specs/006-patient-safety-scaffold/
  spec.md, research.md, plan.md, data-model.md, quickstart.md,
  contracts/{tool-registry.schema.json, safety-rule.schema.json, interaction-trace.schema.json},
  checklists/requirements.md, tasks.md, analysis.md

Intended implementation (deferred, NOT created in this planning PR):
  src/commandmed/spec006/
    __init__.py, registry.py, policy.py, trace.py, scaffold.py, canonical.py (re-exports)
  tests/spec006/
    test_registry.py, test_policy.py, test_trace.py, test_scaffold.py + fixtures/
  data/spec006/
    fixtures/*.json (synthetic offline only)
```

Core validators (intended):

- `registry.validate_tool_record` / `validate_registry` — closed allow-list, input/output JSON Schemas, SHA-256, freshness, network-false, authority NONE.
- `policy.validate_safety_rule` / `evaluate_precedence` — frozen precedence order (Sec. 5 of research.md), exact-equality for EMERGENCY/ESCALATE, conflict → ABSTAIN/ESCALATE, injection/spoof → fail-closed, reason codes.
- `trace.validate_trace` / `append_trace` — canonical, deterministic, append-only, hash-bound, privacy-safe (no raw PHI), determinism proof.
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

- `contracts/tool-registry.schema.json` — one record per tool; bundle hashed as registry identity.
- `contracts/safety-rule.schema.json` — one record per rule; bundle hashed as policy identity.
- `contracts/interaction-trace.schema.json` — one trace per synthetic interaction; hash-bound and replay-verifiable.

All contracts use JSON Schema draft 2020-12, standard-library validation only.

## 7. Verification plan

- `python3 -m compileall -q src tests` PASS
- `pytest -q` — baseline 513 pass preserved; spec006 fixtures add deterministically (no network/model/PHI)
- `git diff --check` PASS
- `audit: git diff --name-status origin/main...HEAD` — no accidental implementation deletion; no `src/commandmed/spec006` implementation yet (planning PR)
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

This plan is `AUTHORIZED_TO_SPECIFY` planning only. Implementation may begin only after a separately authorized `AUTHORIZED_TO_START` gate. The PR remains Draft until `analyze` passes cleanly and exact-head review qualifies it.
