# E001 Candidate Manifest Freeze — 2026-08-27

**Spec:** 007 SFT V1
**Task:** E001
**Decision owner:** Founder + ChatGPT
**Decision state:** FROZEN
**Evidence merge base:** `1af0e05bf5e04eb3b75b39e170e4ec2b31d08cd5` (PR #55)

## Decision

Founder + ChatGPT freeze the exact E001 candidate manifest already qualified in PR #55.

```text
CANDIDATE_MANIFEST_FROZEN=YES
MANIFEST_VERSION=e001-mass-reach-v1
MANIFEST_CANONICAL_SHA256=98d586500d12e7904bce199061c48d5ac50e9f66a372de034d9ecba4e2d3cc28
MANIFEST_PATH=specs/007-sft-v1/e001-proposed-candidate-manifest.json
QUARANTINE_MATRIX_IDENTITY=b59fd86a7f63c8de7058a0386f57de1cadc7c817edfa1e9e0aa392ca5219e080
```

The manifest bytes are not modified by this decision. The approved SHA-256 therefore continues to identify the exact previously reviewed manifest.

## Frozen candidate membership

### PRIMARY

1. `Qwen/Qwen3-0.6B-Base`
   - immutable upstream revision: `da87bfb608c14b7cf20ba1ce41287e8de496c0cd`
2. `Qwen/Qwen3.5-0.8B-Base`
   - immutable upstream revision: `dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`
3. `ibm-granite/granite-4.0-350m-base`
   - immutable upstream revision: `a50b46cef21c8a86b15f0496cb794487a78a910b`

### CONTROL

1. `Qwen/Qwen3-4B-Base`
   - immutable upstream revision: `906bfd4b4dc7f14ee4320094d8b41684abff8539`
   - `winner_eligible=NO`
   - purpose: `SCALE_QUALITY_OPPORTUNITY_COST`

No 2B/3B/4B fallback candidate is promoted into PRIMARY by this freeze.

## Frozen membership policies

```text
COMMON_CORE_PRIMARY_RANKING=ENFORCED
QUALITY_FLOOR_THEN_SIZE_FIRST=ENFORCED
BASE_ONLY_PRIMARY=ENFORCED
FULLY_ADMITTED_PRIMARY_ONLY=ENFORCED
SUB_700MB_MASS_REACH=ENFORCED
```

Core remains a capability/safety/product/resource contract, not a parameter-count label.

## Contamination boundary

This freeze preserves the accepted dual-axis semantics:

```text
PRIMARY_MODEL_LINEAGE_MEMBERSHIP_ADMISSION=ELIGIBLE
PRIMARY_BENCHMARK_SELECTION_ELIGIBILITY=INCOMPLETE
BENCHMARK_CONTAMINATION_DOES_NOT_BLOCK_E001_MEMBERSHIP_FREEZE=YES
BENCHMARK_CONTAMINATION_BLOCKS_SELECTION_USE_UNTIL_RESOLVED=YES
```

No benchmark slice is declared `ASSESSED_CLEAN` by this decision. Frozen candidate membership does not authorize use of an unresolved benchmark slice for ranking or selection.

## Explicit non-decisions

This decision does **not** select the backbone winner.

```text
BACKBONE_WINNER=NEEDS_EVIDENCE
```

This decision grants no downstream execution/access authority:

```text
E002_AUTHORITY=NONE
E003_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
TOURNAMENT_EXECUTION_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
```

E002 remains a separate authorization gate. E003 remains a separate authorization gate. Neither is implied by this freeze or by merge of this decision record.

## Founder decision evidence

On 2026-08-27, after presentation of the exact proposed manifest version, SHA-256, PRIMARY/CONTROL membership, quarantine identity, exact PR #55 qualification state, and the explicit statement that downstream authorities remain `NONE`, the Founder responded:

> `go ahead`

For this bounded decision, that response is interpreted only as explicit acceptance of the exact E001 manifest presented immediately before it. It is not interpreted as weight-access, benchmark-access, model-execution, tournament-execution, device, training, credential, or spend authorization.

ChatGPT decision position immediately before Founder acceptance was:

```text
CHATGPT_FREEZE_POSITION=READY_TO_FREEZE_AS_PROPOSED
```

Therefore the joint Founder+ChatGPT E001 decision is satisfied.

## Closure condition

On canonical merge of this exact decision record:

```text
E001=CLOSED_CANONICAL
CANDIDATE_MANIFEST_FROZEN=YES
NEXT_TASK=E002
NEXT_TASK_STATE=SEPARATE_AUTHORIZATION_REQUIRED
```

No work under E002 or E003 is authorized by E001 closure.
