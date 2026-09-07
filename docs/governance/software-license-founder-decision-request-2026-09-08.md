# commandMed Software License / Distribution Founder Decision Request — 2026-09-08

**Project:** `TheHalfMoon/commandMed`  
**Canonical base at authoring:** `d080a6ecfad8ced5285b0f9e3af75968c7c6e700`  
**Artifact class:** Founder decision request / governance planning  
**Authority effect before post-canonical exact Founder selection:** NONE  
**Implementation authority effect:** NONE  
**Donor-code admission effect before decision capture:** NONE  
**Model / tournament / training effect:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Resolve a repository-level software distribution posture before commandMed canonically redistributes copied or derivative donor code.

The Grand Master Plan already lists the intended open-weight/commercial licensing posture as an unresolved Founder-level decision. The Tencent-informed planning amendment and `docs/governance/external-code-adoption.md` make this decision operationally relevant because commandMed may later adopt code from Apache-2.0 and MIT sources.

This request does not itself add a root license, import donor code, change any current Spec 007 / E004 authority, or authorize release/model/training execution.

## 2. Current observed state

At the canonical base used for this request:

```text
COMMANDMED_ROOT_SOFTWARE_LICENSE=ABSENT
COMMANDMED_SOFTWARE_DISTRIBUTION_POSTURE=UNRESOLVED
CANONICAL_REDISTRIBUTED_DONOR_CODE=BLOCKED
```

Founder-supplied donor sources currently qualified for future use include:

```text
Tencent/AI-Infra-Guard@e4e622af3ad2b8228ce82dd62b01415dd8ce2b9c=Apache-2.0
Tencent/AICGSecEval@94428ebf45141bf4ecd365a51d596dcd51caa690=Apache-2.0
Tencent/hpc-ops@2a2e26562433a8ba4b504858f1c938eb7612c901=MIT_WITH_THIRD_PARTY_BSD_3_CLAUSE_COMPONENTS
```

The Founder has also stated that commandMed has permission to copy source code from supplied sources. That permission remains separate from preservation of license, NOTICE, copyright, patent, third-party and redistribution obligations.

## 3. Engineering recommendation

For the commandMed-owned **software source code** layer, the narrow engineering recommendation is Apache License 2.0.

Reasons:

1. two of the three newly qualified donor sources are already Apache-2.0;
2. Apache-2.0 provides an explicit patent grant and patent-termination mechanism that is useful for a public engineering project;
3. Apache-2.0 has an explicit NOTICE mechanism that aligns well with commandMed's planned file-level donor provenance and attribution governance;
4. MIT-licensed source can be incorporated while preserving its MIT copyright/license notice;
5. third-party components retain their own licenses and are never silently relicensed by a commandMed root license;
6. this choice does not determine future model-weight, dataset, benchmark, paper, trademark, or clinical-content licensing; those remain artifact-specific.

This is an engineering/governance recommendation, not legal advice.

## 4. Decision scope

This decision applies only to commandMed-owned repository software source unless an artifact explicitly states otherwise.

It does **not** automatically license:

- third-party donor files under a different license;
- model weights;
- tokenizer/model artifacts controlled by upstream model licenses;
- datasets or benchmark payloads;
- Private Gold;
- PHI;
- publications/papers;
- trademarks/logos;
- external documentation whose source license differs;
- generated artifacts carrying their own upstream obligations.

Every copied/adapted donor file still requires the source-admission record defined by `docs/governance/external-code-adoption.md`.

## 5. Founder choices

### Decision A — remain unlicensed for now

Exact token:

```text
FOUNDER_COMMANDMED_SOFTWARE_LICENSE_DECISION=COMMANDMED_SOFTWARE_LICENSE_DECISION_A
```

Effect after post-canonical exact capture:

```text
COMMANDMED_ROOT_SOFTWARE_LICENSE=ABSENT
CANONICAL_REDISTRIBUTED_DONOR_CODE=BLOCKED
REFERENCE_ONLY=ALLOWED
PATTERN_REIMPLEMENTATION_PLANNING=ALLOWED
```

No root software license would be added.

### Decision B — adopt Apache License 2.0 for commandMed-owned software source

Exact token:

```text
FOUNDER_COMMANDMED_SOFTWARE_LICENSE_DECISION=COMMANDMED_SOFTWARE_LICENSE_DECISION_B
```

Effect only after this decision request becomes canonical and the exact token is supplied separately and captured canonically:

```text
COMMANDMED_OWNED_SOFTWARE_LICENSE=Apache-2.0
ROOT_LICENSE_IMPLEMENTATION_PREPARATION_AUTHORITY=AUTHORIZED_REVIEW_FIRST
THIRD_PARTY_LICENSE_PRESERVATION=MANDATORY
DONOR_FILE_LEVEL_PROVENANCE=MANDATORY
NOTICE_AGGREGATION=MANDATORY_WHEN_APPLICABLE
DONOR_CODE_AUTOMATIC_ADMISSION=NO
DONOR_DEPENDENCY_AUTOMATIC_ADMISSION=NO
```

Decision B would authorize a separate review-first governance implementation that adds the standard Apache-2.0 root license text plus commandMed-native third-party/NOTICE scaffolding. It would **not** by itself authorize copying any donor file. Each donor-code adoption remains a separate bounded change with exact provenance, security qualification, tests, and license/NOTICE preservation.

## 6. Why MIT is not the primary recommended root choice

MIT is a valid permissive license, but it is not the recommended default here because the highest-priority donor source (`AI-Infra-Guard`) and the security-evaluation donor (`AICGSecEval`) are Apache-2.0. Choosing Apache-2.0 for commandMed-owned source makes the project's patent/NOTICE posture more explicit while remaining compatible with retaining MIT-licensed donor files under their original terms.

This does not prohibit an MIT-licensed subcomponent or imported file when its original terms require preservation.

## 7. No silent authority expansion

Regardless of either decision:

```text
CURRENT_E004_AUTHORITY_EXPANSION=NONE
OPERATIONAL_PREFLIGHT_EVIDENCE_RUN_AUTHORITY=UNCHANGED
MODEL_EXECUTION_AUTHORITY_EXPANSION=NONE
TOURNAMENT_EXECUTION_AUTHORITY_EXPANSION=NONE
A15_AUTHORITY_EXPANSION=NONE
TRAINING_AUTHORITY=NONE
PHI_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The separate E004 operational-preflight Founder decision remains governed only by its own exact canonical token.

## 8. Current lawful next transition for this license surface

Before either choice has authority:

```text
SOFTWARE_LICENSE_DECISION_SURFACE=PREPARED_NOT_YET_CANONICAL
FOUNDER_COMMANDMED_SOFTWARE_LICENSE_DECISION=ABSENT
ROOT_LICENSE_IMPLEMENTATION_PREPARATION_AUTHORITY=NONE
```

After this request is canonically merged, the next lawful transition is one exact post-canonical Founder selection from Section 5, followed by a separate canonical decision-capture record before any root-license implementation.
