# commandMed Software License Implementation — 2026-09-08

**Authority:** `FOUNDER_COMMANDMED_SOFTWARE_LICENSE_DECISION=COMMANDMED_SOFTWARE_LICENSE_DECISION_B`  
**Authority record:** `docs/governance/software-license-founder-decision-2026-09-08.md`  
**Implementation class:** review-first repository governance  
**CommandMed-owned software license:** Apache-2.0  
**Donor-code admission effect:** NONE  
**Model / tournament / training effect:** NONE  
**Current authorized spend:** USD 0

## 1. Implemented surface

This change adds:

```text
LICENSE=Apache-2.0_STANDARD_TEXT
NOTICE=COMMANDMED_ROOT_NOTICE
THIRD_PARTY_NOTICES.md=THIRD_PARTY_ATTRIBUTION_REGISTRY_SCAFFOLD
```

It also updates repository-facing documentation to stop reporting the root software license as unresolved.

## 2. Scope

The root Apache-2.0 license applies to commandMed-owned software source unless a file or component states otherwise.

It does not silently relicense or automatically admit:

- donor or third-party source;
- model weights, tokenizer/model artifacts or runtimes with separate terms;
- datasets, evaluation payloads or benchmarks;
- papers, trademarks, logos or external documentation;
- Private Gold or PHI;
- any artifact with separate upstream obligations.

## 3. Donor provenance remains mandatory

Every future copied, adapted or vendored donor source still requires the source-admission process in `docs/governance/external-code-adoption.md`.

```text
SOURCE_USE_PERMISSION
!= LICENSE_COMPATIBILITY
!= FILE_LEVEL_PROVENANCE
!= SECURITY_QUALIFICATION
!= CANONICAL_ADMISSION
```

The root license is infrastructure for lawful, reviewable distribution. It is not a blanket donor-code import approval.

## 4. Current Tencent incorporation state

```text
Tencent/AI-Infra-Guard=REFERENCE_ONLY_NO_CODE_IMPORTED
Tencent/AICGSecEval=REFERENCE_ONLY_NO_CODE_IMPORTED
Tencent/hpc-ops=REFERENCE_ONLY_NO_CODE_IMPORTED
```

Their exact currently qualified revisions and upstream license classes are recorded in `THIRD_PARTY_NOTICES.md` for future admission work without misrepresenting them as incorporated components.

## 5. Non-expansion

```text
CURRENT_E004_AUTHORITY_EXPANSION=NONE
MODEL_EXECUTION_AUTHORITY_EXPANSION=NONE
TOURNAMENT_EXECUTION_AUTHORITY_EXPANSION=NONE
A15_AUTHORITY_EXPANSION=NONE
TRAINING_AUTHORITY=NONE
DONOR_CODE_AUTOMATIC_ADMISSION=NO
DONOR_DEPENDENCY_AUTOMATIC_ADMISSION=NO
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```
