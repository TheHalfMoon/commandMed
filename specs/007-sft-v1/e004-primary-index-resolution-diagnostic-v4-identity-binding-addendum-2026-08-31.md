# E004 V4 Merge Identity-Binding Addendum — 2026-08-31

**Spec:** 007 SFT V1
**Decision owner:** Founder
**Artifact class:** bounded diagnostic identity-binding authority addendum
**Canonical base:** `782775c495b0638a8dfd8f39b1ffec01a0fa0152`
**Parent authority:** `specs/007-sft-v1/e004-primary-index-resolution-diagnostic-v4-authority-2026-08-31.md`
**Parent authority merge:** `782775c495b0638a8dfd8f39b1ffec01a0fa0152`
**Authority effect before canonical merge:** NONE
**Training authority:** NONE
**Spend authority:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Resolve one implementation-identity defect discovered during exact-head review of V4 workflow candidate PR #153 without broadening the scientific diagnostic objective.

PR #153 proved that predecessor SHA plus run-attempt checks do not mechanically bind a newly merged workflow to independently reviewed bytes. A fixed final commit SHA or final tree SHA cannot be embedded into that same workflow because adding the identity changes the object being identified. CodeRabbit independently confirmed that this self-reference has no narrower no-network solution and that a separate canonical addendum plus an immutable external enforcement point is required.

This addendum therefore authorizes a two-layer successor implementation:

1. a separately reviewed, reusable, inert-until-called V4 identity-enforcement workflow that becomes canonical before the successor diagnostic caller exists; and
2. a minimal successor diagnostic caller whose only executable job is a call to that reusable workflow pinned to its exact canonical enforcement merge SHA.

The reusable workflow owns every network-capable operation. It must prove the exact GitHub merge provenance first using bounded unauthenticated public GitHub REST metadata, and only then may it execute the already-authorized PyPI/PyTorch V4 index-metadata diagnostic.

This addendum does not authorize target runtime-evidence execution, target repair, model or weight activity, benchmark execution, contamination assessment, A15 activation, training, credentials, uploads, procurement, payment, or spend.

## 2. Preserved evidence and execution state

```text
V4_PARENT_AUTHORITY_MERGE=782775c495b0638a8dfd8f39b1ffec01a0fa0152
PR_153_REVIEWED_HEAD=610dc768d355815d50998e54903b3568f9010f11
PR_153_REVIEWED_TREE=c353e36ebdf94492383b031650f083771d2b29ed
PR_153_CURRENT_DISPOSITION=UNMERGEABLE_IDENTITY_BINDING_BLOCKER
PR_153_EXECUTION_OCCURRED=NO

V4_DIAGNOSTIC_EXECUTION_COUNT=0
V4_DIAGNOSTIC_ALLOWANCE_REMAINING=1
V3_DIAGNOSTIC_EXECUTION_ALLOWANCE_REMAINING=0

PRIMARY_PYPI_INDEX_EXACT_CANDIDATE_SET=NEEDS_EVIDENCE
COMBINED_PIP_INDEX_RESOLUTION_EXCLUSION=NEEDS_EVIDENCE
STATIC_WORKFLOW_DEFECT_PROVEN=NO_NEEDS_PRIMARY_INDEX_EVIDENCE
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
HISTORICAL_FAILURE_CAUSE_ATTRIBUTED_TO_DOWNLOAD_R2=NO
HISTORICAL_STDERR_RECOVERED=NO
HISTORICAL_EXACT_DENY_LINE_CLAIMED=NO
```

No V4 diagnostic execution allowance is consumed by creating, reviewing, or canonically merging this addendum or the inert reusable enforcement workflow.

## 3. Supersession of the original one-file lifetime mechanism

For the V4 successor path only, this addendum supersedes the parent authority's assumption that the newly introduced diagnostic workflow can mechanically prove its own final content identity using only local `push` metadata.

PR #153 itself receives no merge or execution authority from this addendum.

After this addendum becomes canonical, the required structure is:

```text
CANONICAL_V4_IDENTITY_ADDENDUM
-> REVIEWED_REUSABLE_V4_IDENTITY_ENFORCER
-> CANONICAL_V4_IDENTITY_ENFORCER_MERGE
-> SUCCESSOR_DIAGNOSTIC_CALLER_FROM_THAT_EXACT_MAIN
-> SUCCESSOR_PR_NUMBER_BOUND_IN_CALLER
-> FRESH_EXACT_HEAD_REVIEW
-> GUARDED_MERGE
-> ONE V4 DIAGNOSTIC RUN
```

The successor caller merge must occur while canonical `main` is still exactly the reusable-enforcer merge expected by the caller. If `main` moves first, the execution lane fails closed and no rebinding is implicit.

## 4. Reusable immutable enforcement point

After this addendum is canonically merged, one separate implementation PR may add exactly one reusable workflow at:

```text
.github/workflows/e004-primary-index-resolution-enforcer-v4.yml
```

The enforcement workflow must:

```text
TRIGGER=workflow_call_ONLY
STANDALONE_PUSH_TRIGGER=NONE
STANDALONE_WORKFLOW_DISPATCH=NONE
PERMISSIONS={}
RUNNER=ubuntu-24.04
AUTHORIZED_SPEND_USD=0
```

It must be independently reviewed at exact final head with explicit `MATERIAL_BLOCKER=NO` and guarded-merged before any successor diagnostic caller may be created.

The canonical reusable-enforcer merge SHA becomes:

```text
V4_ENFORCER_MERGE_SHA=<exact canonical merge SHA of the reviewed enforcer PR>
```

The successor diagnostic caller must invoke the reusable workflow using an immutable repository-qualified pin:

```text
uses: TheHalfMoon/commandMed/.github/workflows/e004-primary-index-resolution-enforcer-v4.yml@<V4_ENFORCER_MERGE_SHA>
```

No branch, tag, floating ref, or unpinned reusable-workflow reference is authorized.

## 5. Successor diagnostic caller boundary

The successor caller must exist only at:

```text
.github/workflows/e004-primary-index-resolution-diagnostic-v4.yml
```

It must trigger only on `push` to `main` path-scoped to that exact file.

Its executable surface must contain exactly one job, and that job must be a reusable-workflow call to the exact pinned V4 enforcer. The caller may bind only the inputs required by the enforcer, including:

```text
EXPECTED_PREDECESSOR_SHA=<V4_ENFORCER_MERGE_SHA>
SUCCESSOR_PR_NUMBER=<exact PR number of this successor caller>
```

The caller must have:

```text
permissions: {}
CHECKOUT=PROHIBITED
RUN_STEPS=PROHIBITED
SHELL_STEPS=PROHIBITED
NETWORK_CODE_IN_CALLER=PROHIBITED
SECOND_JOB=PROHIBITED
ALTERNATE_TRIGGER=PROHIBITED
```

The successor PR may initially be opened with an inert placeholder input value solely to obtain its PR number. Before review, that same workflow file must be updated to bind the exact PR number. The final PR diff must contain exactly one changed path: the successor caller workflow itself. No placeholder file or second repository surface may remain in the exact reviewed head.

## 6. Enforcer pre-network event gate

The reusable enforcer receives the caller's original `push` event context and must fail closed before its first network request unless all of these hold:

```text
github.event_name == "push"
github.repository == "TheHalfMoon/commandMed"
github.ref == "refs/heads/main"
github.run_attempt == 1
event.before == EXPECTED_PREDECESSOR_SHA
event.after == GITHUB_SHA
event.head_commit.id == GITHUB_SHA
event.forced == false
event.created == false
event.deleted == false
EXPECTED_PREDECESSOR_SHA == V4_ENFORCER_MERGE_SHA_BOUND_BY_REVIEWED_CALLER
```

The runtime must parse local `GITHUB_EVENT_PATH` and repeat the event assertions before any public GitHub REST request.

Later matching pushes, reruns, alternate events, forced pushes, ref creation/deletion, or a predecessor that is not the exact canonical enforcer merge must fail closed before GitHub REST or index metadata access.

## 7. Identity-bootstrap network authority

Only the reusable enforcer may perform pre-diagnostic identity network access.

### 7.1 Transport

```text
IDENTITY_BOOTSTRAP_PROVIDER=PUBLIC_GITHUB_REST_API
IDENTITY_BOOTSTRAP_SCHEME=https
IDENTITY_BOOTSTRAP_HOST=api.github.com
IDENTITY_BOOTSTRAP_PORT=443
IDENTITY_BOOTSTRAP_AUTHENTICATION=NONE
IDENTITY_BOOTSTRAP_CREDENTIAL_USE=PROHIBITED
IDENTITY_BOOTSTRAP_METHOD=GET_ONLY
IDENTITY_BOOTSTRAP_REDIRECTS=PROHIBITED
IDENTITY_BOOTSTRAP_MAX_REQUESTS=3
IDENTITY_BOOTSTRAP_MAX_RESPONSE_BYTES_PER_REQUEST=2097152
IDENTITY_BOOTSTRAP_USER_AGENT=commandMed-e004-v4-identity/1
```

`GITHUB_TOKEN`, `GH_TOKEN`, private tokens, cookies, repository secrets, and `Authorization` headers are prohibited.

### 7.2 Exact authorized endpoints

For the exact bound successor PR number, only these public repository metadata reads are authorized before the diagnostic index requests:

```text
GET https://api.github.com/repos/TheHalfMoon/commandMed/pulls/<SUCCESSOR_PR_NUMBER>
GET https://api.github.com/repos/TheHalfMoon/commandMed/commits/<GITHUB_SHA>
GET https://api.github.com/repos/TheHalfMoon/commandMed/commits/<PR_HEAD_SHA_FROM_PULL_RESPONSE>
```

No GitHub GraphQL request, file-content request, raw-content request, Actions API request, artifact/log request, issue/comment request, additional page, authenticated request, or mutable endpoint is authorized.

Every request must reject redirects, non-HTTPS targets, a host other than exact `api.github.com`, a port other than 443, non-200 responses, unexpected content type, oversized bodies, and malformed JSON.

## 8. Required public-GitHub merge provenance

The three authorized responses must prove all of the following before any PyPI/PyTorch metadata request:

```text
PULL_NUMBER=<SUCCESSOR_PR_NUMBER>
PULL_STATE=closed
PULL_MERGED=true
PULL_BASE_REPOSITORY=TheHalfMoon/commandMed
PULL_BASE_REF=main
PULL_BASE_SHA=<V4_ENFORCER_MERGE_SHA>
PULL_HEAD_REPOSITORY=TheHalfMoon/commandMed
PULL_HEAD_SHA=<exact successor reviewed head returned by GitHub>
PULL_MERGE_COMMIT_SHA=<GITHUB_SHA>

MERGE_COMMIT_SHA=<GITHUB_SHA>
MERGE_COMMIT_PARENT_COUNT=2
MERGE_COMMIT_PARENT_1=<V4_ENFORCER_MERGE_SHA>
MERGE_COMMIT_PARENT_2=<PULL_HEAD_SHA>
MERGE_COMMIT_TREE_SHA=<PULL_HEAD_COMMIT_TREE_SHA>

PULL_HEAD_COMMIT_SHA=<PULL_HEAD_SHA>
```

The two-parent condition makes merge-commit semantics mandatory and rejects squash/rebase execution. The head repository must be the same canonical repository; fork-head provenance is not authorized.

The successor exact-head independent review and guarded merge must separately verify that the final PR changes only `.github/workflows/e004-primary-index-resolution-diagnostic-v4.yml` and that the caller contains no executable surface other than the exact pinned reusable-workflow call. No runtime files-list API expansion is authorized merely to repeat that already identity-bound review fact.

If any provenance assertion fails, the reusable enforcer must stop before either index metadata request.

## 9. Diagnostic surface after identity PASS

Only after Sections 6–8 pass may the reusable enforcer execute the already-authorized V4 diagnostic surface:

- bounded GET of public Simple index metadata for `https://pypi.org/simple/torch/`;
- bounded GET of public Simple index metadata for `https://download.pytorch.org/whl/cpu/torch/`;
- exact `torch==2.11.0+cpu` candidate parsing;
- live pip-compatible wheel-tag classification using runner-present pip-vendored packaging;
- `Requires-Python` classification;
- historical CONNECT allowlist classification of discovered candidate URLs without fetching candidate artifact URLs;
- deterministic observation-oriented job logs only.

The parent V4 evidence semantics and historical-causality discipline remain unchanged.

## 10. Explicit exclusions

```text
PR_153_MERGE_AUTHORITY=NONE
PR_153_EXECUTION_AUTHORITY=NONE
V4_DIAGNOSTIC_EXECUTION_COUNT_BEFORE_SUCCESSOR=0
V4_AUTOMATIC_RETRY_AUTHORITY=NONE
V4_FAILED_JOB_RERUN_AUTHORITY=NONE
V4_SECOND_DIAGNOSTIC_EXECUTION_AUTHORITY=NONE
TARGET_RUNTIME_EVIDENCE_WORKFLOW_DISPATCH=PROHIBITED
TARGET_RUNTIME_EVIDENCE_WORKFLOW_EXECUTION=PROHIBITED
TARGET_WORKFLOW_REPAIR=PROHIBITED
TARGET_WORKFLOW_MUTATION=PROHIBITED
V2_ALLOWANCE_REOPEN_AUTHORITY=NONE
V3_ALLOWANCE_REOPEN_AUTHORITY=NONE
PIP_DOWNLOAD=PROHIBITED
PIP_INSTALL=PROHIBITED
DEPENDENCY_ARTIFACT_BODY_DOWNLOAD=PROHIBITED
DEPENDENCY_INSTALLATION=PROHIBITED
MODEL_SOURCE_WEIGHT_ACQUISITION=PROHIBITED
MODEL_WEIGHT_LOADING=PROHIBITED
MODEL_CONVERSION=PROHIBITED
MODEL_INFERENCE=PROHIBITED
BENCHMARK_PAYLOAD_ACCESS=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS=PROHIBITED
CONTAMINATION_ASSESSMENT_EXECUTION=PROHIBITED
A15_ACTIVATION=PROHIBITED
TRAINING=PROHIBITED
PRIVATE_GOLD_OR_PHI_ACCESS=PROHIBITED
GATED_ASSET_ACCESS=PROHIBITED
PROVIDER_GENERATION=PROHIBITED
CREDENTIAL_USE=PROHIBITED
PRIVATE_SECRET_ACCESS=PROHIBITED
ARTIFACT_UPLOAD=PROHIBITED
CACHE_UPLOAD=PROHIBITED
REPOSITORY_MUTATION_BY_V4_RUNTIME=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
PAID_OR_LARGER_RUNNER=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 11. Required lifecycle

```text
V4_IDENTITY_ADDENDUM_EXACT_HEAD_REVIEW_AND_CANONICAL_MERGE
-> CLOSE_PR_153_AS_SUPERSEDED_WITHOUT_MERGE
-> CREATE_REUSABLE_V4_IDENTITY_ENFORCER_FROM_ADDENDUM_MAIN
-> FRESH_EXACT_HEAD_REVIEW_OF_ENFORCER
-> GUARDED_CANONICAL_MERGE_OF_ENFORCER
-> CREATE_SUCCESSOR_DIAGNOSTIC_CALLER_FROM_EXACT_ENFORCER_MAIN
-> OPEN_SUCCESSOR_PR
-> BIND_EXACT_SUCCESSOR_PR_NUMBER_AND_ENFORCER_MERGE_SHA
-> FRESH_EXACT_HEAD_REVIEW_OF_CALLER
-> GUARDED_MERGE_WHILE_MAIN_IS_EXACT_ENFORCER_MERGE
-> EXACTLY_ONE_V4_DIAGNOSTIC_EXECUTION_VIA_PINNED_ENFORCER
-> RETAINED_GITHUB_PROVENANCE_PLUS_INDEX_METADATA_EVIDENCE
-> CANONICAL_V4_RESULT_RECONCILIATION
```

No automatic retry or second V4 diagnostic run is authorized.

## 12. State while this addendum is under review

```text
V4_IDENTITY_ADDENDUM_STATE=CANDIDATE_UNTIL_CANONICAL_MERGE
V4_REUSABLE_ENFORCER_IMPLEMENTATION_AUTHORITY=NONE
V4_SUCCESSOR_CALLER_IMPLEMENTATION_AUTHORITY=NONE
V4_IDENTITY_BOOTSTRAP_AUTHORITY=NONE
V4_EXECUTION_AUTHORITY=NONE
V4_DIAGNOSTIC_EXECUTION_COUNT=0
V4_DIAGNOSTIC_ALLOWANCE_REMAINING=1
PR_153_MERGE_AUTHORITY=NONE
TARGET_WORKFLOW_REPAIR_AUTHORITY=NONE
NEW_TARGET_RUNTIME_EVIDENCE_ATTEMPT_AUTHORITY=NONE
PRIMARY_PYPI_INDEX_EXACT_CANDIDATE_SET=NEEDS_EVIDENCE
COMBINED_PIP_INDEX_RESOLUTION_EXCLUSION=NEEDS_EVIDENCE
STATIC_WORKFLOW_DEFECT_PROVEN=NO_NEEDS_PRIMARY_INDEX_EVIDENCE
PHASE_A_FAILURE_CAUSE=NEEDS_EVIDENCE
COMPONENT_E004=INCOMPLETE
COMPONENT_E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
MODEL_CONVERSION_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 13. Canonical-merge effect

If and only if this exact addendum passes fresh exact-head independent review with `MATERIAL_BLOCKER=NO` and is guarded-merged canonically, it authorizes creation and qualification of the reusable V4 identity enforcer in Section 4.

It does not authorize the successor caller until the reusable enforcer itself is reviewed and canonically merged. It does not authorize V4 diagnostic execution until the successor caller itself is reviewed at exact final head and guarded-merged under the lifecycle above.

## 14. Required review gate

Before canonical merge, an independent reviewer must verify at least:

- the fixed commit/tree self-reference problem is accurately described;
- PR #153 remains unmerged and no V4 diagnostic execution occurred;
- exactly one V4 diagnostic allowance remains;
- the new external enforcement point is reusable, immutable-by-pin, and inert until called;
- the successor caller is prohibited from owning shell steps or network code;
- only three unauthenticated public GitHub REST GETs are added before identity PASS;
- merge-commit parent/tree/PR provenance is fail-closed and fork heads are excluded;
- the enforcer is pinned by exact canonical SHA in the successor caller;
- only after identity PASS may the existing two index metadata GETs occur;
- all target-workflow/model/benchmark/contamination/A15/training/upload/spend prohibitions remain intact;
- E004 remains incomplete, E005 remains not reached, and historical Phase A cause remains unresolved.

Required reviewer output:

```text
MATERIAL_BLOCKER=NO
```

No reusable enforcer, successor caller merge, or V4 diagnostic execution may occur before guarded canonical merge of this exact reviewed addendum.