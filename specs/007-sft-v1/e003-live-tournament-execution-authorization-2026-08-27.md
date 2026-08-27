# E003 Live Tournament Execution Authorization — 2026-08-27

**Spec:** 007 SFT V1
**Task:** E003
**Decision owner:** Founder
**Decision state:** AUTHORIZED_PENDING_CANONICAL_MERGE
**Canonical base:** `065015f89cbae0cb8af860c2a181f4f1fb6b05ad`
**Canonical base tree:** `e490fb0b33c54badde6b6337b674b2add6882a6e`
**E001 freeze record:** `specs/007-sft-v1/e001-candidate-manifest-freeze-2026-08-27.md`
**Frozen manifest:** `specs/007-sft-v1/e001-proposed-candidate-manifest.json`
**Frozen manifest version:** `e001-mass-reach-v1`
**Frozen manifest canonical SHA-256:** `98d586500d12e7904bce199061c48d5ac50e9f66a372de034d9ecba4e2d3cc28`
**Frozen manifest Git blob:** `f81e42ad1cb138f741cd730cda34ffcf49e77824`
**E002 canonical closure:** `065015f89cbae0cb8af860c2a181f4f1fb6b05ad`
**E002 authority record:** `specs/007-sft-v1/e002-model-access-authorization-2026-08-27.md`

## Decision

After E002 became `CLOSED_CANONICAL`, the Founder explicitly directed the project to continue from the separately gated E003 frontier. That direction is interpreted narrowly as authorization of **E003 only**: live execution of the already frozen base-model tournament under the repository's pre-existing Spec 004/005/007 protocols and fail-closed activation controls.

```text
E003_AUTHORITY=AUTHORIZED
MODEL_WEIGHT_ACCESS_AUTHORITY=AUTHORIZED_E002_FROZEN_PUBLIC_CANDIDATES_ONLY
MODEL_EXECUTION_AUTHORITY=AUTHORIZED_E003_FROZEN_TOURNAMENT_ONLY
TOURNAMENT_EXECUTION_AUTHORITY=AUTHORIZED_E003_FROZEN_PROTOCOL_ONLY
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_E003_A15_BOUND_PUBLIC_TOURNAMENT_INPUTS_ONLY
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=AUTHORIZED_E003_A15_BOUND_PUBLIC_TOURNAMENT_INPUTS_ONLY
DEVICE_EXECUTION_AUTHORITY=AUTHORIZED_E003_FROZEN_TOURNAMENT_QUALIFICATION_ONLY
E004_AUTHORITY=AUTHORIZED_BY_E003_SUBJECT_TO_PREFLIGHT
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
EXTERNAL_CLINICAL_DATABASE_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
BACKBONE_WINNER=NEEDS_EVIDENCE
```

This is an authority overlay. It does not rewrite E001 or E002 historical authority snapshots and does not change the frozen candidate manifest.

## Authorized candidate scope

Live model execution is limited to the exact E001 frozen candidate identities and immutable upstream revisions:

### PRIMARY

1. `Qwen/Qwen3-0.6B-Base`
   - revision `da87bfb608c14b7cf20ba1ce41287e8de496c0cd`
2. `Qwen/Qwen3.5-0.8B-Base`
   - revision `dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`
3. `ibm-granite/granite-4.0-350m-base`
   - revision `a50b46cef21c8a86b15f0496cb794487a78a910b`

### CONTROL

1. `Qwen/Qwen3-4B-Base`
   - revision `906bfd4b4dc7f14ee4320094d8b41684abff8539`
   - `winner_eligible=NO`
   - purpose `SCALE_QUALITY_OPPORTUNITY_COST`

No additional candidate, alternate revision, gated checkpoint, fallback model, provider-hosted substitute, or unbound model artifact is authorized.

## Artifact execution boundary

E003 may load and execute only model artifacts whose acquisition is already permitted by E002 and whose identity can be bound to the frozen candidate revision before execution.

For preconverted artifacts, E003 inherits the deterministic E002 allowlist exactly. It does not authorize additional conversion, quantization, requantization, merging, adapter application, or artifact substitution.

If an execution artifact cannot be proven to correspond to the frozen candidate identity, execution fails closed.

## Benchmark payload boundary

E003 does not grant broad benchmark access. A benchmark/evaluation payload may be accessed or executed only when all of the following are true before first payload access:

1. it is public and ungated;
2. its exact source/revision/content identity is bound in the qualified tournament/A15 evidence;
3. its license/provenance status is valid under Spec 003;
4. its intended tournament purpose is explicitly allowed by the canonical quarantine matrix;
5. its contamination state is resolved sufficiently for that purpose;
6. it is not Private Gold, PHI, a restricted clinical database, a credentialed source, or protected final evidence whose policy forbids tournament/model-selection use.

```text
UNBOUND_BENCHMARK_PAYLOAD=UNAUTHORIZED
GATED_BENCHMARK_PAYLOAD=UNAUTHORIZED
PRIVATE_GOLD_PAYLOAD=UNAUTHORIZED
PHI_PAYLOAD=UNAUTHORIZED
CREDENTIAL_REQUIRED_PAYLOAD=UNAUTHORIZED
CONTAMINATION_UNRESOLVED_SELECTION_INPUT=UNAUTHORIZED_FOR_SELECTION_EXECUTION
```

A payload with unresolved contamination may not be executed as selection-bearing tournament evidence. E003 does not convert `PRIMARY_BENCHMARK_SELECTION_ELIGIBILITY=INCOMPLETE` into PASS.

## A15 / preflight boundary

E003 is necessary but not sufficient to execute E004. Before a real model call, benchmark payload access, or device-qualification run, the executor must produce and validate the pre-existing Spec 005 A15 activation/pre-execution state for the exact run.

The preflight must bind current, non-stale evidence for every prerequisite required by the canonical Spec 004/005/007 control plane, including as applicable:

- the exact E001 manifest identity;
- E002 artifact-access authority and exact artifact identity;
- this E003 execution authority identity;
- exact candidate/model artifact binding;
- exact benchmark/evaluation payload identities;
- Spec 003 provenance/license/contamination disposition;
- frozen metrics/evaluation protocol identities;
- required scientific/statistical identities;
- access-state identities;
- finance state proving no unauthorized spend;
- runtime/build/environment identity;
- device/runtime qualification protocol identity where the tournament requires device evidence;
- quarantine and selection-purpose authorization.

Any `BLOCKED`, `INCOMPLETE`, `NEEDS_EVIDENCE`, stale, mismatched, or unauthorized prerequisite fails closed. Founder authorization does not override a failed scientific, provenance, quarantine, access, finance, runtime, or safety preflight.

## Permitted E003/E004 actions after canonical closure and PASS preflight

Within the exact scope above, E003 permits E004 to:

- load an E002-authorized frozen candidate artifact into a bound local runtime;
- run inference required by the frozen tournament protocol;
- access and execute exact public/ungated benchmark payloads that pass the benchmark boundary above;
- execute the frozen tournament device/runtime qualification protocol where required for candidate comparison;
- capture raw model outputs and deterministic evaluator inputs/outputs required by the evidence pack;
- compute the frozen metrics and hard-gate dispositions;
- produce immutable provenance-bound tournament evidence records;
- compare candidates under the pre-registered protocol without autonomously choosing the final backbone.

The evidence pack may report `PASS`, `FAIL`, `DISQUALIFIED`, `INCOMPLETE`, `NO_SELECTION`, or equivalent states only where the frozen protocol supports them. Missing evidence must not be converted into a favorable result.

## Exclusions

E003 does **not** authorize:

- E005 Founder+ChatGPT backbone selection or binding;
- declaring any PRIMARY candidate the winner before E005;
- changing PRIMARY/CONTROL membership or revisions;
- changing the frozen tournament protocol after seeing results;
- model conversion, quantization, requantization, merging, adapter application, or weight transformation;
- training, fine-tuning, gradient probes, CPT, LoRA/QLoRA, distillation, DPO, RL, QAT, or any optimization;
- using tournament outputs as training data;
- Private Gold or PHI access;
- restricted clinical database access;
- credentialed/gated assets;
- provider API generation;
- paid compute, paid APIs, procurement, reimbursement, contracting, or any other spend;
- execution on a substituted candidate/runtime merely because the frozen artifact is unavailable;
- using contamination-unresolved evidence for selection/ranking;
- weakening a hard safety, provenance, quarantine, or access gate;
- claiming SOTA, clinical superiority, release readiness, or medical equivalence from tournament execution.

## Spend and compute boundary

E003 permits execution only on resources that require no new financial authorization.

```text
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PAID_COMPUTE=UNAUTHORIZED
PAID_PROVIDER_API=UNAUTHORIZED
```

If the frozen protocol cannot be completed with already available zero-spend resources, E004 must stop and report the finance/resource blocker rather than incur cost.

## Result-use boundary

Tournament execution is evidence generation, not an automatic model-selection decision.

```text
E004_PRODUCES=TOURNAMENT_EVIDENCE_PACK
E004_MAY_AUTOMATICALLY_SELECT_BACKBONE=NO
E005_OWNER=FOUNDER+CHATGPT
BACKBONE_WINNER=NEEDS_EVIDENCE
```

The CONTROL remains `winner_eligible=NO`. PRIMARY ranking evidence must remain traceable to the frozen protocol and only contamination-eligible sources.

## Founder authorization evidence

After canonical E002 closure was reported with E003 explicitly identified as `SEPARATE_AUTHORIZATION_REQUIRED`, the Founder responded on 2026-08-27:

> `go ahead`

That response is interpreted only as the E003 authorization described here. It does not authorize E005 winner selection, training, conversion, Private Gold/PHI, credentials, gated assets, provider generation, or spend.

## Exit Evidence

E003 may close canonically only when all of the following are true on the same qualified authorization head:

| Exit criterion | Required evidence | State before canonical merge |
|---|---|---|
| Founder separately authorized E003 | This record binds the post-E002 `go ahead` to E003 only | `PRESENT` |
| E001 identity remains frozen | Manifest version/SHA/blob above remain unchanged | `REQUIRED_AT_EXACT_HEAD` |
| E002 remains bounded and canonical | E002 authority record remains `CLOSED_CANONICAL` and unchanged in meaning | `REQUIRED_AT_EXACT_HEAD` |
| Candidate execution scope is exact | Four frozen candidates/revisions enumerated above | `PRESENT` |
| Benchmark access is fail-closed | Exact A15-bound public/ungated/provenance/contamination conditions above | `PRESENT` |
| Downstream exclusions remain explicit | E005/training/conversion/Private Gold/PHI/credential/gated/spend remain unauthorized | `PRESENT` |
| Repository current-state authority summary is reconciled | `specs/README.md` reflects E003 while preserving exclusions | `REQUIRED_IN_THIS_PR` |
| Phase E ledger is reconciled | `tasks.md` closes E003 and leaves E004 as execution work | `REQUIRED_IN_THIS_PR` |
| No execution happened before canonical authorization | PR diff/evidence contains documentation only; no model/benchmark/device execution evidence | `REQUIRED_AT_EXACT_HEAD` |
| Independent exact-head review has no material blocker | Fresh review on the final authorization head | `REQUIRED_BEFORE_MERGE` |

No review silence, pending CI, or unverified preflight is a PASS.

## Closure condition

On canonical merge of an exact-head-qualified version of this record with the current authority summary and Phase E ledger reconciled:

```text
E003=CLOSED_CANONICAL
MODEL_EXECUTION_AUTHORITY=AUTHORIZED_E003_FROZEN_TOURNAMENT_ONLY
TOURNAMENT_EXECUTION_AUTHORITY=AUTHORIZED_E003_FROZEN_PROTOCOL_ONLY
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=AUTHORIZED_E003_A15_BOUND_PUBLIC_TOURNAMENT_INPUTS_ONLY
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=AUTHORIZED_E003_A15_BOUND_PUBLIC_TOURNAMENT_INPUTS_ONLY
DEVICE_EXECUTION_AUTHORITY=AUTHORIZED_E003_FROZEN_TOURNAMENT_QUALIFICATION_ONLY
NEXT_TASK=E004
NEXT_TASK_STATE=EXECUTION_REQUIRED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
```

E003 closure authorizes bounded E004 execution only after the existing fail-closed preflight passes. It does not itself claim that any tournament run has occurred or that the repository is ready to select a winner.