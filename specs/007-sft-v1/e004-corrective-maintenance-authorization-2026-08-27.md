# E004 Corrective-Maintenance Authorization — 2026-08-27

**Spec:** 007 SFT V1
**Frontier:** E004 live tournament evidence
**Decision owner:** Founder
**Decision state:** `AUTHORIZED_BOUNDED_CORRECTIVE_MAINTENANCE`
**Canonical decision base:** `3807d6bb38bdd2e62c3731535b6823d5bf0b146a`
**Canonical decision base tree:** `82cce6c3092ff6d2e115d8118f7298c6a0ffbe71`
**Predecessor blocker record:** `specs/007-sft-v1/e004-prerequisite-frontier-2026-08-27.md`

## Decision

After the canonical E004 prerequisite-frontier audit identified a closed-Spec control-plane deadlock and the next required repository decision as a separately authorized corrective-maintenance repair, the Founder directed the project to continue on 2026-08-27 with:

> `go ahead`

That direction is interpreted narrowly as authorization of the **first dependency-safe decision only**: bounded corrective maintenance needed to repair the Spec 005 ↔ E004 pre-execution interface. It does not authorize later artifact/conversion, contamination-assessment, scientific-threshold, personnel/resource, spend, or E004 execution gates by implication.

```text
E004_CORRECTIVE_MAINTENANCE_AUTHORITY=AUTHORIZED
E004_EXECUTION_AUTHORITY=UNCHANGED_CONDITIONAL_E003_ONLY
MODEL_WEIGHT_ACCESS_AUTHORITY=UNCHANGED_E002_SCOPE_ONLY
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
BACKBONE_WINNER=NEEDS_EVIDENCE
```

## Authorized repair objective

Repair only the repository-internal defects already bound by the canonical E004 prerequisite-frontier record so that the control plane can represent a valid pre-execution state without requiring execution-derived evidence before first execution.

The repair MUST preserve fail-closed behavior and MUST NOT fabricate any real device, model, benchmark, contamination, clinical, statistical, personnel, access, finance, or runtime evidence.

### CM-1 — Break the device/A15 circular dependency

Current canonical behavior conflates two distinct states:

1. **pre-execution device readiness** — exact candidate artifact/runtime/build/tool/signal/protocol identities are frozen and execution may be considered if every other prerequisite passes;
2. **post-execution device qualification** — measured-run evidence exists and the candidate has passed or failed the frozen device qualification protocol.

The corrective repair is authorized to separate these states explicitly.

Required semantics:

```text
PRE_EXECUTION_DEVICE_READINESS_REQUIRES_MEASURED_RUNS=NO
POST_EXECUTION_DEVICE_QUALIFICATION_REQUIRES_MEASURED_RUNS=YES
MISSING_REQUIRED_PRE_EXECUTION_IDENTITY=BLOCKED_OR_INCOMPLETE
MISSING_REQUIRED_POST_EXECUTION_RUN=INCOMPLETE
OBSERVED_HARD_FAILURE=HARD_FAIL
CALLER_OWNED_PASS=NON_AUTHORITATIVE
```

A15/E004 pre-execution validation may depend only on the pre-execution readiness state. Tournament evidence publication/qualification may depend on the post-execution measured state.

No missing measurement may be treated as a post-execution PASS.

### CM-2 — Reconcile frozen device-contract contradictions

The repair is authorized to reconcile only already-frozen policy values and semantics, including:

- the frozen complete minimum text/Core bundle package envelope (`700 MiB` hard cap, `<=600 MiB` engineering target, `<=500 MiB` stretch target) with explicit scope so model-only bytes are not silently substituted for complete-bundle bytes;
- the frozen `FIVE_FRESH_RUNS_MEDIAN_WITH_WORST_CASE` rule with **no non-measured warm-up requests**;
- exact pre-execution runtime/build/tool/signal identity requirements already required by canonical Spec 005 decisions;
- any directly dependent validator/test shape necessary to make those semantics deterministic and fail closed.

The repair MUST NOT invent unresolved numeric latency, throughput, clinical-quality, statistical, thermal-ready, energy-calibration, or other thresholds.

### CM-3 — Add a bounded identity-bound E004 execution envelope

The repository currently has no canonical live E004 execution surface. This authorization permits a minimal E004-specific execution **envelope/adapter contract** sufficient to bind a future real invocation to:

- exact candidate and model-artifact identity;
- exact frozen E001/E002/E003 authority identities;
- exact A15 activation and pre-execution snapshot identity;
- exact runtime/build/executable identity;
- exact benchmark/evaluation input identity and permitted purpose;
- exact tokenizer/template/config identity where applicable;
- exact command/argument/environment projection required for reproducibility;
- exact raw-output/evidence artifact identities produced after execution.

Implementation tests MUST use synthetic/non-medical fixtures or injected fake runners only. The implementation/qualification PR MUST NOT execute a real model, benchmark payload, physical device, network/model download, or paid resource.

The adapter MUST fail closed unless the supplied pre-execution state is fully authorized and exact. It MUST NOT create new authority and MUST NOT bypass contamination, artifact, finance, access, or scientific gates.

Whether a future real invocation uses that adapter remains governed by E003 plus the then-current PASS preflight and all separate prerequisites.

## Authorized implementation surface

Corrective maintenance may change only the minimum required paths in these bounded families:

```text
data/spec005/device_qualification_contract.json
src/commandmed/spec005/device.py
src/commandmed/spec005/manifest.py
src/commandmed/spec005/activation.py          # only if directly required by CM-1 binding
src/commandmed/spec007/*e004*                 # minimal E004-specific envelope only
tests/spec005/test_device.py
tests/spec005/test_manifest.py
tests/spec005/test_activation.py              # only if directly required
tests/spec007/*e004*                           # synthetic/fake-runner only
specs/007-sft-v1/e004-*.md                    # evidence/reconciliation records only
specs/007-sft-v1/tasks.md
specs/README.md
```

No other Spec 005 scientific, provenance, personnel, access, finance, or tournament-comparison semantics may be weakened or redesigned merely to make E004 reachable.

## Explicitly not authorized

This decision does **not** authorize:

- downloading or acquiring any model/benchmark artifact beyond E002/E003's already-bound scope;
- expanding the E002 preconverted-artifact allowlist;
- model conversion, quantization, requantization, merging, or transformation;
- actual contamination assessment or benchmark-payload access needed to perform it;
- choosing clinical/statistical thresholds, margins, N, power, allocation, or reviewer identities;
- binding fabricated personnel/access/finance/device evidence;
- actual model inference, benchmark execution, or physical-device qualification during the corrective-maintenance implementation/qualification PR;
- E005 backbone selection;
- training or optimization;
- credentials, gated terms/assets, Private Gold, PHI, provider generation, or spend.

## Qualification gates

Corrective maintenance is not canonical merely because code exists. Before guarded merge, the exact implementation head must prove at minimum:

```text
BOUNDED_DIFF_SCOPE=PASS
DEVICE_PRE_EXECUTION_VS_POST_EXECUTION_STATES_SEPARATED=PASS
DEVICE_A15_CYCLE_REMOVED_WITHOUT_WEAKENING_POST_EXECUTION_GATE=PASS
FROZEN_PACKAGE_SCOPE_AND_VALUES_RECONCILED=PASS
NO_NON_MEASURED_WARMUP_SEMANTICS_RECONCILED=PASS
E004_EXECUTION_ENVELOPE_FAIL_CLOSED=PASS
NO_REAL_EXTERNAL_EXECUTION_DURING_QUALIFICATION=PASS
FOCUSED_TESTS=PASS
FULL_OFFLINE_REGRESSION=PASS
COMPILEALL=PASS
DIFF_CHECK=PASS
INDEPENDENT_EXACT_HEAD_REVIEW=MATERIAL_BLOCKER_NONE
```

No CI/review PASS may be claimed without exact-head evidence.

## Post-repair state

Even if corrective maintenance closes successfully:

```text
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT_OR_NEXT_EXPLICIT_PREREQUISITE
E004_EXECUTION_OCCURRED=NO
```

unless and until every separate prerequisite is actually resolved.

The next separate frontier after corrective-maintenance closure is expected to remain at least:

1. frozen executable-artifact authority reconciliation for candidates currently lacking an authorized GGUF path;
2. separate contamination-assessment access/execution authority and evidence;
3. real clinical/statistical threshold and design evidence;
4. exact runtime/build/device/personnel/access/finance evidence;
5. A1–A14 ready snapshot + separate A15 activation;
6. only then E004 live execution under E003.

## Authority integrity

```text
CORRECTIVE_MAINTENANCE_IS_EXECUTION_AUTHORITY=NO
CORRECTIVE_MAINTENANCE_IS_CONVERSION_AUTHORITY=NO
CORRECTIVE_MAINTENANCE_IS_CONTAMINATION_ASSESSMENT_AUTHORITY=NO
CORRECTIVE_MAINTENANCE_IS_TRAINING_AUTHORITY=NO
CORRECTIVE_MAINTENANCE_MAY_FABRICATE_PASS_EVIDENCE=NO
```

This decision authorizes repository repair only. It preserves the fail-closed E004 STOP until the remaining separately governed prerequisites are satisfied.