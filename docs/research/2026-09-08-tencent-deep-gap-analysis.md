# commandMed Tencent Source Deep Gap Analysis — 2026-09-08

**Project:** `TheHalfMoon/commandMed`  
**Canonical base:** `97fdb627a01ab2b40706077c433522affb98d12c`  
**Artifact class:** repository-only architecture / research analysis  
**Authority effect:** NONE  
**Implementation authority effect:** NONE  
**Model execution effect:** NONE  
**Training effect:** NONE  
**Current authorized spend:** USD 0

## 1. Purpose

This analysis performs a second-pass, architecture-level review of the Founder-supplied Tencent sources after the initial qualification packet:

- `Tencent/AI-Infra-Guard@e4e622af3ad2b8228ce82dd62b01415dd8ce2b9c`
- `Tencent/AICGSecEval@94428ebf45141bf4ecd365a51d596dcd51caa690`
- `Tencent/hpc-ops@2a2e26562433a8ba4b504858f1c938eb7612c901`

The goal is not to import code immediately. The goal is to identify architectural gaps in commandMed and improve the long-range plan without altering the active Spec 007 / E004 frontier.

The Founder has stated that commandMed has permission to copy source code from the supplied sources. This is recorded as a project-level source-use authorization signal, but it does not erase upstream license, copyright, NOTICE, third-party component, patent, attribution, or redistribution obligations. Any future code copy remains subject to exact file-level provenance and compatibility review.

## 2. Baseline strengths that must be preserved

The existing commandMed plan is already unusually strong in the following areas and should not be replaced by donor architecture:

- evaluation-before-optimization;
- exact artifact and revision binding;
- evidence/provenance and contamination controls;
- deterministic safety boundaries;
- explicit abstention / escalation states;
- tool authority separation;
- English + Arabic evaluation;
- resource-aware medical intelligence density;
- fail-closed execution authority;
- immutable evidence and append-only reconciliation;
- model/load/runtime identity binding;
- no implicit credential, spend, PHI, Private Gold, or training authority.

The Tencent sources should strengthen missing engineering planes around these foundations, not replace commandMed governance.

## 3. Source-level findings

### 3.1 AI-Infra-Guard — strongest security architecture source

Observed architecture patterns with high commandMed relevance:

1. **Rule-first, LLM-augmented security**
   - deterministic rules remain the primary fast/reproducible layer;
   - model reasoning is layered on top for ambiguous or complex findings;
   - rule data is version-controlled rather than hidden in code.

2. **Independent scan engines with shared reporting/orchestration**
   - infrastructure scanning;
   - MCP scanning;
   - agent scanning;
   - skill scanning;
   - prompt/jailbreak evaluation;
   - model/API relay auditing.

3. **Multi-stage security review**
   - `INFO_COLLECTION -> DETECTION -> VULNERABILITY_REVIEW`;
   - standalone fast paths can run only deterministic/static portions.

4. **AI-agent threat classes missing from commandMed planning**
   - indirect prompt injection;
   - authorization bypass;
   - tool abuse;
   - tool poisoning;
   - tool shadowing;
   - name confusion;
   - rug-pull behavior;
   - credential/data leakage;
   - SSRF / web exfiltration;
   - unexpected code execution;
   - agentic supply-chain attacks;
   - inter-agent communication security;
   - cascading failures;
   - human-agent trust exploitation.

5. **Security interoperability**
   - SARIF 2.1.0 output;
   - stable rule IDs;
   - normalized severity;
   - file/line locations;
   - partial fingerprints for deduplication;
   - fix suggestions.

6. **Static pre-scan before agent reasoning**
   - encoding/charset anomalies;
   - bytecode bypass indicators;
   - suspicious dependency/build/cache references;
   - high-risk shell/download patterns.

7. **Provider / model relay integrity**
   - black-box model/API substitution and poisoning detection;
   - API-key isolation;
   - no key persistence;
   - SSRF-resistant target validation;
   - private/loopback/link-local denial by default;
   - no redirect following in sensitive clients;
   - explicit budget warning for expensive probes.

High-value commandMed lesson:

> Safety of the medical answer is not enough. The agent/tool/runtime path that produces the answer must itself be a first-class security subject.

### 3.2 AICGSecEval — strongest secure AI-engineering evaluation source

Observed methodology with high commandMed relevance:

1. **Repository-level rather than snippet-level evaluation**
   - project context is part of the task;
   - generated changes are evaluated inside a real repository/environment.

2. **Functional + security evaluation as separate axes**
   - code can function correctly and still fail security;
   - security cannot be inferred from tests alone.

3. **Static + dynamic verification**
   - static analysis for breadth;
   - executable test/PoC checks for higher-confidence verification.

4. **Repeated cycles**
   - the same task is generated/evaluated more than once;
   - stability is measured rather than assumed from one successful attempt.

5. **Per-vulnerability-family reporting**
   - aggregate scores are supplemented by category-specific evidence.

6. **Checkpoint/resume for long evaluations**
   - partial work is durable;
   - interrupted evaluations do not silently restart and mix provenance.

7. **Real-project/CVE-derived task design**
   - useful methodological inspiration, but every source payload requires separate license and safety review before commandMed admission.

Important commandMed adaptation:

> commandMed should evaluate AI-assisted repository changes with a dual gate: functional correctness AND security correctness. A passing unit-test suite must never imply secure code.

Important non-adoption:

- do not copy the upstream privileged-container assumptions;
- do not execute vulnerability PoCs without a dedicated sandbox and authority;
- do not import the upstream dataset merely because the framework itself is Apache-2.0;
- do not inherit external-LLM credential behavior into commandMed by default.

### 3.3 hpc-ops — strongest future performance-engineering source

Observed methodology with high commandMed relevance:

1. **Operator-specific benchmark suites**
   - attention decode;
   - route GEMM;
   - fused MoE;
   - fused AllReduce + RMSNorm;
   - RoPE / KV-store paths;
   - sampler.

2. **Mixed-shape workload scenarios**
   - uniform short requests;
   - uniform long requests;
   - highly skewed mixed batches;
   - extreme long-tail requests.

3. **Timing discipline**
   - quick event timing for smoke tests;
   - release-style `nsys`/NVTX timing;
   - median latency rather than a single measurement.

4. **Correctness before speed claims**
   - benchmark paths include explicit correctness comparison options.

5. **Multiple comparable baselines**
   - speedup is reported against named baseline implementations rather than an unqualified absolute number.

6. **Optimization is hardware- and precision-specific**
   - SM90/H20 focus;
   - BF16/FP8 paths;
   - CUDA-specific build requirements.

High-value commandMed lesson:

> Performance optimization should be admitted only after profiling proves an end-to-end bottleneck, and every optimization must preserve correctness/medical-equivalence under the exact target hardware, precision and runtime.

Current E004 non-fit remains correct: importing hpc-ops into the frozen CPU/zero-spend successor route would invalidate comparability.

## 4. Gap matrix

| Gap ID | Missing or under-specified commandMed capability | Severity | Source signal | Recommended plan action |
|---|---|---:|---|---|
| G-SEC-01 | No dedicated AI/agent/MCP threat model | CRITICAL | AI-Infra-Guard | Add cross-cutting AI Security Assurance Plane |
| G-SEC-02 | No closed taxonomy for tool poisoning/shadowing/name-confusion/rug-pull | HIGH | AI-Infra-Guard MCP/Skill Scan | Freeze commandMed-native taxonomy before dynamic agent release |
| G-SEC-03 | No canonical security finding schema + fingerprint | HIGH | AI-Infra-Guard SARIF | Define canonical finding record and SARIF projection |
| G-SEC-04 | No static pre-scan for encoded/bytecode/dependency smuggling | HIGH | AI-Infra-Guard Skill Scan | Require deterministic pre-scan before any LLM-assisted security analysis |
| G-SEC-05 | No project-level runtime/provider/model-relay integrity program | HIGH | AI-Infra-Guard API Checker | Add provider/runtime identity attestation for any external or relay-backed route |
| G-SEC-06 | No explicit project-level SSRF/outbound-network policy for agent/tool integrations | CRITICAL | AI-Infra-Guard API Checker | Default-deny private/link-local/loopback targets and redirects unless separately authorized |
| G-SEC-07 | No release gate for agent/tool security regressions | CRITICAL | AI-Infra-Guard | Add non-compensable security gate to release evidence |
| G-SEC-08 | No dedicated sandbox contract for security PoCs/dynamic agent scans | CRITICAL | AICGSecEval + AI-Infra-Guard | Require isolated, disposable, least-privilege sandbox and explicit execution authority |
| G-ENG-01 | AI-assisted code changes are not evaluated as a distinct risk class | HIGH | AICGSecEval | Add Secure AI Engineering Assurance program |
| G-ENG-02 | Functional tests can pass without a mandatory security verdict | HIGH | AICGSecEval | Require dual functional/security result for qualifying AI-generated changes in sensitive surfaces |
| G-ENG-03 | No repeated-generation stability metric for AI code changes | MEDIUM | AICGSecEval | Add optional stability evidence for high-risk generated changes |
| G-ENG-04 | No repository-context security benchmark program | MEDIUM | AICGSecEval | Define later bounded benchmark methodology, not immediate dataset import |
| G-SC-01 | No root commandMed `LICENSE` observed | CRITICAL FOR CODE IMPORT | All donor licenses | Freeze repository distribution/license posture before copied donor code is merged |
| G-SC-02 | No software SBOM/provenance/signing plan found | HIGH | AI-Infra-Guard supply-chain focus | Add software supply-chain evidence to release requirements |
| G-SC-03 | No machine-readable donor-code lineage ledger | HIGH | Existing data/model provenance precedent | Add exact source-revision/file/blob/license/destination lineage contract |
| G-SC-04 | No project-wide NOTICE aggregation policy | MEDIUM | Apache/MIT/BSD donor obligations | Require NOTICE/third-party attribution propagation when applicable |
| G-PERF-01 | No operator-optimization admission gate | HIGH | hpc-ops | Optimize only measured bottlenecks with end-to-end benefit evidence |
| G-PERF-02 | No explicit mixed-length/tail-latency workload class | MEDIUM | hpc-ops dynamic decode | Add skewed/mixed workload performance slices |
| G-PERF-03 | Microbenchmark gains could be mistaken for system gains | HIGH | hpc-ops | Require end-to-end confirmation before adopting operator optimization |
| G-PERF-04 | Performance claims need explicit correctness-equivalence gate | CRITICAL | hpc-ops `--check` pattern + commandMed medical invariants | Every performance optimization must pass functional + medical/safety equivalence |
| G-PERF-05 | Baseline comparison policy is under-specified for future GPU kernels | MEDIUM | hpc-ops benchmark methodology | Freeze comparable baselines, precision, shapes, hardware and timing mode before claims |
| G-OBS-01 | Security evidence is not normalized into a common report plane | HIGH | AI-Infra-Guard SARIF | Use canonical JSON as source of truth plus SARIF export for CI tooling |
| G-OBS-02 | No explicit security-result dedup/fingerprint contract | MEDIUM | AI-Infra-Guard partial fingerprints | Add deterministic fingerprint for recurring findings |
| G-REL-01 | Release Review spec does not explicitly require software/agent supply-chain security evidence | CRITICAL | Combined sources | Extend release evidence contract through additive planning amendment |

## 5. Architecture synthesis

The sources suggest adding five cross-cutting planes to the existing commandMed system architecture.

### 5.1 AI Security Assurance Plane

```text
DETERMINISTIC PRE-SCAN
-> RULE-BASED SECURITY CHECKS
-> OPTIONAL AUTHORIZED MODEL-ASSISTED ANALYSIS
-> DETERMINISTIC EVIDENCE NORMALIZATION
-> SECURITY REVIEW / HARD GATE
```

Rules remain source-controlled and versioned. LLM output never becomes a security truth source by itself.

### 5.2 Agent / Tool Trust Plane

Every future agent/tool/MCP integration should bind:

- identity;
- version/revision;
- declared capabilities;
- allowed filesystem scope;
- allowed network scope;
- credential scope;
- tool-call schema;
- privilege level;
- data classes it may receive;
- deterministic safety precedence;
- audit/logging expectations;
- revocation/kill behavior.

### 5.3 Secure AI Engineering Plane

High-risk AI-assisted repository changes should be evaluated as:

```text
PATCH IDENTITY
+ REPOSITORY CONTEXT IDENTITY
+ FUNCTIONAL VERDICT
+ SECURITY VERDICT
+ STATIC FINDINGS
+ AUTHORIZED DYNAMIC FINDINGS
+ STABILITY / REPLAY EVIDENCE WHEN REQUIRED
```

### 5.4 Performance Engineering Plane

```text
END_TO_END PROFILE
-> BOTTLENECK QUALIFICATION
-> OPERATOR CANDIDATE
-> CORRECTNESS EQUIVALENCE
-> MICROBENCHMARK
-> END_TO_END RE-MEASUREMENT
-> MEDICAL/SAFETY EQUIVALENCE
-> ADOPT OR REJECT
```

A microbenchmark speedup alone never authorizes production adoption.

### 5.5 Software Supply-Chain Plane

Future releasable software should bind:

- dependency lock identity;
- SBOM identity;
- source provenance;
- build provenance;
- donor-code lineage;
- license/NOTICE obligations;
- generated artifact checksums;
- signed/attested release artifacts where the release system supports it;
- security scan evidence;
- known-vulnerability disposition.

## 6. Source-adoption disposition after deep review

### AI-Infra-Guard

```text
OVERALL_DISPOSITION=ADAPT_HIGH_PRIORITY
FULL_PLATFORM_VENDORING=REJECT_CURRENTLY
PATTERN_ADOPTION=YES_FUTURE_BOUNDED
CODE_COPY_ELIGIBILITY=YES_ONLY_AFTER_LICENSE_AND_PROVENANCE_GATES
CURRENT_E004_EFFECT=NONE
```

Highest-value future adoption targets:

- threat taxonomy;
- rule-first architecture;
- deterministic pre-scan;
- SARIF projection;
- security finding fingerprints;
- MCP/Skill/Agent security classes;
- SSRF/network/credential boundaries;
- API/model-relay integrity concepts.

### AICGSecEval

```text
OVERALL_DISPOSITION=ADAPT_METHODOLOGY_HIGH_PRIORITY
FRAMEWORK_VENDORING=REJECT_CURRENTLY
DATASET_IMPORT=REQUIRES_SEPARATE_SOURCE_ADMISSION
POC_EXECUTION=REQUIRES_SEPARATE_SANDBOX_AND_AUTHORITY
CURRENT_E004_EFFECT=NONE
```

Highest-value future adoption targets:

- repository-context evaluation;
- functional + security dual gating;
- static + dynamic evidence composition;
- repeated-run stability;
- resumable evaluation with provenance.

### hpc-ops

```text
OVERALL_DISPOSITION=DEFER_CODE_ADOPTION_KEEP_METHODS
BENCHMARK_METHODOLOGY_ADOPTION=YES_FUTURE
CUDA_KERNEL_IMPORT=NO_CURRENTLY
GPU_RUNTIME_CHANGE=NO_CURRENTLY
CURRENT_E004_EFFECT=NONE
```

Highest-value future adoption targets:

- profile-first optimization;
- mixed-shape/tail scenarios;
- median/repeated timings;
- named comparable baselines;
- correctness checks before speed claims;
- future dynamic scheduling / fusion only when commandMed profiling justifies them.

## 7. What should not be copied

Even with Founder source-use permission, copying more code is not automatically better.

Do not copy by default:

- full AI-Infra-Guard web/platform stack;
- upstream external-provider defaults or API-key handling assumptions;
- privileged Docker behavior from AICGSecEval;
- vulnerability PoC payloads without separate review;
- entire AICGSecEval datasets without per-source licensing;
- hpc-ops `3rd/` tree wholesale;
- SM90/CUDA-only kernels into portable commandMed runtime paths;
- donor scoring formulas when they conflict with commandMed non-compensable safety policy;
- any upstream benchmark result as if it were commandMed evidence.

## 8. Plan-level conclusions

The original commandMed plan remains strong on medical scientific integrity but is incomplete as a modern AI system plan in three places:

1. **AI-native security:** model/tool/agent/MCP and provider integrity need first-class architecture and hard gates.
2. **AI-native software engineering:** generated repository changes need security-aware evaluation, not just ordinary CI.
3. **performance engineering discipline:** operator optimization needs profile-first admission and end-to-end medical-equivalence evidence.

A fourth prerequisite appears before donor code import:

4. **software distribution governance:** commandMed must freeze its root software-license posture and donor-code provenance/NOTICE mechanism before copied source is merged for redistribution.

These conclusions are incorporated into the additive master-plan amendment created alongside this analysis.
