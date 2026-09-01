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

Reconcile the single bounded E004 rebuild-reproducibility diagnostic execution authorized by the canonical authority merge `2fd2915024182100be0e5ce6ffb261e5b76f03bb`.

This record is evidence reconciliation only. It does not execute or rerun the diagnostic, reopen its consumed allowance, repair or normalize a binary, prepare model conversion, accept execution-time identity binding as a policy substitute for byte reconstruction, access model weights or benchmark payloads, perform contamination assessment, activate A15, train, use credentials, upload artifacts, procure resources, make payment, or create spend authority.

The canonical diagnostic authority required that same-path non-reproducibility remain a blocker and that any later repair/normalization experiment require separate authority.

## 2. Completed lifecycle and one-shot consumption

The authorized lifecycle reached its one execution exactly once:

```text
DIAGNOSTIC_AUTHORITY_MERGE=2fd2915024182100be0e5ce6ffb261e5b76f03bb
DIAGNOSTIC_IMPLEMENTATION_PR=167
DIAGNOSTIC_IMPLEMENTATION_REVIEWED_HEAD=40f36acd949897f072fec4f1d51debbfc316d07f
DIAGNOSTIC_IMPLEMENTATION_INDEPENDENT_REVIEW=MATERIAL_BLOCKER_NO
DIAGNOSTIC_IMPLEMENTATION_GUARDED_MERGE=bc3ea6830fc0aaa674df2b439b74a98cda34bd20
DIAGNOSTIC_EXECUTION_COUNT=1
DIAGNOSTIC_EXECUTION_ALLOWANCE_REMAINING=0
AUTOMATIC_RETRY_USED=NO
FAILED_JOB_RERUN_USED=NO
SECOND_DIAGNOSTIC_RUN_USED=NO
```

The allowance was consumed when the merge-triggered run was created. Its successful conclusion does not reopen that allowance.

## 3. Exact retained execution identity

GitHub Actions records the retained execution as:

```text
DIAGNOSTIC_RUN_ID=33507754943
DIAGNOSTIC_RUN_NUMBER=1
DIAGNOSTIC_RUN_ATTEMPT=1
DIAGNOSTIC_RUN_EVENT=push
DIAGNOSTIC_RUN_HEAD_BRANCH=main
DIAGNOSTIC_RUN_HEAD_SHA=bc3ea6830fc0aaa674df2b439b74a98cda34bd20
DIAGNOSTIC_RUN_STATUS=completed
DIAGNOSTIC_RUN_CONCLUSION=success
DIAGNOSTIC_JOB_ID=99855785119
DIAGNOSTIC_JOB_NAME=diagnostic
DIAGNOSTIC_JOB_CONCLUSION=success
RUNNER_LABEL=ubuntu-24.04
```

The terminal job logs are the retained diagnostic evidence. No diagnostic artifact upload was authorized or used.

## 4. Exact diagnostic subject and toolchain

The run used the exact public `llama.cpp` source identity frozen by the authority:

```text
LLAMA_CPP_REPOSITORY=ggml-org/llama.cpp
LLAMA_CPP_COMMIT=c1d0e7a004015f23bc0233470b747b596f29b264
LLAMA_CPP_TREE=2255f4747492109298a5c997f374d49c2af3113d
```

The retained runtime/toolchain observations were:

```text
RUNNER_OS=Ubuntu 24.04.4 LTS
RUNNER_IMAGE=ubuntu-24.04
RUNNER_IMAGE_VERSION=20260823.283.1
CMAKE_VERSION=cmake version 3.31.6
CXX_COMPILER=Ubuntu clang version 18.1.3 (1ubuntu1)
CXX_COMPILER_TARGET=x86_64-pc-linux-gnu
LINKER_VERSION=Ubuntu LLD 18.1.3 (compatible with GNU linkers)
GIT_VERSION=git version 2.53.0
MAKE_VERSION=GNU Make 4.3
NINJA_VERSION=1.11.1
PYTHON_VERSION=Python 3.12.3
```

The workflow performed its one allowed public source fetch before the build cells. The build cells then ran in the authority-bounded network-isolated, dropped-privilege environment with sensitive platform environment removed.

## 5. Historical comparison identities

The diagnostic retained the frozen comparison identities:

```text
HISTORICAL_FULL_SHA256=421c19f0f26b1f20d71278944783f60f1768c17dfcf42b3a256bedd8d51bb59a
HISTORICAL_REPAIRED_FULL_SHA256=bcd6d0088fc46a49a8582b6685fff11ac97387ae169d1a11437b080e064ac910
REBUILT_DIAGNOSTIC_FULL_SHA256=88d687902384b7361e94a6c52867f572d6a49fc4082cd22c7db0863774b2b02b
```

The historical and repaired PATH strings emitted by this diagnostic normalized to the same effective executable-location identity:

```text
NORMALIZED_HISTORICAL_PATH=/opt/hostedtoolcache/Python/3.11.14/x64/bin:/opt/hostedtoolcache/Python/3.11.14/x64:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/usr/bin:/usr/bin:/snap/bin
NORMALIZED_REPAIRED_PATH=/opt/hostedtoolcache/Python/3.11.14/x64/bin:/opt/hostedtoolcache/Python/3.11.14/x64:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/usr/bin:/usr/bin:/snap/bin
ENVIRONMENT_IDENTITIES_MATCH=true
PATH_CAUSAL_ATTRIBUTION=PROHIBITED_EFFECTIVE_PATHS_EQUAL
```

No PATH-causal conclusion is supported.

## 6. Direct A1/A2 same-path observations

A1 and A2 used the same authority-defined historical absolute source/build path layout.

```text
A1_STATUS=SUCCESS
A1_FULL_SHA256=88d687902384b7361e94a6c52867f572d6a49fc4082cd22c7db0863774b2b02b
A1_ELF_LOAD_SHA256=eaad61f5e1ca3d66fd0933c8642501363926269015704ea11f0ff0b84c460c5f
A1_GNU_BUILD_ID=c6f21695207bc4c7ee373a8fd0b3b7ca4c200ceb
A1_BYTES=4240416

A2_STATUS=SUCCESS
A2_FULL_SHA256=8e8d282c45b49bc835681368397d027c87a521596463882c816521bcc2602330
A2_ELF_LOAD_SHA256=eaad61f5e1ca3d66fd0933c8642501363926269015704ea11f0ff0b84c460c5f
A2_GNU_BUILD_ID=812677355ccc31c51abfbd917822240b5744415a
A2_BYTES=4240416

A_REPEATABLE_FULL_SHA256=false
A_REPEATABLE_ELF_LOAD_SHA256=true
A1_VS_A2_FULL_BYTE_DIFFERENCES=20
```

The exact full binary is therefore not reproducible within the A layout, even though its measured ELF LOAD identity is repeatable.

A1 happens to equal the earlier `REBUILT_DIAGNOSTIC_FULL_SHA256`, but A2 does not:

```text
A1_MATCHES_REBUILT_DIAGNOSTIC_FULL_SHA256=true
A2_MATCHES_REBUILT_DIAGNOSTIC_FULL_SHA256=false
DETERMINISTIC_RECONSTRUCTION_FROM_A_LAYOUT=NO
```

The single A1 equality cannot be promoted into reproducibility evidence.

## 7. Direct B1/B2 same-path observations

B1 and B2 used the same authority-defined repaired absolute source/build path layout.

```text
B1_STATUS=SUCCESS
B1_FULL_SHA256=bf7cd9601caf64713348c208ef1bd7aaeb2f4c894ff6fcf7c52663a190ab312a
B1_ELF_LOAD_SHA256=eaad61f5e1ca3d66fd0933c8642501363926269015704ea11f0ff0b84c460c5f
B1_GNU_BUILD_ID=a4ea0a0a18d4735138890f325c1717830c3cd16d
B1_BYTES=4240416

B2_STATUS=SUCCESS
B2_FULL_SHA256=3b4ddc91379f26146622961187b503575249475ffe342acd469f895335051cfe
B2_ELF_LOAD_SHA256=eaad61f5e1ca3d66fd0933c8642501363926269015704ea11f0ff0b84c460c5f
B2_GNU_BUILD_ID=d351aae65df39859928cf20aaba7bb2b654f3a03
B2_BYTES=4240416

B_REPEATABLE_FULL_SHA256=false
B_REPEATABLE_ELF_LOAD_SHA256=true
B1_VS_B2_FULL_BYTE_DIFFERENCES=20
```

The exact full binary is therefore not reproducible within the B layout, even though its measured ELF LOAD identity is repeatable.

## 8. A-versus-B comparison

The retained comparison is:

```text
A_VS_B_FULL_SHA256_EQUAL=false
A_VS_B_ELF_LOAD_SHA256_EQUAL=true
A_VS_B_BUILD_IDS_EQUAL=false
A1_VS_B1_FULL_BYTE_DIFFERENCES=20
```

All four cells produced the same measured ELF LOAD SHA-256:

```text
ELF_LOAD_SHA256=eaad61f5e1ca3d66fd0933c8642501363926269015704ea11f0ff0b84c460c5f
```

All four cells produced different GNU Build IDs and different full-file SHA-256 identities.

The workflow additionally searched the resulting binary bytes for the authority-defined historical/repaired source and build path strings and observed zero occurrences in every cell.

These observations narrow the mismatch but do not prove a causal mechanism. In particular:

```text
BUILD_ID_CAUSALITY=NEEDS_EVIDENCE
NON_LOADABLE_METADATA_CAUSALITY=NEEDS_EVIDENCE
BYTE_OFFSET_TO_ELF_SECTION_MAPPING=NEEDS_EVIDENCE
ABSOLUTE_PATH_LAYOUT_CAUSALITY=NOT_PROVEN
```

The observed 20 differing bytes in the three measured comparisons MUST NOT be asserted to be Build-ID bytes without a separately retained localization proof.

## 9. Historical reconstruction result

The bounded diagnostic did not reproduce either frozen historical full-file identity as a repeatable build result:

```text
A_MATCHES_HISTORICAL_FULL_SHA256=false
B_MATCHES_HISTORICAL_FULL_SHA256=false
B_MATCHES_HISTORICAL_REPAIRED_FULL_SHA256=false
HISTORICAL_FULL_SHA_RECONSTRUCTED=NO
HISTORICAL_REPAIRED_FULL_SHA_RECONSTRUCTED=NO
HISTORICAL_TWO_HASH_SPLIT_REPRODUCED=NO
```

Because A and B are each internally non-repeatable at the full-file level, an A-versus-B full-file difference cannot establish deterministic path-layout causality.

The directly supported disposition from the run is:

```text
DIAGNOSTIC_DISPOSITION=A_SAME_PATH_NOT_REPRODUCIBLE_RUNTIME_RECONSTRUCTION_REMAINS_BLOCKED
REBUILD_BINARY_REPRODUCIBILITY=NOT_PROVEN
REBUILD_MISMATCH_CAUSE=NEEDS_EVIDENCE
RUNTIME_RECONSTRUCTION_READINESS=BLOCKED
```

This is consistent with the canonical authority rule that same-path non-byte-identity keeps runtime reconstruction blocked.

## 10. Safety, cleanup, and authority boundary

The terminal logs record the authority-preserving end state:

```text
DIAGNOSTIC_RETAINED_EVIDENCE=TERMINAL_JOB_LOGS_ONLY
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
COMPONENT_E005_STATE=NOT_REACHED
E004_REBUILD_REPRO_DIAGNOSTIC_AUTHORITY=CONSUMED_NOT_REUSABLE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The transient source/build directories were deleted before the job completed. No persistent diagnostic binary was retained by this run.

No model source weight was acquired or loaded, no model conversion or quantization was performed, no inference or benchmark was executed, no contamination payload was accessed, no A15 activation occurred, no training occurred, no credential was used for the diagnostic body, and no diagnostic artifact/cache upload or paid runner was authorized.

## 11. Evidence-backed next-resolution candidates

The current evidence supports only narrow candidate questions for a later separately authorized decision or diagnostic. It does not authorize them.

A technically bounded diagnostic candidate is:

```text
NEXT_DIAGNOSTIC_CANDIDATE_SCOPE=NON_LOADABLE_BINARY_METADATA_DIFFERENCE_LOCALIZATION_ONLY
NEXT_DIAGNOSTIC_MODEL_WEIGHT_ACCESS=NONE
NEXT_DIAGNOSTIC_MODEL_EXECUTION=NONE
NEXT_DIAGNOSTIC_SPEND_USD=0
BUILD_ID_CAUSALITY=NEEDS_EVIDENCE
BYTE_OFFSET_TO_ELF_SECTION_MAPPING=NEEDS_EVIDENCE
NORMALIZATION_EXPERIMENT_AUTHORITY=NONE
```

Such a later diagnostic would need separate reviewed authority before execution. Its purpose would be to localize the already-observed same-source build variation without accepting, rewriting, stripping, or normalizing the binary by policy in advance.

The alternative policy path named by the parent authority also remains unselected:

```text
EXECUTION_TIME_IDENTITY_BINDING_POLICY_DISPOSITION=NONE
```

No policy record presently accepts execution-time identity binding as a substitute for byte-for-byte reconstruction.

## 12. Post-reconciliation authority state

Canonicalization of this result record may only establish the evidence interpretation below; it creates no successor execution authority.

```text
E004_REBUILD_REPRO_DIAGNOSTIC_EXECUTION_STATE=CONSUMED_COMPLETE
E004_REBUILD_REPRO_DIAGNOSTIC_AUTHORITY=CONSUMED_NOT_REUSABLE
REBUILD_NORMALIZATION_EXPERIMENT_AUTHORITY=NONE
BINARY_METADATA_LOCALIZATION_DIAGNOSTIC_AUTHORITY=NONE
EXECUTION_TIME_IDENTITY_BINDING_POLICY_DISPOSITION=NONE
MODEL_SOURCE_WEIGHT_ACQUISITION_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
CONVERSION_EXECUTION_AUTHORITY=NONE
MODEL_INFERENCE_AUTHORITY=NONE
BENCHMARK_EXECUTION_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_PAYLOAD_ACCESS_AUTHORITY=NONE
CONTAMINATION_ASSESSMENT_AUTHORITY=NONE
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TRAINING_AUTHORITY=NONE
SPEND_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0

COMPONENT_RUNTIME_RECONSTRUCTION=BLOCKED_SAME_PATH_FULL_BINARY_NONREPRODUCIBILITY
COMPONENT_PERSISTENT_CONVERSION_SUBJECT=INCOMPLETE
COMPONENT_E004=INCOMPLETE
COMPONENT_E004_STATE=BLOCKED_PREFLIGHT
COMPONENT_E005_STATE=NOT_REACHED
BACKBONE_WINNER=NEEDS_EVIDENCE
PROJECT_FINISHED=NO
```

E004 therefore remains unchecked in `tasks.md`.

## 13. Required merge-exit gate

This reconciliation may become canonical only after a fresh exact-head independent repository review verifies at least:

- authority merge `2fd2915024182100be0e5ce6ffb261e5b76f03bb`, reviewed implementation head `40f36acd949897f072fec4f1d51debbfc316d07f`, and guarded implementation merge `bc3ea6830fc0aaa674df2b439b74a98cda34bd20` are recorded exactly;
- run `33507754943`, attempt `1`, job `99855785119`, and terminal success are recorded exactly;
- the one-shot allowance is consumed and no retry/rerun/second execution is implied;
- all A1/A2/B1/B2 full SHA-256, ELF LOAD SHA-256, GNU Build-ID, and byte-count observations are copied exactly from retained terminal logs;
- A and B are both correctly classified as full-file non-repeatable while their measured ELF LOAD identities are repeatable;
- the three directly measured pairwise full-file difference counts are each 20 bytes and are not generalized into unmeasured pairwise comparisons;
- the one-time A1 equality to the earlier rebuilt-diagnostic full hash is not represented as deterministic reconstruction;
- normalized PATH identities are equal and PATH-causal attribution remains prohibited;
- no causal claim maps the 20-byte variation to GNU Build-ID or another ELF section without evidence;
- neither historical full-file identity is represented as reconstructed;
- the historical two-hash split is not represented as reproduced;
- mismatch cause remains `NEEDS_EVIDENCE` and runtime reconstruction remains blocked;
- Section 11 identifies only separately authorized candidate questions and creates no successor diagnostic, normalization, policy, model, conversion, inference, benchmark, contamination, A15, training, credential, upload, procurement/payment, or spend authority;
- E004 remains incomplete and E005 remains `NOT_REACHED`.

Required reviewer output:

```text
MATERIAL_BLOCKER=NO
```

Only guarded canonical merge of the exact independently reviewed head may make this diagnostic-result interpretation canonical.