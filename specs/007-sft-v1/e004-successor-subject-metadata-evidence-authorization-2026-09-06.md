# E004 Successor Subject-Metadata Evidence Authorization — 2026-09-06

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Predecessor frontier:** `specs/007-sft-v1/e004-registry-current-state-reconciliation-v33-2026-09-06.md`  
**Canonical base:** `12b0e4eec3fcedff81cbd1a9c1ecd10e8a0422d8`  
**Decision owner:** Founder  
**Decision class:** `E004_SUCCESSOR_SUBJECT_METADATA_EVIDENCE_AUTHORIZATION`  
**Decision state:** `AUTHORIZED_BOUNDED`  
**Model execution authority effect:** NONE  
**Tournament execution authority effect:** NONE  
**A15 effect:** NONE  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Founder direction and dependency-safe interpretation

At the V33 frontier the canonical next-state rule requires existing E001/E002/source-bundle evidence to be consumed first, followed by the minimum separately bounded evidence needed to close exact per-candidate bundle/tokenizer/config metadata without executing a model.

The Founder directed:

```text
FOUNDER_DIRECTION=go ahead, follow the plan in repo, do not stop until finish the projects
```

Consistent with repository bounded-authority precedent, that direction is interpreted only as authorization of this first dependency-safe successor unit. It does not authorize model load, inference, tournament execution, conversion, A15 activation, training, credentialed access, protected-data access, procurement, payment, or spend.

```text
E004_SUCCESSOR_SUBJECT_METADATA_EVIDENCE_AUTHORITY=AUTHORIZED_BOUNDED
MAX_AUTHORIZED_SUBJECT_METADATA_EVIDENCE_RUNS=1
RERUN_AUTHORITY=NONE_BY_DEFAULT
MODEL_EXECUTION_AUTHORITY_EXPANSION=NONE
TOURNAMENT_EXECUTION_AUTHORITY_EXPANSION=NONE
A15_ACTIVATION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 2. Inherited access authority

Canonical E002 already authorizes non-executing access for the exact frozen public candidate artifacts, including static container metadata inspection and exact tokenizer/config acquisition, while prohibiting model load and execution.

This unit relies only on that existing access authority and does not broaden candidate membership or artifact allowlists.

### Exact GGUF artifacts admitted for metadata-only inspection

```text
QWEN06_REPOSITORY=Antigma/Qwen3-0.6B-Base-GGUF
QWEN06_REVISION=f457544766bcdc72afd3514439eb3d422d4434dc
QWEN06_FILENAME=qwen3-0.6b-base-q4_k_m.gguf
QWEN06_BYTES=396704512
QWEN06_SHA256=218d3f063193b40008d4e63d90cf83e7dc6d33a8c6c1c647589f868a8fc74492

QWEN35_REPOSITORY=ggml-org/Qwen3.5-0.8B-Base-GGUF
QWEN35_REVISION=1bd44f68963429437d08bc12f465716eb31ba6e5
QWEN35_FILENAME=Qwen3.5-0.8B-Base-Q4_0.gguf
QWEN35_BYTES=563035840
QWEN35_SHA256=0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d
```

### Exact frozen source revisions admitted for non-weight metadata acquisition

```text
QWEN06_SOURCE=Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
QWEN35_SOURCE=Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
GRANITE_SOURCE=ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
CONTROL_SOURCE=Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
```

Only explicitly enumerated non-weight config/tokenizer files at those immutable revisions may be acquired by this lane.

## 3. Exact objective

The one authorized run may establish only:

1. exact byte/SHA-256 re-verification of the two E002-allowlisted GGUF files;
2. static GGUF header/KV/tensor-directory parsing without reading tensor payload bytes;
3. exact `general.architecture` and tokenizer-metadata presence for each GGUF;
4. deterministic SHA-256 identity of the parsed GGUF metadata-and-tensor-directory byte prefix;
5. exact content SHA-256 identities for the frozen non-weight `config.json` / tokenizer files needed by the four candidate provenance bindings;
6. equality of Granite and Qwen3-4B non-weight hashes with already-canonical run `33183096268` evidence;
7. fresh Qwen3-0.6B and Qwen3.5 source non-weight hashes at their immutable frozen revisions;
8. exact runner/image/network/credential/no-spend evidence for this metadata lane.

The parser must stop after the GGUF tensor directory and must not seek into or read tensor payload bytes.

## 4. Permitted actions

A review-first workflow may be prepared and, only after canonical merge, executed once on a standard public `ubuntu-24.04` GitHub-hosted runner to:

- fetch the exact two allowlisted GGUF artifacts over public HTTPS without credentials;
- require their exact canonical byte counts and SHA-256 values before inspection;
- parse only container metadata and tensor-directory structures using repository-authored Python standard-library code embedded in the workflow;
- fetch only the exact enumerated non-weight config/tokenizer files from the four frozen source revisions;
- hash those non-weight files and compare Granite/CONTROL values to prior canonical evidence where exact hashes already exist;
- emit evidence only to retained GitHub Actions logs;
- delete nothing persistently because the hosted runner is ephemeral and no upload/cache action is permitted.

## 5. Explicit prohibitions

```text
MODEL_OBJECT_CONSTRUCTION=PROHIBITED
MODEL_RUNTIME_LOAD=PROHIBITED
MODEL_INFERENCE=PROHIBITED
GENERATION=PROHIBITED
TENSOR_PAYLOAD_READ_BY_GGUF_PARSER=PROHIBITED
TRANSFORMERS_FROM_PRETRAINED=PROHIBITED
TRUST_REMOTE_CODE=PROHIBITED
BENCHMARK_OR_EVALUATION_PAYLOAD_ACCESS=PROHIBITED
TOURNAMENT_EXECUTION=PROHIBITED
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
ARTIFACT_OR_CACHE_UPLOAD=PROHIBITED
PAID_OR_LARGER_RUNNER=PROHIBITED
PROCUREMENT=PROHIBITED
PAYMENT=PROHIBITED
SPEND_USD=0
```

Opening the two exact E002-allowlisted GGUF files for static metadata parsing is authorized by existing E002 static-container-metadata authority. It is not model load and must not be represented as runtime compatibility PASS.

## 6. Qualification and one-run boundary

Before the evidence workflow is executable:

```text
REVIEW_FIRST=REQUIRED
PULL_REQUEST_METADATA_EVIDENCE_JOB=INERT
EXACT_HEAD_STATIC_QUALIFICATION=REQUIRED
BOUNDED_AUTHORITY_BIND=REQUIRED
DIFF_WHITESPACE=PASS_REQUIRED
EXPECTED_HEAD_GUARDED_MERGE=REQUIRED
```

After canonical merge exactly one marker-push run may be created.

```text
MAX_AUTHORIZED_SUBJECT_METADATA_EVIDENCE_RUNS=1
RERUN_AUTHORITY=NONE_BY_DEFAULT
FAILED_RUN_AUTOMATIC_RETRY_AUTHORITY=NONE
```

Ordinary transport retries inside that one run are permitted only for the same exact immutable public bytes.

## 7. Effect of successful evidence

A successful run may promote only directly observed bundle/tokenizer/config metadata fields. It may not infer empirical model-load compatibility or future execution-resource identity.

The following remain separately gated even after a successful metadata run unless later exact evidence closes them:

```text
EXACT_PER_CANDIDATE_MODEL_LOAD_COMPATIBILITY=INCOMPLETE
EXACT_FINAL_MODEL_EXECUTION_ARGV=INCOMPLETE
EXACT_FUTURE_MODEL_EXECUTION_ENVIRONMENT=INCOMPLETE
EXACT_RESOURCE_BINDING=INCOMPLETE
EXACT_ACCESS_BINDING_FOR_EXECUTION_SUBJECT=INCOMPLETE
ZERO_INCREMENTAL_SPEND_TOURNAMENT_RESOURCE_BINDING=INCOMPLETE
A1_A14_APPLICABLE_PASS_SNAPSHOT=ABSENT
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
```

No model may execute under this authorization.