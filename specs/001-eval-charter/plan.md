# Spec 001 Plan — Evaluation Charter

**Spec:** `001-eval-charter`
**Plan status:** READY_FOR_ANALYZE
**Implementation style:** fixture-only, offline, deterministic, Python 3.11 standard library unless analysis proves otherwise

## 1. Technical objective

Implement the smallest local mechanism that can:

1. represent and validate benchmark/metric/Gold/quarantine metadata;
2. deterministically canonicalize those artifacts;
3. compute stable SHA-256 identities;
4. prove hard-gate dominance and prohibited-use rules using fixtures;
5. emit reviewable closeout evidence.

No model framework, ML library, database, service, or network runtime is required.

## 2. Proposed minimal artifact layout

The implementation phase may create only what is needed, with a target layout similar to:

```text
src/commandmed/eval_contract/
  __init__.py
  model.py
  validate.py
  canonical.py

data/eval/
  benchmarks.json
  metrics.json
  gold_protocols.json
  quarantine.json

tests/eval_contract/
  test_registry.py
  test_hard_gates.py
  test_gold_quarantine.py
  test_canonical.py

docs/evaluation/
  benchmark-registry.md
  metrics-and-gates.md
  gold-and-quarantine.md
```

This is a target, not permission to add packaging/framework files that are not required to run the spec. During `analyze`, Antigravity should reduce or adjust the layout if the same guarantees can be met more simply.

## 3. Data representation

Prefer JSON for canonical source artifacts because Python stdlib can parse it and canonical JSON can be serialized deterministically.

Rules:

- UTF-8;
- sorted object keys for canonical output;
- compact canonical separators;
- explicit arrays preserve semantic order only where order is meaningful;
- duplicate stable IDs rejected at validation;
- enums validated against closed allowed sets;
- unknown facts represented explicitly (for example `UNRESOLVED`) rather than omitted when required;
- no environment-specific paths/timestamps in identity unless semantically required.

Do not add JSON Schema or Pydantic unless a concrete requirement cannot be satisfied cleanly with standard-library validation.

## 4. Python design

Prefer a few immutable/frozen dataclasses or TypedDict-like explicit parsing functions over a hierarchy/framework.

Likely responsibilities:

- `model.py`: small enums/data records used by validation;
- `validate.py`: fail-closed semantic validation;
- `canonical.py`: canonical serialization and SHA-256 digest;
- tests directly construct fixture objects or load tiny local fixtures.

Avoid:

- ORM;
- plugin registry;
- dependency injection framework;
- dynamic class loading;
- custom DSL;
- web API;
- database;
- CLI framework.

A tiny stdlib CLI is optional only if needed for acceptance/closeout; tests can be sufficient.

## 5. Benchmark registry population

Research/population step (not runtime):

For every initial benchmark family in FR-002:

1. identify primary/current canonical source;
2. record exact display name and stable project ID;
3. record verification date;
4. record artifact/version/access state known at that date;
5. record license/use status as known, including `UNRESOLVED` when necessary;
6. classify languages, roles, modalities, capability domains;
7. record contamination sensitivity and intended commandMed use.

Do not fetch or store benchmark case content in this spec.

The registry's purpose is to stop name drift and phantom assets, not to clone datasets.

## 6. Metrics and hard gates

Represent metric definitions separately from thresholds where threshold evidence is not ready.

Metric record should support at least:

- stable metric ID;
- description;
- direction (`HIGHER_BETTER`, `LOWER_BETTER`, `TARGET_RANGE`);
- unit/scale;
- aggregation notes;
- hard-gate boolean;
- threshold state;
- applicable roles/modalities/languages;
- required evidence/reviewer type where relevant.

Hard-gate evaluator semantics:

- any evaluated hard gate with failure => overall `FAIL`;
- unknown/not-evaluated hard gates cannot be converted to `PASS`;
- aggregate utility metrics are reported separately and cannot override hard gates.

Do not invent clinical threshold numbers in Spec 001.

## 7. Gold protocols

Store metadata only.

Each Gold family record should include:

- stable family ID;
- purpose;
- intended strata;
- content location policy (not payload);
- allowed access roles;
- adjudication/reviewer policy;
- power-analysis required = true;
- prohibited optimization uses;
- permitted scoring stage(s);
- release-claim scope;
- identity/access audit expectations.

Tests must ensure a Gold protocol cannot authorize training/selection uses.

## 8. Quarantine model

Define a small closed set of logical purposes, such as:

- `TRAIN`
- `DEV`
- `CALIBRATION`
- `CHECKPOINT_SELECTION`
- `PUBLIC_EXTERNAL_EVAL`
- `PRIVATE_GOLD`

Define allowed/prohibited flows as data or explicit code, whichever is smaller and clearer.

Hard prohibition: `PRIVATE_GOLD` cannot flow into optimization/selection purposes.

Contamination metadata should include exact-match identity status plus a semantic-overlap assessment status/interface. No embedding model is built here.

## 9. Canonical identity

Canonicalization function:

1. validate semantic object;
2. normalize only explicitly allowed representation differences;
3. JSON serialize with deterministic ordering/encoding;
4. SHA-256 over exact canonical bytes.

Tests:

- same semantic data in different input key order => same canonical bytes/digest;
- changed semantic value => different digest;
- invalid object => no digest promoted.

## 10. Test strategy

Use Python stdlib `unittest` unless the repository bootstrap introduces an already-approved test runner for a clear reason.

Minimum required test groups:

1. registry valid/invalid/duplicate/unknown-state cases;
2. hard-gate dominance;
3. Gold prohibited-use enforcement;
4. quarantine purpose validation;
5. deterministic serialization;
6. semantic mutation changes digest;
7. fixtures contain no prohibited patient/benchmark payload markers as defined by the spec.

Tests must run offline.

## 11. Documentation generation

Prefer hand-authored concise Markdown derived from the same registry identities rather than building a documentation generator unless drift becomes a demonstrated problem.

If a generated summary is truly needed, implement one simple deterministic renderer; do not add a template engine.

## 12. Source verification evidence

Spec 001 may record primary-source references and verification notes. It should not introduce a crawler/scraper. Source verification is bounded research performed while populating the registry.

If an external suite cannot be verified:

- mark `UNRESOLVED`;
- exclude it from executable comparison/gate status;
- document what is missing.

Do not fabricate a substitute benchmark.

## 13. Security/privacy review

Even fixture-only code must enforce:

- no PHI/restricted case content in repository fixtures;
- no network calls from validator/tests;
- no arbitrary code execution from registry fields;
- no path traversal/file inclusion mechanism;
- no secret fields.

Spec 001 should not require credentials.

## 14. Implementation order

1. Reconcile Spec Kit initialization and run `analyze`.
2. Create minimal package/layout required to run tests.
3. Define closed enums/records and validators.
4. Implement canonical serialization/digest.
5. Add registry/metric/Gold/quarantine fixture artifacts.
6. Add tests proving normal and fail-closed behavior.
7. Populate initial verified benchmark metadata from primary sources without case content.
8. Write concise evaluation docs.
9. Run full Spec 001 validation.
10. Produce closeout evidence bound to exact HEAD/artifact digests.

## 15. Expected validation commands

The exact commands depend on the reconciled repository bootstrap, but the preferred minimal path is stdlib-only, for example:

```bash
python -m unittest discover -s tests -p 'test_*.py'
```

Any additional lint/type/test dependency must be justified rather than added automatically.

## 16. Exit evidence

A closeout report must show:

- exact git HEAD and tree/changed paths;
- test command/results;
- canonical SHA-256 digests of evaluation-governance artifacts;
- list of initial benchmark records and their verification states;
- acceptance criteria matrix;
- unresolved facts/risks;
- confirmation of zero model downloads/inference/training and zero PHI/Gold content;
- `SPEC_002_PLUS=NOT_STARTED`.

## 17. Analyze questions

Before implementation, Spec Kit `analyze`/review must answer:

- Does any proposed file/dependency exceed Spec 001 scope?
- Are all hard-gate semantics consistent with the constitution?
- Can standard library satisfy the contract?
- Does any registry field accidentally invite protected content into the repository?
- Is Gold separation enforceable without storing Gold payload?
- Are unknown licenses/facts represented honestly?
- Are implementation tasks independently verifiable and dependency ordered?

If any answer reveals a material conflict, repair spec/plan/tasks before implementation.
