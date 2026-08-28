# E004 Converter Runtime Dependency Reconciliation — 2026-08-28

**Spec:** 007 SFT V1  
**Canonical base:** `39f8e8a1793376cde7d6b8a0213e9e7f9b9b1a46`  
**Artifact class:** non-executing static runtime/dependency reconciliation  
**Authority effect:** NONE  
**Package installation performed:** NO  
**Python/converter execution performed:** NO  
**Model/source-weight access performed:** NO  
**Spend:** USD 0

This record narrows the runtime identity required by the already-prepared Decision B conversion subjects. It reads only exact pinned `llama.cpp` source and dependency manifests. It does not freeze an executable runtime and does not authorize conversion.

```text
CONVERSION_TOOL_REPOSITORY=ggml-org/llama.cpp
CONVERSION_TOOL_REVISION=c1d0e7a004015f23bc0233470b747b596f29b264
CONVERSION_TOOL_TREE=2255f4747492109298a5c997f374d49c2af3113d
CONVERSION_ENTRYPOINT=convert_hf_to_gguf.py
CONVERSION_ENTRYPOINT_GIT_BLOB=78ad26c6563062e2a801c9f76f77a7ce196dd195
CONVERSION_EXECUTION_AUTHORITY=NONE
```

## 1. Exact upstream dependency-manifest identities

```text
ROOT_PYPROJECT=pyproject.toml
ROOT_PYPROJECT_GIT_BLOB=46cf68ca1a398d40dc71f0eff043c03ceeaa73fe
ROOT_REQUIREMENTS=requirements.txt
ROOT_REQUIREMENTS_GIT_BLOB=f2a18d62879b4e37249b566d6d85fd9485fb20e2
HF_CONVERTER_REQUIREMENTS=requirements/requirements-convert_hf_to_gguf.txt
HF_CONVERTER_REQUIREMENTS_GIT_BLOB=b1f7c863e27e184e55408c9e5792158301c86547
LEGACY_CONVERTER_REQUIREMENTS=requirements/requirements-convert_legacy_llama.txt
LEGACY_CONVERTER_REQUIREMENTS_GIT_BLOB=28221fad0ce9790f91dc6adfbc893010454bdfe5
LOCAL_GGUF_PYPROJECT=gguf-py/pyproject.toml
LOCAL_GGUF_PYPROJECT_GIT_BLOB=d11c34a2186d7180345f0050c746df51043b5620
LOCAL_GGUF_VERSION=0.19.0
```

No root `uv.lock`, Poetry lockfile, pip hash-lock file, or equivalent fully resolved transitive dependency lock is present in the pinned root tree.

```text
UPSTREAM_FULLY_RESOLVED_DEPENDENCY_LOCK_PRESENT=NO
UPSTREAM_MANIFESTS_EQUAL_EXACT_TRANSITIVE_RUNTIME=NO
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256=NEEDS_EVIDENCE
```

## 2. Python runtime boundary

Pinned root `pyproject.toml` declares:

```text
PYTHON_DECLARED_RANGE=>=3.10,<3.15
```

Pinned local `gguf-py/pyproject.toml` declares:

```text
LOCAL_GGUF_PYTHON_FLOOR=>=3.10
```

These are compatibility constraints, not an exact interpreter identity.

```text
PYTHON_IMPLEMENTATION=NEEDS_EVIDENCE
PYTHON_EXACT_VERSION=NEEDS_EVIDENCE
PYTHON_EXECUTABLE_SHA256=NEEDS_EVIDENCE
PYTHON_RUNTIME_IDENTITY=NEEDS_EVIDENCE
```

A future execution-authoritative environment must bind the exact interpreter implementation/version and environment manifest before conversion.

## 3. Upstream declared converter dependencies

`requirements/requirements-convert_hf_to_gguf.txt` includes the legacy converter requirements and pins:

```text
TORCH_REQUIREMENT=torch==2.11.0
TORCH_EXTRA_INDEX=https://download.pytorch.org/whl/cpu
```

The included legacy requirements declare:

```text
NUMPY_REQUIREMENT=~=1.26.4
SENTENCEPIECE_REQUIREMENT=>=0.1.98,<0.3.0
TRANSFORMERS_REQUIREMENT===4.57.6
GGUF_DISTRIBUTION_REQUIREMENT=>=0.1.0
PROTOBUF_REQUIREMENT=>=4.21.0,<5.0.0
```

Root `pyproject.toml` independently declares:

```text
NUMPY_PROJECT_RANGE=>=1.26.4,<3.0.0
SENTENCEPIECE_PROJECT_RANGE=>=0.1.98,<0.3.0
TRANSFORMERS_PROJECT_VERSION=4.57.6
PROTOBUF_PROJECT_RANGE=>=4.21.0,<5.0.0
TORCH_PROJECT_RANGE=>=2.6.0,<3.0.0
GGUF_PROJECT_SOURCE=./gguf-py
```

Its Poetry platform mapping specifies `torch==2.11.0+cpu` for Linux through the explicit PyTorch CPU source. The requirements file and project metadata therefore establish a strong torch target but still do not constitute a cryptographic wheel/package lock.

```text
TORCH_EXACT_PACKAGE_ARTIFACT_SHA256=NEEDS_EVIDENCE
TRANSFORMERS_EXACT_PACKAGE_ARTIFACT_SHA256=NEEDS_EVIDENCE
OTHER_PACKAGE_ARTIFACT_SHA256_SET=NEEDS_EVIDENCE
PACKAGE_INDEX_SNAPSHOT_OR_WHEELHOUSE_IDENTITY=NEEDS_EVIDENCE
```

## 4. Local GGUF source must win

The pinned `convert_hf_to_gguf.py` and `conversion/base.py` both execute the same fail-open environment check:

```python
if 'NO_LOCAL_GGUF' not in os.environ:
    sys.path.insert(1, <PINNED_REPOSITORY>/gguf-py)
import gguf
```

For Decision B the intended source-bound runtime must therefore preserve local `gguf-py` import resolution from the exact pinned source tree.

```text
LOCAL_GGUF_SOURCE_MODE=REQUIRED
LOCAL_GGUF_SOURCE_TREE=gguf-py@c1d0e7a004015f23bc0233470b747b596f29b264
LOCAL_GGUF_PROJECT_VERSION=0.19.0
NO_LOCAL_GGUF_ENVIRONMENT_VARIABLE=PROHIBITED
NO_LOCAL_GGUF_MUST_BE_UNSET=YES
EXTERNAL_GGUF_CODE_AS_SELECTED_RUNTIME=PROHIBITED
```

The legacy requirements entry `gguf>=0.1.0` must not be interpreted as authority to execute an arbitrary resolver-selected GGUF implementation. It may influence dependency installation in an upstream-style environment, but selected runtime code must resolve to the pinned local source.

A future runtime attestation must prove the actual imported `gguf.__file__` resides under the pinned local source tree before conversion execution. This record does not perform that import.

```text
ACTUAL_GGUF_IMPORT_PATH_ATTESTATION=NEEDS_EVIDENCE
ACTUAL_GGUF_CODE_SHA256_OR_TREE_ATTESTATION=NEEDS_EVIDENCE
```

## 5. Local GGUF transitive declared dependencies

Pinned `gguf-py/pyproject.toml` declares:

```text
GGUF_NUMPY=>=1.17
GGUF_TQDM=>=4.27
GGUF_PYYAML=>=5.1
GGUF_REQUESTS=>=2.25
```

The selected local conversion path imports the local `gguf` package. `gguf/__init__.py` imports `metadata`, and pinned `metadata.py` directly imports `yaml`; therefore PyYAML is a real selected-path runtime dependency, not merely optional packaging metadata.

The selected local-only model path does not grant remote HF conversion mode. Any `requests` capability present through GGUF dependencies must remain unused for model acquisition/conversion execution unless separately authorized.

```text
REMOTE_HF_CONVERSION_MODE=NOT_SELECTED
REMOTE_MODEL_NETWORK_USE=PROHIBITED
GGUF_REQUESTS_PACKAGE_PRESENCE_DOES_NOT_AUTHORIZE_NETWORK=YES
```

## 6. Selected Granite/Qwen import surface

Pinned entrypoint directly imports `torch`, local `gguf`, and `conversion`.

Pinned `conversion/base.py` directly imports:

```text
transformers.AutoConfig
numpy
torch
local gguf
```

It attempts `mistral_common` imports under `try/except ImportError`; the selected Granite/Qwen subjects are not Mistral-format subjects.

Pinned `gguf/vocab.py` attempts `sentencepiece` and `mistral_common` under guarded imports. The frozen Granite/Qwen tokenizer surfaces select local tokenizer handling already documented elsewhere; no Mistral runtime authority is created here.

Pinned architecture loading is dynamic by exact HF architecture mapping rather than importing every architecture as a requirement for the selected path:

```text
GraniteMoeHybridForCausalLM -> conversion.granite
Qwen3ForCausalLM -> conversion.qwen
```

`conversion.granite` also imports the local `llama` and `mamba` converter modules. These selected modules rely on Python stdlib plus already-declared `numpy`, `torch`, `transformers`, and local `gguf` surfaces.

```text
MISTRAL_COMMON_REQUIRED_FOR_SELECTED_DECISION_B_SUBJECTS=NO_EVIDENCE_OF_REQUIREMENT
MISTRAL_COMMON_SELECTED_RUNTIME_AUTHORITY=NONE
```

## 7. Why upstream manifests are not an execution lock

The upstream files contain both exact pins and compatible-version ranges. They do not bind:

- exact Python interpreter artifact;
- exact NumPy/SentencePiece/Protobuf/TQDM/PyYAML/Requests versions;
- exact transitive dependencies of Transformers/Torch/Requests;
- exact wheel/sdist hashes;
- exact resolver version/behavior;
- exact index snapshot;
- exact installed-environment manifest.

Therefore the repository must not convert `requirements*.txt` or `pyproject.toml` identities into a false `DEPENDENCY_LOCK=PASS` claim.

```text
UPSTREAM_DEPENDENCY_DECLARATIONS=SOURCE_BOUND
EXACT_RESOLVED_RUNTIME_ENVIRONMENT=INCOMPLETE
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256=NEEDS_EVIDENCE
BUILD_ENVIRONMENT_MANIFEST_SHA256=NEEDS_EVIDENCE
PYTHON_RUNTIME_IDENTITY=NEEDS_EVIDENCE
CONVERSION_RUNTIME_EXECUTABLE_SHA256=NEEDS_EVIDENCE
```

## 8. Future exact-runtime evidence contract

Before any conversion execution authorization, a separate exact environment record must minimally bind:

```text
PYTHON_IMPLEMENTATION
PYTHON_EXACT_VERSION
PYTHON_EXECUTABLE_SHA256
OS_AND_ARCHITECTURE_IDENTITY
RESOLVER_AND_VERSION
PACKAGE_INDEX_OR_OFFLINE_WHEELHOUSE_BOUNDARY
EXACT_PACKAGE_NAME_VERSION_ARTIFACT_SHA256_SET
INSTALLED_ENVIRONMENT_MANIFEST_SHA256
GGUF_IMPORTED_FILE_PATH
GGUF_IMPORTED_SOURCE_IDENTITY
NO_LOCAL_GGUF_UNSET_ATTESTATION
NETWORK_BOUNDARY
CREDENTIAL_STATE
```

Preferred fail-closed posture for later authorization is an exact pre-provisioned/offline dependency set with artifact hashes, rather than resolving version ranges at conversion time. This is a preparation requirement, not authority to construct that environment now.

```text
PACKAGE_INSTALLATION_AUTHORITY=NONE_FROM_THIS_RECORD
RUNTIME_ENVIRONMENT_CREATION_AUTHORITY=NONE_FROM_THIS_RECORD
CONVERSION_EXECUTION_AUTHORITY=NONE
```

## 9. Current state

```text
CONVERTER_RUNTIME_SOURCE_DEPENDENCY_SURFACE=STATICALLY_RECONCILED
PINNED_LOCAL_GGUF_SOURCE_REQUIREMENT=IDENTIFIED
NO_LOCAL_GGUF_PROHIBITION=IDENTIFIED
UPSTREAM_FULLY_RESOLVED_DEPENDENCY_LOCK_PRESENT=NO
EXACT_RESOLVED_RUNTIME_ENVIRONMENT=NEEDS_EVIDENCE
DEPENDENCY_LOCK_OR_EXACT_DEPENDENCY_SET_SHA256=NEEDS_EVIDENCE
PYTHON_RUNTIME_IDENTITY=NEEDS_EVIDENCE
CONVERSION_RUNTIME_EXECUTABLE_SHA256=NEEDS_EVIDENCE
BUILD_ENVIRONMENT_MANIFEST_SHA256=NEEDS_EVIDENCE
MODEL_CONVERSION_AUTHORITY=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
BUILD_PASS=NO
E004=INCOMPLETE
E004_STATE=BLOCKED_PREFLIGHT
E005_STATE=NOT_REACHED
```

## Exclusions

This artifact performs no package installation, dependency resolution, Python import execution, converter execution, model/source-weight download, model loading, conversion, quantization, inference, benchmark/device execution, network model access, credential use, contamination assessment, training, procurement, personnel engagement, payment, or spend. It creates no workflow and consumes no authorized workflow run.
