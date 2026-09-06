# E004 Registry Current-State Reconciliation V33 — 2026-09-06

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Canonical base before this reconciliation:** `6a86bbc4a52adac3846a1eef97f89cb170fe202b`
**Predecessor:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v32-2026-09-05.md`
**Runtime evidence:** `specs/007-sft-v1/e004-successor-runtime-binding-run-evidence-2026-09-06.md`
**Artifact class:** deterministic current-state and dependency-frontier overlay
**Authority effect:** NONE beyond recording consumption of the already-authorized one-run runtime-evidence unit
**Model execution effect:** NONE
**Tournament execution effect:** NONE
**A15 effect:** NONE
**Training authority:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Recompute the exact E004 successor frontier after the single authorized non-model runtime-binding evidence run completed successfully as GitHub Actions run `33974098680`.

This reconciliation uses only evidence emitted by that run and previously canonical artifact/bundle/governance records. It does not infer model compatibility from static identifiers, open or load candidate weights, execute the tournament, or create A15 or any other authority.

## 2. One-run authority consumption

```text
MAX_AUTHORIZED_RUNTIME_BINDING_EVIDENCE_RUNS=1
OBSERVED_AUTHORIZED_RUNTIME_BINDING_EVIDENCE_RUNS=1
REMAINING_AUTHORIZED_RUNTIME_BINDING_EVIDENCE_RUNS=0
RERUN_AUTHORITY=NONE_BY_DEFAULT
RUNTIME_BINDING_EVIDENCE_RUN_ID=33974098680
RUNTIME_BINDING_EVIDENCE_RUN_HEAD=f5f5fbdcafa82d11bc0ddeb3dc641c729cf9fc79
RUNTIME_BINDING_EVIDENCE_RUN_CONCLUSION=success
WORKFLOW_ARTIFACT_COUNT=0
```

No second run, rerun, failed-job retry, or broadened evidence lane is authorized by this transition.

## 3. Candidate byte-integrity state retained from V32

```text
QWEN06_BYTE_INTEGRITY=PASS
QWEN35_BYTE_INTEGRITY=PASS
GRANITE_SELECTED_SOURCE_BYTE_INTEGRITY=PASS
CONTROL_SELECTED_SOURCE_BYTE_INTEGRITY=PASS
EXACT_FOUR_CANDIDATE_FROZEN_IDENTITY_SET=PASS
```

The exact frozen candidates remain:

```text
PRIMARY=Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
PRIMARY=Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
PRIMARY=ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
CONTROL=Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
CONTROL_WINNER_ELIGIBLE=NO
```

No candidate addition, substitution, revision drift, role drift, or winner selection is introduced.

## 4. Runtime evidence now closed

The selected llama.cpp route is directly bound by run `33974098680`:

```text
LLAMA_CPP_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
LLAMA_CPP_TAG=b10621
LLAMA_CPP_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
LLAMA_CPP_RUNTIME_FILE_MANIFEST_SHA256=4a6b0d2a9dee9d91fb1553ead9e26f49c1f232c86269013bd8a7edb82f0cd711
LLAMA_CPP_CLI_SHA256=f0034d9e6959f6c32b40cbb5326f41ccdbac21b77feb27a6f32c0a7465c9ebf7
LLAMA_CPP_CLI_NON_MODEL_INTROSPECTION=PASS_OFFLINE_NAMESPACE
STATIC_QWEN3_ARCHITECTURE_IDENTIFIER=PASS
STATIC_QWEN35_ARCHITECTURE_IDENTIFIER=PASS
EXACT_LLAMA_RUNTIME_ARCHIVE_INTEGRITY=PASS
EXACT_LLAMA_RUNTIME_EXECUTABLE_SHA256=PASS
EXACT_LLAMA_RUNTIME_SOURCE_REVISION_BINDING=PASS
```

Static architecture identifiers do not establish candidate-weight execution compatibility.

The selected Transformers/Torch route is directly bound by the same run:

```text
TRANSFORMERS_VERSION=4.57.6
TRANSFORMERS_COMMIT=753d61104116eefc8ffc977327b441ee0c8d599f
TORCH_VERSION=2.11.0+cpu
DEPENDENCY_ARTIFACT_COUNT=27
DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
PYTHON_RUNTIME_VERSION=Python_3.12.3
PYTHON_RUNTIME_SHA256=a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223
INSTALLED_ENVIRONMENT_MANIFEST_SHA256=54517b34077e193c9bc019e8a2b232d3c9b6d6a85c4c6df13bcd38aa2b66c384
QWEN3_CONFIG_MAPPING=PASS
QWEN3_CAUSAL_LM_MAPPING=PASS
GRANITE_CONFIG_MAPPING=PASS
GRANITE_CAUSAL_LM_MAPPING=PASS
STATIC_IMPORT_ONLY_COMPATIBILITY=PASS
EXACT_TRANSFORMERS_DEPENDENCY_CLOSURE=PASS
EXACT_TRANSFORMERS_RUNTIME_SOURCE_REVISION_BINDING=PASS
EXACT_PYTHON_RUNTIME_IDENTITY=PASS
EXACT_TRANSFORMERS_INSTALLED_ENVIRONMENT_IDENTITY=PASS
```

No model object was instantiated and no candidate weight file was opened, loaded, or executed. Static/import-only mapping evidence cannot be promoted into candidate-weight execution compatibility PASS.

## 5. Runtime-evidence safety state

```text
MODEL_OBJECT_INSTANTIATED=NO
MODEL_WEIGHT_FILE_OPENED=NO
MODEL_LOAD_PERFORMED=NO
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
CREDENTIAL_USE_PERFORMED=NO
ARTIFACT_UPLOAD_PERFORMED=NO
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
PAID_OR_LARGER_RUNNER_USED=NO
SPEND_USD=0
WORKFLOW_ARTIFACT_COUNT=0
```

The observed `ubuntu-24.04` / `20260831.293.1` runner identity is evidence for this runtime-evidence run only and is not automatically the future tournament execution-environment binding.

## 6. Exact four-candidate execution-subject recomputation

The successor control plane requires, for every frozen candidate, exact model-artifact and complete-bundle identities plus runtime artifact/executable/source/toolchain, tokenizer/config identity, execution-plan identity, entrypoint/argv, and candidate/runtime compatibility PASS.

```text
EXACT_LLAMA_RUNTIME_ARTIFACT_IDENTITY=PASS
EXACT_LLAMA_RUNTIME_EXECUTABLE_IDENTITY=PASS
EXACT_TRANSFORMERS_RUNTIME_ENVIRONMENT_IDENTITY=PASS
EXACT_RUNTIME_STATIC_ARCHITECTURE_OR_MAPPING_EVIDENCE=PASS_FOR_SELECTED_ROUTES
EXACT_FOUR_CANDIDATE_MODEL_BYTE_INTEGRITY=PASS

EXACT_FOUR_CANDIDATE_COMPLETE_BUNDLE_BINDINGS=INCOMPLETE
EXACT_FOUR_CANDIDATE_TOKENIZER_CONFIG_BINDINGS=INCOMPLETE
EXACT_FOUR_CANDIDATE_EXECUTION_PLAN_SHA256_BINDINGS=INCOMPLETE
EXACT_FOUR_CANDIDATE_RUNTIME_ARGV_BINDINGS=INCOMPLETE
EXACT_FOUR_CANDIDATE_RUNTIME_FORMAT_COMPATIBILITY=INCOMPLETE
EXACT_FOUR_CANDIDATE_RUNTIME_BINDINGS=INCOMPLETE
EXACT_FOUR_CANDIDATE_EXECUTION_ARTIFACT_SET=INCOMPLETE
EXACT_TOURNAMENT_EXECUTION_ENVIRONMENT_BINDING=INCOMPLETE
```

The remaining compatibility state stays fail-closed because no candidate weight was opened by the runtime-evidence lane.

## 7. Resource, access, finance, and A1-A14

The zero-spend runtime-evidence job proves only that its own evidence lane spent USD 0. It does not prove tournament resource suitability.

```text
CURRENT_AUTHORIZED_SPEND_USD=0
RUNTIME_EVIDENCE_LANE_SPEND=USD_0
EXACT_RESOURCE_BINDING=INCOMPLETE
EXACT_ACCESS_BINDING=INCOMPLETE
ZERO_INCREMENTAL_SPEND_TOURNAMENT_RESOURCE_BINDING=INCOMPLETE
A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
```

No incompatible legacy Spec 005 device semantics are imported into SP007.

## 8. Evaluation, contamination, privacy, and winner boundary

Previously canonical SP007 protocol/evaluation/curriculum/quarantine/contamination evidence remains governed by its own exact records and identities. This transition does not widen those scopes or expose protected payloads.

```text
PROTOCOL_ID=SP007_RO_001_NONCLINICAL_BACKBONE_TOURNAMENT_V1
PROTOCOL_SHA256=1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8
EVALUATION_ASSET_SET_SHA256=709d5f73c1599364fc184b959cbdfd199c7ec07307fef8f8091d8eafb10f5454
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
MODEL_WINNER_SELECTED=NO
E005_STATE=NOT_REACHED
```

## 9. A15 remains separate

```text
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
GENERIC_CONTINUATION_COUNTS_AS_A15_ACTIVATION=NO
```

A15 is not yet the sole unresolved prerequisite, so this reconciliation does not create or present an A15 activation token as though all earlier gates had passed.

## 10. Fresh successor disposition

```text
SUCCESSOR_PREFLIGHT_DISPOSITION=BLOCKED
SUCCESSOR_PASS_PREFLIGHT=NO
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
LIVE_SP007_PREEXECUTION_SUBJECT=ABSENT
MODEL_EXECUTION_NOW=NOT_AUTHORIZED_BY_GATE_STATE
TOURNAMENT_EXECUTION_NOW=NOT_AUTHORIZED_BY_GATE_STATE
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
TRAINING_PERFORMED=NO
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

The hardened caller-owned-PASS lock remains unchanged: supplied PASS labels or attestations cannot authorize a live request while the exact canonical pre-execution subject SHA is absent.

## 11. Task-ledger reconciliation

`specs/007-sft-v1/tasks.md` remains correctly unchecked for E004. This bounded transition updates only its E004 explanatory paragraph to point at V33 and the consumed runtime-evidence run without granting later-phase authority.

## 12. Next dependency-safe frontier

The next repository work is limited to deterministic reconciliation of already-canonical, non-sensitive evidence to determine whether remaining candidate bundle/tokenizer/config/execution-plan fields can be closed without new external execution or model access.

The unresolved dependency order is:

1. exact complete-bundle and tokenizer/config identities for all four frozen candidates;
2. exact per-candidate runtime entrypoint/argv and execution-plan identities;
3. exact candidate/runtime compatibility evidence sufficient under SP007 rather than static inference alone;
4. exact tournament execution-environment, resource, access, and zero-incremental-spend bindings;
5. a genuine applicable A1-A14 PASS snapshot;
6. only then the separately required A15 activation surface;
7. only after the exact canonical pre-execution subject is authorized may the frozen tournament execute.

No new runtime-evidence run is available under the consumed authorization. Any missing evidence requiring new model opening/execution, new external runtime evidence, credentials, gated assets, procurement, payment, or spend must stop at its separately scoped canonical authority boundary.

E005 winner selection remains downstream of an actual E004 tournament evidence pack and is not reached by this reconciliation.