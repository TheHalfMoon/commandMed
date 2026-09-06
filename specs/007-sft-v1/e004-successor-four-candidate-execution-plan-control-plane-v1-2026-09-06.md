# E004 Successor Four-Candidate Execution-Plan Control Plane V1 — 2026-09-06

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Canonical base at branch creation:** `21f0f8e321d10719dfbd424ec4f29b9eda0f3ff9`
**Predecessor implementation:** PR #273 / merge `21f0f8e321d10719dfbd424ec4f29b9eda0f3ff9`
**Authority source:** CM-3 bounded E004 execution-envelope corrective maintenance
**Execution effect:** NONE
**Training authority:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Close only the next dependency-safe deterministic control-plane gap after the canonical llama.cpp and Transformers/PyTorch adapter units: compose all four frozen candidates into one deterministic per-candidate execution-plan identity with one exact top-level orchestration entrypoint and `runtime_argv` per candidate.

This unit does not implement or invoke the future external executor. It does not load a model, execute a benchmark, open a device, access the network, select a winner, activate A15, or authorize execution.

## 2. Exact frozen candidate routes

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
ROLE=PRIMARY
ROUTE=LLAMA_CPP_GGUF

Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
ROLE=PRIMARY
ROUTE=LLAMA_CPP_GGUF

ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
ROLE=PRIMARY
ROUTE=TRANSFORMERS_TORCH_CPU

Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
ROLE=CONTROL
WINNER_ELIGIBLE=false
ROUTE=TRANSFORMERS_TORCH_CPU
```

Every plan is built from the exact frozen candidate artifact-bundle set and preserves the corresponding model artifact, complete bundle, tokenizer/config, role, winner-eligibility, and artifact-format identities.

## 3. Canonical adapter composition

For each GGUF PRIMARY candidate, `src/commandmed/spec007/e004_execution_plan.py` constructs and validates the canonical `e004_execution_adapter.py` llama.cpp manifest using a deterministic relative candidate workspace and frozen evaluation-payload layout.

For Granite PRIMARY and Qwen3-4B CONTROL, it constructs and validates the canonical `e004_transformers_adapter.py` manifest.

Each execution plan binds:

```text
adapter_id
adapter_sha256
adapter_operation_set_sha256
```

The adapter SHA-256 transitively binds the exact frozen scoring/resource operation projection. No adapter output is executed by this unit.

## 4. Backend runtime identities

The GGUF plans preserve the already-evidenced llama.cpp route:

```text
RUNTIME_FAMILY=LLAMA_CPP_GGUF
LLAMA_CPP_SOURCE_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
RUNTIME_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
BUILD_TOOLCHAIN_IDENTITY=GNU_11.4.0_LINUX_X86_64
LLAMA_PERPLEXITY_EXECUTABLE_SHA256=1c06240ed8594fd377d655aef2dab0865431e3e779c06638474c96b38e6d74a0
LLAMA_CLI_EXECUTABLE_SHA256=f0034d9e6959f6c32b40cbb5326f41ccdbac21b77feb27a6f32c0a7465c9ebf7
```

The SAFETENSORS plans preserve the already-evidenced Transformers/PyTorch route:

```text
RUNTIME_FAMILY=TRANSFORMERS_TORCH_CPU
TRANSFORMERS_SOURCE_REVISION=753d61104116eefc8ffc977327b441ee0c8d599f
TRANSFORMERS_VERSION=4.57.6
TORCH_VERSION=2.11.0+cpu
PYTHON_RUNTIME_ENTRYPOINT=python3.12
PYTHON_RUNTIME_VERSION=3.12.3
PYTHON_RUNTIME_SHA256=a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223
DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
INSTALLED_ENVIRONMENT_MANIFEST_SHA256=54517b34077e193c9bc019e8a2b232d3c9b6d6a85c4c6df13bcd38aa2b66c384
TRANSFORMERS_MODULE_SHA256=aa8cb54da488cf43ba37b9955bb6c0d84d2000db0306f6a5f1c20b6842482d04
TORCH_MODULE_SHA256=0387d8b811b289287479c8bfdf4e1dac3a71b246f938d82da1331cf2dc8bf001
```

These are static/runtime-toolchain identities already evidenced by the bounded runtime-binding lane. They are not empirical proof that any exact candidate weight bundle loads successfully.

## 5. Top-level orchestration contract

All four plans bind the same exact control-plane entrypoint identity:

```text
ORCHESTRATOR_CONTRACT_ID=COMMANDMED_E004_EXTERNAL_EXECUTOR_CONTRACT_V1
RUNTIME_ENTRYPOINT=commandmed-e004-external-executor-v1
ORCHESTRATOR_IMPLEMENTATION_STATE=NEEDS_FUTURE_EXECUTION_ENVIRONMENT_BINDING
WORKSPACE_LAYOUT_ID=SP007_RO_001_RELATIVE_WORKSPACE_V1
```

Each candidate has a deterministic `runtime_argv` containing only:

- the exact execution-plan ID;
- candidate ID and revision;
- exact backend family;
- exact adapter SHA-256;
- exact candidate-bundle-set SHA-256;
- exact evaluation-asset-set SHA-256;
- `network-mode=offline`;
- `authorized-spend-usd=0`.

The entrypoint is an exact future external-executor contract identity, not a claim that an executable implementation is already bound. The future execution environment must separately bind an implementation/executable identity before a live pre-execution subject can exist.

## 6. Deterministic execution-plan identity

Each per-candidate record carries:

```text
execution_plan_sha256=SHA256(canonical plan projection excluding execution_plan_sha256)
```

The four records are additionally composed into:

```text
plan_set_id=SP007_RO_001_FOUR_CANDIDATE_EXECUTION_PLAN_SET_V1
plan_set_sha256=SHA256(canonical plan-set projection excluding plan_set_sha256)
```

The canonical serializer is the repository's existing `eval_contract.canonical.compute_canonical_sha256`; no second identity mechanism is introduced.

## 7. Fail-closed boundary

Construction and validation require exact equality with:

- the frozen four-candidate set in dependency order;
- the frozen protocol and evaluation-asset-set identities;
- the frozen candidate artifact-bundle set;
- exact model artifact, complete bundle, tokenizer/config, role and format identities;
- the correct canonical adapter route for each candidate;
- exact previously evidenced backend runtime/toolchain identities;
- the exact top-level orchestrator contract and deterministic argv;
- canonical per-candidate and plan-set self hashes;
- `execution_performed=false`;
- `authorized_spend_usd=0`.

Tampered candidate identity, bundle data, route, adapter identity, argv, plan hash, plan order, or plan-set hash fails closed.

## 8. Deliberate non-closure

This unit must preserve:

```text
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=INCOMPLETE
RUNTIME_FORMAT_COMPATIBILITY_STATE=NEEDS_EMPIRICAL_MODEL_LOAD_EVIDENCE
ORCHESTRATOR_IMPLEMENTATION_STATE=NEEDS_FUTURE_EXECUTION_ENVIRONMENT_BINDING
EXACT_FUTURE_EXECUTION_ENVIRONMENT=INCOMPLETE
EXACT_RESOURCE_BINDING=INCOMPLETE
EXACT_ACCESS_BINDING_FOR_EXECUTION_SUBJECT=INCOMPLETE
ZERO_INCREMENTAL_SPEND_TOURNAMENT_RESOURCE_BINDING=INCOMPLETE
A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_PERFORMED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

Static adapter/runtime evidence must never be promoted into empirical model-load compatibility.

## 9. Qualification

The exact final PR head must pass the existing E004 research-component workflow. Qualification remains offline and deterministic and must include the new execution-plan tests through the Spec 007 regression and full repository regression suites.

```text
MODEL_LOAD_DURING_QUALIFICATION=PROHIBITED
MODEL_EXECUTION_DURING_QUALIFICATION=PROHIBITED
TOURNAMENT_EXECUTION_DURING_QUALIFICATION=PROHIBITED
SUBPROCESS_EXECUTION_DURING_QUALIFICATION=PROHIBITED
NETWORK_ACCESS_DURING_QUALIFICATION=PROHIBITED
A15_ACTIVATION_DURING_QUALIFICATION=PROHIBITED
SPEND_DURING_QUALIFICATION=PROHIBITED
```

Independent repository review remains optional by default under FD-007. Bot silence or review-service unavailability is not review PASS.

## 10. Successor frontier after canonical merge

If this unit becomes canonical on an exact qualified head, the next dependency-safe frontier is not model execution. It is a fresh reconciliation of the remaining pre-execution prerequisites, beginning with the separately evidenced exact per-candidate empirical model-load/runtime-format compatibility requirement and the still-unbound future execution environment/resource/access identities.

A15 remains separately authorized only after every preceding applicable gate is genuinely PASS. Generic continuation language does not activate A15.
