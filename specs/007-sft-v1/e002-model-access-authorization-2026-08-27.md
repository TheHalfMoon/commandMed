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

This record is an authority overlay. It **does not mutate** the frozen E001 manifest bytes or SHA-256. The `authority` object inside the E001 manifest records the pre-E002 state at freeze time and remains historical, identity-bearing evidence. Current authority is determined by this later E002 record plus the canonical task ledger.

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

- fetch/download public model weight files at the immutable candidate revisions;
- fetch/download the exact tokenizer, config, special-token, processor, license, and repository metadata required to bind those revisions;
- fetch already-public preconverted artifacts that are already explicitly referenced by the frozen E001 manifest/evidence, solely for byte acquisition, digest/size verification, and later separately authorized tournament preparation;
- calculate cryptographic hashes and byte sizes of downloaded artifacts without loading them as models;
- inspect static file/container metadata without executing repository-supplied code;
- store/cache those exact public artifacts in a local isolated evidence workspace for later separately authorized use.

This access permission does not make any preconverted artifact the canonical tournament runtime artifact merely because its bytes were fetched. Existing E001 feasibility labels remain unchanged, including `EXACT_BASE_DERIVATIVE_FEASIBILITY_ONLY_NOT_FINAL_RELEASE_BINDING` where applicable.

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

## Closure condition

On canonical merge of this exact authorization record with the Spec 007 task ledger reconciled:

```text
E002=CLOSED_CANONICAL
MODEL_WEIGHT_ACCESS_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
NEXT_TASK=E003
NEXT_TASK_STATE=SEPARATE_AUTHORIZATION_REQUIRED
```

No work requiring E003 or later authority is authorized by E002 closure.
