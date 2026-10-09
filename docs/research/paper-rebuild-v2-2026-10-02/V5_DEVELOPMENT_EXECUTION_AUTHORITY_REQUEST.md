# V5 bounded development execution authority request

**Program:** CommandMed paper rebuild V5
**Decision owner:** Founder
**Decision state:** `REQUESTED_NOT_AUTHORIZED`
**Current branch:** `research/commandmed-paper-first-principles`
**Current attestation head:** `7ee460adb88919b5af88b81cb8194d95895ca067`
**Canonical base:** `51f73ec05750137e5bd94ffa0765f6383f475fee`

## Purpose

Request a narrow development-only execution boundary needed to qualify B1/C1/C2, estimate repeatability/nuisance quantities, and freeze property-specific meaningful margins and final power before any confirmatory execution.

This request does not authorize confirmatory evaluation, reserve-set access, paid resources, protected data, clinical deployment, or empirical paper claims.

## Requested authority state

```text
V5_DEVELOPMENT_EXECUTION_AUTHORITY=REQUESTED_NOT_AUTHORIZED
MODEL_WEIGHT_ACCESS=QWEN_0_8B_PIN_ONLY_IF_APPROVED
MODEL_LOAD=DEVELOPMENT_ONLY_IF_APPROVED
MODEL_INFERENCE=DEVELOPMENT_CALIBRATION_ONLY_IF_APPROVED
TRAINING=B1_C1_C2_DEVELOPMENT_ONLY_IF_APPROVED
CONFIRMATORY_EXECUTION=NO
CONFIRMATORY_IDENTITY_MATERIALIZATION=NO
RESERVE_EXECUTION=NO
PAID_COMPUTE=NO
PAID_API=NO
PHI=NO
GATED_DATA=NO
SPEND_USD=0
```
## Exact model boundary

Primary development model only:

- `Qwen/Qwen3.5-0.8B-Base`
- revision `dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`

The independent-family SmolLM2 candidate remains out of the first execution grain. It may receive a later separate authorization only after the primary-family development path is qualified.

No alternate revision, quantized substitute, provider-hosted replacement, gated checkpoint, merged checkpoint, or unbound artifact is authorized by this request.

## Permitted data boundary

If approved, execution is limited to already-bound development/calibration assets and project-owned synthetic/mechanical fixtures whose identities and rights status pass the V5 preflight.

Permitted roles may include:

- committed RULE_ORACLE development identities;
- committed RULE_ORACLE calibration identities;
- the narrow admitted SQuAD retention control where required by C2;
- project-owned unit/synthetic fixtures used to validate mechanics.

Forbidden roles include confirmatory and reserve identities, Private Gold, PHI, restricted clinical databases, gated benchmarks, credentials-required sources, and any asset without exact provenance/rights admission.
## Permitted actions after explicit approval

Within the exact boundary above, the executor may:

1. acquire and integrity-bind the exact public 0.8B model artifact;
2. load it in a zero-cost local or genuinely free runtime;
3. perform smoke inference required to validate the frozen interface;
4. run development/calibration-only baseline measurements;
5. integrate and train B1/C1/C2 under the frozen objective contracts;
6. estimate development-only repeatability/nuisance quantities;
7. freeze `m_j`, power assumptions, and stop/kill rules from development evidence only;
8. produce immutable manifests, raw development outputs, and analysis artifacts.

Every run must bind code SHA, model revision, data-role identity, environment, seed, configuration, raw output, and analysis identity.

## Explicit exclusions

Approval would not authorize:

- confirmatory or reserve-set execution;
- materializing future confirmatory/reserve identities before the clean freeze event;
- model merging or Qwen-Image/HCF work;
- 27B execution;
- provider APIs;
- paid cloud/GPU/API usage;
- PHI or restricted/gated clinical data;
- autonomous publication or merge;
- clinical-validity claims from rule conformance;
- `first`, `best`, `SOTA`, `safe`, `clinical-grade`, or `revolutionary` claims.
## Fail-closed preflight

Even after founder approval, the first real model call remains blocked until a run preflight records PASS for:

- exact approved model revision and artifact identity;
- zero-spend runtime/resource status;
- development/calibration-only role binding;
- data provenance/rights admission;
- frozen intervention/objective contract identity;
- code and environment identity;
- no confirmatory/reserve materialization;
- no PHI/gated/private asset access;
- output/evidence destination and privacy scan.

Any mismatch, missing identity, unauthorized cost, or stale prerequisite stops execution.

## Requested founder decision

A valid approval should be explicit, for example:

> I approve the V5 bounded development execution authority exactly as defined in `V5_DEVELOPMENT_EXECUTION_AUTHORITY_REQUEST.md`. This approval is limited to the pinned Qwen3.5-0.8B development/calibration path, B1/C1/C2 qualification, development-only repeatability/nuisance estimation, and freezing margins/power. Confirmatory/reserve execution, paid resources, PHI/gated data, HCF/Qwen-Image work, publication, and merge remain unauthorized.

Until such approval is received, the authority state remains `REQUESTED_NOT_AUTHORIZED` and no model weight access, load, inference, or training may occur under V5.
