# E004 Current Prerequisite Frontier Reconciliation — 2026-08-27

**Spec:** 007 SFT V1  
**Assessment type:** append-only current-state overlay  
**Canonical base:** `54c4f7bea09ea4be7031302b63273c3d1743b644`  
**Historical frontier preserved:** `specs/007-sft-v1/e004-prerequisite-frontier-2026-08-27.md`  
**Execution performed:** NO  
**Authority effect:** NONE

This file reconciles the live E004 prerequisite frontier after corrective maintenance, bounded artifact research, A2 public-evidence discovery, and the A2 evidence-package workbench. It does **not** rewrite historical clarification/audit records whose status fields were correct at their capture time.

The purpose is to prevent stale historical states such as `A1_STATUS=BLOCKED`, the former device/A15 cycle, or the former Arabic V1 evidence-role conflict from being mistaken for current canonical truth.

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

Existing bounded E002/E003 authority remains exactly preserved:

```text
MODEL_WEIGHT_ACCESS_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
MODEL_EXECUTION_AUTHORITY=AUTHORIZED_E003_FROZEN_TOURNAMENT_ONLY
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_E003_A15_BOUND_PUBLIC_TOURNAMENT_INPUTS_ONLY
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=AUTHORIZED_E003_A15_BOUND_PUBLIC_TOURNAMENT_INPUTS_ONLY
DEVICE_EXECUTION_AUTHORITY=AUTHORIZED_E003_FROZEN_TOURNAMENT_QUALIFICATION_ONLY
```

Those authorizations are not currently executable because E004 preflight has not reached PASS.

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

## 2. What has changed since the historical prerequisite frontier

The earlier frontier correctly identified several blockers at its audit base. Subsequent canonical work resolved or refined some of them.

### 2.1 Spec 005 ↔ E004 corrective maintenance — resolved structurally

Canonical closeout:

- authorization merge: `238d8a0b8cfed54356ca39bb892f94ebf12d89de`;
- implementation qualified head: `53aa3ab29636563f11a82b72d4cfd940a2351792`;
- implementation merge: `5bb6177dc7908dfb3a6a51d3c39db66a4e289fb1`.

Current result:

```text
E004_CORRECTIVE_MAINTENANCE=CLOSED_CANONICAL
DEVICE_A15_STRUCTURAL_CYCLE=RESOLVED_BY_CONTROL_PLANE_REPAIR
DEVICE_PACKAGE_WARMUP_CONTRACT=RECONCILED
E004_NON_EXECUTING_REQUEST_ENVELOPE=IMPLEMENTED
```

`evaluate_device_execution_readiness()` now separates static pre-execution readiness from post-execution measured qualification, and `src/commandmed/spec007/e004.py` provides the deterministic non-executing request envelope.

This closes the former **structural** device circularity and missing-envelope defects. It does not provide the real runtime/build/tool/physical-device evidence needed for E004.

### 2.2 A1 metrics-v2 — canonical implementation exists

Historical Session 10/11 documents predate the canonical A1 implementation and therefore contain `A1_STATUS=BLOCKED` or pending pre-merge language.

Current canonical repository truth contains:

```text
V2_SCHEMA_ID=commandmed-metrics-catalog
V2_SCHEMA_VERSION=2.0
V2_CATALOG_PATH=data/eval/metrics-v2.json
V2_METRICS_SHA256=bad51bffe30c0fb7de37afcaf8620ad1ad2deed2dd626a1ec6c2eb47c4107f4b
```

Spec 005 `tasks.md` records T003–T010 complete and permits all later implemented control-plane tasks only after the A1 merge/reverification gate.

Current state for DAG node R1:

```text
R1_A1_METRICS_V2_CONTROL_PLANE=CANONICAL_COMPLETE
R1_REAL_EXTERNAL_EXECUTION_ACTION=NOT_APPLICABLE
```

This does not imply A2 or any downstream real gate is complete.

### 2.3 Arabic parity V1 evidence-role conflict — resolved for V2 consumers

Canonical metrics-v2 now separates:

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

Current result:

```text
PUBLIC_PRECONVERTED_RESEARCH_RESULT=NO_EXPANSION_SUPPORTED_BY_CURRENT_EVIDENCE
CURRENT_PUBLIC_ARTIFACT_RESEARCH_PASS=CLOSED
PUBLIC_ARTIFACT_RESEARCH_EXHAUSTIVE_FOR_ALL_FUTURE_EVIDENCE=NO
E002_PRECONVERTED_ALLOWLIST_COUNT=2
NEW_PRECONVERTED_ALLOWLIST_ENTRIES=0
MODEL_CONVERSION_AUTHORITY=NONE
ARTIFACT_AUTHORITY_DECISION=NOT_TAKEN
```

Granite and CONTROL remain incomplete for exact E002-compatible preconverted artifact binding under current evidence. This is not a permanent rejection and does not authorize conversion.

### 2.5 A2 public evidence — research/workbench complete, real A2 still incomplete

PR #75 canonically added the bounded public evidence discovery; PR #76 added the metadata-only evidence-package workbench.

Current research result:

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

At this reconciliation base, `data/spec005/` contains exactly three policy/control-plane contract files:

```text
data/spec005/device_qualification_contract.json
data/spec005/preconstruction_contract.json
data/spec005/selection_quality_contract.json
```

No additional real A2–A14 evidence-record files are present under that canonical data directory.

Therefore the correct distinction is:

```text
SPEC005_VALIDATORS_AND_POLICY_CONTRACTS=CANONICAL_IMPLEMENTED
REAL_A2_TO_A14_EVIDENCE_SNAPSHOT=ABSENT
REAL_A15_ACTIVATION=ABSENT
```

Synthetic fixtures used by tests remain non-authoritative and cannot substitute for real records.

## 4. Current DAG state — structural capability versus real PASS

The canonical preconstruction DAG is encoded in `data/spec005/preconstruction_contract.json`. This overlay evaluates only current repository evidence; it does not manufacture PASS.

| DAG node | Gate | Control-plane status | Real-gate status | Current reason |
|---|---|---|---|---|
| `R1` | A1 metrics-v2 | `CANONICAL_COMPLETE` | `PASS_FOR_PRECONSTRUCTION_DEPENDENCY` | V2 contract/consumer binding exists canonically |
| `T1` | A2 threshold/margin policy | `VALIDATOR_READY` | `INCOMPLETE` | 0/6 thresholds frozen; no qualified review dispositions |
| `D34` | A3+A4 statistical design/allocation | `VALIDATOR_READY` | `BLOCKED_BY_T1` | exact threshold/margin must precede final N/allocation |
| `G1` | A5 rights instrument | `VALIDATOR/POLICY_ARCHITECTURE_READY` | `REAL_EVIDENCE_NOT_PROVEN` | no actual contributor/content-rights evidence set bound |
| `G2` | A6 non-PHI policy | `VALIDATOR/POLICY_ARCHITECTURE_READY` | `REAL_EVIDENCE_NOT_PROVEN` | no actual author/source privacy attestations bound |
| `G3` | A8 authoring/review protocol | `VALIDATOR/POLICY_ARCHITECTURE_READY` | `REAL_OPERATIONAL_BINDING_NOT_PROVEN` | no real author/reviewer assignments or review execution |
| `G4` | A12 change control | `VALIDATOR/POLICY_ARCHITECTURE_READY` | `REAL_SUITE_IDENTITY_NOT_AVAILABLE` | no constructed/frozen suite exists to bind operational identity |
| `S1` | A10 exact source route | `VALIDATOR_READY` | `INCOMPLETE` | no exact real selection-suite source route record admitted |
| `P1` | A9 provenance template/bindings | `VALIDATOR_READY` | `INCOMPLETE` | no real suite/root/pair metadata records exist |
| `C1` | A11 contamination plan | `VALIDATOR_READY` | `INCOMPLETE` | exact real source/provenance identities absent; assessment authority also absent |
| `H1` | A7 personnel roster/nonexposure | `VALIDATOR_READY` | `INCOMPLETE` | no real qualified roster/nonexposure evidence bound |
| `I1` | A13 access/firewall | `VALIDATOR_READY` | `INCOMPLETE` | no real personnel/suite/storage/access binding |
| `F1` | A14 spend/engagement | `VALIDATOR_READY` | `INCOMPLETE` | `$0`/absence cannot prove NOT_REQUIRED; real workload/personnel requirements unresolved |
| `J1` | A1–A14 recheck | `VALIDATOR_READY` | `NOT_REACHED` | upstream real gates incomplete |
| `ACT` | A15 activation | `VALIDATOR_READY` | `ABSENT_NOT_AUTHORIZED` | requires exact current PASS snapshot plus separate explicit activation |

`VALIDATOR_READY` means only that repository code can validate a future record. It is not evidence that the real gate passed.

## 5. Arabic selection-suite construction remains prohibited

Session 10 Q5 remains controlling for formal case construction:

```text
ARABIC_SELECTION_PRECONSTRUCTION_GATE_RESULT=NOT_READY_TO_CONSTRUCT
ARABIC_SELECTION_EVIDENCE_CREATION_AUTHORITY=NONE
ARABIC_SELECTION_ROOT_TASK_AUTHORING_AUTHORITY=NONE
ARABIC_SELECTION_PAIR_ADAPTATION_AUTHORITY=NONE
ARABIC_SELECTION_REVIEW_EXECUTION_AUTHORITY=NONE
```

The preferred source architecture and five coverage anchors are already frozen. Therefore a new public-dataset search does not authorize construction and does not replace the preconstruction gates.

Current route preference remains:

```text
PREFERRED_ROOT_ORIGIN_TYPE=ORIGINAL
PREFERRED_ROOT_CONTENT=INDEPENDENT_HUMAN_AUTHORED_CLINICAL_NON_PHI
PREFERRED_PRIVATE_GOLD_PARENT_COUNT=0
```

Public dev or derived components remain only conditional alternatives subject to exact split identity, immutable binding, rights, derivation permission, privacy, lineage, and contamination requirements.

## 6. Contamination frontier — two distinct stages

The preconstruction A11 **plan** and the postconstruction contamination **assessment** must not be conflated.

```text
A11_PRECONSTRUCTION_PLAN_VALIDATOR=AVAILABLE
A11_REAL_PLAN_IDENTITY=INCOMPLETE_WITHOUT_REAL_SOURCE_PROVENANCE_BINDINGS
POSTCONSTRUCTION_CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
POSTCONSTRUCTION_CONTAMINATION_ASSESSMENT_EXECUTION=NOT_AUTHORIZED
```

Actual contamination results cannot be created for a suite that has not been constructed and frozen. Conversely, the exact method/identity/candidate-binding plan must be frozen before authoring under the canonical DAG.

## 7. Artifact frontier remains a separate Founder decision

The current public research pass found no additional exact E002-compatible preconverted binding. The next artifact step remains a separate Founder authorization decision.

This overlay does not take that decision.

```text
ARTIFACT_AUTHORITY_DECISION=NOT_TAKEN
FOUNDER_SEPARATE_ARTIFACT_DECISION_REQUIRED=YES
GENERIC_CONTINUATION_OF_REPOSITORY_WORK_DOES_NOT_AUTO_EXPAND_E002=YES
MODEL_CONVERSION_AUTHORITY=NONE
```

Possible future evidence may reopen read-only research without changing this boundary.

## 8. Scientific threshold frontier remains external-review bound

Public literature now supplies method/risk context, but not a transferable numeric policy.

Real T1/A2 completion still requires, per metric where applicable:

1. exact intended-use/population and stratum scope;
2. exact identity-bound commandMed evaluation evidence;
3. clinical-domain review authority and actual disposition;
4. statistical-method review authority and actual disposition;
5. threshold/margin numeric policy frozen pre-result;
6. conflict/dissent disposition;
7. canonical governance adoption.

D34 then requires exact candidate-neutral statistical design, numeric N, allocation, dependency/pairing, multiplicity, uncertainty/error parameters, and method identity.

No repository agent may impersonate required human clinical/statistical authority.

## 9. Runtime/device/resource frontier after structural repair

The former control-plane circularity is gone, but real static execution readiness remains unproven.

Required future evidence still includes exact, immutable, current identities for applicable:

```text
EXECUTABLE_CANDIDATE_ARTIFACT
LLAMA_CPP_OR_OTHER_FROZEN_RUNTIME_COMMIT
PLATFORM_BUILD_IDENTITY
TOOLCHAIN_OR_WRAPPER_IDENTITY
MEMORY_MEASUREMENT_METHOD
TIMING_METHOD
THERMAL_SIGNAL_IDENTITY
ENERGY_SIGNAL_IDENTITY
PHYSICAL_TARGET_BINDING
ZERO_SPEND_RESOURCE_AVAILABILITY
```

A favorable static readiness result must be computed from real records. Post-execution device qualification still requires the frozen measured-run evidence and must not be fabricated pre-execution.

## 10. Dependency-safe work remaining without new execution authority

The following work classes remain safe in principle if they do not create prohibited content or impersonate external authorities:

1. read-only source/evidence research;
2. append-only current-state reconciliation;
3. metadata/template design grounded in existing validators, without case content;
4. rights/privacy/review/change-control policy extraction from already-frozen architecture, provided it creates no contributor signature, personnel assignment, access grant, spend commitment, or construction authority;
5. statistical-method research that leaves numeric policy/N unresolved until qualified review;
6. exact runtime/tool metadata research without device/model execution or artifact acquisition outside E002.

The following cannot be completed by repository-only continuation:

```text
ARTIFACT_AUTHORITY_DECISION
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

## 11. Current critical path

The canonical DAG and live evidence yield this current critical path:

```text
R1=A1                         -> COMPLETE
T1=A2                         -> INCOMPLETE_REAL_EVIDENCE_AND_REVIEW
D34=A3+A4                     -> BLOCKED_BY_T1
H1/A7                         -> BLOCKED_BY_D34_PLUS_REAL_PERSONNEL_EVIDENCE
I1/A13                        -> BLOCKED_BY_H1_PLUS_REAL_SUITE/ACCESS_BINDING
F1/A14                        -> BLOCKED_BY_D34/H1_AND_REAL_RESOURCE_REQUIREMENT
J1=A1_TO_A14_RECHECK          -> NOT_REACHED
ACT=A15                       -> NOT_REACHED_AND_SEPARATELY_AUTHORIZED_ONLY
E004_FINAL_PREFLIGHT          -> BLOCKED
E004_EXECUTION                -> NOT_REACHED
```

Parallel governance/source branches remain incomplete in real evidence terms:

```text
G1/A5,G2/A6,G3/A8,G4/A12 -> CONTROL_PLANE_READY_REAL_BINDINGS_INCOMPLETE
S1/A10                     -> INCOMPLETE_EXACT_REAL_SOURCE_ROUTE
P1/A9                      -> INCOMPLETE_REAL_PROVENANCE_BINDINGS
C1/A11                     -> INCOMPLETE_REAL_PLAN_BINDING_AND_NO_ASSESSMENT_AUTHORITY
```

## 12. Current decision/evidence frontier

```text
NEXT_FOUNDER_DECISION_1=FROZEN_ARTIFACT_AUTHORITY_RECONCILIATION
NEXT_FOUNDER_DECISION_1_STATE=REQUIRED_NOT_TAKEN

NEXT_SCIENTIFIC_EVIDENCE_NODE=T1_A2
NEXT_SCIENTIFIC_EVIDENCE_NODE_STATE=PUBLIC_RESEARCH_PREPARED_REAL_QUALIFIED_REVIEW_REQUIRED

NEXT_DOWNSTREAM_STATISTICAL_NODE=D34_A3_A4
NEXT_DOWNSTREAM_STATISTICAL_NODE_STATE=BLOCKED_BY_A2

NEXT_EXTERNAL_OPERATIONAL_EVIDENCE=
RIGHTS_PRIVACY_PERSONNEL_ACCESS_RESOURCE_RUNTIME_DEVICE_BINDINGS

CONTAMINATION_ASSESSMENT_AUTHORITY=SEPARATE_DECISION_REQUIRED
A15_ACTIVATION=SEPARATE_DECISION_AFTER_A1_TO_A14_PASS
```

No single repository-only mutation can turn this frontier into E004 PASS.

## 13. Non-events

No model, benchmark payload, selection-suite payload, physical device, contamination assessment, conversion, quantization, training, credential/gated asset, Private Gold, PHI, provider generation, personnel engagement, payment, or spend execution occurred in producing this reconciliation.
