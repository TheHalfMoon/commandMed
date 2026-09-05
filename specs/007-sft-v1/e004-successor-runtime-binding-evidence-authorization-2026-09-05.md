# E004 Successor Runtime-Binding Evidence Authorization — 2026-09-05

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical frontier before this record:** `6d328b9a64a420bcb43fcd08f82745fd2604d47c`  
**Decision owner:** Founder  
**Decision class:** `E004_SUCCESSOR_RUNTIME_BINDING_EVIDENCE_AUTHORIZATION`  
**Decision state:** `AUTHORIZED_BOUNDED`  
**Model execution authority effect:** NONE  
**Tournament execution authority effect:** NONE  
**A15 authority effect:** NONE  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Founder direction and narrow interpretation

At the current canonical E004 successor frontier, after the exact E002 preconverted byte-integrity evidence run was launched and the repository plan identified runtime/toolchain/environment/resource binding as the next dependency-safe work, the Founder directed:

```text
FOUNDER_DIRECTION=go ahead, follow the plan in repo, do not stop until finish the projects
```

Consistent with the repository's bounded-authority precedent, this general continuation direction is interpreted only as authorization of the **first dependency-safe separately gated unit now required by the canonical plan**: non-model runtime-binding evidence needed to populate the exact `SP007-RO-001` pre-execution subject.

It is explicitly **not** interpreted as A15 activation, model execution, tournament execution, evaluation-payload execution, conversion, winner selection, training, credential/gated/private-data access, procurement, payment, or spend authority.

```text
E004_SUCCESSOR_RUNTIME_BINDING_EVIDENCE_AUTHORITY=AUTHORIZED_BOUNDED
A15_ACTIVATION_AUTHORITY=NONE
MODEL_EXECUTION_EXPANSION=NONE
TOURNAMENT_EXECUTION_EXPANSION=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 2. Exact objective

The authorized objective is to produce immutable evidence sufficient to determine — without loading any model — whether exact public runtime routes can be bound for the frozen four-candidate successor subject.

The evidence unit may bind only:

- exact runtime source/release identity;
- exact runtime archive/package and executable identities;
- exact runtime dependency/toolchain identities;
- exact environment manifest identity;
- exact static architecture/format-support evidence;
- exact entrypoint and non-model inspection argv;
- exact network/credential boundary used while obtaining runtime evidence;
- exact standard public GitHub-hosted runner metadata actually observed;
- exact zero-incremental-spend execution-resource candidate evidence without declaring the later execution-resource gate PASS by inference.

No model artifact may be opened by the runtime during this evidence unit.

## 3. Frozen candidate routes under investigation

The candidate universe remains exactly the canonical E001 set.

### GGUF route candidates

```text
QWEN06_CANDIDATE=Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
QWEN06_E002_GGUF_SHA256=218d3f063193b40008d4e63d90cf83e7dc6d33a8c6c1c647589f868a8fc74492
QWEN35_CANDIDATE=Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
QWEN35_E002_GGUF_SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
```

The bounded runtime candidate is the already project-qualified upstream source revision:

```text
LLAMA_CPP_REPOSITORY=ggml-org/llama.cpp
LLAMA_CPP_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
LLAMA_CPP_VERSION=0.3.0
LLAMA_CPP_NIGHTLY_TAG=b10621
LLAMA_CPP_NIGHTLY_TARGET_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_UBUNTU_X64_ARCHIVE=llama-b10621-bin-ubuntu-x64.tar.gz
LLAMA_CPP_UBUNTU_X64_ARCHIVE_BYTES=16291771
LLAMA_CPP_UBUNTU_X64_ARCHIVE_SHA256=91d7b03ddae498a39f28fdb85d84d2b4a0fd3838d10b4f897e0ef8975bb9b583
```

Static source evidence at the exact source commit contains both `LLM_ARCH_QWEN3` and `LLM_ARCH_QWEN35`. This permits static compatibility investigation only; it does not establish executable compatibility until the exact runtime artifact and its relevant static metadata are independently bound.

### Safetensors route candidates

```text
GRANITE_CANDIDATE=ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
CONTROL_CANDIDATE=Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
CONTROL_WINNER_ELIGIBLE=NO
```

The bounded Python-runtime candidate is the already evidenced dependency family used by the canonical E004 runtime-evidence lane:

```text
TRANSFORMERS_VERSION=4.57.6
TRANSFORMERS_TAG=v4.57.6
TRANSFORMERS_TAG_TARGET_COMMIT=753d61104116eefc8ffc977327b441ee0c8d599f
TORCH_RUNTIME_TARGET=2.11.0+cpu
PREVIOUS_EXACT_DEPENDENCY_SET_MANIFEST_SHA256=ebfd3c49dc83c35b3ad00e0d4d8b903502a8951fd65da80186b6677007bbfd3f
```

Static source evidence at the exact Transformers commit contains Qwen3 and Granite configuration/modeling implementations. This permits a static/import-only compatibility investigation for the source-safetensors route. It does not authorize `from_pretrained`, model construction from weights, tensor materialization, inference, generation, or any other model execution.

Qwen3.5 is **not** assigned to the Transformers 4.57.6 route by this record; it remains on the exact GGUF/llama.cpp investigation route above.

## 4. Permitted evidence actions

A review-first workflow may be prepared and, only after canonical qualification/merge, executed once on standard public `ubuntu-24.04` GitHub-hosted runners to:

1. download the exact public `llama-b10621-bin-ubuntu-x64.tar.gz` release archive and require its GitHub-published byte size and SHA-256;
2. extract it without model files, enumerate and hash the exact runtime files, bind `llama-cli` and required shared-library identities, and execute only non-model introspection such as `--version` or `--help`;
3. independently verify that the exact `c1d0e7a...` source revision contains the frozen Qwen3 and Qwen3.5 architecture identifiers used by the GGUF route;
4. acquire exact public Python packages needed to reconstruct the previously evidenced Transformers/Torch CPU dependency family, hash the dependency closure, install it into an isolated ephemeral environment, and bind Python/runtime/package identities;
5. import only library modules/classes required to prove that the exact Transformers runtime recognizes Qwen3 and Granite configurations/classes, without constructing or loading candidate weights;
6. emit all evidence to retained GitHub Actions logs only;
7. record exact runner/image/tool identities, network-acquisition phase, offline/static-inspection phase, credential state, and zero-spend boundary.

The workflow must use `permissions: {}` or the minimum technically required read-only repository permission, explicitly unset sensitive credential variables inside acquisition/inspection shells, use no Actions cache/artifact upload, and use no larger or paid runner.

## 5. Explicit prohibitions

```text
MODEL_WEIGHT_DOWNLOAD_BY_RUNTIME_EVIDENCE_LANE=PROHIBITED
MODEL_WEIGHT_OPEN_BY_RUNTIME=PROHIBITED
MODEL_OBJECT_CONSTRUCTION_FROM_CANDIDATE_WEIGHTS=PROHIBITED
MODEL_LOAD=PROHIBITED
MODEL_INFERENCE=PROHIBITED
GENERATION=PROHIBITED
BENCHMARK_OR_EVALUATION_PAYLOAD_ACCESS=PROHIBITED
TOURNAMENT_EXECUTION=PROHIBITED
RESOURCE_MEASUREMENT_WITH_MODEL=PROHIBITED
MODEL_CONVERSION=PROHIBITED
QUANTIZATION=PROHIBITED
REQUANTIZATION=PROHIBITED
WINNER_SELECTION=PROHIBITED
TRAINING=PROHIBITED
A15_ACTIVATION=PROHIBITED
CREDENTIAL_USE=PROHIBITED
GATED_ASSET_ACCESS=PROHIBITED
PRIVATE_GOLD_ACCESS=PROHIBITED
PHI_ACCESS=PROHIBITED
PROVIDER_API_GENERATION=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
SPEND_USD=0
```

The runtime evidence lane may not use the E002 model files as command arguments, stdin, environment variables, test fixtures, or runtime inputs. Static format support must be established from runtime source/release/package evidence only.

## 6. Qualification and one-run boundary

Before the evidence workflow is canonical and executable:

```text
REVIEW_FIRST=REQUIRED
PULL_REQUEST_RUNTIME_EVIDENCE_JOBS=SKIPPED_OR_INERT
EXACT_HEAD_STATIC_QUALIFICATION=REQUIRED
BOUNDED_AUTHORITY_BIND=REQUIRED
DIFF_WHITESPACE=PASS_REQUIRED
EXPECTED_HEAD_GUARDED_MERGE=REQUIRED
```

After the reviewed workflow is merged, exactly one evidence-trigger run may be created for this authority unit.

```text
MAX_AUTHORIZED_RUNTIME_BINDING_EVIDENCE_RUNS=1
RERUN_AUTHORITY=NONE_BY_DEFAULT
FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
```

Ordinary transport retries inside one job are permitted only for the same exact public runtime/dependency bytes and may not broaden source hosts or identities.

## 7. Effect of successful evidence

A successful evidence run may close only runtime-artifact/toolchain/static-compatibility evidence fields that it directly proves.

It does **not** automatically produce:

```text
LIVE_SP007_PREEXECUTION_SUBJECT=PASS
A1_A14_APPLICABLE_PASS_SNAPSHOT=PASS
A15_ACTIVATION=PASS
RESOURCE_BINDING=PASS
ACCESS_BINDING=PASS
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=<value>
MODEL_EXECUTION_AUTHORIZED_NOW=YES
```

Those transitions remain separately governed and must be established from their own exact evidence.

## 8. A15 separation

The Founder's general continuation direction captured here is not A15.

```text
GENERIC_CONTINUATION_COUNTS_AS_A15_ACTIVATION=NO
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
```

If all non-A15 successor prerequisites are later proven PASS, the repository must present the then-current exact A15 decision surface and obtain the separately required exact activation before the execution-subject lock can be opened.