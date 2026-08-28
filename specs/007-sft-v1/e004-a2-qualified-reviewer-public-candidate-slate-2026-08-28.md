# E004 A2 Qualified Reviewer Public Candidate Slate — 2026-08-28

**Spec:** 007 SFT V1  
**Artifact class:** public-evidence candidate research only  
**Canonical base:** `f18da1e17dd4d65266c4252e61c76d637efc026c`  
**Research capture date:** 2026-08-28  
**Reviewer appointment:** NO  
**Reviewer outreach:** NO  
**Reviewer engagement:** NO  
**Reviewer consent/availability:** UNKNOWN  
**Conflict check:** PENDING  
**Spend:** USD 0

## Purpose

Reduce, but do not close, the A2 reviewer-identity blocker by binding a small public candidate slate to authoritative institutional profile evidence.

The now-canonical A2 review-governance profile requires three distinct functions for any metric policy:

```text
CLINICAL_DOMAIN_REVIEW
STATISTICAL_METHOD_REVIEW
CANONICAL_GOVERNANCE_ADOPTION
```

This record researches candidates only for the first two scientific functions. It does not appoint any reviewer, establish availability or consent, prove absence of conflicts, authorize outreach or payment, or create a scientific review disposition.

```text
PUBLIC_CANDIDATE_RESEARCH_PERFORMED=YES
CANDIDATE_IDENTITIES_PUBLICLY_BOUND=YES
EXACT_APPOINTED_REVIEWER_IDENTITIES=UNRESOLVED
CLINICAL_REVIEW_DISPOSITION=ABSENT
STATISTICAL_REVIEW_DISPOSITION=ABSENT
CANONICAL_THRESHOLD_POLICY_ADOPTION=ABSENT
```

## Candidate-evidence vocabulary

```text
PUBLIC_EVIDENCE_FIT=public institutional evidence supports a plausible match to the future review function
NEEDS_CONFIRMATION=the exact future competence/availability/conflict/consent requirement is not proven by public profile evidence
NOT_APPOINTED=no repository decision or contact has selected the person as a commandMed reviewer
```

Public profile evidence is screening evidence only. A title, degree, publication, or institutional role is not by itself a commandMed review credential record.

Before any appointment, the future protected/auditable evidence package must verify the canonical review-governance requirements, including exact identity, qualification evidence, scope competence, conflicts, candidate-result exposure state, and consent/availability.

## 1. Emergency-miss clinical review candidates

Canonical competence target:

```text
METRIC=emergency_miss_rate
REQUIRED_DOMAIN=acute_or_emergency_clinical_expertise
```

### C-EM-01 — Zohair Al Aseri / Zuhair Al-Asiri, King Saud University

Public institutional evidence:

```text
PUBLIC_ROLE=Professor and Consultant, Emergency Medicine and Critical Care
PUBLIC_QUALIFICATION_SIGNAL=FRCPC Emergency Medicine; critical-care specialist training/certification
PUBLIC_SCOPE_SIGNAL=Emergency Medicine + Critical Care; national academic/clinical leadership
PUBLIC_EVIDENCE_FIT=STRONG
APPOINTMENT=NO
AVAILABILITY=UNKNOWN
CONFLICT_CHECK=PENDING
```

Source locators:

- https://faculty.ksu.edu.sa/ar/zalaseri
- https://faculty.ksu.edu.sa/en/node/75887

The institutional profile describes him as Professor and Consultant in Emergency Medicine and Critical Care and records Canadian emergency/critical-care specialist qualifications and extensive program/clinical leadership.

### C-EM-02 — Anas A. Khan, King Saud University

Public institutional evidence:

```text
PUBLIC_ROLE=Professor/Associate Professor and Consultant, Emergency & Disaster Medicine
PUBLIC_QUALIFICATION_SIGNAL=MBBS; Saudi Board Emergency Medicine; Arab Board Emergency Medicine; disaster-medicine fellowship
PUBLIC_SCOPE_SIGNAL=Emergency Medicine, disaster management, public-health emergencies
PUBLIC_EVIDENCE_FIT=STRONG
APPOINTMENT=NO
AVAILABILITY=UNKNOWN
CONFLICT_CHECK=PENDING
```

Source locators:

- https://faculty.ksu.edu.sa/en/anaskhan
- https://faculty.ksu.edu.sa/en/node/153220

Institutional pages identify him as an emergency-medicine consultant/faculty member with Saudi and Arab emergency-medicine board credentials and disaster-medicine training.

## 2. Medication-critical-error clinical review candidates

Canonical competence target:

```text
METRIC=medication_critical_error_rate
REQUIRED_DOMAIN=medication_or_pharmacology_safety_expertise
```

### C-MED-01 — Tariq Alhawassi, King Saud University

Public institutional evidence:

```text
PUBLIC_ROLE=Associate Professor of Clinical Pharmacy; Director/Supervisor, Medication Safety Research Chair
PUBLIC_QUALIFICATION_SIGNAL=BSc Pharmacy; Master of Clinical Pharmacy; PhD in Quality Use of Medicines
PUBLIC_SCOPE_SIGNAL=Medication safety, pharmacovigilance, drug-use evaluation, pharmacoepidemiology
PUBLIC_EVIDENCE_FIT=STRONG
APPOINTMENT=NO
AVAILABILITY=UNKNOWN
CONFLICT_CHECK=PENDING
```

Source locators:

- https://faculty.ksu.edu.sa/en/tarriq
- https://faculty.ksu.edu.sa/en/node/144285

The KSU profile explicitly identifies medication-safety research-chair leadership and research focus in pharmacovigilance, medication safety, drug-use evaluation, and adverse drug reactions.

### C-MED-02 — Ghadah A. Assiri, King Saud University

Public institutional evidence:

```text
PUBLIC_ROLE=Associate Professor, Clinical Pharmacy
PUBLIC_QUALIFICATION_SIGNAL=BPharm; MSc; PhD
PUBLIC_SCOPE_SIGNAL=Medication errors and error-related adverse drug events; Saudi/community-care medication-safety research
PUBLIC_EVIDENCE_FIT=STRONG
APPOINTMENT=NO
AVAILABILITY=UNKNOWN
CONFLICT_CHECK=PENDING
```

Source locators:

- https://faculty.ksu.edu.sa/en/gassiri/publication/256185
- https://faculty.ksu.edu.sa/ar/gassiri/publication/305974

The institutional publication pages identify her as Associate Professor of Clinical Pharmacy and bind research specifically on medication errors and error-related adverse drug events.

## 3. Selective-risk / clinical-safety review candidates

Canonical competence target:

```text
METRIC=selective_risk_at_target_coverage
REQUIRED_DOMAIN=clinical_safety_expertise
```

The exact future reviewer must understand the clinical-harm interpretation of abstention/coverage decisions. Public AI-safety or patient-safety work is useful screening evidence but does not itself prove commandMed-specific selective-risk competence.

### C-SAFE-01 — Sumant Ranji, MD, UCSF

Public institutional evidence:

```text
PUBLIC_ROLE=Professor of Clinical Medicine; Director, UCSF Coordinating Center for Diagnostic Excellence (CODEX)
PUBLIC_SCOPE_SIGNAL=National patient-safety expertise; diagnostic excellence; AI applications to diagnostic quality/safety
PUBLIC_EVIDENCE_FIT=STRONG_CLINICAL_SAFETY
EXACT_SELECTIVE_RISK_METHOD_COMPETENCE=NEEDS_CONFIRMATION
APPOINTMENT=NO
AVAILABILITY=UNKNOWN
CONFLICT_CHECK=PENDING
```

Source locator:

- https://profiles.ucsf.edu/sumant.ranji

The UCSF profile describes Dr. Ranji as a national expert in patient safety and diagnostic excellence and states that CODEX studies AI applications to improving diagnosis.

### C-SAFE-02 — Smitha Ganeshan, MD, MBA, UCSF

Public institutional evidence:

```text
PUBLIC_ROLE=Assistant Professor of Medicine; Medical Director for AI Programs at UCSF
PUBLIC_SCOPE_SIGNAL=Hospital medicine; care quality and safety; clinical AI evaluation/implementation; safety/equity/clinician experience
PUBLIC_EVIDENCE_FIT=STRONG_CLINICAL_AI_SAFETY
EXACT_SELECTIVE_RISK_METHOD_COMPETENCE=NEEDS_CONFIRMATION
APPOINTMENT=NO
AVAILABILITY=UNKNOWN
CONFLICT_CHECK=PENDING
```

Source locator:

- https://profiles.ucsf.edu/smitha.ganeshan

The UCSF profile identifies her as a practicing hospitalist and Medical Director for AI Programs, with work on safe clinical-AI implementation and clinical outcomes.

## 4. Citation-entailment / clinical-evidence interpretation candidates

Canonical competence target:

```text
METRIC=citation_entailment_fidelity
REQUIRED_DOMAIN=clinical_evidence_interpretation_expertise
```

### C-EVID-01 — Carl Heneghan, University of Oxford

Public institutional evidence:

```text
PUBLIC_ROLE=Professor of Evidence-Based Medicine; Director, Centre for Evidence-Based Medicine; NHS Urgent Care GP
PUBLIC_SCOPE_SIGNAL=Clinical epidemiology; evidence-based medicine; research methods; evidence synthesis; assessment of health claims/harms
PUBLIC_EVIDENCE_FIT=STRONG
APPOINTMENT=NO
AVAILABILITY=UNKNOWN
CONFLICT_CHECK=PENDING
```

Source locator:

- https://www.phc.ox.ac.uk/team/carl-heneghan

Oxford describes him as a clinical epidemiologist with expertise in evidence-based medicine, research methods, and evidence synthesis.

### C-EVID-02 — Ben Goldacre, University of Oxford

Public institutional evidence:

```text
PUBLIC_ROLE=Director, Bennett Institute for Applied Data Science; Bennett Professor of Evidence Based Medicine
PUBLIC_SCOPE_SIGNAL=Clinical epidemiology; evidence-based medicine; healthcare data/evidence infrastructure; trial/data transparency
PUBLIC_EVIDENCE_FIT=STRONG
APPOINTMENT=NO
AVAILABILITY=UNKNOWN
CONFLICT_CHECK=PENDING
```

Source locator:

- https://www.phc.ox.ac.uk/team/ben-goldacre

Oxford identifies him as a clinical epidemiologist trained in medicine and epidemiology whose academic work centers on data infrastructure, epidemiology, and evidence-based medicine.

## 5. Arabic clinical parity candidates

Canonical competence target:

```text
METRIC=arabic_clinical_parity_gap
REQUIRED_DOMAIN=Arabic-speaking clinical professional with bilingual clinical comparison competence
```

The public KSU profiles below are available in Arabic and English and support Saudi clinical practice/academic context. That is useful screening evidence, but it is not sufficient to prove the exact commandMed requirement of bilingual clinical comparison competence.

### C-AR-01 — Zohair Al Aseri / Zuhair Al-Asiri, King Saud University

```text
PUBLIC_CLINICAL_FIT=STRONG_EMERGENCY_AND_CRITICAL_CARE
PUBLIC_ARABIC_INSTITUTIONAL_PROFILE=YES
PUBLIC_ENGLISH_INSTITUTIONAL_PROFILE=YES
LIKELY_ARABIC_CLINICAL_COMPETENCE=PUBLIC_EVIDENCE_SUPPORTS_CANDIDATE_SCREENING_ONLY
EXACT_BILINGUAL_CLINICAL_COMPARISON_COMPETENCE=NEEDS_CONFIRMATION
APPOINTMENT=NO
AVAILABILITY=UNKNOWN
CONFLICT_CHECK=PENDING
```

Source locators:

- https://faculty.ksu.edu.sa/ar/zalaseri
- https://faculty.ksu.edu.sa/en/node/75887

### C-AR-02 — Anas A. Khan, King Saud University

```text
PUBLIC_CLINICAL_FIT=STRONG_EMERGENCY_MEDICINE
PUBLIC_ARABIC_INSTITUTIONAL_PROFILE=YES
PUBLIC_ENGLISH_INSTITUTIONAL_PROFILE=YES
LIKELY_ARABIC_CLINICAL_COMPETENCE=PUBLIC_EVIDENCE_SUPPORTS_CANDIDATE_SCREENING_ONLY
EXACT_BILINGUAL_CLINICAL_COMPARISON_COMPETENCE=NEEDS_CONFIRMATION
APPOINTMENT=NO
AVAILABILITY=UNKNOWN
CONFLICT_CHECK=PENDING
```

Source locators:

- https://faculty.ksu.edu.sa/ar/anaskhan
- https://faculty.ksu.edu.sa/en/anaskhan

No Arabic reviewer may be admitted solely from language inference based on nationality, name, location, or an Arabic profile. Exact bilingual clinical comparison competence remains an explicit future evidence requirement.

## 6. Laboratory-report field-extraction candidates

Canonical competence target:

```text
METRIC=lab_report_field_extraction_accuracy
REQUIRED_DOMAIN=laboratory_medicine_pathology_or_relevant_lab_clinical_informatics_expertise
```

### C-LAB-01 — Christopher Naugler, MD, University of Calgary

Public institutional evidence:

```text
PUBLIC_ROLE=Professor, Pathology and Laboratory Medicine; Department Head; laboratory medical leadership
PUBLIC_QUALIFICATION_SIGNAL=MD; General Pathology specialty certification (FRCPC)
PUBLIC_SCOPE_SIGNAL=Laboratory test appropriateness; clinical epidemiology; pathology informatics; big-data modelling of laboratory data
PUBLIC_EVIDENCE_FIT=STRONG
APPOINTMENT=NO
AVAILABILITY=UNKNOWN
CONFLICT_CHECK=PENDING
```

Source locators:

- https://profiles.ucalgary.ca/christopher-naugler
- https://cumming.ucalgary.ca/departments/pathology/faculty-staff

The University of Calgary profile documents pathology/laboratory-medicine leadership and research in laboratory testing, clinical epidemiology, and pathology informatics.

### C-LAB-02 — Etienne Mahe, MD, University of Calgary

Public institutional evidence:

```text
PUBLIC_ROLE=Hematopathologist / molecular pathologist; clinical faculty
PUBLIC_SCOPE_SIGNAL=Laboratory medicine/pathology; molecular pathology; bioinformatics
PUBLIC_EVIDENCE_FIT=PLAUSIBLE_STRONG
EXACT_LAB_REPORT_EXTRACTION_REVIEW_SCOPE=NEEDS_CONFIRMATION
APPOINTMENT=NO
AVAILABILITY=UNKNOWN
CONFLICT_CHECK=PENDING
```

Source locators:

- https://cumming.ucalgary.ca/research/amyloidcalgary/about/our-team
- https://charbonneau.ucalgary.ca/research/resources/institute-resources/cancer-translational-research-core

University of Calgary pages identify Dr. Mahe as a hematopathologist/molecular pathologist and clinical faculty member with bioinformatics-related work.

## 7. Statistical-method review candidates

Canonical requirement:

```text
FUNCTION=STATISTICAL_METHOD_REVIEW
BASE_REQUIREMENT=identity-bound competence in biostatistics/statistics/epidemiologic or equivalent methods AND exact future method family
```

No public profile below proves competence for every method family in the A2 candidate packet. Appointment must match the actual frozen method set; one statistician must not be assumed to cover rare-event inference, clustering, paired noninferiority/equivalence, selective-risk methods, F1 inference, and multiplicity merely from a general title.

### S-01 — Rafael Perera, University of Oxford

Public institutional evidence:

```text
PUBLIC_ROLE=Professor of Medical Statistics; Director, Statistics Group
PUBLIC_SCOPE_SIGNAL=Leads methodologists across multiple clinical areas; clinical-trials/statistical leadership; healthcare-policy boards
PUBLIC_EVIDENCE_FIT=STRONG_GENERAL_MEDICAL_STATISTICS
EXACT_METHOD_FAMILY_COVERAGE=NEEDS_CONFIRMATION_AGAINST_FROZEN_A2_METHOD_SET
APPOINTMENT=NO
AVAILABILITY=UNKNOWN
CONFLICT_CHECK=PENDING
```

Source locator:

- https://www.phc.ox.ac.uk/team/rafael-perera

### S-02 — Richard Stevens, University of Oxford

Public institutional evidence:

```text
PUBLIC_ROLE=Professor of Medical Statistics; Deputy Director, Statistics Group; MSc EBHC Medical Statistics Course Director
PUBLIC_SCOPE_SIGNAL=Medical statistics; clinical research; meta-analysis methodology
PUBLIC_EVIDENCE_FIT=STRONG_GENERAL_MEDICAL_STATISTICS
EXACT_METHOD_FAMILY_COVERAGE=NEEDS_CONFIRMATION_AGAINST_FROZEN_A2_METHOD_SET
APPOINTMENT=NO
AVAILABILITY=UNKNOWN
CONFLICT_CHECK=PENDING
```

Source locator:

- https://www.phc.ox.ac.uk/team/richard-stevens

### S-03 — Frank E. Harrell Jr., PhD, Vanderbilt University Medical Center

Public institutional evidence:

```text
PUBLIC_ROLE=Professor of Biostatistics
PUBLIC_SCOPE_SIGNAL=Biostatistics; clinical-trial/statistical methodology; predictive modelling; prior FDA CDER senior biostatistics advisory role documented by Vanderbilt
PUBLIC_EVIDENCE_FIT=STRONG_GENERAL_BIOSTATISTICS
EXACT_METHOD_FAMILY_COVERAGE=NEEDS_CONFIRMATION_AGAINST_FROZEN_A2_METHOD_SET
APPOINTMENT=NO
AVAILABILITY=UNKNOWN
CONFLICT_CHECK=PENDING
```

Source locators:

- https://www.vumc.org/biostatistics/person/primary-faculty
- https://medsites.vumc.org/vtracc/people/vtracc-team

The Vanderbilt department currently lists Frank Harrell as Professor of Biostatistics; Vanderbilt records also document senior biostatistics advisory work for FDA CDER.

## 8. Screening matrix

| Metric / function | Primary public candidate | Alternate public candidate | Public-evidence fit | Critical unresolved qualification |
|---|---|---|---|---|
| Emergency miss | Zohair Al Aseri | Anas A. Khan | Strong | availability, conflicts, exact commandMed scope consent |
| Medication critical error | Tariq Alhawassi | Ghadah A. Assiri | Strong | availability, conflicts, exact commandMed scope consent |
| Selective-risk clinical safety | Sumant Ranji | Smitha Ganeshan | Strong clinical-safety fit | exact selective-risk clinical-review competence |
| Citation entailment / evidence interpretation | Carl Heneghan | Ben Goldacre | Strong | exact commandMed evidence-entailment review scope |
| Arabic clinical parity | Zohair Al Aseri | Anas A. Khan | Plausible strong clinical/Arabic-context screening | exact bilingual clinical-comparison competence |
| Lab extraction | Christopher Naugler | Etienne Mahe | Strong / plausible strong | exact extraction-policy review scope |
| Statistical method | Rafael Perera | Richard Stevens / Frank Harrell | Strong general medical statistics | exact frozen method-family coverage |

This matrix is a research shortlist, not a ranking of scientific quality and not an appointment order.

## 9. Required pre-appointment verification

No candidate may become an exact reviewer identity until a separate bounded selection/engagement process records at least:

```text
CURRENT_INSTITUTIONAL_ROLE_REVERIFIED=YES
EXACT_IDENTITY=BOUND
QUALIFICATION_EVIDENCE_REFERENCE=BOUND
METRIC_OR_METHOD_SCOPE_COMPETENCE=PASS
AVAILABILITY=CONFIRMED
CONSENT_TO_REVIEW=CONFIRMED
CONFLICT_DISCLOSURE=COMPLETE
MATERIAL_UNMANAGED_CONFLICT=NO
CANDIDATE_RESULT_EXPOSURE_STATE=BOUND_ACCEPTABLE
PRIVATE_GOLD_EXPOSURE_STATE=BOUND_ACCEPTABLE
REVIEW_INDEPENDENCE=PASS
ENGAGEMENT_AND_PAYMENT_AUTHORITY=BOUND_IF_APPLICABLE
```

A candidate who does not meet these checks remains screened-out or pending; public prominence does not override a failed governance requirement.

## 10. Current-state reduction

This record reduces only the search-space uncertainty:

```text
A2_PUBLIC_REVIEWER_CANDIDATE_SEARCH=COMPLETED_FOR_INITIAL_SLATE
CLINICAL_CANDIDATE_SLATE=BOUND_PUBLIC_EVIDENCE
STATISTICAL_CANDIDATE_SLATE=BOUND_PUBLIC_EVIDENCE
EXACT_APPOINTED_REVIEWER_IDENTITIES=UNRESOLVED
REVIEWER_AVAILABILITY_AND_CONSENT=UNRESOLVED
REVIEWER_CONFLICT_AND_INDEPENDENCE_CHECK=UNRESOLVED
REVIEWER_ENGAGEMENT_AUTHORITY=NONE
PAID_REVIEWER_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The scientific frontier remains:

```text
CLINICAL_REVIEW_DISPOSITION=ABSENT
STATISTICAL_REVIEW_DISPOSITION=ABSENT
COMMANDMED_SPECIFIC_NUMERIC_THRESHOLD_OR_MARGIN_POLICY=ABSENT
NUMERIC_CONFIDENCE_OR_ERROR_RATE_POLICY=ABSENT
NUMERIC_SAMPLE_SIZE_OR_POWER_DESIGN=ABSENT
CANONICAL_THRESHOLD_POLICY_ADOPTION=ABSENT
T1_A2=INCOMPLETE
D34_A3_A4=BLOCKED_BY_T1
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

## 11. Authority boundary

```text
REVIEWER_APPOINTMENT_AUTHORITY_CREATED=NO
REVIEWER_OUTREACH_AUTHORITY_CREATED=NO
REVIEWER_ENGAGEMENT_AUTHORITY_CREATED=NO
PAID_REVIEWER_AUTHORITY=NONE

MODEL_WEIGHT_ACCESS_AUTHORITY=UNCHANGED_EXISTING_E002_ONLY
MODEL_EXECUTION_AUTHORITY=UNCHANGED_EXISTING_E003_ONLY_SUBJECT_TO_PREFLIGHT
MODEL_CONVERSION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
PRIVATE_GOLD_AUTHORITY=NONE
PHI_AUTHORITY=NONE
CREDENTIAL_ACCESS_AUTHORITY=NONE
PROVIDER_GENERATION_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## Exclusions

This artifact performs no outreach, appointment, reviewer engagement, payment, scientific review, threshold/margin selection, benchmark/model/device execution, model conversion, contamination assessment, selection-suite construction, Private Gold/PHI access, credential use, provider generation, training, procurement, or spend.

It does not assert that any named person endorses commandMed, is aware of commandMed, is available, has consented, or has passed conflict/independence screening.
