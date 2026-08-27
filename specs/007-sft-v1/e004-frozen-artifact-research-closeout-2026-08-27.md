# E004 Frozen-Artifact Research Closeout — 2026-08-27

**Spec:** 007 SFT V1
**Lifecycle:** E004 prerequisite research only
**Canonical research base:** `a5c7fb746e577e222341aaef18f7ce9cbceccd5d`
**Authority effect:** NONE

This closeout synthesizes the current read-only public evidence pass for the frozen Granite PRIMARY artifact gap and the frozen Qwen3 4B CONTROL artifact gap. It closes only this bounded research pass. It is not an artifact-authority decision, does not claim that all possible future public evidence is exhausted, and does not expand E002, authorize acquisition of any new preconverted artifact, authorize conversion, authorize contamination assessment, execute E004, select a backbone, authorize training, or authorize spend.

```text
CURRENT_PUBLIC_ARTIFACT_RESEARCH_PASS=CLOSED
PUBLIC_ARTIFACT_RESEARCH_EXHAUSTIVE_FOR_ALL_FUTURE_EVIDENCE=NO
ARTIFACT_AUTHORITY_DECISION=NOT_TAKEN
E002_PRECONVERTED_ALLOWLIST_COUNT=2
NEW_PRECONVERTED_ALLOWLIST_ENTRIES=0
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_EXECUTION_AUTHORITY=NONE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 1. Controlling artifact standard

E002 remains canonical and unchanged. It permits acquisition only of exact explicitly allowlisted preconverted artifacts and preserves the exact frozen E001 candidate revisions. Repository-family similarity, a mutable `main` relationship, a human-readable artifact size, a community model card, or a plausible temporal relationship does not independently satisfy the deterministic artifact binding standard.

The current artifact reconciliation question is therefore not:

> Does a plausible GGUF exist?

It is:

> Is there sufficient immutable evidence to bind an exact executable artifact to the exact frozen candidate identity under the current E002 contract, including provenance and exact artifact identity, without inventing or weakening required fields?

For the unresolved Granite PRIMARY and Qwen3 4B CONTROL paths, the current answer is **no expansion supported by the evidence presently recorded**.

## 2. Canonical evidence packets synthesized

This closeout relies on the canonical research chain already merged into `main`:

- `specs/007-sft-v1/e004-artifact-public-evidence-2026-08-27.md`
- `specs/007-sft-v1/e004-granite-run-attestation-followup-2026-08-27.md`
- `specs/007-sft-v1/e004-granite-artifact-history-correction-2026-08-27.md`
- `specs/007-sft-v1/e004-control-artifact-provenance-correction-2026-08-27.md`

Those packets preserve their own narrower evidence histories. This closeout does not rewrite them.

## 3. Granite PRIMARY research result

Frozen subject:

```text
CANDIDATE_ID=ibm-granite/granite-4.0-350m-base
FROZEN_UPSTREAM_REVISION=a50b46cef21c8a86b15f0496cb794487a78a910b
ROLE=PRIMARY
```

Public first-party Q4_K_M artifact identity recovered:

```text
GGUF_REPOSITORY=ibm-granite/granite-4.0-350m-base-GGUF
GGUF_FILENAME=granite-4.0-350m-base-Q4_K_M.gguf
GGUF_SHA256=2c22ed74d6c11791eb017886e1356ae11a6b8207b1ab2c1dfee047370110389a
GGUF_XET_HASH=3e8f4874960be082b8605f5a55e0c1ca1654b2cba4ac102b9188429cdb3189c8
GGUF_PUBLIC_DISPLAY_SIZE=237 MB
GGUF_EXACT_BYTES=NEEDS_EVIDENCE
```

The Granite history research additionally recovered:

```text
HISTORICAL_GGUF_REVISION=ad57f4f9b49d26004e766e0d085039ed6f85e1c5
HISTORICAL_IBM_RUN_ID=18753378058
HISTORICAL_BASE_CONVERSION_JOB_ID=53499040376
HISTORICAL_Q4_K_M_JOB_ID=53499879576
HISTORICAL_PIPELINE_IDENTITY=PASS
HISTORICAL_Q4_K_M_CONTENT_IDENTITY=PASS
```

The public IBM downloader used by the recovered historical conversion path does not pass an immutable Hugging Face `revision` argument. The historical conversion/quantization logs are no longer retained and return `410 Gone`, so they cannot now provide a runtime-resolved source SHA. The frozen source revision and historical conversion occur on the same calendar date, but exact ordering sufficient to bind the conversion to the frozen source was not established.

Therefore:

```text
GRANITE_FIRST_PARTY_Q4_K_M_ARTIFACT_IDENTITY=PASS
GRANITE_HISTORICAL_CONVERSION_PIPELINE_IDENTITY=PASS
GRANITE_EXACT_FROZEN_SOURCE_REVISION_USED_TO_PRODUCE_BYTES=NEEDS_EVIDENCE
GRANITE_EXACT_ARTIFACT_BYTES=NEEDS_EVIDENCE
GRANITE_E002_ALLOWLIST_ELIGIBILITY=INCOMPLETE
GRANITE_NEW_PRECONVERTED_AUTHORITY=NONE
```

The April 2026 IBM refresh evidence does not cure the historical byte-origin gap because the same Q4_K_M content identity was already public in October 2025.

## 4. Qwen3 4B CONTROL research result

Frozen subject:

```text
CANDIDATE_ID=Qwen/Qwen3-4B-Base
FROZEN_UPSTREAM_REVISION=906bfd4b4dc7f14ee4320094d8b41684abff8539
ROLE=CONTROL
WINNER_ELIGIBLE=NO
```

Current Antigma Q4_K_M artifact identity recovered:

```text
GGUF_REPOSITORY=Antigma/Qwen3-4B-Base-GGUF
GGUF_FILENAME=qwen3-4b-base-q4_k_m.gguf
GGUF_FILE_COMMIT=ab03cef12ef7fac77574d54a28331026c21257a0
GGUF_SHA256=a91798f5f24b6ef5e9309fa97cb82be19c930f5b1e359e5d1af80d20e24b3f68
GGUF_XET_HASH=3701df64f3275dbbe1736bb655927456b4d7f452b5242e40a1af5cceed23e984
GGUF_PUBLIC_DISPLAY_SIZE=2.5 GB
GGUF_CARD_REPORTED_SIZE=2.33 GB
GGUF_EXACT_BYTES=NEEDS_EVIDENCE
```

The inspected public Antigma conversion implementation downloads by repository ID but does not pass an immutable Hugging Face source `revision`. Repository/index update dates are context only; they are not treated as immutable timestamps for the identified file bytes or conversion execution. Accordingly no source-revision match or mismatch is inferred.

A later exact-base Q4_K_M research lead was also identified:

```text
ALTERNATE_REPOSITORY=straino/Qwen3-4B-Base-Q4_K_M-GGUF
ALTERNATE_DECLARED_SOURCE=Qwen/Qwen3-4B-Base
ALTERNATE_DECLARED_QUANTIZATION=Q4_K_M
ALTERNATE_CONVERSION_SERVICE=ggml.ai GGUF-my-repo
```

The inspected public `ggml-org/gguf-my-repo` source likewise downloads by repository ID without an immutable source `revision` parameter. No immutable conversion execution record binding that artifact to `906bfd4b4dc7f14ee4320094d8b41684abff8539` was recovered, and exact integer artifact bytes were not established.

Therefore:

```text
CONTROL_ANTIGMA_ARTIFACT_IDENTITY=PASS
CONTROL_ANTIGMA_EXACT_FROZEN_SOURCE_REVISION_USED_BY_CONVERSION=NEEDS_EVIDENCE
CONTROL_ANTIGMA_EXACT_ARTIFACT_BYTES=NEEDS_EVIDENCE
CONTROL_ANTIGMA_E002_ALLOWLIST_ELIGIBILITY=INCOMPLETE

CONTROL_LATER_EXACT_BASE_ARTIFACT_EXISTS=YES
CONTROL_LATER_ARTIFACT_IMMUTABLE_SOURCE_ATTESTATION=NEEDS_EVIDENCE
CONTROL_LATER_ARTIFACT_EXACT_BYTES=NEEDS_EVIDENCE
CONTROL_LATER_ARTIFACT_E002_ALLOWLIST_ELIGIBILITY=INCOMPLETE
CONTROL_NEW_PRECONVERTED_AUTHORITY=NONE
```

This is not a CONTROL-model NO-GO. The CONTROL remains frozen for its opportunity-cost role; only the preconverted-artifact binding remains incomplete.

## 5. Current deterministic reconciliation matrix

| Frozen path | Exact artifact identity | Immutable frozen-source binding | Exact integer bytes | Current E002 expansion support |
|---|---|---|---|---|
| Granite 350M Base Q4_K_M | `PASS` | `NEEDS_EVIDENCE` | `NEEDS_EVIDENCE` | `NO` |
| Qwen3 4B Base Antigma Q4_K_M | `PASS` | `NEEDS_EVIDENCE` | `NEEDS_EVIDENCE` | `NO` |
| Qwen3 4B Base later research artifact | `INCOMPLETE` | `NEEDS_EVIDENCE` | `NEEDS_EVIDENCE` | `NO` |

`NO` in the final column means **the current evidence does not support an E002 allowlist expansion**. It is not a permanent prohibition on future evidence, a candidate disqualification, or a conversion authorization.

## 6. Current public research pass conclusion

The current read-only pass materially improved provenance knowledge but did not produce a complete new artifact binding under E002.

```text
PUBLIC_PRECONVERTED_RESEARCH_RESULT=NO_EXPANSION_SUPPORTED_BY_CURRENT_EVIDENCE
CURRENT_PUBLIC_ARTIFACT_RESEARCH_PASS=CLOSED
FUTURE_NEW_PUBLIC_EVIDENCE_MAY_BE_CONSIDERED=YES
E002_MUTATION_PERFORMED=NO
PRECONVERTED_ALLOWLIST_CHANGED=NO
MODEL_CONVERSION_AUTHORITY_CHANGED=NO
```

The repository must not continue searching indefinitely merely to manufacture a PASS. A new public artifact or immutable first-party attestation may reopen research, but absence of such evidence is preserved as an incomplete prerequisite rather than replaced with inference.

## 7. Artifact-authority decision remains separate

This research closeout does not choose among future governance options. The next artifact step remains a separate explicit Founder authorization decision.

Dependency-safe decision classes include, without authorizing any of them here:

1. **Preserve current artifact authority** — keep E002 at two preconverted entries, preserve `MODEL_CONVERSION_AUTHORITY=NONE`, and keep the full frozen tournament blocked on artifact prerequisites.
2. **Authorize a separately bounded conversion path** — define exact frozen source revision(s), conversion runtime/tool revision, quantization, deterministic outputs, hashing/size attestation, rights/provenance, zero-spend/resource envelope, storage/retention, and review/qualification gates before any conversion may occur.
3. **Accept a future new preconverted artifact** — only after a new immutable evidence packet satisfies the complete E002 binding standard and a separate explicit allowlist mutation is authorized.
4. **Amend the frozen protocol/candidate obligations** — a governance change requiring its own explicit authority and scientific justification; not implied by artifact inconvenience.

This document recommends none of these by authority. It only records the evidence state needed for the separate decision.

```text
NEXT_ARTIFACT_STEP=SEPARATE_FOUNDER_AUTHORIZATION_DECISION
FOUNDER_DECISION_TAKEN_BY_THIS_CLOSEOUT=NO
CONVERSION_AUTHORIZED_BY_THIS_CLOSEOUT=NO
ALLOWLIST_EXPANSION_AUTHORIZED_BY_THIS_CLOSEOUT=NO
PROTOCOL_AMENDMENT_AUTHORIZED_BY_THIS_CLOSEOUT=NO
```

## 8. Other E004 blockers remain independent

Closing the current artifact research pass does not make E004 ready. The corrective-maintenance closeout already preserves additional independent blockers, including:

- contamination-assessment authority and candidate × selection-slice evidence;
- scientific/governance threshold and statistical-design evidence;
- runtime/build/tool/signal and physical-target bindings;
- personnel/access/finance and verified zero-spend resource evidence;
- real A1–A14 snapshot construction and separate A15 activation;
- exact E004 manifest/admission records and final pre-execution validation.

No one blocker should be silently treated as resolved because another blocker becomes better understood.

## 9. Post-research STOP state

```text
FROZEN_ARTIFACT_RESEARCH=INCOMPLETE_AS_AUTHORITY_PREREQUISITE
CURRENT_PUBLIC_RESEARCH_PASS=CLOSED
FROZEN_ARTIFACT_AUTHORITY_RECONCILIATION=DECISION_NOT_TAKEN
E002_PRECONVERTED_ALLOWLIST_COUNT=2
NEW_PRECONVERTED_ALLOWLIST_ENTRIES=0
MODEL_CONVERSION_AUTHORITY=NONE
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E004_EXECUTION_OCCURRED=NO
A15_REAL_ACTIVATION=ABSENT
TOURNAMENT_EVIDENCE_PACK=NOT_PRODUCED
E005_REACHABLE=NO
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

This is the furthest state reached by the current public artifact research pass. It is not project completion and not E004 completion.

## 10. Non-events

No model or GGUF payload bytes were downloaded. No model was loaded. No inference, benchmark, physical-device measurement, contamination assessment, conversion, quantization, training, credentialed/gated-asset access, Private Gold, PHI, provider generation, or paid-resource execution occurred in producing this closeout.
