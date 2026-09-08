# E004 Operational Preflight V3 Attempt Founder Decision Request — 2026-09-08

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical V2 failure reconciliation:** `specs/007-sft-v1/e004-operational-preflight-evidence-run-v2-failure-reconciliation-2026-09-08.md`  
**Canonical current-state overlay:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v51-2026-09-08.md`  
**Decision owner:** Founder  
**Artifact class:** Founder decision request only  
**Authority effect before exact post-canonical selection:** NONE  
**Execution effect:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Request a new explicit Founder decision after the single authorized V2 operational-preflight evidence attempt terminated fail-closed and permanently consumed its one-shot allowance.

This request does not rerun, retry, replay, replace, reinterpret, or reclassify V1 or V2. It creates no new implementation, runtime, empirical, model, evaluation, tournament, A15, training, credential, procurement, payment, or spend authority by itself.

## 2. Canonical evidence requiring a new decision

The canonical V2 evidence identity is:

```text
V2_EVIDENCE_RUN_ID=34176481565
V2_EVIDENCE_JOB_ID=101906795703
V2_EVIDENCE_RUN_ATTEMPT=1
V2_EVIDENCE_RUN_HEAD=225d0ebe280a4ae2305dcc84dd5795ba90d198d0
V2_EVIDENCE_RUN_CONCLUSION=failure
V2_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_RERUN_AUTHORITY=NONE
V2_RETRY_AUTHORITY=NONE
V2_REPLAY_AUTHORITY=NONE
```

The V2 run passed the one-run authority guard, public/ungated access boundary, host/resource observation, and exact llama.cpp no-model runtime reconstruction. It then failed in the Transformers/Torch dependency-set reconstruction.

The exact observed dependency frontier is:

```text
EXPECTED_DEPENDENCY_ARTIFACT_COUNT=27
OBSERVED_DEPENDENCY_ARTIFACT_COUNT=28
DEPENDENCY_ARTIFACT_COUNT_GATE=FAIL
EXPECTED_DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
ACTUAL_DEPENDENCY_SET_MANIFEST_SHA256=NOT_CAPTURED
TRANSFORMERS_RUNTIME_RECONSTRUCTION=FAILED_BEFORE_VENV_INSTALL
```

The exact failing gate was:

```bash
test "$(wc -l < "$manifest" | tr -d ' ')" = "$DEPENDENCY_ARTIFACT_COUNT"
```

Because the count equality test failed before the later checks, the V2 evidence did not execute the dependency-manifest digest comparison, virtual-environment creation, offline dependency installation, installed-environment digest validation, Python-runtime digest validation, offline Transformers/Torch static imports, or the post-staging default-deny network proof.

The observed evidence proves dependency-set drift relative to the frozen 27-artifact contract. It does not establish a package-level causal explanation. No filename, package, wheel, platform, Python, resolver, or upstream-artifact cause may be treated as proven without direct evidence.

Cleanup passed, workflow artifact count was zero, and V2 performed no model-weight acquisition, model load, inference, generation, evaluation-payload execution, benchmark, tournament, A15 activation, training, paid compute, procurement, payment, or spend.

## 3. Decision A — remain blocked

Exact Founder selection:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION=E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION_A
```

Decision A means:

```text
V3_OPERATIONAL_PREFLIGHT_IMPLEMENTATION_AUTHORITY=NONE
V3_OPERATIONAL_PREFLIGHT_STATIC_QUALIFICATION_AUTHORITY=NONE
V3_OPERATIONAL_PREFLIGHT_RUNTIME_PROVISIONING_AUTHORITY=NONE
V3_OPERATIONAL_PREFLIGHT_EMPIRICAL_ATTEMPT_AUTHORITY=NONE
NEW_OPERATIONAL_PREFLIGHT_EVIDENCE_ATTEMPT_AUTHORITY=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
```

No V3 operational-preflight implementation or empirical attempt is prepared or executed.

## 4. Decision B — authorize one separately versioned V3 attempt

Recommended exact Founder selection:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION=E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION_B
```

Only after this exact token is supplied **after this decision request is canonically merged** and then separately captured canonically, Decision B authorizes the following bounded sequence:

1. prepare a new review-first V3 operational-preflight implementation from the then-current canonical `main`;
2. preserve the consumed V1 and V2 histories unchanged;
3. use new V3 workflow, evidence branch, and evidence marker surfaces rather than rerunning or reusing V1/V2;
4. repair V2's observability ordering prospectively so the actual dependency artifact count, sorted artifact manifest, and actual dependency-set manifest SHA-256 are emitted before any fail-closed expected-count or expected-digest equality check;
5. keep the frozen V2 dependency contract historical and immutable;
6. prohibit silently rebasing the expected dependency set to current resolver output;
7. require any prospective V3 expected dependency-set update to be explicit, versioned, reviewable, justified by direct evidence, and canonically bound before the empirical V3 trigger;
8. statically qualify the exact V3 implementation head without executing the empirical V3 lane;
9. guarded-merge the qualified V3 implementation canonically;
10. create exactly one marker-only direct-child commit on the exact V3 evidence branch from the exact canonical V3 implementation merge;
11. execute exactly one new V3 operational-preflight empirical attempt, run attempt 1 only;
12. treat that first V3 run as consuming the complete V3 empirical allowance regardless of PASS, INCOMPLETE, FAIL, infrastructure failure, or guard failure;
13. reconcile the observed V3 result append-only without automatic retry, rerun, replay, second marker, alternate branch, or replacement attempt.

The reserved V3 surfaces are:

```text
V3_WORKFLOW_PATH=.github/workflows/e004-operational-preflight-evidence-v3.yml
V3_EVIDENCE_BRANCH=evidence/e004-operational-preflight-run-v3
V3_EVIDENCE_MARKER=.github/e004-operational-preflight-run-v3.txt
MAX_AUTHORIZED_V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
V3_RUN_ATTEMPT_REQUIRED=1
V3_RERUN_AUTHORITY=NONE_BY_DEFAULT
V3_FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
```

## 5. Required V3 observability and fail-closed behavior

A Decision B V3 implementation must preserve or strengthen the V2 security and authority boundaries while repairing only prospective observability and any separately evidenced dependency-contract defect.

At minimum, before dependency equality gates, V3 must emit into the job log:

```text
ACTUAL_DEPENDENCY_ARTIFACT_COUNT=<observed integer>
ACTUAL_DEPENDENCY_SET_MANIFEST_SHA256=<observed sha256>
ACTUAL_DEPENDENCY_ARTIFACT_MANIFEST_BEGIN
<sorted basename<TAB>size<TAB>sha256 records>
ACTUAL_DEPENDENCY_ARTIFACT_MANIFEST_END
```

Then it must fail closed if the canonically bound expected count or expected digest does not match.

```text
SILENT_DEPENDENCY_CONTRACT_REBASE=PROHIBITED
V2_HISTORICAL_EXPECTED_DEPENDENCY_SET_MUTATION=PROHIBITED
V3_OBSERVED_DEPENDENCY_MANIFEST_CAPTURE_BEFORE_EQUALITY_GATE=REQUIRED
PROSPECTIVE_V3_EXPECTED_DEPENDENCY_SET_UPDATE=SEPARATE_EXPLICIT_CANONICAL_BINDING_REQUIRED
PACKAGE_LEVEL_ROOT_CAUSE=UNKNOWN_UNTIL_DIRECTLY_EVIDENCED
```

Decision B does not authorize treating the observed count of 28 as correct by declaration.

## 6. Review-first execution separation

Any V3 implementation authorized by Decision B must retain strict separation:

```text
PULL_REQUEST_PATH=STATIC_QUALIFICATION_ONLY
PULL_REQUEST_EMPIRICAL_JOB=SKIPPED
WORKFLOW_DISPATCH=ABSENT
REPOSITORY_DISPATCH=ABSENT
SCHEDULE=ABSENT
EMPIRICAL_TRIGGER=EXACT_V3_EVIDENCE_BRANCH_PLUS_EXACT_MARKER_ONLY
EMPIRICAL_TRIGGER_PARENT=EXACT_CANONICAL_V3_IMPLEMENTATION_MERGE
EMPIRICAL_RUN_ATTEMPT=1_ONLY
```

Static qualification cannot be represented as empirical operational-preflight evidence.

## 7. Non-expansion boundary

Decision B, if later selected and canonically captured, does **not** authorize any of the following:

```text
V1_RERUN=PROHIBITED
V1_RETRY=PROHIBITED
V1_REPLAY=PROHIBITED
V2_RERUN=PROHIBITED
V2_RETRY=PROHIBITED
V2_REPLAY=PROHIBITED
V2_SECOND_MARKER=PROHIBITED
MODEL_WEIGHT_ACQUISITION=PROHIBITED
MODEL_LOAD=PROHIBITED
MODEL_FORWARD_PASS=PROHIBITED
MODEL_INFERENCE=PROHIBITED
TOKEN_GENERATION=PROHIBITED
EVALUATION_PAYLOAD_ACCESS=PROHIBITED
EVALUATION_PAYLOAD_EXECUTION=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
TOURNAMENT_EXECUTION=PROHIBITED
WINNER_SELECTION=PROHIBITED
MODEL_CONVERSION=PROHIBITED
A15_ACTIVATION=PROHIBITED
TRAINING=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
PHI_ACCESS=PROHIBITED
GATED_ASSET_ACCESS=PROHIBITED
PRIVATE_CREDENTIAL_USE=PROHIBITED
PAID_OR_LARGER_RUNNER=PROHIBITED
SELF_HOSTED_RUNNER=PROHIBITED
GPU_RUNNER=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
SPEND=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

A future V3 PASS would be evidence only for fields directly observed by that V3 run. It would not itself activate A15, bind a tournament execution subject, authorize tournament execution, select a model winner, authorize conversion, or authorize training.

## 8. Exact post-canonical selection rule

At authoring time no V3 selection is active.

```text
POST_CANONICAL_EXACT_V3_FOUNDER_DECISION_TOKEN=ABSENT
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION=ABSENT
V3_OPERATIONAL_PREFLIGHT_IMPLEMENTATION_AUTHORITY=NONE
V3_OPERATIONAL_PREFLIGHT_STATIC_QUALIFICATION_AUTHORITY=NONE
V3_OPERATIONAL_PREFLIGHT_RUNTIME_PROVISIONING_AUTHORITY=NONE
V3_OPERATIONAL_PREFLIGHT_EMPIRICAL_ATTEMPT_AUTHORITY=NONE
NEW_OPERATIONAL_PREFLIGHT_EVIDENCE_ATTEMPT_AUTHORITY=NONE
```

Generic continuation language, ordinary approvals, `go ahead`, `all permissions`, prior Founder directives, and the consumed V1/V2 decisions do not match either exact V3 token and cannot create V3 authority.

The recommended Decision B token is deliberately not self-executing. It must be supplied by the Founder in a later message after this decision request is canonical.

For later exact identity capture, the recommended Decision B token line has:

```text
V3_DECISION_B_TOKEN_SHA256=e21b6faea3700c716d702ff80b13269721083f9e0ea06b33e215d289f0930fdf
```

## 9. Decision criteria

Decision B is appropriate only if the Founder accepts all of the following:

- V1 and V2 remain permanently consumed historical evidence;
- neither failed run is rewritten as PASS;
- V3 is a new versioned one-shot attempt, not a retry of V2;
- V3 remains no-model, no-evaluation-payload, zero-spend, and bounded to public runtime-preflight evidence;
- the observed 28-artifact V2 result is not silently promoted into a new expected contract;
- V3 captures the actual dependency manifest and digest before fail-closed equality checks;
- any prospective V3 expected dependency-set change requires direct evidence and an explicit canonical binding;
- exact-head static qualification and guarded canonical merge occur before the V3 marker exists;
- one V3 empirical run attempt consumes the entire V3 allowance regardless of conclusion;
- no automatic retry follows a V3 failure;
- A1-A14 applicability, A15 activation, tournament execution, winner selection, model conversion, and training remain separate downstream gates.

## 10. Current disposition

Until an exact post-canonical selection is supplied and separately captured:

```text
CURRENT_GLOBAL_FRONTIER=EXACT_POST_CANONICAL_FOUNDER_V3_OPERATIONAL_PREFLIGHT_ATTEMPT_DECISION
V1_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_TERMINAL_FAILURE
V3_DECISION_SURFACE=READY_FOR_CANONICALIZATION
POST_CANONICAL_V3_DECISION=ABSENT
NEW_V3_IMPLEMENTATION_AUTHORITY=NONE
NEW_V3_EMPIRICAL_ATTEMPT_AUTHORITY=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```
