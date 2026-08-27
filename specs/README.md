# commandMed Spec Registry

This directory is the dependency-ordered **spec-of-specs** for commandMed.

The roadmap is not execution authority. Only one bounded spec becomes active at a time, and every spec must prove its exit conditions before a dependent spec may begin.

## State legend

- `CANONICAL_PLANNING` — definition is frozen enough to govern later work; not necessarily executable.
- `AUTHORIZED_TO_SPECIFY` — specification-stage work may begin; does not authorize clarification, planning, implementation, execution, model/weight/data access, or later lifecycle stages.
- `AUTHORIZED_TO_CLARIFY` — clarification-stage work may begin on a canonically merged specification; does not authorize planning, implementation, execution, model/weight/data access, or later lifecycle stages.
- `AUTHORIZED_TO_PLAN` — the complete non-executing planning package may be created and qualified from a canonically merged clarification, including plan, supporting research/data-model/contracts/quickstart, requirements checklist, dependency-ordered tasks, and static analyze; does not authorize implementation, model execution, weight/data access, training, device execution, credentials, spend, or any other execution authority.
- `AUTHORIZED_TO_START` — may be implemented under its bounded scope.
- `ACTIVE` — implementation/reconciliation in progress.
- `CLOSED_CANONICAL` — acceptance evidence is complete and merged canonically.
- `BLOCKED` — dependency/decision/gate prevents start.
- `DEFERRED` — intentionally outside the present execution horizon.

## Registry

| ID | Name | State | Depends on | Notes |
|---|---|---|---|---|
| 000 | Program Charter | `CLOSED_CANONICAL` | — | Planning package canonical at `b0398f2fe514bd3ccd339908d739aef61055f929`; closure evidence in `specs/000-program-charter/closeout.md`. |
| 001 | Evaluation Charter | `CLOSED_CANONICAL` | 000 | Implementation merge `531343f785a6430036cbb2770d0504676514b9a7`; closure merge `cc02b0d99d67e5a720502953c99307c8b991720d`. |
| 002 | Safety Gates | `CLOSED_CANONICAL` | 001 | Implementation merge `b637382fd9a0d8a02f71c11073a5276d61726bb6`; dedicated closure records final 54/9/157 exact-head qualification. |
| 003 | Data, License & Provenance | `CLOSED_CANONICAL` | 001 | Qualified implementation merge `a5fef84f9f0cee12dcd2ea6735888faee43db1ec`, tree `d7b2e11a8470ec66f50f1cff77bba4dddff20812`; final exact-head evidence: 71 focused / 9 hard-gate / 228 full tests and independent review with no material blocker. |
| 004 | Tournament Harness | `CLOSED_CANONICAL` | 001, 002, 003 | Qualified implementation merge `9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d`, tree `7e37fa626f825ee25271e0bf21a627a2e64e49da`; exact implementation head `cf6158ea4193aa7db895607c6fac5a3a1442f708`; closure merge `3dc705a1de09347f3574b305afb1bfaa6d46ecff`. Final 48 focused / 9 hard-gate / 276 full tests. Fixture/precomputed-results-only; no model or benchmark-payload execution authority. |
| 005 | Base Model Tournament | `CLOSED_CANONICAL` | 004 `CLOSED_CANONICAL` | Implementation `5e35cd4` (tree `5b823d20`, head `d4caf94`) + planning reconciliation `799c36a` (tree `eaa8942`, head `83d7612`); closure `CLOSED_CANONICAL` via this closeout. Deterministic control plane only; no model/benchmark/Private Gold/PHI/device/spend execution. 513 tests + exact-head reviews `d4caf94`/`83d7612` MATERIAL_BLOCKER=NO. |
| 006 | Patient Safety Scaffold & Deterministic Tools | `CLOSED_CANONICAL` | 002 `CLOSED_CANONICAL`, 005 `CLOSED_CANONICAL` | Implementation merge `4df3dc4eab5d3160d88b2f296dea62a8dd884b60` (tree `b5a88fa89c52335a2343d37d33bde32fb42d5082`, final head `09da2d1b4f6d21a1053967df0b4c3a68ea6078f3`) under founder authorization PR #40; planning reconciliation `a9d7f37ea1abc537e99bbb75dda2a5b1f8625a8f`. Final 114+51 focused / 627+128 full tests; exact-head reviews no remaining material blocker. Offline deterministic scope only; T017-T020 remain typed `NEEDS_EVIDENCE` fail-closed gates. See closeout for full binding. |
| 007 | SFT V1 | `AUTHORIZED_TO_START` | 003 `CLOSED_CANONICAL`, 005 `CLOSED_CANONICAL`, 006 `CLOSED_CANONICAL` | Specification canonical via PR #46 (`645da20`, final head `07fb71e`); clarification canonical via PR #49 / merge `16ae16b50680469fe14f44c1e3fdcb655d34b822`, qualified head `1919779ba87725b7d529ba35465dc546f61fbc13`; planning package canonical via PR #51 / merge `947f3aba4d4316e21470ac26352d96e3bfb74ae6`; bounded offline implementation closed; E001 candidate manifest frozen; E002 bounded public/ungated artifact access authorized. E003 remains a separate execution gate. `TRAINING_AUTHORITY=NONE`; `BACKBONE_WINNER=NEEDS_EVIDENCE`. See authorization records below. |
| 008 | Knowledge Strategy Ablation | `BLOCKED` | 007 | CPT vs no-CPT/distillation+retrieval. |
| 009 | Distillation V1 | `BLOCKED` | 008 | Minimum license-clean distillation; on-policy candidate. |
| 010 | RLVR V1 | `BLOCKED` | 009 | Verifiable tasks only; optional NO-GO outcome. |
| 011 | Calibration & Abstention | `BLOCKED` | relevant trained candidate | Selective risk and behavioral-state hardening. |
| 012 | Quantization & Device | `BLOCKED` | 011 | Medical re-gating on exact device/builds. |
| 013 | Arabic Deepening | `BLOCKED` | 007 + Arabic evaluation readiness | Fix measured Arabic gaps. |
| 014 | Multimodal Documents & Labs | `BLOCKED` | 004–006 | Unified-vs-structured perception falsification. |
| 015 | Human Evaluation | `BLOCKED` | patient/professional candidate + safety readiness | Patient comprehension and human+AI evidence. |
| 016 | Advanced Modality Adapters | `DEFERRED` | separate modality prerequisites | ECG, wearables, imaging volumes, WSI, audio/video etc. |
| 017 | Release Review & Paper | `BLOCKED` | all claimed capabilities | Independent review and claims package. |

## Spec 004 canonical closure record

Spec 004 has a qualified fixture/precomputed-results-only implementation canonically merged through [PR #28](https://github.com/TheHalfMoon/commandMed/pull/28):

```text
IMPLEMENTATION_MERGE=9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d
IMPLEMENTATION_TREE=7e37fa626f825ee25271e0bf21a627a2e64e49da
FINAL_REVIEWED_HEAD=cf6158ea4193aa7db895607c6fac5a3a1442f708
FINAL_VALIDATION_RUN=32603944702
FINAL_VALIDATION_JOB=97106155513
FOCUSED_SPEC004_TESTS=48/48 PASS
INHERITED_HARD_GATES=9/9 PASS
FULL_OFFLINE_SUITE=276/276 PASS
```

Direct implementation evidence:

- [GitHub Actions Run 32603944702](https://github.com/TheHalfMoon/commandMed/actions/runs/32603944702)
- [GitHub Actions Job 97106155513](https://github.com/TheHalfMoon/commandMed/actions/runs/32603944702/job/97106155513)
- [Fresh exact-head Qodo review result](https://github.com/TheHalfMoon/commandMed/pull/28#issuecomment-5383054440)
- [Qodo review update marker through exact `cf6158ea...`](https://github.com/TheHalfMoon/commandMed/pull/28#issuecomment-5383058920)

The fresh exact-head review reported no material correctness, security, scientific-integrity, lifecycle, authorization, deterministic-reporting, or execution-surface blocker. The guarded implementation merge used that exact head, after which canonical `main` was verified at `9ab91850f7cb7a5b7d8bfa4de8f006e9e669c89d` / tree `7e37fa626f825ee25271e0bf21a627a2e64e49da`. Temporary validation carrier PR #29 was closed without merge after evidence capture.

## Spec 004 dedicated closure transition

The implementation merge alone did not close Spec 004. The final closure-only transition ultimately reconciled seven lifecycle/governance records after review identified additional stale `ACTIVE` headers:

- `specs/004-tournament-harness/spec.md`
- `specs/004-tournament-harness/plan.md`
- `specs/004-tournament-harness/closeout.md`
- `specs/004-tournament-harness/tasks.md`
- `specs/004-tournament-harness/review-reconciliation.md`
- `specs/004-tournament-harness/checklists/requirements.md`
- `specs/README.md`

The first closure candidate head `45037b988bd716adc1750199df6c6069ff15f5ac` was rejected as closure authority after [Qodo closure review](https://github.com/TheHalfMoon/commandMed/pull/30#issuecomment-5383104852) found:

```text
C004-01 NONCANONICAL_CLOSEOUT_STATUS
C004-02 STALE_SPEC004_LIFECYCLE_ARTIFACTS
C004-03 UNLINKED_CI_REVIEW_EVIDENCE
```

Later review also identified stale Spec 004 `spec.md` / `plan.md` `ACTIVE` lifecycle headers. The final repaired closure head `4b08cbe02743a101ea258d26ac5245964e063055` reconciled those headers, preserved no-execution authority, and was independently reviewed with no material blocker before guarded merge.

Canonical closure is effective at:

```text
SPEC004_CLOSURE_MERGE=3dc705a1de09347f3574b305afb1bfaa6d46ecff
SPEC004_CLOSURE_TREE=3a33c0e13e870849c1f2c3bc1e26de3c5e62c563
FINAL_CLOSURE_HEAD=4b08cbe02743a101ea258d26ac5245964e063055
FINAL_CLOSURE_VALIDATION_RUN=32605817757
FINAL_CLOSURE_VALIDATION_JOB=97110591073
```

At the time of that closure, Spec 005 remained `BLOCKED` pending its separate founder decisions and explicit entry authorization. Those later founder prerequisites were subsequently satisfied canonically by PR #32 / merge `a68d37acd713049694106e81dc134ccf4d51feb9` for the specify stage only.

## Spec 005 specification boundary

Founder decisions `FD-001`, `FD-002`, and `FD-006` were canonically locked by PR #32 / merge `a68d37acd713049694106e81dc134ccf4d51feb9`. The dependency and founder-decision prerequisites for the **specify stage** are therefore satisfied.

Spec 005 is `AUTHORIZED_TO_SPECIFY` only. Its specification may define the tournament problem, inherited contracts, admission/comparability rules, fail-closed behavior, and questions that clarification must resolve. It must not freeze or execute a live tournament merely by naming candidate families.

Successful canonical definition of `specs/005-base-model-tournament/spec.md` advances only to a separately authorized clarification step.

## Planning rule

Do not generate detailed implementation plans for blocked future specs merely to make the repository look complete. Add detail only when the dependency frontier reaches that spec and explicit authorization exists.

## Branch/PR rule

Prefer one bounded spec per implementation branch/PR. A spec's merged closeout evidence, not mere code existence, is what can satisfy its dependency edge. Satisfying a dependency does not itself grant start authority to the dependent spec when separate founder decisions or explicit authorization are required.

## Spec 005 canonical closure record

Spec 005 deterministic control plane is canonically closed via:

```text
SPEC005_IMPLEMENTATION_PR=36
SPEC005_IMPLEMENTATION_HEAD=d4caf94952e77888755788b490d6a5267e5e3a9d
SPEC005_IMPLEMENTATION_MERGE=5e35cd423c54ce743b9b305287971a97eeeb7a64
SPEC005_IMPLEMENTATION_TREE=5b823d20fd1106669e1b79af4d301d15c5e4e8dd
SPEC005_RECONCILIATION_PR=37
SPEC005_RECONCILIATION_HEAD=83d76127df340b26350a79ccd4c6b2b266479ec6
SPEC005_RECONCILIATION_MERGE=799c36a9a6113357a6fa9b02a7178f94fad6ee0c
SPEC005_RECONCILIATION_TREE=eaa89429f996f2fed315ebc15462273dfa5125a4
SPEC005_CLOSEOUT_PR=<THIS_PR>
SPEC005_TASKS=49/49 checked with evidence mapping (tasks.md reconciled 2026-08-25)
FULL_OFFLINE_SUITE=513/513 PASS
QODO_REVIEWS=d4caf94 NO_FINDINGS, 83d7612 NO_FINDINGS
V1_SHA_PRESERVED=304c980ce4ce84c18f70115661089db29430d0166a630cd9e95948726d24143a
```

Planning reconciliation superseded stale PR #34 (`f116bea`) without deleting implementation. All `src/commandmed/spec005/*` + `tests/spec005/*` + `data/spec005/*` canonical. See `specs/005-base-model-tournament/closeout.md` for full binding. `SPEC_005=CLOSED_CANONICAL` effective after this closure merge.

## Spec 006 implementation authorization record

> Superseded 2026-08-25: Spec 006 has since been implemented (PR #41) and closed canonically; see the Spec 006 canonical closure record below and `specs/006-patient-safety-scaffold/closeout.md`. This section is preserved as historical authorization evidence.

The founder has explicitly authorized the bounded implementation of Spec 006. This authorization is recorded canonically here before any `src/commandmed/spec006` implementation begins.

```text
SPEC006_IMPLEMENTATION_AUTHORITY=AUTHORIZED_TO_START
QUALIFIED_PLANNING_PR=#39
QUALIFIED_PLANNING_BRANCH=spec/006-specify
QUALIFIED_PLANNING_HEAD=6308e40f5f134bae7acccd66c8aa695ad9bba8ba
QUALIFIED_PLANNING_REVIEW=MATERIAL_BLOCKER=NO (exact-head independent review)
IMPLEMENTATION_SCOPE=OFFLINE_DETERMINISTIC_SPEC006_ONLY
AUTHORIZED_TASKS=T011,T012,T013,T014,T015,T016,T021
EVIDENCE_GATE_TASKS=T017,T018,T019,T020 executed ONLY as typed fail-closed NEEDS_EVIDENCE records (validators must accept/reject such records; real clinical-score authorities, interaction-database identities, versioned Arabic/English emergency lexicons, and jurisdiction routing must NOT be fabricated)
TASKS_FILE_AT_QUALIFIED_HEAD=
  path=specs/006-patient-safety-scaffold/tasks.md
  git_blob_oid=3cf4e37808ff3621376bfa9da1403f91eaeba43a
  raw_bytes_sha256=fa44671dd8d85756ed909ff6dec9a5f5813b5a49605b42500c031c68f5da8ae8
```

### Supersession of earlier Spec 006 lifecycle text

The `specs/README.md` registry above is the single authoritative Spec 006 lifecycle state as of this authorization merge. Earlier canonical text that describes the post-005 state as `SPEC_006=AUTHORIZED_TO_SPECIFY` — including the "Execution and training authority" section of `specs/005-base-model-tournament/closeout.md` and the prior README authority block — is superseded by this record for the implementation-start stage only. Those statements remain accurate historical snapshots of their own merge points and are not rewritten. No other lifecycle field changes: all execution/training/data/spend authorities stay `NONE`.

### Planning exit-gate checklist (criterion → evidence)

| Exit criterion | Evidence |
|---|---|
| Bounded problem, exclusions, testable stories, verifiable FRs frozen | `spec.md` FR-001..FR-007 + explicit out-of-scope section at qualified head |
| Deterministic precedence + fail-closed semantics frozen | `research.md` §5–§6 (SP-001..SP-002 order, conflict → ABSTAIN/ESCALATE, reason-code vocabulary) |
| Tool registry contract frozen | `contracts/tool-registry.schema.json` (14 required fields, `network_required const false`, `execution_authority const NONE`) |
| Trace/seal/manifest trust model frozen | `data-model.md` §1.4–§1.5 + `contracts/{interaction-trace,trace-seal,fixture-manifest}.schema.json`; trusted commit OID out-of-band |
| Typed evidence prerequisites marked, not fabricated | `checklists/requirements.md` FR-006 `[~]`, FR-007 `[~]`; T017..T020 unexecuted |
| Static analyze clean | `analysis.md`: CRITICAL=0 HIGH=0 MEDIUM=0 RESULT=PASS (planning) |
| Independent exact-head review qualified | Qodo review of PR #39 head `6308e40` MATERIAL_BLOCKER=NO |
| Baseline preserved | 513 tests + 77 subtests PASS, `compileall` PASS, worktree clean at `52f799b` |

Scope boundary: this authorizes offline deterministic software implementation of the frozen qualified planning package only. It does NOT grant model execution, model-weight access, model conversion, training, benchmark payload access/execution, Private Gold access, PHI access, device execution, external clinical database access, credential access, or any spend.

```text
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
EXTERNAL_CLINICAL_DATABASE_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Spec 006 canonical closure record

Spec 006 patient safety scaffold is canonically closed via:

```text
SPEC006_AUTHORIZATION_PR=40
SPEC006_AUTHORIZATION_MERGE=18d26f75506cfd60de03caabe2083ff96eafa762
QUALIFIED_PLANNING_PR=39 (superseded by #42, head 6308e40f5f134bae7acccd66c8aa695ad9bba8ba)
SPEC006_IMPLEMENTATION_PR=41
SPEC006_IMPLEMENTATION_HEAD=09da2d1b4f6d21a1053967df0b4c3a68ea6078f3
SPEC006_IMPLEMENTATION_MERGE=4df3dc4eab5d3160d88b2f296dea62a8dd884b60
SPEC006_IMPLEMENTATION_TREE=b5a88fa89c52335a2343d37d33bde32fb42d5082
SPEC006_RECONCILIATION_PR=42
SPEC006_RECONCILIATION_HEAD=9f59932496d09a41ba4da5cda4347c4dd1cbd243
SPEC006_RECONCILIATION_MERGE=a9d7f37ea1abc537e99bbb75dda2a5b1f8625a8f
SPEC006_CLOSEOUT_PR=<THIS_PR>
SPEC006_TASKS=22/22 (T017-T020 as typed NEEDS_EVIDENCE fail-closed gates)
FULL_OFFLINE_SUITE=627 passed + 128 subtests PASS
QODO_REVIEWS=09da2d1 NO_MATERIAL_BLOCKER, 9f59932 NO_MATERIAL_BLOCKER
EVIDENCE_GATES_CARRIED_FORWARD=T017,T018,T019,T020 NEEDS_EVIDENCE
```

See `specs/006-patient-safety-scaffold/closeout.md` for full binding. `SPEC_006=CLOSED_CANONICAL` effective after this closure merge and resulting canonical `main` verification.

## Spec 007 specification authorization record

The founder approved the Spec 007 entry gate after the Spec 006 canonical closure unblocked its dependency edges. Recorded canonically here before any `specs/007-*` artifact begins.

```text
SPEC007_SPECIFICATION_AUTHORITY=AUTHORIZED_TO_SPECIFY
AUTHORIZATION_DATE=2026-08-25
DEPENDENCY_EDGES_SATISFIED=003 CLOSED_CANONICAL, 005 CLOSED_CANONICAL, 006 CLOSED_CANONICAL
IMPLEMENTATION_SCOPE=SPECIFICATION_STAGE_ONLY
AUTHORIZED_STAGE=specify (Spec Kit: define bounded problem, exclusions, testable stories, verifiable FRs, typed evidence prerequisites, no implied execution authority)
```

Scope boundary: this authorizes **specification-stage work only**. It does NOT authorize clarification beyond the specify stage's own gate, planning, implementation, or any execution. Training authority remains explicitly withheld:

```text
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
EXTERNAL_CLINICAL_DATABASE_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Each later Spec 007 lifecycle transition (`AUTHORIZED_TO_PLAN`, implementation start, and especially any training run) requires a separate explicit founder authorization recorded in this register before work begins.

## Spec 007 clarification authorization record

The founder approved the Spec 007 clarification stage after the specification merged canonically. Recorded here before any clarification artifact begins.

```text
SPEC007_CLARIFICATION_AUTHORITY=AUTHORIZED_TO_CLARIFY
AUTHORIZATION_DATE=2026-08-26
CANONICAL_SPEC007_MERGE=645da20263fc44d1ed8977024cf2df57aa6f7465
QUALIFIED_SPECIFICATION_HEAD=07fb71e60e783cb9b689c97e08eb8b001b056cfe
QUALIFIED_SPECIFICATION_REVIEW=NO_MATERIAL_BLOCKER
AUTHORIZED_STAGE=clarify
MODEL_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
PI_MODEL_SELECTION_AUTHORITY=NONE
BACKBONE_WINNER=NEEDS_EVIDENCE
```

Hard boundary: candidate-model selection and final backbone-winner selection are reserved exclusively to FOUNDER+CHATGPT. PI must not choose, rank, eliminate, recommend, or freeze any model lineage, and must not substitute a likely winner for missing evidence. When planning requires a concrete model identity it is recorded only as:

```text
BACKBONE_WINNER=NEEDS_EVIDENCE
OWNER=FOUNDER+CHATGPT
EVIDENCE_KIND=AUTHORIZED_TOURNAMENT_RESULT
```

Scope boundary: this authorizes the clarification lifecycle plus ordinary non-destructive repository work to qualify and canonicalize that stage. All execution authorities remain withheld:

```text
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
EXTERNAL_CLINICAL_DATABASE_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Decision-register T-001 remains TEST_BEFORE_LOCK: clarification may identify what evidence the future tournament must return to satisfy Spec 007 binding, but must not resolve T-001, run the tournament, or choose a winner.

## Spec 007 planning authorization record

The founder explicitly approved a real, strengthened Spec 007 planning package on 2026-08-27 after PR #49 made the clarification/research artifacts canonical. This authorization is recorded before any planning artifact becomes canonical.

```text
SPEC007_PLANNING_AUTHORITY=AUTHORIZED_TO_PLAN
AUTHORIZATION_DATE=2026-08-27
CANONICAL_CLARIFICATION_PR=#49
CANONICAL_CLARIFICATION_MERGE=16ae16b50680469fe14f44c1e3fdcb655d34b822
QUALIFIED_CLARIFICATION_HEAD=1919779ba87725b7d529ba35465dc546f61fbc13
QUALIFIED_CLARIFICATION_REVIEW=MATERIAL_BLOCKER=NO (CodeRabbit exact-head review)
AUTHORIZED_STAGE=plan
PLANNING_SCOPE=COMPLETE_NON_EXECUTING_SPEC_KIT_PLANNING_PACKAGE
MODEL_CANDIDATE_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
BACKBONE_WINNER_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
PI_MODEL_SELECTION_AUTHORITY=NONE
BACKBONE_WINNER=NEEDS_EVIDENCE
```

Planning authority permits the complete non-executing planning lifecycle for Spec 007: `plan.md`, additional bounded research needed by planning, data-model/contracts/quickstart, requirements checklist, dependency-ordered tasks, and static analyze/qualification artifacts. It does not authorize implementation or any runtime/model/data/device/spend activity.

The planning package must preserve the founder's research objective — maximize **verified medical usefulness and safety per byte, joule, second, peak RAM, shipped GB, parameter, and reasoning token** — while keeping record/SOTA claims narrower than independently reproducible evidence. It may define record-class scoreboards and future experiments, but it must not fabricate a record or select a model.

```text
TRAINING_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
EXTERNAL_CLINICAL_DATABASE_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Decision-register T-001 remains `TEST_BEFORE_LOCK`. Planning may define the candidate-decision packet, record-class definitions, tournament evidence requirements, training contracts, and future handoffs, but only Founder + ChatGPT may freeze candidates and select the final backbone after separately authorized tournament evidence exists.

## Execution and training authority

This is the repository-wide **current-state** authority summary. It supersedes earlier historical lifecycle/grant snapshots below only for current authority. E002 authorizes bounded, non-executing access to the exact frozen E001 public/ungated candidate artifacts; it does not authorize model execution or any later gate.

```text
SPEC_005=CLOSED_CANONICAL
SPEC_005_LIFECYCLE_AUTHORITY=CLOSED_CANONICAL (control-plane only)
SPEC_006=CLOSED_CANONICAL
SPEC_006_LIFECYCLE_AUTHORITY=IMPLEMENTATION_ONLY (offline deterministic)
SPEC_007=AUTHORIZED_TO_START
E001=CLOSED_CANONICAL
E002_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
MODEL_WEIGHT_ACCESS_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
MODEL_WEIGHT_ACCESS_SCOPE=PUBLIC_UNGATED_EXACT_FROZEN_E001_CANDIDATES_ONLY
E003_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AGAINST_MODELS=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
PHI_RESTRICTED_DATA_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_PAYLOAD_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
BACKBONE_WINNER=NEEDS_EVIDENCE
```

Current E002 scope is defined by `specs/007-sft-v1/e002-model-access-authorization-2026-08-27.md`. Historical blocks below remain evidence of what their specific earlier grants did and did not authorize; they are not the current aggregate authority state.

## Spec 007 implementation authorization record

Founder authorization on 2026-08-27 advances Spec 007 from `AUTHORIZED_TO_PLAN` to `AUTHORIZED_TO_START` for the bounded **offline deterministic implementation control plane only**.

```text
SPEC007_IMPLEMENTATION_AUTHORITY=AUTHORIZED_TO_START
AUTHORIZATION_DATE=2026-08-27
CANONICAL_PLANNING_PR=#51
CANONICAL_PLANNING_MERGE=947f3aba4d4316e21470ac26352d96e3bfb74ae6
CANONICAL_PLANNING_TREE=faa5c15c84dbd84d162b6ba6850bbc312584203b
QUALIFIED_PLANNING_HEAD=701c933acdf84572f627446e5199231236f97988
QUALIFIED_PLANNING_TREE=faa5c15c84dbd84d162b6ba6850bbc312584203b
P013_VALIDATED_SUBJECT_SHA=701c933acdf84572f627446e5199231236f97988
P013_VALIDATED_SUBJECT_TREE=faa5c15c84dbd84d162b6ba6850bbc312584203b
P013_VALIDATION_RUN=33040059680
P013_VALIDATION_JOB=98411371329
P013_WORKFLOW_CARRIER_SHA=65973326632d07bb63cab03d9ab696b5f1f0c375
P013_WORKFLOW_CARRIER_ROLE=TRIGGER_ONLY_NOT_VALIDATED_SUBJECT
P013_EXACT_CHECKOUT_BINDING=JOB_98411371329_CHECKOUT_AND_VERIFY_HEAD_BOTH_EQUAL_VALIDATED_SUBJECT_SHA
P013_COMPILEALL=PASS
P013_PYTEST=627 passed + 128 subtests
P013_GIT_DIFF_CHECK=PASS
FINAL_QODO_REVIEW=MATERIAL_BLOCKER=NO
FINAL_CODERABBIT_REVIEW=MATERIAL_BLOCKER=NO
AUTHORIZED_IMPLEMENTATION_TASKS=I001-I045
AUTHORIZED_SCOPE=OFFLINE_DETERMINISTIC_SPEC007_CONTROL_PLANE_ONLY
```

This authorization permits implementation and qualification of the dependency-ordered I-phase validators, identity/serialization utilities, synthetic fixtures, quarantine/provenance composition, rendering/loss/packing policies, Arabic/language evidence shapes, checkpoint-selection policy enforcement, reproducibility/resume records, record/resource/efficiency/failure contracts, non-executing run-manifest composition, activation preflight, and their offline tests.

It does **not** authorize any E-phase external-evidence activity and grants none of the following:

```text
MODEL_CANDIDATE_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
BACKBONE_WINNER_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
PI_MODEL_SELECTION_AUTHORITY=NONE
BACKBONE_WINNER=NEEDS_EVIDENCE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
EXTERNAL_CLINICAL_DATABASE_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

P013 exact-subject binding: workflow carrier `65973326632d07bb63cab03d9ab696b5f1f0c375` is trigger-only. Job `98411371329` explicitly checked out and verified `701c933acdf84572f627446e5199231236f97988` (tree `faa5c15c84dbd84d162b6ba6850bbc312584203b`) before compileall, full pytest, and diff-check. The validated subject tree equals the canonical planning merge tree.

The implementation authorization above is a historical grant-specific boundary. Its statement that `E001-E015` were blocked and model-weight access was `NONE` remains true for that grant. Current Phase E authority is governed by the current-state summary above and the later E001/E002 decision records: E001 is closed, E002 is boundedly authorized, and E003-E015 remain separately gated.

A pilot, smoke-train, one-step gradient probe, adapter run, model load, benchmark execution, or empirical convergence test remains a training/model-execution activity and is not authorized by E002.

Implementation must remain fail-closed, offline, deterministic, synthetic-fixture based, and consistent with Specs 002, 003, 005, and 006. Exact-head implementation review and repository regression evidence remain required before any implementation merge.
