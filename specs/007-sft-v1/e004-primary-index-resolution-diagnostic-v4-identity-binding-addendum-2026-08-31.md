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

Resolve one implementation-identity defect discovered during exact-head review of V4 workflow candidate PR #153 without broadening the scientific diagnostic scope.

The canonical V4 authority requires a mechanically one-shot `push` execution. PR #153 exact-head review established that predecessor SHA and run-attempt checks alone do not bind the diagnostic body to the independently reviewed implementation bytes. A proposed fixed Git tree-ID constant cannot be added to the same workflow without creating a self-referential hash problem: changing the workflow to embed its own final tree identity changes that tree identity.

This addendum therefore authorizes the narrowest practical merge-compatible identity bootstrap: bounded unauthenticated public GitHub REST metadata reads that mechanically prove the `main` push corresponds to the exact independently reviewed successor implementation PR before any PyPI or PyTorch diagnostic metadata request may occur.

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

No V4 execution allowance is consumed by creating, reviewing, or canonically merging this addendum.

## 3. Superseded V4 implementation-binding mechanism

For a successor V4 implementation only, this addendum supersedes the parent authority's requirement that the diagnostic implementation merge push must have:

```text
V4_IMPLEMENTATION_REQUIRED_EVENT_BEFORE_SHA=782775c495b0638a8dfd8f39b1ffec01a0fa0152
```

That predecessor is no longer usable after this addendum itself becomes canonical.

If and only if this addendum is independently reviewed at exact head with `MATERIAL_BLOCKER=NO` and guarded-merged canonically, the successor implementation MUST instead bind:

```text
V4_IDENTITY_ADDENDUM_MERGE_SHA=<exact canonical merge SHA of this addendum PR>
V4_IMPLEMENTATION_REQUIRED_EVENT=push
V4_IMPLEMENTATION_REQUIRED_REF=refs/heads/main
V4_IMPLEMENTATION_REQUIRED_PATH=.github/workflows/e004-primary-index-resolution-diagnostic-v4.yml
V4_IMPLEMENTATION_REQUIRED_EVENT_BEFORE_SHA=V4_IDENTITY_ADDENDUM_MERGE_SHA
V4_IMPLEMENTATION_REQUIRED_RUN_ATTEMPT=1
V4_IMPLEMENTATION_REQUIRED_FORCED=false
V4_IMPLEMENTATION_REQUIRED_CREATED=false
V4_IMPLEMENTATION_REQUIRED_DELETED=false
```

The successor workflow must be created from then-current canonical `main`. PR #153 itself is not authorized for merge under this addendum and should be closed as superseded after this addendum becomes canonical.

## 4. Identity-bootstrap network authority

Only after this addendum becomes canonical and a successor implementation PR exists may that successor implementation include an identity bootstrap with the following maximum network surface.

### 4.1 Transport

```text
IDENTITY_BOOTSTRAP_PROVIDER=PUBLIC_GITHUB_REST_API
IDENTITY_BOOTSTRAP_SCHEME=https
IDENTITY_BOOTSTRAP_HOST=api.github.com
IDENTITY_BOOTSTRAP_PORT=443
IDENTITY_BOOTSTRAP_AUTHENTICATION=NONE
IDENTITY_BOOTSTRAP_CREDENTIAL_USE=PROHIBITED
IDENTITY_BOOTSTRAP_METHOD=GET_ONLY
IDENTITY_BOOTSTRAP_REDIRECTS=PROHIBITED
IDENTITY_BOOTSTRAP_MAX_REQUESTS=4
IDENTITY_BOOTSTRAP_MAX_RESPONSE_BYTES_PER_REQUEST=2097152
IDENTITY_BOOTSTRAP_USER_AGENT=commandMed-e004-v4-identity/1
```

The runtime must unset or avoid `GITHUB_TOKEN`, `GH_TOKEN`, and all private credentials before these requests. It may not send an `Authorization` header, cookies, repository secrets, or user credentials.

### 4.2 Exact endpoint families

The successor implementation must bind one exact successor PR number after that PR is opened. Only these four public repository metadata reads are authorized:

```text
GET https://api.github.com/repos/TheHalfMoon/commandMed/pulls/<BOUND_SUCCESSOR_PR_NUMBER>
GET https://api.github.com/repos/TheHalfMoon/commandMed/git/commits/<GITHUB_SHA>
GET https://api.github.com/repos/TheHalfMoon/commandMed/git/commits/<PR_HEAD_SHA_FROM_FIRST_RESPONSE>
GET https://api.github.com/repos/TheHalfMoon/commandMed/pulls/<BOUND_SUCCESSOR_PR_NUMBER>/files?per_page=100&page=1
```

No other GitHub API path, page, query, GraphQL request, authenticated request, repository download, raw-content request, artifact request, Actions API request, issue/comment mutation, or ref/content mutation is authorized by this addendum.

If any required response exceeds the byte limit, returns a redirect, is not HTTP 200, is malformed, is incomplete, or requires another request/page to establish identity, the V4 diagnostic must fail closed before any PyPI/PyTorch metadata request. No pagination beyond the single authorized files page is permitted; therefore the successor PR must remain small enough that its complete changed-file set is represented by that page.

## 5. Required mechanical merge-provenance gate

The successor implementation must perform two levels of checks.

### 5.1 Job-level pre-bootstrap gate

Before any network-capable step can start, the job-level predicate must require at least:

```text
github.repository == 'TheHalfMoon/commandMed'
github.ref == 'refs/heads/main'
github.event.before == '<V4_IDENTITY_ADDENDUM_MERGE_SHA>'
github.event.after == github.sha
github.event.head_commit.id == github.sha
github.event.forced == false
github.event.created == false
github.event.deleted == false
github.run_attempt == 1
```

The workflow trigger must remain exactly `push` to `main` path-scoped to:

```text
.github/workflows/e004-primary-index-resolution-diagnostic-v4.yml
```

Later matching pushes, reruns, alternate events, ref creation/deletion, forced pushes, or a predecessor other than the exact canonical addendum merge must skip the diagnostic job.

### 5.2 Local event assertions before identity REST reads

Before the first GitHub REST identity request, the runtime must parse local `GITHUB_EVENT_PATH` and recheck the same repository/ref/before/after/head-commit/forced/created/deleted/run-attempt conditions. It must require:

```text
GITHUB_SHA == event.after
GITHUB_SHA == event.head_commit.id
```

No PyPI/PyTorch metadata request is permitted until the GitHub REST identity gate in Section 5.3 also passes.

### 5.3 Public GitHub REST identity assertions

The four authorized responses must establish all of the following:

```text
PR_NUMBER=<exact bound successor implementation PR number>
PR_REPOSITORY=TheHalfMoon/commandMed
PR_BASE_REF=main
PR_BASE_SHA=<V4_IDENTITY_ADDENDUM_MERGE_SHA>
PR_HEAD_REF=<exact successor implementation branch>
PR_HEAD_SHA=<exact independently reviewed implementation head>
PR_STATE=closed
PR_MERGED=true
PR_MERGE_COMMIT_SHA=<GITHUB_SHA>

MERGE_COMMIT_SHA=<GITHUB_SHA>
MERGE_COMMIT_PARENT_COUNT=2
MERGE_COMMIT_PARENT_1=<V4_IDENTITY_ADDENDUM_MERGE_SHA>
MERGE_COMMIT_PARENT_2=<PR_HEAD_SHA>

HEAD_COMMIT_SHA=<PR_HEAD_SHA>
MERGE_TREE_SHA=<HEAD_COMMIT_TREE_SHA>

SUCCESSOR_PR_CHANGED_FILE_COUNT=1
SUCCESSOR_PR_CHANGED_FILE_1=.github/workflows/e004-primary-index-resolution-diagnostic-v4.yml
SUCCESSOR_PR_CHANGED_FILE_1_STATUS=added
```

The PR head SHA is not embedded as a self-referential constant in the workflow. It is learned from the exact bound public PR metadata response and must equal the second parent of the GitHub merge commit. The merge tree must equal that PR-head tree. The changed-file response must prove the successor PR changes only the exact V4 workflow file and adds no additional repository surface.

If any assertion fails, the workflow must exit before the two existing index-metadata GETs.

## 6. Diagnostic surface after identity PASS

Only after Section 5 is fully satisfied may the successor workflow execute the already-authorized V4 diagnostic surface from the parent authority:

- bounded GET of public Simple index metadata for `https://pypi.org/simple/torch/`;
- bounded GET of public Simple index metadata for `https://download.pytorch.org/whl/cpu/torch/`;
- exact `torch==2.11.0+cpu` candidate parsing;
- live pip-compatible wheel-tag classification using the runner's existing pip-vendored packaging code;
- `Requires-Python` classification;
- historical CONNECT allowlist classification of discovered candidate URLs without fetching candidate artifact URLs;
- deterministic observation-oriented job logs only.

This addendum does not change the candidate-evidence semantics, conclusion discipline, or historical-causality boundary in the parent V4 authority.

## 7. Explicit exclusions

```text
PR_153_MERGE_AUTHORITY=NONE
PR_153_EXECUTION_AUTHORITY=NONE
V4_AUTOMATIC_RETRY_AUTHORITY=NONE
V4_FAILED_JOB_RERUN_AUTHORITY=NONE
V4_SECOND_EXECUTION_AUTHORITY=NONE
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

## 8. Lifecycle

```text
V4_IDENTITY_ADDENDUM_EXACT_HEAD_REVIEW_AND_CANONICAL_MERGE
-> CLOSE_PR_153_AS_SUPERSEDED_WITHOUT_MERGE
-> CREATE_SUCCESSOR_V4_IMPLEMENTATION_FROM_ADDENDUM_MAIN
-> OPEN_SUCCESSOR_PR_AND_BIND_ITS_EXACT_PR_NUMBER
-> FRESH_EXACT_HEAD_INDEPENDENT_REPOSITORY_REVIEW
-> GUARDED_CANONICAL_MERGE_OF_EXACT_REVIEWED_HEAD
-> EXACTLY_ONE_V4_RUN
-> GITHUB_IDENTITY_BOOTSTRAP_PASS
-> PRIMARY_AND_EXTRA_INDEX_METADATA_EVIDENCE_CAPTURE
-> CANONICAL_V4_RESULT_RECONCILIATION
```

No successor implementation merge may occur unless its exact final head receives explicit independent `MATERIAL_BLOCKER=NO` and canonical `main` still equals the exact addendum merge SHA expected by the implementation guard.

## 9. State while this addendum is under review

```text
V4_IDENTITY_ADDENDUM_STATE=CANDIDATE_UNTIL_CANONICAL_MERGE
V4_IDENTITY_BOOTSTRAP_AUTHORITY=NONE
V4_SUCCESSOR_IMPLEMENTATION_AUTHORITY=NONE
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

## 10. Canonical-merge effect

If and only if this exact addendum passes fresh exact-head independent review with `MATERIAL_BLOCKER=NO` and is guarded-merged canonically, it authorizes creation and qualification of one successor V4 workflow implementation using Sections 3–6.

It does not authorize V4 execution before that successor implementation is itself independently reviewed at exact final head and guarded-merged. It does not consume the remaining V4 execution allowance by itself.

## 11. Required review gate

Before canonical merge, an independent reviewer must verify at least:

- the tree-ID self-reference problem is accurately described;
- PR #153 remains unmerged and no V4 execution occurred;
- exactly one V4 diagnostic allowance remains;
- only four unauthenticated public GitHub REST GETs are added to the network surface;
- those GETs are limited to exact successor PR/commit/files metadata required for merge provenance;
- the identity bootstrap cannot access repository content, Actions logs/artifacts, credentials, secrets, or mutable endpoints;
- the successor must remain exactly one changed workflow file;
- PyPI/PyTorch metadata access cannot begin until merge provenance passes;
- all target-workflow/model/benchmark/contamination/A15/training/upload/spend prohibitions remain intact;
- E004 remains incomplete, E005 remains not reached, and historical Phase A cause remains unresolved.

Required reviewer output:

```text
MATERIAL_BLOCKER=NO
```

No successor workflow implementation may be merged or executed before guarded canonical merge of this exact reviewed addendum.