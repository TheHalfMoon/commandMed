# E004 Granite Run-Attestation Follow-Up — 2026-08-27

**Spec:** 007 SFT V1
**Lifecycle:** E004 prerequisite research only
**Canonical research base:** `1b88ee228f823af03c9a2780e6ac51941be43043`
**Predecessor evidence packet:** `specs/007-sft-v1/e004-artifact-public-evidence-2026-08-27.md`
**Authority effect:** NONE

This follow-up records new read-only public provenance evidence for the frozen Granite artifact path. It does not expand E002, authorize acquisition of any new preconverted artifact, authorize conversion, authorize contamination assessment, execute E004, select a backbone, or authorize training.

```text
ARTIFACT_RESEARCH_ONLY=YES
MODEL_WEIGHT_ACCESS_AUTHORITY=UNCHANGED
PRECONVERTED_ARTIFACT_ALLOWLIST=UNCHANGED
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
```

## 1. Question resolved by this follow-up

The predecessor packet established the first-party Granite GGUF artifact identity but left the exact frozen source revision used by IBM's conversion as `NEEDS_EVIDENCE`.

This follow-up asks a narrower question:

> Can the public IBM Actions record for the exact Granite 350M Base conversion provide an explicit immutable Hugging Face source-revision attestation?

The answer is **no with currently retained public evidence**. The exact conversion job can now be identified and its successful download/conversion/upload stages can be verified, but the detailed job log required to observe any runtime-resolved snapshot identity is no longer retained by GitHub. IBM's public downloader also does not accept or pass an immutable Hugging Face `revision` argument.

## 2. Frozen commandMed subject

The E001 subject remains unchanged:

```text
CANDIDATE_ID=ibm-granite/granite-4.0-350m-base
FROZEN_UPSTREAM_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
ROLE=PRIMARY
```

The first-party GGUF candidate established by the predecessor packet remains:

```text
GGUF_REPOSITORY=ibm-granite/granite-4.0-350m-base-GGUF
GGUF_FILENAME=granite-4.0-350m-base-Q4_K_M.gguf
GGUF_FILE_COMMIT=61ff4f9133240330c7b06009eaa173999b367cd9
GGUF_SHA256=2c22ed74d6c11791eb017886e1356ae11a6b8207b1ab2c1dfee047370110389a
GGUF_XET_HASH=3e8f4874960be082b8605f5a55e0c1ca1654b2cba4ac102b9188429cdb3189c8
GGUF_PUBLIC_DISPLAY_SIZE=237 MB
GGUF_EXACT_BYTES=NEEDS_EVIDENCE
```

Public artifact source:

- `https://huggingface.co/ibm-granite/granite-4.0-350m-base-GGUF/blob/main/granite-4.0-350m-base-Q4_K_M.gguf`

The file page binds the upload to GitHub Actions run `24843593968` and workflow ref `IBM/gguf/.github/workflows/granite-4.0-release-ibm-granite.yml@refs/tags/v4.0-language-refresh-20260423-01`.

## 3. Exact IBM conversion job now identified

The public GitHub Actions job listing for IBM run `24843593968` contains the exact base-model conversion job:

```text
IBM_GGUF_RUN_ID=24843593968
IBM_GGUF_RUN_ATTEMPT=2
IBM_GGUF_CALLER_HEAD_SHA=c82d14edcaebe6688cf560abd619653e4309fad3
IBM_GGUF_RELEASE_TAG=v4.0-language-refresh-20260423-01
GRANITE_CONVERSION_JOB_ID=72764761465
GRANITE_CONVERSION_JOB_NAME=language-convert-hf-to-f16-gguf (ibm-granite/granite-4.0-350m-base) / convert-safetensor-to-gguf
GRANITE_CONVERSION_JOB_RESULT=SUCCESS
```

Public job URL:

- `https://github.com/IBM/gguf/actions/runs/24843593968/job/72764761465`

The retained job metadata reports these relevant stages as successful:

```text
DOWNLOAD_MODEL_SNAPSHOT_STEP=SUCCESS
DOWNLOAD_MODEL_SNAPSHOT_START_UTC=2026-04-23T15:25:59Z
DOWNLOAD_MODEL_SNAPSHOT_END_UTC=2026-04-23T15:26:13Z

DOWNLOAD_SAFETENSORS_CONVERT_TO_GGUF_STEP=SUCCESS
DOWNLOAD_SAFETENSORS_CONVERT_TO_GGUF_START_UTC=2026-04-23T15:26:53Z
DOWNLOAD_SAFETENSORS_CONVERT_TO_GGUF_END_UTC=2026-04-23T15:27:08Z

UPLOAD_CONVERTED_GGUF_TO_TARGET_REPO_STEP=SUCCESS
UPLOAD_CONVERTED_GGUF_TO_TARGET_REPO_START_UTC=2026-04-23T15:27:08Z
UPLOAD_CONVERTED_GGUF_TO_TARGET_REPO_END_UTC=2026-04-23T15:27:09Z
```

This resolves **which exact public job produced the conversion path**. It does not by itself resolve the immutable Hugging Face source revision downloaded by that job.

## 4. The public downloader is not revision-pinned

At the caller run head `c82d14edcaebe6688cf560abd619653e4309fad3`, IBM's public downloader is:

- `scripts/hf_model_download_snapshot.py`
- `https://github.com/IBM/gguf/blob/c82d14edcaebe6688cf560abd619653e4309fad3/scripts/hf_model_download_snapshot.py`

Its `snapshot_download(...)` invocation supplies:

```text
repo_id
local_dir
allow_patterns
token
resume_download
```

It does **not** supply a Hugging Face `revision` argument. The command-line interface likewise accepts repository organization/name, token, and optional allow-pattern, but no revision.

Therefore:

```text
GRANITE_PUBLIC_DOWNLOADER_REPOSITORY_PIN=YES
GRANITE_PUBLIC_DOWNLOADER_IMMUTABLE_HF_REVISION_PIN=NO
```

This is a provenance limitation, not evidence of a wrong source revision.

## 5. Tagged caller workflow does not fully freeze reusable workflow implementation

The public release workflow at caller head `c82d14edcaebe6688cf560abd619653e4309fad3` includes the exact source repository in `SOURCE_LANGUAGE_REPOS` and uses llama.cpp build tag `b8100`.

It invokes the language conversion reusable workflow as:

```text
uses: IBM/gguf/.github/workflows/reusable-convert-hf-to-bf16-gguf.yml@main
```

rather than an immutable commit SHA or the release tag itself.

Accordingly, the release tag is strong evidence for the caller configuration and repository membership, but the caller file alone does not create an immutable identity for the reusable workflow implementation resolved at runtime.

```text
GRANITE_CALLER_WORKFLOW_TAGGED=YES
GRANITE_REUSABLE_CONVERSION_WORKFLOW_IMMUTABLY_PINNED_BY_CALLER=NO
```

No stronger runtime identity is inferred without retained run evidence.

## 6. Detailed job logs are no longer available

On 2026-08-27, a read-only request to GitHub's public job-log endpoint for job `72764761465` returned:

```text
HTTP_STATUS=410
RESULT=GONE
```

The retained job metadata remains available, but the detailed log body does not. Consequently this research pass cannot inspect runtime stdout/stderr for a Hugging Face resolved snapshot SHA or another explicit immutable source-revision marker.

```text
GRANITE_JOB_METADATA_RETAINED=YES
GRANITE_DETAILED_JOB_LOG_RETAINED=NO
GRANITE_RUNTIME_RESOLVED_SNAPSHOT_SHA_FROM_LOG=UNAVAILABLE
```

A missing retained log must not be replaced by inference.

## 7. Temporal default-HEAD evidence is strong but non-attesting

The public Hugging Face commit history for `ibm-granite/granite-4.0-350m-base` currently lists `a50b46c...` as the latest commit, dated 2025-10-23, with no later commit listed before the IBM conversion run on 2026-04-23.

Public history source:

- `https://huggingface.co/ibm-granite/granite-4.0-350m-base/commits/main`

This is strong temporal evidence that a default-revision `snapshot_download(repo_id=...)` on 2026-04-23 would have resolved to the commandMed-frozen revision, subject to the limitations of reconstructing historical mutable-ref state from current public history.

It is **not** an explicit run attestation and must remain semantically separate:

```text
GRANITE_TEMPORAL_DEFAULT_HEAD_MATCH=STRONG_PUBLIC_INFERENCE
GRANITE_EXPLICIT_RUN_SOURCE_REVISION_ATTESTATION=NEEDS_EVIDENCE
```

The project must not promote `STRONG_PUBLIC_INFERENCE` to `PASS` for a field whose contract requires an immutable conversion-input revision.

## 8. Exact byte count remains unresolved

The Hugging Face artifact page exposes:

- human-readable remote size: `237 MB`;
- exact SHA-256;
- exact Xet hash;
- a `Raw pointer file` link.

During this read-only pass, fetching the raw pointer through the available public retrieval path returned a cache miss rather than the pointer contents. No model payload was requested or downloaded.

The human-readable `237 MB` display is not converted into an exact integer byte count.

```text
GRANITE_EXACT_ARTIFACT_BYTES=NEEDS_EVIDENCE
MODEL_OR_GGUF_PAYLOAD_DOWNLOADED=NO
```

## 9. Deterministic evidence result

This follow-up strengthens provenance without satisfying the complete E002 preconverted-artifact binding standard:

| Evidence field | Result |
|---|---|
| Exact frozen family | `PASS` |
| First-party GGUF repository | `PASS` |
| Exact Q4_K_M filename | `PASS` |
| Exact GGUF commit | `PASS` |
| Exact GGUF SHA-256 | `PASS` |
| Exact GGUF Xet identity | `PASS` |
| Exact IBM conversion run | `PASS` |
| Exact IBM conversion job | `PASS` |
| Snapshot-download step success | `PASS` |
| Conversion step success | `PASS` |
| Upload step success | `PASS` |
| Explicit immutable HF revision supplied to downloader | `FAIL_ABSENT` |
| Runtime-resolved source revision from retained logs | `UNAVAILABLE_410_GONE` |
| Temporal default-HEAD match to E001 frozen revision | `STRONG_PUBLIC_INFERENCE` |
| Explicit run attestation to E001 frozen revision | `NEEDS_EVIDENCE` |
| Exact artifact bytes | `NEEDS_EVIDENCE` |
| E002 allowlist eligibility | `INCOMPLETE` |

`FAIL_ABSENT` above describes the absence of a revision pin in the public downloader interface. It is not a claim that the conversion used the wrong source commit.

## 10. Authority reconciliation remains fail-closed

The new evidence does not justify an allowlist change because the strict unresolved fields remain unresolved.

```text
GRANITE_EXACT_CONVERSION_JOB_IDENTITY=PASS
GRANITE_EXACT_FROZEN_SOURCE_REVISION_USED_BY_CONVERSION=NEEDS_EVIDENCE
GRANITE_EXACT_ARTIFACT_BYTES=NEEDS_EVIDENCE
GRANITE_E002_ALLOWLIST_ELIGIBILITY=INCOMPLETE

FROZEN_ARTIFACT_AUTHORITY_RECONCILIATION=EVIDENCE_INCOMPLETE_NO_EXPANSION
E002_PRECONVERTED_ALLOWLIST_COUNT=2
NEW_PRECONVERTED_ALLOWLIST_ENTRIES=0
GRANITE_PRECONVERTED_ACQUISITION_AUTHORITY=NONE_BEYOND_EXISTING_E002
MODEL_CONVERSION_AUTHORITY=NONE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
```

This is not a candidate NO-GO. It is a provenance-attestation limitation under commandMed's frozen identity standard.

## 11. Next dependency-safe research options

Without expanding authority, later read-only work may seek either:

1. an IBM/Hugging Face immutable conversion manifest, attestation, release artifact, or API record binding run `24843593968` / job `72764761465` to source revision `a50b46cef21c8a86b15f0496cb794487a78a910b`; or
2. public pointer/API metadata that exposes the GGUF exact integer byte count without downloading model payload bytes.

If neither exists, the repository should preserve the provenance gap rather than weaken E002. Any fresh conversion remains a separate Founder authorization decision and is not implied by this research.

## 12. Non-events

No model or GGUF payload bytes were downloaded. No model was loaded. No inference, benchmark, physical-device measurement, contamination assessment, conversion, training, credentialed/gated-asset access, Private Gold, PHI, provider generation, or paid-resource execution occurred.
