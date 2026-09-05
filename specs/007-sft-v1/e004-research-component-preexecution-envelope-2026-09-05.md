# E004 Research-Component Tournament Pre-Execution Envelope — 2026-09-05

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical base at branch creation:** `c94e8f5e2e31993b902afb41115dc802ecc91195`  
**Artifact class:** deterministic non-executing pre-execution control plane  
**Corrective-maintenance authority:** `E004_CORRECTIVE_MAINTENANCE_AUTHORITY=AUTHORIZED` / CM-3  
**Execution authority effect:** NONE  
**Winner-selection effect:** NONE  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Adapt the already-authorized CM-3 identity-bound E004 execution-envelope concept to the canonical `SP007-RO-001` non-clinical backbone tournament without executing a model, opening a device, accessing a protected asset, selecting a winner, or creating new authority.

The frozen successor tournament already binds:

```text
SCOPE_ID=SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1
PROTOCOL_ID=SP007_RO_001_NONCLINICAL_BACKBONE_TOURNAMENT_V1
PROTOCOL_SHA256=1c6a3ff38be596396fbd3025b1317be88e4c2068feace167d8187d22830b5dd8
EVALUATION_ASSET_SET_SHA256=709d5f73c1599364fc184b959cbdfd199c7ec07307fef8f8091d8eafb10f5454
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
CURRENT_AUTHORIZED_SPEND_USD=0
```

The missing control-plane surface was an exact pre-execution subject that composes those frozen identities with real candidate artifact/runtime identities and the remaining operational gates before any external executor can receive a request.

## 2. Implementation

```text
IMPLEMENTATION=src/commandmed/spec007/research_execution.py
TESTS=tests/spec007/test_research_execution.py
```

The implementation validates only metadata and canonical identities. It imports no subprocess, network, model loader, device runtime, optimizer, or training mechanism.

A valid subject must bind:

1. the exact canonical `SP007-RO-001` scope, protocol, and evaluation asset-set identities;
2. the canonical successor execution-authority identities;
3. exactly the four frozen E001 candidates and immutable upstream revisions;
4. for every candidate, an exact model-artifact digest/size/format/access state;
5. for every candidate, an exact runtime binding authority, runtime executable digest, runtime source revision, tokenizer/config digest, executable entrypoint and argv, and explicit artifact/runtime compatibility PASS;
6. an exact A15 activation identity and PASS state;
7. exact resource and access binding identities and PASS states;
8. an exact execution-environment manifest identity;
9. zero authorized spend and explicit absence of credentials, gated assets, Private Gold, PHI, and winner selection.

The subject is self-addressed with a canonical SHA-256. Any mutation invalidates the identity.

## 3. Frozen candidate boundary

The validator accepts exactly:

```text
PRIMARY=Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
PRIMARY=Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
PRIMARY=ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
CONTROL=Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
CONTROL_WINNER_ELIGIBLE=NO
```

Candidate additions, substitutions, revision drift, role drift, duplicate identities, and control winner eligibility fail closed.

## 4. Runtime and artifact boundary

This control plane does not freeze or invent a runtime. It requires a future real subject to provide canonical runtime evidence.

```text
RUNTIME_BINDING_CREATED_BY_THIS_PR=NO
MODEL_ARTIFACT_BINDING_CREATED_BY_THIS_PR=NO
FORMAT_COMPATIBILITY_PASS_CREATED_BY_THIS_PR=NO
```

Accepted metadata format classes are limited to `GGUF` and `SAFETENSORS`. A format label is not sufficient: `runtime_format_compatibility_state=PASS` and the exact executable/source/tokenizer identities are independently required.

Shell entrypoints and credential-bearing runtime arguments are prohibited.

## 5. A15, resource, access, privacy, and finance gates

The envelope deliberately keeps these gates noncompensable:

```text
A15_STATE_REQUIRED=PASS
RESOURCE_STATE_REQUIRED=PASS
ACCESS_STATE_REQUIRED=PASS
AUTHORIZED_SPEND_USD_REQUIRED=0
CREDENTIALS_USED_REQUIRED=false
GATED_ASSETS_USED_REQUIRED=false
PRIVATE_GOLD_USED_REQUIRED=false
PHI_USED_REQUIRED=false
WINNER_SELECTION_PERFORMED_REQUIRED=false
```

The implementation cannot manufacture any corresponding real identity.

## 6. Execution behavior

A fully valid metadata subject may produce only:

```text
STATE=READY_FOR_EXTERNAL_EXECUTOR
EXECUTION_PERFORMED=false
```

Any validation error produces:

```text
STATE=BLOCKED
EXECUTION_PERFORMED=false
REQUEST=null
```

No executor is implemented by this unit.

## 7. Current live subject state

This repository unit closes only the missing successor-specific CM-3 control-plane representation. It does not change the live operational preflight result.

```text
LIVE_SP007_PREEXECUTION_SUBJECT=ABSENT
LIVE_FOUR_CANDIDATE_RUNTIME_BINDINGS=INCOMPLETE
LIVE_FOUR_CANDIDATE_EXECUTABLE_ARTIFACT_BINDINGS=INCOMPLETE
LIVE_RUNTIME_FORMAT_COMPATIBILITY_EVIDENCE=INCOMPLETE
LIVE_RESOURCE_BINDING=INCOMPLETE
LIVE_ACCESS_BINDING=INCOMPLETE
A15_ACTIVATION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
SUCCESSOR_PASS_PREFLIGHT=NO
MODEL_EXECUTION_PERFORMED=NO
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_PERFORMED=NO
PRIVATE_GOLD_ACCESSED=NO
PHI_ACCESSED=NO
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 8. Qualification boundary

Before merge, require the exact PR head to pass the applicable repository workflow with:

```text
EXACT_HEAD_CHECKOUT=PASS
BOUNDED_AUTHORITY_BIND=PASS
COMPILE=PASS
FOCUSED_PREEXECUTION_TESTS=PASS
SPEC007_REGRESSION=PASS
FULL_REPOSITORY_REGRESSION=PASS
DIFF_WHITESPACE=PASS
```

Independent repository review is optional by default under FD-007 unless a later exact bounded authority reintroduces it.

## 9. Successor frontier after canonical merge

After this envelope is canonical, the next dependency-safe work is evidence collection and exact binding for the operational subject, not model execution by inference.

The order is:

1. reconcile exact executable artifact availability for every frozen candidate under existing public/ungated/no-conversion authority;
2. bind an exact inference runtime and prove format compatibility for every candidate without credentials or spend;
3. bind exact resource and access evidence for the intended execution environment;
4. recompute the successor preflight including the still-separate A15 requirement;
5. execute the frozen tournament only if the complete exact subject genuinely passes every gate.

No E005 winner selection is performed by this unit or by the tournament evidence pack.
