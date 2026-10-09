# V5 bounded development execution authorization — 2026-10-03

**Program:** CommandMed paper rebuild V5
**Decision owner:** Founder
**Decision state:** `APPROVED`
**Authority class:** bounded development-only execution overlay
**Authority source:** Founder instruction in the CommandMed V5 continuation conversation on 2026-10-03
**Authoritative scope request:** `V5_DEVELOPMENT_EXECUTION_AUTHORITY_REQUEST.md`
**Request Git blob:** `ef5e2545c8bb79caca28f7311cac459b15738935`
**Request-bearing branch head before this transition:** `575aa5cc11083ea3cb3db04c23411e9422257071`
**Request-bearing tree:** `c0c96e33ddf4f05ce2daa86d557f821b9c4a91bb`
**Canonical main at authorization time:** `51f73ec05750137e5bd94ffa0765f6383f475fee`
**Active branch:** `research/commandmed-paper-first-principles`

## Founder decision

The Founder explicitly approved the bounded V5 development execution authority exactly as defined in `V5_DEVELOPMENT_EXECUTION_AUTHORITY_REQUEST.md`.

This record is an append-only authorization overlay. It does not rewrite the request's historical `REQUESTED_NOT_AUTHORIZED` state and does not broaden, reinterpret, or weaken any requirement in that request.

```text
V5_DEVELOPMENT_EXECUTION_AUTHORITY=APPROVED
MODEL_WEIGHT_ACCESS=QWEN_0_8B_PIN_ONLY
MODEL_LOAD=DEVELOPMENT_ONLY
MODEL_INFERENCE=DEVELOPMENT_CALIBRATION_ONLY
TRAINING=B1_C1_C2_DEVELOPMENT_ONLY
CONFIRMATORY_EXECUTION=NO
CONFIRMATORY_IDENTITY_MATERIALIZATION=NO
RESERVE_EXECUTION=NO
PAID_COMPUTE=NO
PAID_API=NO
PHI=NO
GATED_DATA=NO
SPEND_USD=0
AUTONOMOUS_PUBLICATION=NO
AUTONOMOUS_MERGE=NO
```

## Exact authorized model boundary

The only authorized model for this execution grain is:

- repository: `Qwen/Qwen3.5-0.8B-Base`
- revision: `dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68`

No alternate revision, quantized substitute, provider-hosted replacement, gated checkpoint, merged checkpoint, independent-family replication model, 27B model, Qwen-Image model, or HCF model path is authorized by this decision.

## Authorized data roles

Execution is limited to already-bound development/calibration assets and project-owned synthetic/mechanical fixtures whose exact provenance and rights status pass the V5 preflight:

- `RULE_ORACLE_DEVELOPMENT`;
- `RULE_ORACLE_CALIBRATION`;
- `SQUAD_RETENTION` only where required by `C2_CRDI_RETAIN_V1`;
- `SYNTHETIC_MECHANICAL` fixtures used to validate mechanics.

Confirmatory and reserve identities, Private Gold, PHI, restricted clinical databases, gated benchmarks, credential-required sources, and assets without exact provenance/rights admission remain forbidden.

## Authorized operations

Subject to a PASS fail-closed preflight for the exact run, the executor may:

1. acquire and integrity-bind the exact public 0.8B model artifact;
2. load it in a zero-cost local or genuinely free runtime;
3. perform smoke inference required to validate the frozen interface;
4. run development/calibration-only baseline measurements;
5. integrate and train `B1_TYPED_V1`, `C1_CRDI_V1`, and `C2_CRDI_RETAIN_V1` under the frozen objective contracts;
6. estimate development-only repeatability and nuisance quantities;
7. freeze property-specific meaningful margins `m_j`, power assumptions, and stop/kill rules from development evidence only;
8. produce immutable manifests, raw development outputs, and analysis artifacts.

Every executed run must bind the exact code SHA, model revision and artifact identity, data-role identity, environment identity, seed, configuration, raw output identity, and analysis identity.

## Fail-closed boundary

Founder authorization is necessary but not sufficient for a real model call. The first real model call remains blocked until the repository-defined V5 preflight records PASS for the exact run, including exact artifact identity, zero-spend runtime/resource status, admissible development/calibration roles, provenance/rights admission, frozen intervention/objective identity, code/environment identity, holdout quarantine, protected-data exclusions, and bounded evidence destination.

Any mismatch, stale prerequisite, missing identity, unauthorized resource/cost, confirmatory/reserve materialization, PHI/gated/private access, or output-boundary violation stops execution.

## Explicit exclusions preserved

This authorization does not permit:

- confirmatory or reserve-set execution;
- materializing confirmatory/reserve identities before the clean freeze event;
- SmolLM2 replication in this first execution grain;
- model merging, Qwen-Image, HCF, or 27B execution;
- provider APIs or paid compute/API usage;
- PHI, restricted/gated clinical data, credentials, or Private Gold;
- autonomous publication or merge;
- clinical-validity claims from deterministic rule conformance;
- `first`, `best`, `SOTA`, `safe`, `clinical-grade`, or `revolutionary` scientific claims.

## Current transition state

```text
FOUNDER_V5_AUTHORITY=APPROVED
PREFLIGHT_REQUIRED_BEFORE_FIRST_MODEL_CALL=YES
MODEL_ARTIFACT_ACQUIRED=NO_AT_AUTHORIZATION_TRANSITION
MODEL_LOADED=NO_AT_AUTHORIZATION_TRANSITION
MODEL_INFERENCE=NO_AT_AUTHORIZATION_TRANSITION
TRAINING=NO_AT_AUTHORIZATION_TRANSITION
CONFIRMATORY_FROZEN=NO
HCF_STATUS=DEFERRED_UNPROVEN
```

The next safe action is to qualify the exact zero-cost runtime and artifact identity, build the run manifest, and require `PREFLIGHT_PASS` before model load or inference.