# External Code Adoption Governance

**Status:** ADDITIVE GOVERNANCE PLANNING — NO IMPLEMENTATION AUTHORITY  
**Applies to:** copied, adapted, vendored, translated, ported, or substantially derived external source code  
**Current authorized spend:** USD 0

## 1. Purpose

commandMed already has strong provenance rules for datasets, models and evidence. This policy extends the same discipline to external software source code.

The Founder has stated that commandMed has permission to copy source code from supplied repositories. That authorization does not remove upstream license, copyright, NOTICE, third-party component, patent, attribution, or redistribution obligations.

This file defines the minimum governance required before external code becomes canonical commandMed source.

## 2. Core rule

```text
SOURCE_USE_PERMISSION
!= LICENSE_COMPATIBILITY
!= FILE_LEVEL_PROVENANCE
!= SECURITY_QUALIFICATION
!= CANONICAL_ADMISSION
```

Every transition must be proven separately.

## 3. Adoption modes

Every external-source adoption must declare exactly one mode:

```text
REFERENCE_ONLY
PATTERN_REIMPLEMENTED
ADAPTED_DERIVATIVE
COPIED_SOURCE
VENDORED_COMPONENT
```

### `REFERENCE_ONLY`

No donor code enters commandMed. The source informs planning/research only.

### `PATTERN_REIMPLEMENTED`

commandMed independently implements a design pattern. The planning record should still cite the inspiration source when material, but donor source text/code is not copied.

### `ADAPTED_DERIVATIVE`

A donor implementation is materially transformed. Upstream obligations still apply when the adaptation is derivative under the applicable license.

### `COPIED_SOURCE`

Exact or near-exact source material enters commandMed. File-level provenance and attribution are mandatory.

### `VENDORED_COMPONENT`

A donor package/subtree is imported substantially intact. This is the highest-complexity mode and requires explicit justification under Ponytail discipline.

## 4. Required source-admission record

Before `ADAPTED_DERIVATIVE`, `COPIED_SOURCE`, or `VENDORED_COMPONENT` becomes canonical, record at least:

```text
adoption_record_id
donor_repository
donor_revision
donor_path
donor_blob_sha
upstream_license_id
upstream_license_file_identity
upstream_notice_state
third_party_component_state
permission_basis
adoption_mode
commandmed_destination_path
intended_capability
why_existing_commandmed_code_is_insufficient
transitive_dependency_change
network_or_credential_change
privilege_change
execution_surface_change
security_review_state
test_evidence_state
attribution_state
modification_notice_state
```

A directory-level donor revision alone is insufficient when individual copied files have different licenses or embedded third-party code.

## 5. Root commandMed software-license gate

A root `LICENSE` file was not observed at the commandMed canonical base used when this policy was authored.

Before commandMed redistributes copied donor code, the project must establish an explicit software-license/distribution posture compatible with the intended adoption.

Until then:

```text
REFERENCE_ONLY=ALLOWED
PATTERN_REIMPLEMENTATION_PLANNING=ALLOWED
DONOR_CODE_RESEARCH=ALLOWED_WITHIN_AUTHORITY
CANONICAL_REDISTRIBUTED_COPIED_SOURCE=BLOCKED
CANONICAL_VENDORED_COMPONENT=BLOCKED
```

This gate is about redistribution clarity, not about whether the Founder may privately inspect or study source code.

## 6. License and attribution obligations

For each adopted source:

1. preserve required copyright notices;
2. preserve license text where required;
3. preserve NOTICE content where required;
4. mark modified files when required;
5. preserve third-party license terms independently;
6. do not represent donor work as original commandMed work;
7. do not imply endorsement by an upstream project;
8. record exact source revision and path;
9. review dependency licenses introduced by the copied code;
10. keep release documentation consistent with actual incorporated material.

## 7. Security admission

Permission and license compatibility are not security qualification.

External code that can affect any of the following is high risk:

- model loading/execution;
- network access;
- credentials/secrets;
- subprocess/shell execution;
- filesystem writes;
- deserialization;
- archives;
- package installation;
- MCP/agent/tool execution;
- patient-facing output;
- deterministic medical-tool authority;
- provenance/evaluation records;
- release signing/build logic.

High-risk external code must receive commandMed-native negative tests and exact-head qualification before merge.

## 8. Minimal-copy rule

Prefer the smallest mechanism that closes the measured gap.

Order of preference:

```text
EXISTING_COMMANDMED_MECHANISM
-> STANDARD_LIBRARY_OR_NATIVE_PLATFORM
-> PATTERN_REIMPLEMENTATION
-> SMALL_ADAPTED_DERIVATIVE
-> SMALL_EXACT_COPY
-> EXTERNAL_DEPENDENCY
-> VENDORED_SUBTREE
```

The order may be overridden only when evidence shows a lower item is materially safer, more correct, more maintainable, or substantially better for the required capability.

## 9. Donor-specific current boundaries

### Tencent/AI-Infra-Guard

Current recommended mode:

```text
REFERENCE_ONLY -> PATTERN_REIMPLEMENTED -> SMALL_ADAPTED_DERIVATIVE_IF_JUSTIFIED
```

Do not vendor the full platform by default.

If future copying occurs, preserve Apache-2.0 and applicable NOTICE/attribution requirements.

### Tencent/AICGSecEval

Current recommended mode:

```text
REFERENCE_ONLY -> PATTERN_REIMPLEMENTED
```

Framework license does not automatically license all benchmark/task payloads derived from third-party projects. Dataset/PoC admission is separate from code adoption.

### Tencent/hpc-ops

Current recommended mode:

```text
REFERENCE_ONLY_FOR_CURRENT_CPU_PATH
FUTURE_SMALL_ADAPTATION_ONLY_AFTER_GPU_PROFILE_AND_TARGET_FREEZE
```

Do not vendor `3rd/` wholesale. Preserve MIT plus component-specific licenses such as CUTLASS BSD-3-Clause.

## 10. Dataset, model and code boundaries remain separate

A repository can contain multiple legal/evidence classes.

```text
CODE_LICENSE_PASS
DOES_NOT_IMPLY
DATASET_LICENSE_PASS

CODE_LICENSE_PASS
DOES_NOT_IMPLY
MODEL_WEIGHT_LICENSE_PASS

SOURCE_USE_PERMISSION
DOES_NOT_IMPLY
SECURITY_POC_EXECUTION_AUTHORITY
```

Each class follows its own canonical admission process.

## 11. Upstream drift

Never update copied/adapted code merely because an upstream branch changed.

A donor update requires:

- new immutable revision;
- changed-file review;
- license/NOTICE recheck;
- security-impact review;
- dependency-impact review;
- commandMed tests;
- evidence that the update solves a real issue or produces a justified benefit.

## 12. Release evidence

When commandMed eventually contains external copied/derived code, release review should be able to reconstruct:

```text
COMMANDMED_RELEASE_ARTIFACT
-> COMMANDMED_SOURCE_COMMIT
-> EXTERNAL_ADOPTION_RECORDS
-> DONOR_REPOSITORIES_AND_REVISIONS
-> DONOR_FILES_AND_BLOB_IDENTITIES
-> LICENSE_AND_NOTICE_OBLIGATIONS
-> MODIFICATION_STATE
-> SECURITY_AND_TEST_EVIDENCE
```

## 13. Current authority boundary

This governance file does not authorize:

- copying source into current active implementation;
- adding dependencies;
- installing donor packages;
- running donor scanners;
- executing vulnerability PoCs;
- accessing credentials;
- model execution;
- tournament execution;
- training;
- GPU execution;
- spend.

Future code adoption remains dependency- and authority-gated by the active bounded spec or other canonical authorization.
