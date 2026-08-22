# Data, License & Provenance — Spec 003

## Status

Spec 003 defines a metadata-only, machine-verifiable lineage contract for commandMed research assets.

It does **not** authorize data/model downloads, benchmark execution, model execution, training, teacher/API generation, PHI/restricted-data access, private-Gold payload access, gated-asset access, or Spec 004 tournament work.

The canonical contract is:

```text
data/lineage/lineage_contract.json
```

The validator/evaluator is:

```text
src/commandmed/eval_contract/lineage.py
```

## Trust boundary

There are three distinct objects:

1. **Lineage contract** — closed vocabularies and invariants. It must validate before it can govern anything.
2. **Lineage evidence record** — source, rights, access/privacy, artifact-binding, split/quarantine, contamination, and derivation evidence for one exact declared use.
3. **Computed admission result** — evaluator-owned output. A caller cannot self-assert `ELIGIBLE`, `record_sha256`, or an equivalent scientific identity.

An invalid/weakened contract or malformed record fails closed and cannot produce `ELIGIBLE`.

## Source verification is not artifact binding

A source or benchmark family may be `VERIFIED` while its executable payload is still `UNBOUND`.

Spec 003 therefore keeps two questions separate:

- Is this the source/family we think it is?
- Are the exact bytes/subresource for the declared use identity-bound?

Source verification alone never answers the second question.

## Exact artifact binding

A use requiring exact payload identity has two valid V1 binding modes.

### Direct digest

`DIRECT_DIGEST` requires a SHA-256 digest of the exact payload bytes.

### Immutable revision + exact locator

`IMMUTABLE_REVISION_LOCATOR` requires:

- an accepted content-addressed/cryptographic source revision;
- an exact artifact/subresource locator inside that revision; and
- source evidence for the revision.

For V1, commandMed conservatively accepts canonical Git/Hugging Face commit-style 40- or 64-hex revisions for this binding mode.

Named or mutable labels such as `main`, `master`, `latest`, `v1.0`, or `release-current` are useful reference metadata but do **not** prove immutable executable identity by themselves.

### Unbound

`UNBOUND` is a truthful state. It may describe a verified family/reference asset, but it cannot satisfy a declared use that requires exact payload identity.

This preserves the canonical Spec 001 benchmark rule: a verified family is not automatically an executable benchmark.

## Rights and license evidence

The lineage record keeps the exact declared-use rights state separate from the source's descriptive license metadata.

V1 rights states are:

```text
SUPPORTED
CONDITIONAL
UNRESOLVED
INCOMPATIBLE
```

Rules are fail-closed:

- `SUPPORTED` requires evidence;
- `CONDITIONAL` and `UNRESOLVED` cannot produce `ELIGIBLE`;
- `INCOMPATIBLE` produces `PROHIBITED` for that exact declared use;
- framework/repository licenses do not automatically license separately distributed components or data;
- component-specific/mixed rights cannot be widened by relabeling.

An optional SPDX License Expression is evidence metadata only. Spec 003 does not claim that a partial syntax check proves legal correctness, SPDX-list membership, or compatibility with commandMed's final product posture.

FD-001 therefore remains deferred until final release/product posture is actually required.

This document and validator are governance/research controls, **not legal advice**.

## Access, privacy, and PHI

Privacy/access metadata is also independent of license evidence.

V1 privacy states include:

```text
NO_PHI_KNOWN
DEIDENTIFIED
RESTRICTED_OR_PHI
UNRESOLVED
NOT_APPLICABLE
```

Unknown privacy state blocks relevant executable/optimization use. `DEIDENTIFIED` is a classification, not a blanket authorization that overrides access or rights.

No real PHI or restricted clinical payload is required or permitted as a Spec 003 fixture.

## Purpose, split, and Gold quarantine

Spec 003 reuses the canonical Spec 001 purpose vocabulary rather than creating a second partition model:

```text
TRAIN
DEV
CALIBRATION
CHECKPOINT_SELECTION
PUBLIC_EXTERNAL_EVAL
PRIVATE_GOLD
```

Private Gold remains quarantined. It cannot silently become training, teacher-generation, development-selection, checkpoint-selection, retrieval, derivation, or redistribution material.

A broader Spec 003 `declared_use` never erases the more specific Spec 001 split/purpose identity.

## Contamination

Spec 003 records and validates contamination/overlap state; it does not scan corpora, run embeddings, or execute benchmarks.

For uses that require clean optimization separation, unresolved/pending overlap blocks admission and established high-risk overlap prohibits that optimization use.

## Synthetic and derived lineage

Generated and derived assets retain parentage.

Where applicable, records carry:

- parent asset IDs;
- origin type;
- generator/teacher identity;
- generation/configuration identity; and
- output-use evidence.

Model-generated output does not become training lineage by omission. A training/adaptation use of generated or derived output requires explicit output-use evidence in addition to the other rights/privacy/contamination gates.

This preserves the project default that MedGemma/HAI-DEF and frontier-provider outputs are not automatically training data.

## Computed admission

Admission is computed for the **exact declared use** and returns one state:

```text
ELIGIBLE
REFERENCE_ONLY
BLOCKED
PROHIBITED
```

The result also carries deterministic reason codes plus:

```text
contract_sha256
record_sha256
```

Both identities are recomputed by commandMed. Caller-provided admission or record identities are not trusted.

`ELIGIBLE` means only that the lineage evidence required by this contract is satisfied for that exact declared use. It does not mean clinical safety, release readiness, legal clearance, or permission for another use.

## Scientific identity vs audit metadata

Scientific identity uses an explicit projection and the existing Spec 001 canonical SHA-256 mechanism.

Identity-bearing examples include:

- stable asset/class identity;
- immutable source revision;
- artifact-binding evidence;
- declared use;
- rights evidence/state;
- split/purpose/quarantine identity;
- contamination evidence/state;
- parent/generator/configuration lineage.

Audit-only examples include:

- retrieval/check timestamps;
- local filesystem paths;
- reviewer workstation metadata;
- convenience references that do not change governed facts.

Audit-only changes do not silently create a new scientific asset identity.

## Spec 001 compatibility

Spec 003 does not migrate or rewrite `data/eval/benchmarks.json`.

Compatibility tests prove that:

- a canonical executable HealthBench record with exact artifact locator + immutable 40-hex dataset revision maps to `IMMUTABLE_REVISION_LOCATOR`;
- the canonical MedAbstain family-level `REFERENCE_ONLY` / `UNBOUND` / `COMPONENT_SPECIFIC` boundary cannot be widened into an eligible executable use.

The Spec 001 registry remains canonical prior art.

## Standards used as design evidence

The Spec 003 clarification reviewed primary public specifications including:

- SPDX 3.0.1 license-expression semantics;
- MLCommons Croissant 1.1 resource/version/checksum concepts;
- W3C PROV entity/derivation concepts;
- DataCite 4.6 persistent-identifier/relationship concepts.

commandMed does not adopt their full runtime stacks in Spec 003. The implementation remains standard-library Python/JSON plus the repository's existing canonicalization mechanisms.

## Verification boundary

The implementation is intentionally testable with synthetic metadata only. The focused suite must prove contract weakening, self-asserted admission/identity, mutable revision labels, unresolved rights/privacy/contamination, Gold misuse, generated-output laundering, malformed inputs, and Spec 001 compatibility all fail closed.

No external payload access is necessary to verify the contract.