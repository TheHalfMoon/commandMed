# Spec 003 Tasks — Data, License & Provenance

**Spec:** `003-data-license-provenance`
**Task status:** REPAIRED_READY_FOR_ANALYZE_PASS_2
**Canonical base:** `a57f87e77bbd396332b197342d8129f6805ba452`

## T003-01 — Canonical lineage contract artifact

Create `data/lineage/lineage_contract.json` containing only controlled vocabularies and invariant metadata.

Acceptance:

- closed asset/admission/declared-use/artifact-binding vocabularies;
- required invariant IDs are explicit;
- no real dataset/model/Gold payload;
- canonical SHA-256 computable through existing canonicalizer;
- direct SHA-256 and cryptographic immutable-revision locator binding represented distinctly;
- `UNBOUND` exact-byte use blocked;
- admission is defined as computed output, not caller evidence.

## T003-02 — Fail-closed contract validator

Implement `validate_lineage_contract(contract)` in `src/commandmed/eval_contract/lineage.py`.

Acceptance:

- malformed/non-object contract returns errors rather than raising;
- required vocabularies and invariant IDs are enforced;
- duplicate/non-string vocabulary values fail closed;
- missing/weakened exact-binding or computed-admission invariants fail;
- invalid contract can never authorize `ELIGIBLE`.

## T003-03 — Fail-closed lineage evidence validator

Implement `validate_lineage_record(record, contract)`.

Acceptance:

- contract validation occurs first;
- ordinary malformed parsed JSON returns errors, not crashes;
- duplicate/non-string IDs and closed-vocabulary violations fail;
- conditional fields derive from asset class + declared use;
- source verification does not imply artifact binding;
- caller-supplied `admission_state` / `admission_reasons` are rejected as non-evidence fields;
- no new third-party dependency.

## T003-04 — Cryptographic binding, rights, and privacy rules

Implement exact-artifact, rights, and access/privacy checks.

Acceptance:

- valid direct SHA-256 binding accepted;
- 40/64-hex cryptographic/content-addressed revision + exact locator + evidence accepted for immutable-container binding;
- mutable/named revisions (`main`, `latest`, `v1.0`, etc.) cannot satisfy immutable binding;
- unbound exact-byte use blocked;
- unresolved/conditional rights cannot be `ELIGIBLE`;
- incompatible rights yield `PROHIBITED` for exact declared use;
- optional SPDX expression is evidence metadata only and cannot independently authorize use;
- unknown/restricted PHI state cannot be repository/training eligible.

## T003-05 — Purpose/quarantine, contamination, and derived lineage

Extend the validator/evaluator only enough to enforce cross-cutting lineage constraints.

Acceptance:

- canonical `Purpose` values reused;
- private Gold/test/quarantine conflicts fail closed;
- `CHECKPOINT_SELECTION` remains distinct from ordinary dev;
- unresolved contamination blocks use requiring clean separation;
- synthetic/derived assets require parent/generator/configuration lineage where applicable;
- MedGemma/HAI-DEF/frontier-output training defaults are not silently weakened.

## T003-06 — Scientific identity projection

Add a narrow identity projection and reuse `compute_canonical_sha256()`.

Acceptance:

- representation-only set ordering does not change identity;
- audit timestamp/local-path changes do not change identity when explicitly excluded;
- source revision, artifact binding, declared use, rights evidence, split/purpose, contamination evidence, or parent lineage changes do change identity when applicable;
- no global arbitrary-field ignore mechanism is introduced.

## T003-07 — Computed admission evaluator

Implement `evaluate_lineage_admission(record, contract)` as evaluator-owned output.

Acceptance:

- invalid contract => never `ELIGIBLE`;
- invalid record => never `ELIGIBLE`;
- caller cannot self-assert eligibility;
- result contains exactly one closed admission state;
- reason codes are deterministic;
- result binds `contract_sha256` and `record_sha256`;
- evaluation is scoped to exact declared use and infers no broader permission.

## T003-08 — Spec 001 compatibility proof

Add tests mapping canonical benchmark semantics without modifying `data/eval/benchmarks.json`.

Acceptance:

- executable `DEVELOPMENT` benchmark with cryptographic source revision + concrete artifact maps to immutable-revision locator semantics;
- `REFERENCE_ONLY` + `UNBOUND` remains non-executable;
- component-specific/unresolved rights do not broaden admission;
- full existing eval-contract suite remains green.

## T003-09 — Documentation and review surface

Create `docs/governance/data-license-provenance.md` and expose only minimal public helpers if useful.

Acceptance:

- contract-validation trust boundary documented;
- source verification vs cryptographic artifact binding documented;
- computed-admission boundary documented;
- rights/privacy/quarantine/contamination/derived lineage explained;
- standards named as design evidence, not dependencies/legal authority;
- no speculative registry/service/API surface.

## T003-10 — Exact-head verification and reconciliation

Required evidence on final implementation head:

```text
python -m unittest tests.eval_contract.test_lineage -v
python -m unittest discover -s tests -v
python -m compileall -q src tests
```

Also record:

- exact candidate SHA;
- changed-path inventory;
- canonical lineage-contract SHA-256;
- contract-invalid, self-asserted-admission, mutable-revision, malformed-input negative tests;
- no prohibited payload/model/training/PHI/Gold/gated access;
- independent exact-head review findings and reconciliation.

T003-10 does not authorize merge by itself.

## T003-11 — Canonical implementation and dedicated closure

Only after T003-10 proves every gate:

1. merge the qualified implementation PR without history rewriting;
2. verify resulting canonical `main`;
3. create a dedicated closure-only transition binding qualification evidence to the canonical implementation merge;
4. only after closure is merged and verified may Spec 003 become `CLOSED_CANONICAL` and Spec 004 become eligible for separate authorization.

## Dependency order

```text
T003-01
  -> T003-02
  -> T003-03
  -> T003-04
  -> T003-05
  -> T003-06
  -> T003-07
  -> T003-08
  -> T003-09
  -> T003-10
  -> T003-11
```

## Explicitly blocked

- Spec 004 Tournament Harness;
- any benchmark/model execution;
- any training or teacher generation;
- PHI/restricted/private-Gold/gated payload access;
- final model selection;
- FD-001 resolution before needed.
