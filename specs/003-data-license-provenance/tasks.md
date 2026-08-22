# Spec 003 Tasks — Data, License & Provenance

**Spec:** `003-data-license-provenance`
**Task status:** READY_FOR_ANALYZE
**Canonical base:** `a57f87e77bbd396332b197342d8129f6805ba452`

## T003-01 — Canonical lineage contract artifact

Create `data/lineage/lineage_contract.json` containing only controlled vocabularies and invariant metadata.

Acceptance:

- closed asset/admission/declared-use/artifact-binding vocabularies;
- no real dataset/model/Gold payload;
- canonical SHA-256 computable through existing canonicalizer;
- direct-digest and immutable-container binding represented distinctly;
- `UNBOUND` semantics explicit.

## T003-02 — Fail-closed lineage validator

Create `src/commandmed/eval_contract/lineage.py` with small enums/frozen sets and structural validation helpers.

Acceptance:

- ordinary malformed parsed JSON returns validation errors, not crashes;
- duplicate/non-string IDs fail closed;
- closed vocabularies enforced;
- conditional required fields derive from asset class + declared use;
- source verification does not imply artifact binding;
- no new third-party dependency.

## T003-03 — Binding, rights, and privacy admission rules

Implement exact-artifact, rights, access/privacy, and final admission checks.

Acceptance:

- valid direct SHA-256 binding accepted;
- valid immutable revision + exact locator binding accepted;
- unbound executable use blocked;
- unresolved/conditional rights cannot be `ELIGIBLE`;
- incompatible rights yield `PROHIBITED` for exact declared use;
- unknown/restricted PHI state cannot be repository/training eligible;
- admission reasons are deterministic and machine-readable.

## T003-04 — Purpose/quarantine, contamination, and derived lineage

Extend the validator/evaluator only enough to enforce Spec 003 cross-cutting lineage constraints.

Acceptance:

- canonical `Purpose` values reused;
- private Gold/test/quarantine conflicts fail closed;
- `CHECKPOINT_SELECTION` remains distinct from ordinary dev;
- unresolved contamination blocks use requiring clean separation;
- synthetic/derived assets require parent/generator/configuration lineage where applicable;
- MedGemma/HAI-DEF/frontier-output training defaults are not silently weakened.

## T003-05 — Scientific identity projection

Add the minimum helper required to compute a lineage scientific identity with `compute_canonical_sha256()`.

Acceptance:

- representation-only set ordering does not change identity;
- audit timestamp/local-path changes do not change identity when excluded by the explicit projection;
- source revision, artifact binding, declared use, rights evidence, split/purpose, contamination evidence, or parent lineage changes do change identity when applicable;
- no global arbitrary-field ignore mechanism is introduced.

## T003-06 — Spec 001 compatibility proof

Add tests that map canonical benchmark semantics without modifying `data/eval/benchmarks.json`.

Acceptance:

- executable `DEVELOPMENT` benchmark with concrete revision + artifact maps to immutable-container binding;
- `REFERENCE_ONLY` + `UNBOUND` remains non-executable;
- component-specific/unresolved rights do not broaden admission;
- full existing eval-contract suite remains green.

## T003-07 — Documentation and contract review surface

Create `docs/governance/data-license-provenance.md` and expose only the minimal public helpers if an export is useful.

Acceptance:

- source verification vs artifact binding clearly documented;
- rights/privacy/quarantine/contamination/derived lineage explained;
- design-evidence standards named without claiming adoption/dependency;
- non-legal-advice and no-payload boundaries explicit;
- no speculative registry/service/API surface.

## T003-08 — Exact-head verification and reconciliation

Run the bounded verification set on the final candidate head.

Required evidence:

```text
python -m unittest tests.eval_contract.test_lineage -v
python -m unittest discover -s tests -v
python -m compileall -q src tests
```

Also record:

- exact candidate SHA;
- changed-path inventory;
- canonical lineage-contract SHA-256;
- no prohibited payload/model/training/PHI/Gold/gated access;
- independent exact-head review findings and reconciliation.

T003-08 does not authorize merge by itself.

## T003-09 — Canonical implementation and dedicated closure

Only after T003-08 proves every gate:

1. merge the qualified implementation PR without rewriting history;
2. verify resulting canonical `main`;
3. create a dedicated closure-only transition that binds qualification evidence to the canonical implementation merge;
4. only after closure is merged and verified may Spec 003 become `CLOSED_CANONICAL` and Spec 004 become eligible for separate authorization.

## Task dependency order

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
```

## Explicitly blocked

- Spec 004 Tournament Harness;
- any benchmark/model execution;
- any training or teacher generation;
- PHI/restricted/private-Gold/gated payload access;
- final model selection;
- FD-001 resolution before needed.
