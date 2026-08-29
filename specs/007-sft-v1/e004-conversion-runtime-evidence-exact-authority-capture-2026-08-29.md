# E004 Conversion Runtime Evidence Exact Authority Capture — 2026-08-29

**Spec:** 007 SFT V1  
**Canonical base:** `3d53a56f6c6576794cbf015c95977eb9510b4dd6`  
**Artifact class:** exact workflow identity / promotion authority capture  
**Authority source:** `e004-founder-conversion-runtime-evidence-authority-2026-08-29.md`  
**Execution performed by this record:** NO  
**Live workflow created by this record:** NO  
**Model conversion authority:** NONE  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Bind the exact reviewed non-executable E004 conversion-runtime evidence workflow bytes after canonical merge so any later live promotion can be proven byte-identical rather than reconstructed from prose or copied text.

This record does not create a live GitHub Actions workflow and does not dispatch anything.

## 2. Canonical Founder authority

Canonical main `3d53a56f6c6576794cbf015c95977eb9510b4dd6` contains the Founder-bound authority record and the independently reviewed non-executable candidate.

```text
E004_CONVERSION_RUNTIME_EVIDENCE_AUTHORITY=AUTHORIZED_BOUNDED
PROVIDER=GitHub_Actions
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
RUNNER_LABEL=ubuntu-24.04
MAX_AUTHORIZED_WORKFLOW_RUNS=1
TRIGGER=workflow_dispatch_only
PURPOSE=RESOLVE_AND_BIND_EXACT_CONVERSION_RUNTIME_DEPENDENCY_AND_REBUILD_EVIDENCE_ONLY
CURRENT_AUTHORIZED_SPEND_USD=0
```

The prior build-evidence allowance is unaffected:

```text
PRIOR_BUILD_EVIDENCE_RUN=33187438094
PRIOR_BUILD_EVIDENCE_ALLOWANCE_REMAINING=0
PRIOR_BUILD_EVIDENCE_WORKFLOW_RERUN_AUTHORIZED=NO
```

## 3. Exact canonical candidate identity

```text
CANDIDATE_CANONICAL_COMMIT=3d53a56f6c6576794cbf015c95977eb9510b4dd6
CANDIDATE_PATH=specs/007-sft-v1/candidates/e004-conversion-runtime-evidence.workflow.yml.example
CANDIDATE_GIT_BLOB_SHA1=591317f1f570480b9ac68e7956d070db8ed5ef45
CANDIDATE_RAW_INTEGER_BYTES=24581
CANDIDATE_RAW_SHA256=95512021832788d5cd6362e6fa9ea0c7771bf81f5725ae4ab18b4d5199967327
```

GitHub contents metadata on canonical main independently exposes the same Git blob SHA-1. CodeRabbit then read the raw blob from canonical merge `3d53a56f6c6576794cbf015c95977eb9510b4dd6` and independently reported:

```text
GIT_BLOB_SHA1=591317f1f570480b9ac68e7956d070db8ed5ef45
RAW_BYTE_COUNT=24581
RAW_BYTES_SHA256=95512021832788d5cd6362e6fa9ea0c7771bf81f5725ae4ab18b4d5199967327
EXPECTED_BLOB_MATCH=YES
CHECKSUM_EVIDENCE_COMMENT_ID=5462089002
```

## 4. Exact candidate qualification evidence

The candidate and Founder authority record were qualified together on PR #131.

```text
QUALIFIED_BASE=8b41051801c004cd85179dee3f26b4210b31de95
QUALIFIED_HEAD=7d31d4291953a03838d852cb77f852f630c6488d
QUALIFIED_CHANGED_PATH_COUNT=2
CODE_RABBIT_FINAL_REVIEW_COMMENT_ID=5462073799
MATERIAL_BLOCKER=NO
```

The final exact-head review independently verified the prior material repairs and reported that:

- YAML parsing succeeded;
- extracted Bash passed `bash -n`;
- all embedded Python heredocs passed syntax compilation;
- Phase A network destinations are proactively constrained before remote connection;
- Founder decision ordering is transparently evidence-bound without pretending PR #130 contained the response;
- Phase B re-binds source and dependency bytes before build;
- local `gguf-py`, offline install, privilege/capability/network isolation, and lifecycle/authority boundaries remain fail closed.

## 5. Exact future live path

The only live path eligible under this capture is:

```text
AUTHORIZED_LIVE_WORKFLOW_PATH=.github/workflows/e004-conversion-runtime-evidence.yml
```

No alternate filename or secondary executable copy is authorized.

## 6. Byte-identical promotion requirement

Promotion must reuse the exact canonical candidate Git blob object, not reconstruct or edit the file contents.

```text
PROMOTED_LIVE_GIT_BLOB_SHA1_MUST_EQUAL=591317f1f570480b9ac68e7956d070db8ed5ef45
PROMOTED_LIVE_RAW_INTEGER_BYTES_MUST_EQUAL=24581
PROMOTED_LIVE_RAW_SHA256_MUST_EQUAL=95512021832788d5cd6362e6fa9ea0c7771bf81f5725ae4ab18b4d5199967327
BYTE_IDENTICAL_PROMOTION_REQUIRED=YES
TEXT_RECONSTRUCTION_AS_PROMOTION_METHOD=PROHIBITED
CANDIDATE_BYTE_MUTATION_AFTER_CAPTURE=INVALIDATES_CAPTURE
```

A Git tree entry that points the authorized live path directly at the already-canonical candidate blob is the preferred promotion method because Git object identity itself proves byte equality.

## 7. Promotion scope

A future promotion PR is bounded to exactly one added live workflow path and no candidate mutation:

```text
PROMOTION_CHANGED_PATH_COUNT=1
PROMOTION_ADDED_PATH=.github/workflows/e004-conversion-runtime-evidence.yml
CANDIDATE_PATH_MUTATION=PROHIBITED
OTHER_WORKFLOW_MUTATION=PROHIBITED
OTHER_REPOSITORY_MUTATION=PROHIBITED
```

The promotion PR must be created from then-current canonical main, independently reviewed on its exact head, and merged guarded only if the exact live blob identity remains equal to this capture.

## 8. Post-merge pre-dispatch conditions

Canonical promotion alone does not consume the one-run allowance and does not prove execution readiness. Before any dispatch, all of the following must still be true:

```text
LIVE_WORKFLOW_PATH_PRESENT=YES
LIVE_WORKFLOW_GIT_BLOB_SHA1=591317f1f570480b9ac68e7956d070db8ed5ef45
LIVE_WORKFLOW_RAW_INTEGER_BYTES=24581
LIVE_WORKFLOW_RAW_SHA256=95512021832788d5cd6362e6fa9ea0c7771bf81f5725ae4ab18b4d5199967327
LIVE_WORKFLOW_EQUALS_CAPTURED_CANDIDATE=YES
LIVE_WORKFLOW_TRIGGER=workflow_dispatch_only
LIVE_WORKFLOW_PERMISSIONS={}
AUTHORIZED_RUNTIME_EVIDENCE_RUNS_ALREADY_EXECUTED=0
AUTHORIZED_RUNTIME_EVIDENCE_RUNS_REMAINING=1
CONNECTED_FRESH_WORKFLOW_DISPATCH_ACTION_AVAILABLE=REQUIRES_LIVE_RECHECK
```

If a fresh `workflow_dispatch` action is unavailable to the connected executor, rerunning another workflow/job, changing the trigger, adding a push trigger, adding a schedule, or using an alternate execution route is prohibited. Such absence is a tooling blocker, not authority to bypass the trigger contract.

## 9. Explicit exclusions

This capture does not authorize or perform:

```text
MODEL_SOURCE_WEIGHT_ACQUISITION=PROHIBITED
MODEL_WEIGHT_LOADING=PROHIBITED
MODEL_CONVERSION=PROHIBITED
MODEL_WEIGHT_QUANTIZATION=PROHIBITED
MODEL_INFERENCE=PROHIBITED
BENCHMARK_PAYLOAD_ACCESS=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
DEVICE_QUALIFICATION=PROHIBITED
CONTAMINATION_ASSESSMENT=PROHIBITED
A15_ACTIVATION=PROHIBITED
PRIVATE_GOLD=PROHIBITED
PHI=PROHIBITED
GATED_ASSETS=PROHIBITED
EXTERNAL_REVIEWER_OUTREACH=PROHIBITED
TRAINING=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 10. Current lifecycle

```text
E004_CONVERSION_RUNTIME_EVIDENCE_AUTHORITY=AUTHORIZED_BOUNDED
EXACT_RUNTIME_EVIDENCE_WORKFLOW_IDENTITY=CAPTURED_PENDING_CANONICAL_REVIEW_AND_MERGE
LIVE_RUNTIME_EVIDENCE_WORKFLOW_PRESENT=NO
RUNTIME_EVIDENCE_EXECUTION_OCCURRED=NO
AUTHORIZED_RUNTIME_EVIDENCE_RUNS_REMAINING=1
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
```

## Exit Evidence

This exact-capture artifact is repository-level complete only after fresh exact-head review confirms:

```text
CANONICAL_CANDIDATE_COMMIT_BOUND=YES
CANONICAL_CANDIDATE_GIT_BLOB_BOUND=YES
CANONICAL_CANDIDATE_RAW_BYTES_BOUND=YES
CANONICAL_CANDIDATE_SHA256_BOUND=YES
PR131_EXACT_QUALIFICATION_BOUND=YES
LIVE_PATH_EXACTLY_ONE=YES
BYTE_IDENTICAL_PROMOTION_REQUIRED=YES
PRIOR_BUILD_ALLOWANCE_REMAINS_ZERO=YES
NO_EXECUTION_OCCURRED=YES
NO_DOWNSTREAM_AUTHORITY_CREATED=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
E005_REMAINS_NOT_REACHED=YES
```

Canonical merge of this record authorizes only the exact byte-identical promotion process described above. It does not execute the workflow.