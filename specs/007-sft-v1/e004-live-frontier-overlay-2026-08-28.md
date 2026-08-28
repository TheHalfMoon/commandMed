# E004 Live Frontier Overlay — 2026-08-28

**Spec:** 007 SFT V1  
**Task:** E004  
**Artifact class:** append-only current-state reconciliation overlay  
**Canonical base:** `9d21403cf44ed3997ba106660160bb65c2898aa8`  
**Authority effect:** NONE  
**Execution performed by this record:** NO  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Earlier E004 prerequisite/frontier records remain immutable historical evidence, but several of their then-current frontier statements are now stale. In particular, the 2026-08-27 reconciliation predates the canonical Founder `ARTIFACT_DECISION_B`, exact conversion-subject preparation, static conversion-toolchain evidence, the qualified GitHub Actions successor/promotion chain, the canonical execution-tooling blocker, and the latest GitHub-hosted runner static evidence.

This overlay records the live frontier after those canonical events. It does not rewrite historical records or mark any real gate PASS merely because a control-plane or evidence artifact now exists.

```text
HISTORICAL_FRONTIER_RECORDS_PRESERVED=YES
THIS_RECORD_OVERRIDES_STALE_CURRENT_STATE_INTERPRETATION_ONLY=YES
REAL_GATE_PASS_CREATED=NO
EXECUTION_AUTHORITY_EXPANDED=NO
```

## 2. Canonical repository state at capture

```text
CANONICAL_MAIN_AT_CAPTURE=9d21403cf44ed3997ba106660160bb65c2898aa8
CANONICAL_MAIN_TREE=5cd4f02650c631a335344e45a9b4265c690b33d9

E001=CLOSED_CANONICAL
E002=CLOSED_CANONICAL
E003=CLOSED_CANONICAL
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The live E004 build-evidence workflow remains present at the sole authorized path:

```text
LIVE_WORKFLOW_PATH=.github/workflows/e004-llama-quantize-build-evidence.yml
LIVE_WORKFLOW_GIT_BLOB_SHA1=710cb4e6ecf1b34e93d3dfa3d59e24c3d60d1d79
QUALIFIED_WORKFLOW_SHA256=836175ee057e2a6802b47db00766119d54c2034b63c8487f138dc125285f226b
LIVE_WORKFLOW_TRIGGER=workflow_dispatch_only
```

The exact Git blob remains the independently qualified successor blob. No byte change is introduced by this record.

## 3. Artifact-decision frontier — historical decision request superseded

The older frontier stated:

```text
NEXT_FOUNDER_DECISION_1=FROZEN_ARTIFACT_ALLOWLIST_EXPANSION_OR_CONVERSION_RECONCILIATION
NEXT_FOUNDER_DECISION_1_STATE=REQUIRED_NOT_TAKEN
```

That statement is no longer current for the bounded preparation path.

PR #85 canonically captured Founder `ARTIFACT_DECISION_B` and prepared exactly two conversion subjects:

```text
PR85_MERGE=e7c83db3c305cc0f98bf04e182249cbd261e5da0
FOUNDER_ARTIFACT_DECISION=ARTIFACT_DECISION_B
EXACT_CONVERSION_SUBJECT_PREPARATION_AUTHORIZED=YES

SUBJECT_1=E004-CONVERT-GRANITE-350M-Q4_K_M-V1
SUBJECT_1_SOURCE=ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
SUBJECT_1_ROLE=PRIMARY

SUBJECT_2=E004-CONVERT-QWEN3-4B-CONTROL-Q4_K_M-V1
SUBJECT_2_SOURCE=Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
SUBJECT_2_ROLE=CONTROL
SUBJECT_2_WINNER_ELIGIBLE=NO
```

The decision authorizes preparation only:

```text
ARTIFACT_DECISION_B_STATE=CANONICAL_PREPARATION_AUTHORITY
OLD_ARTIFACT_DECISION_REQUIRED_NOT_TAKEN_STATE=SUPERSEDED_FOR_PREPARATION_SCOPE
CONVERSION_EXECUTION_AUTHORITY=NONE
CONVERTER_BUILD_EXECUTION_AUTHORITY=NONE
MODEL_LOADING_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
```

A later exact conversion-execution authorization would still be required. It is not currently eligible for truthful issuance because mandatory execution-subject fields remain unresolved.

## 4. Static conversion-toolchain frontier

PR #86 canonically bound the remaining repository-verifiable static source identities for the proposed toolchain:

```text
PR86_MERGE=e50f6ca65c23039613318153429030cbdc578c56
TOOL_REPOSITORY=ggml-org/llama.cpp
TOOL_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
CONVERSION_ENTRYPOINT=convert_hf_to_gguf.py
QUANTIZATION_ENTRYPOINT=llama-quantize
PROPOSED_QUANTIZATION_METHOD=Q4_K_M
STATIC_SOURCE_IDENTITY_RESEARCH=CLOSED_CANONICAL
```

Static source support is not executable identity or conversion evidence. The current unresolved toolchain fields include:

```text
CONVERSION_RUNTIME_EXECUTABLE_SHA256=NEEDS_EVIDENCE
LLAMA_QUANTIZE_EXECUTABLE_SHA256=NEEDS_EVIDENCE
BUILD_TOOLCHAIN_IDENTITY=NEEDS_EVIDENCE
COMPILER_IDENTITY=NEEDS_EVIDENCE
CMAKE_IDENTITY=NEEDS_EVIDENCE
PYTHON_RUNTIME_IDENTITY=NEEDS_EVIDENCE
EXACT_RESOLVED_DEPENDENCY_SET=NEEDS_EVIDENCE
DEPENDENCY_PACKAGE_HASH_SET=NEEDS_EVIDENCE
BUILD_ENVIRONMENT_MANIFEST_SHA256=NEEDS_EVIDENCE
```

No converter build is authorized by the preparation decision.

## 5. Source-model acquisition/integrity frontier

Canonical E002 remains independently active within its exact frozen scope. It authorizes non-executing acquisition and integrity/provenance work for the exact frozen public candidate revisions, including the Granite PRIMARY and Qwen3-4B CONTROL subjects above.

```text
MODEL_WEIGHT_ACCESS_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
MODEL_WEIGHT_DOWNLOAD_WITHOUT_EXECUTION=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
MODEL_ARTIFACT_METADATA_ACCESS_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
NO_MODEL_LOAD=ENFORCED
NO_MODEL_CONVERSION=ENFORCED
NO_BENCHMARK_PAYLOAD=ENFORCED
NO_TRAINING=ENFORCED
NO_CREDENTIALS=ENFORCED
NO_SPEND=ENFORCED
```

The prepared conversion subjects already bind public source-weight SHA-256 metadata, but public metadata is not local byte verification.

Current conversion-subject blockers still include:

```text
GRANITE_LOCAL_SOURCE_BUNDLE_IDENTITY=NEEDS_EVIDENCE
QWEN_CONTROL_LOCAL_SOURCE_BUNDLE_IDENTITY=NEEDS_EVIDENCE
EXACT_NON_WEIGHT_REQUIRED_INPUT_FILE_SHA256_SET=NEEDS_EVIDENCE
EXACT_INTEGER_SOURCE_WEIGHT_BYTES=NEEDS_EVIDENCE
EXACT_INTEGER_SOURCE_WEIGHT_BYTES_PER_QWEN_SHARD=NEEDS_EVIDENCE
```

Read-only public repository inspection performed during this reconciliation confirms the frozen source repositories/revisions remain public and available. No source-model bytes are stored in this repository by this record.

## 6. GitHub Actions build-evidence chain — promotion is canonical

The old frontier also predates the completed qualification/promotion chain.

```text
PR98_QUALIFIED_SUCCESSOR_MERGE=4b4f31ec330d559318ae9aaaa6ad88533b6f0f8a
PR99_CANONICAL_PROMOTION_MERGE=85bd67981e6e7c04e9015fa046244128641469ea
PR100_POST_PROMOTION_BLOCKER_RECORD_MERGE=6b0ca9d654b5302d95695ca46f4c669164543434
PR101_RUNNER_STATIC_EVIDENCE_MERGE=9d21403cf44ed3997ba106660160bb65c2898aa8
```

The live workflow was promoted byte-for-byte from the qualified subject and remains unchanged at capture.

The connected execution surface still does not expose initiation of a new GitHub Actions `workflow_dispatch` run. Canonical PR #100 therefore records:

```text
CONNECTED_DISPATCH_ACTION_AVAILABLE=NO
EXECUTION_TOOLING_BLOCKER=ACTIVE
AUTHORIZED_MANUAL_RUN_EXECUTED=NO
AUTHORIZED_MANUAL_RUN_ALLOWANCE_REMAINING=1
AUTHORIZED_MANUAL_RUN_TRIGGER=workflow_dispatch_only
DISPATCH_ATTEMPTED_BY_CONNECTED_EXECUTOR=NO
WORKAROUND_TRIGGER_ATTEMPTED=NO
BUILD_EXECUTION_OCCURRED=NO
BUILD_PASS=NO
```

No push, automatic trigger, unrelated rerun, alternate path, or API workaround may consume or emulate the one manual allowance.

## 7. Current GitHub-hosted runner static evidence

PR #101 canonically binds current public provider evidence for the already-selected standard `ubuntu-24.04` class while preserving runtime fail-closed semantics.

At that evidence capture, GitHub's public runner-image inventory bound:

```text
RUNNER_IMAGES_SOURCE_COMMIT=cbb8df97e1dd32af7cb23a90590f12734ec11d0b
PUBLISHED_IMAGE_VERSION=20260823.283.1
PUBLISHED_OS_VERSION=24.04.4_LTS
PUBLISHED_KERNEL_VERSION=6.17.0-1022-azure
PASSWORDLESS_SUDO_CLASS_DOCUMENTED=YES
```

Published inventory supports many required tools, but runtime-only evidence remains unresolved:

```text
UNSHARE_RUNTIME_AVAILABILITY=NEEDS_RUNTIME_EVIDENCE
SETPRIV_RUNTIME_AVAILABILITY=NEEDS_RUNTIME_EVIDENCE
SUDO_N_UNSHARE_NET_RUNTIME_SUCCESS=NEEDS_RUNTIME_EVIDENCE
NETWORK_NAMESPACE_CREATION=NEEDS_RUNTIME_EVIDENCE
SETUID_SETGID_DROP=NEEDS_RUNTIME_EVIDENCE
CAPABILITY_DROP=NEEDS_RUNTIME_EVIDENCE
NO_NEW_PRIVS=NEEDS_RUNTIME_EVIDENCE
POST_RESET_TOOL_IDENTITY=NEEDS_RUNTIME_EVIDENCE
FUTURE_ASSIGNED_IMAGE_VERSION=NEEDS_RUNTIME_EVIDENCE
```

The standard public runner remains a zero-spend evidence candidate under current provider policy; this creates no paid-runner or spend authority.

## 8. PR hygiene frontier

PR #97 represented an older V2 workflow subject and stale run-accounting state. After PRs #98-#100 became canonical, PR #97 was explicitly documented as superseded and closed without merge.

```text
PR97_STATE=CLOSED_UNMERGED_SUPERSEDED
PR97_MERGE_AUTHORITY=NONE
OLDER_V2_SUBJECT_REINTRODUCTION=PROHIBITED
```

The historical branch/PR remains audit evidence only.

## 9. Scientific A2/T1 frontier

The earlier public-research phase is not the current bottleneck for A2 method prose. Canonical artifacts already include a statistical-method candidate packet and a qualified-review request brief.

```text
A2_PUBLIC_RESEARCH=PREPARED
A2_STATISTICAL_METHOD_PACKET=CANONICAL_PREPARED
A2_QUALIFIED_REVIEW_REQUEST_BRIEF=CANONICAL_PREPARED
CLINICAL_REVIEW_AUTHORITY_IDENTITY=UNRESOLVED
STATISTICAL_REVIEW_AUTHORITY_IDENTITY=UNRESOLVED
CLINICAL_REVIEW_DISPOSITION=ABSENT
STATISTICAL_REVIEW_DISPOSITION=ABSENT
CANONICAL_GOVERNANCE_ADOPTION=ABSENT
NUMERIC_THRESHOLD_OR_MARGIN_FREEZE=NO
NUMERIC_N_FREEZE=NO
T1_A2=INCOMPLETE_REAL_EVIDENCE_NUMERIC_POLICY_AND_QUALIFIED_REVIEW
D34_A3_A4=BLOCKED_BY_T1
```

Repository/LLM/code-review activity cannot impersonate the required clinical or statistical review functions.

## 10. Parallel G1-G4 governance frontier

The operational candidate extraction for `G1/A5`, `G2/A6`, `G3/A8`, and `G4/A12` is already prepared from frozen Spec 005 architecture.

```text
G1_A5_OPERATIONAL_TEXT_CANDIDATE=PREPARED_FOR_GOVERNANCE_REVIEW_ONLY
G2_A6_OPERATIONAL_TEXT_CANDIDATE=PREPARED_FOR_GOVERNANCE_REVIEW_ONLY
G3_A8_OPERATIONAL_TEXT_CANDIDATE=PREPARED_FOR_GOVERNANCE_REVIEW_ONLY
G4_A12_OPERATIONAL_TEXT_CANDIDATE=PREPARED_FOR_GOVERNANCE_REVIEW_ONLY

G1_A5_REAL_GATE_PASS=NO
G2_A6_REAL_GATE_PASS=NO
G3_A8_REAL_GATE_PASS=NO
G4_A12_REAL_GATE_PASS=NO
```

The remaining evidence is not ordinary repository prose. Depending on the node it includes canonical governance/privacy/rights adoption, real contributor/content-rights evidence, real privacy attestations, real author/reviewer assignments and dispositions, or exact frozen-suite identity. Code review by repository bots is not a substitute.

## 11. Contamination and A15 remain separate

```text
CONTAMINATION_PRECONSTRUCTION_PLAN_CONTROL_PLANE=AVAILABLE
POSTCONSTRUCTION_CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
POSTCONSTRUCTION_CONTAMINATION_ASSESSMENT_EXECUTION=NOT_AUTHORIZED
REAL_A1_TO_A14_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
```

Actual contamination assessment cannot be performed for an unconstructed/unfrozen suite and has no current execution authority.

## 12. Current dependency-safe work

The following work remains permitted in principle when bounded to existing authority and performed without model/device/benchmark execution:

1. E002-authorized exact public source-model acquisition and static integrity/provenance verification at frozen revisions;
2. read-only source/evidence research that does not create scientific or governance PASS;
3. append-only state reconciliation when live truth supersedes an older current-state overlay;
4. static metadata/tool/source identity research under already-authorized preparation scope;
5. preparation of reviewer/governance coordination material without appointing or impersonating reviewers;
6. exact-head review/repair/merge of those bounded evidence artifacts.

The following are not repository-agent-authorizable merely from generic continuation approval:

```text
CONVERSION_EXECUTION_AUTHORITY
CONVERTER_BUILD_EXECUTION_AUTHORITY
QUALIFIED_CLINICAL_REVIEW_DISPOSITION
QUALIFIED_STATISTICAL_REVIEW_DISPOSITION
REAL_CONTRIBUTOR_OR_PERSONNEL_ATTESTATION
REAL_ACCESS_GRANT
REAL_SPEND_OR_ENGAGEMENT_AUTHORIZATION
CONTAMINATION_ASSESSMENT_AUTHORITY
A15_EXPLICIT_ACTIVATION
E005_BACKBONE_WINNER_SELECTION_BEFORE_E004_EVIDENCE
TRAINING
```

## 13. Live next-action frontier

The old single line `NEXT_FOUNDER_DECISION_1_STATE=REQUIRED_NOT_TAKEN` is superseded by a multi-branch live frontier:

```text
ARTIFACT_PREPARATION_DECISION=ARTIFACT_DECISION_B_CANONICAL
ARTIFACT_PREPARATION_SUBJECTS=PREPARED_INCOMPLETE_NOT_EXECUTABLE
CONVERSION_TOOLCHAIN_STATIC_IDENTITY=CANONICAL_PREPARED
SOURCE_BUNDLE_LOCAL_BYTE_INTEGRITY=INCOMPLETE_E002_AUTHORIZED_NON_EXECUTING
CONVERTER_BUILD_EXECUTION=BLOCKED_NO_AUTHORITY
CONVERSION_EXECUTION=BLOCKED_NO_AUTHORITY_AND_INCOMPLETE_SUBJECT

GITHUB_BUILD_EVIDENCE_WORKFLOW=CANONICAL_PROMOTED_VERIFIED
GITHUB_BUILD_EVIDENCE_DISPATCH=BLOCKED_CONNECTED_EXECUTION_TOOLING
AUTHORIZED_MANUAL_RUN_ALLOWANCE_REMAINING=1

A2_T1=BLOCKED_QUALIFIED_CLINICAL_STATISTICAL_REVIEW_AND_NUMERIC_POLICY
G1_G2_G3_G4=BLOCKED_REAL_GOVERNANCE_OPERATIONAL_EVIDENCE
CONTAMINATION_ASSESSMENT=BLOCKED_NO_AUTHORITY_AND_NO_FROZEN_SUITE
A15=BLOCKED_A1_TO_A14_NOT_PASS_AND_SEPARATE_ACTIVATION_REQUIRED
```

No one branch is allowed to imply that the others are complete.

## 14. Current state

```text
CANONICAL_BASE_AT_CAPTURE=9d21403cf44ed3997ba106660160bb65c2898aa8
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
BUILD_EXECUTION_OCCURRED=NO
BUILD_PASS=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

No task checkbox is changed by this record. No model, benchmark, device, converter, conversion, training, credential, personnel, procurement, or spend operation is performed.
