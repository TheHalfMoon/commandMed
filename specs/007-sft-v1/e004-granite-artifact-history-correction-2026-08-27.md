# E004 Granite Artifact-History Correction — 2026-08-27

**Spec:** 007 SFT V1
**Lifecycle:** E004 prerequisite research only
**Canonical research base:** `30bdbae7812a26a99b6120a53555d7f8e1976d5e`
**Predecessor evidence packets:**
- `specs/007-sft-v1/e004-artifact-public-evidence-2026-08-27.md`
- `specs/007-sft-v1/e004-granite-run-attestation-followup-2026-08-27.md`
**Authority effect:** NONE

This document records newly recovered public provenance history for the frozen Granite Q4_K_M artifact and narrowly corrects affected statements in the 2026-08-27 run-attestation follow-up. It does not rewrite the predecessor documents, widen E002, authorize artifact acquisition, authorize conversion, authorize contamination assessment, execute E004, select a backbone, authorize training, or authorize spend.

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
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
```

## 1. Scope of correction

The predecessor follow-up correctly preserved the unresolved frozen-source-revision and exact-byte gaps, but subsequent read-only research recovered three additional facts that change the provenance interpretation:

1. the exact `granite-4.0-350m-base-Q4_K_M.gguf` content identity already existed in an IBM-produced Hugging Face revision on 2025-10-23, months before the April 2026 refresh run;
2. GitHub run metadata records immutable resolved SHA values for reusable workflows even when the caller source spells the reference as `@main`; and
3. the April 2026 run exposes separate attempt-scoped job records whose timestamps must not be interpreted as two conversion executions.

These discoveries strengthen pipeline identity while making the historical source-revision question more important, not less.

## 2. Frozen commandMed subject remains unchanged

```text
CANDIDATE_ID=ibm-granite/granite-4.0-350m-base
FROZEN_UPSTREAM_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
ROLE=PRIMARY
```

The target preconverted artifact identity remains:

```text
GGUF_REPOSITORY=ibm-granite/granite-4.0-350m-base-GGUF
GGUF_FILENAME=granite-4.0-350m-base-Q4_K_M.gguf
GGUF_SHA256=2c22ed74d6c11791eb017886e1356ae11a6b8207b1ab2c1dfee047370110389a
GGUF_XET_HASH=3e8f4874960be082b8605f5a55e0c1ca1654b2cba4ac102b9188429cdb3189c8
GGUF_PUBLIC_DISPLAY_SIZE=237 MB
GGUF_EXACT_BYTES=NEEDS_EVIDENCE
```

No integer byte count is inferred from the human-readable display size.

## 3. Historical artifact revision proves the bytes predate the April 2026 refresh

A historical Hugging Face file revision at commit:

```text
HISTORICAL_GGUF_REVISION=ad57f4f9b49d26004e766e0d085039ed6f85e1c5
HISTORICAL_GGUF_DATE=2025-10-23
```

contains the same file:

```text
granite-4.0-350m-base-Q4_K_M.gguf
```

with the same public content identities:

```text
SHA256=2c22ed74d6c11791eb017886e1356ae11a6b8207b1ab2c1dfee047370110389a
XET_HASH=3e8f4874960be082b8605f5a55e0c1ca1654b2cba4ac102b9188429cdb3189c8
DISPLAY_SIZE=237 MB
```

The historical file page attributes that upload to:

```text
IBM_GGUF_RUN_ID=18753378058
IBM_GGUF_WORKFLOW_REF=IBM/gguf/.github/workflows/granite-4.0-release-ibm-granite.yml@refs/tags/v4.0-nano-bf16-all-quants-01
```

Public historical file URL:

- `https://huggingface.co/ibm-granite/granite-4.0-350m-base-GGUF/blob/ad57f4f9b49d26004e766e0d085039ed6f85e1c5/granite-4.0-350m-base-Q4_K_M.gguf`

Therefore:

```text
Q4_K_M_CONTENT_PRESENT_BY_2025_10_23=PASS
APRIL_2026_RUN_IS_EARLIEST_KNOWN_ORIGIN_OF_CURRENT_Q4_K_M_BYTES=NO
APRIL_2026_RUN_ALONE_CAN_ATTEST_ORIGINAL_BYTE_PROVENANCE=NO
```

The April 2026 refresh may have downloaded, converted, and/or re-uploaded equivalent content, but it cannot be used as the sole provenance origin for bytes demonstrably present in the public artifact repository in October 2025.

## 4. Exact October 2025 IBM run identity

Public GitHub Actions metadata for run `18753378058` records:

```text
HISTORICAL_RUN_ID=18753378058
HISTORICAL_RUN_ATTEMPT=1
HISTORICAL_RUN_RESULT=SUCCESS
HISTORICAL_RUN_HEAD_SHA=d08fdef1034a3885092f405df64230644258ae8e
HISTORICAL_RELEASE_TAG=v4.0-nano-bf16-all-quants-01
HISTORICAL_RUN_CREATED_UTC=2025-10-23T15:22:28Z
HISTORICAL_RUN_UPDATED_UTC=2025-10-23T17:10:39Z
```

GitHub's retained `referenced_workflows` metadata also resolves the mutable source-level reusable workflow references to immutable runtime SHA identities. In particular, the reusable conversion and quantization workflows resolve to:

```text
HISTORICAL_RESOLVED_REUSABLE_WORKFLOW_SHA=d08fdef1034a3885092f405df64230644258ae8e
```

Thus the correct semantics are:

```text
CALLER_SOURCE_USES_MUTABLE_REF=YES
RUNTIME_RESOLVED_REUSABLE_WORKFLOW_SHA_AVAILABLE=YES
RUNTIME_REUSABLE_WORKFLOW_IMPLEMENTATION_IDENTITY=PASS
```

The predecessor statement that the caller's `@main` syntax alone failed to create immutable reusable-workflow identity was correct at the source-text level but incomplete at the run-record level. GitHub's retained run metadata supplies the resolved SHA.

## 5. Exact historical base conversion job

The October run contains the exact Granite 350M Base conversion job:

```text
HISTORICAL_BASE_CONVERSION_JOB_ID=53499040376
HISTORICAL_BASE_CONVERSION_JOB_NAME=convert-hf-to-f16-gguf (ibm-granite/granite-4.0-350m-base) / convert-safetensor-to-gguf
HISTORICAL_BASE_CONVERSION_JOB_RESULT=SUCCESS
HISTORICAL_BASE_CONVERSION_JOB_STARTED_UTC=2025-10-23T15:24:46Z
HISTORICAL_BASE_CONVERSION_JOB_COMPLETED_UTC=2025-10-23T15:26:22Z
```

Public job URL:

- `https://github.com/IBM/gguf/actions/runs/18753378058/job/53499040376`

The historical job listing retains the job identity and timestamps, but not step-level logs.

## 6. Exact historical Q4_K_M quantization job

The same run contains the exact quantization job for the target artifact variant:

```text
HISTORICAL_Q4_K_M_JOB_ID=53499879576
HISTORICAL_Q4_K_M_JOB_NAME=quantize-upload-gguf (ibm-granite/granite-4.0-350m-base, Q4_K_M) / quantize
HISTORICAL_Q4_K_M_JOB_RESULT=SUCCESS
HISTORICAL_Q4_K_M_JOB_STARTED_UTC=2025-10-23T15:46:41Z
HISTORICAL_Q4_K_M_JOB_COMPLETED_UTC=2025-10-23T15:49:02Z
```

Public job URL:

- `https://github.com/IBM/gguf/actions/runs/18753378058/job/53499879576`

This job executes after the exact base conversion job in the same successful release run, providing a public execution chain from the named base-repository conversion stage to the named Q4_K_M quantization stage.

It does not, by itself, identify the immutable Hugging Face source revision consumed by the initial download.

## 7. Historical downloader is also not Hugging Face revision-pinned

At historical run head:

```text
d08fdef1034a3885092f405df64230644258ae8e
```

IBM's public `scripts/hf_model_download_snapshot.py` invokes `snapshot_download(...)` with repository identity and local/download parameters but no `revision` argument. Its CLI likewise provides no immutable source-revision input.

Therefore:

```text
HISTORICAL_PUBLIC_DOWNLOADER_REPOSITORY_PIN=YES
HISTORICAL_PUBLIC_DOWNLOADER_IMMUTABLE_HF_REVISION_PIN=NO
```

This is not evidence that the wrong source commit was used. It means exact source identity must be attested from another retained record before commandMed can treat the preconverted bytes as bound to the E001 frozen source revision.

## 8. Historical logs are no longer retained

On 2026-08-27, read-only requests to GitHub's public job-log endpoint returned `410 Gone` for both:

```text
JOB=53499040376
ROLE=historical base conversion
LOG_STATUS=410_GONE

JOB=53499879576
ROLE=historical Q4_K_M quantization
LOG_STATUS=410_GONE
```

Consequently, the historical execution logs cannot now be inspected for a runtime-resolved Hugging Face snapshot SHA or other immutable source-revision marker.

```text
HISTORICAL_JOB_METADATA_RETAINED=YES
HISTORICAL_DETAILED_JOB_LOGS_RETAINED=NO
HISTORICAL_RUNTIME_RESOLVED_HF_SOURCE_SHA_FROM_LOG=UNAVAILABLE
```

No missing log is replaced by inference.

## 9. Same-day source-history ordering remains unresolved

Public Hugging Face history lists commandMed's frozen source revision:

```text
a50b46cef21c8a86b15f0496cb794487a78a910b
```

on 2025-10-23, the same calendar date as IBM run `18753378058`.

The currently available public evidence in this research pass did not expose a reliable exact timestamp for that Hugging Face commit that can be compared to the historical conversion job start at `2025-10-23T15:24:46Z`.

Therefore commandMed must not infer ordering merely from the shared date:

```text
FROZEN_SOURCE_REVISION_DATE_MATCHES_HISTORICAL_RUN_DATE=YES
FROZEN_SOURCE_REVISION_EXACT_TIMESTAMP=NEEDS_EVIDENCE
FROZEN_SOURCE_REVISION_PROVEN_TO_PRECEDE_HISTORICAL_DOWNLOAD=NO
HISTORICAL_CONVERSION_SOURCE_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b_UNATTESTED
```

The April 2026 default-HEAD evidence may remain useful for describing what the April refresh likely resolved, but it is insufficient to prove the production origin of bytes already present in October 2025.

## 10. April 2026 attempt/job semantics correction

Run `24843593968` has two attempts:

```text
APRIL_RUN_ID=24843593968
APRIL_ATTEMPT1_RESULT=FAILURE
APRIL_ATTEMPT1_STARTED_UTC=2026-04-23T15:23:36Z
APRIL_ATTEMPT2_RESULT=SUCCESS
APRIL_ATTEMPT2_STARTED_UTC=2026-04-23T19:33:22Z
```

The attempt-scoped job listing exposes two records for the same successful Granite base conversion path.

### Attempt 1 execution record

```text
APRIL_ATTEMPT1_BASE_CONVERSION_JOB_ID=72724359318
APRIL_ATTEMPT1_BASE_CONVERSION_JOB_RESULT=SUCCESS
APRIL_ATTEMPT1_BASE_CONVERSION_JOB_STARTED_UTC=2026-04-23T15:25:46Z
APRIL_ATTEMPT1_BASE_CONVERSION_JOB_COMPLETED_UTC=2026-04-23T15:27:15Z
```

The retained steps include successful snapshot download, conversion, and upload during those attempt-1 timestamps.

### Attempt 2 job record

```text
APRIL_ATTEMPT2_BASE_CONVERSION_JOB_ID=72764761465
APRIL_ATTEMPT2_BASE_CONVERSION_JOB_RESULT=SUCCESS
APRIL_ATTEMPT2_RECORD_CREATED_AFTER_ATTEMPT2_START=YES
APRIL_ATTEMPT2_RECORD_STEP_TIMESTAMPS=ATTEMPT1_TIME_WINDOW
```

The `run_attempt=2` record retains execution/step timestamps around `15:25–15:27Z`, which precede attempt 2's run start near `19:33Z`.

The safe interpretation is therefore:

```text
APRIL_ATTEMPT1_ORIGINAL_EXECUTION_JOB=72724359318
APRIL_ATTEMPT2_JOB_RECORD=72764761465
APRIL_ATTEMPT2_RECORD_PROVES_SECOND_CONVERSION_EXECUTION_AT_19_33=NO
```

No stronger GitHub retry-behavior semantics are inferred from this metadata.

This supersedes only the predecessor follow-up's use of job `72764761465` as if it were the single unqualified exact conversion execution identity.

## 11. April reusable workflow identity correction

GitHub run metadata for the April run likewise retains immutable resolved workflow SHA information:

```text
APRIL_CALLER_HEAD_SHA=c82d14edcaebe6688cf560abd619653e4309fad3
APRIL_CALLER_SOURCE_USES_REUSABLE_WORKFLOW_AT_MAIN=YES
APRIL_RESOLVED_REUSABLE_WORKFLOW_SHA=c82d14edcaebe6688cf560abd619653e4309fad3
APRIL_RUNTIME_REUSABLE_WORKFLOW_IMPLEMENTATION_IDENTITY=PASS
```

Therefore source-level `@main` mutability does not leave the completed run's reusable workflow implementation unknown once the retained GitHub run record is considered.

This correction does not solve the Hugging Face source-snapshot identity gap because the IBM downloader itself still lacks an immutable HF `revision` input and the detailed logs are unavailable.

## 12. Exact artifact byte count remains unresolved

The public artifact UI continues to expose:

```text
DISPLAY_SIZE=237 MB
SHA256=2c22ed74d6c11791eb017886e1356ae11a6b8207b1ab2c1dfee047370110389a
XET_HASH=3e8f4874960be082b8605f5a55e0c1ca1654b2cba4ac102b9188429cdb3189c8
```

A raw pointer link exists, but the available public retrieval paths in this research pass did not return the pointer contents. No GGUF/model payload was requested or downloaded.

```text
GRANITE_EXACT_ARTIFACT_BYTES=NEEDS_EVIDENCE
MODEL_OR_GGUF_PAYLOAD_DOWNLOADED=NO
```

The project continues to reject conversion of `237 MB` into guessed integer bytes.

## 13. Corrected provenance matrix

| Evidence field | Corrected result |
|---|---|
| Frozen Granite family | `PASS` |
| First-party GGUF repository | `PASS` |
| Exact Q4_K_M filename | `PASS` |
| Exact GGUF SHA-256 | `PASS` |
| Exact GGUF Xet identity | `PASS` |
| Same content publicly present by 2025-10-23 | `PASS` |
| Historical IBM release run identity | `PASS` |
| Historical resolved reusable-workflow SHA | `PASS` |
| Historical exact base conversion job | `PASS` |
| Historical exact Q4_K_M quantization job | `PASS` |
| Historical downloader immutable HF revision pin | `FAIL_ABSENT` |
| Historical runtime source SHA from retained logs | `UNAVAILABLE_410_GONE` |
| E001 frozen revision proven to precede historical download | `NEEDS_EVIDENCE` |
| Exact frozen source revision used to produce current Q4_K_M bytes | `NEEDS_EVIDENCE` |
| April attempt-1 exact conversion execution job | `PASS` |
| April attempt-2 record proves a second conversion execution | `NO` |
| April resolved reusable-workflow SHA | `PASS` |
| April default-HEAD match to frozen revision | `STRONG_PUBLIC_INFERENCE_ONLY` |
| April run proves original current-byte provenance | `NO` |
| Exact artifact integer bytes | `NEEDS_EVIDENCE` |
| E002 allowlist eligibility | `INCOMPLETE` |

`FAIL_ABSENT` describes the missing immutable HF revision parameter in IBM's public downloader. It is not a claim that IBM used the wrong model revision.

## 14. Authority reconciliation remains unchanged and fail-closed

The newly recovered history strengthens artifact/pipeline identity but does not satisfy the strict source-revision and exact-byte requirements for a new preconverted allowlist entry.

```text
GRANITE_HISTORICAL_PIPELINE_IDENTITY=PASS
GRANITE_Q4_K_M_HISTORICAL_CONTENT_IDENTITY=PASS
GRANITE_EXACT_FROZEN_SOURCE_REVISION_USED_TO_PRODUCE_BYTES=NEEDS_EVIDENCE
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
CURRENT_AUTHORIZED_SPEND_USD=0
```

This is not a candidate NO-GO. It is an unresolved immutable source-binding requirement.

## 15. Dependency-safe next research

Without changing authority, later read-only work may seek:

1. an immutable IBM/Hugging Face manifest or attestation tying historical run `18753378058`, conversion job `53499040376`, or Q4_K_M job `53499879576` to source revision `a50b46cef21c8a86b15f0496cb794487a78a910b`;
2. exact timestamp evidence for the 2025-10-23 Hugging Face frozen source commit sufficient to establish or disprove ordering against the historical model download;
3. public Hugging Face/Xet pointer/API metadata exposing exact integer file bytes without downloading the model payload; or
4. another first-party immutable artifact record that directly binds source revision, quantization, filename, exact bytes, and digest.

If those records do not exist, commandMed must preserve the provenance gap. A fresh deterministic conversion remains a separate Founder authorization decision and is not implied by this research.

## 16. Non-events

No model or GGUF payload bytes were downloaded. No model was loaded. No inference, benchmark, physical-device measurement, contamination assessment, model conversion, training, credentialed/gated-asset access, Private Gold, PHI, provider generation, or paid-resource execution occurred.
