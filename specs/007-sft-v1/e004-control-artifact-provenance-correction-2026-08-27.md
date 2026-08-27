# E004 CONTROL Artifact-Provenance Correction — 2026-08-27

**Spec:** 007 SFT V1
**Lifecycle:** E004 prerequisite research only
**Canonical research base:** `4b679134258ba1b95e5400309b41a975cdced07c`
**Predecessor evidence packet:** `specs/007-sft-v1/e004-artifact-public-evidence-2026-08-27.md`
**Authority effect:** NONE

This document records newly recovered read-only public evidence for the frozen CONTROL `Qwen/Qwen3-4B-Base` preconverted-artifact path. It narrows the Antigma artifact result from `NEEDS_EVIDENCE` to a deterministic non-match against the exact E001 frozen revision, and records a later community candidate as a research lead only. It does not rewrite E001, expand E002, authorize acquisition of any new preconverted artifact, authorize model conversion, authorize E004 execution, select a backbone, authorize training, or authorize spend.

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
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
```

## 1. Frozen CONTROL identity

E001/E002 bind the CONTROL to exactly:

```text
CANDIDATE_ID=Qwen/Qwen3-4B-Base
FROZEN_UPSTREAM_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
ROLE=CONTROL
WINNER_ELIGIBLE=NO
PURPOSE=SCALE_QUALITY_OPPORTUNITY_COST
```

E002 explicitly enforces:

```text
IMMUTABLE_FROZEN_CANDIDATE_REVISIONS_ONLY=ENFORCED
PRECONVERTED_EXACT_ALLOWLIST_ONLY=ENFORCED
PRECONVERTED_ARTIFACTS_NOT_EXPLICITLY_LISTED=UNAUTHORIZED
```

E002 does not permit substituting another source revision merely because the repository family is the same or the weight-bearing files may appear similar.

## 2. Antigma artifact identity remains stable

The predecessor packet identified this exact-base-family community artifact:

```text
GGUF_REPOSITORY=Antigma/Qwen3-4B-Base-GGUF
GGUF_DECLARED_ORIGINAL_MODEL=Qwen/Qwen3-4B-Base
GGUF_DECLARED_QUANTIZER=llama.cpp b5215
GGUF_FILENAME=qwen3-4b-base-q4_k_m.gguf
GGUF_FILE_COMMIT=ab03cef12ef7fac77574d54a28331026c21257a0
GGUF_SHA256=a91798f5f24b6ef5e9309fa97cb82be19c930f5b1e359e5d1af80d20e24b3f68
GGUF_XET_HASH=3701df64f3275dbbe1736bb655927456b4d7f452b5242e40a1af5cceed23e984
GGUF_PUBLIC_DISPLAY_SIZE=2.5 GB
GGUF_CARD_REPORTED_SIZE=2.33 GB
GGUF_EXACT_BYTES=NEEDS_EVIDENCE
```

Public sources:

- `https://huggingface.co/Antigma/Qwen3-4B-Base-GGUF`
- `https://huggingface.co/Antigma/Qwen3-4B-Base-GGUF/blob/main/qwen3-4b-base-q4_k_m.gguf`
- `https://huggingface.co/Antigma/Qwen3-4B-Base-GGUF/tree/ab03cef12ef7fac77574d54a28331026c21257a0`

The repository card explicitly points to `Qwen/Qwen3-4B-Base`, and the file page exposes the stable SHA-256 and Xet identities above.

The human-readable `2.5 GB` file display and `2.33 GB` model-card table entry are not exact integer-byte metadata and must not be converted into an exact byte count by assumption.

## 3. Antigma conversion implementation is repository-pinned only

The public Antigma Quantize Space source currently exposes its conversion path in:

- `https://huggingface.co/spaces/Antigma/quantize-my-repo/blob/main/app.py`

The application accepts a `model_id` string and downloads the model using the equivalent of:

```python
api.snapshot_download(
    repo_id=model_id,
    local_dir=local_dir,
    local_dir_use_symlinks=False,
    allow_patterns=dl_pattern,
)
```

No immutable Hugging Face `revision` parameter is passed to `snapshot_download(...)` in the inspected source. The generated model card also records only the original repository identity, not a source commit SHA.

Therefore:

```text
ANTIGMA_PUBLIC_CONVERTER_REPOSITORY_IDENTITY_INPUT=YES
ANTIGMA_PUBLIC_CONVERTER_IMMUTABLE_HF_REVISION_INPUT=NO
ANTIGMA_GENERATED_CARD_IMMUTABLE_SOURCE_REVISION_ATTESTATION=NO
```

This alone would keep exact frozen-revision provenance incomplete. The temporal evidence below is stronger and deterministically excludes the frozen revision from being the conversion input for this artifact.

## 4. Antigma artifact predates the E001 frozen revision

The Hugging Face quantization index for `Qwen/Qwen3-4B-Base` reports:

```text
ANTIGMA_QWEN3_4B_BASE_GGUF_UPDATED_DATE=2025-05-29
```

The upstream Qwen commit history reports the E001 frozen revision:

```text
FROZEN_UPSTREAM_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
FROZEN_UPSTREAM_REVISION_DATE=2025-07-26
FROZEN_UPSTREAM_REVISION_COMMIT_MESSAGE=Create LICENSE
```

Public source history:

- `https://huggingface.co/Qwen/Qwen3-4B-Base/commits/main`
- `https://huggingface.co/Qwen/Qwen3-4B-Base/commits/906bfd4b4dc7f14ee4320094d8b41684abff8539`

The Antigma artifact repository was already published/updated approximately two months before the exact frozen revision existed. An artifact that already existed on 2025-05-29 cannot have been produced by downloading a source commit first created on 2025-07-26.

Therefore the predecessor field can be deterministically corrected for this artifact:

```text
ANTIGMA_ARTIFACT_PREDATES_FROZEN_REVISION=YES
ANTIGMA_EXACT_FROZEN_SOURCE_REVISION_USED_BY_CONVERSION=NO
```

This is stronger than `NEEDS_EVIDENCE` for the Antigma artifact itself.

It does **not** mean `Qwen/Qwen3-4B-Base` is a NO-GO CONTROL candidate. It means only that this specific preconverted artifact cannot satisfy E002's exact frozen-revision binding standard.

## 5. Later LICENSE-only revision does not authorize predecessor substitution

The E001 frozen commit message is `Create LICENSE`. Public repository history shows the model family existed before that commit and the July commit appears later than the original weight publication.

That fact does not permit commandMed to silently replace exact revision identity with a predecessor revision. E002 states that access is limited to the exact frozen revisions and explicitly prohibits substituting another checkpoint revision.

Accordingly:

```text
FROZEN_REVISION_MAY_BE_CONTENT_CLOSE_TO_PREDECESSOR=UNDECIDED_NOT_AUTHORITY
PREDECESSOR_REVISION_SUBSTITUTION_ALLOWED=NO
ANTIGMA_ARTIFACT_ALLOWLIST_ELIGIBILITY=REJECT_EXACT_REVISION_MISMATCH
```

A separately accepted canonical method could in principle establish byte-equivalent source identity for a future authority decision, but no such method is created by this packet and no byte-equivalence proof was executed here.

## 6. Later exact-base Q4_K_M candidate scan

Read-only discovery of Hugging Face's quantized-model index found at least one later exact-base-family Q4_K_M artifact published after the frozen revision:

```text
ALTERNATE_REPOSITORY=straino/Qwen3-4B-Base-Q4_K_M-GGUF
ALTERNATE_DECLARED_SOURCE=Qwen/Qwen3-4B-Base
ALTERNATE_DECLARED_FORMAT=GGUF
ALTERNATE_DECLARED_QUANTIZATION=Q4_K_M
ALTERNATE_PUBLIC_UPDATED_DATE=2025-09-08
ALTERNATE_CONVERSION_SERVICE=ggml.ai GGUF-my-repo
```

Public source:

- `https://huggingface.co/straino/Qwen3-4B-Base-Q4_K_M-GGUF`

The publication date is after the frozen source revision date, so this candidate does not suffer the same deterministic temporal impossibility as the Antigma artifact.

However, publication after the frozen revision is not the same thing as an immutable conversion-input attestation.

## 7. ggml-org GGUF-my-repo is also not immutable-source-revision pinned

The public `ggml-org/gguf-my-repo` Space source shows the model acquisition path using `snapshot_download(...)`/`HfApi.snapshot_download(...)` with `repo_id=model_id` and no immutable source `revision` parameter in the inspected implementations.

Representative public source:

- `https://huggingface.co/spaces/ggml-org/gguf-my-repo/blob/c8a66eb03325cd45b4ed3efeef760cf06a52ab9d/app.py`

The relevant acquisition path is equivalent to:

```python
api.snapshot_download(
    repo_id=model_id,
    local_dir=model_name,
    local_dir_use_symlinks=False,
    allow_patterns=dl_pattern,
)
```

Older public implementations likewise call `snapshot_download(repo_id=model_id, ...)` without an immutable revision.

Therefore:

```text
GGML_MY_REPO_REPOSITORY_IDENTITY_INPUT=YES
GGML_MY_REPO_IMMUTABLE_HF_REVISION_INPUT=NO
```

## 8. Temporal inference for later candidates is strong but not an attestation

The public Qwen commit history currently lists `906bfd4b4dc7f14ee4320094d8b41684abff8539` as the latest commit after 2025-07-26; no later source commit is listed.

A default-revision conversion of `Qwen/Qwen3-4B-Base` performed on 2025-09-08 would therefore be strongly consistent with resolving to the frozen revision, assuming the service resolved the default `main` ref in the ordinary way at conversion time.

This is useful research evidence, but commandMed's current CONTROL requirement is stronger:

> obtain an immutable conversion-source revision attestation proving the exact input was `Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539`.

The later candidate therefore remains:

```text
ALTERNATE_TEMPORAL_DEFAULT_HEAD_MATCH=STRONG_PUBLIC_INFERENCE
ALTERNATE_IMMUTABLE_CONVERSION_SOURCE_REVISION_ATTESTATION=NEEDS_EVIDENCE
ALTERNATE_E002_ALLOWLIST_ELIGIBILITY=INCOMPLETE
```

`STRONG_PUBLIC_INFERENCE` must not be promoted to `PASS` for an immutable provenance field.

## 9. Alternative inventory does not expand artifact authority

The Hugging Face model tree exposes multiple quantizations of `Qwen/Qwen3-4B-Base`, including later artifacts. Their existence is discovery evidence only.

A later publication date, exact family name, model-tree relationship, or community conversion statement does not independently satisfy all of E002's deterministic binding requirements:

- exact artifact repository;
- immutable artifact revision;
- exact filename;
- exact integer byte count;
- exact SHA-256;
- exact frozen source-revision provenance;
- acceptable rights/provenance;
- explicit authority expansion.

No alternate artifact is added to E002 by this packet.

## 10. Corrected CONTROL provenance matrix

| Evidence field | Antigma Q4_K_M | Later exact-base research candidate |
|---|---|---|
| Exact CONTROL repository family | `PASS` | `PASS` |
| Declared original model is `Qwen/Qwen3-4B-Base` | `PASS` | `PASS` |
| Q4_K_M artifact | `PASS` | `PASS` |
| Stable artifact SHA-256 | `PASS` | `NEEDS_EVIDENCE_IN_THIS_PACKET` |
| Stable artifact Xet identity | `PASS` | `NEEDS_EVIDENCE_IN_THIS_PACKET` |
| Exact integer bytes | `NEEDS_EVIDENCE` | `NEEDS_EVIDENCE` |
| Conversion service public | `PASS` | `PASS` |
| Converter accepts immutable HF revision | `FAIL_ABSENT` | `FAIL_ABSENT` |
| Artifact predates frozen revision | `YES` | `NO` |
| Exact frozen revision could have been conversion input | `NO` | `POSSIBLE` |
| Immutable frozen revision attested | `NO` | `NEEDS_EVIDENCE` |
| E002 allowlist eligibility | `REJECT_EXACT_REVISION_MISMATCH` | `INCOMPLETE` |

The alternate row is intentionally not promoted beyond the evidence inspected in this packet. It is a research lead, not a proposed allowlist mutation.

## 11. Artifact-authority reconciliation result

The CONTROL evidence is now more decisive than the predecessor packet for the Antigma artifact:

```text
CONTROL_ANTIGMA_EXACT_BASE_FAMILY_MATCH=PASS
CONTROL_ANTIGMA_ARTIFACT_IDENTITY=PASS
CONTROL_ANTIGMA_EXACT_FROZEN_SOURCE_REVISION_USED_BY_CONVERSION=NO
CONTROL_ANTIGMA_E002_ALLOWLIST_ELIGIBILITY=REJECT_EXACT_REVISION_MISMATCH

CONTROL_LATER_EXACT_BASE_ARTIFACT_EXISTS=YES
CONTROL_LATER_ARTIFACT_IMMUTABLE_SOURCE_ATTESTATION=NEEDS_EVIDENCE
CONTROL_LATER_ARTIFACT_EXACT_BYTES=NEEDS_EVIDENCE
CONTROL_LATER_ARTIFACT_E002_ALLOWLIST_ELIGIBILITY=INCOMPLETE

FROZEN_ARTIFACT_AUTHORITY_RECONCILIATION=EVIDENCE_INCOMPLETE_NO_EXPANSION
E002_PRECONVERTED_ALLOWLIST_COUNT=2
NEW_PRECONVERTED_ALLOWLIST_ENTRIES=0
CONTROL_PRECONVERTED_ACQUISITION_AUTHORITY=NONE_BEYOND_EXISTING_E002
MODEL_CONVERSION_AUTHORITY=NONE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

This is an artifact-level rejection, not a CONTROL-model rejection.

## 12. Remaining dependency-safe CONTROL research

Without changing authority, later read-only work may seek:

1. a later Q4_K_M exact-base artifact whose immutable conversion manifest directly records source revision `906bfd4b4dc7f14ee4320094d8b41684abff8539`;
2. immutable Space/job/log metadata for a later conversion binding the default source checkout to that exact SHA;
3. public Hugging Face/Xet/LFS metadata exposing exact integer artifact bytes without downloading model payload bytes;
4. a first-party Qwen exact-base GGUF generated from the frozen revision, if one is published later; or
5. a separately accepted canonical byte-equivalence method, if the repository explicitly authorizes such a method in a future decision.

If no qualifying preconverted artifact can satisfy the frozen identity standard, the repository must preserve the gap. A fresh deterministic conversion from the frozen E001 source remains a separate Founder authorization decision and is not implied by this research.

## 13. Non-events

No model or GGUF payload bytes were downloaded. No model was loaded. No inference, benchmark, physical-device measurement, contamination assessment, model conversion, quantization, training, credentialed/gated-asset access, Private Gold, PHI, provider generation, or paid-resource execution occurred.
