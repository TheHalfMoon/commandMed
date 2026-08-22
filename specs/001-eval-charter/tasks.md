# Spec 001 Tasks — Evaluation Charter

**State:** ACTIVE (IMPLEMENTATION_COMPLETE_CANDIDATE)

Execute in dependency order. Do not start a later task merely because its files are obvious.

## T001 — Reconcile Spec Kit bootstrap

**Goal:** Ensure `agy` Spec Kit skills/scripts exist without overwriting commandMed canonical planning authority.

**Actions:**

- verify exact branch/HEAD and clean/known worktree;
- initialize pinned Spec Kit integration according to `docs/antigravity-execution.md`;
- inspect all generated diffs affecting `AGENTS.md`, `.specify`, `.agents`, `docs`, or `specs`;
- preserve/reconcile commandMed constitution and agent rules;
- run planning consistency analysis.

**Acceptance:**

- canonical planning content preserved;
- valid Spec Kit `agy` skills available;
- no unexplained generated mutation remains;
- analysis has no unresolved material contradiction.

**Hard stop:** any canonical-file destructive overwrite that cannot be safely reconciled.

---

## T002 — Create minimal evaluation-contract structure

**Depends on:** T001

**Goal:** Establish only the files/module structure needed for Spec 001 validation.

**Actions:**

- use the smallest Python 3.11-compatible package/test layout;
- do not add ML/model frameworks;
- avoid third-party dependencies unless analysis records a requirement.

**Acceptance:**

- Python imports/tests can run offline;
- changed paths remain within Spec 001 needs.

---

## T003 — Implement registry and contract validation

**Depends on:** T002

**Goal:** Fail-closed validation for benchmark, metric, Gold-protocol, quarantine and contamination metadata.

**Required behaviors:**

- required-field validation;
- closed enum validation;
- duplicate stable-ID rejection;
- explicit unresolved-state support;
- prohibited Gold-use rejection;
- no arbitrary code/path execution from metadata.

**Acceptance:** synthetic valid fixtures pass; targeted invalid fixtures fail for the expected reason.

---

## T004 — Implement hard-gate semantics

**Depends on:** T003

**Goal:** Prove critical-gate dominance over aggregate quality.

**Acceptance fixtures:**

- high aggregate + one failed hard gate => overall `FAIL`;
- all evaluated hard gates pass => not failed by hard-gate layer;
- required hard gate not evaluated => never silently `PASS`.

No clinical numeric thresholds are invented in this task.

---

## T005 — Implement canonical serialization and identity

**Depends on:** T003

**Goal:** Create deterministic canonical bytes and SHA-256 identities for validated evaluation-governance artifacts.

**Acceptance:**

- key-order-only input differences produce same canonical bytes/digest;
- semantic mutation changes digest;
- invalid data cannot produce a promoted digest;
- runtime path/time/machine details do not alter identity unless explicitly semantic.

---

## T006 — Populate initial benchmark registry metadata

**Depends on:** T003

**Goal:** Record current verified metadata without downloading/storing benchmark content.

**Minimum families:**

- MedHELM;
- HealthBench / Hard / Consensus / Professional;
- MedXpertQA text/multimodal;
- MedQA;
- MedMCQA;
- PubMedQA;
- MedQAbstain;
- MedAbstain.

**Rules:**

- primary/current source required for `VERIFIED`;
- unresolved license/version/access facts remain explicit;
- no copied question/case payload;
- no network dependency in runtime validators/tests.

**Acceptance:** every minimum family is either verified with evidence metadata or explicitly unresolved/excluded with reason.

---

## T007 — Define metrics, Gold, quarantine and contamination artifacts

**Depends on:** T003, T004

**Goal:** Materialize the governance data defined by the spec.

**Artifacts include:**

- metric categories/hard-gate metadata;
- three Gold family protocols without cases;
- purpose/quarantine rules;
- contamination evidence/interface fields.

**Acceptance:** validators reject prohibited Gold optimization/selection use and invalid purpose flows.

---

## T008 — Complete fixture-only test suite

**Depends on:** T004, T005, T006, T007

**Goal:** Prove required pass/fail/determinism behavior offline.

**Required coverage:**

- valid registry;
- missing field;
- duplicate ID;
- invalid state;
- hard-gate dominance;
- Gold quarantine;
- deterministic canonicalization;
- semantic digest mutation;
- no prohibited case payload in fixtures.

**Acceptance:** all tests pass with exact command recorded.

---

## T009 — Write concise evaluation governance documentation

**Depends on:** T006, T007

**Goal:** Make machine contracts independently reviewable without building a documentation system.

**Minimum docs:**

- benchmark registry/status summary;
- metrics/hard-gate semantics;
- Gold/quarantine/contamination rules.

**Acceptance:** docs match machine identities/terminology and do not overstate unresolved facts.

---

## T010 — Spec 001 closeout evidence

**Depends on:** T008, T009

**Goal:** Prove the bounded spec candidate, not merely code completion.

**Report must include:**

- two-layer evidence protocol (in-tree candidate evidence + PR review candidate HEAD);
- exact changed paths;
- validation/test commands and output summary;
- canonical artifact SHA-256 identities;
- acceptance criteria PASS/FAIL matrix;
- unresolved facts/risks;
- explicit zero-model/zero-training/zero-PHI/zero-Gold-content attestations;
- `SPEC_002_PLUS=NOT_STARTED`.

**Exit:** Spec 001 may be submitted as `CLOSEOUT_CANDIDATE` for independent review. State becomes `CLOSED_CANONICAL` only via dedicated post-merge closure PR. Do not start Spec 002.
