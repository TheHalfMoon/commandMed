# E004 Successor Transformers/PyTorch Adapter Control Plane V1 — 2026-09-06

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Predecessor frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v37-2026-09-06.md`
**Authority source:** CM-3 bounded E004 execution-envelope corrective maintenance
**Execution effect:** NONE
**Training authority:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Close only the next dependency-safe deterministic control-plane gap identified by V37: bind the frozen Granite PRIMARY and Qwen3-4B CONTROL SAFETENSORS candidates to the already-evidenced Transformers/PyTorch runtime identities and to exact non-executing projections of the frozen SP007-RO-001 scoring/resource semantics.

This unit does not load either model and does not prove empirical model-load compatibility.

## 2. Frozen candidate route

```text
GRANITE_CANDIDATE=ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
GRANITE_ROLE=PRIMARY
GRANITE_WINNER_ELIGIBLE=true
GRANITE_MODEL_ARTIFACT_SHA256=a65363c0803a05c1c74e114c692c57f35b2641aeffce24d5a8ee8fad3b34dcf0
GRANITE_MODEL_ARTIFACT_BYTES=704786224
GRANITE_COMPLETE_BUNDLE_SHA256=90c8061eefbe53328a9eb217d1163941a16387d5a078dc789dbccb159c0b41db
GRANITE_COMPLETE_BUNDLE_BYTES=714515562
GRANITE_TOKENIZER_CONFIG_SHA256=a5ec5daab12ba090a90f3dd169c8f9c275557013a87b9c1258dc7cb497a35c86

CONTROL_CANDIDATE=Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
CONTROL_ROLE=CONTROL
CONTROL_WINNER_ELIGIBLE=false
CONTROL_MODEL_ARTIFACT_SHA256=d7daa1f7a5f70276b29b71838f8e2c830a61f06b4e70c04de0987bd8c5b4a397
CONTROL_MODEL_ARTIFACT_BYTES=8044982000
CONTROL_COMPLETE_BUNDLE_SHA256=9d4e39cdff26b357a698371b4096167a7b70f07975d016460e4b7996399170b9
CONTROL_COMPLETE_BUNDLE_BYTES=8056508630
CONTROL_TOKENIZER_CONFIG_SHA256=3c04ed3ca964ea2f6b2b5faf0dc4d31aec1cb1e8b4bcf63f402d295046b422b5
```

The CONTROL remains ineligible to win and remains exempt only from the PRIMARY package hard cap.

## 3. Exact previously evidenced runtime identities

```text
TRANSFORMERS_VERSION=4.57.6
TRANSFORMERS_SOURCE_REVISION=753d61104116eefc8ffc977327b441ee0c8d599f
TORCH_VERSION=2.11.0+cpu
PYTHON_RUNTIME_ENTRYPOINT=python3.12
PYTHON_RUNTIME_PATH=/usr/bin/python3.12
PYTHON_RUNTIME_VERSION=3.12.3
PYTHON_RUNTIME_SHA256=a92f0f95e883390c7256b2e441484aac06b1002dbe1d924141a77c8d82f96223
TRANSFORMERS_DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
TRANSFORMERS_INSTALLED_ENVIRONMENT_MANIFEST_SHA256=54517b34077e193c9bc019e8a2b232d3c9b6d6a85c4c6df13bcd38aa2b66c384
TRANSFORMERS_MODULE_SHA256=aa8cb54da488cf43ba37b9955bb6c0d84d2000db0306f6a5f1c20b6842482d04
TORCH_MODULE_SHA256=0387d8b811b289287479c8bfdf4e1dac3a71b246f938d82da1331cf2dc8bf001
```

Architecture-module evidence remains exact:

```text
GRANITE_CONFIG_MODULE_SHA256=535090da0bd3606c7be77517d2de4839f70b9658a40d4ec9ba98fb365397dc39
GRANITE_MODELING_MODULE_SHA256=920678d503bcb6795ba46c1b9579c28aad208a3ff0b73e7e02754e7cd9e3c19c
QWEN3_CONFIG_MODULE_SHA256=27863e9718fdbc899f2d0e567621e4d3d36d8dc500c1d54b49dba4242d08d2bd
QWEN3_MODELING_MODULE_SHA256=4b95c371fd26d40c69083dab36ac1eafd8cf82b415a0bb827275097c5ad2305b
```

These identities were established by static/import-only evidence. They are not empirical proof that either exact weight bundle can be loaded.

## 4. Loader policy

The adapter freezes the future loader policy without importing or invoking Transformers during qualification:

```text
MODEL_API=AutoModelForCausalLM.from_pretrained
TOKENIZER_API=AutoTokenizer.from_pretrained
LOCAL_FILES_ONLY=true
TRUST_REMOTE_CODE=false
REQUESTED_DEVICE=cpu
REQUESTED_DTYPE=auto
NETWORK_ALLOWED=false
```

The policy creates no permission to execute it before full preflight and exact-subject authorization.

## 5. Multiple-choice scoring contract

The six frozen scoring assets use:

```text
SCORING_METHOD=NORMALIZED_CONDITIONAL_LOG_LIKELIHOOD_ARGMAX
SEQUENCE_CONSTRUCTION=PROMPT_PLUS_SINGLE_ASCII_SPACE_PLUS_CHOICE
ADD_SPECIAL_TOKENS=true
COMMON_PREFIX=LONGEST_COMMON_TOKEN_ID_PREFIX_ACROSS_CHOICES
SCORED_REGION=CHOICE_DEPENDENT_CONTINUATION_FROM_COMMON_PREFIX
TOKEN_SCORE=AUTOREGRESSIVE_LOG_SOFTMAX_NEXT_TOKEN
NORMALIZATION=MEAN_LOG_PROBABILITY_PER_SCORED_TOKEN
SELECTION=MAX_NORMALIZED_LOG_PROBABILITY
TIE_POLICY=FIRST_IN_FROZEN_CHOICE_ORDER
CHOICE_ORDER=A,B,C,D
```

`src/commandmed/spec007/e004_transformers_adapter.py` includes only a pure normalization/argmax helper for this contract. It does not tokenize or call a model.

## 6. Resource-operation projection

The exact frozen resource asset remains:

```text
RESOURCE_ASSET_ID=SP007-RO-001-EVAL-RESOURCE-EFFICIENCY-V1
RESOURCE_ASSET_SHA256=a1ddea12b740886643fc396c62553b1ab954404090d16db499a57e933056a200
PROBE_COUNT=8
WARMUP_RUNS_PER_PROBE=1
MEASURED_RUNS_PER_PROBE=3
TOTAL_PROJECTED_INVOCATIONS=32
MAX_NEW_TOKENS=8
GENERATION_MODE=GREEDY_CAUSAL_LM
DO_SAMPLE=false
SEED=1
NETWORK_ALLOWED=false
```

Every measured run remains required to produce exactly:

```text
MODEL_ARTIFACT_BYTES
PEAK_RSS_BYTES
TIME_TO_FIRST_TOKEN_MS
DECODE_TOKENS_PER_SECOND
WALL_CLOCK_MS
```

This adapter only binds the invocation schedule and hashed frozen inputs. It produces no measurement and creates no threshold PASS.

## 7. Fail-closed boundary

The adapter manifest requires exact equality with:

- the frozen evaluation asset set;
- the frozen four-candidate artifact-bundle set;
- the exact Granite or CONTROL candidate identity;
- exact candidate bundle/model/tokenizer identities;
- exact Python/Transformers/Torch/runtime dependency identities;
- exact static architecture-module identities;
- exact loader, scoring, and resource-generation contracts;
- all six scoring operations and all 32 resource invocations;
- canonical self-hash;
- `execution_performed=false`;
- `runtime_format_compatibility_state=NEEDS_EMPIRICAL_MODEL_LOAD_EVIDENCE`;
- `authorized_spend_usd=0`.

Any candidate outside the exact Granite/CONTROL route fails closed.

## 8. Qualification restrictions

Qualification must use only offline deterministic Python control-plane tests.

```text
TRANSFORMERS_IMPORT_DURING_QUALIFICATION=PROHIBITED
TORCH_IMPORT_DURING_QUALIFICATION=PROHIBITED
MODEL_FILE_OPEN_DURING_QUALIFICATION=PROHIBITED
MODEL_LOAD_DURING_QUALIFICATION=PROHIBITED
INFERENCE_DURING_QUALIFICATION=PROHIBITED
SUBPROCESS_EXECUTION_DURING_QUALIFICATION=PROHIBITED
NETWORK_ACCESS_DURING_QUALIFICATION=PROHIBITED
SPEND_DURING_QUALIFICATION=PROHIBITED
```

The exact-head PR must pass the existing E004 control-plane compile, focused, Spec 007, full-repository, and diff-whitespace qualification gates.

Independent repository review remains optional by default under FD-007. No bot silence or unavailable service may be represented as review PASS.

## 9. Deliberate non-closure

Even after this adapter becomes canonical:

```text
EXACT_FOUR_CANDIDATE_TOP_LEVEL_RUNTIME_ARGV=INCOMPLETE
EXACT_EXECUTION_PLAN_SHA256_PER_CANDIDATE=INCOMPLETE
EMPIRICAL_RUNTIME_FORMAT_COMPATIBILITY=INCOMPLETE
EXACT_FUTURE_EXECUTION_ENVIRONMENT=INCOMPLETE
EXACT_RESOURCE_ACCESS_FINANCE_BINDINGS=INCOMPLETE
A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
E005_STATE=NOT_REACHED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The next dependency-safe unit is the four-candidate execution-plan/orchestrator identity that composes the canonical llama and Transformers adapter manifests into one exact top-level runtime entrypoint/argv per candidate without execution.
