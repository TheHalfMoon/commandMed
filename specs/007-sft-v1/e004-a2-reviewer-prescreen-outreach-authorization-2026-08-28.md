# E004 A2 Reviewer Pre-Screen Outreach Authorization — 2026-08-28

**Spec:** 007 SFT V1  
**Artifact class:** bounded external-information-gathering authorization  
**Canonical base:** `06b888832423bef95560bf816245abdb7fe501e5`  
**Founder direction date:** 2026-08-28  
**Authorization becomes effective:** only after fresh exact-head qualification and canonical merge  
**Spend:** USD 0

## Purpose

Authorize one narrowly bounded **pre-screen inquiry** to public reviewer candidates already listed in the canonical A2 public reviewer candidate slate, solely to determine whether a candidate may be willing and potentially eligible to enter a later formal reviewer-selection process.

This authorization deliberately distinguishes an information-only inquiry from a commitment to perform scientific work.

```text
PRESCREEN_OUTREACH_IS_REVIEWER_ENGAGEMENT_COMMITMENT=NO
PRESCREEN_OUTREACH_IS_REVIEWER_APPOINTMENT=NO
PRESCREEN_OUTREACH_IS_PERSONNEL_ASSIGNMENT=NO
PRESCREEN_OUTREACH_IS_SCIENTIFIC_REVIEW=NO
PRESCREEN_OUTREACH_IS_A14_AUTHORIZED_PASS=NO
PRESCREEN_OUTREACH_IS_A7_ASSIGNMENT=NO
```

The inquiry may ask only for non-sensitive screening information needed to decide whether a future separately governed selection/engagement process is worth pursuing.

## Founder authorization evidence and narrow interpretation

The Founder directed on 2026-08-28:

```text
go ahead, do not stop, you have all my approval
```

That broad continuation direction is interpreted **only** as authorization for this dependency-safe, zero-spend, information-only pre-screen outreach after this exact record is independently qualified and merged.

It is not interpreted as:

```text
REVIEWER_APPOINTMENT_AUTHORITY
SCIENTIFIC_ROLE_ASSIGNMENT_AUTHORITY
A7_PASS
A14_PASS
PAID_OR_UNPAID_REVIEW_ENGAGEMENT_AUTHORITY
CLINICAL_REVIEW_DISPOSITION
STATISTICAL_REVIEW_DISPOSITION
MODEL_CONVERSION_AUTHORITY
CONTAMINATION_ASSESSMENT_AUTHORITY
TRAINING_AUTHORITY
PRIVATE_GOLD_OR_PHI_AUTHORITY
CREDENTIAL_ACCESS_AUTHORITY
SPEND_AUTHORITY
```

## Controlling governance

This authorization is subordinate to:

```text
.specify/memory/constitution.md
AGENTS.md
specs/005-base-model-tournament/session-9-q4-clinical-review-threshold-margin-governance.md
specs/005-base-model-tournament/session-14-q1-a14-spend-engagement-authorization-architecture.md
data/spec005/preconstruction_contract.json
specs/007-sft-v1/e004-a2-review-governance-profile-2026-08-28.md
specs/007-sft-v1/e004-a2-qualified-reviewer-public-candidate-slate-2026-08-28.md
```

The preconstruction DAG remains unchanged:

```text
T1_A2 -> D34 -> H1_A7 -> F1_A14
```

A14 governs creation of new external work commitments, including paid or unpaid reviewer engagements. This record does not create such a commitment. If an inquiry recipient expresses interest, later reviewer work remains blocked until the applicable A7/A14 and scientific-governance requirements are satisfied.

## 1. Authorized candidate scope

The inquiry may be sent only to candidates present in the canonical public candidate slate at merge time.

Initial priority screening set:

```text
C-EM-02=Anas A. Khan, King Saud University
C-MED-01=Tariq Alhawassi, King Saud University
C-SAFE-01=Sumant Ranji, UCSF
C-EVID-01=Carl Heneghan, University of Oxford
C-LAB-01=Christopher Naugler, University of Calgary
S-01=Rafael Perera, University of Oxford
```

`C-EM-02` may also be asked whether he has the exact bilingual clinical-comparison competence required for the Arabic parity review domain. An affirmative self-description is screening evidence only and does not equal qualification PASS.

No recipient outside the canonical slate may be contacted under this authorization.

## 2. Contact-route requirements

Only a contact route published by the candidate's current institution, current institutional profile, or another first-party professional institutional page may be used.

```text
SCRAPED_PRIVATE_EMAIL=PROHIBITED
DATA_BROKER_CONTACT=PROHIBITED
PERSONAL_PHONE_CONTACT=PROHIBITED_UNLESS_EXPLICITLY_PUBLISHED_AS_PROFESSIONAL_ROUTE_AND_SEPARATELY_NEEDED
SOCIAL_MEDIA_DM=NOT_AUTHORIZED
PERSONAL_HOME_ADDRESS=PROHIBITED
```

If no suitable public professional contact route can be verified, that candidate remains `CONTACT_ROUTE_UNRESOLVED` and is not contacted.

## 3. Message content allowed

One initial plain-text email per candidate is authorized. The message may:

1. identify commandMed as an open-source medical-AI research project;
2. state that the project is seeking an independent future clinical-domain or statistical-method reviewer;
3. provide a public GitHub repository/brief link;
4. ask whether the recipient is potentially interested and available to discuss a future review;
5. ask whether the described domain/method scope is within their professional competence;
6. ask for disclosure of any obvious conflict of interest relevant to deciding whether to continue the conversation;
7. for the Arabic-parity candidate, ask whether they are professionally comfortable reviewing matched Arabic/English clinical content for semantic/clinical parity;
8. state clearly that this inquiry is not an appointment, contract, paid offer, or request to begin scientific review work.

The message must not include or request:

```text
PRIVATE_GOLD_CONTENT
BENCHMARK_OR_SELECTION_PAYLOADS
CANDIDATE_RESULTS
PREFERRED_MODEL_OR_WINNER_SIGNALS
PHI
SECRETS_OR_CREDENTIALS
PAYMENT_DETAILS
BANKING_OR_TAX_INFORMATION
PERSONAL_IDENTITY_DOCUMENTS
UNPUBLISHED_CONFIDENTIAL_CLINICAL_DATA
```

No attachments are authorized in the initial inquiry.

## 4. Work-request prohibition

The initial email must not ask the candidate to perform any review, analysis, scoring, adjudication, threshold selection, manuscript work, case authoring, or other deliverable.

```text
REQUEST_TO_BEGIN_SCIENTIFIC_WORK=PROHIBITED
REQUEST_FOR_REVIEW_DISPOSITION=PROHIBITED
REQUEST_FOR_THRESHOLD_RECOMMENDATION=PROHIBITED
REQUEST_FOR_STATISTICAL_ANALYSIS=PROHIBITED
REQUEST_FOR_CASE_OR_DATA_ACCESS=PROHIBITED
```

A recipient's unsolicited scientific opinion in a reply cannot be used as an A2 review disposition. It may be retained only as correspondence evidence and must be re-obtained through the later exact review protocol if the person is formally selected.

## 5. Commitment and compensation boundary

```text
PAYMENT_OFFER=PROHIBITED
HONORARIUM_OFFER=PROHIBITED
CONTRACT_OFFER=PROHIBITED
PURCHASE_ORDER=PROHIBITED
REIMBURSEMENT_COMMITMENT=PROHIBITED
UNPAID_WORK_COMMITMENT=PROHIBITED
EXCLUSIVITY_REQUEST=PROHIBITED
```

The only authorized commitment is the project team's own commitment to handle the inquiry consistently with this record. No recipient is asked to commit work.

```text
CURRENT_AUTHORIZED_SPEND_USD=0
CURRENT_NEW_PAID_ENGAGEMENT_AUTHORITY=NONE
CURRENT_NEW_UNPAID_EXTERNAL_ENGAGEMENT_AUTHORITY=NONE
```

Those A14 states remain unchanged.

## 6. Authorized response evidence

A recipient reply may create only these preliminary evidence fields:

```text
CONTACT_ROUTE_VERIFIED
CONTACT_ATTEMPT_TIMESTAMP_OR_SEQUENCE
INTEREST_STATE=INTERESTED|NOT_INTERESTED|UNSURE|NO_RESPONSE
AVAILABILITY_STATE=PRELIMINARY_AVAILABLE|PRELIMINARY_UNAVAILABLE|UNKNOWN
SELF_DESCRIBED_SCOPE_COMPETENCE=RECORDED_NOT_YET_VERIFIED
SELF_DISCLOSED_CONFLICT_SIGNAL=RECORDED_PENDING_FORMAL_REVIEW
BILINGUAL_COMPARISON_SELF_DESCRIPTION=RECORDED_NOT_YET_VERIFIED_WHERE_APPLICABLE
```

It cannot create:

```text
REVIEWER_ELIGIBILITY_PASS
REVIEWER_ASSIGNMENT
A7_PASS
A14_PASS
CLINICAL_REVIEW_ACCEPT
STATISTICAL_REVIEW_ACCEPT
THRESHOLD_POLICY_ADOPTION
```

## 7. Message-count and follow-up cap

This authorization permits:

```text
INITIAL_MESSAGES_PER_CANDIDATE_MAX=1
FOLLOW_UP_MESSAGES_AUTHORIZED_NOW=0
BULK_MAILING=PROHIBITED
AUTOMATED_MARKETING_SEQUENCE=PROHIBITED
```

No follow-up is authorized by this record. Any later follow-up must be separately justified against the response state and current governance.

## 8. Reputation and identity safeguards

The message must not state or imply that a candidate:

- is affiliated with commandMed;
- has agreed to review commandMed;
- endorses commandMed;
- is part of a reviewer panel;
- has been selected or appointed;
- will be compensated;
- has passed conflict or independence screening.

The candidate slate remains internal/public research context only.

## 9. Exit evidence for this authorization slice

Before an individual initial email may be sent:

```text
THIS_AUTHORIZATION_RECORD=QUALIFIED_AND_CANONICAL
CURRENT_MAIN_REVERIFIED=YES
CANDIDATE_PRESENT_IN_CANONICAL_SLATE=YES
FIRST_PARTY_CONTACT_ROUTE_REVERIFIED=YES
MESSAGE_MATCHES_ALLOWED_CONTENT=YES
NO_ATTACHMENTS=YES
NO_PAYMENT_OR_WORK_COMMITMENT=YES
```

After sending, the only immediate state transition is:

```text
PRESCREEN_CONTACT_ATTEMPT=RECORDED
```

No scientific or personnel gate changes state merely from sending the inquiry.

## 10. Current project state preserved

```text
EXACT_APPOINTED_REVIEWER_IDENTITIES=UNRESOLVED
CLINICAL_REVIEW_DISPOSITION=ABSENT
STATISTICAL_REVIEW_DISPOSITION=ABSENT
T1_A2=INCOMPLETE
D34_A3_A4=BLOCKED_BY_T1
A7_FINAL_PERSONNEL_ROSTER=UNRESOLVED
A14_FINAL_REQUIREMENT_DETERMINATION=NOT_YET_FROZEN
A14_OPERATIONAL_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED

MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Exclusions

This authorization creates no reviewer appointment or scientific-role assignment; no paid or unpaid work engagement; no contract; no payment; no threshold, margin, statistical design, or review disposition; no model, benchmark, device, conversion, contamination, or training execution; no PHI/Private Gold access; no credentials; and no spend.

It authorizes only the bounded information-only initial inquiry described above, and only after canonical exact-head qualification.
