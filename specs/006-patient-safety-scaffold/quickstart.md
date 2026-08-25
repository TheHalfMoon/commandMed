# Quickstart — Spec 006 Patient Safety Scaffold

**Base:** `52f799b` | **Offline only** | No model/PHI/network authority

## 0. Repository synchronization (separate setup step, not part of offline evaluation)

```bash
git fetch origin --prune  # only here, not inside offline verification
git rev-parse HEAD         # must be on planning head derived from 52f799b
cat specs/006-patient-safety-scaffold/spec.md | head -n 6  # Status AUTHORIZED_TO_SPECIFY
```

## 1. Verify baseline (offline, after sync)

```bash
python3 -m compileall -q src tests
python3 -m pytest -q  # 513 PASS inherited baseline — no network
```

## 2. Validate contracts (offline, stdlib only — no network, no vendored validator)

Bundle identities are projection hashes: `registry_sha256 = sha256(canonical_json({registry_version, tools}))` and `policy_sha256 = sha256(canonical_json({policy_version, rules}))` omitting the hash field itself. Determinism proof requires `replayed=true` and semantic equality `replay_input_sha256==input_identity_sha256` + `replay_output_state==state_after` (enforced by semantic validator, not JSON Schema alone).

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
# planning stage has no runtime validator beyond syntax+hash — T011 provides typed validators.
"
```

## 3. How to add a deterministic tool (metadata only, planning stage)

1. Choose `tool_class` from the frozen vocabulary (see `research.md` §3).
2. Write a record per `contracts/tool-registry.schema.json` with `tool_content_identity` = canonical SHA-256 of the versioned content/schema, `source_authority` bound, `network_required=false`, `execution_authority=NONE`, `failure_semantics` fail-closed.
3. Validate (post-implementation only — `src/commandmed/spec006` does not exist in planning PR):
   ```python
   # After T011 (AUTHORIZED_TO_START):
   from src.commandmed.spec006.registry import validate_tool_record
   errors = validate_tool_record(record)  # [] == pass
   # Planning stage: validate against contracts/tool-registry.schema.json via offline JSON Schema check
   ```
4. Real implementation/service binding requires `AUTHORIZED_TO_START` — not granted here.

## 4. How to add a frozen safety rule

1. Bind `source_policy_sha256` + `rule_version`.
2. Set `required_state` with exact equality for `EMERGENCY`/`ESCALATE` (SP-001); set `precedence` per research.md §5 order.
3. Set `threshold_policy_class` per Spec 002 §8 (`FROZEN_*` zero-tolerance vs `PENDING_*`).
4. Validate (post-implementation only):
   ```python
   # After T011 (AUTHORIZED_TO_START):
   from src.commandmed.spec006.policy import validate_safety_rule
   errors = validate_safety_rule(rule)
   # Planning stage: validate against contracts/safety-rule.schema.json via offline JSON Schema check
   ```

## 5. How fixtures prove the scaffold

Synthetic fixtures only, committed JSON, `pytest -q` deterministic:

- `tests/spec006/fixtures/*.json` each carry expected `state_after` + `reason_codes`.
- `trace.validate_trace()` + `scaffold.evaluate_interaction()` replay proves determinism (`replay_output_state == state_after`).
- No network, no weights, no PHI, no external API.

## 6. Authority guardrails

At this stage every registry/policy record must have `execution_authority=NONE`. Any attempt to set `AUTHORIZED_TO_START`, access model weights, benchmark payloads, Private Gold, PHI, devices, or spend must be rejected by validators.
