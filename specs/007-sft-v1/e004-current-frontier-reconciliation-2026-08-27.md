# E004 Current Prerequisite Frontier Reconciliation — 2026-08-27

**Spec:** 007 SFT V1  
**Assessment type:** append-only current-state overlay  
**Canonical base:** `54c4f7bea09ea4be7031302b63273c3d1743b644`  
**Historical frontier preserved:** `specs/007-sft-v1/e004-prerequisite-frontier-2026-08-27.md`  
**Execution performed:** NO  
**Authority effect:** NONE

This file reconciles the live E004 prerequisite frontier after corrective maintenance, bounded artifact research, A2 public-evidence discovery, and the A2 evidence-package workbench. It does **not** rewrite historical clarification/audit records whose status fields were correct at capture time.

Its purpose is to prevent stale historical states such as `A1_STATUS=BLOCKED`, the former device/A15 cycle, or the former Arabic V1 evidence-role conflict from being mistaken for current canonical truth.

## 1. Current top-level state

```text
CANONICAL_MAIN_AT_RECONCILIATION_BASE=54c4f7bea09ea4be7031302b63273c3d1743b644
E001=CLOSED_CANONICAL
E002=CLOSED_CANONICAL
E003=CLOSED_CANONICAL
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Existing bounded authority is preserved exactly:

```text
MODEL_WEIGHT_ACCESS_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
MODEL_EXECUTION_AUTHORITY=AUTHORIZED_E003_FROZEN_TOURNAMENT_ONLY
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_E003_A15_BOUND_PUBLIC_TOURNAMENT_INPUTS_ONLY
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=AUTHORIZED_E003_A15_BOUND_PUBLIC_TOURNAMENT_INPUTS_ONLY
DEVICE_EXECUTION_AUTHORITY=AUTHORIZED_E003_FROZEN_TOURNAMENT_QUALIFICATION_ONLY
```

Executability must be separated by authority source:

```text
E002_NON_EXECUTING_SOURCE_WEIGHT_ACQUISITION_AND_STATIC_INTEGRITY_WORK=CURRENTLY_AUTHORIZED_WITHIN_EXACT_E002_SCOPE
E002_PRECONVERTED_BYTE_ACQUISITION=CURRENTLY_AUTHORIZED_FOR_EXACT_TWO_ENTRY_ALLOWLIST_ONLY

E003_MODEL_EXECUTION=CANNOT_START_WHILE_E004_PREFLIGHT_BLOCKED
E003_A15_BOUND_BENCHMARK_PAYLOAD_ACCESS_EXECUTION=CANNOT_START_WHILE_REQUIRED_A15_PREFLIGHT_BINDINGS_ARE_INCOMPLETE
E003_DEVICE_QUALIFICATION_EXECUTION=CANNOT_START_WHILE_REQUIRED_E004_PREEXECUTION_STATE_IS_INCOMPLETE
```

E004 `BLOCKED_PREFLIGHT` therefore does **not** revoke or suspend the independently authorized non-executing E002 acquisition/static-inspection actions. E002 still prohibits loading weights into a runtime, inference, conversion, benchmark access/execution, and device execution.

Authorities that remain absent:

```text
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 2. What changed since the historical prerequisite frontier

### 2.1 Spec 005 ↔ E004 corrective maintenance — structurally resolved

Canonical closeout records:

```text
AUTHORIZATION_MERGE=238d8a0b8cfed54356ca39bb892f94ebf12d89de
QUALIFIED_IMPLEMENTATION_HEAD=53aa3ab29636563f11a82b72d4cfd940a2351792
IMPLEMENTATION_MERGE=5bb6177dc7908dfb3a6a51d3c39db66a4e289fb1
E004_CORRECTIVE_MAINTENANCE=CLOSED_CANONICAL
DEVICE_A15_STRUCTURAL_CYCLE=RESOLVED_BY_CONTROL_PLANE_REPAIR
DEVICE_PACKAGE_WARMUP_CONTRACT=RECONCILED
E004_NON_EXECUTING_REQUEST_ENVELOPE=IMPLEMENTED
```

`evaluate_device_execution_readiness()` now separates static pre-execution readiness from post-execution measured qualification. `src/commandmed/spec007/e004.py` provides a deterministic non-executing request envelope.

The former structural cycle and missing-envelope defects are no longer blockers. Real runtime/build/tool/physical-device evidence remains unresolved.

### 2.2 A1 metrics-v2 — canonical implementation exists

Historical Session 10/11 artifacts predate the canonical A1 implementation and retain historical `BLOCKED`/pending language.

Current canonical truth contains:

```text
V2_SCHEMA_ID=commandmed-metrics-catalog
V2_SCHEMA_VERSION=2.0
V2_CATALOG_PATH=data/eval/metrics-v2.json
V2_METRICS_SHA256=bad51bffe30c0fb7de37afcaf8620ad1ad2deed2dd626a1ec6c2eb47c4107f4b
R1_A1_METRICS_V2_CONTROL_PLANE=CANONICAL_COMPLETE
```

Spec 005 `tasks.md` records T003–T010 complete and allows later implementation tasks only after the A1 merge/reverification stop gate.

### 2.3 Arabic parity V1 evidence-role conflict — resolved for V2 consumers

Canonical metrics-v2 separates:

```text
SELECTION_DEV
  purpose=CHECKPOINT_SELECTION
  source_policy=SELECTION_SAFE_NON_GOLD

PRIVATE_GOLD_FINAL_AUDIT
  purpose=PRIVATE_GOLD
  source_policy=PRIVATE_GOLD_FAMILY
```

Therefore:

```text
ARABIC_PARITY_V1_SINGLE_REQUIRED_EVIDENCE_CONFLICT=HISTORICAL_SUPERSEDED_FOR_V2_CONSUMERS
ARABIC_PARITY_V2_EVIDENCE_ROLE_SCHEMA_CONFLICT=RESOLVED
PRIVATE_GOLD_SELECTION_PROHIBITION=PRESERVED
```

Arabic parity remains scientifically incomplete because the real selection-safe paired suite, paired threshold/method, qualified review, and numeric N/allocation are not bound.

### 2.4 Frozen-artifact public research — current pass closed, no allowlist expansion

PRs #73 and #74 refined CONTROL provenance and closed the current bounded public artifact-research pass.

```text
PUBLIC_PRECONVERTED_RESEARCH_RESULT=NO_EXPANSION_SUPPORTED_BY_CURRENT_EVIDENCE
CURRENT_PUBLIC_ARTIFACT_RESEARCH_PASS=CLOSED
PUBLIC_ARTIFACT_RESEARCH_EXHAUSTIVE_FOR_ALL_FUTURE_EVIDENCE=NO
E002_PRECONVERTED_ALLOWLIST_COUNT=2
NEW_PRECONVERTED_ALLOWLIST_ENTRIES=0
MODEL_CONVERSION_AUTHORITY=NONE
ARTIFACT_AUTHORITY_DECISION=NOT_TAKEN
```

E002 still authorizes fetching the public source-model weights at the exact frozen revisions and the two exact allowlisted preconverted artifacts. Granite and CONTROL remain incomplete only for additional exact preconverted GGUF binding under current evidence. No new preconverted artifact or conversion authority is implied.

### 2.5 A2 public evidence — research/workbench complete, real A2 incomplete

PR #75 added the bounded public evidence discovery; PR #76 added the metadata-only evidence-package workbench.

```text
A2_PUBLIC_EVIDENCE_DISCOVERY_RESULT=METHOD_AND_RISK_CONTEXT_FOUND_NO_TRANSFERABLE_NUMERIC_POLICY
A2_PUBLIC_EVIDENCE_SOURCE_INVENTORY=AVAILABLE_FOR_LATER_REVIEW
PUBLIC_EVIDENCE_LOCATORS_BOUND_IN_WORKBENCH=YES
A2_REAL_THRESHOLD_RECORDS_CREATED=0
A2_REAL_STATISTICAL_DESIGN_RECORDS_CREATED=0
A2_REAL_REVIEW_DISPOSITIONS_CREATED=0
NUMERIC_THRESHOLDS_FROZEN=0
STATISTICAL_DESIGNS_FROZEN=0
HARD_GATE_POPULATION_THRESHOLDS_READY_TO_FREEZE=0
HARD_GATE_POPULATION_THRESHOLDS_NOT_READY_TO_FREEZE=6
```

The workbench is explicitly not validator input and cannot be promoted to PASS by replacing placeholders.

## 3. Current Spec 005 real-record inventory

At this reconciliation base, `data/spec005/` contains exactly:

```text
data/spec005/device_qualification_contract.json
data/spec005/preconstruction_contract.json
data/spec005/selection_quality_contract.json
```

These are policy/control-plane contracts. No additional real A2–A14 evidence-record files are present under that canonical data directory.

```text
SPEC005_VALIDATORS_AND_POLICY_CONTRACTS=CANONICAL_IMPLEMENTED
REAL_A2_TO_A14_EVIDENCE_SNAPSHOT=ABSENT
REAL_A15_ACTIVATION=ABSENT
```

Synthetic fixture records remain non-authoritative.

## 4. Current DAG state — structural capability versus real PASS

The canonical DAG is encoded in `data/spec005/preconstruction_contract.json`.

| Node | Gate | Control-plane status | Real-gate status | Current reason |
|---|---|---|---|---|
| `R1` | A1 metrics-v2 | `CANONICAL_COMPLETE` | `PASS_FOR_PRECONSTRUCTION_DEPENDENCY` | V2 contract/consumer binding exists canonically |
| `T1` | A2 threshold/margin policy | `VALIDATOR_READY` | `INCOMPLETE` | 0/6 thresholds frozen; no qualified review dispositions |
| `D34` | A3+A4 statistical design/allocation | `VALIDATOR_READY` | `BLOCKED_BY_T1` | exact threshold/margin precedes final N/allocation |
| `G1` | A5 rights instrument | `VALIDATOR/POLICY_ARCHITECTURE_READY` | `REAL_EVIDENCE_NOT_PROVEN` | no actual contributor/content-rights evidence set bound |
| `G2` | A6 non-PHI policy | `VALIDATOR/POLICY_ARCHITECTURE_READY` | `REAL_EVIDENCE_NOT_PROVEN` | no actual author/source privacy attestations bound |
| `G3` | A8 authoring/review protocol | `VALIDATOR/POLICY_ARCHITECTURE_READY` | `REAL_OPERATIONAL_BINDING_NOT_PROVEN` | no real author/reviewer assignments or review execution |
| `G4` | A12 change control | `VALIDATOR/POLICY_ARCHITECTURE_READY` | `REAL_SUITE_IDENTITY_NOT_AVAILABLE` | no constructed/frozen suite exists to bind operational identity |
| `S1` | A10 exact source route | `VALIDATOR_READY` | `INCOMPLETE` | no exact real selection-suite source-route record admitted |
| `P1` | A9 provenance template/bindings | `VALIDATOR_READY` | `INCOMPLETE` | no real suite/root/pair metadata records exist |
| `C1` | A11 contamination plan | `VALIDATOR_READY` | `INCOMPLETE` | real source/provenance identities absent; assessment authority absent |
| `H1` | A7 personnel roster/nonexposure | `VALIDATOR_READY` | `INCOMPLETE` | mandatory predecessors and real qualified roster evidence incomplete |
| `I1` | A13 access/firewall | `VALIDATOR_READY` | `INCOMPLETE` | mandatory predecessors and real suite/storage/access bindings incomplete |
| `F1` | A14 spend/engagement | `VALIDATOR_READY` | `INCOMPLETE` | mandatory predecessors and real workload/personnel requirements incomplete |
| `J1` | A1–A14 recheck | `VALIDATOR_READY` | `NOT_REACHED` | all incoming prerequisite branches are not PASS |
| `ACT` | A15 activation | `VALIDATOR_READY` | `ABSENT_NOT_AUTHORIZED` | exact current PASS snapshot plus separate activation required |

`VALIDATOR_READY` is never equivalent to real evidence PASS.

## 5. Dependency-complete blocking graph

The current DAG must preserve **every** incoming edge rather than imply a simplified linear path.

Scientific branch:

```text
R1 -> T1 -> D34
```

Governance/source/provenance branch:

```text
G1 -> S1
G2 -> S1

G1 -> P1
G2 -> P1
G3 -> P1
G4 -> P1
S1 -> P1

S1 -> C1
P1 -> C1
```

Personnel branch:

```text
G1 -> H1
G2 -> H1
G3 -> H1
D34 -> H1
```

Access branch:

```text
G2 -> I1
G3 -> I1
G4 -> I1
P1 -> I1
H1 -> I1
```

Finance/engagement branch:

```text
D34 -> F1
G3 -> F1
H1 -> F1
```

Preactivation recheck:

```text
R1,T1,D34,G1,G2,G3,G4,S1,P1,C1,H1,I1,F1 -> J1
J1 -> ACT
```

No subset of these edges may establish readiness.

## 6. Arabic selection-suite construction remains prohibited

Session 10 Q5 remains controlling:

```text
ARABIC_SELECTION_PRECONSTRUCTION_GATE_RESULT=NOT_READY_TO_CONSTRUCT
ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
ARABIC_SELECTION_ROOT_TASK_AUTHORING_AUTHORITY=NONE
ARABIC_SELECTION_PAIR_ADAPTATION_AUTHORITY=NONE
ARABIC_SELECTION_REVIEW_EXECUTION_AUTHORITY=NONE
```

The preferred source architecture and five coverage anchors are already frozen. A new public-dataset search cannot replace the preconstruction gates.

```text
PREFERRED_ROOT_ORIGIN_TYPE=ORIGINAL
PREFERRED_ROOT_CONTENT=INDEPENDENT_HUMAN_AUTHORED_CLINICAL_NON_PHI
PREFERRED_PRIVATE_GOLD_PARENT_COUNT=0
```

Public-dev or derived components remain only conditional alternatives subject to exact split identity, immutable binding, rights, derivation permission, privacy, lineage, and contamination requirements.

## 7. Contamination frontier — plan versus assessment

A11 preconstruction planning and postconstruction contamination assessment are distinct:

```text
A11_PRECONSTRUCTION_PLAN_VALIDATOR=AVAILABLE
A11_REAL_PLAN_IDENTITY=INCOMPLETE_WITHOUT_REAL_SOURCE_PROVENANCE_BINDINGS
POSTCONSTRUCTION_CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
POSTCONSTRUCTION_CONTAMINATION_ASSESSMENT_EXECUTION=NOT_AUTHORIZED
```

Actual contamination results cannot exist for a suite that has not been constructed/frozen. The exact assessment method/identity/candidate-binding plan must nevertheless be frozen before authoring under the canonical DAG.

## 8. Artifact frontier remains a separate Founder decision for expansion/conversion

Current public research found no additional exact E002-compatible preconverted binding. Existing E002 actions remain usable within their exact scope; what remains undecided is any **expansion** needed for Granite/CONTROL preconverted qualification or a conversion route.

```text
EXISTING_E002_SOURCE_WEIGHT_ACCESS=AUTHORIZED_NON_EXECUTING
EXISTING_E002_TWO_ENTRY_PRECONVERTED_ALLOWLIST_ACCESS=AUTHORIZED_NON_EXECUTING
ARTIFACT_ALLOWLIST_EXPANSION_OR_CONVERSION_DECISION=NOT_TAKEN
FOUNDER_SEPARATE_ARTIFACT_DECISION_REQUIRED_FOR_EXPANSION_OR_CONVERSION=YES
MODEL_CONVERSION_AUTHORITY=NONE
```

Generic continuation does not expand E002.

## 9. Scientific threshold frontier remains external-review bound

Public literature supplies method/risk context, not transferable numeric policy.

Real T1/A2 completion still requires, where applicable:

1. exact intended-use/population and stratum scope;
2. exact identity-bound commandMed evaluation evidence;
3. clinical-domain review authority and actual disposition;
4. statistical-method review authority and actual disposition;
5. threshold/margin numeric policy frozen pre-result;
6. conflict/dissent disposition;
7. canonical governance adoption.

Only after T1 PASS may D34 freeze exact candidate-neutral statistical design, numeric N, allocation, dependency/pairing, multiplicity, uncertainty/error parameters, and method identity.

No repository agent may impersonate required human clinical/statistical authority.

## 10. Runtime/device/resource frontier after structural repair

The former structural circularity is gone, but real static execution readiness remains unproven. Future records still need exact identities for applicable executable artifacts, frozen runtime/build/toolchain, memory/timing/thermal/energy methods, physical targets, and zero-spend resource availability.

A favorable static readiness result must be computed from real records. Post-execution device qualification still requires the frozen measured-run evidence and must not be fabricated pre-execution.

## 11. Dependency-safe work without new execution authority

Safe in principle when bounded and non-executing:

1. E002-authorized exact public source-weight/two-allowlisted-artifact acquisition and static integrity/provenance work;
2. read-only source/evidence research;
3. append-only current-state reconciliation;
4. metadata/template design grounded in existing validators without case content;
5. rights/privacy/review/change-control policy extraction from frozen architecture without contributor acceptance, personnel assignment, access grant, spend commitment, or construction;
6. statistical-method research that leaves numeric policy/N unresolved until qualified review;
7. exact runtime/tool metadata research without model/device execution or unapproved artifact acquisition.

Repository-only continuation cannot fabricate or self-authorize:

```text
ARTIFACT_ALLOWLIST_EXPANSION_OR_CONVERSION_DECISION
QUALIFIED_CLINICAL_REVIEW_DISPOSITION
QUALIFIED_STATISTICAL_REVIEW_DISPOSITION
REAL_CONTRIBUTOR_OR_PERSONNEL_ATTESTATION
REAL_ACCESS_GRANT
REAL_SPEND_OR_ENGAGEMENT_AUTHORIZATION
CONTAMINATION_ASSESSMENT_AUTHORITY
A15_EXPLICIT_ACTIVATION
MODEL_CONVERSION
TRAINING
```

## 12. Current decision/evidence frontier

```text
NEXT_FOUNDER_DECISION_1=FROZEN_ARTIFACT_ALLOWLIST_EXPANSION_OR_CONVERSION_RECONCILIATION
NEXT_FOUNDER_DECISION_1_STATE=REQUIRED_NOT_TAKEN

NEXT_SCIENTIFIC_EVIDENCE_NODE=T1_A2
NEXT_SCIENTIFIC_EVIDENCE_NODE_STATE=PUBLIC_RESEARCH_PREPARED_REAL_QUALIFIED_REVIEW_REQUIRED

NEXT_DOWNSTREAM_STATISTICAL_NODE=D34_A3_A4
NEXT_DOWNSTREAM_STATISTICAL_NODE_STATE=BLOCKED_BY_A2

PARALLEL_GOVERNANCE_BRANCHES=G1_G2_G3_G4
PARALLEL_GOVERNANCE_BRANCH_STATE=DESIGN_CONTROL_PLANE_PRESENT_REAL_BINDINGS_INCOMPLETE

NEXT_EXTERNAL_OPERATIONAL_EVIDENCE=RIGHTS_PRIVACY_PERSONNEL_ACCESS_RESOURCE_RUNTIME_DEVICE_BINDINGS
CONTAMINATION_ASSESSMENT_AUTHORITY=SEPARATE_DECISION_REQUIRED
A15_ACTIVATION=SEPARATE_DECISION_AFTER_A1_TO_A14_PASS
```

No single repository-only mutation can turn this frontier into E004 PASS.

## 13. Non-events

No model execution, benchmark/selection payload execution, physical-device run, contamination assessment, conversion, quantization, training, credential/gated asset access, Private Gold access, PHI access, provider generation, personnel engagement, payment, or spend execution occurred in producing this reconciliation.
