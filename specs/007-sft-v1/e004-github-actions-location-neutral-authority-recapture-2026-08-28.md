# E004 GitHub Actions Location-Neutral Authority Recapture — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `80bfdd08d76d3fdd418a036f6d6bc35c9eed45a8`  
**Predecessor authority capture:** `specs/007-sft-v1/e004-github-actions-exact-authority-capture-2026-08-28.md` / PR #93  
**Abandoned promotion:** PR #94 / CLOSED_UNMERGED  
**Founder environment decision:** `BUILD_ENVIRONMENT_DECISION_B`  
**Authority class:** successor exact-subject recapture for comment-only claims-integrity correction  
**Runtime semantics authority expansion:** NONE  
**Live workflow created:** NO  
**Workflow execution occurred:** NO  
**Build pass:** NO  
**Current authorized spend:** USD 0

## 1. Why a successor capture is required

PR #93 canonically bound the first exact promotion subject. During the subsequent byte-identical promotion attempt, PR #94 exposed a claims-integrity defect in that subject's provenance-era header: after placement at `.github/workflows/e004-llama-quantize-build-evidence.yml`, the copied text would still state that the file is stored outside `.github/workflows`.

PR #94 was closed without merge and without execution. The predecessor capture explicitly requires a new exact authority capture whenever candidate bytes change. This record follows that rule instead of editing the live-promotion copy or silently inheriting the old digest.

```text
PR94_MERGED=NO
PR94_WORKFLOW_RUN_EXECUTED=NO
OLD_QUALIFIED_CANDIDATE_GIT_BLOB_SHA1=73cfdb744fddb48004047b441cf4a3f08b4385b3
OLD_QUALIFIED_CANDIDATE_SHA256=c50a94993a8ec7e412346d3b26806ef4472360a7fac90cc7da33b6409ee4f63b
OLD_CAPTURE_REMAINS_HISTORICAL_CANONICAL=YES
OLD_CAPTURE_AUTHORIZES_NEW_BYTES=NO
```

## 2. Corrected exact subject

The candidate remains at:

```text
CANDIDATE_PATH=specs/007-sft-v1/candidates/e004-github-actions-build-evidence.workflow.yml.example
CANDIDATE_GIT_BLOB_SHA1=b9ebaa40fa48d41bc2dfecab57368e0fe5647d4a
CANDIDATE_SHA256=b422568fa535a29f6887cad2b158c3bbad059c8bbb4999c3ca5a75e5e840332f
DIGEST_EVIDENCE_HEAD=ffd84716d126cbafa37b9ad9f42a9cbefe4eab28
DIGEST_EVIDENCE_SOURCE=LOCAL_BYTE_LEVEL_GIT_BLOB_CROSSCHECK_PLUS_CUBIC_EXACT_HEAD_SEMANTIC_REVIEW
INTENDED_LIVE_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
```

The new header is location-neutral:

- while the file is stored outside `.github/workflows`, it describes the file as non-executable review material;
- it states that promotion is allowed only under canonical Decision B, exact authority capture, and fresh exact-subject review;
- it states that presence at the live path does not itself authorize dispatch;
- it preserves post-merge byte verification and pre-run gates.

A byte-level recomputation of the exact candidate content reproduced Git blob SHA-1 `b9ebaa40fa48d41bc2dfecab57368e0fe5647d4a` and SHA-256 `b422568fa535a29f6887cad2b158c3bbad059c8bbb4999c3ca5a75e5e840332f`. Cubic's exact-head summary for `ffd84716d126cbafa37b9ad9f42a9cbefe4eab28` independently confirmed that the candidate delta is comment-only, executable YAML after the header is unchanged, the new header fixes the location-truthfulness defect, no `.github/workflows` file is created or modified, and no workflow run is dispatched. CodeRabbit manual review was requested but its chat surface hit a rate limit; no CodeRabbit PASS is claimed for this head.

## 3. Runtime-semantic invariance

Repository compare evidence from canonical base `80bfdd08...` to candidate-correction commit `459f9e88...` shows exactly one changed file with 5 additions and 3 deletions, all in the opening comment block. Cubic independently summarized the exact PR head as comment-only and confirmed the executable YAML following the header remains unchanged.

```text
RUNTIME_YAML_CHANGED=NO
TRIGGER_CHANGED=NO
PERMISSIONS_CHANGED=NO
RUNNER_CHANGED=NO
SOURCE_IDENTITY_CHANGED=NO
BUILD_TARGET_CHANGED=NO
NETWORK_BOUNDARY_CHANGED=NO
PRIVILEGE_BOUNDARY_CHANGED=NO
CAPABILITY_BOUNDARY_CHANGED=NO
NO_NEW_PRIVS_BOUNDARY_CHANGED=NO
ENVIRONMENT_BOUNDARY_CHANGED=NO
SECURITY_EVIDENCE_CHANGED=NO
PERSISTENCE_POLICY_CHANGED=NO
```

## 4. Inherited bounded envelope

Only the exact subject identity changes. All other canonical Decision B / PR #93 limits remain unchanged:

```text
PROVIDER=GitHub_Actions
RUNNER_LABEL=ubuntu-24.04
TRIGGER=workflow_dispatch_only
WORKFLOW_PERMISSIONS={}
MAX_AUTHORIZED_WORKFLOW_RUNS=1
TOOL_REPOSITORY_URL=https://github.com/ggml-org/llama.cpp.git
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
BUILD_TARGET=llama-quantize
CURRENT_AUTHORIZED_SPEND_USD=0
```

No package installation, third-party action, cache, artifact upload, release, package publication, model operation, benchmark/device operation, contamination assessment, selection-suite construction, training, credentials, procurement, or spend is authorized by this recapture.

## 5. Promotion conditions for the successor subject

The new subject may not be promoted until this recapture is reviewed and canonical:

```text
THIS_RECAPTURE_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
-> THIS_RECAPTURE_CANONICAL
-> FRESH_PROMOTION_BRANCH_FROM_THEN_CURRENT_CANONICAL_MAIN
-> PROMOTED_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
-> PROMOTED_WORKFLOW_GIT_BLOB_EQUALS_NEW_QUALIFIED_CANDIDATE_BLOB=YES
-> PROMOTED_WORKFLOW_SHA256_EQUALS_NEW_QUALIFIED_CANDIDATE_SHA256=YES
-> FRESH_PROMOTION_EXACT_HEAD_REVIEW_MATERIAL_BLOCKER=NO
-> CANONICAL_PROMOTION_MERGE
-> POST_MERGE_BYTE_VERIFICATION
-> ALL_PRE_RUN_CONDITIONS_STILL_PASS
-> AT_MOST_ONE_MANUAL_RUN
```

Any further candidate-byte change requires another exact authority capture.

## 6. Current state

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION=BUILD_ENVIRONMENT_DECISION_B
SUCCESSOR_EXACT_AUTHORITY_RECAPTURE=PENDING_FINAL_EXACT_HEAD_REVIEW_AFTER_DIGEST_BINDING
NEW_CANDIDATE_GIT_BLOB_SHA1=b9ebaa40fa48d41bc2dfecab57368e0fe5647d4a
NEW_CANDIDATE_SHA256=b422568fa535a29f6887cad2b158c3bbad059c8bbb4999c3ca5a75e5e840332f
LIVE_WORKFLOW_CREATED=NO
WORKFLOW_RUN_EXECUTED=NO
BUILD_PASS=NO
CONVERSION_EXECUTION_AUTHORITY=NONE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Exit evidence required

Fresh exact-head review after digest binding must independently confirm:

```text
COMMENT_ONLY_DELTA=YES
LOCATION_NEUTRAL_HEADER_IS_TRUTHFUL_IN_CANDIDATE_AND_LIVE_CONTEXTS=YES
RUNTIME_YAML_BYTE_SEQUENCE_AFTER_HEADER_UNCHANGED=YES
NEW_CANDIDATE_GIT_BLOB_MATCHES=YES
NEW_CANDIDATE_SHA256_RECOMPUTED_AND_BOUND=YES
PREDECESSOR_RUNTIME_AND_AUTHORITY_LIMITS_UNCHANGED=YES
NO_LIVE_WORKFLOW_OR_RUN_CREATED=YES
NO_DOWNSTREAM_AUTHORITY_EXPANSION=YES
BUILD_PASS_REMAINS_NO=YES
E004_REMAINS_BLOCKED_PREFLIGHT=YES
```

Any material finding must be repaired before canonical merge.