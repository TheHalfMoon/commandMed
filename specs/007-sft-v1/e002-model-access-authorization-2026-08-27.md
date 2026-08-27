# E002 Model / Weight Access Authorization — 2026-08-27

**Spec:** 007 SFT V1
**Task:** E002
**Decision owner:** Founder
**Decision state:** AUTHORIZED_PENDING_CANONICAL_MERGE
**Canonical base:** `c097ff973ca8b00922a3ca78a794da87daf3a1f1`
**E001 freeze record:** `specs/007-sft-v1/e001-candidate-manifest-freeze-2026-08-27.md`
**Frozen manifest:** `specs/007-sft-v1/e001-proposed-candidate-manifest.json`
**Frozen manifest version:** `e001-mass-reach-v1`
**Frozen manifest canonical SHA-256:** `98d586500d12e7904bce199061c48d5ac50e9f66a372de034d9ecba4e2d3cc28`

## Decision

The Founder explicitly directed the project to continue after E001 became `CLOSED_CANONICAL`. For the current canonical frontier, that direction is interpreted narrowly as authorization of **E002 only**: public, ungated model/artifact access required to prepare the already frozen tournament candidate set.

```text
E002_AUTHORITY=AUTHORIZED
MODEL_WEIGHT_ACCESS_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
MODEL_ARTIFACT_METADATA_ACCESS_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
MODEL_WEIGHT_DOWNLOAD_WITHOUT_EXECUTION=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
E003_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
BACKBONE_WINNER=NEEDS_EVIDENCE
```

This record is an authority overlay. It **does not mutate** the frozen E001 manifest bytes or SHA-256. The `authority` object inside the E001 manifest records the pre-E002 state at freeze time and remains historical, identity-bearing evidence. Current authority is determined by this later E002 record plus the canonical task ledger and current repository authority summary.

## Authorized candidate scope

Access is limited to the exact frozen E001 candidate identities.

### PRIMARY

1. `Qwen/Qwen3-0.6B-Base`
   - immutable upstream revision: `da87bfb608c14b7cf20ba1ce41287e8de496c0cd`
   - upstream repository access state at E001: `PUBLIC_UNGATED`
2. `Qwen/Qwen3.5-0.8B-Base`
   - immutable upstream revision: `dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`
   - upstream repository access state at E001: `PUBLIC_UNGATED`
3. `ibm-granite/granite-4.0-350m-base`
   - immutable upstream revision: `a50b46cef21c8a86b15f0496cb794487a78a910b`
   - upstream repository access state at E001: `PUBLIC_UNGATED`

### CONTROL

1. `Qwen/Qwen3-4B-Base`
   - immutable upstream revision: `906bfd4b4dc7f14ee4320094d8b41684abff8539`
   - upstream repository access state at E001: `PUBLIC_UNGATED`
   - `winner_eligible=NO`
   - purpose: `SCALE_QUALITY_OPPORTUNITY_COST`

No other model family, fallback, checkpoint revision, gated repository, private artifact, or credentialed model source is authorized by E002.

## Permitted access actions

E002 permits only non-executing artifact acquisition and integrity/provenance work for the exact scope above:

- fetch/download public source-model weight files present at the exact immutable candidate revisions listed above;
- fetch/download the exact tokenizer, config, special-token, processor, license, and repository metadata present at those same revisions;
- fetch only the explicitly enumerated preconverted artifacts in the deterministic allowlist below;
- calculate cryptographic hashes and byte sizes of downloaded artifacts without loading them as models;
- inspect static file/container metadata without executing repository-supplied code;
- store/cache those exact public artifacts in a local isolated evidence workspace for later separately authorized use.

### Deterministic preconverted-artifact allowlist

Only the following preconverted artifacts are authorized because the frozen E001 manifest binds their repository/revision locator, filename, exact byte size, and SHA-256. No other preconverted artifact is implied by prose evidence or repository adjacency.

1. Qwen3 0.6B exact-base derivative feasibility artifact
   - repository: `Antigma/Qwen3-0.6B-Base-GGUF`
   - immutable artifact revision: `f457544766bcdc72afd3514439eb3d422d4434dc`
   - filename: `qwen3-0.6b-base-q4_k_m.gguf`
   - bytes: `396704512`
   - SHA-256: `218d3f063193b40008d4e63d90cf83e7dc6d33a8c6c1c647589f868a8fc74492`
   - E001 state: `EXACT_BASE_DERIVATIVE_FEASIBILITY_ONLY_NOT_FINAL_RELEASE_BINDING`
2. Qwen3.5 0.8B official Q4_0 text/Core artifact
   - repository: `ggml-org/Qwen3.5-0.8B-Base-GGUF`
   - immutable artifact revision: `1bd44f68963429437d08bc12f465716eb31ba6e5`
   - filename: `Qwen3.5-0.8B-Base-Q4_0.gguf`
   - bytes: `563035840`
   - SHA-256: `0dabf7f08793293d999ea306cee8c9caa3d76099e791ea2b0ce8f555f4e4098d`
   - E001 state: `DIRECT_DIGEST_PUBLIC_METADATA`

```text
PRECONVERTED_ARTIFACT_ALLOWLIST_COUNT=2
PRECONVERTED_ARTIFACTS_NOT_EXPLICITLY_LISTED=UNAUTHORIZED
```

The Granite Q4_K_M feasibility artifact remains **unauthorized for E002 byte acquisition** because the frozen E001 manifest records a public size display rather than an exact byte count. The CONTROL has no preconverted artifact binding in the frozen manifest. Either case requires a later explicit complete binding before acquisition.

This access permission does not make any preconverted artifact the canonical tournament runtime artifact merely because its bytes were fetched. Existing E001 feasibility labels remain unchanged.

## Explicitly prohibited under E002

E002 does **not** authorize:

- importing/loading model weights into a model runtime;
- inference or generation;
- model conversion, quantization, requantization, merging, adapter application, or weight transformation;
- execution of `trust_remote_code` or arbitrary repository code;
- benchmark payload access or benchmark execution;
- tournament scoring, ranking, elimination, or winner selection;
- device performance execution;
- training, fine-tuning, gradient probes, CPT, distillation, RL, or optimization;
- Private Gold, PHI, restricted clinical database, or credential access;
- paid provider/API use, procurement, or spend;
- expanding PRIMARY or CONTROL membership.

If any required artifact becomes gated, credentialed, paywalled, license-conflicted, materially changed, or unavailable at the frozen identity, E002 fails closed for that artifact. This authorization does not permit substituting another revision or model.

## Static access invariants

```text
PUBLIC_UNGATED_ONLY=ENFORCED
IMMUTABLE_FROZEN_CANDIDATE_REVISIONS_ONLY=ENFORCED
PRECONVERTED_EXACT_ALLOWLIST_ONLY=ENFORCED
NO_REMOTE_CODE_EXECUTION=ENFORCED
NO_MODEL_LOAD=ENFORCED
NO_MODEL_CONVERSION=ENFORCED
NO_BENCHMARK_PAYLOAD=ENFORCED
NO_TOURNAMENT_EXECUTION=ENFORCED
NO_DEVICE_EXECUTION=ENFORCED
NO_TRAINING=ENFORCED
NO_CREDENTIALS=ENFORCED
NO_SPEND=ENFORCED
```

## Benchmark-contamination boundary

E002 changes only model/artifact access. It does not resolve benchmark contamination and does not authorize benchmark bytes.

```text
PRIMARY_BENCHMARK_SELECTION_ELIGIBILITY=INCOMPLETE
BENCHMARK_CONTAMINATION_BLOCKS_SELECTION_USE_UNTIL_RESOLVED=YES
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
```

## Founder authorization evidence

After E001 was reported as `CLOSED_CANONICAL` with the next frontier explicitly identified as E002 `SEPARATE_AUTHORIZATION_REQUIRED`, the Founder responded on 2026-08-27:

> `go ahead`

That response is interpreted only as the separate E002 authorization described in this record. It is not interpreted as E003, tournament, benchmark, model-execution, conversion, device, training, credential, or spend authority.

## Exit Evidence

E002 may close only when all of the following are true on the same qualified authorization PR/head or are immutable upstream inputs already bound by E001:

| Exit criterion | Required evidence | Current state before canonical merge |
|---|---|---|
| Founder authorization exists | This record's bounded interpretation of the post-E001 `go ahead` | `PRESENT` |
| Frozen candidate scope is identity-bound | E001 manifest version `e001-mass-reach-v1`, SHA-256 `98d586500d12e7904bce199061c48d5ac50e9f66a372de034d9ecba4e2d3cc28`, exact PRIMARY+CONTROL revisions | `PRESENT` |
| Frozen E001 bytes remain unchanged | `specs/007-sft-v1/e001-proposed-candidate-manifest.json` remains blob-identical to the E001 freeze | `REQUIRED_AT_MERGE` |
| Preconverted access is deterministic | Exact allowlist above; every allowed entry has repository, immutable revision, filename, byte count, and SHA-256 | `PRESENT` |
| Current authority summary is reconciled | `specs/README.md` reports the bounded E002 model-weight access overlay and preserves E003/execution/benchmark/device/training/credential/spend as `NONE` | `REQUIRED_IN_THIS_PR` |
| E002 task ledger is reconciled | `specs/007-sft-v1/tasks.md` marks E002 complete and E003 separately gated | `PRESENT_IN_THIS_PR` |
| No downstream authority is smuggled in | Exact-head diff/review confirms E003 and all prohibited authorities remain `NONE` | `REQUIRED_AT_EXACT_HEAD` |
| Independent exact-head review has no material blocker | Fresh Qodo review, with CodeRabbit service-unavailable behavior recorded transparently if applicable | `REQUIRED_BEFORE_MERGE` |
| Changed scope remains documentation-only | PR diff contains authority/ledger/current-summary documentation only; no model/benchmark bytes, product code, runtime, credentials, device or training surface | `REQUIRED_BEFORE_MERGE` |

`NEEDS_EVIDENCE`, a pending review, or an unresolved material finding is not a closure PASS.

## Closure condition

On canonical merge of an exact-head-qualified version of this authorization record with the Spec 007 task ledger and current repository authority summary reconciled:

```text
E002=CLOSED_CANONICAL
MODEL_WEIGHT_ACCESS_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
NEXT_TASK=E003
NEXT_TASK_STATE=SEPARATE_AUTHORIZATION_REQUIRED
```

No work requiring E003 or later authority is authorized by E002 closure.
