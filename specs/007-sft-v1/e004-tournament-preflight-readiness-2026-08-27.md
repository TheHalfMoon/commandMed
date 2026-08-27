# E004 Tournament Preflight Readiness — 2026-08-27

**Spec:** 007 SFT V1
**Task:** E004
**Assessment type:** fail-closed pre-execution readiness audit
**Canonical base:** `ee56cf25e9c73d64b63e24814e32c00f0ba7c42e`
**Canonical base tree:** `4d191bf63eeae7cf67fcc67fa653c60e9a7c080e`
**E003 state at audit start:** `CLOSED_CANONICAL`
**Execution performed:** `NO`

## Decision

E003 provides the separate Founder authority required for bounded live-tournament execution, but the current canonical repository does **not** satisfy the existing Spec 005/007 A15/preflight prerequisites required before E004 may load a model, access a benchmark payload, or execute device qualification.

```text
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_STARTED=NO
MODEL_LOADED=NO
BENCHMARK_PAYLOAD_ACCESSED=NO
DEVICE_EXECUTION_STARTED=NO
TOURNAMENT_RESULT_CREATED=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

This is a readiness finding, not a revocation of E003. E003 remains the execution-authority overlay, but its own fail-closed rule makes PASS preflight a necessary condition for E004 execution.

## Canonical authority state preserved

```text
E003=CLOSED_CANONICAL
MODEL_WEIGHT_ACCESS_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
MODEL_EXECUTION_AUTHORITY=AUTHORIZED_E003_FROZEN_TOURNAMENT_ONLY
TOURNAMENT_EXECUTION_AUTHORITY=AUTHORIZED_E003_FROZEN_PROTOCOL_ONLY
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_E003_A15_BOUND_PUBLIC_TOURNAMENT_INPUTS_ONLY
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=AUTHORIZED_E003_A15_BOUND_PUBLIC_TOURNAMENT_INPUTS_ONLY
DEVICE_EXECUTION_AUTHORITY=AUTHORIZED_E003_FROZEN_TOURNAMENT_QUALIFICATION_ONLY
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
BACKBONE_WINNER=NEEDS_EVIDENCE
```

## Evidence audited

The audit inspected current canonical repository structure and the governing control-plane contracts rather than accessing external model or benchmark bytes.

### 1. Current canonical data inventory

The recursive canonical tree at `4d191bf63eeae7cf67fcc67fa653c60e9a7c080e` contains exactly three files under `data/spec005/`:

```text
data/spec005/device_qualification_contract.json
data/spec005/preconstruction_contract.json
data/spec005/selection_quality_contract.json
```

These are policy/control-plane contracts. The canonical tree contains no separate real E004/A15 activation record, no real preconstruction snapshot, no real tournament manifest, no real candidate-admission record set, no real per-metric threshold record set, no real statistical-design record set, and no real device preflight PASS evidence artifact.

### 2. A15 activation requirement

`src/commandmed/spec005/manifest.py` is fail closed. A real projection requires an identity-bearing construction activation tied to the exact ready preconstruction snapshot. Absence of that activation produces the canonical reason:

```text
PROJECTION:A15_REAL_ACTIVATION_NOT_AUTHORIZED
```

The repository contains schemas/validators and synthetic tests for this boundary, but no real canonical activation record satisfying it.

### 3. Threshold/statistical readiness

The canonical Session 9 Q5 threshold-freeze readiness matrix records:

```text
HARD_GATE_POPULATION_THRESHOLDS_READY_TO_FREEZE=0
HARD_GATE_POPULATION_THRESHOLDS_NOT_READY_TO_FREEZE=6
BENIGN_CASE_OVER_TRIAGE_THRESHOLD_READY_TO_FREEZE=NO
```

It also records unresolved exact identity-bound evaluation suites, reviewer authorities, statistical methods/numeric inputs, sample-size/power derivations, and canonical governance adoption for the relevant population thresholds. Architecture and validator availability therefore do not constitute frozen execution thresholds.

### 4. Benchmark contamination / selection eligibility

The current canonical quarantine registry records public benchmark contamination states as `NOT_ASSESSED`. The E001/E003 boundary also preserves:

```text
PRIMARY_BENCHMARK_SELECTION_ELIGIBILITY=INCOMPLETE
BENCHMARK_CONTAMINATION_BLOCKS_SELECTION_USE_UNTIL_RESOLVED=YES
```

E003 explicitly forbids using contamination-unresolved benchmark evidence as selection-bearing tournament input. No current canonical assessment upgrades that state to PASS.

### 5. Device/runtime execution binding

`data/spec005/device_qualification_contract.json` defines the five-target device protocol, but it is a metadata-only contract rather than real qualification evidence. It requires exact runtime/build identities and says exact values are resolved before execution, not by the contract. It also still carries unresolved execution values such as the Windows primary memory method and null package-boundary fields in that contract projection. No separate current device preflight artifact with `PREFLIGHT_PASS` is present in canonical data.

### 6. Tournament manifest / candidate admission

The Spec 005 manifest validator requires exact identity-bound manifest, candidate-admission, scientific, device, activation, and access evidence. Current canonical data contains the validators/contracts but no real E004 tournament manifest and no real candidate-admission record set. E001 freezes membership, but membership freeze is not a replacement for the execution-time admission/evidence records required by the tournament preflight.

## Fail-closed blocker matrix

| Gate | Current canonical evidence | State | Reason |
|---|---|---|---|
| E003 execution authority | E003 canonical closure record | `PASS` | authority exists, subject to preflight |
| Frozen candidate identity | E001 manifest version/SHA/blob + E002/E003 overlays | `PASS` | exact candidate membership/revisions are frozen |
| Real A15/construction activation identity | no real canonical activation record found | `BLOCKED` | `E004_A15_REAL_ACTIVATION_RECORD_ABSENT` |
| Real ready preconstruction snapshot | policy contract and validators only | `BLOCKED` | `E004_REAL_PRECONSTRUCTION_SNAPSHOT_ABSENT` |
| Real tournament manifest | no canonical real E004 manifest found | `BLOCKED` | `E004_TOURNAMENT_MANIFEST_ABSENT` |
| Candidate-admission evidence set | no real candidate-admission records found | `BLOCKED` | `E004_CANDIDATE_ADMISSION_RECORDS_ABSENT` |
| Exact population hard-gate thresholds | Q5 says 0/6 ready to freeze | `BLOCKED` | `E004_HARD_GATE_THRESHOLDS_NOT_FROZEN` |
| Exact statistical design / sample-size identities | architecture exists; exact numeric derivations unresolved | `BLOCKED` | `E004_STATISTICAL_DESIGN_NOT_FROZEN` |
| Benchmark contamination eligibility | canonical quarantine records `NOT_ASSESSED`; selection eligibility incomplete | `BLOCKED` | `E004_SELECTION_CONTAMINATION_UNRESOLVED` |
| Exact selection-bearing benchmark payload binding | no qualified E004/A15 input manifest exists | `BLOCKED` | `E004_SELECTION_INPUT_MANIFEST_ABSENT` |
| Device/runtime preflight evidence | device protocol contract exists; no real PASS record | `BLOCKED` | `E004_DEVICE_PREFLIGHT_EVIDENCE_ABSENT` |
| Exact runtime/build identity | contract requires later exact binding; no real run binding found | `BLOCKED` | `E004_RUNTIME_BUILD_IDENTITY_ABSENT` |
| Zero-spend boundary | E003/current authority has spend `NONE`, authorized USD `0` | `PASS_WITH_CONSTRAINT` | execution may not incur spend |

Because these gates are noncompensable, any one blocker is sufficient to forbid E004 execution. Multiple independent blockers are present.

## Why no tournament was executed

The E003 authorization record states that any `BLOCKED`, `INCOMPLETE`, `NEEDS_EVIDENCE`, stale, mismatched, or unauthorized prerequisite fails closed before first model call, first benchmark payload access, or first device-qualification execution.

Executing now would therefore violate the canonical protocol by turning missing evidence into implicit PASS. This audit intentionally did not:

- download or load model weights;
- access benchmark payload bytes;
- run inference;
- open a device qualification run;
- construct an ad hoc evaluation suite;
- invent clinical/statistical thresholds;
- infer contamination clearance;
- select or recommend a backbone;
- spend money;
- train or convert a model.

## Minimum evidence needed to unblock E004

E004 can be reconsidered only after identity-bearing canonical evidence resolves all applicable preflight blockers. At minimum the exact run must have:

1. a real preconstruction snapshot whose required dependencies are complete and whose readiness state permits separate activation;
2. a real A15/construction activation identity bound to that exact snapshot and current canonical commit;
3. a real tournament manifest for the exact frozen E001 candidates and permitted artifacts;
4. exact candidate-admission evidence records accepted by the canonical validator;
5. identity-bound public/ungated selection inputs with Spec 003 provenance/license evidence;
6. contamination assessment sufficient for selection use for every selection-bearing source;
7. frozen hard-gate threshold records and exact clinical/statistical authority evidence required by the frozen policy;
8. frozen statistical design/sample-size/power identities where required;
9. exact runtime/build identity and device-preflight evidence satisfying the frozen device protocol;
10. finance/access state proving the entire run remains within current zero-spend/no-credential/no-gated-asset authority.

Nothing in this blocker record authorizes fabricating those records. Where a prerequisite requires real external evidence, authorized evidence collection must occur under the relevant existing authority and remain fail closed.

## E005 boundary

```text
E004_COMPLETE=NO
TOURNAMENT_EVIDENCE_PACK=NOT_PRODUCED
E005_REACHABLE=NO
E005_OWNER=FOUNDER+CHATGPT
BACKBONE_WINNER=NEEDS_EVIDENCE
```

No candidate may be ranked as the final winner from static E001 metadata, E003 authority, synthetic control-plane tests, or this preflight audit.

## Exit Evidence

This readiness audit may close as a canonical **blocked-state evidence record** when:

- the exact canonical base/tree is verified;
- the current canonical inventory and governing preflight contracts are cited in this record;
- E004 remains unchecked in `tasks.md` and is marked `BLOCKED_PREFLIGHT` with this evidence path;
- the repository current-state summary distinguishes `E004_AUTHORITY=AUTHORIZED_BY_E003_SUBJECT_TO_PREFLIGHT` from `E004_STATE=BLOCKED_PREFLIGHT`;
- exact-head independent review finds no material blocker in the audit itself;
- no model, benchmark, device, training, credential, gated-asset, or spend execution occurs on the audit branch.

Canonicalizing this record does **not** close E004. It records why E004 is not currently executable.

## Current frontier

```text
E001=CLOSED_CANONICAL
E002=CLOSED_CANONICAL
E003=CLOSED_CANONICAL
E004=BLOCKED_PREFLIGHT
E004_EXECUTION_AUTHORITY=CONDITIONAL_EXISTING_E003
E004_EXECUTION_OCCURRED=NO
E005=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
```
