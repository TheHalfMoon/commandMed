# Spec 003 Plan — Data, License & Provenance

**Spec:** `003-data-license-provenance`
**Plan status:** READY_FOR_CHECKLIST_TASKS_ANALYZE
**Canonical base:** `a57f87e77bbd396332b197342d8129f6805ba452`
**Implementation style:** metadata-only, fixture-only, offline, deterministic, Python 3.11 standard library; reuse Spec 001 canonicalization and purpose/quarantine semantics

## 1. Technical objective

Implement the smallest machine-verifiable lineage layer that can:

1. validate a universal lineage envelope for data, benchmark, Gold metadata, model, synthetic/derived, and evidence-source assets;
2. distinguish source verification from exact artifact binding;
3. support both direct-digest and immutable-revision-plus-artifact-locator exact binding;
4. evaluate one exact declared use against rights, access/privacy, split/quarantine, contamination, and synthetic/derived lineage;
5. return a closed admission result (`ELIGIBLE`, `REFERENCE_ONLY`, `BLOCKED`, `PROHIBITED`) with machine-readable reasons;
6. preserve canonical Spec 001 benchmark, purpose, Gold, and quarantine semantics;
7. produce deterministic canonical lineage/contract identities using the existing canonicalizer.

No dataset/model download, external registry, network call, legal engine, database, service, or third-party dependency is required.

## 2. Minimal artifact layout

Target only:

```text
src/commandmed/eval_contract/
  lineage.py                    # closed vocabularies + validation/admission helpers
  canonical.py                  # only add explicit set-like lineage fields if required
  __init__.py                   # exports only if useful to tests/callers

data/lineage/
  lineage_contract.json         # canonical machine-readable policy/contract artifact

tests/eval_contract/
  test_lineage.py               # fixture-only lineage/admission/identity tests

docs/governance/
  data-license-provenance.md    # reviewer-facing contract summary

specs/003-data-license-provenance/
  spec.md
  research.md
  plan.md
  tasks.md
  checklists/requirements.md
  analysis.md
  closeout.md                   # only after qualified implementation evidence
```

Do not modify `data/eval/benchmarks.json`, Gold payloads, model files, or external assets to make tests pass.

## 3. Canonical contract artifact

`data/lineage/lineage_contract.json` is metadata/policy only and contains no external payloads.

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

The policy artifact defines closed vocabularies and invariant identities, not a registry of real datasets/models.

### Artifact binding states

Use the minimum semantics:

```text
DIRECT_DIGEST
IMMUTABLE_REVISION_LOCATOR
UNBOUND
NOT_APPLICABLE
```

`DIRECT_DIGEST` requires a syntactically valid SHA-256 identity.

`IMMUTABLE_REVISION_LOCATOR` requires a non-empty immutable source revision plus exact artifact locator.

`UNBOUND` cannot become `ELIGIBLE` for a declared use that requires exact payload identity.

### Admission states

Exactly:

```text
ELIGIBLE
REFERENCE_ONLY
BLOCKED
PROHIBITED
```

The validator/evaluator must return reasons separately; admission is not a mega-status replacing lineage dimensions.

## 4. Lineage record model

Prefer plain dictionaries plus small `str, Enum` declarations/frozen sets rather than a large dataclass hierarchy.

Universal fields:

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
admission_state
admission_reasons[]
```

Conditional fields are required from asset class + declared use, never by meaningless placeholders:

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
generator_identity
generation_config_id
output_use_evidence_uri
```

The exact implementation may use fewer names if equivalent semantics are preserved and tests remain explicit.

## 5. Validation architecture

Implement one small public entry point such as:

```python
validate_lineage_record(record: object, contract: object) -> list[str]
```

and one registry helper if needed:

```python
validate_lineage_registry(records: object, contract: object) -> tuple[bool, list[str]]
```

Validation collects actionable errors and does not raise on ordinary malformed parsed JSON.

Required checks include:

- top-level/object/list type validation before hashing/set/sort operations;
- required non-empty string fields;
- closed-vocabulary membership;
- duplicate stable IDs;
- admission-reason list type/uniqueness;
- exact artifact-binding invariants;
- rights evidence consistency;
- privacy/PHI fail-closed behavior;
- purpose/split/quarantine consistency;
- contamination requirements;
- parent/generator lineage for derived/synthetic assets;
- final admission consistency.

Do not add a generic schema framework or JSON Schema dependency.

## 6. Exact artifact binding

A helper such as `validate_artifact_binding(record)` should enforce:

### `DIRECT_DIGEST`

Requires:

```text
content_sha256 = 64 lowercase/uppercase hexadecimal characters
```

An artifact locator/source revision may also exist, but the digest is the binding proof.

### `IMMUTABLE_REVISION_LOCATOR`

Requires:

```text
source_revision = concrete, non-sentinel string
artifact_locator = concrete, non-sentinel string
```

No redundant direct digest is required.

### `UNBOUND`

Permitted for source/family/reference metadata. It blocks any use whose contract requirement says exact payload identity is required.

This rule is explicitly tested against synthetic records shaped like canonical Spec 001 benchmark semantics.

## 7. Rights model

Do not attempt legal reasoning from arbitrary prose.

Use a small evidence state for the exact declared use, for example:

```text
SUPPORTED
CONDITIONAL
UNRESOLVED
INCOMPATIBLE
```

Rules:

- `SUPPORTED` requires a rights evidence reference;
- `CONDITIONAL` and `UNRESOLVED` cannot yield `ELIGIBLE`;
- `INCOMPATIBLE` yields `PROHIBITED` for that declared use;
- component-specific/mixed rights cannot be widened to all components;
- optional `spdx_license_expression` must have conservative syntax validation only; do not implement the full SPDX grammar unless standard-library validation stays small and defensible;
- custom/non-standard terms use an exact `custom_terms_id`/evidence reference rather than pretending to be a standard license.

FD-001-dependent compatibility remains `BLOCKED` when the final product posture is required.

## 8. Access/privacy boundary

Use minimal privacy states sufficient to fail closed, for example:

```text
NO_PHI_KNOWN
DEIDENTIFIED
RESTRICTED_OR_PHI
UNRESOLVED
NOT_APPLICABLE
```

For any repository-payload or training/adaptation eligibility path:

- `RESTRICTED_OR_PHI` => not eligible;
- `UNRESOLVED` => blocked;
- no fixture contains real PHI or restricted content.

This is metadata classification, not de-identification software.

## 9. Purpose, split, and Gold quarantine

Do not duplicate the Spec 001 purpose engine.

Where `purpose` is present, validate against canonical `Purpose` values.

At minimum prove:

- `PRIVATE_GOLD` cannot be training/adaptation or teacher-generation eligible;
- a record explicitly marked as test/Gold/quarantined cannot claim a prohibited optimization/selection use;
- existing `CHECKPOINT_SELECTION` remains distinct from ordinary development;
- broader Spec 003 declared-use values map to, rather than erase, the Spec 001 purpose dimension.

Use synthetic metadata only.

## 10. Contamination boundary

The minimum contract needs only enough semantics to prevent laundering unresolved overlap into clean optimization lineage.

Prefer a closed state such as:

```text
NOT_ASSESSED
PENDING
ASSESSED_CLEAN
OVERLAP_OR_HIGH_RISK
BLOCKED
NOT_APPLICABLE
```

For a declared use requiring clean separation, only `ASSESSED_CLEAN`/explicitly compatible state may contribute to `ELIGIBLE`.

Do not implement fuzzy matching, embedding similarity, corpus scanning, or benchmark retrieval in Spec 003.

## 11. Synthetic / derived lineage

For `MODEL_GENERATED_OR_SYNTHETIC_ASSET` and `DERIVED_RESEARCH_ARTIFACT`, require where applicable:

```text
parent_asset_ids[]
origin_type
generator_identity or derivation identity
generation_config_id when scientifically relevant
output_use_evidence_uri when external model/provider terms matter
```

Tests must prove that missing parent/generator lineage blocks training/adaptation eligibility.

The contract must encode the canonical default that MedGemma/HAI-DEF outputs and frontier API outputs are not automatically training lineage.

Do not call any model/provider.

## 12. Admission evaluation

Implement a pure function such as:

```python
evaluate_lineage_admission(record: object, contract: object) -> dict[str, object]
```

The function:

1. validates first;
2. never returns `ELIGIBLE` for malformed input;
3. evaluates only the exact `declared_use` in the record;
4. returns one admission state and deterministic reason codes;
5. does not infer permissions outside recorded evidence;
6. does not treat source verification as sufficient by itself.

Suggested reason codes should be stable and narrow, e.g.:

```text
ARTIFACT_UNBOUND
RIGHTS_UNRESOLVED
RIGHTS_INCOMPATIBLE
PRIVACY_UNRESOLVED
RESTRICTED_OR_PHI
QUARANTINE_CONFLICT
CONTAMINATION_UNRESOLVED
PARENT_LINEAGE_MISSING
SOURCE_UNVERIFIED
```

Avoid a general rule engine.

## 13. Canonical identity

Reuse `compute_canonical_sha256()`.

If new set-like fields need order normalization, add only the explicit fields required by lineage tests, likely:

```text
admission_reasons
parent_asset_ids
```

Do not globally sort lists whose order may be scientifically meaningful.

Tests must distinguish:

- representation-only reorder => same digest;
- audit-only timestamp/local-path change => same scientific identity if those fields are explicitly excluded before hashing;
- source revision/artifact binding/declared use/rights evidence/split/parent change => different digest.

Prefer a small helper that constructs the identity-bearing projection before calling the existing canonicalizer rather than teaching the global canonicalizer to ignore arbitrary fields.

## 14. Compatibility proof

Do not migrate `data/eval/benchmarks.json`.

Add a compatibility adapter/test that proves at least:

- a canonical `DEVELOPMENT` benchmark with concrete `source_revision` + `artifact_version` can map to `IMMUTABLE_REVISION_LOCATOR` semantics;
- a canonical `REFERENCE_ONLY` benchmark with `artifact_version=UNBOUND` maps to non-executable/reference-only semantics;
- `COMPONENT_SPECIFIC`/`UNRESOLVED` rights do not become broader eligible use.

Compatibility code may be test-only if no runtime consumer needs a permanent adapter yet.

## 15. Documentation

`docs/governance/data-license-provenance.md` should explain:

- source verification vs artifact binding;
- exact-binding alternatives;
- declared-use/admission scope;
- rights and privacy fail-closed semantics;
- Gold/quarantine and contamination boundaries;
- synthetic/derived parentage;
- standards used as design evidence but not dependencies;
- explicit non-legal-advice boundary.

No dataset/model inventory is added in this spec.

## 16. Validation commands

Use existing repository style and standard-library tests. Minimum evidence should include:

```text
python -m unittest tests.eval_contract.test_lineage -v
python -m unittest discover -s tests -v
python -m compileall -q src tests
```

Also compute the canonical SHA-256 of `data/lineage/lineage_contract.json` through the existing canonicalizer.

If the repository's live CI uses a different exact command, live workflow truth overrides this plan.

## 17. Implementation order

1. canonical contract JSON;
2. `lineage.py` closed vocabularies + structural validator;
3. artifact-binding + rights/privacy checks;
4. purpose/quarantine + contamination + derived-lineage checks;
5. admission evaluator;
6. canonical identity projection/helper;
7. focused tests including Spec 001 compatibility;
8. documentation;
9. full offline verification;
10. independent exact-head review and repair;
11. implementation merge only after every gate passes;
12. dedicated closure transition afterward.

## 18. Risk controls

- No network/runtime dependency.
- No payload download.
- No PHI/restricted/Gold payload.
- No model execution/training.
- No license permission inferred from ambiguity.
- No rewrite of canonical Spec 001 evidence.
- No Spec 002 repair mixed into this branch.
- No Spec 004 work.

## 19. Exit from plan

Plan is acceptable only if checklist/tasks/analyze prove:

- every Spec 003 FR has an implementation/test path;
- the direct-digest vs immutable-container identity rule is internally consistent;
- canonical Spec 001 semantics are preserved;
- no founder decision is required yet;
- no prohibited runtime/data/model action is needed;
- the implementation remains bounded to the minimal artifact set above.