# E004 Rebuild Reproducibility Diagnostic Result Reconciliation — 2026-09-01

**Spec:** 007 SFT V1  
**Artifact class:** execution-result reconciliation  
**Canonical diagnostic authority merge:** `2fd2915024182100be0e5ce6ffb261e5b76f03bb`  
**Diagnostic implementation PR:** `#167`  
**Reviewed diagnostic implementation head:** `40f36acd949897f072fec4f1d51debbfc316d07f`  
**Canonical diagnostic implementation merge:** `bc3ea6830fc0aaa674df2b439b74a98cda34bd20`  
**Diagnostic workflow:** `.github/workflows/e004-rebuild-reproducibility-diagnostic-v1.yml`  
**Model conversion authority:** NONE  
**Conversion execution authority:** NONE  
**Contamination assessment authority:** NONE  
**A15 activation:** ABSENT_NOT_AUTHORIZED  
**Training authority:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Reconcile the single bounded E004 rebuild-reproducibility diagnostic execution authorized by canonical authority merge `2fd2915024182100be0e5ce6ffb261e5b76f03bb`.

This record is evidence reconciliation only. It does not rerun the diagnostic, reopen its consumed one-shot allowance, modify or normalize a binary, accept execution-time identity binding as policy, access model weights or benchmark payloads, perform model conversion or inference, perform contamination assessment, activate A15, train, use protected data, authorize credentials, upload binaries, procure resources, make payment, or create spend authority.

## 2. One-shot lifecycle and retained execution

The bounded lifecycle reached its single execution exactly once:

```text
DIAGNOSTIC_AUTHORITY_MERGE=2fd2915024182100be0e5ce6ffb261e5b76f03bb
DIAGNOSTIC_IMPLEMENTATION_PR=167
DIAGNOSTIC_IMPLEMENTATION_REVIEWED_HEAD=40f36acd949897f072fec4f1d51debbfc316d07f
DIAGNOSTIC_IMPLEMENTATION_GUARDED_MERGE=bc3ea6830fc0aaa674df2b439b74a98cda34bd20
DIAGNOSTIC_EXECUTION_COUNT=1
DIAGNOSTIC_EXECUTION_ALLOWANCE_REMAINING=0
AUTOMATIC_RETRY_USED=NO
FAILED_JOB_RERUN_USED=NO
SECOND_DIAGNOSTIC_RUN_USED=NO
```

The retained GitHub Actions identity is:

```text
DIAGNOSTIC_RUN_ID=33507754943
DIAGNOSTIC_RUN_NUMBER=1
DIAGNOSTIC_RUN_ATTEMPT=1
DIAGNOSTIC_RUN_EVENT=push
DIAGNOSTIC_RUN_HEAD_BRANCH=main
DIAGNOSTIC_RUN_HEAD_SHA=bc3ea6830fc0aaa674df2b439b74a98cda34bd20
DIAGNOSTIC_JOB_ID=99855785119
DIAGNOSTIC_JOB_NAME=diagnostic
DIAGNOSTIC_JOB_STATUS=completed
DIAGNOSTIC_JOB_CONCLUSION=success
BOUNDED_DIAGNOSTIC_STEP_CONCLUSION=success
```

A successful job means only that the bounded diagnostic completed and retained its evidence. It does not authorize acceptance of the historical mismatch.

## 3. Frozen comparison subject

The workflow and authority froze the public tool source and historical comparison identities as:

```text
TOOL_REPOSITORY=https://github.com/ggml-org/llama.cpp.git
TOOL_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
TARGET=llama-quantize

PRIOR_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
REBUILT_LLAMA_QUANTIZE_SHA256=18ff27aab20ab7b4e239ac847be7636fb8e182ac9d1474efa7c4cfc915bbb4fc
EXPECTED_LLAMA_QUANTIZE_BYTES=6513680
```

Those are the only historical full-file identities against which the diagnostic result is reconciled.

## 4. Environment and PATH qualification

The diagnostic recorded:

```text
HISTORICAL_PATH_VALUE=/usr/local/bin:/usr/bin
REPAIRED_PATH_VALUE=/usr/local/bin:/usr/bin:/bin
NORMALIZED_HISTORICAL_PATH_IDENTITY=/usr/local/bin:/usr/bin
NORMALIZED_REPAIRED_PATH_IDENTITY=/usr/local/bin:/usr/bin
EFFECTIVE_PATH_IDENTITIES_EQUAL=YES
PATH_CONTEXT_CLASSIFICATION=REDUNDANT_USRMERGE_ENTRY_NOT_INDEPENDENT_VARIABLE
ENVIRONMENT_IDENTITIES_MATCH=YES
PATH_CAUSAL_ATTRIBUTION=PROHIBITED_EFFECTIVE_PATHS_EQUAL
```

Therefore the syntactic PATH difference is not an independent causal variable. The diagnostic's `ABSOLUTE_PATH_CONTEXT` terminology refers to the authority-defined absolute source/build directory layouts, not to the normalized executable search PATH.

## 5. A1/A2 historical-layout observations

A1 and A2 repeated the authority-defined historical absolute source/build layout. Both completed successfully and produced the same full-file identity:

```text
A1_STATUS=PASS
A1_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
A1_LLAMA_QUANTIZE_INTEGER_BYTES=6513680
A1_ELF_BUILD_ID_IF_PRESENT=c3b1ffcb29aa0b069380b8aaf7aef6e4928f5738
A1_CMAKE_CACHE_SHA256=0b499b1dfa63d0f3fcf80cb3c0f45b25b95de2b5cd128574cc3d1e5f49ad0599
A1_SOURCE_ABSOLUTE_PATH_PRESENT_IN_BINARY=YES
A1_BUILD_ABSOLUTE_PATH_PRESENT_IN_BINARY=NO

A2_STATUS=PASS
A2_LLAMA_QUANTIZE_SHA256=e1d88ef6fee265fc6aba97f18b8cc268b0632de7cbcdaca9c94b2c5f078900a0
A2_LLAMA_QUANTIZE_INTEGER_BYTES=6513680
A2_ELF_BUILD_ID_IF_PRESENT=c3b1ffcb29aa0b069380b8aaf7aef6e4928f5738
A2_CMAKE_CACHE_SHA256=0b499b1dfa63d0f3fcf80cb3c0f45b25b95de2b5cd128574cc3d1e5f49ad0599
A2_SOURCE_ABSOLUTE_PATH_PRESENT_IN_BINARY=YES
A2_BUILD_ABSOLUTE_PATH_PRESENT_IN_BINARY=NO

SHA_EQUAL_A1_A2=YES
BUILD_ID_EQUAL_A1_A2=YES
BYTE_DIFFERENCE_COUNT_A1_A2=0
A1_EQUALS_PRIOR_SHA=YES
A2_EQUALS_PRIOR_SHA=YES
A1_EQUALS_REBUILT_SHA=NO
A2_EQUALS_REBUILT_SHA=NO
A1_BYTES_EQUAL_HISTORICAL=YES
A2_BYTES_EQUAL_HISTORICAL=YES
```

Result: the historical-layout build was byte-repeatable in this bounded run and exactly reproduced the frozen prior full-file SHA-256.

## 6. B1/B2 repaired-layout observations

B1 and B2 repeated the authority-defined repaired absolute source/build layout. Both completed successfully and produced the same third full-file identity:

```text
B1_STATUS=PASS
B1_LLAMA_QUANTIZE_SHA256=1f5c96a6763656d439455fdd331097cd73e607031c19f465dedf0dd4cfadeca6
B1_LLAMA_QUANTIZE_INTEGER_BYTES=6513680
B1_ELF_BUILD_ID_IF_PRESENT=010b019c3e0733f4b09d9b8d0934412a0ffca5e0
B1_CMAKE_CACHE_SHA256=5a2f8b139183dfba6d422db476cd8ad1b69388749199d909055744c082532bc3
B1_SOURCE_ABSOLUTE_PATH_PRESENT_IN_BINARY=YES
B1_BUILD_ABSOLUTE_PATH_PRESENT_IN_BINARY=NO

B2_STATUS=PASS
B2_LLAMA_QUANTIZE_SHA256=1f5c96a6763656d439455fdd331097cd73e607031c19f465dedf0dd4cfadeca6
B2_LLAMA_QUANTIZE_INTEGER_BYTES=6513680
B2_ELF_BUILD_ID_IF_PRESENT=010b019c3e0733f4b09d9b8d0934412a0ffca5e0
B2_CMAKE_CACHE_SHA256=5a2f8b139183dfba6d422db476cd8ad1b69388749199d909055744c082532bc3
B2_SOURCE_ABSOLUTE_PATH_PRESENT_IN_BINARY=YES
B2_BUILD_ABSOLUTE_PATH_PRESENT_IN_BINARY=NO

SHA_EQUAL_B1_B2=YES
BUILD_ID_EQUAL_B1_B2=YES
BYTE_DIFFERENCE_COUNT_B1_B2=0
B1_EQUALS_PRIOR_SHA=NO
B2_EQUALS_PRIOR_SHA=NO
B1_EQUALS_REBUILT_SHA=NO
B2_EQUALS_REBUILT_SHA=NO
B1_BYTES_EQUAL_HISTORICAL=YES
B2_BYTES_EQUAL_HISTORICAL=YES
```

Result: the repaired-layout build was byte-repeatable in this bounded run, but it reproduced neither frozen historical full-file SHA-256.

## 7. Cross-layout comparison

The terminal evidence records the complete bounded comparison matrix as:

```text
SHA_EQUAL_A1_A2=YES
SHA_EQUAL_A1_B1=NO
SHA_EQUAL_A1_B2=NO
SHA_EQUAL_A2_B1=NO
SHA_EQUAL_A2_B2=NO
SHA_EQUAL_B1_B2=YES

BUILD_ID_EQUAL_A1_A2=YES
BUILD_ID_EQUAL_A1_B1=NO
BUILD_ID_EQUAL_A1_B2=NO
BUILD_ID_EQUAL_A2_B1=NO
BUILD_ID_EQUAL_A2_B2=NO
BUILD_ID_EQUAL_B1_B2=YES

BYTE_DIFFERENCE_COUNT_A1_A2=0
BYTE_DIFFERENCE_COUNT_A1_B1=760129
BYTE_DIFFERENCE_COUNT_A1_B2=760129
BYTE_DIFFERENCE_COUNT_A2_B1=760129
BYTE_DIFFERENCE_COUNT_A2_B2=760129
BYTE_DIFFERENCE_COUNT_B1_B2=0
```

The workflow measured full-file SHA-256, integer byte size, GNU Build-ID where present, exact-source/build-path string presence, and byte-difference counts. It did **not** compute an `ELF LOAD SHA-256`; this reconciliation therefore makes no ELF LOAD identity claim.

The different Build IDs and the large cross-layout byte-difference count are observations only. They do not independently localize the differing bytes to any ELF section and do not prove a Build-ID-only mechanism.

## 8. Historical reconstruction result

The diagnostic reproduced the frozen prior hash at A1/A2, but the repaired-layout B1/B2 result was a third hash rather than the frozen repaired-runtime hash:

```text
A1_EQUALS_PRIOR_SHA=YES
A2_EQUALS_PRIOR_SHA=YES
B1_EQUALS_REBUILT_SHA=NO
B2_EQUALS_REBUILT_SHA=NO
HISTORICAL_TWO_HASH_SPLIT_REPRODUCED=NO
```

Because both layouts were internally byte-repeatable while their full-file outputs differed across layouts, the workflow selected the authority-permitted disposition:

```text
DIAGNOSTIC_DISPOSITION=ABSOLUTE_PATH_CONTEXT_AFFECTS_BYTES_BUT_DOES_NOT_REPRODUCE_HISTORICAL_SPLIT
DIAGNOSTIC_RUN_COMPLETED=YES
```

This disposition is narrow. It establishes that the authority-controlled source/build absolute layout changed output bytes in this run, while the previously observed `e1d88ef6...` versus `18ff27aa...` historical split was **not** reproduced.

It does not establish that the absolute layout fully explains the earlier repaired-runtime hash, and it does not permit causal attribution to the syntactic PATH difference because the normalized effective PATH identities were equal.

## 9. Canonical interpretation required by the authority

Section 11 of the canonical authority requires that when the historical split is not reproduced, the cause remains `NEEDS_EVIDENCE` and later conversion authority remains blocked unless a separately reviewed policy disposition explicitly accepts execution-time identity binding without byte-for-byte reconstruction.

Therefore this reconciliation records:

```text
REBUILD_BINARY_REPRODUCIBILITY=PARTIALLY_DEMONSTRATED_WITHIN_DIAGNOSTIC_LAYOUTS
HISTORICAL_REPAIRED_HASH_RECONSTRUCTION=NOT_REPRODUCED
REBUILD_MISMATCH_CAUSE=NEEDS_EVIDENCE
RUNTIME_RECONSTRUCTION_READINESS=INCOMPLETE_PENDING_SEPARATE_RESOLUTION
EXECUTION_TIME_IDENTITY_BINDING_POLICY_DISPOSITION=NONE
```

`PARTIALLY_DEMONSTRATED_WITHIN_DIAGNOSTIC_LAYOUTS` is descriptive reconciliation language, not a new execution state or authority. It means only that A1=A2 and B1=B2 in this one bounded matrix; it does not satisfy the unresolved requirement to reconstruct the frozen repaired-runtime identity.

## 10. Safety and authority boundary after the run

The terminal workflow state and controlling governance remain:

```text
E004_REBUILD_REPRO_DIAGNOSTIC_EXECUTION_STATE=CONSUMED_COMPLETE
E004_REBUILD_REPRO_DIAGNOSTIC_AUTHORITY=CONSUMED_NOT_REUSABLE
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0

COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
COMPONENT_E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
PROJECT_FINISHED=NO
```

No rerun, retry, second diagnostic, normalization experiment, binary rewrite, execution-time identity-binding policy, model access, conversion, inference, benchmark execution, contamination assessment, A15 activation, training, protected-data access, credential use, paid compute, procurement, payment, or spend authority is created by this record.

## 11. Dependency-safe next frontier

This result closes only the consumed one-shot diagnostic's evidence-reconciliation obligation after canonical merge of this document. It does not close E004.

The evidence leaves two classes of later resolution named or permitted by existing governance, neither authorized by this document:

1. a separately reviewed bounded diagnostic/repair authority that can explain or resolve why the repaired-layout build in this controlled run produced `1f5c96a6...` instead of the frozen repaired-runtime `18ff27aa...`; or
2. a separately reviewed policy disposition deciding whether execution-time exact identity binding may be accepted without byte-for-byte reconstruction of the earlier repaired-runtime binary.

Any successor execution must obtain its own canonical authority before implementation. In particular:

```text
REBUILD_NORMALIZATION_EXPERIMENT_AUTHORITY=NONE
BINARY_DIFFERENCE_LOCALIZATION_DIAGNOSTIC_AUTHORITY=NONE
EXECUTION_TIME_IDENTITY_BINDING_POLICY_DISPOSITION=NONE
MODEL_SOURCE_WEIGHT_ACQUISITION_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
```

## 12. Required merge-exit gate

This reconciliation may become canonical only after a fresh independent exact-head review verifies the complete one-file diff against the authority, the merged workflow, and terminal run/job evidence and concludes that no material correctness, evidence-integrity, governance, reproducibility, or authority-boundary blocker remains.

The review must verify at least:

- exact run `33507754943`, attempt `1`, job `99855785119`, and merge head `bc3ea6830fc0aaa674df2b439b74a98cda34bd20`;
- the one-shot allowance remains consumed with no rerun or replacement execution;
- frozen historical identities are exactly `e1d88ef6...`, `18ff27aa...`, and `6513680` bytes;
- A1/A2 are identical to each other and equal the frozen prior hash;
- B1/B2 are identical to each other and equal `1f5c96a6...`, but not the frozen repaired-runtime hash;
- cross-layout full-file byte-difference count is `760129` for every A/B pair and `0` within A/A and B/B;
- normalized effective PATH identities are equal and PATH causal attribution remains prohibited;
- no unsupported ELF LOAD measurement or other unexecuted evidence appears in the record;
- the exact workflow disposition is `ABSOLUTE_PATH_CONTEXT_AFFECTS_BYTES_BUT_DOES_NOT_REPRODUCE_HISTORICAL_SPLIT`;
- `REBUILD_MISMATCH_CAUSE=NEEDS_EVIDENCE` remains in force;
- no successor execution or model/scientific/spend authority is created;
- E004 remains incomplete and blocked preflight, E005 remains not reached, and the project is not declared finished.

Until that exact-head review succeeds and a guarded canonical merge is completed, this file is only a PR candidate and has no canonical authority effect.
