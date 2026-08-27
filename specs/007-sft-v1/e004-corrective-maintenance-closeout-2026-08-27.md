# E004 Corrective Maintenance Closeout — 2026-08-27

**Spec:** 007 SFT V1
**Scope:** bounded Spec 005 ↔ E004 corrective maintenance only
**Authorization record:** `specs/007-sft-v1/e004-corrective-maintenance-authorization-2026-08-27.md`
**Authorization PR / merge:** #66 / `238d8a0b8cfed54356ca39bb892f94ebf12d89de`
**Implementation PR:** #67
**Qualified implementation head:** `53aa3ab29636563f11a82b72d4cfd940a2351792`
**Canonical implementation merge:** `5bb6177dc7908dfb3a6a51d3c39db66a4e289fb1`
**Canonical implementation tree:** `493fa9290d10046a854ae36909f4590272987c46`
**E004 execution performed:** NO

## Closeout decision

The separately authorized corrective-maintenance scope is complete and canonically implemented. This closeout does **not** close E004 itself and grants no new execution or access authority.

```text
E004_CORRECTIVE_MAINTENANCE=CLOSED_CANONICAL
DEVICE_A15_STRUCTURAL_CYCLE=RESOLVED_BY_CONTROL_PLANE_REPAIR
DEVICE_PACKAGE_WARMUP_CONTRACT=RECONCILED
E004_NON_EXECUTING_REQUEST_ENVELOPE=IMPLEMENTED
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
```

## What was repaired

### CM-1 — pre-execution readiness vs post-execution qualification

`src/commandmed/spec005/device.py` now separates two trust boundaries:

- `evaluate_device_execution_readiness()` computes static pre-execution readiness from exact contract/runtime/build/tool/signal/target identities and requires no measured run evidence;
- `evaluate_device_preflight()` remains post-execution qualification and still requires the frozen five measured runs per target plus fail-closed measured evidence.

The pre-execution record prohibits measured runs. A favorable readiness state is not caller-owned: `src/commandmed/spec005/manifest.py` recomputes the readiness record from supplied canonical inputs and verifies its canonical SHA-256.

This removes the prior closed loop without converting missing measurements into PASS.

### CM-2 — frozen device-contract reconciliation

`data/spec005/device_qualification_contract.json` now reflects already-frozen Spec 005 decisions:

```text
COMPLETE_MINIMUM_TEXT_CORE_BUNDLE_HARD_CAP_BYTES=734003200
ENGINEERING_TARGET_BYTES=629145600
STRETCH_TARGET_BYTES=524288000
PRIMARY_PACKAGE_CAP_NONCOMPENSABLE=YES
CONTROL_PACKAGE_CAP_CONTROL_WINNING_GATE=NO
NON_MEASURED_WARMUP_REQUESTS=0
MEASURED_RUNS_PER_TARGET=5
FRESH_PROCESS_PER_MEASURED_RUN=YES
MEASURED_REQUESTS_PER_PROCESS=1
```

Numeric performance thresholds remain explicitly unresolved and cannot be invented by this repair. Exact runtime/build/tool/signal identities remain real pre-execution evidence requirements.

### CM-3 — deterministic E004 execution envelope

`src/commandmed/spec007/e004.py` provides a deterministic, fail-closed request builder only. It binds existing authority and identity records, rejects widened authority, shells, secrets/credential flags, Private Gold/PHI markers, undeclared fields, malformed plans, and stale/unqualified prerequisite state.

A valid plan may produce a canonical external-executor request identity, but the module always reports:

```text
execution_performed=false
```

It imports no process/network/model-runtime execution mechanism and therefore does not itself execute E004.

## Exact-head qualification evidence

A temporary trigger-only validation carrier explicitly checked out the exact implementation subject rather than validating the carrier tree.

```text
VALIDATED_SUBJECT_SHA=53aa3ab29636563f11a82b72d4cfd940a2351792
VALIDATION_RUN=33082514984
VALIDATION_JOB=98553269856
COMPILEALL=PASS
FOCUSED_CORRECTIVE_MAINTENANCE_TESTS=70 PASS
FULL_OFFLINE_REGRESSION=811 PASS + 136 subtests PASS
GIT_DIFF_CHECK=PASS
BOUNDED_DIFF_SCOPE=PASS
```

The bounded path gate accepted exactly:

- `data/spec005/device_qualification_contract.json`
- `src/commandmed/spec005/device.py`
- `src/commandmed/spec005/manifest.py`
- `src/commandmed/spec007/e004.py`
- `tests/spec005/test_device.py`
- `tests/spec005/test_manifest.py`
- `tests/spec007/test_e004.py`

No model, benchmark payload, physical device, network/model download, conversion, training, credentialed/gated asset, Private Gold, PHI, provider-generation, or paid-resource execution occurred during qualification.

## Independent exact-head review

Review carrier PR #68 pointed directly at the same exact implementation SHA `53aa3ab29636563f11a82b72d4cfd940a2351792` and introduced no additional commit or content. Qodo recommended retaining the explicit phase separation and dedicated E004 validator because the design removes the circular readiness dependency, recomputes favorable state instead of trusting caller declarations, and introduces no execution capability. No inline review threads were present.

GitHub subsequently reports PR #68 as merged because its head is exactly the commit that entered `main` through canonical PR #67; PR #68 was not a separate merge path and added no extra bytes.

## Post-merge canonical verification

After guarded merge with `expected_head_sha=53aa3ab29636563f11a82b72d4cfd940a2351792`, canonical `main` was verified at:

```text
MAIN=5bb6177dc7908dfb3a6a51d3c39db66a4e289fb1
TREE=493fa9290d10046a854ae36909f4590272987c46
PARENT_BASE=238d8a0b8cfed54356ca39bb892f94ebf12d89de
PARENT_IMPLEMENTATION=53aa3ab29636563f11a82b72d4cfd940a2351792
```

## Authority preserved

The repair changes repository control-plane semantics only. It does not widen the current authority envelope.

```text
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

E003 remains the only bounded live-tournament execution grant, and it remains conditional on a complete PASS A15/preflight. The corrective-maintenance merge does not itself create that PASS.

## Remaining E004 blocker frontier

The former device/A15 structural cycle is no longer a blocker. E004 remains fail-closed on separate prerequisites documented by the earlier frontier audit and preserved by this closeout:

1. **Frozen artifact authority reconciliation** — bind an exact executable GGUF path for every frozen candidate that requires qualification, or separately authorize a bounded conversion path. Current E002 allowlist must not expand by implication.
2. **Contamination-assessment authority and evidence** — separately authorize the exact public/ungated assessment inputs and methods needed to create candidate × selection-slice contamination evidence. E003 does not authorize opening unresolved selection payloads merely to manufacture its prerequisite.
3. **Scientific/governance evidence** — exact evaluation-suite identities, clinical/statistical authorities, frozen threshold/margin values, uncertainty methods, N/power/allocation records, and FD-004 where applicable.
4. **Runtime/resource preconstruction** — exact runtime/build/tool/signal identities, physical target bindings, personnel/access/finance evidence, and verified zero-spend resource availability.
5. **Real A1–A14 snapshot and separate A15 activation** — only after all prerequisite records are complete, current, identity-bound, and PASS.
6. **Exact E004 manifest + final pre-execution validation** — any `BLOCKED`, `INCOMPLETE`, `NEEDS_EVIDENCE`, stale, mismatched, or unauthorized state remains fail-closed.

Only after those prerequisites are satisfied may the already-authorized E003 scope permit E004 execution. E004 produces evidence only; E005 remains a Founder+ChatGPT decision.

## Next dependency-safe decision

```text
NEXT_REPOSITORY_DECISION=FROZEN_ARTIFACT_AUTHORITY_RECONCILIATION
NEXT_DECISION_AUTHORITY=SEPARATE_FOUNDER_AUTHORIZATION_REQUIRED
NEXT_DECISION_MUST_NOT_IMPLY_CONVERSION=YES
NEXT_DECISION_MUST_NOT_IMPLY_CONTAMINATION_ASSESSMENT_AUTHORITY=YES
```

Read-only public artifact research may inform that decision, but no new artifact bytes, conversion, contamination assessment, or execution authority is created by this closeout.
