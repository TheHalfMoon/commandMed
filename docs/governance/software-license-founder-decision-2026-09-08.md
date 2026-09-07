# commandMed Software License / Distribution Founder Decision — 2026-09-08

**Project:** `TheHalfMoon/commandMed`  
**Canonical decision request:** `docs/governance/software-license-founder-decision-request-2026-09-08.md`  
**Canonical predecessor main:** `df5d40be96d51cfeeb68804b0a6ef7888a7b1367`  
**Artifact class:** Founder decision capture  
**Decision owner:** Founder  
**Decision state before canonical merge:** CAPTURED_PENDING_CANONICAL_MERGE  
**Model / tournament / training effect:** NONE  
**Current authorized spend:** USD 0

## 1. Exact post-canonical Founder token

After the software-license decision request became canonical, the Founder separately supplied exactly:

```text
FOUNDER_COMMANDMED_SOFTWARE_LICENSE_DECISION=COMMANDMED_SOFTWARE_LICENSE_DECISION_B
```

Exact token SHA-256:

```text
FOUNDER_COMMANDMED_SOFTWARE_LICENSE_DECISION_TOKEN_SHA256=fcd2232f16fe224982f2e75191dfe369b9d75655fbbf8e4089e9251f034c6d9d
```

This is the operative Decision B token. It is not inferred from generic project approval, source-use permission, or any unrelated Founder decision.

## 2. Decision effect after canonical merge

Only after this decision record is canonically merged:

```text
FOUNDER_COMMANDMED_SOFTWARE_LICENSE_DECISION=COMMANDMED_SOFTWARE_LICENSE_DECISION_B
COMMANDMED_OWNED_SOFTWARE_LICENSE=Apache-2.0
ROOT_LICENSE_IMPLEMENTATION_PREPARATION_AUTHORITY=AUTHORIZED_REVIEW_FIRST
THIRD_PARTY_LICENSE_PRESERVATION=MANDATORY
DONOR_FILE_LEVEL_PROVENANCE=MANDATORY
NOTICE_AGGREGATION=MANDATORY_WHEN_APPLICABLE
DONOR_CODE_AUTOMATIC_ADMISSION=NO
DONOR_DEPENDENCY_AUTOMATIC_ADMISSION=NO
```

Decision B authorizes a separate review-first governance implementation that adds the standard Apache License 2.0 root license text and commandMed-native third-party/NOTICE scaffolding.

## 3. Scope boundary

The root Apache-2.0 posture applies only to commandMed-owned software source unless an artifact explicitly states otherwise.

It does not silently relicense or automatically admit:

- third-party donor source;
- model weights or tokenizer/model artifacts;
- datasets or benchmark payloads;
- Private Gold or PHI;
- publications, trademarks, logos or external documentation;
- generated artifacts with separate upstream obligations.

Every future copied, adapted or vendored donor file remains subject to `docs/governance/external-code-adoption.md`, including exact source revision/path/blob identity, applicable license and NOTICE preservation, security qualification, tests and attribution.

## 4. Current qualified donor license posture

```text
Tencent/AI-Infra-Guard@e4e622af3ad2b8228ce82dd62b01415dd8ce2b9c=Apache-2.0
Tencent/AICGSecEval@94428ebf45141bf4ecd365a51d596dcd51caa690=Apache-2.0
Tencent/hpc-ops@2a2e26562433a8ba4b504858f1c938eb7612c901=MIT_WITH_THIRD_PARTY_BSD_3_CLAUSE_COMPONENTS
```

Source-use permission remains separate from license/NOTICE/copyright/patent/third-party obligations.

## 5. Explicit non-expansion

```text
DONOR_CODE_AUTOMATIC_ADMISSION=NO
DONOR_DEPENDENCY_AUTOMATIC_ADMISSION=NO
CURRENT_E004_AUTHORITY_EXPANSION=NONE
MODEL_EXECUTION_AUTHORITY_EXPANSION=NONE
TOURNAMENT_EXECUTION_AUTHORITY_EXPANSION=NONE
A15_AUTHORITY_EXPANSION=NONE
TRAINING_AUTHORITY=NONE
PHI_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

The separate E004 operational-preflight decision remains governed by its own exact decision record.

## 6. Current disposition before canonical merge

```text
FOUNDER_COMMANDMED_SOFTWARE_LICENSE_DECISION=COMMANDMED_SOFTWARE_LICENSE_DECISION_B
POST_CANONICAL_EXACT_SOFTWARE_LICENSE_FOUNDER_DECISION_TOKEN=CAPTURED_PENDING_CANONICAL_MERGE
COMMANDMED_OWNED_SOFTWARE_LICENSE=PENDING_CANONICAL_DECISION_CAPTURE
ROOT_LICENSE_IMPLEMENTATION_PREPARATION_AUTHORITY=PENDING_CANONICAL_DECISION_CAPTURE
CANONICAL_REDISTRIBUTED_DONOR_CODE=BLOCKED_PENDING_SEPARATE_ADMISSION
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```
