# E004 GitHub Actions Promotion Verification and Execution-Tooling Blocker — 2026-08-28

**Spec:** 007 SFT V1  
**Task:** E004  
**Record class:** append-only post-promotion verification / execution-tooling blocker  
**Authority source:** `specs/007-sft-v1/e004-github-actions-exact-authority-capture-2026-08-28.md` plus `specs/007-sft-v1/e004-github-actions-runner-context-authority-recapture-2026-08-28.md`  
**Authority effect:** NONE — records canonical promotion truth and the connected-executor limitation only  
**Execution performed by this record:** NO  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

The canonical exact-authority record requires the selected Decision B workflow to be promoted only after fresh exact-head qualification, then requires post-merge byte verification and preservation of all applicable pre-run conditions before the single conditional manual `workflow_dispatch` allowance can be used.

The same authority record explicitly states that, if the connected GitHub action surface still does not expose initiation of a new `workflow_dispatch` after canonical promotion, the executor must record an execution-tooling blocker rather than claim execution evidence.

This record performs exactly that bounded bookkeeping step. It does not dispatch, rerun, execute, build, convert, load, benchmark, evaluate, train, purchase, or spend anything.

## 2. Canonical promotion chain

PR #98 canonically bound the qualified successor subject after fresh exact-head review:

```text
PR98_EXACT_HEAD=83b686fb5763e09d7540258880806e8c8dae12df
PR98_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
PR98_RAW_ACTIONS_RUNS_ON_EXACT_HEAD=0
PR98_MERGE=4b4f31ec330d559318ae9aaaa6ad88533b6f0f8a
QUALIFIED_SUCCESSOR_GIT_BLOB_SHA1=710cb4e6ecf1b34e93d3dfa3d59e24c3d60d1d79
QUALIFIED_SUCCESSOR_SHA256=836175ee057e2a6802b47db00766119d54c2034b63c8487f138dc125285f226b
```

A fresh promotion branch was then created from canonical `main` at PR #98 merge `4b4f31ec330d559318ae9aaaa6ad88533b6f0f8a`. The promoted live workflow reused the already-qualified Git blob directly rather than reconstructing or rewriting its text.

```text
PROMOTION_BASE=4b4f31ec330d559318ae9aaaa6ad88533b6f0f8a
PROMOTION_HEAD=2c69e54c18669ee96a077a0b2c197520118b7026
PROMOTION_PR=99
PROMOTION_CHANGED_PATH_COUNT=1
PROMOTION_CHANGED_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
PROMOTION_WORKFLOW_GIT_BLOB_SHA1=710cb4e6ecf1b34e93d3dfa3d59e24c3d60d1d79
PROMOTION_WORKFLOW_SHA256=836175ee057e2a6802b47db00766119d54c2034b63c8487f138dc125285f226b
PROMOTION_RAW_ACTIONS_RUNS_ON_EXACT_HEAD=0
PROMOTION_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
```

CodeRabbit independently qualified exact promotion head `2c69e54c18669ee96a077a0b2c197520118b7026` and reported:

```text
EXACT_HEAD=2c69e54c18669ee96a077a0b2c197520118b7026
PROMOTED_WORKFLOW_GIT_BLOB_SHA1=710cb4e6ecf1b34e93d3dfa3d59e24c3d60d1d79
PROMOTED_WORKFLOW_SHA256=836175ee057e2a6802b47db00766119d54c2034b63c8487f138dc125285f226b
PROMOTION_PR_CHANGED_PATH_COUNT=1
RAW_ACTIONS_RUNS_ON_EXACT_HEAD=0
MATERIAL_BLOCKER=NO
```

PR #99 was merged only with an expected-head guard against that exact qualified head.

```text
CANONICAL_PROMOTION_MERGE=85bd67981e6e7c04e9015fa046244128641469ea
CANONICAL_PROMOTION_TREE=db37beafdd74714c128b2f0ac5c1618231a937ee
CANONICAL_PROMOTION_PARENT_1=4b4f31ec330d559318ae9aaaa6ad88533b6f0f8a
CANONICAL_PROMOTION_PARENT_2=2c69e54c18669ee96a077a0b2c197520118b7026
```

## 3. Post-merge byte verification

After canonical promotion, the live workflow at the exact canonical merge was fetched from:

```text
.github/workflows/e004-llama-quantize-build-evidence.yml
```

GitHub reports its blob identity as:

```text
CANONICAL_LIVE_WORKFLOW_GIT_BLOB_SHA1=710cb4e6ecf1b34e93d3dfa3d59e24c3d60d1d79
```

This is the exact same Git blob as the independently SHA-256-qualified successor subject. Because Git blob identity is byte-identity, the post-merge live workflow bytes are unchanged from the reviewed subject and therefore retain the independently recomputed SHA-256:

```text
CANONICAL_LIVE_WORKFLOW_SHA256=836175ee057e2a6802b47db00766119d54c2034b63c8487f138dc125285f226b
POST_MERGE_WORKFLOW_BYTES_EQUAL_QUALIFIED_SUCCESSOR_BYTES=YES
POST_MERGE_WORKFLOW_GIT_BLOB_EQUALS_QUALIFIED_SUCCESSOR_GIT_BLOB=YES
POST_MERGE_WORKFLOW_SHA256_EQUALS_QUALIFIED_SUCCESSOR_SHA256=YES
```

The raw GitHub Actions API reports zero workflow runs with canonical promotion merge `85bd67981e6e7c04e9015fa046244128641469ea` as `head_sha`.

```text
RAW_ACTIONS_RUNS_ON_CANONICAL_PROMOTION_MERGE=0
UNEXPECTED_PROMOTION_OR_MERGE_RUN=NO
BUILD_EXECUTION_OCCURRED=NO
```

## 4. PR #96 allowance disposition remains unchanged

Run `33153171634` remains the pre-promotion incident already bound by the canonical successor recapture:

```text
PR96_RUN_ID=33153171634
PR96_EVENT=push
PR96_JOB_COUNT=0
PR96_BUILD_EXECUTION_OCCURRED=NO
AUTHORIZED_RUN_ALLOWANCE_CONSUMPTION_DISPOSITION=DOES_NOT_CONSUM_AUTHORIZED_MANUAL_ALLOWANCE
```

No later run has consumed the separately bounded manual allowance.

## 5. Pre-dispatch authority verification

The static governance and exact-subject conditions that can be verified before initiating the one bounded run now have the following state:

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION_B=CANONICAL
EXACT_AUTHORITY_CAPTURE=CANONICAL
SUCCESSOR_AUTHORITY_RECAPTURE=CANONICAL
CANONICAL_PROMOTION=YES
PROMOTED_WORKFLOW_PATH_MATCH=YES
PROMOTED_WORKFLOW_BYTE_IDENTITY_MATCH=YES
PROMOTION_SCOPE_EXACT=YES
FRESH_PROMOTION_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
UNEXPECTED_ACTIONS_RUN_BEFORE_OR_DURING_PROMOTION=NO
POST_MERGE_BYTE_VERIFICATION=PASS
PRE_DISPATCH_STATIC_GOVERNANCE_GATE=PASS
```

Runtime-only assertions remain deliberately unclaimed because no authorized run has started. The workflow itself is fail-closed on runner/tool availability, passwordless namespace creation, privilege/capability drop, `no_new_privs`, environment reset, sensitive platform environment absence, source identity, CMake configuration, target build, executable evidence, nonzero spend, unauthorized persistence, or any model/benchmark operation.

```text
RUNTIME_PREFLIGHT_EXECUTED=NO
RUNTIME_PREFLIGHT_PASS=NOT_CLAIMED
BUILD_PASS=NO
```

The unresolved exact provider-managed job-log retention-day value remains `NEEDS_EVIDENCE_CONNECTOR_NOT_EXPOSED`; the canonical authority record explicitly states that this does not authorize inference and is not itself a hard pre-run blocker unless later governance makes the numeric value mandatory. No such later requirement is established by this record.

## 6. Connected-executor capability check

After canonical promotion, the connected GitHub action surface available to this executor was re-inventoried. It exposes repository mutation, PR review/merge, workflow-run inspection, workflow-job/log/artifact inspection, and rerun operations for already-existing runs. It does **not** expose an action that initiates a new `workflow_dispatch` run.

Therefore the canonical tooling condition remains:

```text
CONNECTED_DISPATCH_ACTION_AVAILABLE=NO
EXECUTION_TOOLING_BLOCKER=ACTIVE
AUTHORIZED_MANUAL_RUN_EXECUTED=NO
AUTHORIZED_MANUAL_RUN_ALLOWANCE_REMAINING=1
AUTHORIZED_MANUAL_RUN_TRIGGER=workflow_dispatch_only
DISPATCH_ATTEMPTED_BY_CONNECTED_EXECUTOR=NO
WORKAROUND_TRIGGER_ATTEMPTED=NO
```

No automatic trigger, push workaround, rerun of an unrelated run, alternate workflow path, API substitution outside the connected authorized tool surface, or second-run interpretation is permitted.

### 6.1 Final exact-record-head Actions binding

The first exact-head review of this record correctly identified that the file must not rely on an unrecorded Actions lookup for the record's final review head. The record therefore makes the final-head evidence rule explicit.

A Git commit cannot contain a literal copy of its own final commit SHA without changing the commit being identified. The exact commit identity is therefore bound by immutable PR metadata plus a fresh exact-head review performed **after** the final record-content commit. The run count itself is recorded here and must be re-queried against that externally bound exact head before merge:

```text
THIS_RECORD_EXACT_HEAD_IDENTITY_SOURCE=IMMUTABLE_PR_METADATA_PLUS_FRESH_EXACT_HEAD_REVIEW
RAW_ACTIONS_RUNS_ON_THIS_RECORD_HEAD=0
FINAL_EXACT_HEAD_REVIEW_REQUIRED=YES
FINAL_EXACT_HEAD_REVIEW_MUST_REQUERY_RAW_ACTIONS=YES
FINAL_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NEEDS_FINAL_REVIEW
```

The `RAW_ACTIONS_RUNS_ON_THIS_RECORD_HEAD=0` assertion is not allowed to qualify by self-assertion. If the final exact-head reviewer observes any nonzero run count, head mismatch, changed scope, or other material discrepancy, this record fails closed and must not merge.

The superseded record-content head reviewed before this repair was:

```text
SUPERSEDED_RECORD_HEAD=7b9989965d6fd449ec150b04ebbdcd8a0c389ea2
RAW_ACTIONS_RUNS_ON_SUPERSEDED_RECORD_HEAD=0
SUPERSEDED_RECORD_HEAD_MATERIAL_BLOCKER=YES_MISSING_EXPLICIT_FINAL_HEAD_BINDING_RULE
```

That prior-head evidence is historical only and cannot qualify the repaired head.

## 7. Captured state at canonical promotion base

```text
CANONICAL_PROMOTION_BASE_AT_CAPTURE=85bd67981e6e7c04e9015fa046244128641469ea
CANONICAL_PROMOTION_TREE=db37beafdd74714c128b2f0ac5c1618231a937ee
LIVE_E004_BUILD_EVIDENCE_WORKFLOW=YES
CANONICAL_LIVE_WORKFLOW_GIT_BLOB_SHA1=710cb4e6ecf1b34e93d3dfa3d59e24c3d60d1d79
CANONICAL_LIVE_WORKFLOW_SHA256=836175ee057e2a6802b47db00766119d54c2034b63c8487f138dc125285f226b
CANONICAL_PROMOTION_VERIFIED=YES
EXECUTION_TOOLING_BLOCKER=ACTIVE
BUILD_EXECUTION_OCCURRED=NO
BUILD_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The broader E004 tournament remains blocked by its existing evidence and authority frontier, including the real A1-A14/A15 path and other separately governed prerequisites. This record does not alter those blockers and does not mark E004 complete.

## 8. Next executable frontier

The next action in this narrow Decision B build-evidence path is not available through the current connected executor.

If a future connected execution surface explicitly exposes initiation of a new GitHub Actions `workflow_dispatch`, the executor must first re-read live canonical `main`, this record's controlling authority, the exact live workflow bytes, all Actions runs since promotion, the remaining authorized-run count, and any intervening governance changes before deciding whether the single bounded run is still exercisable.

Until then:

```text
STOP_REASON=EXECUTION_TOOLING_BLOCKER
DO_NOT_CLAIM_BUILD_PASS=YES
DO_NOT_CONSUM_MANUAL_ALLOWANCE_BY_WORKAROUND=YES
DO_NOT_ADVANCE_E005=YES
DO_NOT_AUTHORIZE_TRAINING=YES
DO_NOT_AUTHORIZE_SPEND=YES
```
