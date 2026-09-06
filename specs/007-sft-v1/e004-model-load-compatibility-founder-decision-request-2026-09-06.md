# E004 Model-Load Compatibility Founder Decision Request — 2026-09-06

**Spec:** 007 SFT V1  
**Task:** E004  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Current global frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v38-2026-09-06.md`  
**Canonical base:** `75261eeef5cedf4963e77cc2ec6b8a59dbf1ca2e`  
**Artifact class:** Founder decision request only  
**Decision owner:** Founder  
**Decision state:** ABSENT  
**Authority effect of this document:** NONE  
**Model load performed:** NO  
**Model inference performed:** NO  
**Tournament execution performed:** NO  
**A15 activation:** ABSENT_NOT_AUTHORIZED  
**Training performed:** NO  
**Current authorized spend:** USD 0

## 1. Purpose

Resolve the earliest dependency-required authority gap after canonical V38: whether the repository may perform one exact, bounded, zero-spend empirical model-load compatibility evidence run for the four frozen `SP007-RO-001` candidates.

The sole scientific question is whether each exact frozen candidate artifact can be opened and loaded successfully by its exact already-bound runtime route without executing a forward pass, generation, benchmark, evaluation payload, tournament, winner selection, training, or any optimization.

This decision-request document creates no authority by itself.

## 2. Why a separate Founder decision is required

V38 canonically records:

```text
EXACT_FOUR_CANDIDATE_TOP_LEVEL_RUNTIME_ARGV=COMPLETE_BOUND_CONTROL_PLANE_ONLY
EXACT_EXECUTION_PLAN_SHA256_PER_CANDIDATE=COMPLETE_DETERMINISTIC
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=INCOMPLETE
RUNTIME_FORMAT_COMPATIBILITY_STATE_FOR_LIVE_SUBJECT=NOT_YET_PASS
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
```

The existing successor runtime-binding evidence authority explicitly prohibits opening candidate weights or loading a model. Therefore static architecture support, package imports, executable hashes, adapter construction, and deterministic argv cannot close this empirical compatibility fact.

The Founder's latest broad direction is captured only as context:

```text
FOUNDER_DIRECTION_CONTEXT=go ahead , do not stop until finish the project, you have my all permissions
```

That broad direction is not substituted for the exact decision below. Canonical precedent requires the operative Founder token to occur after this decision surface becomes canonical.

## 3. Exact frozen candidate and artifact subject

The candidate universe is exactly the canonical four-candidate artifact-bundle set:

```text
CANDIDATE_ARTIFACT_BUNDLE_SET_ID=SP007_RO_001_CANDIDATE_ARTIFACT_BUNDLE_SET_V1
CANDIDATE_ARTIFACT_BUNDLE_SET_SHA256=ee97fe0751743cc0d3a564b8f91add3c336267f08f2da86bf125dd7333db83fd
PROTOCOL_ID=SP007_RO_001_NONCLINICAL_BACKBONE_TOURNAMENT_V1
PROTOCOL_SHA256=1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8
```

### Candidate 1 — Qwen3 0.6B PRIMARY

```text
CANDIDATE=Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
ROLE=PRIMARY
ARTIFACT_FORMAT=GGUF
MODEL_ARTIFACT_SHA256=218d3f063193b40008d4e63d90cf83e7dc6d33a8c6c1c647589f868a8fc74492
MODEL_ARTIFACT_BYTES=396704512
COMPLETE_BUNDLE_SHA256=8b207e94ad7c5937dceced686603294ae5f150022ac2b355fee9997a408fc415
TOKENIZER_CONFIG_SHA256=3c04ed3ca964ea2f6b2b5faf0dc4d31aec1cb1e8b4bcf63f402d295046b422b5
RUNTIME_ROUTE=LLAMA_CPP_GGUF
```

### Candidate 2 — Qwen3.5 0.8B PRIMARY

```text
CANDIDATE=Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
ROLE=PRIMARY
ARTIFACT_FORMAT=GGUF
MODEL_ARTIFACT_SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
MODEL_ARTIFACT_BYTES=563035840
COMPLETE_BUNDLE_SHA256=682ef5c8fb914feb5346d5153e26b83e6bb3bb834aa1313cba240b61c0657592
TOKENIZER_CONFIG_SHA256=e611fbccc7c29ef3b1cafb1cb7ea548d189968632901d678fd62be68c47885de
RUNTIME_ROUTE=LLAMA_CPP_GGUF
```

### Candidate 3 — Granite 350M PRIMARY

```text
CANDIDATE=ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
ROLE=PRIMARY
ARTIFACT_FORMAT=SAFETENSORS
MODEL_ARTIFACT_SHA256=a65363c0803a05c1c74e114c692c57f35b2641aeffce24d5a8ee8fad3b34dcf0
MODEL_ARTIFACT_BYTES=704786224
COMPLETE_BUNDLE_SHA256=90c8061eefbe53328a9eb217d1163941a16387d5a078dc789dbccb159c0b41db
TOKENIZER_CONFIG_SHA256=a5ec5daab12ba090a90f3dd169c8f9c275557013a87b9c1258dc7cb497a35c86
RUNTIME_ROUTE=TRANSFORMERS_TORCH_CPU
```

### Candidate 4 — Qwen3 4B CONTROL

```text
CANDIDATE=Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
ROLE=CONTROL
WINNER_ELIGIBLE=false
ARTIFACT_FORMAT=SAFETENSORS
MODEL_ARTIFACT_IDENTITY_KIND=CANONICAL_WEIGHT_SHARD_MANIFEST_SHA256_V1
MODEL_ARTIFACT_SHA256=d7daa1f7a5f70276b29b71838f8e2c830a61f06b4e70c04de0987bd8c5b4a397
MODEL_ARTIFACT_BYTES=8044982000
COMPLETE_BUNDLE_SHA256=9d4e39cdff26b357a698371b4096167a7b70f07975d016460e4b7996399170b9
TOKENIZER_CONFIG_SHA256=3c04ed3ca964ea2f6b2b5faf0dc4d31aec1cb1e8b4bcf63f402d295046b422b5
RUNTIME_ROUTE=TRANSFORMERS_TORCH_CPU
```

No candidate, revision, artifact, shard set, tokenizer/config identity, role, or route may be substituted by caller choice.

## 4. Exact previously evidenced runtime identities

### llama.cpp route

```text
LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
LLAMA_BUILD_TOOLCHAIN_IDENTITY=GNU_11.4.0_LINUX_X86_64
LLAMA_CLI_EXECUTABLE_SHA256=f0034d9e6959f6c32b40cbb5326f41ccdbac21b77feb27a6f32c0a7465c9ebf7
LLAMA_PERPLEXITY_EXECUTABLE_SHA256=1c06240ed8594fd377d655aef2dab0865431e3e779c06638474c96b38e6d74a0
```

### Transformers/PyTorch CPU route

```text
TRANSFORMERS_SOURCE_REVISION=753d61104116eefc8ffc977327b441ee0c8d599f
TRANSFORMERS_VERSION=4.57.6
TORCH_VERSION=2.11.0+cpu
PYTHON_RUNTIME_ENTRYPOINT=python3.12
PYTHON_RUNTIME_VERSION=3.12.3
PYTHON_RUNTIME_SHA256=a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223
TRANSFORMERS_DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
TRANSFORMERS_INSTALLED_ENVIRONMENT_MANIFEST_SHA256=54517b34077e193c9bc019e8a2b232d3c9b6d6a85c4c6df13bcd38aa2b66c384
TRANSFORMERS_MODULE_SHA256=aa8cb54da488cf43ba37b9955bb6c0d84d2000db0306f6a5f1c20b6842482d04
TORCH_MODULE_SHA256=0387d8b811b289287479c8bfdf4e1dac3a71b246f938d82da1331cf2dc8bf001
```

Decision B, if selected after this surface is canonical, applies only when the evidence implementation rebinds and verifies these exact runtime identities. Any mismatch fails closed and consumes no authority to substitute a different runtime.

## 5. Decision classes

### `E004_MODEL_LOAD_COMPATIBILITY_DECISION_A` — preserve current prohibition

```text
FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_DECISION=E004_MODEL_LOAD_COMPATIBILITY_DECISION_A
MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=NONE
MODEL_WEIGHT_ACQUISITION_FOR_COMPATIBILITY_PROBE=NONE
MODEL_LOAD_AUTHORITY=NONE
```

Effect: V38 remains blocked at empirical model-load compatibility.

### `E004_MODEL_LOAD_COMPATIBILITY_DECISION_B` — authorize one exact four-candidate compatibility evidence run

```text
FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_DECISION=E004_MODEL_LOAD_COMPATIBILITY_DECISION_B
MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=AUTHORIZED_EXACT_SP007_RO_001_FOUR_CANDIDATE_LOAD_ONLY
MODEL_WEIGHT_ACQUISITION_FOR_COMPATIBILITY_PROBE=AUTHORIZED_EXACT_PUBLIC_UNGATED_CANONICAL_BUNDLE_FILES_ONLY
MODEL_LOAD_AUTHORITY=AUTHORIZED_COMPATIBILITY_PROBE_ONLY
MODEL_FORWARD_PASS_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
GENERATION_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
EVALUATION_PAYLOAD_EXECUTION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY_EXPANSION=NONE
WINNER_SELECTION_AUTHORITY=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Decision B permits only preparation, exact-head qualification, guarded merge, and exactly one post-merge evidence workflow run implementing the bounded probe described below.

## 6. Exact compatibility-probe semantics under Decision B

A candidate may receive `EMPIRICAL_MODEL_LOAD_COMPATIBILITY=PASS` only when all of the following are observed in the same identity-bound candidate probe:

1. every required candidate file is acquired from the exact public ungated source/revision already bound by the canonical bundle set;
2. every acquired file byte count and SHA-256 equals the canonical bundle record before runtime use;
3. the exact runtime route and runtime identities in Section 4 are reverified;
4. network and sensitive credential variables are disabled before model loading begins;
5. the runtime opens the exact candidate artifact and completes model construction/loading successfully;
6. no model forward pass, logits computation, token generation, benchmark input, evaluation input, tournament input, or training operation occurs;
7. the process records only repository-safe metadata needed to prove success/failure and exits;
8. candidate bytes are deleted from the ephemeral runner before job completion.

A process exit caused by unsupported format/architecture, malformed artifact, missing required local file, load exception, runtime crash, out-of-memory, or any other inability to complete exact loading is evidence of `FAIL` or `INCOMPLETE` according to the frozen implementation contract. It must never be converted to PASS by static evidence.

The evidence implementation must define exact pass/fail reason codes before the evidence run.

## 7. Acquisition, network, credential, retention, resource, and finance boundary

Decision B is intentionally narrow:

```text
SOURCE_CLASS=PUBLIC_UNGATED_EXACT_CANONICAL_BUNDLE_FILES_ONLY
NETWORK_DURING_BYTE_ACQUISITION=AUTHORIZED_ONLY_FOR_EXACT_PUBLIC_SOURCE_BYTES
NETWORK_DURING_MODEL_LOAD=PROHIBITED
USER_MANAGED_CREDENTIAL_USE=PROHIBITED
FOUNDER_PERSONAL_TOKEN_USE=PROHIBITED
REPOSITORY_SECRET_USE=PROHIBITED
GATED_ASSET_ACCESS=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
PHI_ACCESS=PROHIBITED
BENCHMARK_OR_EVALUATION_PAYLOAD_ACCESS=PROHIBITED
RAW_MODEL_BYTE_ARTIFACT_UPLOAD=PROHIBITED
ACTIONS_CACHE_FOR_MODEL_BYTES=PROHIBITED
MODEL_BYTE_PERSISTENCE_AFTER_JOB=PROHIBITED
RETAINED_EVIDENCE=GITHUB_ACTIONS_LOG_METADATA_ONLY
RUNNER_CLASS=STANDARD_PUBLIC_UBUNTU_24_04_ONLY
LARGER_OR_PAID_RUNNER=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
```

If an exact candidate cannot be loaded within the standard public `ubuntu-24.04` resource envelope, the probe must fail closed. Decision B does not authorize a larger runner, paid compute, a local Founder device, cloud credentials, or a second resource class.

## 8. One-run and no-rerun boundary

```text
MAX_AUTHORIZED_MODEL_LOAD_COMPATIBILITY_WORKFLOW_RUNS=1
AUTHORIZED_CANDIDATE_PROBES_PER_WORKFLOW=4_EXACTLY_ONE_PER_FROZEN_CANDIDATE
AUTOMATIC_RERUN_AUTHORITY=NONE
FAILED_RUN_RETRY_AUTHORITY=NONE
RESOURCE_ESCALATION_AUTHORITY=NONE
RUNTIME_SUBSTITUTION_AUTHORITY=NONE
CANDIDATE_SUBSTITUTION_AUTHORITY=NONE
```

The one workflow run may use separate standard public runner jobs for the four exact candidates if the implementation requires isolation. No additional workflow dispatch or rerun is authorized by Decision B.

Ordinary transport retries inside the same candidate job are allowed only for the same exact public source URL/revision/file identity and only before the SHA-256 gate. They do not authorize alternate mirrors or revisions.

## 9. Review-first and merge boundary

Decision B does not authorize immediate ad-hoc model loading from a pull-request job.

The repository must first prepare a bounded implementation/workflow on a feature branch. Before the single evidence run can occur:

```text
PULL_REQUEST_MODEL_LOAD=PROHIBITED
REVIEW_FIRST_WORKFLOW_PREPARATION=REQUIRED
EXACT_HEAD_STATIC_QUALIFICATION=REQUIRED
AUTHORITY_TOKEN_BINDING=REQUIRED
DIFF_WHITESPACE=PASS_REQUIRED
EXPECTED_HEAD_GUARDED_MERGE=REQUIRED
POST_MERGE_CANONICAL_REVERIFICATION=REQUIRED
```

The model-load step must be impossible on `pull_request` events. The one authorized evidence run may occur only after the implementation is canonical and only through the exact dedicated post-merge trigger defined by the implementation.

Independent repository review remains optional by default under FD-007 unless the implementation itself introduces a later explicit reviewer requirement.

## 10. Evidence effect and non-closure

A successful Decision B run may close only exact per-candidate empirical model-load/runtime-format compatibility fields directly proved by the run.

It does not automatically establish:

```text
ORCHESTRATOR_IMPLEMENTATION_STATE=PASS
EXACT_FUTURE_MODEL_EXECUTION_ENVIRONMENT=PASS
EXACT_COMPUTE_RESOURCE_IDENTITY=PASS
RESOURCE_AUTHORIZATION_BASIS=PASS
EXPECTED_CPU_RAM_DISK_ENVELOPE=PASS
EXPECTED_MAX_WALLCLOCK=PASS
EXACT_ACCESS_BINDING_FOR_EXECUTION_SUBJECT=PASS
EXACT_CREDENTIAL_STATE_BINDING=PASS
NETWORK_DURING_EXECUTION_BINDING=PASS
RETENTION_BINDING=PASS
ZERO_INCREMENTAL_SPEND_TOURNAMENT_RESOURCE_BINDING=PASS
A1_A14_APPLICABLE_PASS_SNAPSHOT=PASS
A15_ACTIVATION=PASS
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=<value>
MODEL_EXECUTION_AUTHORIZED_NOW=YES
TOURNAMENT_EXECUTION_AUTHORIZED_NOW=YES
```

Those remain dependency-ordered separate evidence/authority transitions.

## 11. A15 and training remain separate

Even if all four model-load probes pass:

```text
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
GENERIC_CONTINUATION_COUNTS_AS_A15_ACTIVATION=NO
TRAINING_AUTHORITY=NONE
TRAINING_PERFORMED=NO
```

A15 may be presented only after all preceding applicable pre-execution prerequisites are genuinely PASS. Training remains outside this decision entirely.

## 12. Exact Founder response required after canonical merge

To preserve the current prohibition:

```text
FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_DECISION=E004_MODEL_LOAD_COMPATIBILITY_DECISION_A
```

To authorize the exact bounded four-candidate compatibility evidence run:

```text
FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_DECISION=E004_MODEL_LOAD_COMPATIBILITY_DECISION_B
```

A broad continuation instruction, generic approval, statement that all permissions are granted, PR merge, or an earlier Founder token is not substituted for this exact decision.

The operative Founder response must occur after this decision-request surface is canonical and must be captured in a separate canonical decision record before model-weight acquisition or model-load workflow execution is authorized.

## 13. Current state until an operative decision is captured

```text
FOUNDER_E004_MODEL_LOAD_COMPATIBILITY_DECISION=ABSENT
MODEL_LOAD_COMPATIBILITY_PROBE_AUTHORITY=NONE
MODEL_WEIGHT_ACQUISITION_FOR_COMPATIBILITY_PROBE=NONE
MODEL_LOAD_AUTHORITY=NONE
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=INCOMPLETE
A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
MODEL_LOAD_PERFORMED=NO
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_AUTHORITY=NONE
TRAINING_PERFORMED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

## 14. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is optional by default for this bounded decision-request artifact.

Before merge, reverify exact base/head/diff, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, exact V38/bundle/runtime identities, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
