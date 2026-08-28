# E004 Live Frontier Build-Authority Correction — 2026-08-28

**Spec:** 007 SFT V1  
**Task:** E004  
**Artifact class:** append-only canonical-state correction  
**Canonical base:** `7032016fbc277ad7ceaf0d597b98814c1cd89b35`  
**Corrects current-state interpretation in:** `e004-live-frontier-overlay-2026-08-28.md` / PR #102  
**Authority effect:** NONE — restores already-canonical authority truth only  
**Execution performed by this record:** NO  
**Model conversion authority:** NONE  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Correction purpose

PR #102 correctly reconciled several stale E004 frontier statements, but its live-state overlay made one material authority-class error: it stated or implied that converter-build execution authority remained `NONE`.

That assertion conflicts with an earlier canonical Founder authority record that PR #102 should have treated as controlling live truth.

This correction is append-only. It does not rewrite or delete PR #102. It explicitly supersedes only the incorrect current-state interpretation of the build-evidence authority class while preserving all correct PR #102 statements about conversion, E004 completion, E005, training, credentials, and spend.

```text
PR102_MERGE=7032016fbc277ad7ceaf0d597b98814c1cd89b35
PR102_BUILD_AUTHORITY_ASSERTION=INCORRECT_STALE_INTERPRETATION
THIS_CORRECTION_SCOPE=BUILD_EVIDENCE_AUTHORITY_STATE_ONLY
HISTORY_REWRITE=NO
AUTHORITY_EXPANSION_BY_THIS_RECORD=NO
```

## 2. Canonical build authority predates PR #102

PR #87 canonically merged the Founder-authorized bounded conversion-toolchain build-evidence lane.

```text
PR87=MERGED
PR87_HEAD=8916b087d3cf6b1e042e5df15fc6985472c20074
PR87_MERGE=0a0d1768f496a8043acf8bfccc3f8b6f213d0ff5
AUTHORITY_RECORD=specs/007-sft-v1/e004-conversion-toolchain-build-authority-2026-08-28.md
```

The canonical authority record states:

```text
E004_CONVERSION_TOOLCHAIN_BUILD_AUTHORITY=AUTHORIZED_BOUNDED
CONVERTER_BUILD_EXECUTION_AUTHORITY=AUTHORIZED_EXACT_LLAMA_CPP_REVISION_BUILD_EVIDENCE_ONLY
BUILD_TOOL_REPOSITORY=ggml-org/llama.cpp
BUILD_TOOL_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
BUILD_TARGET=llama-quantize
OUTPUT_AUTHORITY=BUILD_EVIDENCE_ONLY
```

The bounded authority permits exact tool-source/dependency acquisition, an isolated zero-spend build environment, building `llama-quantize`, executable hashing, and environment/toolchain evidence collection. It does not permit transforming model bytes.

## 3. PR #88 blocked an environment, not the authority

PR #88 canonically recorded the first real build-evidence preflight attempt.

```text
PR88=MERGED
PR88_HEAD=36941015659adb58051bf5258e7244f2fd119632
PR88_MERGE=5da5949ee9c3cc08f94d2f3f0993097cc30c060d
BUILD_PREFLIGHT_EXECUTED=YES
EXACT_SOURCE_BYTES_MATERIALIZED=NO
BUILD_CONFIGURATION_EXECUTED=NO
LLAMA_QUANTIZE_BUILD_EXECUTED=NO
LLAMA_QUANTIZE_EXECUTABLE_PRODUCED=NO
BUILD_PASS=NO
```

The exact source archive could not be materialized in the available execution environment because outbound source-materialization connectivity was unavailable. The preflight therefore failed closed before configure/build.

The same canonical record explicitly preserves:

```text
CONVERTER_BUILD_EXECUTION_AUTHORITY=AUTHORIZED_EXACT_LLAMA_CPP_REVISION_BUILD_EVIDENCE_ONLY
BUILD_EVIDENCE_LANE_STATE=BLOCKED_SOURCE_MATERIALIZATION_IN_CURRENT_ENVIRONMENT
```

Therefore:

```text
FAILED_LOCAL_PREFLIGHT_REVOKES_BUILD_AUTHORITY=NO
FAILED_LOCAL_PREFLIGHT_EQUALS_BUILD_PASS=NO
FAILED_LOCAL_PREFLIGHT_EQUALS_CONVERSION_AUTHORITY=NO
```

## 4. GitHub Actions is the selected bounded alternate environment path

After the local source-materialization blocker, the Founder selected `BUILD_ENVIRONMENT_DECISION_B` for an exact bounded external environment class:

```text
FOUNDER_BUILD_ENVIRONMENT_DECISION=BUILD_ENVIRONMENT_DECISION_B
PROVIDER=GitHub_Actions
RUNNER_CLASS=STANDARD_GITHUB_HOSTED_PUBLIC_REPOSITORY_RUNNER
RUNNER_LABEL=ubuntu-24.04
PURPOSE=E004_LLAMA_QUANTIZE_BUILD_EVIDENCE_ONLY
MAX_AUTHORIZED_WORKFLOW_RUNS=1
TRIGGER=workflow_dispatch_only
CURRENT_AUTHORIZED_SPEND_USD=0
```

That environment decision did not authorize model conversion. It established the next governed environment path for exercising the pre-existing bounded build-evidence purpose only after exact subject capture/review/promotion.

The later canonical chain completed those preparation/promotion steps:

```text
PR98_QUALIFIED_SUCCESSOR_MERGE=4b4f31ec330d559318ae9aaaa6ad88533b6f0f8a
PR99_CANONICAL_PROMOTION_MERGE=85bd67981e6e7c04e9015fa046244128641469ea
PR100_POST_PROMOTION_TOOLING_BLOCKER_MERGE=6b0ca9d654b5302d95695ca46f4c669164543434
PR101_RUNNER_STATIC_EVIDENCE_MERGE=9d21403cf44ed3997ba106660160bb65c2898aa8
LIVE_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
LIVE_WORKFLOW_GIT_BLOB_SHA1=710cb4e6ecf1b34e93d3dfa3d59e24c3d60d1d79
QUALIFIED_WORKFLOW_SHA256=836175ee057e2a6802b47db00766119d54c2034b63c8487f138dc125285f226b
```

The current connected execution surface still cannot initiate a new `workflow_dispatch`, so the selected GitHub Actions execution path remains blocked by tooling rather than by absence of build authority.

```text
CONNECTED_DISPATCH_ACTION_AVAILABLE=NO
EXECUTION_TOOLING_BLOCKER=ACTIVE
AUTHORIZED_MANUAL_RUN_EXECUTED=NO
AUTHORIZED_MANUAL_RUN_ALLOWANCE_REMAINING=1
AUTHORIZED_MANUAL_RUN_TRIGGER=workflow_dispatch_only
BUILD_EXECUTION_OCCURRED_ON_GITHUB_ACTIONS_PATH=NO
BUILD_PASS=NO
```

## 5. Correct authority separation

The current canonical distinction is:

```text
E004_CONVERSION_TOOLCHAIN_BUILD_AUTHORITY=AUTHORIZED_BOUNDED
CONVERTER_BUILD_EXECUTION_AUTHORITY=AUTHORIZED_EXACT_LLAMA_CPP_REVISION_BUILD_EVIDENCE_ONLY

MODEL_CONVERSION_AUTHORITY=NONE
QUANTIZATION_OF_MODEL_WEIGHTS_AUTHORITY=NONE
MODEL_LOADING_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

A successful `llama-quantize` tool build would still be build evidence only. It would not authorize using that executable on model weights.

## 6. Effect on the PR #102 overlay

The following PR #102/live-overlay interpretation is superseded:

```text
CONVERTER_BUILD_EXECUTION=BLOCKED_NO_AUTHORITY
```

The correct current interpretation is:

```text
CONVERTER_BUILD_EXECUTION_AUTHORITY=AUTHORIZED_EXACT_LLAMA_CPP_REVISION_BUILD_EVIDENCE_ONLY
LOCAL_BUILD_ATTEMPT_STATE=BLOCKED_SOURCE_MATERIALIZATION_IN_PREVIOUS_ENVIRONMENT
GITHUB_ACTIONS_BUILD_PATH_STATE=BLOCKED_CONNECTED_EXECUTION_TOOLING
AUTHORIZED_MANUAL_RUN_ALLOWANCE_REMAINING=1
BUILD_PASS=NO
```

All other fail-closed downstream boundaries remain unchanged.

## 7. Current live frontier after correction

```text
E004_CONVERSION_TOOLCHAIN_BUILD_AUTHORITY=AUTHORIZED_BOUNDED
BUILD_EVIDENCE_LANE=AUTHORIZED_BUT_NOT_SUCCESSFULLY_EXECUTED

LOCAL_PREVIOUS_ENVIRONMENT_BUILD_RESULT=NOT_EXECUTED_SOURCE_MATERIALIZATION_BLOCKED
GITHUB_BUILD_EVIDENCE_WORKFLOW=CANONICAL_PROMOTED_VERIFIED
GITHUB_BUILD_EVIDENCE_DISPATCH=BLOCKED_CONNECTED_EXECUTION_TOOLING
AUTHORIZED_MANUAL_RUN_ALLOWANCE_REMAINING=1
BUILD_PASS=NO

ARTIFACT_DECISION_B=CANONICAL_PREPARATION_AUTHORITY
EXACT_CONVERSION_SUBJECT_PREPARATION_AUTHORIZED=YES
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE

SOURCE_BUNDLE_LOCAL_BYTE_INTEGRITY=INCOMPLETE_E002_AUTHORIZED_NON_EXECUTING
A2_T1=BLOCKED_QUALIFIED_CLINICAL_STATISTICAL_REVIEW_AND_NUMERIC_POLICY
G1_G2_G3_G4=BLOCKED_REAL_GOVERNANCE_OPERATIONAL_EVIDENCE
CONTAMINATION_ASSESSMENT=BLOCKED_NO_AUTHORITY_AND_NO_FROZEN_SUITE
A15=BLOCKED_A1_TO_A14_NOT_PASS_AND_SEPARATE_ACTIVATION_REQUIRED

E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 8. Review requirement

This correction must receive fresh exact-head review because PR #102's exact-head review did not detect the conflict with the canonical build-authority record.

The reviewer must independently re-read at minimum:

- PR #87 / `e004-conversion-toolchain-build-authority-2026-08-28.md`;
- PR #88 / `e004-conversion-toolchain-build-execution-preflight-2026-08-28.md`;
- `e004-founder-build-environment-decision-b-2026-08-28.md`;
- the exact GitHub Actions authority/promotion/tooling-blocker chain;
- PR #102 and this correction.

No prior review result may be reused as qualification for this correction.
