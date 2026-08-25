# Spec 005 — Base Model Tournament Canonical Closeout

**Closeout type:** dedicated post-implementation governance closure
**Status:** `CLOSED_CANONICAL` — effective only after this closure-only PR is merged and resulting canonical `main` is verified
**Implementation PR:** `#36`
**Planning reconciliation PR:** `#37` (supersedes stale `#34`)
**Canonical implementation merge:** `5e35cd423c54ce743b9b305287971a97eeeb7a64`
**Canonical implementation tree:** `5b823d20fd1106669e1b79af4d301d15c5e4e8dd`
**Final reviewed implementation head:** `d4caf94952e77888755788b490d6a5267e5e3a9d`
**Canonical implementation base:** `e681f92dc9479fdc077d21dafcacca5e29cfa7eb`
**Planning reconciliation merge:** `799c36a9a6113357a6fa9b02a7178f94fad6ee0c`
**Planning reconciliation tree:** `eaa89429f996f2fed315ebc15462273dfa5125a4`
**Final reviewed reconciliation head:** `83d76127df340b26350a79ccd4c6b2b266479ec6`
**Canonical planning base:** `5e35cd423c54ce743b9b305287971a97eeeb7a64`

> This closeout is intentionally non-self-referential. It binds already-canonical implementation and planning evidence below but does not claim the closure merge SHA containing itself. `SPEC_005=CLOSED_CANONICAL` becomes effective only after this exact closure head is independently reviewed, guarded-merged unchanged, and the resulting canonical `main` plus lifecycle records are verified.

## 1. Canonical implementation binding

Spec 005 deterministic control plane was guarded squash-merged through PR #36 with expected heads:

```text
FINAL_REVIEWED_IMPLEMENTATION_HEAD=d4caf94952e77888755788b490d6a5267e5e3a9d
CANONICAL_IMPLEMENTATION_MERGE=5e35cd423c54ce743b9b305287971a97eeeb7a64
CANONICAL_IMPLEMENTATION_TREE=5b823d20fd1106669e1b79af4d301d15c5e4e8dd
CANONICAL_IMPLEMENTATION_BASE=e681f92dc9479fdc077d21dafcacca5e29cfa7eb
```

Canonical `main` was verified at the implementation merge/tree before the planning reconciliation branch was created. Planning PR #34 (`f116bea462a868f990fc3f5d2196b4c29bc7b1b2`) was then identified as stale (pre-implementation base, would delete `src/commandmed/spec005/*` if merged). Fresh reconciliation branch `docs/005-post-implementation-reconciliation` was cut from `5e35cd4`.

## 2. Planning reconciliation binding

Planning artifacts were recovered without implementation deletion via:

```text
git checkout origin/spec/005-clarify -- specs/005-base-model-tournament/
```

and reconciled on PR #37:

```text
FINAL_REVIEWED_RECONCILIATION_HEAD=83d76127df340b26350a79ccd4c6b2b266479ec6
CANONICAL_RECONCILIATION_MERGE=799c36a9a6113357a6fa9b02a7178f94fad6ee0c
CANONICAL_RECONCILIATION_TREE=eaa89429f996f2fed315ebc15462273dfa5125a4
CANONICAL_RECONCILIATION_BASE=5e35cd423c54ce743b9b305287971a97eeeb7a64
```

Recovered artifacts (57 files):
- `clarification-closeout.md`, `research.md`, `plan.md` (with post-implementation banner), `data-model.md`, `contracts/preconstruction-control-contract.md`, `quickstart.md` (with banner), `checklists/implementation-readiness.md`, `tasks.md` (49 tasks reconciled to [x] with evidence mapping), `jetbrains-handoff.md` (with banner)
- 30 session research docs (`session-6-*` through `session-14-*`), `admission-evidence.md`, `context-kv-envelope-research.md`, `device-target-research.md`, `qwen-*`, `safety-floor-evidence.md`, `ultra-compact-candidate-sweep.md`

Stale lifecycle claims (`AUTHORIZED_TO_SPECIFY`, `spec/005-clarify`, `IMPLEMENTATION_STATUS=NOT_STARTED`, `NEXT_LIFECYCLE_STEP=IMPLEMENT`) are preserved as historical evidence but explicitly labeled with post-implementation banners dated 2026-08-25 pointing to canonical implementation `5e35cd4`. `tasks.md` was reconciled to check all 49 tasks with commit/path/test mapping; real-world execution (A15 construction, model/benchmark/Private Gold/PHI/device/spend) remains `NOT_AUTHORIZED`.

Verification on reconciliation head `83d7612`:
```text
compileall PASS
pytest 513 PASS
git diff --check PASS
IMPLEMENTATION_DELETION=NONE
HISTORICAL_EVIDENCE_PRESERVED=YES
STALE_LIFECYCLE_CLAIMS_RECONCILED=YES
AUTHORITY_BOUNDARIES_PRESERVED=YES
```

## 3. Final exact-head qualification

Implementation head `d4caf94` qualification:
- Local: `compileall PASS`, `pytest 513 PASS` (216 spec005 + 297 inherited), no V1 identity drift
- Qodo exact-head review on PR #36 at `d4caf94`: `No Qodo review findings` (documentation + implementation readiness still correctly blocked for execution)

Reconciliation head `83d7612` qualification:
- Local: `compileall PASS`, `pytest 513 PASS`, `git diff --check PASS`
- Qodo exact-head review on PR #37 at `83d7612`: `no actionable correctness or security defects; documentation/evidence contracts only; implementation readiness still correctly marked blocked`

PR #34 was closed as superseded after preservation was proven (preservation comment `5404699994`), not merged.

## 4. Bounded implementation completed

Spec 005 provides the deterministic offline control plane for baseline-only tournament **preparation**, not execution:

- additive metrics-v2 (`data/eval/metrics-v2.json`, `eval_contract` V2) preserving V1 SHA `304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a`
- seven noncompensable medical quality lanes (A2) + metric/evidence-role mapping + per-metric threshold/margin + estimand/direction + clinical+statistical evidence + paired Arabic parity
- atomic A3+A4 statistical design/allocation with candidate-neutral planning and BLOCKED on missing N/allocation
- A5–A12 preconstruction: source-route/rights/privacy/parent-derivation, metadata-only root/pair/review bindings, contamination-plan identity, material-change identity, dependency DAG + staleness
- A7 personnel: opaque identity, qualification, Gold exposure, role-scoped assignment, independence, bootstrap handshake
- A13 access: three-zone policy, A7 handshake, revocation, result firewall
- A14 finance: workload/capacity requirement (`NOT_REQUIRED`/`REQUIRED`/`BLOCKED`), authorization identity + separation of duties, lifecycle state machine, `A14_NOT_REQUIRED_PASS`/`A14_AUTHORIZED_PASS` with staleness
- A15 + device: frozen five targets/8K-16K/Q8_0/5-run metadata validation, immutable activation binding requiring `READY_FOR_SEPARATE_ACTIVATION_NOT_AUTHORIZED` snapshot + all PASS gates including T1/D34
- Spec 004 projection adapter: emits Spec 004 tournament manifest only when all prerequisite identities valid; otherwise fail-closed no-selection

All validators are pure, deterministic, standard-library, fail-closed, SHA-256-bound.

## 5. Exact canonical identities bound

Inherited V1 identities (unchanged):
```text
benchmarks_sha256=7f58edba1ac179cbf24cb2d5c902e2ef947024bfd1c6eacdbef1a609b00f64a7
metrics_sha256=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
gold_protocols_sha256=40c89702469d759f4dc893aff6bc6fdb7e300f9cb2d8f19f2b3e0dbd78200666
quarantine_sha256=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
safety_policy_sha256=79a12414fe68fc08efb43070f3eede36976f2e0dc0ece7f4eed4bbcc5496d14f
lineage_contract_sha256=2b085339c17c3b8b89e55f53fc62c23bcbcf968cdc744b8ead0549b462bda962
```

Metrics-v2 additive artifact: `data/eval/metrics-v2.json` (additive, V1 preserved). Spec 005 control-plane contracts: `selection_quality_contract.json`, `preconstruction_contract.json`, `device_qualification_contract.json`.

## 6. Explicit authority boundary (still enforced after closure)

Spec 005 does **not** authorize or perform:

```text
MODEL_EXECUTION=NONE
MODEL_WEIGHT_ACCESS=NONE
MODEL_CONVERSION=NONE
TRAINING=NONE
BENCHMARK_PAYLOAD_ACCESS=NONE
BENCHMARK_PAYLOAD_EXECUTION=NONE
PRIVATE_GOLD_ACCESS=NONE
PROVIDER_GENERATION=NONE
PHI_ACCESS=NONE
GATED_ASSET_ACCESS=NONE
DEVICE_EXECUTION=NONE
A13_STORAGE_PROVISIONING=NONE
A13_PAYLOAD_ACCESS=NONE
A13_RESULT_ACCESS=NONE
A14_SPEND_EXECUTION=NONE
A14_PAYMENT_EXECUTION=NONE
A15_CONSTRUCTION_ACTIVATION=NONE
REAL_SELECTION_CASE_AUTHORING=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Control-plane validators may return synthetic `PASS`/`READY_FOR_SEPARATE_AUTHORIZATION` fixtures; no fixture creates real authority. Real tournament execution, threshold selection from results, and winner selection remain separately authorized and separately gated.

Valid outcomes remain `NO_SELECTION` when evidence is incomplete.

## 7. Closure-review reconciliation

This closeout reconciles:

- `specs/005-base-model-tournament/closeout.md` (this file)
- `specs/005-base-model-tournament/tasks.md` (49/49 checked with evidence mapping + footer)
- `specs/005-base-model-tournament/spec.md` (historical AUTHORIZED_TO_SPECIFY preserved + post-implementation banner)
- `specs/005-base-model-tournament/plan.md`, `jetbrains-handoff.md`, `quickstart.md` (historical planning branch preserved + banner)
- `specs/README.md` (registry transition, see §8)

No implementation files were deleted in reconciliation; planning evidence was recovered additively.

## 8. Registry transition

Upon guarded merge of this closeout, `specs/README.md` transitions:

```text
005 Base Model Tournament: AUTHORIZED_TO_SPECIFY → CLOSED_CANONICAL
  Implementation: 5e35cd4 (PR #36, d4caf94)
  Planning reconciliation: 799c36a (PR #37, 83d7612)
  Closure: <THIS_MERGE_SHA> (this PR, <HEAD_SHA>)
```

`006 Patient Safety Scaffold & Deterministic Tools: BLOCKED (002,005) → AUTHORIZED_TO_SPECIFY` (dependency 005 satisfied; lifecycle SPECIFY may begin per Spec Kit workflow). No other registry rows change in this PR.

## 9. Post-closure verification

After merge, verify:

```text
git fetch origin --prune
git checkout main
git pull --ff-only
git rev-parse HEAD
git rev-parse HEAD^{tree}
pytest -q   # 513 PASS expected
python -m compileall -q src tests
git ls-files --others --exclude-standard  # empty
```

## 10. Next frontier

With `005 CLOSED_CANONICAL`, the next repository-defined frontier is `006 Patient Safety Scaffold & Deterministic Tools`. Its Spec Kit lifecycle (specify → clarify → plan → tasks → analyze → implement) may be started under `AUTHORIZED_TO_SPECIFY` without granting model/benchmark/execution authority. Implementation of 006 must not begin until its own `AUTHORIZED_TO_START`.
