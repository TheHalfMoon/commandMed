# Spec 006 Research — Patient Safety Scaffold & Deterministic Tools

**Status:** CANONICAL PLANNING EVIDENCE (pre-implementation)
**Authority:** NONE — no model/weight/benchmark/Private Gold/PHI/device/spend execution
**Base:** `52f799b` / PR #39 `ba5b35b`
**Depends on:** Spec 002 `CLOSED_CANONICAL`, Spec 005 `CLOSED_CANONICAL`

## 1. Research scope

Spec 006 composes Spec 002 safety gates and Spec 005 control-plane validators into an operational interaction scaffold. Research must not redefine Spec 002 states, precedence, or truth-boundary classes, and must not invent clinical truth where authoritative source identity is required.

Research is evidence, not implementation authority. No network/tool execution is authorized by this document.

## 2. Authoritative sources consulted

| Domain | Authoritative source | Version/Date | Why authoritative | What it does NOT authorize |
|---|---|---|---|---|
| Safety-critical software | IEC 62304 (medical device software lifecycle) + FDA General Principles of Software Validation | IEC 62304:2006+A1:2015; FDA GPSV 2002 | International standard / regulator guidance for fail-closed, traceable, validated medical software | Numeric clinical thresholds; device classification |
| Clinical decision support | WHO guidance on CDS + national authorities (e.g., Saudi MOH, FDA CDS guidance 2022) | WHO CDS framework; FDA CDS Guidance Sep 2022 | Primary policy owners for escalation/evidence requirements | Exact red-flag lists without jurisdiction binding |
| Validated clinical scores | Original validation papers (e.g., Wells, CURB-65, HEART, CHA2DS2-VASc, MELD-Na, APACHE) + official calculators (MDCalc source attribution) | Per-score publication identity required per registry entry | Only peer-reviewed validation establishes cutoff/interpretation | Inclusion of a score without frozen version/source hash |
| Medication/drug interaction | FDA drug labels (DailyMed/SPL), EMA SmPC, Saudi SFDA, WHO ATC/DDD, authoritative interaction DBs (e.g., DrugBank, Lexicomp, Micromedex — license-gated) | Per-label/DB version + content SHA-256 | Only version-bound label/DB provides interaction truth | Hard-coding interaction truth into model weights |
| Terminology & schemas | HL7 FHIR R4/R5, ICD-11, LOINC, SNOMED CT (where licensed), UCUM (units) | FHIR R4 v4.0.1; UCUM 2.1 | International standards for structured validation & unit conversion | Clinical interpretation of coded values |
| Emergency/escalation | WHO Clinical Red Flags, national emergency triage (e.g., ESI v4, Manchester Triage), Saudi Red Crescent / MOH emergency routing — jurisdiction-bound | Per-system version | Only jurisdiction-bound routing may emit locale-specific service info | Fabricating emergency phone numbers or universal triage thresholds |
| Provenance & SHA-256 | NIST FIPS 180-4 (SHA-256), existing commandMed `eval_contract/canonical.py` | FIPS 180-4; repo canonical serializer | Cryptographic identity for deterministic tool/policy/trace records | Medical correctness |

`TOOL_CONTENT_IDENTITY` and `SOURCE_AUTHORITY` fields in the tool registry must bind each exact version/date/content hash before any `PASS` claim.

## 3. Deterministic tool boundary (Ponytail-minimal)

Candidate tool **classes** only; no implementation is authorized here. Each class maps to Spec 002 truth-boundary `TASK_CLASS`:

- `UNIT_CONVERSION` → `unit_conversion` (UCUM-bound, pure arithmetic)
- `ARITHMETIC` → `pure_dosage_arithmetic` (closed-form, no guideline lookup)
- `VALIDATED_CLINICAL_SCORE` → `validated_clinical_score` (per-score version + source hash, fail-closed on missing inputs)
- `MEDICATION_INTERACTION_OR_CONTRAINDICATION_LOOKUP` → `interaction_lookup` (per-DB identity + version + freshness policy, no inference)
- `STRUCTURED_SCHEMA_VALIDATION` → `schema_validation` (FHIR/JSON schema-bound)
- `IDENTITY_BOUND_EVIDENCE_LOOKUP` / `HARD_ESCALATION_POLICY` → `evidence_retrieval` + `escalation_policy_eval` (policy SHA-256-bound, deterministic outcome)

Schema validation and evidence retrieval are routing/binding checks, not content generation.

## 4. Tool registry contract (metadata-only, pre-implementation)

Every registry entry is a **record**, not a service binding. Required fields (canonical JSON, SHA-256-bound):

```
TOOL_ID, TOOL_VERSION, TOOL_CONTENT_IDENTITY (sha256),
TOOL_CLASS, INPUT_SCHEMA (json-schema), OUTPUT_SCHEMA,
SOURCE_AUTHORITY (WHO/label/DB/standard identifier),
FAILURE_SEMANTICS (fail-closed state + reason code),
APPLICABLE_WHEN, PROHIBITED_WHEN,
FRESHNESS_POLICY, RESULT_PROVENANCE_REQUIRED,
NETWORK_REQUIRED (must be false for offline fixture suite),
EXECUTION_AUTHORITY (NONE at this stage)
```

Real database/service/live lookup is an implementation dependency deferred to `AUTHORIZED_TO_START`. This spec freezes only metadata and validation rules.

## 5. Behavioral state precedence (derived from Spec 002 SP-001…SP-006)

Spec 002 defines `SP-001`…`SP-006` as non-overridable precedence, not a total order. Spec 006 operationalizes one **deterministic evaluation order** that respects all six without inventing clinical severity ranking:

```
1. Contradictory/malformed safety state → ABSTAIN with frozen reason code BLOCKED_SAFETY_STATE (SP-006, fail-closed, zero tolerance; `BLOCKED` is a gate-result, not a behavioral state)
2. Identity-bound EMERGENCY trigger present → EMERGENCY (SP-001, exact equality)
3. Identity-bound ESCALATE trigger present → ESCALATE (SP-001, exact equality)
4. Required evidence missing/contradictory for claimed finding → RETRIEVE_EVIDENCE / ASK_MORE / ABSTAIN per policy (SP-005, SP-002)
5. Required deterministic/authoritative tool available and applicable → USE_TOOL / RETRIEVE_EVIDENCE (SP-003)
6. Deterministic result already valid → must be preserved, never altered by prose (SP-004)
7. Otherwise → ANSWER (only when no higher rule fires)
```

- Exactly **one terminal state** per interaction after evaluation.
- Intermediate evaluations may emit `USE_TOOL`/`RETRIEVE_EVIDENCE` but the final interaction state is exactly one of the seven.
- Generative text **cannot lower** a deterministic safety state; it may only explain or acquire information within the state.
- Conflicting triggers: higher precedence wins; if two equal-precedence required outcomes conflict and are distinct, the interaction fails closed to `ABSTAIN`/`ESCALATE` with `CONFLICTING_SAFETY_OUTCOMES` reason code (SP-006).
- Allowed transitions: any intermediate `ASK_MORE`/`USE_TOOL`/`RETRIEVE_EVIDENCE` → terminal state per re-evaluation with new evidence.
- Forbidden: skipping a required deterministic step to reach `ANSWER`; overriding a valid deterministic result; silently averaging conflicting tool outputs.

Reason codes are frozen vocabulary (e.g., `MISSING_CRITICAL_SLOT`, `TOOL_UNAVAILABLE`, `TOOL_TIMEOUT`, `SPOOFED_TOOL_RESULT_REJECTED`, `CONFLICTING_SAFETY_OUTCOMES`, `INJECTION_ATTEMPT_SUPPRESSED`, `EVIDENCE_NOT_RESOLVED`).

## 6. Emergency design rule

- Deterministic frozen emergency rules remain authoritative; they are version/hash-bound policy records, not model prose.
- Multilingual emergency lexicons (Arabic/English) are **evidence/signals**, not the entire decision function; absence of one literal word never proves safety.
- High-risk ambiguous cases fail toward `ASK_MORE` / `ESCALATE` / `EMERGENCY` per frozen policy, never toward `ANSWER`.
- System must never fabricate locale-specific emergency service numbers/addresses. Any routing that names a service must be jurisdiction-bound and source-attributed; otherwise emit generic escalation without fabricated contact details.
- Trigger classes: `lexical_match` (frozen lexicon, versioned), `semantic_pattern` (frozen policy, not generative improvisation), `tool_result_flag` (e.g., validated score threshold breach). All trigger records carry `policy_id`, `policy_version`, `policy_sha256`, `trigger_evidence_id`.

## 7. Trace / audit model (privacy-safe minimum)

Offline fixtures must be verifiable without network/model weights. Trace is appendix-only, standard-library, deterministic, append-only semantics = no mutation of prior records, only new records appended.

Minimum canonical fields (hashed where PHI-risk exists):

```
interaction_id (uuid), trace_version,
input_identity_sha256, context_identity_sha256,
policy_identity_sha256, tool_registry_identity_sha256,
state_before, state_after,
trigger_record_ids, tool_call_record_ids,
output_identity_sha256, failure_reason_codes,
safety_context (role, language, tool_availability — no raw PHI),
determinism_proof (replay with same inputs/policies → same state)
```

Raw user text is never logged for auditability; hashes and structured reasons suffice. `output_identity_sha256` is hash of the final system utterance, not its raw text in the trace store.

## 8. Clarifications resolved from repository truth

- Tool categories and schemas are typed prerequisites (Sec. 4), not invented.
- Clinical-score registry, interaction DB identities, emergency lexicon source, and escalation routing are **typed pre-implementation evidence prerequisites** (FR-006/FR-007 remain as prerequisite markers; they are not silent PASS).
- Arabic/English emergency handling: both MSA + Saudi/Gulf colloquial + code-switch + transliterated drug names per master plan §13; emergency lexicons must be versioned per language.
- Tool unavailable/timeout → fail-closed `ASK_MORE`/`ABSTAIN`/`ESCALATE` with reason; not `ANSWER`.
- Conflicting deterministic evidence → `CONFLICTING_SAFETY_OUTCOMES` + escalation, never averaging.
- Spoofed tool-result rejection → signature/provenance validation per tool; unsigned/unknown-origin results treated as `SPOOFED_TOOL_RESULT_REJECTED`.
- Network prohibition for fixture tests → `NETWORK_REQUIRED=false`; fixtures replay from committed JSON with fixture-local expected results only.

## 9. What remains as typed founder/external prerequisites

- Exact clinical-score inclusion list + per-score validation paper identity/hash.
- Exact interaction database selection + version + license compatibility with `FD-001` permissive downstream use.
- Exact Arabic/English emergency lexicon content + jurisdiction-specific escalation routing table (Saudi context: MOH/937/Red Crescent 997 — must be sourced and versioned before any routing that names them).
- Any locale-specific emergency service information beyond generic escalation.

These are recorded as `NEEDS_EVIDENCE` checklist items, not fabrications.

## 10. Reuse of existing mechanisms

- SHA-256 canonical JSON + identity hashing: `src/commandmed/eval_contract/canonical.py`
- Hard-gate aggregation: `evaluate_hard_gates()` (Spec 002/001) — Spec 006 adapters must delegate, not re-aggregate
- Deterministic fail-closed validators: `validate_*` patterns in `eval_contract` and `spec005/*` validators
- Lifecycle gates: `AUTHORIZED_TO_START` remains the implementation gate; no separate research lifecycle state is invented
