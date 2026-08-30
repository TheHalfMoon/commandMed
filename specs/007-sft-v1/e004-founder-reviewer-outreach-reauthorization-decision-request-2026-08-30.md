# E004 Founder Reviewer Outreach Reauthorization Decision Request — 2026-08-30

**Spec:** 007 SFT V1  
**Canonical base:** `c0cc823c22bece6b85ffd6d7cc8a3c9e25d0bca9`  
**Artifact class:** Founder decision request only  
**Decision owner:** Founder  
**Decision state:** ABSENT  
**Authority effect of this document:** NONE  
**External reviewer outreach performed:** NO  
**Reviewer appointment performed:** NO  
**Scientific review performed:** NO  
**Spend:** USD 0

## Purpose

Convert the current E004 reviewer-contact blocker into one exact Founder decision surface without inferring authority from generic continuation language.

PR #117 / merge `ac24d897c66349d833e016b770be71915c9f15c7` is the controlling prospective no-outreach boundary:

```text
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
INITIAL_PRESCREEN_MESSAGES_AUTHORIZED_NOW=0
FOLLOW_UP_MESSAGES_AUTHORIZED_NOW=0
REVIEWER_CANDIDATE_CONTACT_EXECUTION=PROHIBITED
EXTERNAL_REVIEWER_ENGAGEMENT_EXECUTION=PROHIBITED
```

The earlier PR #116 pre-screen authorization remains historical evidence only. It is not executable while PR #117 remains controlling.

The Founder's later generic continuation instructions do not automatically reverse PR #117. A new explicit decision against this exact surface is required before any reviewer-candidate contact may resume.

## 1. Current scientific state

```text
EXACT_APPOINTED_REVIEWER_IDENTITIES=UNRESOLVED
CLINICAL_REVIEW_DISPOSITION=ABSENT
STATISTICAL_REVIEW_DISPOSITION=ABSENT
T1_A2=INCOMPLETE
D34_A3_A4=BLOCKED_BY_T1
A7_FINAL_PERSONNEL_ROSTER=UNRESOLVED
A14_OPERATIONAL_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Repository review bots, LLMs, static literature, or Founder self-attestation cannot substitute for the qualified clinical/statistical reviewer functions required by the canonical governance profile.

## 2. Decision classes

The Founder must select exactly one decision class below. Silence, a repository merge, or a generic instruction to continue is not a selection.

### `E004_OUTREACH_DECISION_A` — preserve the current prohibition

```text
FOUNDER_OUTREACH_DECISION=E004_OUTREACH_DECISION_A
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
INITIAL_PRESCREEN_MESSAGES_AUTHORIZED_NOW=0
FOLLOW_UP_MESSAGES_AUTHORIZED_NOW=0
REVIEWER_CANDIDATE_CONTACT_EXECUTION=PROHIBITED
```

Effect: E004 remains blocked on external reviewer evidence unless qualified reviewers/evidence are supplied through another separately permitted path.

### `E004_OUTREACH_DECISION_B` — reauthorize the exact PR #116 information-only pre-screen scope

```text
FOUNDER_OUTREACH_DECISION=E004_OUTREACH_DECISION_B
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=AUTHORIZED_PRESCREEN_ONLY
AUTHORIZED_SCOPE=PR116_INFORMATION_ONLY_PRESCREEN
INITIAL_MESSAGES_PER_CANDIDATE_MAX=1
FOLLOW_UP_MESSAGES_AUTHORIZED_NOW=0
CURRENT_AUTHORIZED_SPEND_USD=0
```

Decision B prospectively supersedes PR #117 only for the exact bounded pre-screen action class. It does not restore any broader historical interpretation.

The historical PR #116 priority screening set is:

```text
C-EM-02=Anas A. Khan, King Saud University
C-MED-01=Tariq Alhawassi, King Saud University
C-SAFE-01=Sumant Ranji, UCSF
C-EVID-01=Carl Heneghan, University of Oxford
C-LAB-01=Christopher Naugler, University of Calgary
S-01=Rafael Perera, University of Oxford
```

That historical list is not, by itself, executable authority. Immediately before any later authorized Decision B contact, each candidate MUST be reverified as a member of the then-current canonical public candidate slate and the repository record MUST bind the candidate identifier to that current-slate evidence. If membership is absent, stale, ambiguous, or cannot be verified, no message may be sent to that candidate.

Only a current first-party public professional contact route may be used. If none can be reverified, no message is sent to that candidate.

The initial message remains plain text, has no attachment, and may ask only about preliminary interest, availability, self-described scope competence, obvious conflict signals, and—where applicable—professional comfort reviewing matched Arabic/English clinical content.

Decision B does **not** authorize:

```text
REVIEWER_APPOINTMENT
SCIENTIFIC_ROLE_ASSIGNMENT
REQUEST_TO_BEGIN_SCIENTIFIC_WORK
CLINICAL_REVIEW_DISPOSITION
STATISTICAL_REVIEW_DISPOSITION
THRESHOLD_RECOMMENDATION
FOLLOW_UP_MESSAGE
PAYMENT_OFFER
HONORARIUM_OFFER
CONTRACT_OFFER
PAID_OR_UNPAID_REVIEW_ENGAGEMENT
A7_PASS
A14_PASS
PRIVATE_GOLD_ACCESS
PHI_ACCESS
CREDENTIAL_ACCESS
MODEL_CONVERSION
CONTAMINATION_ASSESSMENT
A15_ACTIVATION
MODEL_INFERENCE
TOURNAMENT_EXECUTION
TRAINING
PROCUREMENT
PAYMENT
SPEND
```

A reply can create only preliminary contact evidence such as interest, preliminary availability, self-described competence, and conflict signals. It cannot create reviewer eligibility PASS, appointment, A2 scientific acceptance, or any downstream gate PASS.

## 3. ChatGPT recommendation for Founder review

```text
CHATGPT_OUTREACH_POSITION=RECOMMEND_E004_OUTREACH_DECISION_B
RATIONALE_1=T1_A2_REQUIRES_REAL_QUALIFIED_CLINICAL_AND_STATISTICAL_REVIEW
RATIONALE_2=PR117_PROHIBITION_CURRENTLY_PREVENTS_THE_REPOSITORY_FROM_GATHERING_EVEN_PRELIMINARY_REVIEWER_AVAILABILITY_EVIDENCE
RATIONALE_3=PR116_ALREADY_DEFINES_A_NARROW_ZERO_SPEND_INFORMATION_ONLY_SCOPE_WITH_NO_WORK_COMMITMENT
RATIONALE_4=DECISION_B_PRESERVES_A7_A14_SCIENTIFIC_AND_SPEND_GATES_WHILE_REOPENING_ONLY_THE_MINIMUM_CONTACT_STEP
```

This recommendation is not a Founder decision.

## 4. Exact Founder response required

To select Decision B, the Founder must respond unambiguously after this decision surface is canonical and presented, for example:

```text
FOUNDER_OUTREACH_DECISION=E004_OUTREACH_DECISION_B
```

To preserve the prohibition:

```text
FOUNDER_OUTREACH_DECISION=E004_OUTREACH_DECISION_A
```

No later decision record may make either option effective from response text alone. Before an outreach decision becomes effective, the canonical record MUST bind all of the following evidence:

```text
FOUNDER_IDENTITY=ATTRIBUTABLE_AND_VERIFIED
FOUNDER_RESPONSE_SOURCE=TRUSTED_FIRST_PARTY_CHANNEL_OR_CANONICALLY_VERIFIABLE_SOURCE
FOUNDER_RESPONSE_CONTENT=EXACT_CAPTURE
FOUNDER_RESPONSE_TIMESTAMP=VERIFIABLE
FOUNDER_RESPONSE_ORDERING=AFTER_THIS_DECISION_SURFACE_BECAME_CANONICAL
```

If identity, trusted source/channel, exact content, timestamp, or ordering evidence is absent or ambiguous, the response is non-operative and PR #117 remains controlling. Decision B cannot supersede PR #117 without all of that provenance evidence.

The current generic continuation instruction predating this exact canonical decision surface is not retroactively treated as either decision.

## 5. Lifecycle boundaries unchanged by this request

```text
EXTERNAL_REVIEWER_OUTREACH_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

No contact, appointment, scientific review, execution, access, procurement, payment, or spend occurs from creating, reviewing, or merging this request.

## Exit evidence

This decision-request artifact is repository-level complete only after fresh exact-head independent review confirms:

```text
PR117_NO_OUTREACH_BOUNDARY_REPRESENTED_ACCURATELY=YES
PR116_HISTORICAL_PRESCREEN_SCOPE_REPRESENTED_ACCURATELY=YES
DECISION_A_PRESERVES_PROHIBITION=YES
DECISION_B_REOPENS_ONLY_PR116_PRESCREEN_SCOPE=YES
DECISION_B_REQUIRES_CURRENT_CANONICAL_SLATE_MEMBERSHIP_EVIDENCE_PER_CANDIDATE=YES
DECISION_EFFECT_REQUIRES_ATTRIBUTABLE_FOUNDER_IDENTITY=YES
DECISION_EFFECT_REQUIRES_TRUSTED_SOURCE_EXACT_CONTENT_TIMESTAMP_AND_ORDERING=YES
FOLLOW_UP_AUTHORITY_CREATED=NO
REVIEWER_APPOINTMENT_AUTHORITY_CREATED=NO
SCIENTIFIC_REVIEW_AUTHORITY_CREATED=NO
A7_OR_A14_PASS_CREATED=NO
MODEL_OR_DOWNSTREAM_EXECUTION_AUTHORITY_CREATED=NO
SPEND_AUTHORITY_CREATED=NO
E004_REMAINS_BLOCKED_PREFLIGHT=YES
E005_REMAINS_NOT_REACHED=YES
```
