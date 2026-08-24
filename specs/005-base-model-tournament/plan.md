# Implementation Plan: Spec 005 — Base Model Tournament

**Branch**: `spec/005-clarify` (planning carrier) | **Date**: 2026-08-24 | **Spec**: `specs/005-base-model-tournament/spec.md`

**Input**: Feature specification plus accepted clarification Sessions 1–14 and `clarification-closeout.md`.

**Plan status:** `COMPLETE_READY_FOR_CHECKLIST_AND_TASKS`

## Summary

Build the deterministic, offline, identity-bound control plane required to prepare commandMed's baseline-only base-model tournament without downloading/executing models, benchmarks, Private Gold, PHI, provider APIs, paid services, or devices.

The implementation has two layers:

1. **A1 upstream corrective maintenance** — add metrics-v2 as an additive, versioned evaluation contract in a separate branch/PR while preserving historical V1 identities.
2. **Spec 005 preconstruction package** — implement pure validators/state machines for A5–A15, device/runtime protocol metadata, and a fail-closed adapter that can produce a Spec 004-compatible tournament manifest only after every required prerequisite identity is valid.

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
- unresolved scientific/runtime/personnel values remain fail-closed evidence prerequisites, not guessed defaults.

**Scale/Scope**: One additive metrics-v2 contract; one small `commandmed.spec005` package; two small canonical policy JSON files; focused fixture tests; no live asset registry/service.

## Constitution Check

*GATE: passed for planning; re-evaluated after Phase 1 design.*

| Constitution principle | Plan disposition |
|---|---|
| I. Evidence Before Training | PASS — thresholds/evaluation contracts precede any future execution; no training in scope. |
| II. Clinical Safety Is a Hard Gate | PASS — noncompensable safety/quality gates and unresolved thresholds fail closed. |
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
    ├── preconstruction.py
    ├── personnel.py
    ├── access.py
    ├── finance.py
    ├── device.py
    ├── activation.py
    └── manifest.py

data/
├── eval/
│   ├── metrics.json              # immutable V1
│   └── metrics-v2.json           # A1 additive artifact
└── spec005/
    ├── preconstruction_contract.json
    └── device_qualification_contract.json

tests/
├── eval_contract/
│   └── test_metrics_v2.py
├── test_tournament_metrics_v2_identity.py
└── spec005/
    ├── __init__.py
    ├── test_preconstruction.py
    ├── test_personnel.py
    ├── test_access.py
    ├── test_finance.py
    ├── test_device.py
    ├── test_activation.py
    └── test_manifest.py
```

**Structure Decision**: Extend the existing single Python package. Each Spec 005 module corresponds to one frozen governance boundary. Do not create services, plugin systems, databases, workflow engines, or model-runtime wrappers in this bounded implementation.

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

### 2. Preconstruction policy core — A5/A6/A8/A9/A10/A11/A12

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

### 3. Personnel governance — A7

`personnel.py` implements pure record validation/state transitions for:

- opaque personnel references;
- identity verification state;
- role-scoped qualification eligibility;
- conflicts and Gold-exposure dispositions;
- assignment state;
- reviewer/adjudicator independence;
- result-exposure transition restrictions;
- bootstrap/steady-state evidence readiness;
- signals consumed by A13.

It stores/validates references to protected evidence; it does not create a personnel vault or ingest credentials.

### 4. Payload/result access boundary — A13

`access.py` validates the three-zone policy and A7→A13 handshake:

- metadata/governance references;
- selection-content access grants;
- candidate-result access grants;
- role incompatibilities;
- revoke/revalidation signals;
- export/copy restrictions;
- audit-record shape.

It does not provision storage or grant real filesystem/cloud access.

### 5. Spend/engagement governance — A14

`finance.py` implements pure policy/state validation for:

- requirement/workload manifest shape;
- `NOT_REQUIRED` / `REQUIRED` / blocked disposition evidence;
- precommitment authorization identity;
- approval/payment/reconciliation separation;
- payee/vendor conflicts;
- authorization lifecycle and material supersession;
- `A14_NOT_REQUIRED_PASS` and `A14_AUTHORIZED_PASS` evidence;
- staleness/revalidation.

It never performs a payment, contract, reimbursement, vendor call, or provisioning action.

### 6. Device/runtime qualification contract

`device.py` + `data/spec005/device_qualification_contract.json` represent the already-frozen protocol:

- five target classes;
- 8K core and 16K stress applicability;
- Q8_0 symmetric KV;
- prompt/generation budgets;
- B512/U128 cold/no-reuse profile;
- five fresh measured runs, median + worst evidence;
- platform-native peak-memory semantics and 2 GiB core hard cap;
- timing decomposition;
- thermal-ready and energy-required evidence shape;
- package-size hard/target/stretch boundaries;
- immutable runtime/platform build identity requirements;
- fatal vs incomplete failure semantics.

The module validates metadata only. Actual llama.cpp/model/device execution is out of scope.

### 7. A15 activation record

`activation.py` validates an immutable prerequisite snapshot for construction activation. A valid activation object must bind current identities for all required A1–A14 gates and fail if any dependency is blocked, stale or identity-mismatched.

The module may validate a synthetic fixture that represents `AUTHORIZED_TO_CONSTRUCT`, but the repository MUST NOT create a real activation record without separate explicit founder authorization after real prerequisites pass.

### 8. Spec 005 tournament manifest adapter

`manifest.py` builds/validates the pre-execution Spec 005 manifest from exact prerequisite records and delegates comparison semantics to existing `commandmed.tournament` contracts.

It MUST NOT:

- download/load model weights;
- access benchmark payloads;
- execute candidate inference;
- run device tests;
- infer missing scientific thresholds;
- admit Private Gold as selection evidence;
- select a winner from fabricated/partial evidence.

A blocked/incomplete prerequisite produces a deterministic non-executable preflight disposition.

## Interface Contracts

The internal record/validator contract is specified in `contracts/preconstruction-control-contract.md`. The implementation should prefer plain dictionaries, frozen string vocabularies, small enums/frozensets where helpful, and pure functions returning deterministic error/reason lists or immutable-style result dictionaries.

## Data Model

`data-model.md` defines the exact entities, relationships and state transitions. Canonical identity is SHA-256 over explicit scientific/governance projections; timestamps/local paths/reviewer workstation details do not silently alter scientific identity unless a policy explicitly says they are identity-bearing.

## Verification Strategy

TDD is required for the high-risk validators/state machines.

Focused validation order:

```text
python -m compileall -q src tests
python -m unittest tests.eval_contract.test_metrics_v2 -v
python -m unittest tests.test_tournament_metrics_v2_identity -v
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
6. Run full offline verification and independent exact-head review before any implementation merge.
7. Construction/model/device/tournament execution requires later explicit activation and is not part of this code-build plan.

No force-push or rebase is needed. If canonical `main` advances, reconcile by ordinary non-destructive merge where necessary and requalify the exact resulting head.

## Implementation Slices Used by `tasks.md`

The existing Spec 005 document is governance/decision-centric rather than a persona UI feature. For Spec Kit task organization, the following **delivery stories** are derived directly from frozen requirements; they are engineering increments, not new product requirements:

- **US1 — Additive Metrics V2 Without Breaking V1**
- **US2 — Preconstruction Evidence and Source Governance**
- **US3 — Personnel Governance**
- **US4 — Payload and Candidate-Result Access Firewall**
- **US5 — Spend and Engagement Governance**
- **US6 — Construction Activation, Device Protocol and Tournament Manifest**

Each slice is independently fixture-testable and traceable to accepted clarification artifacts.

## Post-Design Constitution Re-check

PASS. The design remains offline, deterministic, standard-library-first, fixture-only, fail-closed, identity-bound, Gold-quarantined and bounded. It adds no training/model/provider/device/payment authority and preserves historical V1 evidence.

## Complexity Tracking

No constitution violation requires justification. The seven-module `spec005` package is the minimum separation needed to avoid conflating scientific eligibility, personnel governance, access control, financial authority, device protocol and activation state.