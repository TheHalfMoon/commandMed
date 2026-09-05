# E004 Registry Current-State Reconciliation V31 — 2026-09-05

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical base:** `a34fa31666d4f87e8c9a98a5078b6429579135bf`  
**Canonical base tree:** `2670a051d80566cbea4e86e3c7652de02e153cff`  
**Artifact class:** deterministic post-PR-254 current-state and successor-preflight reconciliation  
**Authority effect:** NONE  
**Execution effect:** NONE  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Recompute the `SP007-RO-001` successor execution preflight from the canonical state after PR #254 instead of inheriting the pre-PR-254 `SUCCESSOR_PASS_PREFLIGHT=ABSENT` state from V30.

This record is fail closed. It does not load model weights, execute inference, run a tournament, open a device, convert or quantize weights, access protected or gated assets, use credentials, access Private Gold or PHI, perform training, select a winner, procure resources, make payments, or authorize spend.

```text
PREVIOUS_RECONCILIATION=specs/007-sft-v1/e004-registry-current-state-reconciliation-v30-2026-09-05.md
PREVIOUS_RECONCILIATION_STATE=HISTORICAL_PRE_PR254
CURRENT_CANONICAL_BASE=a34fa31666d4f87e8c9a98a5078b6429579135bf
CURRENT_CANONICAL_TREE=2670a051d80566cbea4e86e3c7652de02e153cff
POST_PR254_SUCCESSOR_PREFLIGHT_RECOMPUTED=YES
```

## 2. Controlling authority remains unchanged

The canonical successor execution decision remains:

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
SUCCESSOR_SCOPE_MODEL_EXECUTION_AUTHORITY=AUTHORIZED_E001_FROZEN_CANDIDATES_ONLY_AFTER_PASS_PREFLIGHT
SUCCESSOR_SCOPE_TOURNAMENT_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_FROZEN_NONCLINICAL_PROTOCOL_ONLY_AFTER_PASS_PREFLIGHT
CURRENT_AUTHORIZED_SPEND_USD=0
```

Decision B does not make any prerequisite pass by itself. Model and tournament execution remain conditional on a fresh exact-subject preflight PASS.

The frozen E001 candidate universe remains exactly:

```text
PRIMARY_1=Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
PRIMARY_2=Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
PRIMARY_3=ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
CONTROL=Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
CONTROL_WINNER_ELIGIBLE=NO
```

## 3. PR #254 closes the evaluation-asset freeze gate

PR #254 merged the repaired exact seven-asset subject and its deterministic evidence. The qualified subject binds:

```text
PR254_QUALIFIED_HEAD=b5fc18274152fbc45f1fbefbe3ae290917b59c30
PR254_MERGE_SHA=a34fa31666d4f87e8c9a98a5078b6429579135bf
ASSET_SET_ID=SP007_RO_001_NONCLINICAL_EVALUATION_ASSET_SET_V1
ASSET_SET_SHA256=709d5f73c1599364fc184b959cbdfd199c7ec07307fef8f8091d8eafb10f5454
PROVENANCE_INSTRUMENT_SHA256=82d29ba6374b1f74cd70d4c77be567f16ff78efb38008a8bc1764d9e1ac73d1f
SOURCE_VERIFICATION_INSTRUMENT_SHA256=6a71619aa8a940d97beeef13be935fbf83d865f2892f0fd3c37e53e32f427529
PRIVACY_INSTRUMENT_SHA256=ab3f2449888f753279492d669f08aaf3aa78115b698126c90c1602edff63c41c
TOURNAMENT_PROTOCOL_ID=SP007_RO_001_NONCLINICAL_BACKBONE_TOURNAMENT_V1
TOURNAMENT_PROTOCOL_SHA256=1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8
SPEC003_COMPUTED_ELIGIBLE_COUNT=7
CALLER_CONTROLLED_ELIGIBLE_STATE=PROHIBITED
```

The exact-head PR #254 qualification recorded successful exact-head checkout, bounded-authority binding, compile, focused asset/evidence tests, deterministic qualification verification, Spec 007 regression, full repository regression, and diff-whitespace verification.

The following pre-result gates are therefore no longer absent:

```text
SUCCESSOR_EVALUATION_ASSET_SET=PASS_EXACT_FROZEN_SET
SUCCESSOR_EVALUATION_RIGHTS=PASS_EXACT_DECLARED_SET
SUCCESSOR_EVALUATION_PROVENANCE=PASS_EXACT_DECLARED_SET
SUCCESSOR_EVALUATION_SOURCE_VERIFICATION=PASS_EXACT_DECLARED_SET
SUCCESSOR_EVALUATION_PRIVACY_CLASSIFICATION=PASS_EXACT_DECLARED_NONCLINICAL_FIXTURES
SUCCESSOR_EVALUATION_QUARANTINE=PASS_FOR_MODEL_SELECTION_DEV_SET_CHECKPOINT_SELECTION
SUCCESSOR_EVALUATION_CONTAMINATION=PASS_NARROW_NONEXPOSURE_NONADAPTATION_SEMANTICS_ONLY
SUCCESSOR_EVALUATION_SPEC003_ADMISSION=PASS_7_COMPUTED_ELIGIBLE
SUCCESSOR_FROZEN_TOURNAMENT_PROTOCOL=PASS
CANDIDATE_OUTPUTS_OBSERVED_BEFORE_FREEZE=NO
WINNER_SELECTION_PERFORMED_BY_PROTOCOL=NO
```

The contamination PASS above has only the canonical narrow meaning for the exact project-authored frozen fixtures. It is not a semantic-task-novelty claim and does not assert inspection of candidate pretraining corpora.

## 4. Frozen source identities are not complete executable artifact bindings

E001/E002 preserve exact public candidate and source identities, and some provider-reported weight or preconverted-artifact identities exist. They do not provide a complete execution bundle for every exact frozen candidate.

Current canonical evidence explicitly preserves unresolved executable-bundle fields including:

```text
model_artifact_sha256=NEEDS_EVIDENCE_FOR_EXACT_EXECUTION_SUBJECT
complete_bundle_sha256=NEEDS_EVIDENCE
complete_bundle_bytes=NEEDS_EVIDENCE
runtime_artifact_sha256=NEEDS_EVIDENCE
runtime_executable_sha256=NEEDS_EVIDENCE
exact_runtime_entrypoint=NEEDS_EVIDENCE
exact_environment_manifest_sha256=NEEDS_EVIDENCE
exact_argv=NEEDS_EVIDENCE
```

For the two remaining PRIMARY public-source metadata reconciliations, locally materialized full source-bundle integrity also remains incomplete. Public provider metadata does not become local byte verification by inference.

The two E002 preconverted GGUF identities remain bounded feasibility/provider evidence only and do not create a complete four-candidate tournament execution package. Granite and the 4B control do not acquire preconverted executable identities by substitution, and no conversion authority may be inferred for missing formats.

```text
CANONICAL_FROZEN_CANDIDATE_IDENTITIES=PASS
CANONICAL_COMPLETE_EXECUTION_ARTIFACT_SET=ABSENT
EXECUTABLE_FORMAT_COMPATIBILITY_FOR_EXACT_FOUR_CANDIDATE_RUN=UNRESOLVED
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
```

## 5. Runtime, environment, resource, access, and finance bindings remain incomplete

The canonical runtime/resource intake and later execution-time identity policy preserve fail-closed exact-subject requirements. The current main state does not bind a complete tournament execution subject with all required runtime/environment/resource identities.

```text
EXACT_RUNTIME_TOOLCHAIN_BINDING=ABSENT_OR_INCOMPLETE
EXACT_RUNTIME_EXECUTABLE_BINDING=ABSENT_OR_INCOMPLETE
EXACT_ENVIRONMENT_BINDING=ABSENT_OR_INCOMPLETE
EXACT_COMPUTE_RESOURCE_IDENTITY=NEEDS_EVIDENCE
RESOURCE_AUTHORIZATION_BASIS=NEEDS_EVIDENCE
EXACT_DEVICE_OR_RESOURCE_MEASUREMENT_BINDING=NEEDS_EVIDENCE_WHERE_APPLICABLE
EXACT_ACCESS_BINDING_FOR_EXECUTION_SUBJECT=INCOMPLETE
EXACT_CREDENTIAL_STATE_BINDING=INCOMPLETE
ZERO_INCREMENTAL_SPEND_EXECUTION_RESOURCE_BINDING=NEEDS_EVIDENCE
CURRENT_AUTHORIZED_SPEND_USD=0
```

A free, public, already-owned, or nominally zero-cost path is not automatically an exact finance/resource/access PASS. No protected, gated, credentialed, or paid path may be used to fill these fields under current authority.

## 6. A15 remains a controlling execution prerequisite

E003 binds benchmark payload access/execution to `AUTHORIZED_E003_A15_BOUND_PUBLIC_TOURNAMENT_INPUTS_ONLY`. Current canonical registry text preserves:

```text
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
```

The canonical A15 design also prohibits generic continuation language from becoming activation and requires a separate explicit activation bound to exact prerequisites and exact scope.

Therefore the successor decision's conditional requirement for separately authorized A15 is applicable to the current E003-controlled execution path.

```text
E003_A15_BINDING_REQUIRED_FOR_CURRENT_EXECUTION_PATH=YES
CURRENT_A15_BINDING=ABSENT
A15_GATE=BLOCKING
GENERIC_GO_AHEAD_COUNTS_AS_A15_ACTIVATION=NO
```

This record does not create an A15 decision surface, invent a token, or claim that A15 is the only remaining blocker.

## 7. Fresh post-PR-254 successor preflight matrix

| Gate | Current disposition | Effect |
|---|---|---|
| Exact successor scope and Decision B authority | `PASS` | Authority exists only after full preflight PASS |
| Exact E001 frozen candidate identities | `PASS` | Four-candidate identity set remains frozen |
| Exact frozen evaluation asset set | `PASS` | PR #254 repaired and qualified the seven-asset set |
| Rights / provenance / source verification / privacy | `PASS` | Exact bounded fixture evidence is canonical |
| Evaluation quarantine | `PASS` | Exact declared selection purpose only |
| Narrow evaluation contamination disposition | `PASS` | Exact-fixture nonexposure/nonadaptation semantics only |
| Spec 003 computed admission | `PASS` | Seven exact assets computed `ELIGIBLE` |
| Frozen non-clinical tournament protocol | `PASS` | Exact protocol SHA is canonical |
| Complete executable candidate artifact set | `FAIL_CLOSED` | Exact complete bundle/runtime bindings remain absent or incomplete |
| Executable format/runtime compatibility | `FAIL_CLOSED` | No exact four-candidate execution route is fully bound; conversion authority is none |
| Exact runtime/toolchain/environment identity | `FAIL_CLOSED` | Required exact execution-subject identities remain incomplete |
| Exact resource/device binding where applicable | `FAIL_CLOSED` | Required exact resource/device evidence remains incomplete |
| Exact access/credential boundary for execution subject | `FAIL_CLOSED` | No protected/gated/credential route is authorized; exact execution binding incomplete |
| Finance/resource authorization for exact execution subject | `FAIL_CLOSED` | Spend remains USD 0 and no exact zero-incremental-spend execution resource binding is canonical |
| E003-required A15 activation | `FAIL_CLOSED` | A15 authority/activation remains absent |

The preflight is conjunctive. Any single fail-closed row is sufficient to prohibit model or tournament execution.

## 8. Computed successor disposition

The previous historical state `SUCCESSOR_PASS_PREFLIGHT=ABSENT` is superseded only as a statement about whether a post-PR-254 recomputation has occurred. The result of that recomputation is not PASS.

```text
POST_PR254_SUCCESSOR_PREFLIGHT_RECOMPUTED=YES
SUCCESSOR_PREFLIGHT_DISPOSITION=BLOCKED
SUCCESSOR_PASS_PREFLIGHT=NO
MODEL_EXECUTION_NOW=NOT_AUTHORIZED_BY_GATE_STATE
TOURNAMENT_EXECUTION_NOW=NOT_AUTHORIZED_BY_GATE_STATE
TOURNAMENT_EVIDENCE_PACK_CREATED=NO
MODEL_WINNER_SELECTED=NO
E005_STATE=NOT_REACHED
BASE_CHECKPOINT_BINDING=ABSENT
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

No model or tournament result may be recorded from this reconciliation because no execution is permitted by the computed gate state.

## 9. Task-ledger reconciliation

`specs/007-sft-v1/tasks.md` correctly leaves E004 incomplete, but its E004 narrative predates PRs #249-#254 and is not a complete description of the current post-PR-254 frontier.

This V31 record provides the append-only current-state overlay without changing the incomplete E004 checkbox:

```text
E004_TASK_CHECKBOX=REMAINS_INCOMPLETE
E004_EVALUATION_ASSET_QUALIFICATION_SUBUNIT=COMPLETE
E004_SUCCESSOR_PREFLIGHT_RECOMPUTATION_SUBUNIT=COMPLETE_BLOCKED_RESULT
E004_MODEL_EXECUTION_SUBUNIT=NOT_STARTED_NOT_AUTHORIZED_BY_GATE_STATE
E004_TOURNAMENT_EXECUTION_SUBUNIT=NOT_STARTED_NOT_AUTHORIZED_BY_GATE_STATE
E004_WINNER_SELECTION_SUBUNIT=SEPARATE_E005_NOT_REACHED
```

No task is closed by prose if its required evidence is absent.

## 10. Next dependency-safe frontier

The next permissible work is limited to evidence/control-plane work that can truthfully resolve current preflight blockers under already applicable exact authority. Any proposed transition must first prove that its authority covers the exact subject.

Dependency-safe order:

1. reconcile the exact four-candidate executable artifact/runtime route without conversion unless a separately canonical conversion authority exists;
2. bind exact executable artifact, runtime, toolchain, environment, argv, network, and credential-state identities for the exact successor subject;
3. bind exact compute/resource/device identities required by the frozen non-clinical protocol and prove a zero-incremental-spend authorized resource path;
4. satisfy every other applicable exact-subject access/finance/resource prerequisite;
5. only after all non-A15 prerequisites genuinely pass, use the then-canonical A15 decision surface if a separate exact Founder/canonical activation is still required;
6. rerun the full successor preflight and require every conjunctive gate to PASS before the first model call;
7. only then execute the exact frozen candidates/protocol within Decision B authority and record genuine evidence without selecting or recommending a winner;
8. preserve E005 as a separate later winner-selection transition.

This ordering authorizes none of the missing items by itself.

## 11. Explicit protected-data and execution exclusions

```text
RAW_AYA_PROMPTS_ACCESSED=NO
RAW_AYA_TARGETS_ACCESSED=NO
RAW_AYA_MATCHED_NGRAMS_ACCESSED=NO
AYA_USER_IDS_ACCESSED=NO
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
GATED_ASSET_ACCESSED=NO
CREDENTIAL_USED=NO
MODEL_WEIGHTS_LOADED=NO
MODEL_INFERENCE_EXECUTED=NO
TOURNAMENT_EXECUTED=NO
DEVICE_EXECUTION_PERFORMED=NO
MODEL_CONVERSION_PERFORMED=NO
TRAINING_PERFORMED=NO
PROCUREMENT_PERFORMED=NO
PAYMENT_PERFORMED=NO
SPEND_USD=0
```

## 12. Qualification boundary

Under FD-007 / constitutional amendment 0.1.1, independent repository/PR review is optional by default for this bounded evidence-only reconciliation unless a later exact bounded authority explicitly reintroduces it.

Before canonical merge, verify the exact base/head/diff, applicable CI/status checks, unresolved review threads, mergeability, repository ruleset/branch state available to the acting integration, absence of later canonical invalidation, and use an expected-head guarded merge.

No unavailable check, silent bot, skipped review, or inaccessible branch-protection endpoint may be represented as a PASS.
