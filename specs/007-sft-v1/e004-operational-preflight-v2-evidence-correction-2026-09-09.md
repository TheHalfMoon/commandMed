# E004 Operational Preflight V2 Evidence Correction — 2026-09-09

**Spec:** 007 SFT V1
**Scope:** `SPEC007_RESEARCH_ENGINEERING_COMPONENT_V1`
**Successor policy:** `SP007-RO-001`
**Historical V2 evidence run:** `34176481565`
**Historical V2 evidence job:** `101906795703`
**Historical V2 evidence head:** `225d0ebe280a4ae2305dcc84dd5795ba90d198d0`
**Historical V2 implementation merge:** `a1bc59ca4fa7ab9d3e0dc92346093eb444b504b0`
**Superseded evidence interpretation:** `specs/007-sft-v1/e004-operational-preflight-evidence-run-v2-failure-reconciliation-2026-09-08.md`
**Artifact class:** append-only evidence correction
**Authority effect:** SUSPENDS V3 AUTHORITY PENDING CORRECTED FOUNDER REVALIDATION
**Execution effect:** NONE
**Current authorized spend:** USD 0

## 1. Purpose

Correct a material factual error in the canonical interpretation of the single consumed V2 operational-preflight evidence run after direct reinspection of the immutable GitHub Actions job log and the exact workflow at the canonical implementation merge.

This document does not rewrite or delete historical evidence. It preserves the V2 run as failed and consumed, but supersedes the incorrect claim that V2 observed 28 dependency artifacts and failed at the 27-versus-28 artifact-count equality gate.

## 2. Exact immutable run identity

```text
V2_EVIDENCE_RUN_ID=34176481565
V2_EVIDENCE_JOB_ID=101906795703
V2_EVIDENCE_RUN_NUMBER=3
V2_EVIDENCE_RUN_ATTEMPT=1
V2_EVIDENCE_RUN_HEAD=225d0ebe280a4ae2305dcc84dd5795ba90d198d0
V2_IMPLEMENTATION_CANONICAL_MERGE=a1bc59ca4fa7ab9d3e0dc92346093eb444b504b0
V2_EVIDENCE_RUN_CONCLUSION=failure
V2_AUTHORIZED_RUNS_EXECUTED=1
V2_AUTHORIZED_RUNS_REMAINING=0
```

V2 remains permanently consumed. This correction creates no rerun, retry, replay, replacement marker, alternate branch, or new empirical allowance.

## 3. Correct terminal failure frontier

The exact V2 workflow first downloaded the bounded dependency wheelhouse and captured its verbose pip log. Before the workflow created `dependency-artifacts.tsv`, counted artifacts, calculated the dependency-set manifest digest, created a virtual environment, or performed an offline install, it parsed every HTTPS host appearing in the pip log and rejected any host outside this frozen set:

```text
pypi.org
files.pythonhosted.org
download.pytorch.org
```

The retained V2 job log records that pip obtained the exact compatible CPU Torch wheel through:

```text
download-r2.pytorch.org
```

The same retained log then terminates the Transformers/Torch reconstruction step with:

```text
unexpected pip provisioning hosts: ['download-r2.pytorch.org']
Process completed with exit code 1
```

Therefore the correct terminal disposition is:

```text
OPERATIONAL_PREFLIGHT_EVIDENCE=INCOMPLETE_FAIL_CLOSED_TRANSFORMERS_PROVISIONING_HOST_POLICY_MISMATCH
TRANSFORMERS_RUNTIME_RECONSTRUCTION=FAIL_BEFORE_DEPENDENCY_MANIFEST_CREATION
UNEXPECTED_TRANSFORMERS_PROVISIONING_HOST=download-r2.pytorch.org
DEPENDENCY_ARTIFACT_COUNT_GATE=NOT_EXECUTED
DEPENDENCY_SET_MANIFEST_SHA256_COMPARISON=NOT_EXECUTED
VIRTUAL_ENVIRONMENT_CREATION=NOT_EXECUTED
OFFLINE_DEPENDENCY_INSTALL=NOT_EXECUTED
INSTALLED_ENVIRONMENT_MANIFEST_SHA256_COMPARISON=NOT_EXECUTED
PYTHON_RUNTIME_SHA256_COMPARISON=NOT_EXECUTED
TRANSFORMERS_TORCH_OFFLINE_STATIC_IMPORT=NOT_EXECUTED
POST_STAGING_DEFAULT_DENY_NETWORK_PROOF=NOT_EXECUTED
```

## 4. Exact dependency artifacts actually saved before the host-policy failure

The V2 job log records exactly 27 `Saved .../wheelhouse/...` lines before the host validation failed. Their filenames are the same 27-artifact set that had previously succeeded in the canonical runtime-binding evidence run on 2026-09-05.

The previously successful runtime-binding job printed the complete deterministic artifact manifest. Reconstructing that exact printed TSV produces 27 rows and the already canonical digest:

```text
DEPENDENCY_ARTIFACT_COUNT=27
DEPENDENCY_SET_MANIFEST_SHA256=bcd0b7a64bca02f85b0561376b057823f8e5857b69328cb3aa3a1d3aff2c8c05
```

Exact historical manifest:

```text
certifi-2026.7.22-py3-none-any.whl	136983	62f22742b58a1a33014a2b6b706588a8d7e2a88ae7bd1a6ebe8c992928483775
charset_normalizer-3.5.1-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl	248801	b9af956078716df40d985fb0dfeb2c2120c5ca92ba4ff4b388acfd01cdc14d08
filelock-3.32.5-py3-none-any.whl	100003	142cd9fa77a872c5e78c62329a0d15278fadc686eb89e760017968961a4fd6b2
fsspec-2026.7.0-py3-none-any.whl	206583	b57ddbafedfaef7018c1ecab32aa200a9d7ca26b77965f64e48b70061249d279
hf_xet-1.6.0-cp38-abi3-manylinux2014_x86_64.manylinux_2_17_x86_64.whl	4464663	d62671bb130879cef0ee4c9ebe47a14af6c66ec53e6d84dc15936e5ffdfac82f
huggingface_hub-0.36.2-py3-none-any.whl	566395	48f0c8eac16145dfce371e9d2d7772854a4f591bcb56c9cf548accf531d54270
idna-3.19-py3-none-any.whl	68550	815e7be7a7806d54abb586dc943addc79e8b2ee16915059658cbeff4b1b43bf4
jinja2-3.1.6-py3-none-any.whl	134899	85ece4451f492d0c13c5dd7c13a64681a86afae63a5f347908daf103ce6d2f67
markupsafe-3.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl	22947	d6dd0be5b5b189d31db7cda48b91d7e0a9795f31430b7f271219ab30f1d3ac9d
mpmath-1.3.0-py3-none-any.whl	536198	a0b2b9fe80bbcd81a6647ff13108738cfb482d481d826cc0e02f5b35e5c88d2c
networkx-3.6.1-py3-none-any.whl	2068504	d47fbf302e7d9cbbb9e2555a0d267983d2aa476bac30e90dfbe5669bd57f3762
numpy-1.26.4-cp312-cp312-manylinux_2_17_x86_64.manylinux2014_x86_64.whl	17950613	675d61ffbfa78604709862923189bad94014bef562cc35cf61d3a07bba02a7ed
packaging-26.3-py3-none-any.whl	129956	d7193f7c8e4e93f444fde0262bf90af30e16fa0ad0ad44cb553c87339b23cd1c
protobuf-4.25.9-cp37-abi3-manylinux2014_x86_64.whl	295178	438c636de8fb706a0de94a12a268ef1ae8f5ba5ae655a7671fcda5968ba3c9be
pyyaml-6.0.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl	807870	ba1cc08a7ccde2d2ec775841541641e4548226580ab850948cbfda66a1befcdc
regex-2026.9.3-cp312-cp312-manylinux2014_x86_64.manylinux_2_17_x86_64.manylinux_2_28_x86_64.whl	801965	665207e41bacd435db001099eeab44103197c2c1a729d73ade74688a905ed4ce
requests-2.34.2-py3-none-any.whl	73075	2a0d60c172f83ac6ab31e4554906c0f3b3588d37b5cb939b1c061f4907e278e0
safetensors-0.8.0-cp310-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl	516040	fd6f3f93c9a0a7cc2788ee63fb763353d4bd2e89b0751bc78fcf7dda00bea774
sentencepiece-0.2.2-cp312-cp312-manylinux_2_27_x86_64.manylinux_2_28_x86_64.whl	1397736	c8a168b040bc61681293f79a949b5d911c8e25086f4260285b8d97ab5f1195da
setuptools-81.0.0-py3-none-any.whl	1062021	fdd925d5c5d9f62e4b74b30d6dd7828ce236fd6ed998a08d81de62ce5a6310d6
sympy-1.14.0-py3-none-any.whl	6299353	e091cc3e99d2141a0ba2847328f5479b05d94a6635cb96148ccb3f34671bd8f5
tokenizers-0.22.2-cp39-abi3-manylinux_2_17_x86_64.manylinux2014_x86_64.whl	3274982	369cc9fc8cc10cb24143873a0d95438bb8ee257bb80c71989e3ee290e8d72c67
torch-2.11.0+cpu-cp312-cp312-manylinux_2_28_x86_64.whl	190312281	f82e2ae20c1545bb03997d1cc3143d94e14b800038669ee1aca45808a9acc338
tqdm-4.70.0-py3-none-any.whl	80184	7f585706bfddbdebf89daac705b2dfcc16890130727d3197ca62c732b4310953
transformers-4.57.6-py3-none-any.whl	11993498	4c9e9de11333ddfe5114bc872c9f370509198acf0b87a832a0ab9458e2bd0550
typing_extensions-4.16.0-py3-none-any.whl	45571	481caa481374e813c1b176ada14e97f1f67a4539ce9cfeb3f350d78d6370c2e8
urllib3-2.7.0-py3-none-any.whl	131087	9fb4c81ebbb1ce9531cce37674bbc6f1360472bc18ca9a553ede278ef7276897
```

The V2 log itself did not print sizes or SHA-256 values after download because it terminated at host validation before manifest construction. The sizes and digests above are historical identity evidence from the earlier successful runtime-binding run, not newly measured V2 values. The V2 log independently confirms the same 27 filenames were saved.

## 5. Provisioning-host evidence

The retained V2 pip log includes these relevant public hosts:

```text
pypi.org
files.pythonhosted.org
download.pytorch.org
download-r2.pytorch.org
```

The exact compatible Torch artifact route is:

```text
TORCH_ARTIFACT_FILENAME=torch-2.11.0+cpu-cp312-cp312-manylinux_2_28_x86_64.whl
TORCH_ARTIFACT_SHA256=f82e2ae20c1545bb03997d1cc3143d94e14b800038669ee1aca45808a9acc338
TORCH_ARTIFACT_EFFECTIVE_HOST=download-r2.pytorch.org
```

This route is consistent with the earlier canonical metadata-only V4 diagnostic that independently proved `download-r2.pytorch.org:443` was the required compatible public Torch route for the same Ubuntu/Python subject.

## 6. Claims explicitly superseded

These previously canonical claims are materially incorrect for V2 and are superseded by this correction:

```text
OBSERVED_DEPENDENCY_ARTIFACT_COUNT=28
DEPENDENCY_ARTIFACT_COUNT_GATE=FAIL
ACTUAL_DEPENDENCY_SET_MANIFEST_SHA256=NOT_CAPTURED_BECAUSE_COUNT_GATE_FAILED
TRANSFORMERS_PROVISIONING_HOSTS=download.pytorch.org,files.pythonhosted.org,pypi.org
UNEXPECTED_TRANSFORMERS_PROVISIONING_HOSTS=NONE_OBSERVED
```

Correct replacement interpretation:

```text
V2_SAVED_DEPENDENCY_ARTIFACT_FILENAME_COUNT=27
V2_SAVED_DEPENDENCY_ARTIFACT_FILENAMES_MATCH_HISTORICAL_27_SET=YES
V2_DEPENDENCY_MANIFEST_CREATED=NO
V2_DEPENDENCY_ARTIFACT_COUNT_GATE=NOT_EXECUTED
V2_DEPENDENCY_SET_MANIFEST_SHA256_COMPARISON=NOT_EXECUTED
V2_UNEXPECTED_PROVISIONING_HOST=download-r2.pytorch.org
V2_TERMINAL_FAILURE_GATE=TRANSFORMERS_PROVISIONING_HOST_POLICY
```

## 7. Effect on the already captured V3 Founder Decision B

The canonical V3 decision request and its subsequent Founder Decision B capture were authored from the incorrect premise that V2 failed on a 28-versus-27 dependency-set drift.

The canonical Decision B capture makes its authority conditional on the canonical V3 decision-request constraints remaining satisfied. Direct reinspection now proves that the material failure premise in that request is not satisfied.

Therefore, fail closed:

```text
FOUNDER_E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION=E004_OPERATIONAL_PREFLIGHT_V3_ATTEMPT_DECISION_B
V3_DECISION_B_CAPTURE_STATUS=CANONICAL_BUT_MATERIALLY_STALE_AFTER_EVIDENCE_CORRECTION
V3_OPERATIONAL_PREFLIGHT_IMPLEMENTATION_AUTHORITY=SUSPENDED_PENDING_CORRECTED_FOUNDER_REVALIDATION
V3_OPERATIONAL_PREFLIGHT_STATIC_QUALIFICATION_AUTHORITY=SUSPENDED_PENDING_CORRECTED_FOUNDER_REVALIDATION
V3_OPERATIONAL_PREFLIGHT_RUNTIME_PROVISIONING_AUTHORITY=SUSPENDED_PENDING_CORRECTED_FOUNDER_REVALIDATION
V3_OPERATIONAL_PREFLIGHT_EVIDENCE_RUN_AUTHORITY=SUSPENDED_PENDING_CORRECTED_FOUNDER_REVALIDATION
V3_EVIDENCE_MARKER_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

Generic continuation language, ordinary approvals, or the stale Decision B token must not be interpreted as corrected revalidation authority.

## 8. Preserved safety and historical boundaries

```text
V1_RERUN=PROHIBITED
V2_RERUN=PROHIBITED
V2_RETRY=PROHIBITED
V2_REPLAY=PROHIBITED
V2_FAILED_JOB_RERUN=PROHIBITED
V2_SECOND_MARKER=PROHIBITED
MODEL_WEIGHT_ACQUISITION=PROHIBITED
MODEL_LOAD=PROHIBITED
MODEL_INFERENCE=PROHIBITED
EVALUATION_PAYLOAD_ACCESS=PROHIBITED
EVALUATION_PAYLOAD_EXECUTION=PROHIBITED
BENCHMARK_EXECUTION=PROHIBITED
TOURNAMENT_EXECUTION=PROHIBITED
A15_ACTIVATION=PROHIBITED
TRAINING=PROHIBITED
PRIVATE_CREDENTIAL_USE=PROHIBITED
SPEND=PROHIBITED
CURRENT_AUTHORIZED_SPEND_USD=0
PROJECT_FINISHED=NO
```

## 9. Dependency-safe next transition

The next safe transition is a corrected Founder revalidation decision request. No V3 implementation or empirical marker may be created until an exact post-canonical corrected Founder selection is supplied and separately captured canonically.
