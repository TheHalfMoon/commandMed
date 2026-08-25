# Spec 005 — Planning Research

**Status:** `COMPLETE`
**Purpose:** Phase 0 Spec Kit research consolidation for the Base Model Tournament.

This file condenses the accepted clarification archive into implementation decisions. Historical clarification artifacts remain the detailed evidence record; this file is the implementation-facing rationale index.

## Decision 1 — Keep implementation deterministic, offline, and standard-library-first

**Decision:** Implement Spec 005 planning-stage machinery in Python 3.11 using the standard library and the repository's existing `commandmed` evaluation/tournament primitives. Do not add runtime frameworks, databases, services, model SDKs, provider clients, device-execution libraries, or new third-party dependencies.

**Rationale:** The active scope is validation, identity binding, governance state machines, manifest construction, and fail-closed prerequisite evaluation. Existing Specs 001–004 already use deterministic JSON metadata, canonical hashing, fixture tests, `unittest`, and pure evaluators. The constitution's Minimal Mechanism / Maximum Assurance principle prefers the smallest mechanism that preserves safety, provenance, reproducibility and auditability.

**Alternatives considered:**
- Generic policy/rule engine — rejected as unnecessary abstraction.
- Database-backed workflow service — rejected because no live multi-user control plane is authorized.
- Pydantic/JSON-Schema framework — rejected unless a concrete implementation task proves the existing hand-written validators cannot satisfy the bounded contract.

## Decision 2 — A1 metrics-v2 is an upstream additive corrective-maintenance PR

**Decision:** Implement metrics-v2 in a separate corrective-maintenance branch/PR from live canonical `main`. Preserve `data/eval/metrics.json` and its historical SHA-256 exactly. Spec 005 code may consume metrics-v2 only after A1 is merged and canonical `main` is reverified.

**Rationale:** The existing V1 metrics identity is embedded in historical Spec 004 evidence. In-place reinterpretation would break reproducibility. The accepted preflight defines a minimal additive V2 contract with evidence-role semantics.

**Alternatives considered:**
- Edit V1 in place — prohibited by frozen governance.
- Add Spec 005-only ad-hoc metric names — rejected because it duplicates canonical evaluation authority.
- Let Spec 005 infer a metric from benchmark names — prohibited; metric identity must be explicit.

## Decision 3 — Build one bounded `commandmed.spec005` package

**Decision:** Add a small package with direct domain modules:

```text
src/commandmed/spec005/
  __init__.py
  preconstruction.py
  personnel.py
  access.py
  finance.py
  device.py
  activation.py
  manifest.py
```

**Rationale:** These modules map directly to frozen A5–A15 responsibility boundaries and keep high-risk concerns separated without introducing a framework. `manifest.py` is the adapter into the existing Spec 004 tournament harness; it does not execute a tournament.

**Alternatives considered:**
- Put all new logic in `tournament.py` — rejected because personnel/access/finance/preconstruction policy would make the existing harness monolithic.
- One class per policy — rejected as class-hierarchy overengineering.
- Multiple services/packages — rejected; the bounded package is sufficient.

## Decision 4 — Store policy contracts, never sensitive payloads

**Decision:** Canonical repository data for Spec 005 is metadata/policy only. Use small JSON contracts under `data/spec005/` for closed vocabularies and frozen policy defaults. Do not commit selection case text, answers/rubrics, Private Gold content, PHI, personnel credentials, candidate outputs, model weights, or provider payloads.

**Rationale:** Sessions 10–13 freeze metadata/payload separation, opaque personnel references, non-PHI authoring and a three-zone access model. Public Git is not a payload vault.

**Alternatives considered:**
- Store synthetic cases in Git immediately — rejected because A15 construction is not activated.
- Store protected personnel evidence in Git — prohibited.
- Store direct unauthenticated payload locators — prohibited by A13.

## Decision 5 — Model every unresolved scientific/runtime value as a prerequisite, not a default

**Decision:** Exact thresholds, sample counts, runtime SHA, build identities, device signal identities, personnel roster, storage implementation and contamination results remain typed unresolved prerequisite fields until their evidence exists. Validators return `BLOCKED`/`INCOMPLETE`; they never insert guessed values.

**Rationale:** Clarification is complete because the method for resolving these values is frozen. The actual values depend on later evidence/authorization and therefore are not design ambiguity.

**Alternatives considered:**
- Choose plausible defaults so implementation can continue — rejected as scientifically invalid and contrary to fail-closed governance.
- Leave free-text TODOs — rejected because JetBrains needs machine-verifiable states.

## Decision 6 — Preconstruction is a prerequisite graph, not a boolean checklist

**Decision:** Implement dependency-aware validation for A1–A15. A1 is upstream. A3+A4 is one atomic statistical/allocation node. A5/A6/A8/A12 can be implemented as governance contracts in parallel; A9/A10/A11 depend on those design identities; A7/A13/A14 have separate state/evidence dependencies; A15 is a separate activation record after current prerequisite identities pass.

**Rationale:** The frozen DAG prevents circular authoring/sample-size decisions and prevents a single aggregate `ready=true` from laundering stale prerequisites.

**Alternatives considered:**
- One mutable readiness flag — rejected because it cannot represent identity/staleness.
- Linear A1→A14 sequence — rejected because independent governance work can progress safely in parallel.

## Decision 7 — Personnel, access, and finance are independent state machines

**Decision:** Keep A7 personnel eligibility/assignment, A13 resource access, and A14 financial authority separate. Cross-domain transitions occur through identity-bound signals/references only.

**Rationale:** Qualification must not imply assignment, assignment must not imply payload access, and payment must not imply scientific authority. This also makes revocation/staleness deterministic.

**Alternatives considered:**
- One global `person_status` or `approved` field — rejected as privilege conflation.
- Founder/admin override path — rejected for scientific qualification, Gold exposure, independence, and conflict decisions.

## Decision 8 — Device protocol implementation is metadata validation only in this build phase

**Decision:** Implement deterministic validation of the frozen device/runtime protocol: five targets, context/KV/batch profile, memory cap, timing/thermal/energy evidence schema, run-count/failure semantics, package-size boundaries, and immutable runtime/build identities. Do not run llama.cpp, quantize models, access weights, or execute devices.

**Rationale:** The protocol is sufficiently clarified to build validators, but actual runtime/artifact binding and device evidence require separate execution authority.

**Alternatives considered:**
- Skip device logic until models are available — rejected because predeclared contracts must precede execution.
- Execute small smoke models — outside current authority.

## Decision 9 — Reuse the Spec 004 tournament harness through an adapter

**Decision:** `manifest.py` constructs/validates a Spec 005 pre-execution manifest and only emits a Spec 004-compatible comparison manifest when every required identity and hard prerequisite is valid. It never invokes a model or benchmark.

**Rationale:** Spec 004 already owns deterministic comparison/no-selection behavior and canonical artifact bindings. Spec 005 should extend eligibility evidence, not fork the harness.

**Alternatives considered:**
- New tournament engine — rejected as duplicate logic.
- Modify Spec 004 historical semantics — prohibited.

## Decision 10 — Tests are fixture-only and TDD-oriented

**Decision:** Add focused `unittest` coverage before each implementation slice, using synthetic/non-medical metadata fixtures. Required verification remains offline:

```text
python -m compileall -q src tests
python -m unittest tests.eval_contract.test_metrics_v2 -v
python -m unittest tests.test_tournament_metrics_v2_identity -v
python -m unittest discover -s tests/spec005 -v
python -m unittest discover -s tests -v
```

**Rationale:** Safety/provenance/governance code needs negative-path proof and historical V1 regression protection. Fixture-only tests respect all current access boundaries.

**Alternatives considered:**
- Live model/provider tests — unauthorized.
- Device integration tests — deferred to separately authorized execution.

## Decision 11 — JetBrains executes `tasks.md`, not the clarification archive

**Decision:** The implementation agent reads the canonical governing files, then executes exactly one unchecked task at a time from `tasks.md`. Historical clarification files are rationale/evidence, not an independent work queue.

**Rationale:** The clarification archive is intentionally detailed but too fragmented for efficient implementation. A single dependency-ordered task list makes progress auditable and prevents accidental scope expansion.

## Resolved planning unknowns

No `NEEDS CLARIFICATION` remains for the implementation architecture. Values that depend on later scientific, personnel, runtime, financial, payload, device or execution evidence are explicit prerequisite records and remain fail-closed until separately satisfied.