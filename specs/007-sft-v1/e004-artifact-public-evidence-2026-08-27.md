# E004 Frozen Artifact Public-Evidence Packet — 2026-08-27

**Spec:** 007 SFT V1
**Lifecycle:** E004 prerequisite research only
**Canonical research base:** `0023c4fc0fb2168b8994f9cae08663e84752a6d0`
**Purpose:** read-only public-metadata research for the next frozen-artifact authority reconciliation decision
**Authority effect:** NONE

This packet does not expand E002, does not authorize acquisition of any preconverted artifact not already enumerated by E002, and does not authorize conversion, model loading, benchmark access/execution, device execution, contamination assessment, training, credentials, Private Gold, PHI, provider generation, or spend.

```text
ARTIFACT_RESEARCH_ONLY=YES
MODEL_WEIGHT_ACCESS_AUTHORITY=UNCHANGED
PRECONVERTED_ARTIFACT_ALLOWLIST=UNCHANGED
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=UNCHANGED_E003_CONDITIONAL_ONLY
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
E004_EXECUTION_OCCURRED=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
```

## 1. Frozen identities and current allowlist boundary

The E001 manifest remains immutable and binds these unresolved artifact-reconciliation subjects:

### PRIMARY Granite

```text
CANDIDATE_ID=ibm-granite/granite-4.0-350m-base
FROZEN_UPSTREAM_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
ROLE=PRIMARY
```

### CONTROL Qwen3 4B Base

```text
CANDIDATE_ID=Qwen/Qwen3-4B-Base
FROZEN_UPSTREAM_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
ROLE=CONTROL
WINNER_ELIGIBLE=NO
PURPOSE=SCALE_QUALITY_OPPORTUNITY_COST
```

E002 currently authorizes only two preconverted artifacts: the exact Qwen3-0.6B-Base Q4_K_M feasibility artifact and the exact Qwen3.5-0.8B-Base Q4_0 artifact. Granite and CONTROL preconverted bytes remain outside the E002 deterministic allowlist.

No repository adjacency, filename similarity, public availability, or family relationship is sufficient to expand that allowlist.

## 2. Granite official GGUF evidence

### 2.1 Public artifact identity

IBM publishes a first-party GGUF repository for the exact base-model family:

```text
GGUF_REPOSITORY=ibm-granite/granite-4.0-350m-base-GGUF
GGUF_REPOSITORY_OWNER=ibm-granite
GGUF_LICENSE=apache-2.0
GGUF_DECLARED_BASE_MODEL=ibm-granite/granite-4.0-350m-base
GGUF_FILENAME=granite-4.0-350m-base-Q4_K_M.gguf
GGUF_FILE_COMMIT=61ff4f9133240330c7b06009eaa173999b367cd9
GGUF_SHA256=2c22ed74d6c11791eb017886e1356ae11a6b8207b1ab2c1dfee047370110389a
GGUF_XET_HASH=3e8f4874960be082b8605f5a55e0c1ca1654b2cba4ac102b9188429cdb3189c8
GGUF_PUBLIC_DISPLAY_SIZE=237 MB
GGUF_EXACT_BYTES=NEEDS_EVIDENCE
```

The Hugging Face file page exposes the SHA-256 and Xet hash directly and identifies the file as `Q4_K_M`. The repository card declares the base model as `ibm-granite/granite-4.0-350m-base`.

### 2.2 IBM conversion-pipeline evidence

The file history identifies IBM's public conversion workflow:

```text
CONVERSION_WORKFLOW_REPOSITORY=IBM/gguf
CONVERSION_WORKFLOW_PATH=.github/workflows/granite-4.0-release-ibm-granite.yml
CONVERSION_WORKFLOW_TAG=v4.0-language-refresh-20260423-01
CONVERSION_SOURCE_REPOSITORY_ENTRY=ibm-granite/granite-4.0-350m-base
CONVERSION_TARGET_QUANTIZATION_ENTRY=Q4_K_M
CONVERSION_LLAMA_CPP_BUILD_TAG=b8100
```

The tagged workflow is strong first-party evidence that IBM's pipeline includes this exact source repository and Q4_K_M output class. However, the workflow does not pin an immutable Hugging Face source revision for each input repository.

Therefore this packet must not infer that the published GGUF was converted specifically from E001's frozen upstream revision `a50b46cef21c8a86b15f0496cb794487a78a910b` merely because the repository identity matches.

```text
GRANITE_REPOSITORY_LINEAGE_MATCH=PASS
GRANITE_FIRST_PARTY_CONVERSION_PIPELINE=PASS
GRANITE_EXACT_ARTIFACT_SHA256=PASS
GRANITE_EXACT_ARTIFACT_COMMIT=PASS
GRANITE_EXACT_ARTIFACT_XET_HASH=PASS
GRANITE_EXACT_ARTIFACT_BYTES=NEEDS_EVIDENCE
GRANITE_EXACT_FROZEN_SOURCE_REVISION_USED_BY_CONVERSION=NEEDS_EVIDENCE
GRANITE_E002_ALLOWLIST_ELIGIBILITY=INCOMPLETE
```

## 3. CONTROL Qwen3-4B-Base evidence

### 3.1 Frozen upstream source remains exact and public

The frozen CONTROL source repository is still publicly inspectable at the E001 revision:

```text
SOURCE_REPOSITORY=Qwen/Qwen3-4B-Base
SOURCE_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
SOURCE_LICENSE=apache-2.0
SOURCE_MODEL_TYPE=qwen3
SOURCE_CONTEXT_LENGTH=32768
SOURCE_WEIGHT_SET=3 safetensors shards
SOURCE_REPOSITORY_DISPLAY_SIZE=8.06 GB
```

This is the BASE/PRETRAINED checkpoint. It must not be substituted with `Qwen/Qwen3-4B`, which is the post-trained model.

### 3.2 Official post-trained GGUF is not an exact-base substitute

Qwen publishes `Qwen/Qwen3-4B-GGUF`, but its own model card describes Qwen3-4B as a model with both pretraining and post-training and links the post-trained `Qwen/Qwen3-4B` lineage. That artifact is therefore not admissible as the exact frozen `Qwen/Qwen3-4B-Base` CONTROL runtime artifact.

```text
QWEN_OFFICIAL_QWEN3_4B_GGUF_EXACT_BASE_MATCH=NO
SUBSTITUTION_ALLOWED=NO
```

### 3.3 Strong community exact-base candidate evidence

A public community repository explicitly identifies `Qwen/Qwen3-4B-Base` as its original model and publishes a Q4_K_M file:

```text
GGUF_REPOSITORY=Antigma/Qwen3-4B-Base-GGUF
GGUF_DECLARED_ORIGINAL_MODEL=Qwen/Qwen3-4B-Base
GGUF_DECLARED_QUANTIZER=llama.cpp b5215
GGUF_FILENAME=qwen3-4b-base-q4_k_m.gguf
GGUF_FILE_COMMIT=ab03cef12ef7fac77574d54a28331026c21257a0
GGUF_SHA256=a91798f5f24b6ef5e9309fa97cb82be19c930f5b1e359e5d1af80d20e24b3f68
GGUF_XET_HASH=3701df64f3275dbbe1736bb655927456b4d7f452b5242e40a1af5cceed23e984
GGUF_PUBLIC_DISPLAY_SIZE=2.5 GB
GGUF_EXACT_BYTES=NEEDS_EVIDENCE
```

The repository-level lineage points to the correct BASE checkpoint family, not the post-trained model. The file has a stable commit, SHA-256 and Xet identity. However, the public metadata inspected in this pass does not bind the conversion input to E001's exact frozen source revision `906bfd4b4dc7f14ee4320094d8b41684abff8539`.

A repository-level source statement is not equivalent to an immutable source-revision attestation.

```text
CONTROL_EXACT_BASE_FAMILY_MATCH=PASS
CONTROL_ARTIFACT_SHA256=PASS
CONTROL_ARTIFACT_COMMIT=PASS
CONTROL_ARTIFACT_XET_HASH=PASS
CONTROL_EXACT_ARTIFACT_BYTES=NEEDS_EVIDENCE
CONTROL_EXACT_FROZEN_SOURCE_REVISION_USED_BY_CONVERSION=NEEDS_EVIDENCE
CONTROL_FIRST_PARTY_QWEN_ARTIFACT=NO
CONTROL_E002_ALLOWLIST_ELIGIBILITY=INCOMPLETE
```

Other public repositories also advertise quantizations of `Qwen/Qwen3-4B-Base`; their existence does not improve the authority state unless one can satisfy the same exact source-revision, file, byte-count, hash and rights/provenance requirements.

## 4. Deterministic decision matrix

| Subject | Exact frozen family | Exact artifact file | Exact artifact commit | SHA-256 | Xet identity | Exact bytes | Exact frozen source revision attested | First-party conversion | Current result |
|---|---|---|---|---|---|---|---|---|---|
| Granite Q4_K_M | PASS | PASS | PASS | PASS | PASS | NEEDS_EVIDENCE | NEEDS_EVIDENCE | PASS | `INCOMPLETE_NO_ALLOWLIST_EXPANSION` |
| Qwen3-4B-Base CONTROL Q4_K_M candidate | PASS | PASS | PASS | PASS | PASS | NEEDS_EVIDENCE | NEEDS_EVIDENCE | NO | `INCOMPLETE_NO_ALLOWLIST_EXPANSION` |
| Official Qwen3-4B GGUF | FAIL exact-base identity | N/A | N/A | N/A | N/A | N/A | N/A | PASS | `REJECT_AS_CONTROL_SUBSTITUTE` |

No row satisfies the complete deterministic E002 preconverted-artifact binding standard in this packet.

## 5. Artifact-authority reconciliation result

The evidence supports a stronger description of the available artifacts, but not an authority expansion.

```text
FROZEN_ARTIFACT_AUTHORITY_RECONCILIATION=EVIDENCE_INCOMPLETE_NO_EXPANSION
E002_PRECONVERTED_ALLOWLIST_COUNT=2
NEW_PRECONVERTED_ALLOWLIST_ENTRIES=0
GRANITE_PRECONVERTED_ACQUISITION_AUTHORITY=NONE_BEYOND_EXISTING_E002
CONTROL_PRECONVERTED_ACQUISITION_AUTHORITY=NONE_BEYOND_EXISTING_E002
MODEL_CONVERSION_AUTHORITY=NONE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
```

This is not a NO-GO on either candidate. It is a fail-closed result on artifact identity completeness.

## 6. Remaining evidence required before any later artifact authority decision

### Granite

1. Obtain an exact byte count from public read-only artifact metadata without downloading model payload bytes.
2. Obtain first-party evidence that the published Q4_K_M conversion consumed the exact frozen upstream source revision `a50b46cef21c8a86b15f0496cb794487a78a910b`, or otherwise prove byte-equivalent source identity under an accepted canonical method.
3. If exact source-revision lineage cannot be established, do not infer it; a separately authorized bounded conversion path from the frozen E001 source would remain a different future decision.

### CONTROL

1. Obtain an exact byte count from public read-only metadata.
2. Obtain an immutable conversion-source revision attestation proving the exact input was `Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539`.
3. Prefer a first-party or independently reproducible provenance route if available; community publication alone is not sufficient to infer exact frozen-revision lineage.
4. Do not substitute the official post-trained Qwen3-4B GGUF.

## 7. Sources inspected

Public read-only sources inspected for this packet:

- `https://huggingface.co/ibm-granite/granite-4.0-350m-base-GGUF`
- `https://huggingface.co/ibm-granite/granite-4.0-350m-base-GGUF/blob/main/granite-4.0-350m-base-Q4_K_M.gguf`
- `https://github.com/IBM/gguf/blob/v4.0-language-refresh-20260423-01/.github/workflows/granite-4.0-release-ibm-granite.yml`
- `https://huggingface.co/Qwen/Qwen3-4B-Base/tree/906bfd4b4dc7f14ee4320094d8b41684abff8539`
- `https://huggingface.co/Qwen/Qwen3-4B-GGUF`
- `https://huggingface.co/Antigma/Qwen3-4B-Base-GGUF`
- `https://huggingface.co/Antigma/Qwen3-4B-Base-GGUF/blob/main/qwen3-4b-base-q4_k_m.gguf`

Repository authority sources:

- `specs/007-sft-v1/e001-proposed-candidate-manifest.json`
- `specs/007-sft-v1/e002-model-access-authorization-2026-08-27.md`
- `specs/007-sft-v1/e003-live-tournament-execution-authorization-2026-08-27.md`
- `specs/007-sft-v1/e004-corrective-maintenance-closeout-2026-08-27.md`

## 8. Next state

```text
NEXT_ACTION=CONTINUE_READ_ONLY_ARTIFACT_METADATA_RESOLUTION
NEXT_MUTATING_AUTHORITY_DECISION=NOT_READY
NEXT_EXECUTION_AUTHORITY=NONE_CREATED
```

The repository should continue read-only public metadata research. No download of the newly researched preconverted artifacts, conversion, model execution, benchmark payload access, contamination assessment, or training is authorized by this packet.
