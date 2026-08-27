# Spec 007 — SFT V1 Implementation Authorization

**Date:** 2026-08-27
**Lifecycle:** `AUTHORIZED_TO_START`
**Authorized scope:** offline deterministic Spec 007 control plane only
**Training authority:** NONE
**Model execution authority:** NONE

## Canonical planning evidence

```text
CANONICAL_PLANNING_PR=#51
CANONICAL_PLANNING_MERGE=947f3aba4d4316e21470ac26352d96e3bfb74ae6
CANONICAL_PLANNING_TREE=faa5c15c84dbd84d162b6ba6850bbc312584203b
QUALIFIED_PLANNING_HEAD=701c933acdf84572f627446e5199231236f97988
P013_VALIDATION_RUN=33040059680
P013_COMPILEALL=PASS
P013_PYTEST=627 passed + 128 subtests
P013_GIT_DIFF_CHECK=PASS
FINAL_QODO_REVIEW=MATERIAL_BLOCKER=NO
FINAL_CODERABBIT_REVIEW=MATERIAL_BLOCKER=NO
```

## Founder authorization

The Founder explicitly directed the project to proceed on 2026-08-27 after the planning package became canonical. This record interprets that direction narrowly and fail-closed: implementation may begin only for the I-phase offline deterministic control plane described by the canonical Spec 007 task graph.

```text
SPEC007_IMPLEMENTATION_AUTHORITY=AUTHORIZED_TO_START
AUTHORIZED_IMPLEMENTATION_TASKS=I001-I045
AUTHORIZED_SCOPE=OFFLINE_DETERMINISTIC_SPEC007_CONTROL_PLANE_ONLY
```

## Permitted implementation

Permitted work includes only repository-local deterministic validators, canonical identity/serialization, strict record parsing, synthetic fixtures, provenance/quarantine composition, rendering/loss/packing contracts, language/Arabic evidence packet validation, selection-policy enforcement, reproducibility/resume records, resource/efficiency/failure contracts, non-executing run-manifest composition, activation preflight, and offline tests/review qualification.

Implementation must prefer existing repository mechanisms and stdlib/native facilities over new frameworks or services. No network, credentials, model runtime, benchmark payload, PHI, Private Gold, device execution, or paid service is required or permitted.

## Explicitly not authorized

```text
MODEL_CANDIDATE_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
BACKBONE_WINNER_SELECTION_AUTHORITY=FOUNDER+CHATGPT_ONLY
PI_MODEL_SELECTION_AUTHORITY=NONE
BACKBONE_WINNER=NEEDS_EVIDENCE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
BENCHMARK_PAYLOAD_ACCESS_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
DEVICE_EXECUTION_AUTHORITY=NONE
EXTERNAL_CLINICAL_DATABASE_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

`E001-E015` are not activated by this record. No candidate model may be selected, ranked, eliminated, recommended as canonical, downloaded, loaded, converted, inferred, benchmarked, trained, fine-tuned, or used in a pilot under this authority.

## Exit discipline

Before implementation merge, the exact implementation head must satisfy the canonical I-phase task/evidence map, focused Spec 007 tests, full offline regression, compileall, diff-check, and fresh independent exact-head review with no unresolved material blocker. Any head movement invalidates prior exact-head qualification.
