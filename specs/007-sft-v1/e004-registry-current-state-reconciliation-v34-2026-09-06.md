# E004 Registry Current-State Reconciliation V34 — 2026-09-06

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Predecessor:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v33-2026-09-06.md`  
**Canonical base before this transition:** `12b0e4eec3fcedff81cbd1a9c1ecd10e8a0422d8`  
**Artifact class:** deterministic append-only current-state / dependency-frontier overlay  
**Authority effect:** only the separately bounded subject-metadata evidence authorization introduced in this transition  
**Model execution effect:** NONE  
**Tournament execution effect:** NONE  
**A15 effect:** NONE  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Consume V33's dependency-safe ordering without reopening the exhausted runtime-binding lane. This reconciliation distinguishes evidence that is already exact and reusable from evidence that still requires a separately bounded metadata-only run.

No model is loaded or executed by this record. No tournament, evaluation payload, conversion, A15 activation, training, credential use, protected-data access, procurement, payment, or spend is authorized.

## 2. Live repository hygiene at transition preparation

At preparation time:

```text
CANONICAL_MAIN_SHA=12b0e4eec3fcedff81cbd1a9c1ecd10e8a0422d8
CANONICAL_MAIN_TREE=acf33cc05c4d40510527bb7cbc4049aa3db1d7b1
MAIN_PROTECTED=false
REPOSITORY_RULESET_COUNT=0
STALE_PR_265=LOSED_SUPERSEDED_BY_PR_266
OPEN_PULL_REQUESTS_AFTER_STALE_CARRIER_CLOSE=0
```

PR #266 is the canonical V33 merge. The stale unmerged PR #265 has been closed as superseded and contributes no authority or evidence.

## 3. Existing exact candidate identity evidence reused

The exact frozen four-candidate set remains unchanged:

```text
QWEN06_SOURCE=Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
QWEN35_SOURCE=Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
GRANITE_SOURCE=ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
CONTROL_SOURCE=Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
CONTROL_WINNER_ELIGIBLE=NO
```

Exact candidate artifact evidence already available:

```text
QWEN06_GGUF_BYTE_INTEGRITY=PASS
QWEN35_GGUF_BYTE_INTEGRITY=PASS
GRANITE_SOURCE_BUNDLE_BYTE_INTEGRITY=PASS_ON_RUN_33183096268
CONTROL_SOURCE_BUNDLE_BYTE_INTEGRITY=PASS_ON_RUN_33183096268
```

Exact runtime/toolchain evidence already available from the consumed successor runtime lane:

```text
LLAMA_RUNTIME_ARCHIVE_IDENTITY=PASS_EVIDENCE_ONLY
LLAMA_RUNTIME_EXECUTABLE_IDENTITY=PASS_EVIDENCE_ONLY
LLAMA_STATIC_QWEN3_ROUTE_SUPPORT=PASS_EVIDENCE_ONLY
LLAMA_STATIC_QWEN35_ROUTE_SUPPORT=PASS_EVIDENCE_ONLY
TRANSFORMERS_DEPENDENCY_CLOSURE_IDENTITY=PASS_EVIDENCE_ONLY
TRANSFORMERS_PYTHON_RUNTIME_IDENTITY=PASS_EVIDENCE_ONLY
TRANSFORMERS_STATIC_QWEN3_ROUTE_SUPPORT=PASS_EVIDENCE_ONLY
TRANSFORMERS_STATIC_GRANITE_ROUTE_SUPPORT=PASS_EVIDENCE_ONLY
```

The consumed runtime lane is not rerunnable by this transition.

## 4. Exact tokenizer/config evidence already directly available

Canonical run `33183096268` recomputed the selected Granite and CONTROL non-weight source files. The following execution-relevant source-side identities are directly byte-bound already.

### Granite PRIMARY

```text
config.json=089690e22b9eafadcdd385afa5b6f3ea2446674ff5398c71df23be059d7c795d
merges.txt=b6fe424e334903f7fb84d3a106d9730455f4744b9fe3c21ee136d97a00e72502
special_tokens_map.json=c08676c49fd7969a3130f72be6d4bf34da66aa484a6e21dffe359893a1bd5f2e
tokenizer.json=e2bad66439538cb4d5a7580680932432ed9ece9d3b8577e675512bdf11599253
tokenizer_config.json=a5ec5daab12ba090a90f3dd169c8f9c275557013a87b9c1258dc7cb497a35c86
vocab.json=8af71076de8b0b626eed0f4c984faf0a7c062479164b2a31308a948524d4f69c
```

### Qwen3-4B CONTROL

```text
config.json=304b2545a258d35620f1d4bf46940c0471d9baa00715ff8e77f84c2fca5057c1
merges.txt=8831e4f1a044471340f7c0a83d7bd71306a5b867e95fd870f74d0c5308a904d5
tokenizer.json=c0382117ea329cdf097041132f6d735924b697924d6f6fc3945713e96ce87539
tokenizer_config.json=3c04ed3ca964ea2f6b2b5faf0dc4d31aec1cb1e8b4bcf63f402d295046b422b5
vocab.json=ca10d7e9fb3ed18575dd1e277a2579c16d108e32f27439684afa0e10b1440910
```

These hashes may be reused only with exact source-revision compatibility. They do not prove model-load compatibility.

## 5. Qwen GGUF metadata gap

For Qwen3-0.6B and Qwen3.5-0.8B, E001 binds exact source-side tokenizer/config paths at immutable revisions and E002 binds exact GGUF bytes. However the current commandMed evidence set does not yet directly bind the exact GGUF metadata/tensor-directory prefix to the expected architecture and tokenizer metadata without runtime loading.

Therefore:

```text
QWEN06_SOURCE_TOKENIZER_CONFIG_CONTENT_HASH_SET=INCOMPLETE
QWEN35_SOURCE_TOKENIZER_CONFIG_CONTENT_HASH_SET=INCOMPLETE
QWEN06_EXACT_GGUF_ARCHITECTURE_METADATA_BINDING=INCOMPLETE
QWEN35_EXACT_GGUF_ARCHITECTURE_METADATA_BINDING=INCOMPLETE
QWEN06_GGUF_TOKENIZER_METADATA_PRESENCE=INCOMPLETE
QWEN35_GGUF_TOKENIZER_METADATA_PRESENCE=INCOMPLETE
```

These are metadata-evidence gaps, not permission to load either model.

## 6. Minimum next evidence unit

The minimum dependency-safe separately bounded unit is a one-run metadata-only lane under existing E002 public-artifact access authority.

Authorization record:

`specs/007-sft-v1/e004-successor-subject-metadata-evidence-authorization-2026-09-06.md`

Workflow:

`.github/workflows/e004-successor-subject-metadata-evidence-v1.yml`

The lane may:

- reverify exact Qwen06/Qwen35 GGUF bytes;
- parse only GGUF header/KV/tensor-directory structures and stop before tensor payload;
- bind Qwen06/Qwen35 source config/tokenizer file hashes from exact frozen revisions;
- reverify Granite/CONTROL non-weight hashes against prior canonical evidence;
- emit exact runner/network/credential/no-spend evidence.

It may not load or execute a model.

## 7. Authority disposition

```text
E004_SUCCESSOR_RUNTIME_BINDING_EVIDENCE_AUTHORITY=CONSUMED_EXACTLY_ONCE
RUNTIME_BINDING_EVIDENCE_RERUN_AUTHORIZED_NOW=NO
E004_SUCCESSOR_SUBJECT_METADATA_EVIDENCE_AUTHORITY=AUTHORIZED_BOUNDED
MAX_AUTHORIZED_SUBJECT_METADATA_EVIDENCE_RUNS=1
AUTHORIZED_SUBJECT_METADATA_EVIDENCE_RUNS_EXECUTED=0
AUTHORIZED_SUBJECT_METADATA_EVIDENCE_RUNS_REMAINING=1
SUBJECT_METADATA_RERUN_AUTHORITY=NONE_BY_DEFAULT
```

## 8. Preflight remains fail closed

The new bounded evidence unit does not make the successor executable.

```text
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=INCOMPLETE
EXACT_FINAL_MODEL_EXECUTION_ARGV=INCOMPLETE
EXACT_EXECUTION_PLAN_SHA256=INCOMPLETE
EXACT_FUTURE_MODEL_EXECUTION_ENVIRONMENT=INCOMPLETE
EXACT_RESOURCE_BINDING=INCOMPLETE
EXACT_ACCESS_BINDING_FOR_EXECUTION_SUBJECT=INCOMPLETE
ZERO_INCREMENTAL_SPEND_TOURNAMENT_RESOURCE_BINDING=INCOMPLETE
A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
MODEL_EXECUTION_NOW=NOT_AUTHORIZED_BY_GATE_STATE
TOURNAMENT_EXECUTION_NOW=NOT_AUTHORIZED_BY_GATE_STATE
```

## 9. Task-ledger interpretation

```text
E004_TASK_CHECKBOX=REMAINS_INCOMPLETE
E004_RUNTIME_BINDING_EVIDENCE_SUBUNIT=COMPLETE_AUTHORITY_CONSUMED
E004_SUBJECT_METADATA_EVIDENCE_SUBUNIT=AUTHORIZED_NOT_YET_EXECUTED
E004_EXACT_SUBJECT_BINDING_SUBUNIT=INCOMPLETE
E004_RESOURCE_ACCESS_FINANCE_SUBUNIT=INCOMPLETE
E004_A1_A14_SNAPSHOT_SUBUNIT=INCOMPLETE
E004_A15_SUBUNIT=NOT_REACHED_AS_SOLE_BLOCKER
E004_MODEL_EXECUTION_SUBUNIT=NOT_STARTED_NOT_AUTHORIZED_BY_GATE_STATE
E005_STATE=NOT_REACHED
```

No task checkbox is closed by this record.

## 10. Next dependency-safe frontier

1. qualify and canonicalize the inert metadata-only workflow and its bounded authority;
2. execute exactly one marker-push metadata evidence run after canonical merge;
3. capture only directly observed metadata/config/tokenizer evidence and mark the one-run authority consumed;
4. recompute exact subject, execution-plan, resource/access/finance, and A1-A14 prerequisites;
5. do not prepare A15 until every earlier applicable prerequisite is genuinely PASS;
6. do not execute any model until the exact canonical pre-execution subject hash is non-`NONE` and the hardened request builder accepts that exact subject.

## 11. Current disposition

```text
CURRENT_GLOBAL_FRONTIER=specs/007-sft-v1/e004-registry-current-state-reconciliation-v34-2026-09-06.md
SUCCESSOR_PREFLIGHT_DISPOSITION=BLOCKED
SUCCESSOR_PASS_PREFLIGHT=NO
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
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
