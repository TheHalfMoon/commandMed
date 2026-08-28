# E004 GitHub Actions Validation Corrective Recapture — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `c6a6427447ed38d93a52d381db1a8a6ae4296131`  
**Founder environment decision:** `BUILD_ENVIRONMENT_DECISION_B`  
**Predecessor exact capture:** PR #93  
**Predecessor location-neutral recapture:** PR #95  
**Abandoned promotion attempts:** PR #94 and PR #96 / CLOSED_UNMERGED  
**Authority class:** corrective successor exact-subject recapture  
**Authority expansion:** NONE  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Why this corrective recapture is required

PR #96 exact-head review discovered a provider workflow-run record that earlier repository checks had missed because the connector helper used at the time filtered to pull-request-triggered runs. Direct GitHub Actions history now proves that both abandoned promotion attempts produced failed provider records before any job was created.

```text
PR94_HEAD=d572e14a77f3751e37b0bff8039e37bf08146ab4
PR94_PROVIDER_RUN_ID=33151283011
PR94_PROVIDER_RUN_NUMBER=1
PR94_PROVIDER_RUN_EVENT=push
PR94_PROVIDER_RUN_CONCLUSION=failure
PR94_PROVIDER_RUN_JOBS=0
PR94_MERGED=NO

PR96_HEAD=3ad3ca3ca35f799cb0d4b8ba704e16196b2ca9c2
PR96_PROVIDER_RUN_ID=33153171634
PR96_PROVIDER_RUN_NUMBER=2
PR96_PROVIDER_RUN_EVENT=push
PR96_PROVIDER_RUN_CONCLUSION=failure
PR96_PROVIDER_RUN_JOBS=0
PR96_MERGED=NO
```

These records correct prior wording that stated or implied no workflow-run record existed for PR #94 or the first PR #96 review surface.

The evidence supports the following narrower claims only:

```text
PROVIDER_WORKFLOW_RUN_RECORDS_OBSERVED=2
PROVIDER_WORKFLOW_RUN_RECORDS_BOTH_ZERO_JOB=YES
AUTHORIZED_MANUAL_WORKFLOW_DISPATCH_OCCURRED=NO
RUNNER_JOB_EXECUTION_OCCURRED=NO
BUILD_EXECUTION_OCCURRED=NO
BUILD_EVIDENCE_PRODUCED=NO
BUILD_PASS=NO
```

A zero-job provider validation failure is not relabeled as a successful or authorized execution. It is nevertheless a real GitHub Actions run record and must remain visible in provenance.

## 2. Root cause

The predecessor candidate placed runner-dependent expressions in workflow-level `env`:

```text
SOURCE_DIR=${{ runner.temp }}/e004-llama.cpp
BUILD_DIR=${{ runner.temp }}/e004-llama.cpp-build
E004_HOME=${{ runner.temp }}/e004-home
SECURITY_EVIDENCE=${{ runner.temp }}/e004-security-boundary.txt
```

GitHub's current Actions context-availability contract permits only `github`, `secrets`, `inputs`, and `vars` in workflow-level `env`. The `runner` context is available once a job/step context exists, including step `env` and `run`, but not at workflow-level `env`.

Primary reference:

```text
https://docs.github.com/en/actions/reference/workflows-and-actions/contexts#context-availability
```

The observed `push` + `failure` + zero-job records are consistent with workflow validation failing before job scheduling.

## 3. Additional pre-runtime defect corrected

The predecessor subject required hashing:

```text
compile_commands.json
```

but did not explicitly set:

```text
CMAKE_EXPORT_COMPILE_COMMANDS=ON
```

The corrected subject binds that CMake option and requires the file to exist before evidence emission. This avoids a deterministic post-build evidence failure caused by relying on an unfrozen default.

## 4. Corrected exact review subject V2

```text
CANDIDATE_PATH=specs/007-sft-v1/candidates/e004-github-actions-build-evidence-v2.workflow.yml.example
CANDIDATE_GIT_BLOB_SHA1=6c371bc989502be2ad44ff4c493e95ba3d00c3a0
CANDIDATE_SHA256=NEEDS_EVIDENCE_EXACT_HEAD_RECOMPUTE
INTENDED_LIVE_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
LIVE_WORKFLOW_ON_CANONICAL_MAIN=NO
```

V2 removes all `runner` expressions from workflow-level `env`. Runner-temporary paths are derived from the runner-provided `RUNNER_TEMP` environment variable only inside shell steps, after the job has started. The first step fails closed unless `RUNNER_TEMP` is nonempty and absolute.

V2 also:

- retains `workflow_dispatch` as the sole declared trigger;
- retains `permissions: {}`;
- retains `ubuntu-24.04`;
- retains the exact public llama.cpp repository, commit, tree, and `llama-quantize` target;
- retains credential-free source fetch;
- retains network isolation for configure/build;
- retains nonroot UID/GID, cleared supplementary groups, zero Linux capability sets, `no_new_privs`, reset environment, and sensitive-platform-environment absence assertions;
- retains job-log-only evidence and prohibits cache/upload/release/package persistence;
- adds `CMAKE_EXPORT_COMPILE_COMMANDS=ON` and explicit existence checks for `CMakeCache.txt` and `compile_commands.json`;
- performs no model, conversion, inference, benchmark, device, contamination, selection-suite, training, procurement, or spend operation.

## 5. Inherited bounded authority

No Founder or downstream authority is expanded by this correction.

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION=BUILD_ENVIRONMENT_DECISION_B
PROVIDER=GitHub_Actions
RUNNER_LABEL=ubuntu-24.04
DECLARED_TRIGGER=workflow_dispatch_only
WORKFLOW_PERMISSIONS={}
TOOL_REPOSITORY_URL=https://github.com/ggml-org/llama.cpp.git
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
BUILD_TARGET=llama-quantize
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 6. Run-accounting ambiguity is not self-resolved

The predecessor capture uses both:

```text
MAX_AUTHORIZED_WORKFLOW_RUNS=1
```

and language describing an `at-most-one manual build-evidence run` under `workflow_dispatch` authority. Two historical provider validation records now exist, both event `push`, both failed before any job, and neither was an authorized manual dispatch.

This corrective record does **not** silently decide whether those zero-job, unauthorized provider validation records consume the one authorized manual-run budget.

```text
AUTHORIZED_MANUAL_RUN_BUDGET_DISPOSITION=NEEDS_GOVERNANCE_REVIEW
MANUAL_DISPATCH_EXERCISABLE=NO_PENDING_RUN_ACCOUNTING_DISPOSITION
MAX_AUTHORIZED_MANUAL_DISPATCHES_ASSUMED=NO
SECOND_MANUAL_RUN_AUTHORITY_CREATED=NO
```

No generic continuation instruction may be used to invent or widen the run budget. A future disposition must be explicit and evidence-bound before any manual dispatch is claimed exercisable.

## 7. Successor promotion conditions

The V2 subject may not be promoted until this corrective recapture is reviewed and canonical.

```text
CORRECTIVE_RECAPTURE_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
-> CORRECTIVE_RECAPTURE_CANONICAL
-> FRESH_PROMOTION_BRANCH_FROM_THEN_CURRENT_CANONICAL_MAIN
-> PROMOTED_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
-> PROMOTED_WORKFLOW_BYTES_EQUAL_V2_QUALIFIED_CANDIDATE_BYTES=YES
-> PROMOTED_WORKFLOW_GIT_BLOB_EQUALS_V2_QUALIFIED_CANDIDATE_GIT_BLOB=YES
-> PROMOTED_WORKFLOW_SHA256_EQUALS_V2_QUALIFIED_CANDIDATE_SHA256=YES
-> NO_UNEXPECTED_PROVIDER_RUN_OR_JOB_EXECUTION_ON_PROMOTION_HEAD=YES
-> FRESH_PROMOTION_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
-> CANONICAL_PROMOTION_MERGE
-> POST_MERGE_BYTE_VERIFICATION
```

Canonical promotion alone does not clear the run-accounting ambiguity in Section 6 and does not authorize manual dispatch while that disposition remains unresolved.

Any further candidate-byte change requires another exact authority capture.

## 8. Current state

```text
CORRECTIVE_RECAPTURE=PENDING_EXACT_HEAD_REVIEW
V2_CANDIDATE_GIT_BLOB_SHA1=6c371bc989502be2ad44ff4c493e95ba3d00c3a0
V2_CANDIDATE_SHA256=NEEDS_EVIDENCE_EXACT_HEAD_RECOMPUTE
LIVE_WORKFLOW_ON_CANONICAL_MAIN=NO
PROVIDER_WORKFLOW_RUN_RECORDS_OBSERVED=2
AUTHORIZED_MANUAL_WORKFLOW_DISPATCH_OCCURRED=NO
RUNNER_JOB_EXECUTION_OCCURRED=NO
BUILD_EXECUTION_OCCURRED=NO
BUILD_PASS=NO
AUTHORIZED_MANUAL_RUN_BUDGET_DISPOSITION=NEEDS_GOVERNANCE_REVIEW
MANUAL_DISPATCH_EXERCISABLE=NO_PENDING_RUN_ACCOUNTING_DISPOSITION
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Exit evidence required

Fresh exact-head review must independently confirm:

```text
PR94_PROVIDER_RUN_EVIDENCE_MATCHES=YES
PR96_PROVIDER_RUN_EVIDENCE_MATCHES=YES
BOTH_PROVIDER_RUN_RECORDS_ZERO_JOB=YES
PRIOR_NO_RUN_WORDING_REQUIRES_CORRECTION=YES
ROOT_CAUSE_WORKFLOW_LEVEL_RUNNER_CONTEXT_INVALID=YES
V2_WORKFLOW_LEVEL_ENV_HAS_NO_RUNNER_CONTEXT=YES
V2_DECLARED_TRIGGER_WORKFLOW_DISPATCH_ONLY=YES
V2_CMAKE_EXPORT_COMPILE_COMMANDS_ON=YES
V2_SECURITY_AND_AUTHORITY_BOUNDARIES_PRESERVED=YES
V2_CANDIDATE_GIT_BLOB_MATCHES=YES
V2_CANDIDATE_SHA256_RECOMPUTED_AND_BOUND=YES
NO_LIVE_WORKFLOW_ON_CANONICAL_MAIN=YES
NO_MANUAL_DISPATCH_OR_JOB_BUILD_EXECUTION_OCCURRED=YES
RUN_ACCOUNTING_AMBIGUITY_NOT_SELF_RESOLVED=YES
NO_DOWNSTREAM_AUTHORITY_EXPANSION=YES
BUILD_PASS_REMAINS_NO=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
```

Any material finding must be repaired before canonical merge.