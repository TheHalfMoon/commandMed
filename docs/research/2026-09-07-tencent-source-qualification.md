# Tencent External-Source Qualification — 2026-09-07

**Project:** `TheHalfMoon/commandMed`  
**Canonical base:** `fde75d3b2ed49e0aecb610545d6e7a6110d35f8d`  
**Artifact class:** repository-only external-source qualification / research record  
**Authority effect:** NONE  
**Implementation authority effect:** NONE  
**Model execution effect:** NONE  
**Tournament execution effect:** NONE  
**Training effect:** NONE  
**Credential/access effect:** NONE  
**Spend effect:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

Qualify three Founder-supplied public Tencent repositories as potential commandMed engineering references without silently importing code, dependencies, datasets, workflows, execution authority, credentials, or runtime assumptions.

The supplied sources are:

1. `Tencent/hpc-ops`
2. `Tencent/AICGSecEval`
3. `Tencent/AI-Infra-Guard`

This record answers only:

- what each source actually provides at the inspected immutable revision;
- whether its license posture is compatible in principle with future reuse;
- where it fits commandMed;
- what must **not** be imported into the current Spec 007 / E004 frontier;
- which future bounded engineering surfaces may benefit from the source.

It does not modify the current E004 execution frontier. In particular, it does not change:

```text
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

## 2. Inspection rule

Each source is bound to an immutable repository revision observed on 2026-09-07. Mutable branch names are informational only.

```text
SOURCE_1_REPOSITORY=Tencent/hpc-ops
SOURCE_1_BRANCH=main
SOURCE_1_REVISION=2a2e26562433a8ba4b504858f1c938eb7612c901

SOURCE_2_REPOSITORY=Tencent/AICGSecEval
SOURCE_2_BRANCH=master
SOURCE_2_REVISION=94428ebf45141bf4ecd365a51d596dcd51caa690

SOURCE_3_REPOSITORY=Tencent/AI-Infra-Guard
SOURCE_3_BRANCH=main
SOURCE_3_REVISION=e4e622af3ad2b8228ce82dd62b01415dd8ce2b9c
```

No source payload, dependency, container, benchmark, model, PoC, or executable was run as part of this qualification.

## 3. Source qualification summary

| Source | Primary value for commandMed | Current fit | Reuse posture | Current action |
|---|---|---|---|---|
| `Tencent/AI-Infra-Guard` | AI-agent, MCP, skill, infrastructure and prompt-security assurance patterns | **HIGH** for future security assurance; not part of current E004 tournament execution | Apache-2.0; attribution/NOTICE obligations must be preserved for copied code | `QUALIFIED_REFERENCE_PRIORITY_1`; design patterns may inform a later bounded security-hardening unit |
| `Tencent/AICGSecEval` | Repository-level AI-generated-code security benchmark methodology; static + dynamic verification | **HIGH** for future secure-code/agent evaluation | Apache-2.0; dataset-derived/project-derived licensing must be assessed separately from framework license | `QUALIFIED_REFERENCE_PRIORITY_2`; methodology/reference only until a dedicated benchmark-admission unit exists |
| `Tencent/hpc-ops` | Highly optimized CUDA inference operators and performance methodology | **LOW for current E004**, potentially high for future GPU/server research | MIT for hpc-ops code with bundled third-party components under their own licenses, including CUTLASS BSD-3-Clause | `QUALIFIED_REFERENCE_DEFERRED`; no current code import or dependency addition |

## 4. `Tencent/AI-Infra-Guard`

### 4.1 Observed source identity

```text
REPOSITORY=Tencent/AI-Infra-Guard
REVISION=e4e622af3ad2b8228ce82dd62b01415dd8ce2b9c
LICENSE_CLASS=Apache-2.0
LICENSE_ATTRIBUTION_REQUIREMENTS=PRESENT
```

The project describes itself as an AI red-teaming platform and currently exposes multiple security surfaces relevant to commandMed, including:

- Agent Scan;
- MCP Server scan;
- Agent Skill scan;
- AI infrastructure vulnerability scanning;
- jailbreak evaluation;
- prompt-security research;
- API/model relay auditing;
- structured security reports.

The inspected `agent-scan` surface implements a three-stage security-testing pattern:

```text
INFO_COLLECTION
-> PARALLEL_VULNERABILITY_DETECTION
-> VULNERABILITY_REVIEW
```

It includes detection classes directly relevant to a future commandMed agent/tool ecosystem:

```text
AUTHORIZATION_BYPASS
DATA_LEAKAGE
INDIRECT_PROMPT_INJECTION
TOOL_ABUSE
WEB_EXFILTRATION
AGENTIC_SUPPLY_CHAIN
UNEXPECTED_CODE_EXECUTION
INTER_AGENT_COMMUNICATION_SECURITY
CASCADING_FAILURE
HUMAN_AGENT_TRUST_EXPLOIT
```

The inspected `mcp-scan` surface provides a SARIF-compatible static/dynamic scanning pattern and explicitly covers MCP-oriented classes such as:

```text
TOKEN_AND_SECRET_EXPOSURE
PRIVILEGE_ESCALATION_AND_SCOPE_CREEP
TOOL_POISONING
SUPPLY_CHAIN_ATTACK
COMMAND_INJECTION_AND_EXECUTION
PROMPT_INJECTION
INSUFFICIENT_AUTH_AND_AUTHORIZATION
MISSING_AUDIT_AND_TELEMETRY
SHADOW_MCP_SERVER
CONTEXT_INJECTION_AND_OVERSHARING
NAME_CONFUSION
RUG_PULL
TOOL_SHADOWING
```

### 4.2 Strong commandMed fit

This source is the strongest of the three for commandMed's future security-assurance layer because it maps naturally to existing commandMed invariants:

- deterministic tool authority;
- least privilege;
- credential isolation;
- provenance and supply-chain evidence;
- prompt-injection resistance;
- auditability;
- fail-closed external-tool boundaries;
- no silent privilege expansion;
- separation between model output and deterministic authority.

Recommended future reuse is **pattern-first**, not platform import.

Candidate reusable ideas:

1. a closed commandMed AI-agent/MCP threat taxonomy;
2. SARIF output for repository/security findings;
3. security finding identity + dedup fingerprinting;
4. static pre-scan before any dynamic agent execution;
5. explicit tool-poisoning / tool-shadowing / command-injection gates;
6. credential-exfiltration and web-exfiltration negative fixtures;
7. security scorecards that retain raw findings rather than hiding hard failures behind averages;
8. separation of discovery, detection, and review phases.

### 4.3 Explicit non-adoption boundary

Do **not** vendor or enable the full AI-Infra-Guard platform in the current Spec 007 / E004 path.

Reasons:

- several modes expect external LLM/API credentials;
- dynamic scanning can contact external endpoints;
- the upstream project explicitly warns that its web deployment lacks an authentication mechanism and should not be exposed publicly;
- its default model/provider assumptions are not commandMed authority;
- its broad AI-security platform dependencies are unnecessary for the current model-tournament preflight;
- importing its Docker/services stack would violate Ponytail minimalism for the present bounded work.

Current disposition:

```text
AI_INFRA_GUARD_SOURCE_QUALIFIED=YES
AI_INFRA_GUARD_CODE_IMPORTED=NO
AI_INFRA_GUARD_DEPENDENCIES_INSTALLED=NO
AI_INFRA_GUARD_DYNAMIC_SCAN_AUTHORITY=NONE
AI_INFRA_GUARD_CREDENTIAL_USE_AUTHORITY=NONE
AI_INFRA_GUARD_RECOMMENDED_ROLE=FUTURE_SECURITY_ASSURANCE_REFERENCE
```

## 5. `Tencent/AICGSecEval`

### 5.1 Observed source identity

```text
REPOSITORY=Tencent/AICGSecEval
REVISION=94428ebf45141bf4ecd365a51d596dcd51caa690
LICENSE_CLASS=Apache-2.0
```

AICGSecEval provides a repository-level security evaluation framework for AI-generated code. Its inspected design combines:

- code-generation tasks derived from real-world repositories and CVE patches;
- repository/project context extraction;
- static security analysis;
- dynamic tests and vulnerability PoCs;
- agent-oriented evaluation;
- checkpoint/resume support for long evaluations.

Its stated coverage includes important secure-coding families derived from OWASP Top 10 and CWE Top 25, with multiple languages and 29 CWE vulnerability types in the described v2 dataset.

### 5.2 Strong commandMed fit

The highest-value contribution to commandMed is **evaluation methodology**, not immediate dataset ingestion.

Recommended future patterns:

1. repository-level rather than isolated-snippet security evaluation;
2. exact pre-change project context binding;
3. paired functional correctness + security correctness;
4. hybrid static + dynamic verdicts;
5. CVE-inspired regression fixtures;
6. replayable task/result identities;
7. agent-generated patch security evaluation;
8. checkpoint/resume that does not lose audit provenance.

This is particularly valuable if commandMed later exposes coding, workflow-authoring, MCP, plugin, or agent-building capabilities. It can also inform internal secure-development quality gates for AI-assisted repository changes.

### 5.3 Dataset and PoC caution

The framework's Apache-2.0 repository license does **not** automatically prove that every embedded or referenced task payload may be copied into commandMed under the same terms.

The benchmark derives tasks from external projects and CVE-related material. Therefore any future dataset/content admission must separately bind at least:

```text
SOURCE_PROJECT_IDENTITY
SOURCE_PROJECT_REVISION
SOURCE_FILE_OR_PATCH_IDENTITY
SOURCE_LICENSE
CVE_OR_ADVISORY_IDENTITY
PAYLOAD_LICENSE_OR_USE_BASIS
CONTENT_SHA256
MALICIOUS_OR_EXPLOIT_PAYLOAD_CLASSIFICATION
SANDBOX_REQUIREMENTS
NETWORK_BOUNDARY
EXECUTION_AUTHORITY
```

No vulnerability PoC should be executed merely because the framework repository is qualified as a reference.

Current disposition:

```text
AICGSECEVAL_SOURCE_QUALIFIED=YES
AICGSECEVAL_FRAMEWORK_IMPORTED=NO
AICGSECEVAL_DATASET_ADMITTED=NO
AICGSECEVAL_POC_EXECUTION_AUTHORITY=NONE
AICGSECEVAL_EXTERNAL_LLM_CREDENTIAL_AUTHORITY=NONE
AICGSECEVAL_RECOMMENDED_ROLE=FUTURE_REPOSITORY_SECURITY_EVALUATION_REFERENCE
```

## 6. `Tencent/hpc-ops`

### 6.1 Observed source identity and license

```text
REPOSITORY=Tencent/hpc-ops
REVISION=2a2e26562433a8ba4b504858f1c938eb7612c901
PRIMARY_LICENSE=MIT
THIRD_PARTY_COMPONENT_LICENSES=PRESERVED_SEPARATELY
CUTLASS_LICENSE=BSD-3-Clause
```

The source is a production-oriented CUDA operator library focused on high-throughput/low-latency LLM inference. The inspected operator catalog includes:

- prefill/decode attention;
- paged KV-cache paths;
- dynamic decode scheduling;
- block-sparse FP8 attention;
- BF16 × FP32 GEMM;
- FP8 grouped GEMM;
- fused MoE;
- fused AllReduce + residual + RMSNorm;
- fused sampling;
- normalization/RoPE/activation utilities.

The current upstream requirements and stated target are materially different from commandMed's current E004 successor lane:

```text
UPSTREAM_PRIMARY_GPU_TARGET=NVIDIA_H20_OR_SM90_CLASS
UPSTREAM_CUDA_REQUIREMENT=12.9_PLUS_FOR_FULL_WHEEL_PATH
UPSTREAM_PRIMARY_PRECISIONS=BF16_AND_FP8
CURRENT_COMMANDMED_E004_ZERO_SPEND_PATH=CPU_BOUND_FROZEN_LLAMA_CPP_AND_TRANSFORMERS_ROUTES
```

### 6.2 Why this source should be deferred now

HPC-Ops is valuable, but importing it into the current E004 tournament would change too many frozen variables simultaneously:

- hardware class;
- runtime backend;
- precision policy;
- build toolchain;
- dependency surface;
- resource/spend requirements;
- comparability with the already-frozen candidate execution route.

That would invalidate rather than strengthen the current E004 preflight.

### 6.3 Future value

HPC-Ops should remain a high-quality future reference for a separately authorized GPU/server efficiency program, especially for:

1. kernel-level latency profiling methodology;
2. attention scheduling under mixed-length requests;
3. sampling-kernel fusion;
4. communication/computation fusion;
5. precision-sensitive GEMM strategies;
6. reproducible operator benchmarking against multiple baselines;
7. future server-tier medical intelligence density research.

Any future code reuse must preserve MIT notice obligations and all third-party component notices/licenses. Importing the upstream `3rd/` tree wholesale is not approved by this qualification.

Current disposition:

```text
HPC_OPS_SOURCE_QUALIFIED=YES
HPC_OPS_CURRENT_E004_FIT=NO
HPC_OPS_CODE_IMPORTED=NO
HPC_OPS_CUDA_DEPENDENCY_ADDED=NO
HPC_OPS_GPU_EXECUTION_AUTHORITY=NONE
HPC_OPS_RECOMMENDED_ROLE=FUTURE_GPU_SERVER_PERFORMANCE_REFERENCE
```

## 7. Cross-source synthesis for commandMed

The three repositories are complementary rather than interchangeable.

### Security architecture

Use `AI-Infra-Guard` as the primary reference for **what to test** in AI-agent/tool/MCP security and for SARIF/security-reporting patterns.

### Security evaluation science

Use `AICGSecEval` as the primary reference for **how to evaluate generated repository changes** using reproducible repository context and hybrid static/dynamic evidence.

### Inference performance

Use `hpc-ops` as a future reference for **how to optimize GPU inference hot paths** after commandMed has a separately frozen GPU/server target and execution authority.

Recommended priority:

```text
PRIORITY_1=AI_INFRA_GUARD_SECURITY_TAXONOMY_AND_REPORTING_PATTERNS
PRIORITY_2=AICGSECEVAL_REPOSITORY_LEVEL_SECURITY_EVALUATION_METHODOLOGY
PRIORITY_3=HPC_OPS_FUTURE_GPU_INFERENCE_OPTIMIZATION_RESEARCH
```

## 8. Current E004 relationship

None of the three sources is required to complete the already-active E004 model-tournament preflight.

They must not be used to change:

- the frozen four-candidate set;
- the current llama.cpp / Transformers runtime identities;
- the model-load compatibility evidence;
- the zero-spend constraint;
- the current execution environment/resource/access sequencing;
- the A1-A14-equivalent prerequisite snapshot;
- A15 authority;
- tournament authority boundaries;
- Founder+ChatGPT winner-selection authority.

Therefore:

```text
TENCENT_SOURCE_PACKET_CHANGES_E004_FRONTIER=NO
TENCENT_SOURCE_PACKET_AUTHORIZES_CODE_IMPORT=NO
TENCENT_SOURCE_PACKET_AUTHORIZES_DEPENDENCY_INSTALL=NO
TENCENT_SOURCE_PACKET_AUTHORIZES_DATASET_ACCESS=NO
TENCENT_SOURCE_PACKET_AUTHORIZES_SECURITY_POC_EXECUTION=NO
TENCENT_SOURCE_PACKET_AUTHORIZES_GPU_EXECUTION=NO
```

## 9. Safe future implementation policy

If a later bounded spec selects a concrete source-derived feature, use this order:

1. bind the exact donor revision;
2. identify the smallest exact files/concepts needed;
3. verify the license of those exact files and transitive third-party material;
4. prefer reimplementation of the design pattern when that avoids unnecessary dependency or attribution complexity;
5. if copying code, preserve required copyright/license/NOTICE information;
6. add commandMed-native deterministic contracts and negative tests;
7. keep external network/credential behavior disabled unless separately authorized;
8. qualify exact-head CI before merge;
9. record provenance from donor revision to commandMed implementation;
10. never claim donor benchmark/security results as commandMed evidence without commandMed-specific execution.

## 10. Decision

```text
TENCENT_HPC_OPS=QUALIFIED_REFERENCE_DEFERRED
TENCENT_AICGSECEVAL=QUALIFIED_REFERENCE_PRIORITY_2
TENCENT_AI_INFRA_GUARD=QUALIFIED_REFERENCE_PRIORITY_1

IMMEDIATE_CODE_IMPORT=NO
IMMEDIATE_DEPENDENCY_ADDITION=NO
IMMEDIATE_DATASET_ADMISSION=NO
IMMEDIATE_EXTERNAL_SCAN_EXECUTION=NO
IMMEDIATE_GPU_EXECUTION=NO
CURRENT_E004_AUTHORITY_EXPANSION=NONE
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The next lawful action for these sources is future source-specific bounded planning/implementation only after the active E004 frontier permits adjacent work or a separate canonical bounded spec explicitly authorizes that work.
