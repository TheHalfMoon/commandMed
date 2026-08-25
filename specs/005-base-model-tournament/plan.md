# Implementation Plan: Spec 005 — Base Model Tournament
> **Post-implementation reconciliation — 2026-08-25** — Control-plane implementation canonical at `5e35cd423c54ce743b9b305287971a97eeeb7a64` (PR #36). Planning branch `spec/005-clarify` and lifecycle claims below are historical evidence; implementation is now on `main`. No execution authority granted. See `tasks.md` reconciliation.



**Branch**: `spec/005-clarify` (planning carrier) | **Date**: 2026-08-24 | **Spec**: `specs/005-base-model-tournament/spec.md`

**Input**: Feature specification plus accepted clarification Sessions 1–14 and `clarification-closeout.md`.

**Plan status:** `REPAIRED_COMPLETE_READY_FOR_CHECKLIST_AND_TASKS`

## Summary

Build the deterministic, offline, identity-bound control plane required to prepare commandMed's baseline-only base-model tournament without downloading/executing models, benchmarks, Private Gold, PHI, provider APIs, paid services, or devices.

The implementation has two layers:

1. **A1 upstream corrective maintenance** — add metrics-v2 as an additive, versioned evaluation contract in a separate branch/PR while preserving historical V1 identities.
2. **Spec 005 preconstruction package** — implement pure validators/state machines for scientific quality/statistical design (A2+A3/A4), governance A5–A15, device/runtime protocol metadata, and a fail-closed adapter that can produce a Spec 004-compatible tournament manifest only after every required prerequisite identity is valid.

Actual case construction, model access, benchmark execution, device execution, spending and tournament execution remain outside this implementation plan until their separately frozen activation gates are satisfied.

## Technical Context

**Language/Version**: Python 3.11.

**Primary Dependencies**: Python standard library only; reuse `src/commandmed/eval_contract/*` and `src/commandmed/tournament.py`. No new third-party runtime dependency.

**Storage**: Canonical JSON policy/metadata files under `data/eval/` and `data/spec005/`; no database; no sensitive payload storage in Git.

**Testing**: `unittest`, deterministic synthetic/non-medical fixtures, `compileall`, full offline regression suite.

**Target Platform**: Repository-side offline validation library. Device-specific logic in this phase validates metadata/evidence contracts only; it does not execute iOS/Android/Linux model runtimes.

**Project Type**: Python library / research-governance validation layer.

**Performance Goals**: Deterministic results and stable canonical identities. Validators should remain simple bounded passes over small policy/manifests; no throughput target is needed for the control plane.

**Constraints**:

- no network requirement for tests or validation;
- no model/provider/device execution;
- no benchmark/Gold/PHI payload;
- current authorized spend `$0`;
- no mutable or caller-owned PASS/eligibility/authorization state accepted as authoritative;
- preserve Spec 001–004 historical V1 identities;
- no force-push/rebase/history rewrite;
- A1 must be implemented and merged in a separate corrective-maintenance PR before Spec 005 consumes metrics-v2;
- exact scientific thresholds/sample counts must be evidence-bound A2/A3+A4 records; implementation MUST NOT invent values;
- unresolved runtime/personnel/storage/vendor values remain fail-closed evidence prerequisites, not guessed defaults.

**Scale/Scope**: One additive metrics-v2 contract; one small `commandmed.spec005` package; three small canonical policy JSON files; focused fixture tests; no live asset registry/service.

## Constitution Check

*GATE: passed for planning; re-evaluated after Phase 1 design.*

| Constitution principle | Plan disposition |
|---|---|
| I. Evidence Before Training | PASS — threshold/statistical/evaluation contracts precede any future execution; no training in scope. |
| II. Clinical Safety Is a Hard Gate | PASS — seven noncompensable quality lanes and unresolved thresholds fail closed. |
| III. Provenance, Licensing, Data Lineage | PASS — source/rights/privacy/parent identities are mandatory inputs. |
| IV. Smallness Is Measured in Resources | PASS — named device/resource protocol is represented before execution. |
| V. Universal Roles, Shared Medical Truth | PASS — role and Arabic paired coverage remain explicit metadata dimensions. |
| VI. Hybrid Multimodal Intelligence | PASS — Spec 005 common-core ranking does not overclaim multimodal maturity. |
| VII. Deterministic Truth Boundaries | PASS — control-plane decisions are pure deterministic validators. |
| VIII. Holdout Quarantine | PASS — Private Gold is excluded from selection/training/source parentage. |
| IX. Reproducibility | PASS — exact hashes/revisions and immutable state-transition records required. |
| X. Capability Preservation | PASS — no specialization/training occurs; later regression obligations remain preserved. |
| XI. Defense in Depth | PASS — no patient-critical execution is introduced. |
| XII. Claims Integrity | PASS — valid outcome may remain `NO_SELECTION`; no SOTA/clinical claim. |
| XIII. Minimal Mechanism, Maximum Assurance | PASS — standard-library modules, no generic rule engine/service/database. |
| XIV. Bounded Spec Authority | PASS — A1, A7, A13, A14, A15 and live-execution boundaries remain explicit. |

No constitutional violation requires a complexity exception.

## Project Structure

### Documentation (this feature)

```text
specs/005-base-model-tournament/
├── spec.md
├── clarification-closeout.md
├── research.md
├── plan.md
├── data-model.md
├── quickstart.md
├── contracts/
│   └── preconstruction-control-contract.md
├── checklists/
│   └── implementation-readiness.md
├── tasks.md
└── jetbrains-handoff.md
```

Historical `session-*-q*.md` and discovery/evidence files remain detailed rationale/evidence and are not separate implementation queues.

### Source Code

```text
src/commandmed/
├── eval_contract/
│   ├── __init__.py
│   ├── canonical.py
│   ├── model.py
│   └── validate.py
├── tournament.py
└── spec005/
    ├── __init__.py
    ├── science.py
    ├── preconstruction.py
    ├── personnel.py
    ├── access.py
    ├── finance.py
    ├── device.py
    ├── activation.py
    └── manifest.py

data/
├── eval/
│   ├── metrics.json                    # immutable V1
│   └── metrics-v2.json                 # A1 additive artifact
└── spec005/
    ├── selection_quality_contract.json # A2 + A3/A4 + seven lanes
    ├── preconstruction_contract.json   # A5–A13 metadata/governance vocabularies
    └── device_qualification_contract.json

tests/
├── eval_contract/
│   └── test_metrics_v2.py
├── test_tournament_metrics_v2_identity.py
└── spec005/
    ├── __init__.py
    ├── test_science.py
    ├── test_preconstruction.py
    ├── test_personnel.py
    ├── test_access.py
    ├── test_finance.py
    ├── test_device.py
    ├── test_activation.py
    └── test_manifest.py
```

**Structure Decision**: Extend the existing single Python package. `science.py` isolates scientific metric/estimand/threshold/statistical-allocation logic from source/personnel/access/finance governance. The remaining modules correspond directly to frozen governance boundaries. Do not create services, plugin systems, databases, workflow engines, or model-runtime wrappers in this bounded implementation.

## Phase 0 Result — Research

`research.md` resolves implementation architecture choices. No implementation-level `NEEDS CLARIFICATION` remains.

Values that require later evidence — exact clinical thresholds, sample counts, personnel roster, storage implementation, llama.cpp SHA/builds/signals, candidate artifacts, contamination results — are represented as blocked prerequisite records and are deliberately not guessed during planning.

## Phase 1 Design

### 1. A1 — additive metrics-v2 predecessor

A1 is a separate corrective-maintenance implementation from live canonical `main`.

Required path budget:

```text
ADD    data/eval/metrics-v2.json
MODIFY src/commandmed/eval_contract/model.py
MODIFY src/commandmed/eval_contract/validate.py
MODIFY src/commandmed/eval_contract/canonical.py
MODIFY src/commandmed/eval_contract/__init__.py
MODIFY src/commandmed/tournament.py
ADD    tests/eval_contract/test_metrics_v2.py
ADD    tests/test_tournament_metrics_v2_identity.py
MODIFY docs/evaluation/tournament-harness.md
ADD    specs/001-eval-charter/corrective-maintenance-metrics-v2.md
```

Hard invariant:

```text
V1_METRICS_SHA256=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
```

`data/eval/metrics.json` MUST remain byte/identity compatible with historical evidence. A1 is not implemented on the Spec 005 planning branch.

### 2. Scientific selection contract — A2 + atomic A3/A4

`science.py` + `data/spec005/selection_quality_contract.json` implement the scientific contract that was missing from the first planning draft.

The contract freezes machine-verifiable structure for:

- seven required noncompensable quality lanes A–G;
- metric/evidence-role mapping through metrics-v2;
- intended-use role/language/use-context and required strata identities;
- per-claim estimand, unit of analysis, metric direction and decision role;
- clinical threshold/margin identity and qualified-review reference;
- precision/power objective, confidence/error parameters and nuisance assumptions;
- paired Arabic parity and root-case dependency;
- multiplicity declaration;
- exact sample-size/allocation record identity;
- candidate-neutral planning and post-result mutation prohibition.

The implementation validates **records**, not scientific values. If an exact threshold/margin/N or review identity required for PASS is absent, the result is `BLOCKED`/`INCOMPLETE`; no default value is supplied.

A3 and A4 remain one atomic statistical/allocation record because total N and allocation across required anchors/roles/strata cannot be chosen independently.

### 3. Preconstruction policy core — A5/A6/A8/A9/A10/A11/A12

`preconstruction.py` validates:

- contributor/content rights evidence;
- non-PHI authoring attestations;
- author/reviewer/adjudicator separation;
- source-route and parent-derivation constraints;
- metadata-only case/pair provenance envelopes;
- contamination-plan identity and evidence readiness (not contamination execution);
- material-change/new-identity semantics;
- dependency/staleness relationships.

`data/spec005/preconstruction_contract.json` contains only closed vocabularies/invariants. No case payload belongs there.

### 4. Personnel governance — A7

`personnel.py` implements pure record validation/state transitions for opaque identity, role-scoped qualification, conflicts, Gold exposure, assignment, independence, result exposure, bootstrap readiness and A7→A13 signals. It never creates a personnel vault or ingests credentials.

### 5. Payload/result access boundary — A13

`access.py` validates the three-zone policy, A7 handshake, role incompatibilities, revoke/revalidation signals, export/copy restrictions and audit-record shape. It does not provision storage or grant real filesystem/cloud access.

### 6. Spend/engagement governance — A14

`finance.py` implements pure validation for workload/requirement manifests, precommitment authorization identity, financial separation of duties, payee/vendor conflict, authorization lifecycle/supersession, dual PASS modes and staleness. It never performs a payment, contract, reimbursement, vendor call or provisioning action.

### 7. Device/runtime qualification contract

`device.py` + `data/spec005/device_qualification_contract.json` represent the frozen five targets, 8K/16K protocol, Q8_0 KV, token/batch/cache profile, five fresh runs, memory/timing/thermal/energy evidence, package-size boundaries, immutable runtime/build identity requirements and fatal/incomplete semantics. The module validates metadata only.

### 8. A15 activation record

`activation.py` validates an immutable prerequisite snapshot. A real activation must bind current PASS identities for A1–A14, including the scientific A2/A3+A4 record, and fail on blocked/stale/mismatched evidence. Synthetic activation fixtures test semantics only and never create canonical authority.

### 9. Spec 005 tournament manifest adapter

`manifest.py` builds/validates a Spec 005 pre-execution manifest and emits a Spec 004-compatible projection only when exact metrics-v2, scientific quality/statistical, governance, device and activation identities satisfy the contract.

It MUST NOT download/load weights, access benchmark payloads, execute candidates/devices, infer missing thresholds/N, admit Private Gold as selection evidence, or select a winner from fabricated/partial evidence.

## Interface Contracts

The internal interfaces are specified in `contracts/preconstruction-control-contract.md`. Prefer plain dictionaries, closed string vocabularies, small enums/frozensets where helpful, and pure functions returning deterministic error/reason lists or result dictionaries.

## Data Model

`data-model.md` defines scientific, governance, access, finance, device, activation and manifest entities. Canonical identity is SHA-256 over explicit scientific/governance projections; timestamps/local paths/workstation details are excluded unless explicitly identity-bearing.

## Verification Strategy

TDD is required for high-risk validators/state machines.

```text
python -m compileall -q src tests
python -m unittest tests.eval_contract.test_metrics_v2 -v
python -m unittest tests.test_tournament_metrics_v2_identity -v
python -m unittest tests.spec005.test_science -v
python -m unittest discover -s tests/spec005 -v
python -m unittest discover -s tests -v
```

All tests use synthetic/non-medical fixture metadata. No test may require network, model weights, benchmark/Gold payload, provider credentials, PHI, device runtime, payment instrument or paid service.

## Delivery / Branch Strategy

1. Finish this planning PR and obtain planning review/closeout as governed.
2. **A1 first:** create a new corrective-maintenance branch from then-live canonical `main`; implement only the frozen A1 path budget; qualify/review/merge; verify new `main`.
3. Create/continue a Spec 005 implementation branch from current canonical main after A1.
4. Implement `tasks.md` in dependency order using small commits.
5. Stop at any authority gate instead of substituting synthetic evidence for real prerequisite evidence.
6. Run full offline verification and independent exact-head review before implementation merge.
7. Construction/model/device/tournament execution requires later explicit activation and is not part of this code-build plan.

No force-push or rebase is needed. If canonical `main` advances, reconcile by ordinary non-destructive merge where necessary and requalify the exact resulting head.

## Implementation Slices Used by `tasks.md`

The current Spec 005 is governance/decision-centric rather than a persona UI feature. Spec Kit tasks use these derived engineering delivery stories; they add no product requirements:

- **US1 — Additive Metrics V2 Without Breaking V1**
- **US2 — Scientific Quality, Threshold and Statistical Design**
- **US3 — Preconstruction Evidence and Source Governance**
- **US4 — Personnel Governance**
- **US5 — Payload and Candidate-Result Access Firewall**
- **US6 — Spend and Engagement Governance**
- **US7 — Construction Activation, Device Protocol and Tournament Manifest**

Each slice is independently fixture-testable and traceable to frozen clarification decisions.

## Post-Design Constitution Re-check

PASS. The repaired design explicitly covers A2/A3+A4 and the seven quality lanes while remaining offline, deterministic, standard-library-first, fixture-only, fail-closed, identity-bound, Gold-quarantined and bounded.

## Complexity Tracking

No constitution violation requires justification. The eight-module `spec005` package is the minimum separation needed to avoid conflating scientific threshold/statistical logic with source governance, personnel, access, finance, device protocol and activation state.