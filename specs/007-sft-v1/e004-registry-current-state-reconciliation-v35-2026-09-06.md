# E004 Registry Current-State Reconciliation V35 — 2026-09-06

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Predecessor:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v34-2026-09-06.md`
**Canonical base before result capture:** `b9f8b536b15017f49d72dc6d8da30a2a740ca9b3`
**Evidence result:** `specs/007-sft-v1/e004-successor-subject-metadata-evidence-result-2026-09-06.md`
**Evidence run:** `34046672641`
**Evidence job:** `101522835683`
**Evidence head:** `0148a897543b66b230cc2b4a9cd5d6f17bdb8223`
**Artifact class:** deterministic append-only current-state / dependency-frontier overlay
**Authority effect:** consume the V34 one-run metadata authority; no new model/tournament execution authority
**Current authorized spend:** USD 0

## 1. Purpose

Consume the successful one-run subject-metadata evidence lane and recompute the exact E004 successor frontier without promoting static evidence into empirical runtime compatibility.

```text
E004_SUCCESSOR_SUBJECT_METADATA_EVIDENCE_AUTHORITY=CONSUMED_EXACTLY_ONCE
AUTHORIZED_SUBJECT_METADATA_EVIDENCE_RUNS_EXECUTED=1
AUTHORIZED_SUBJECT_METADATA_EVIDENCE_RUNS_REMAINING=0
SUBJECT_METADATA_RERUN_AUTHORITY=NONE
```

No model load, inference, tournament execution, conversion, A15 activation, training, credential use, protected-data access, procurement, payment, or spend is authorized by this reconciliation.

## 2. Newly closed evidence fields

The exact Qwen GGUF identities remain unchanged and were reverified byte-for-byte:

```text
QWEN06_MODEL_ARTIFACT_SHA256=218d3f063193b40008d4e63d90cf83e7dc6d33a8c6c1c647589f868a8fc74492
QWEN06_MODEL_ARTIFACT_BYTES=396704512
QWEN35_MODEL_ARTIFACT_SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
QWEN35_MODEL_ARTIFACT_BYTES=563035840
```

Static container metadata now directly binds:

```text
QWEN06_GENERAL_ARCHITECTURE=qwen3
QWEN06_TOKENIZER_GGML_MODEL=gpt2
QWEN06_TOKENIZER_GGML_PRE=qwen2
QWEN06_GGUF_TOKENIZER_METADATA_KEY_COUNT=10
QWEN06_METADATA_AND_TENSOR_DIRECTORY_SHA256=f47aa4fd38e69f581b8aacb81c31ca38e4c2f2f6861288dfbe19b3cdd6f5ed07

QWEN35_GENERAL_ARCHITECTURE=qwen35
QWEN35_TOKENIZER_GGML_MODEL=gpt2
QWEN35_TOKENIZER_GGML_PRE=qwen35
QWEN35_GGUF_TOKENIZER_METADATA_KEY_COUNT=9
QWEN35_METADATA_AND_TENSOR_DIRECTORY_SHA256=0f22d5983b378cb108453b822e47b2fbfd23e2593a175a2e9ab880692fdd8e7a

GGUF_TENSOR_PAYLOAD_BYTES_READ=0
```

The exact source-side `tokenizer_config.json` identities required by the current execution-subject schema are now directly byte-bound for all four frozen candidates:

```text
QWEN06_TOKENIZER_CONFIG_SHA256=3c04ed3ca964ea2f6b2b5faf0dc4d31aec1cb1e8b4bcf63f402d295046b422b5
QWEN35_TOKENIZER_CONFIG_SHA256=e611fbccc7c29ef3b1cafb1cb7ea548d189968632901d678fd62be68c47885de
GRANITE_TOKENIZER_CONFIG_SHA256=a5ec5daab12ba090a90f3dd169c8f9c275557013a87b9c1258dc7cb497a35c86
CONTROL_TOKENIZER_CONFIG_SHA256=3c04ed3ca964ea2f6b2b5faf0dc4d31aec1cb1e8b4bcf63f402d295046b422b5
```

The full 21-file non-weight source metadata manifest is:

```text
SOURCE_METADATA_MANIFEST_SHA256=5554df17f7ff21b8ebd0d063e090b9923dccf29076e9c47717162f036c4e99ce
SOURCE_METADATA_FILE_COUNT=21
```

## 3. Runtime evidence composition remains bounded

V33 already established exact runtime/toolchain evidence for the candidate architecture families. The new metadata evidence composes with, but does not widen, those observations.

```text
LLAMA_RUNTIME_ARCHIVE_IDENTITY=PASS_EVIDENCE_ONLY
LLAMA_RUNTIME_EXECUTABLE_IDENTITY=PASS_EVIDENCE_ONLY
LLAMA_STATIC_QWEN3_ROUTE_SUPPORT=PASS_EVIDENCE_ONLY
LLAMA_STATIC_QWEN35_ROUTE_SUPPORT=PASS_EVIDENCE_ONLY
TRANSFORMERS_DEPENDENCY_CLOSURE_IDENTITY=PASS_EVIDENCE_ONLY
TRANSFORMERS_PYTHON_RUNTIME_IDENTITY=PASS_EVIDENCE_ONLY
TRANSFORMERS_STATIC_QWEN3_ROUTE_SUPPORT=PASS_EVIDENCE_ONLY
TRANSFORMERS_STATIC_GRANITE_ROUTE_SUPPORT=PASS_EVIDENCE_ONLY
QWEN06_GGUF_STATIC_ARCHITECTURE_BINDING=PASS_EVIDENCE_ONLY
QWEN35_GGUF_STATIC_ARCHITECTURE_BINDING=PASS_EVIDENCE_ONLY
```

Static support plus static artifact metadata is not equivalent to empirical model-load compatibility. Therefore:

```text
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=INCOMPLETE
RUNTIME_FORMAT_COMPATIBILITY_STATE_FOR_LIVE_SUBJECT=NOT_YET_PASS
```

## 4. Complete execution-bundle gate remains fail closed

The canonical validator requires exact `complete_bundle_sha256`, `complete_bundle_bytes`, runtime artifact/executable identity, build toolchain identity, execution plan identity, tokenizer/config identity, and exact argv for each of the four candidates.

The new evidence directly closes only some components of those bindings. It does not define or prove a canonical complete executable bundle for all four candidates.

```text
LIVE_FOUR_CANDIDATE_COMPLETE_BUNDLE_BINDINGS=INCOMPLETE
LIVE_FOUR_CANDIDATE_RUNTIME_BINDINGS=INCOMPLETE
EXACT_COMPLETE_BUNDLE_SHA256_PER_CANDIDATE=INCOMPLETE
EXACT_COMPLETE_BUNDLE_BYTES_PER_CANDIDATE=INCOMPLETE
EXACT_EXECUTION_PLAN_SHA256_PER_CANDIDATE=INCOMPLETE
EXACT_RUNTIME_ARGV_PER_CANDIDATE=INCOMPLETE
```

No missing value may be replaced by `NEEDS_EVIDENCE`, a placeholder hash, provider metadata inference, or a synthetic favorable value in a live subject.

## 5. Environment, resource, access, and finance remain fail closed

The execution-subject validator and canonical execution-time policy still require exact identities for the live execution environment and resource/access boundary.

```text
EXACT_FUTURE_MODEL_EXECUTION_ENVIRONMENT=INCOMPLETE
EXACT_ENVIRONMENT_MANIFEST_SHA256=INCOMPLETE
EXACT_COMPUTE_RESOURCE_IDENTITY=INCOMPLETE
RESOURCE_AUTHORIZATION_BASIS=INCOMPLETE
EXPECTED_CPU_RAM_DISK_ENVELOPE=INCOMPLETE
EXPECTED_MAX_WALLCLOCK=INCOMPLETE
EXACT_ACCESS_BINDING_FOR_EXECUTION_SUBJECT=INCOMPLETE
EXACT_CREDENTIAL_STATE_BINDING=INCOMPLETE
NETWORK_DURING_EXECUTION_BINDING=INCOMPLETE
ZERO_INCREMENTAL_SPEND_TOURNAMENT_RESOURCE_BINDING=INCOMPLETE
CURRENT_AUTHORIZED_SPEND_USD=0
```

A free or public path is not promoted to exact resource/access/finance PASS without a canonical exact-subject binding.

## 6. A1-A14 and A15 remain ordered prerequisites

```text
A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
A15_IS_SOLE_REMAINING_BLOCKER=NO
GENERIC_GO_AHEAD_COUNTS_AS_A15_ACTIVATION=NO
```

A15 remains later than the unresolved non-A15 prerequisites and must not be prepared as if it were the only blocker.

## 7. Exact-subject lock remains closed

The current canonical execution code intentionally holds:

```text
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
```

The new metadata evidence does not justify changing that constant.

```text
STRUCTURALLY_COMPLETE_SYNTHETIC_SUBJECT_CAN_BUILD_LIVE_REQUEST=NO
LIVE_SP007_PREEXECUTION_SUBJECT=ABSENT
SUCCESSOR_PASS_PREFLIGHT=NO
MODEL_EXECUTION_NOW=NOT_AUTHORIZED_BY_GATE_STATE
TOURNAMENT_EXECUTION_NOW=NOT_AUTHORIZED_BY_GATE_STATE
```

## 8. Task-ledger interpretation

```text
E004_TASK_CHECKBOX=REMAINS_INCOMPLETE
E004_EVALUATION_ASSET_QUALIFICATION_SUBUNIT=COMPLETE
E004_RUNTIME_BINDING_EVIDENCE_SUBUNIT=COMPLETE_AUTHORITY_CONSUMED
E004_SUBJECT_METADATA_EVIDENCE_SUBUNIT=COMPLETE_AUTHORITY_CONSUMED
E004_EXACT_SUBJECT_BINDING_SUBUNIT=INCOMPLETE
E004_RESOURCE_ACCESS_FINANCE_SUBUNIT=INCOMPLETE
E004_A1_A14_SNAPSHOT_SUBUNIT=INCOMPLETE
E004_A15_SUBUNIT=NOT_REACHED_AS_SOLE_BLOCKER
E004_MODEL_EXECUTION_SUBUNIT=NOT_STARTED_NOT_AUTHORIZED_BY_GATE_STATE
E004_TOURNAMENT_EXECUTION_SUBUNIT=NOT_STARTED_NOT_AUTHORIZED_BY_GATE_STATE
E005_STATE=NOT_REACHED
```

No checkbox is closed merely because two evidence lanes succeeded.

## 9. Next dependency-safe frontier

The next dependency-safe work must remain non-executing until the exact subject can truthfully satisfy its validator.

Order:

1. define and bind a deterministic per-candidate complete executable-bundle identity from exact already-authorized candidate/runtime/tokenizer/config components, without loading a model;
2. define exact per-candidate runtime argv and deterministic execution-plan identities against the already-bound runtime families, still without execution;
3. separately close any compatibility fact that cannot be established by exact static evidence; do not infer empirical model-load PASS;
4. bind the exact future execution environment, compute/resource, network, access/credential, retention, wallclock, and zero-incremental-spend identities;
5. construct and qualify the applicable A1-A14 snapshot only from genuine evidence;
6. only after all earlier applicable prerequisites pass may a separate explicit A15 decision surface be prepared;
7. only after A15 and the full exact subject pass may the repository bind a non-`NONE` `CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256` and permit the first model call.

This ordering creates no implicit authority to execute any missing step.

## 10. Current disposition

```text
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v35-2026-09-06.md
SUCCESSOR_PREFLIGHT_DISPOSITION=BLOCKED
SUCCESSOR_PASS_PREFLIGHT=NO
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
MODEL_RUNTIME_LOAD_PERFORMED=NO
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
