# Spec 007 — SFT V1 Implementation Authorization

**Date:** 2026-08-27
**Lifecycle:** `AUTHORIZED_TO_START`
**Authorized scope:** offline deterministic Spec 007 control plane only
**Training authority:** NONE
**Model execution authority:** NONE

## Canonical planning evidence

```text
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
```

## Exact-subject validation binding

Run `33040059680` is triggered by carrier `65973326632d07bb63cab03d9ab696b5f1f0c375`, but job `98411371329` explicitly checks out and verifies subject `701c933acdf84572f627446e5199231236f97988` / tree `faa5c15c84dbd84d162b6ba6850bbc312584203b` before the required checks. The subject tree equals the canonical planning merge tree; the carrier is not treated as the validated content.

## Founder authorization

The Founder explicitly directed the project to proceed on 2026-08-27 after the planning package became canonical. This record interprets that direction narrowly and fail-closed: implementation may begin only for the I-phase offline deterministic control plane described by the canonical Spec 007 task graph.

```text
SPEC007_IMPLEMENTATION_AUTHORITY=AUTHORIZED_TO_START
AUTHORIZED_IMPLEMENTATION_TASKS=I001-I045
AUTHORIZED_SCOPE=OFFLINE_DETERMINISTIC_SPEC007_CONTROL_PLANE_ONLY
```

## Permitted implementation

Permitted work includes only repository-local deterministic validators, canonical identity/serialization, strict record parsing, synthetic fixtures, provenance/quarantine composition, rendering/loss/packing contracts, language/Arabic evidence packet validation, selection-policy enforcement, reproducibility/resume records, resource/efficiency/failure contracts, non-executing run-manifest composition, activation preflight, and offline tests/review qualification.

Implementation must prefer existing repository mechanisms and stdlib/native facilities over new frameworks or services. No network, credentials, model runtime, benchmark payload, PHI, Private Gold, device execution, or paid service is required or permitted.

## Exclusions

The following authorities and activities are explicitly outside this bounded implementation authorization:

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

`E001-E015` are not activated by this record. No candidate model may be selected, ranked, eliminated, recommended as canonical, downloaded, loaded, converted, inferred, benchmarked, trained, fine-tuned, or used in a pilot under this authority. No real benchmark payload, Private Gold payload, PHI, restricted clinical database, credential, paid provider, or device execution may be used.

## Exit Evidence

The implementation merge gate is fail-closed. Each criterion below must have concrete evidence on the **same exact implementation head**; `NEEDS_EVIDENCE` is not a pass state. Any implementation-head movement invalidates prior exact-head qualification and requires the affected evidence to be regenerated.

| Exit criterion | Required concrete evidence | Status at authorization | Canonical reference / future evidence slot |
|---|---|---|---|
| I-phase task/evidence map complete | `specs/007-sft-v1/tasks.md` with I001-I045 completion mapped to implementation paths/tests; no E-task falsely checked | `NEEDS_EVIDENCE` | `specs/007-sft-v1/tasks.md` |
| Focused Spec 007 tests pass | Exact-head command output and test count for the dedicated Spec 007 test surface | `NEEDS_EVIDENCE` | future implementation qualification run/job ID |
| Full offline regression passes | Exact-head `pytest -q` output with actual repository-wide count | `NEEDS_EVIDENCE` | future implementation qualification run/job ID |
| Python compilation passes | Exact-head `python3 -m compileall -q src tests` result | `NEEDS_EVIDENCE` | future implementation qualification run/job ID |
| Diff hygiene passes | `git diff --check <canonical-implementation-base> <exact-implementation-head>` output | `NEEDS_EVIDENCE` | future implementation qualification run/job ID |
| Authority boundary remains closed | Exact-head inspection proving E001-E015 remain gated and model/weight/training/benchmark/PHI/Private Gold/device/credential/spend authority remains `NONE` | `NEEDS_EVIDENCE` | implementation PR review record |
| Independent exact-head review passes | Fresh Qodo and CodeRabbit (or canonical independent-review substitute if one service is unavailable) with no unresolved material blocker on the exact implementation SHA | `NEEDS_EVIDENCE` | implementation PR review/comment references |
| Review threads reconciled | Zero unresolved material review threads; every valid finding repaired and requalified | `NEEDS_EVIDENCE` | implementation PR thread listing |
| Worktree/artifact scope remains bounded | Changed-file evidence limited to authorized offline deterministic implementation, tests, fixtures, and required lifecycle reconciliation | `NEEDS_EVIDENCE` | implementation PR changed-file set |

The planning evidence above is already complete and authorizes entry into implementation; it is not a substitute for the implementation-exit evidence in this table. Implementation merge is prohibited until every row reaches a concrete `PASS`/satisfied state with exact-head evidence.