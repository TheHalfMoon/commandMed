# E004 Successor-Scope Execution Authorization Founder Decision — 2026-09-02

**Spec:** 007 SFT V1  
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`  
**Successor policy:** `SP007-RO-001`  
**Canonical decision-request merge:** `80924a5036659a336458c05011a8eabc832600b3`  
**Canonical base for this decision record:** `cb97488e59ea778a1c09af0d8412f973f2015071`  
**Decision owner:** Founder  
**Decision class:** `E004_SUCCESSOR_EXECUTION_DECISION_B`  
**Decision state:** SELECTED  
**Model execution performed by this decision record:** NO  
**Tournament execution performed by this decision record:** NO  
**Training performed:** NO  
**Spend:** USD 0

## 1. Operative Founder decision

After the canonical decision surface was merged, the Founder supplied the exact required decision text:

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
```

This is the exact Decision B token defined by:

`specs/007-sft-v1/e004-successor-scope-execution-authorization-decision-request-2026-09-02.md`

Therefore the successor-scope execution-authority state becomes:

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
SUCCESSOR_SCOPE_MODEL_EXECUTION_AUTHORITY=AUTHORIZED_E001_FROZEN_CANDIDATES_ONLY_AFTER_PASS_PREFLIGHT
SUCCESSOR_SCOPE_TOURNAMENT_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_FROZEN_NONCLINICAL_PROTOCOL_ONLY_AFTER_PASS_PREFLIGHT
SUCCESSOR_SCOPE_DEVICE_EXECUTION_AUTHORITY=AUTHORIZED_ONLY_WHERE_REQUIRED_BY_EXACT_FROZEN_COMPONENT_QUALIFICATION_AFTER_PASS_PREFLIGHT
CURRENT_AUTHORIZED_SPEND_USD=0
```

Decision B removes only the missing successor-scope execution-authority blocker for an exact subject that has already satisfied every applicable preflight gate. It does not itself make any other gate PASS.

## 2. Frozen candidate boundary

This decision remains limited to the already-frozen E001 candidate identities inherited by the canonical decision surface.

### PRIMARY

```text
Qwen/Qwen3-0.6B-Base@da87bfb608c14b7cf20ba1ce41287e8de496c0cd
Qwen/Qwen3.5-0.8B-Base@dc7cdfe2ee4154fa7e30f5b51ca41bfa40174e68
ibm-granite/granite-4.0-350m-base@a50b46cef21c8a86b15f0496cb794487a78a910b
```

### CONTROL

```text
Qwen/Qwen3-4B-Base@906bfd4b4dc7f14ee4320094d8b41684abff8539
CONTROL_WINNER_ELIGIBLE=NO
CONTROL_PURPOSE=SCALE_QUALITY_OPPORTUNITY_COST
```

No candidate or revision is added or substituted by this decision.

## 3. Exact execution effect

Only after an exact PASS preflight for the exact successor subject, Decision B permits evidence-producing execution needed by the frozen non-clinical research-engineering component protocol, including as applicable:

- loading an already E002-authorized exact frozen candidate artifact whose identity is bound before use;
- model inference required by the frozen `SP007-RO-001` qualification protocol;
- execution of the exact seven identity-bound research-component policy/sentinel fixtures;
- execution of public/ungated non-clinical evaluation assets whose exact provenance, license, quarantine, split, scope-purpose, and contamination prerequisites have already passed;
- capture of raw outputs and deterministic evaluator records required by the component evidence pack;
- computation of the frozen non-clinical component metrics and guard dispositions;
- exact zero-spend device/runtime qualification only where required by the frozen component protocol and separately bound resource preflight;
- production of immutable identity-bound component evidence records.

No favorable scientific result is authorized or presumed. A failed gate or failed metric remains a hard fail under the controlling contracts.

## 4. Non-clinical claim boundary

The scope remains exactly:

```text
SUCCESSOR_SCOPE_ID=SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1
SUCCESSOR_SCOPE_CLAIM_CLASS=NON_CLINICAL_RESEARCH_ENGINEERING_ONLY
ADMITTED_ROLE_CLASSES=LEARNER_RESEARCHER
PATIENT_CAREGIVER_ROLE_ADMITTED=NO
CLINICAL_PROFESSIONAL_ROLE_ADMITTED=NO
COMPONENT_EXTERNAL_CLINICAL_REVIEW_REQUIRED=NO
COMPONENT_EXTERNAL_STATISTICAL_REVIEW_REQUIRED=NO
```

Decision B cannot establish patient-facing, clinical-professional, clinical-grade, clinical-safety, deployment, release, or patient-benefit claims.

## 5. Conversion remains unauthorized

Decision B does not authorize any weight transformation.

```text
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
QUANTIZATION_AUTHORITY=NONE
REQUANTIZATION_AUTHORITY=NONE
MERGE_OR_ADAPTER_APPLICATION_AUTHORITY=NONE
```

If an exact E002-authorized artifact cannot execute without conversion or another weight transformation, that path remains blocked pending a separate exact conversion authority and all of its prerequisites.

## 6. Data admission and contamination remain unauthorized

Decision B creates no data-download, data-admission, privacy-screening, or contamination-assessment authority.

```text
DATA_DOWNLOAD_AUTHORITY_CREATED_BY_DECISION_B=NONE
DATA_ADMISSION_AUTHORITY_CREATED_BY_DECISION_B=NONE
PRIVACY_PII_PHI_SCREENING_AUTHORITY_CREATED_BY_DECISION_B=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY_CREATED_BY_DECISION_B=NONE
CONTAMINATION_EVIDENCE_CREATED_BY_DECISION_B=NO
```

The public source due-diligence pins already canonical in PR #182 remain metadata evidence only. They are not admitted content identities and cannot be silently promoted into a DatasetSnapshot, CurriculumRecord, license PASS, privacy PASS, quarantine PASS, contamination PASS, or content-scope PASS.

## 7. Training remains unauthorized

```text
TRAINING_AUTHORITY=NONE
SFT_AUTHORITY=NONE
CPT_AUTHORITY=NONE
LORA_QLORA_AUTHORITY=NONE
DISTILLATION_AUTHORITY=NONE
DPO_RL_GRPO_AUTHORITY=NONE
QAT_AUTHORITY=NONE
```

Any gradient-bearing run requires a separately explicit training authority bound to the exact RunManifest after every applicable prerequisite is PASS.

## 8. Protected, gated, credentialed, and paid resources remain unauthorized

```text
PRIVATE_GOLD_ACCESS_AUTHORITY=NONE
PHI_ACCESS_AUTHORITY=NONE
GATED_ASSET_ACCESS_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
EXTERNAL_CLINICAL_DATABASE_ACCESS_AUTHORITY=NONE
PROVIDER_API_GENERATION_AUTHORITY=NONE
PROCUREMENT_AUTHORITY=NONE
PAYMENT_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Any action requiring credentials, gated assets, paid compute, paid providers, procurement, reimbursement, contracts, or incremental spend remains outside this authority.

## 9. Mandatory preflight remains fail closed

Decision B is necessary but not sufficient for execution.

Before first model execution under the successor scope, the exact subject must satisfy every applicable controlling requirement, including as applicable:

- exact successor scope identity and scope-binding hash;
- exact E001/E002 candidate and artifact identity;
- exact non-clinical evaluation/guard asset identities;
- source/license/provenance PASS;
- privacy/non-PHI evidence where applicable;
- quarantine PASS;
- contamination PASS for every selection-bearing input;
- exact frozen evaluation protocol;
- exact runtime/environment/device identity;
- exact finance/resource/access bindings;
- exact component guard-snapshot evidence required at the relevant transition;
- A1-A14-equivalent applicable PASS snapshot;
- separately authorized A15 activation if required by the controlling execution contract;
- this exact successor execution authority identity.

No Founder authorization converts failed, absent, stale, mismatched, or incomplete evidence into PASS.

## 10. Current state immediately after Decision B capture

At the canonical base of this record, the repository does not yet contain the exact real component bundle required to execute.

Therefore this decision changes the authority field but does not complete E004:

```text
FOUNDER_SUCCESSOR_EXECUTION_DECISION=E004_SUCCESSOR_EXECUTION_DECISION_B
SUCCESSOR_SCOPE_EXECUTION_AUTHORITY=AUTHORIZED_SP007_RO_001_EVIDENCE_ONLY
LIVE_COMPONENT_EXACT_RUN_MANIFEST=ABSENT
LIVE_COMPONENT_DATASET_SNAPSHOT=ABSENT
LIVE_COMPONENT_SCOPE_BINDING=ABSENT
LIVE_COMPONENT_CONTENT_SCOPE_VERIFICATIONS=ABSENT
LIVE_COMPONENT_SENTINEL_FIXTURE_SET=ABSENT
LIVE_COMPONENT_GUARD_SNAPSHOT_PASS=ABSENT
LIVE_COMPONENT_RESOURCE_FINANCE_BINDINGS=INCOMPLETE
LIVE_COMPONENT_ACCESS_BINDINGS=INCOMPLETE
CONTAMINATION_EVIDENCE=INCOMPLETE
MODEL_CONVERSION_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
PROJECT_FINISHED=NO
```

## 11. Relationship to generic continuation approval

The Founder's accompanying generic continuation/ordinary-approval language is preserved as project intent but is not used to manufacture any separately required authority not represented by the exact Decision B token above.

This record therefore does not infer data admission, contamination assessment, model conversion, A15 activation, training, protected-data access, credential use, procurement, payment, spend, or any other separately gated authority.

## 12. Repository qualification

Under FD-007 / constitutional amendment 0.1.1, independent repository review is not required by default for this bounded Founder-decision capture artifact.

Before merge, verify exact base/head/diff, applicable CI/status checks, unresolved review threads, mergeability, branch/ruleset state, exact Decision B correspondence with the canonical decision surface, and absence of later canonical invalidation. Merge only with an exact expected-head guard.
