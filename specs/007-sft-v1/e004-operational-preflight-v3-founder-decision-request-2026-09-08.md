# E004 Operational Preflight V3 Founder Decision Request — 2026-09-08

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Decision owner:** Founder
**Canonical V2 failure reconciliation merge:** `89f3bd245905f016c7c133c84dd47b65c62a8a2f`
**V2 evidence run:** `34176481565`
**V2 evidence job:** `101906795703`
**V2 failure reconciliation:** `specs/007-sft-v1/e004-operational-preflight-evidence-run-v2-failure-reconciliation-2026-09-08.md`
**Current-state overlay:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v51-2026-09-08.md`
**Artifact class:** Founder decision request only
**Authority effect before exact post-canonical selection:** NONE
**Execution effect:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Request a new explicit Founder decision after the single V2 operational-preflight evidence allowance was consumed by terminal dependency-set drift.

V2 proved the corrected ancestry guard, public/ungated access boundary, credential boundary, runner/resource observation, exact llama.cpp runtime reconstruction, and cleanup. It failed closed because the live Transformers/Torch resolver produced 28 dependency artifacts while the frozen contract expected 27.

This request does not rerun, retry, replay, amend, reinterpret, or reclassify V1 or V2. It creates no new implementation or empirical authority by itself.

## 2. Canonical evidence requiring a separate V3 decision

```text
V2_EVIDENCE_RUN_ID=34176481565
V2_EVIDENCE_JOB_ID=101906795703
V2_EVIDENCE_RUN_ATTEMPT=1
V2_EVIDENCE_RUN_HEAD=225d0ebe280a4ae2305dcc84dd5795ba90d198d0
V2_EVIDENCE_RUN_CONCLUSION=failure
V2_AUTHORIZED_RUNS_EXECUTED=1
V2_AUTHORIZED_RUNS_REMAINING=0
V2_RERUN_AUTHORITY=NONE
V2_RETRY_AUTHORITY=NONE
EXPECTED_DEPENDENCY_ARTIFACT_COUNT=27
OBSERVED_DEPENDENCY_ARTIFACT_COUNT=28
ACTUAL_DEPENDENCY_SET_MANIFEST_SHA256=NOT_CAPTURED
OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_FAIL_CLOSED_TRANSFORMERS_DEPENDENCY_SET_DRIFT
```

The V2 failure occurred before the dependency-manifest hash comparison, venv creation/install, installed-environment verification, Python-runtime verification, offline Transformers/Torch static imports, and post-staging network proof.

A future attempt must not merely change the expected artifact count from 27 to 28. The exact dependency set must first be captured, reviewed, frozen, and qualified prospectively.

## 3. Decision A — remain blocked

Exact Founder selection:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_DECISION=E004_OPERATIONAL_PREFLIGHT_V3_DECISION_A
```

Decision A means:

```text
V3_IMPLEMENTATION_PREPARATION_AUTHORITY=NONE
V3_DEPENDENCY_SET_PREPARATION_AUTHORITY=NONE
V3_STATIC_QUALIFICATION_AUTHORITY=NONE
V3_EMPIRICAL_EVIDENCE_RUN_AUTHORITY=NONE
NEW_OPERATIONAL_PREFLIGHT_EVIDENCE_ATTEMPT_AUTHORITY=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
```

No V3 workflow, dependency-set lock, marker, or empirical run is prepared or executed.

## 4. Decision B — authorize one separately versioned V3 attempt

Recommended exact Founder selection:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_DECISION=E004_OPERATIONAL_PREFLIGHT_V3_DECISION_B
```

Exact Decision B token SHA-256:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_DECISION_TOKEN_SHA256=ed76f9a9259201bfd84a66f33a41b2e4e7f02a2f101b2bd2582e054a7c8bc0e7
```

Only after this exact token is supplied **after this decision request is canonically merged** and then separately captured canonically, Decision B authorizes this dependency-ordered sequence:

1. prepare a new review-first V3 operational-preflight implementation from the then-current canonical `main`;
2. preserve V1 and V2 historical evidence and exhausted allowances unchanged;
3. use only new V3 workflow/branch/marker surfaces;
4. perform bounded review-first dependency-set preparation on pull-request CI using only the exact public runtime dependency source families already admitted;
5. capture the complete resolved dependency artifact list, per-artifact size and SHA-256, artifact count, and aggregate manifest SHA-256 in a versioned repository evidence-lock artifact before any empirical V3 attempt;
6. qualify the exact committed dependency lock by resolving the same exact direct requirements again and requiring exact equality to the committed list/count/digests;
7. perform the remaining static repository policy/regression/diff qualification on the exact V3 implementation head;
8. guarded-merge only an exact head whose dependency-set qualification and repository qualification pass;
9. create exactly one marker-only direct-child commit on the exact V3 evidence branch from the exact V3 implementation merge;
10. execute exactly one V3 empirical operational-preflight run, attempt 1 only;
11. reconcile the observed V3 result append-only as PASS, INCOMPLETE, or FAIL;
12. do not retry, rerun, replay, or create a second V3 attempt absent a later separate authority.

## 5. Reserved V3 surfaces

```text
V3_WORKFLOW_PATH=.github/workflows/e004-operational-preflight-evidence-v3.yml
V3_DEPENDENCY_LOCK_PATH=specs/007-sft-v1/e004-operational-preflight-v3-dependency-set-v1.tsv
V3_EVIDENCE_BRANCH=evidence/e004-operational-preflight-run-v3
V3_EVIDENCE_MARKER=.github/e004-operational-preflight-run-v3.txt
MAX_AUTHORIZED_V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
V3_RUN_ATTEMPT_REQUIRED=1
V3_RERUN_AUTHORITY=NONE_BY_DEFAULT
V3_FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
```

V1 and V2 surfaces remain immutable historical evidence and may not be reused for V3 execution.

## 6. Review-first dependency-set preparation boundary

If Decision B becomes canonical, pull-request qualification may download **runtime dependency artifacts only** for the purpose of constructing and verifying the exact dependency-set lock.

```text
V3_PR_DEPENDENCY_RESOLUTION_AUTHORITY=AUTHORIZED_PUBLIC_RUNTIME_ARTIFACTS_ONLY
V3_PR_MODEL_WEIGHT_ACQUISITION=PROHIBITED
V3_PR_MODEL_LOAD=PROHIBITED
V3_PR_MODEL_INFERENCE=PROHIBITED
V3_PR_EVALUATION_PAYLOAD_ACCESS=PROHIBITED
V3_PR_BENCHMARK_EXECUTION=PROHIBITED
V3_PR_TOURNAMENT_EXECUTION=PROHIBITED
V3_PR_TRAINING=PROHIBITED
V3_PR_ALLOWED_DEPENDENCY_HOSTS=pypi.org,files.pythonhosted.org,download.pytorch.org
V3_PR_ALLOWED_LLAMA_HOSTS=github.com,release-assets.githubusercontent.com,objects.githubusercontent.com
V3_PR_WORKFLOW_ARTIFACT_UPLOAD=PROHIBITED
V3_PR_CACHE_UPLOAD=PROHIBITED
V3_PR_CURRENT_AUTHORIZED_SPEND_USD=0
```

The dependency-set lock must be plain repository text containing no executable payload and no model/evaluation data.

Static dependency-set preparation is not empirical operational-preflight evidence and cannot make `OPERATIONAL_PREFLIGHT_EVIDENCE=PASS`.

## 7. V3 dependency-lock requirements

The V3 implementation must fail closed unless the committed dependency lock and live PR qualification agree exactly on:

```text
DIRECT_REQUIREMENT_SET=FROZEN
RESOLVED_ARTIFACT_FILENAME_SET=EXACT_MATCH_REQUIRED
RESOLVED_ARTIFACT_COUNT=EXACT_MATCH_REQUIRED
PER_ARTIFACT_BYTE_SIZE=EXACT_MATCH_REQUIRED
PER_ARTIFACT_SHA256=EXACT_MATCH_REQUIRED
AGGREGATE_DEPENDENCY_MANIFEST_SHA256=EXACT_MATCH_REQUIRED
ALLOWED_PROVISIONING_HOST_SET=EXACT_BOUNDED_MATCH_REQUIRED
```

A resolver result that changes after the lock is committed must fail the PR qualification before merge. It must not consume the one empirical V3 attempt.

The V3 empirical lane must consume only the exact dependency set already qualified on the implementation PR. It must not accept compatible substitutions, floating transitive replacements, count-only equivalence, or silent manifest drift.

## 8. Preserved runtime and provider boundary

V3 remains no-model, no-evaluation-payload, and zero-spend.

```text
PROVIDER=GitHub_Actions
REPOSITORY_VISIBILITY=PUBLIC
RUNNER_LABEL=ubuntu-24.04
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
EXACT_LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
EXACT_LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
EXACT_LLAMA_CPP_TAG=b10621
EXACT_LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
TRANSFORMERS_VERSION=4.57.6
TRANSFORMERS_COMMIT=753d61104116eefc8ffc977327b441ee0c8d599f
TORCH_RUNTIME_TARGET=2.11.0+cpu
CURRENT_AUTHORIZED_SPEND_USD=0
```

The prior 27-artifact dependency manifest is historical evidence, not an automatically reusable V3 lock after observed resolver drift.

## 9. V3 single-run and ancestry boundary

```text
ANCESTRY_GUARD_CHECKOUT_FETCH_DEPTH=0
EVIDENCE_MARKER_DIRECT_CHILD_OF_EXACT_CANONICAL_V3_IMPLEMENTATION_MERGE=REQUIRED
EVIDENCE_MARKER_ONLY_CHANGED_PATH=REQUIRED
IMPLEMENTATION_PARENT_MUST_BE_MERGE_COMMIT=REQUIRED
FOUNDER_V3_DECISION_TOKEN_SHA256_BINDING=REQUIRED
PULL_REQUEST_EMPIRICAL_JOB=SKIPPED
WORKFLOW_DISPATCH=ABSENT
REPOSITORY_DISPATCH=ABSENT
SCHEDULE=ABSENT
MAX_AUTHORIZED_V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUNS=1
V3_RUN_ATTEMPT_REQUIRED=1
V3_RERUN_AUTHORITY=NONE_BY_DEFAULT
V3_FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
```

The first V3 empirical run attempt consumes the full V3 allowance regardless of PASS, INCOMPLETE, FAIL, infrastructure failure, or guard failure.

## 10. Explicit non-expansion

Decision B, if later selected and canonically captured, does **not** authorize:

```text
V1_RERUN=PROHIBITED
V2_RERUN=PROHIBITED
V2_FAILED_JOB_RERUN=PROHIBITED
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
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

A successful V3 operational-preflight result would satisfy only the operational evidence fields it actually proves. It would not itself activate A15, authorize tournament execution, select a winner, or authorize training.

## 11. Exact post-canonical selection rule

At authoring time no V3 selection is active.

```text
POST_CANONICAL_EXACT_V3_FOUNDER_DECISION_TOKEN=ABSENT
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_DECISION=ABSENT
V3_IMPLEMENTATION_PREPARATION_AUTHORITY=NONE
V3_DEPENDENCY_SET_PREPARATION_AUTHORITY=NONE
V3_STATIC_QUALIFICATION_AUTHORITY=NONE
V3_EMPIRICAL_EVIDENCE_RUN_AUTHORITY=NONE
NEW_OPERATIONAL_PREFLIGHT_EVIDENCE_ATTEMPT_AUTHORITY=NONE
```

Generic continuation language, ordinary approvals, `go ahead`, `all permissions`, prior Founder directives, V1 Decision B, and V2 Decision B do not match either exact V3 token and cannot create V3 authority.

The recommended Decision B token is deliberately not self-executing. It must be supplied by the Founder in a later message after this decision request is canonical.

## 12. Decision criteria

Decision B is appropriate only if the Founder accepts all of the following:

- V1 and V2 allowances remain permanently consumed;
- both terminal failures remain canonical historical evidence;
- V3 is a new versioned attempt, never a V2 retry;
- dependency-set drift is repaired prospectively through an exact committed lock rather than count-only relaxation;
- public runtime artifact resolution may occur during V3 PR qualification but remains no-model, no-evaluation-payload, and zero-spend;
- the exact V3 implementation head must qualify before canonical merge;
- one V3 empirical attempt consumes the new allowance regardless of conclusion;
- no automatic retry follows a V3 failure;
- A1-A14, A15, tournament, winner selection, and training gates remain separate.

## 13. Current disposition

Until an exact post-canonical selection is supplied and separately captured:

```text
CURRENT_GLOBAL_FRONTIER=EXACT_POST_CANONICAL_FOUNDER_V3_OPERATIONAL_PREFLIGHT_DECISION
V1_OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_TERMINAL_FAILURE
V1_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V2_OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_TERMINAL_DEPENDENCY_SET_DRIFT
V2_OPERATIONAL_PREFLIGHT_EVIDENCE_AUTHORITY=CONSUMED
V3_DECISION_SURFACE=READY_FOR_CANONICALIZATION
POST_CANONICAL_EXACT_V3_FOUNDER_DECISION_TOKEN=ABSENT
V3_IMPLEMENTATION_PREPARATION_AUTHORITY=NONE
V3_EMPIRICAL_EVIDENCE_RUN_AUTHORITY=NONE
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```
