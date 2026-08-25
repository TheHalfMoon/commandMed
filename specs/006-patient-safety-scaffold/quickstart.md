# Quickstart — Spec 006 Patient Safety Scaffold

> **Post-implementation reconciliation (2026-08-25):** this planning artifact was recovered from qualified planning head `6308e40f5f134bae7acccd66c8aa695ad9bba8ba` (PR #39) after the bounded implementation merged canonically through PR #41 (`4df3dc4eab5d3160d88b2f296dea62a8dd884b60`, tree `b5a88fa89c52335a2343d37d33bde32fb42d5082`). Lifecycle statements below reflecting `AUTHORIZED_TO_SPECIFY` / `SPECIFY ONLY` / deferred implementation are historical snapshots of the planning stage; the authoritative current state is implementation-complete with `SPEC_006=AUTHORIZED_TO_START` recorded in `specs/README.md`. All model/weight/training/data/spend authorities remain NONE.

**Base:** `52f799b` (historical planning base; implementation canonical via PR #41 / merge `4df3dc4`) | **Offline only** | No model/PHI/network authority

## 0. Repository synchronization (separate setup step, not part of offline evaluation)

```bash
git fetch origin --prune  # only here, not inside offline verification
git rev-parse HEAD         # current checkout; canonical implementation is PR #41 (merge 4df3dc4) or a descendant of it
cat specs/README.md | grep SPEC_006   # AUTHORIZED_TO_START; implementation canonical via PR #41
```

## 1. Verify baseline (offline, after sync)

```bash
python3 -m compileall -q src tests
python3 -m pytest -q  # 627 passed + 128 subtests expected on canonical main (513 inherited baseline + spec006 suite)
```

## 2. Validate contracts (offline, stdlib only — no network, no vendored validator)

Bundle identities are projection hashes: `registry_sha256 = sha256(canonical_json({registry_version, tools}))` and `policy_sha256 = sha256(canonical_json({policy_version, rules}))` omitting the hash field itself. Determinism proof requires `replayed=true` and semantic equalities `replay_input_sha256==input_identity_sha256`, `replay_context_identity_sha256==context_identity_sha256`, `replay_policy_identity_sha256==policy_identity_sha256`, `replay_tool_registry_identity_sha256==tool_registry_identity_sha256`, `replay_output_state==state_after` (enforced by semantic validator, not JSON Schema alone). Trace-set verification requires a `trace_seal.json` per interaction_id and a committed `fixture-manifest.json` with `manifest_identity_sha256` projection; verification is supplied a trusted commit OID out-of-band, validates OID (40/64 hex), resolves commit→tree, reads manifest/seal/trace bytes exclusively from that trusted tree at canonical paths, and requires byte-identical caller bytes, manifest_identity_sha256 projection match, contiguous 0..expected_final_sequence, unique keys, predecessor chain, `state_before` continuity (`0 ⇒ null`, `>0 ⇒ predecessor.state_after`), and seal hash equality — missing/mismatched seal or manifest, wrong-tree artifacts, or OID mismatch → INSUFFICIENT_EVIDENCE. Seal/manifest immutability is via trusted-tree byte identity, not manifest-stored OID (append-only ledger).

```bash
python3 -c "
import json, pathlib
from src.commandmed.eval_contract.canonical import compute_canonical_sha256
for name in ['tool-registry','safety-rule','interaction-trace']:
    p = pathlib.Path(f'specs/006-patient-safety-scaffold/contracts/{name}.schema.json')
    j = json.loads(p.read_text())
    assert json.dumps(j)  # syntax check
    sha = compute_canonical_sha256(j)
    print(name, sha[:12], 'valid-json')
# Full schema conformance (required/type/enum/const/pattern/minItems/etc.)
# is proven by committed fixtures in tests/spec006/fixtures/ (see plan.md §6);
# [historical planning note] T011 has since provided typed validators canonically (PR #41);
"
```

## 3. How to add a deterministic tool (metadata record; runtime validators canonical since PR #41)

1. Choose `tool_class` from the frozen vocabulary (see `research.md` §3).
2. Write a record per `contracts/tool-registry.schema.json` with `tool_content_identity` = canonical SHA-256 of the versioned content/schema, `source_authority` bound, `network_required=false`, `execution_authority=NONE`, `failure_semantics` fail-closed.
3. Validate (implementation is canonical since PR #41):
   ```python
   from src.commandmed.spec006.registry import validate_tool_record
   errors = validate_tool_record(record)  # [] == pass
   ```
4. Real implementation/service binding remains outside this scaffold's authority: registry records stay `execution_authority=NONE`; any live binding requires its own separate authorization gate. No model/weight/training/data/spend authority is granted or implied here.

## 4. How to add a frozen safety rule

1. Bind `source_policy_sha256` + `rule_version`.
2. Set `required_state` with exact equality for `EMERGENCY`/`ESCALATE` (SP-001); set `precedence` per research.md §5 order.
3. Set `threshold_policy_class` per Spec 002 §8 (`FROZEN_*` zero-tolerance vs `PENDING_*`).
4. Validate with the canonical validators (implemented since PR #41):
   ```python
   from src.commandmed.spec006.policy import validate_safety_rule
   errors = validate_safety_rule(rule)
   ```

## 5. How fixtures prove the scaffold

Synthetic fixtures only, committed JSON, `pytest -q` deterministic:

- `tests/spec006/fixtures/*.json` each carry expected `state_after` + `reason_codes`.
- `trace.validate_trace()` + `scaffold.evaluate_interaction()` replay proves determinism (`replay_output_state == state_after`).
- No network, no weights, no PHI, no external API.

## 6. Authority guardrails

Every registry/policy record keeps the bounded record constraint `execution_authority=NONE`; the canonical validators enforce this field (see `registry.py` and the schema `const: "NONE"`). Separately — and independently of that per-record field — this scaffold grants no model execution, model-weight access, benchmark payload access/execution, Private Gold access, PHI access, device execution, external clinical database access, credential access, or spend; those require their own explicit authorization gates and are not granted by Spec 006.
