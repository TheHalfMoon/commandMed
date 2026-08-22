# Spec 003 Plan — Data, License & Provenance

**Spec:** `003-data-license-provenance`
**Plan status:** REPAIRED_READY_FOR_ANALYZE_PASS_2
**Canonical base:** `a57f87e77bbd396332b197342d8129f6805ba452`
**Implementation style:** metadata-only, fixture-only, offline, deterministic, Python 3.11 standard library; reuse Spec 001 canonicalization and purpose/quarantine semantics

## 1. Technical objective

Implement the smallest machine-verifiable lineage layer that can:

1. validate the canonical lineage contract itself before trusting it;
2. validate a universal lineage evidence record for data, benchmark, Gold metadata, model, synthetic/derived, and evidence-source assets;
3. distinguish source verification from exact artifact binding;
4. support direct SHA-256 and cryptographic/content-addressed revision + exact artifact locator binding;
5. evaluate one exact declared use against rights, access/privacy, split/quarantine, contamination, and synthetic/derived lineage;
6. compute — never trust from input — one scoped admission result (`ELIGIBLE`, `REFERENCE_ONLY`, `BLOCKED`, `PROHIBITED`) with deterministic reasons;
7. bind that result to the exact contract canonical identity and lineage scientific-record identity;
8. preserve canonical Spec 001 benchmark, purpose, Gold, and quarantine semantics.

No dataset/model download, external registry, network call, legal engine, database, service, or third-party dependency is required.

## 2. Minimal artifact layout

Target only:

```text
src/commandmed/eval_contract/
  lineage.py                    # contract/record validation + pure admission helpers
  canonical.py                  # only explicit set-like lineage fields if tests require
  __init__.py                   # exports only if useful

data/lineage/
  lineage_contract.json         # canonical metadata/policy contract only

tests/eval_contract/
  test_lineage.py               # fixture-only contract/lineage/admission tests

docs/governance/
  data-license-provenance.md    # reviewer-facing summary

specs/003-data-license-provenance/
  spec.md
  research.md
  plan.md
  tasks.md
  checklists/requirements.md
  analysis.md
  closeout.md                   # only after qualified implementation evidence
```

Do not modify `data/eval/benchmarks.json`, Gold payloads, model files, or external assets merely to satisfy Spec 003.

## 3. Canonical contract artifact

`data/lineage/lineage_contract.json` contains policy metadata only.

Minimum top-level shape:

```text
contract_id
schema_version
asset_classes[]
admission_states[]
declared_uses[]
artifact_binding_states[]
rights_states[]
privacy_states[]
contamination_states[]
origin_types[]
universal_required_fields[]
invariants[]
```

The contract defines closed vocabularies/invariants, not a real asset registry.

### Required contract invariants

At minimum identify rules equivalent to:

```text
CONTRACT_MUST_VALIDATE_FIRST
ADMISSION_IS_COMPUTED
SOURCE_VERIFIED_NE_ARTIFACT_BOUND
DIRECT_SHA256_BINDING_ALLOWED
CRYPTO_REVISION_LOCATOR_BINDING_ALLOWED
UNBOUND_EXACT_BYTE_USE_BLOCKED
UNCLEAR_RIGHTS_BLOCK_USE
PRIVATE_GOLD_QUARANTINED
UNKNOWN_PRIVACY_FAILS_CLOSED
UNRESOLVED_CONTAMINATION_BLOCKS_CLEAN_USE
DERIVED_ASSETS_KEEP_PARENTS
```

A contract that omits/weakens required invariants is invalid for Spec 003 admission.

## 4. Contract validation

Add a public validator:

```python
validate_lineage_contract(contract: object) -> list[str]
```

It must collect errors and never raise for ordinary malformed parsed JSON.

Reject at least:

- non-object top level;
- missing/non-string `contract_id` or `schema_version`;
- missing/empty required vocabulary arrays;
- non-string/duplicate vocabulary values;
- missing required admission states or extra unknown admission state;
- missing required binding states;
- missing/duplicate invariant IDs;
- missing required invariant IDs;
- invariant entries with malformed types/fields;
- contract attempting to allow caller-controlled admission;
- contract allowing `UNBOUND` exact-byte use;
- malformed values that would otherwise crash set/sort operations.

Record/admission evaluation first validates the contract. Invalid contract => no `ELIGIBLE` result.

## 5. Closed contract vocabularies

### Artifact binding states

Exactly:

```text
DIRECT_DIGEST
IMMUTABLE_REVISION_LOCATOR
UNBOUND
NOT_APPLICABLE
```

### Admission states

Exactly:

```text
ELIGIBLE
REFERENCE_ONLY
BLOCKED
PROHIBITED
```

### Declared uses

At minimum:

```text
REFERENCE
DEVELOPMENT_EVALUATION
PRIVATE_RELEASE_EVALUATION
TRAINING_OR_ADAPTATION
TEACHER_OR_SYNTHETIC_GENERATION
RETRIEVAL_OR_EVIDENCE_USE
MODIFICATION_OR_DERIVATION
REDISTRIBUTION
```

Other small rights/privacy/contamination/origin vocabularies may be frozen in the contract as required by the spec; do not add user-extensible plugin states.

## 6. Lineage evidence record

Prefer plain dictionaries plus small `str, Enum`/frozenset declarations; do not create a class hierarchy.

Universal evidence input fields:

```text
asset_id
asset_class
canonical_name
record_version
source_identifier
source_uri
source_revision
source_verification_status
source_evidence_uri
declared_use
access_class
rights_state
rights_evidence_uri
artifact_binding_state
```

Conditional evidence fields:

```text
artifact_locator
content_sha256
spdx_license_expression
custom_terms_id
phi_privacy_state
deidentification_state
purpose
split_id
quarantine_state
contamination_state
contamination_evidence_id
parent_asset_ids[]
origin_type
generator_identity
generation_config_id
output_use_evidence_uri
```

**Do not accept caller-owned `admission_state` / `admission_reasons` as authoritative evidence fields.** In the minimal implementation, reject them in an evidence record to make the trust boundary obvious.

## 7. Record validation

Add:

```python
validate_lineage_record(record: object, contract: object) -> list[str]
```

Behavior:

1. validate contract first;
2. validate record top-level type before set/hash/sort work;
3. enforce required strings and closed vocabularies;
4. reject self-asserted admission fields;
5. enforce conditional requirements from asset class + declared use;
6. collect deterministic errors without ordinary malformed-input exceptions.

A registry helper is optional only if duplicate-record testing benefits from it:

```python
validate_lineage_registry(records: object, contract: object) -> tuple[bool, list[str]]
```

No generic JSON Schema framework is required.

## 8. Exact artifact binding

### `DIRECT_DIGEST`

Requires exact payload:

```text
content_sha256 = exactly 64 hexadecimal characters
```

The validator may normalize case for comparison but should emit one canonical lowercase form when constructing identity.

### `IMMUTABLE_REVISION_LOCATOR`

Requires all of:

```text
source_revision = accepted cryptographic/content-addressed revision
artifact_locator = exact non-sentinel subresource locator
source_evidence_uri = non-empty evidence reference
```

For V1, conservatively accept canonical Git/Hugging Face commit-style hexadecimal revision identities (40 or 64 hexadecimal characters). Reject mutable labels and arbitrary named versions such as:

```text
main
master
latest
v1.0
release-current
```

A named version may remain reference metadata, but cannot prove this exact executable-binding mode by itself.

### `UNBOUND`

Permitted for family/reference metadata. It blocks any use whose contract requires exact payload identity.

## 9. Rights evidence

Use one exact-declared-use rights state, e.g.:

```text
SUPPORTED
CONDITIONAL
UNRESOLVED
INCOMPATIBLE
```

Rules:

- `SUPPORTED` requires rights evidence reference;
- `CONDITIONAL` / `UNRESOLVED` cannot yield `ELIGIBLE`;
- `INCOMPATIBLE` yields `PROHIBITED` for that exact declared use;
- component-specific/mixed rights cannot be widened to every component;
- optional `spdx_license_expression` is evidence metadata, not legal adjudication;
- only type/non-empty/basic-safe-string validation is required for the optional SPDX field in Spec 003 unless a complete bounded parser is separately justified;
- custom terms use exact `custom_terms_id` + evidence reference.

FD-001-dependent compatibility remains blocked when product posture is necessary.

## 10. Access/privacy boundary

Minimal states may include:

```text
NO_PHI_KNOWN
DEIDENTIFIED
RESTRICTED_OR_PHI
UNRESOLVED
NOT_APPLICABLE
```

Rules:

- `RESTRICTED_OR_PHI` cannot be repository/training/adaptation eligible under this V1 contract;
- `UNRESOLVED` blocks such uses;
- `DEIDENTIFIED` is classification metadata only and does not by itself override access/rights constraints;
- fixtures contain no real PHI/restricted content.

## 11. Purpose, split, and Gold quarantine

Reuse canonical `Purpose` values from Spec 001:

```text
TRAIN
DEV
CALIBRATION
CHECKPOINT_SELECTION
PUBLIC_EXTERNAL_EVAL
PRIVATE_GOLD
```

At minimum prove:

- `PRIVATE_GOLD` cannot be training/adaptation or teacher-generation eligible;
- test/Gold/quarantine metadata cannot claim prohibited optimization/selection use;
- `CHECKPOINT_SELECTION` remains distinct from ordinary development;
- broader Spec 003 declared uses map to, not erase, the Spec 001 purpose dimension.

Use synthetic metadata only.

## 12. Contamination boundary

Use only enough states to prevent laundering unresolved overlap into clean optimization lineage, e.g.:

```text
NOT_ASSESSED
PENDING
ASSESSED_CLEAN
OVERLAP_OR_HIGH_RISK
BLOCKED
NOT_APPLICABLE
```

For a use requiring clean separation, only `ASSESSED_CLEAN` (or explicit `NOT_APPLICABLE` when truly outside the condition) may contribute to `ELIGIBLE`.

Do not implement matching/scanning/retrieval.

## 13. Synthetic / derived lineage

For synthetic/derived classes require as applicable:

```text
parent_asset_ids[]
origin_type
generator_identity or derivation identity
generation_config_id
output_use_evidence_uri when external terms matter
```

Missing required parent/generator lineage blocks training/adaptation eligibility.

Encode project defaults so MedGemma/HAI-DEF or frontier API outputs do not become training lineage by omission.

No model/provider call occurs.

## 14. Computed admission output

Add a pure evaluator:

```python
evaluate_lineage_admission(record: object, contract: object) -> dict[str, object]
```

It:

1. validates contract;
2. validates record;
3. computes scientific record identity;
4. evaluates the exact declared use;
5. returns one admission state + sorted/deterministic reason codes;
6. returns `contract_sha256` and `record_sha256` bindings;
7. never trusts input `admission_state`;
8. never returns `ELIGIBLE` for malformed/invalid contract or record.

Suggested stable reason codes:

```text
INVALID_CONTRACT
INVALID_RECORD
SOURCE_UNVERIFIED
ARTIFACT_UNBOUND
IMMUTABLE_REVISION_INVALID
RIGHTS_UNRESOLVED
RIGHTS_INCOMPATIBLE
PRIVACY_UNRESOLVED
RESTRICTED_OR_PHI
QUARANTINE_CONFLICT
CONTAMINATION_UNRESOLVED
PARENT_LINEAGE_MISSING
```

Avoid a generic rule engine.

## 15. Scientific identity projection

Reuse `compute_canonical_sha256()` on an explicit identity-bearing projection, not on the raw record indiscriminately.

Include where applicable:

- stable asset/class identity;
- immutable source revision;
- exact artifact-binding evidence;
- declared use;
- rights evidence identity/state;
- purpose/split/quarantine identity;
- contamination evidence state/identity;
- parent/generator/configuration lineage.

Exclude explicit audit-only fields such as:

- retrieval/check timestamps;
- local paths;
- reviewer workstation metadata;
- convenience URLs/notes that do not alter governed facts.

If `parent_asset_ids` or reason-code arrays are semantically set-like, add only those explicit fields to canonical normalization.

## 16. Spec 001 compatibility proof

Do not migrate canonical benchmark JSON.

Test mapping behavior:

- canonical `DEVELOPMENT` benchmark with 40-hex source revision + concrete artifact maps to immutable-revision locator semantics;
- canonical `REFERENCE_ONLY` benchmark with `artifact_version=UNBOUND` remains non-executable;
- component-specific/unresolved rights do not broaden use.

Compatibility code may stay test-only if no runtime consumer needs an adapter yet.

## 17. Canonical documentation

Create `docs/governance/data-license-provenance.md` explaining the contract/admission trust boundary and explicit non-legal-advice/no-payload rules.

No dataset/model inventory is added.

## 18. Validation commands

Minimum local evidence:

```text
python -m unittest tests.eval_contract.test_lineage -v
python -m unittest discover -s tests -v
python -m compileall -q src tests
```

Also compute the canonical SHA-256 of `data/lineage/lineage_contract.json` through the existing canonicalizer.

Live CI truth overrides the exact local command if repository workflows differ.

## 19. Implementation order

1. contract JSON;
2. contract validator;
3. evidence-record validator;
4. cryptographic binding rules;
5. rights/privacy checks;
6. purpose/quarantine + contamination + derived-lineage checks;
7. scientific identity projection;
8. computed admission evaluator bound to contract/record identities;
9. focused tests + Spec 001 compatibility tests;
10. documentation;
11. full offline verification;
12. independent exact-head review/repair;
13. qualified implementation merge;
14. dedicated post-merge closure transition.

## 20. Risk controls

- No network/runtime dependency.
- No payload download.
- No PHI/restricted/Gold payload.
- No model execution/training.
- No rights inferred from ambiguity/SPDX text alone.
- No self-asserted admission trust.
- No named-version masquerading as immutable binding.
- No rewrite of canonical Spec 001 evidence.
- No Spec 002 repair mixed into this branch.
- No Spec 004 work.

## 21. Exit from plan

The repaired plan is ready for Analyze Pass 2 only if tasks/checklist are synchronized with these repairs. Implementation remains unauthorized until Analyze Pass 2 returns PASS.