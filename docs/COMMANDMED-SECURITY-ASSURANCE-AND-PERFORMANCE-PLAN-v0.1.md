# commandMed Security Assurance & Performance Engineering Plan v0.1

**Date:** 2026-09-08  
**Status:** ADDITIVE MASTER-PLAN AMENDMENT — PLANNING ONLY  
**Parent:** `docs/COMMANDMED-GRAND-MASTER-PLAN-v0.1.md`  
**Companion strategy:** `docs/COMMANDMED-MEDICAL-INTELLIGENCE-DENSITY-STRATEGY-v0.1.md`  
**Deep source analysis:** `docs/research/2026-09-08-tencent-deep-gap-analysis.md`  
**Source qualification:** `docs/research/2026-09-07-tencent-source-qualification.md`  
**Active execution frontier:** Spec 007 / E004 remains governed by its current canonical reconciliation  
**Authority effect:** NONE  
**Model execution authority effect:** NONE  
**Training authority effect:** NONE  
**Credential effect:** NONE  
**Spend effect:** NONE  
**Current authorized spend:** USD 0

> This amendment improves the long-range architecture and evidence plan. It does not authorize implementation of blocked future work, change the frozen E004 candidate/runtime/protocol surface, create model/tournament/training authority, or make any donor code canonical by reference.

## 1. Strategic upgrade

The original commandMed plan correctly optimizes for:

> **verified Health & Medical usefulness and safety per byte, joule, and second**.

This amendment extends that north star with two required dimensions that are implicit but not yet sufficiently formalized:

> **verified trustworthiness per integration** and **verified system efficiency per bottleneck**.

The resulting system objective becomes:

```text
MEDICAL_CAPABILITY
+ SAFETY
+ EVIDENCE_INTEGRITY
+ AGENT_TOOL_RUNTIME_SECURITY
+ SOFTWARE_SUPPLY_CHAIN_INTEGRITY
+ RESOURCE_EFFICIENCY
```

No dimension is allowed to compensate for a critical failure in another hard-gated dimension.

## 2. Why this amendment exists

The Founder supplied three high-value engineering sources:

```text
Tencent/AI-Infra-Guard@e4e622af3ad2b8228ce82dd62b01415dd8ce2b9c
Tencent/AICGSecEval@94428ebf45141bf4ecd365a51d596dcd51caa690
Tencent/hpc-ops@2a2e26562433a8ba4b504858f1c938eb7612c901
```

Deep review shows that commandMed should not copy these projects wholesale. Instead, it should absorb the strongest architecture principles while preserving commandMed's stricter medical evidence and authority discipline.

The amendment introduces five cross-cutting programs:

1. **AI Security Assurance Plane**
2. **Agent / Tool Trust Plane**
3. **Secure AI Engineering Assurance**
4. **Software Supply-Chain & Donor Provenance**
5. **Profile-First Performance Engineering**

These are planning programs, not active implementation specs.

## 3. Non-negotiable inheritance

Nothing in this amendment weakens:

- Spec 001 evaluation-before-optimization;
- Spec 002 hard safety gates;
- Spec 003 provenance/license/contamination rules;
- Spec 004 deterministic tournament semantics;
- Spec 005 exact execution/resource governance;
- Spec 006 deterministic medical-tool authority;
- Spec 007 current bounded authority;
- `AGENTS.md` no-fabrication and Ponytail rules;
- no PHI / Private Gold access without explicit authority;
- no hidden external credential or provider use;
- no spend without explicit budget authority;
- no model/training execution merely because a source demonstrates how to do it.

## 4. Source-use permission and legal boundary

The Founder has stated that commandMed has permission to copy source code from the supplied sources.

That project-level permission is useful, but commandMed must still preserve all applicable upstream obligations.

Current observed source-license posture:

```text
Tencent/AI-Infra-Guard=Apache-2.0_WITH_ATTRIBUTION_NOTICE_REQUIREMENTS
Tencent/AICGSecEval=Apache-2.0
Tencent/hpc-ops=MIT_WITH_THIRD_PARTY_COMPONENT_LICENSES
Tencent/hpc-ops/CUTLASS=BSD-3-Clause
```

A root `LICENSE` file was not observed in commandMed at the canonical base used for this amendment. Therefore:

```text
DONOR_CODE_COPY_PLANNING=ALLOWED
DONOR_CODE_COPY_MERGE_FOR_REDISTRIBUTION=BLOCKED_PENDING_COMMANDMED_SOFTWARE_LICENSE_POSTURE_AND_FILE_LEVEL_LINEAGE
```

This is a distribution-governance gate, not a rejection of source reuse.

## 5. Architecture amendment A — AI Security Assurance Plane

### 5.1 Objective

Make security of the **AI system path** a first-class commandMed property, not a side effect of ordinary code quality.

The medical answer path may eventually contain:

```text
USER_INPUT
-> MODEL
-> RETRIEVAL
-> TOOL
-> MCP / SKILL / PLUGIN
-> EXTERNAL OR LOCAL RUNTIME
-> STRUCTURED RESULT
-> SAFETY SHIELD
-> RESPONSE
```

Every arrow is a trust boundary.

### 5.2 Core architecture

Inspired by the strongest AI-Infra-Guard pattern, commandMed should use:

```text
DETERMINISTIC PRE-SCAN
-> VERSIONED RULE ENGINE
-> OPTIONAL AUTHORIZED MODEL-ASSISTED ANALYSIS
-> DETERMINISTIC FINDING NORMALIZATION
-> SECURITY HARD GATE
```

Rule-first behavior is mandatory where a deterministic test exists.

An LLM security reviewer may increase coverage, but it never becomes the sole truth source for critical findings.

### 5.3 Minimum future threat taxonomy

The eventual commandMed security taxonomy should cover at least:

```text
SEC01_INDIRECT_PROMPT_INJECTION
SEC02_DIRECT_PROMPT_INJECTION
SEC03_AUTHORIZATION_BYPASS
SEC04_SECRET_OR_DATA_EXFILTRATION
SEC05_TOOL_ABUSE
SEC06_TOOL_POISONING
SEC07_TOOL_SHADOWING
SEC08_TOOL_NAME_CONFUSION
SEC09_RUG_PULL_OR_BEHAVIOR_DRIFT
SEC10_COMMAND_INJECTION_OR_UNEXPECTED_EXECUTION
SEC11_SSRF_OR_WEB_EXFILTRATION
SEC12_AGENTIC_SUPPLY_CHAIN
SEC13_INSECURE_DEPENDENCY_OR_COMPONENT
SEC14_PRIVILEGE_ESCALATION_OR_SCOPE_CREEP
SEC15_INTER_AGENT_COMMUNICATION_FAILURE
SEC16_CONTEXT_OVER_SHARING
SEC17_MISSING_AUDIT_OR_TELEMETRY
SEC18_CASCADING_FAILURE
SEC19_HUMAN_AGENT_TRUST_EXPLOIT
SEC20_MODEL_OR_API_RELAY_SUBSTITUTION
SEC21_MODEL_OR_API_BACKDOOR_SIGNAL
SEC22_ENCODING_OR_BYTECODE_BYPASS
```

The exact taxonomy must be frozen in a later bounded spec before it becomes executable policy.

### 5.4 Security findings

Future security evidence should use a commandMed-native canonical record with fields conceptually equivalent to:

```text
finding_id
finding_sha256
rule_id
rule_version
subject_id
subject_sha256
severity
hard_gate_class
source_stage
static_evidence
runtime_evidence_if_authorized
artifact_path
start_line
end_line
fingerprint
reproducibility_state
review_state
remediation_state
```

Canonical JSON is the source of truth.

SARIF 2.1.0 should be an interoperability projection for GitHub Code Scanning and developer tooling, not the canonical scientific record.

### 5.5 Security scoring rule

Do not copy donor score formulas directly.

commandMed policy:

```text
CRITICAL_OR_NONCOMPENSABLE_SECURITY_FAILURE != AVERAGEABLE_DEDUCTION
```

A high overall security score cannot offset:

- credential exfiltration;
- unauthorized command execution;
- patient-data exposure;
- deterministic medical-tool authority bypass;
- unbounded network access;
- unsafe tool poisoning;
- release artifact provenance failure.

## 6. Architecture amendment B — Agent / Tool Trust Plane

### 6.1 Objective

Extend the existing deterministic medical-tool philosophy into an explicit least-privilege trust contract for every future tool, MCP server, plugin, skill, agent or specialist module.

### 6.2 Required future integration record

Every integration should eventually bind:

```text
integration_id
integration_version_or_revision
artifact_sha256
source_provenance
license_state
capability_set
allowed_operations
allowed_filesystem_scope
allowed_network_scope
allowed_target_domains_or_endpoints
credential_scope
input_data_classes
output_schema
side_effect_class
privilege_level
timeout_and_resource_limits
audit_event_contract
revocation_behavior
safety_precedence
```

### 6.3 Default posture

```text
NETWORK=DENY_BY_DEFAULT
PRIVATE_NETWORK_TARGETS=DENY_BY_DEFAULT
LOOPBACK_TARGETS=DENY_BY_DEFAULT_FOR_REMOTE_TOOLING
LINK_LOCAL_TARGETS=DENY_BY_DEFAULT
REDIRECTS_WITH_CREDENTIALS=DENY_BY_DEFAULT
CREDENTIAL_PERSISTENCE=PROHIBITED_BY_DEFAULT
SHELL_EXECUTION=PROHIBITED_UNLESS_EXPLICITLY_REQUIRED_AND_SANDBOXED
UNDECLARED_TOOLS=REJECT
UNDECLARED_SIDE_EFFECTS=REJECT
```

Local deterministic medical tools may use narrower purpose-built contracts that never require external-network behavior.

### 6.4 Tool-result trust

A tool result is not automatically authoritative because it came from a registered tool.

Future tool-result records should bind:

- tool identity;
- operation identity;
- arguments;
- evidence/source identity;
- timestamp/freshness where relevant;
- signature/hash where available;
- deterministic validation status;
- trust class;
- conflict-resolution precedence.

## 7. Architecture amendment C — Runtime / Provider Integrity

### 7.1 Objective

Prevent hidden runtime/model/provider substitution from invalidating medical and reproducibility evidence.

### 7.2 Local runtime path

For local runtimes, continue the existing commandMed pattern:

- exact source revision;
- exact binary/library hashes;
- exact dependency manifests;
- exact model artifact hashes;
- exact runtime flags;
- exact environment/resource binding;
- no ambient substitution.

### 7.3 External or relay-backed path

If commandMed ever uses an external or relay-backed model/API for a permitted purpose, add a separate integrity layer inspired by AI-Infra-Guard's API Checker concepts.

Potential future evidence classes:

```text
DECLARED_PROVIDER_IDENTITY
OBSERVED_API_BEHAVIOR_FINGERPRINT
MODEL_SUBSTITUTION_SIGNAL
BACKDOOR_OR_ANOMALY_SIGNAL
RELAY_CONFIGURATION_IDENTITY
TRANSPORT_SECURITY_STATE
KEY_HANDLING_STATE
OUTBOUND_TARGET_VALIDATION_STATE
BUDGET_STATE
```

No black-box fingerprint can prove cryptographic model identity. The plan must describe such evidence as anomaly/substitution detection, not absolute proof.

## 8. Architecture amendment D — Secure AI Engineering Assurance

### 8.1 Objective

Treat AI-assisted repository changes as a separate engineering risk class when they touch safety, security, provenance, execution, data, evaluation or release surfaces.

AICGSecEval demonstrates the value of project-level context plus static/dynamic security evidence. commandMed should adopt the methodology, not the upstream execution assumptions.

### 8.2 Dual-gate principle

For sensitive AI-assisted changes:

```text
FUNCTIONAL_CORRECTNESS=PASS
AND
SECURITY_CORRECTNESS=PASS
```

A passing unit or integration test suite is not a security result.

### 8.3 Repository-context evaluation

A future secure-change record should bind:

```text
repository_base_commit
repository_tree
change_patch_sha256
changed_path_set_sha256
change_risk_class
functional_test_evidence
static_security_evidence
dynamic_security_evidence_if_authorized
review_evidence
```

### 8.4 Stability

For high-risk generated changes, one successful generation may be insufficient evidence.

A later bounded policy may require repeated generations or mutation/replay to measure:

- vulnerability recurrence;
- security stability;
- functional stability;
- nondeterministic failure rate.

Do not require repeated generation for every ordinary change; apply it to high-risk surfaces where the cost is justified.

### 8.5 Dynamic verification sandbox

If dynamic vulnerability tests or PoCs are ever admitted:

```text
SANDBOX=DISPOSABLE
PRIVILEGE=LEAST_REQUIRED
NETWORK=OFF_UNLESS_TEST_REQUIRES_EXACT_ALLOWLIST
CREDENTIALS=NONE_OR_SYNTHETIC
HOST_MOUNTS=MINIMAL_READ_ONLY_WHERE_POSSIBLE
PHI=PROHIBITED
PRIVATE_GOLD=PROHIBITED
TIMEOUT=MANDATORY
RESOURCE_LIMIT=MANDATORY
ARTIFACT_CLEANUP=MANDATORY
```

No PoC execution follows automatically from source qualification.

## 9. Architecture amendment E — Software Supply-Chain & Donor Provenance

### 9.1 Objective

Extend commandMed's strong data/model provenance discipline to software code, dependencies and build artifacts.

### 9.2 Donor-code lineage

Any future copied or substantially adapted source should bind at least:

```text
donor_repository
donor_revision
donor_path
donor_blob_sha
donor_license
donor_notice_requirement
third_party_component_state
permission_basis
adoption_mode=COPIED|ADAPTED|PATTERN_REIMPLEMENTED
commandmed_destination_path
commandmed_introducing_commit
modification_notice_state
attribution_state
security_review_state
test_evidence_state
```

### 9.3 Root software-license gate

Before distributing copied donor code, commandMed should freeze its own repository software-license posture.

The final choice belongs in a dedicated governance/Founder decision if required by canonical governance.

Until that posture exists:

```text
PATTERN_RESEARCH=ALLOWED
PLANNING=ALLOWED
CODE_COPY_EXPERIMENT_ON_NONCANONICAL_BRANCH=ONLY_IF_SEPARATELY_AUTHORIZED
CANONICAL_REDISTRIBUTED_DONOR_CODE=BLOCKED
```

### 9.4 Release supply-chain evidence

Future release evidence should include, where appropriate:

- dependency lock identity;
- SBOM;
- third-party license/NOTICE aggregation;
- source/build provenance;
- generated artifact hashes;
- vulnerability scan evidence;
- signed or attested release artifacts where supported;
- known-vulnerability disposition;
- reproducible build notes or explicit nondeterminism statement.

## 10. Architecture amendment F — Profile-First Performance Engineering

### 10.1 Objective

Prevent premature hardware-specific optimization from weakening portability, reproducibility or medical equivalence.

hpc-ops provides strong methodology signals, especially mixed workload benchmarking, correctness comparison and named baselines.

### 10.2 Optimization admission gate

A future optimization should enter engineering only when:

1. the exact end-to-end workload is frozen;
2. profiling proves the target operation is a material bottleneck;
3. the optimization target hardware/runtime is named;
4. baseline implementation and precision are frozen;
5. correctness-equivalence criteria are frozen;
6. the expected end-to-end benefit is material enough to justify complexity.

If these are not true:

```text
OPTIMIZATION_ADMISSION=NO_GO
```

### 10.3 Benchmark tiers

Future performance work should separate:

```text
TIER_1_CORRECTNESS_SMOKE
TIER_2_OPERATOR_MICROBENCHMARK
TIER_3_END_TO_END_SYSTEM_BENCHMARK
TIER_4_MEDICAL_AND_SAFETY_EQUIVALENCE
TIER_5_SUSTAINED_RESOURCE_THERMAL_ENERGY_EVIDENCE
```

No lower tier can substitute for a required higher tier.

### 10.4 Workload shapes

In addition to average-case latency, measure future serving/runtime paths under:

- short uniform inputs;
- long uniform inputs;
- mixed-length batches;
- extreme long-tail cases;
- bounded concurrency;
- context-growth / KV-cache pressure;
- sustained operation and thermal/throttling behavior where relevant.

### 10.5 Timing policy

Future performance records should freeze:

- warmup count;
- measurement count;
- timing mechanism;
- synchronization semantics;
- median / percentile policy;
- exact hardware/software environment;
- baseline versions;
- precision;
- batch/request shape;
- context lengths;
- caching policy;
- error bars or run dispersion when applicable.

### 10.6 Optimization kill criteria

Reject an optimization if any of the following holds:

- no material end-to-end benefit;
- correctness regression;
- medical/safety regression;
- unacceptable memory increase;
- unacceptable portability cost;
- hardware coverage too narrow for the product tier;
- dependency/build complexity disproportionate to measured gain;
- irreproducible benchmark advantage;
- gain exists only in synthetic microbenchmarks but not real commandMed workloads.

## 11. Source-adoption matrix

### 11.1 AI-Infra-Guard

**Adopt conceptually:**

- rule-first / LLM-augmented security architecture;
- scan-engine separation;
- static pre-scan;
- agent/MCP/skill threat taxonomy;
- SARIF projection;
- finding fingerprints;
- provider/API integrity concepts;
- SSRF/network/key boundaries.

**Adapt rather than copy wholesale:**

- security orchestration;
- security scorecards;
- multi-stage review;
- rule data packaging.

**Defer / reject now:**

- full platform import;
- web UI/services stack;
- provider defaults;
- external LLM dependence;
- broad Docker deployment;
- dynamic scans against real endpoints without authority.

### 11.2 AICGSecEval

**Adopt conceptually:**

- repository-level context;
- static + dynamic evidence composition;
- functional + security dual gates;
- repeated-cycle stability;
- resumable evaluation;
- per-vulnerability-family reporting.

**Adapt rather than copy wholesale:**

- task/result schemas;
- checkpoint/resume mechanism;
- sandbox execution controller.

**Defer / reject now:**

- privileged-container assumptions;
- dataset wholesale import;
- CVE/PoC payload execution;
- external LLM credential behavior.

### 11.3 hpc-ops

**Adopt conceptually now for future planning:**

- mixed-shape benchmark scenarios;
- correctness-vs-performance comparison;
- median/repeated timing;
- named baseline comparisons;
- operator-level benchmark isolation.

**Potential future code adoption only after profiling:**

- dynamic decode scheduling;
- fused sampling;
- attention/GEMM/fusion kernels;
- GPU-specific optimization techniques.

**Reject for current E004:**

- CUDA/SM90 runtime substitution;
- BF16/FP8 path changes;
- vendor tree import;
- GPU spend or new hardware dependency.

## 12. Roadmap integration without renumbering frozen specs

The existing numbered roadmap remains intact. This amendment does **not** renumber Specs 000–017.

Instead, add cross-cutting inheritance gates to future work when the dependency frontier reaches those specs.

### 12.1 Spec 006 inheritance

Future extensions of Patient Safety Scaffold / Deterministic Tools should inherit:

- Agent / Tool Trust Plane;
- tool poisoning/shadowing checks;
- least privilege;
- auditability;
- result provenance;
- external network/credential boundaries.

### 12.2 Spec 011 inheritance

Calibration & Abstention should include adversarial/security slices when security attacks alter confidence, tool choice or escalation behavior.

### 12.3 Spec 012 inheritance

Quantization & Device should inherit the Profile-First Performance Engineering rules and require exact correctness/medical-equivalence after runtime/kernel changes.

### 12.4 Specs 014 / 016 inheritance

Multimodal and specialist modules should enter through the same Agent / Tool Trust Plane rather than becoming privileged side channels.

### 12.5 Spec 017 Release Review inheritance

Before a release claim, the release evidence package should eventually include:

```text
MEDICAL_SAFETY_GATES=PASS
EVALUATION_AND_CONTAMINATION_GATES=PASS
SOFTWARE_SUPPLY_CHAIN_EVIDENCE=PASS
AGENT_TOOL_SECURITY_EVIDENCE=PASS_IF_APPLICABLE
PROMPT_INJECTION_AND_TOOL_POISONING_EVIDENCE=PASS_IF_APPLICABLE
RUNTIME_PROVIDER_INTEGRITY_EVIDENCE=PASS_IF_APPLICABLE
AI_ASSISTED_HIGH_RISK_CHANGE_SECURITY_EVIDENCE=PASS
SBOM_AND_LICENSE_NOTICE_STATE=PASS
RELEASE_ARTIFACT_PROVENANCE=PASS
DEVICE_PERFORMANCE_AND_MEDICAL_EQUIVALENCE=PASS_FOR_CLAIMED_TIERS
```

A future bounded Release Review spec must decide the exact evidence records and thresholds. This amendment does not pre-authorize them.

## 13. Priority order

The strongest dependency-safe long-range priority is:

```text
P0_PRESERVE_AND_FINISH_ACTIVE_E004_FRONTIER
P1_FREEZE_COMMANDMED_SOFTWARE_LICENSE_AND_DONOR_PROVENANCE_GOVERNANCE_BEFORE_CODE_COPY
P2_DEFINE_AI_SECURITY_ASSURANCE_AND_AGENT_TOOL_TRUST_CONTRACTS
P3_DEFINE_SECURE_AI_ENGINEERING_ASSURANCE_FOR_HIGH_RISK_REPOSITORY_CHANGES
P4_BIND_RUNTIME_PROVIDER_INTEGRITY_WHERE_EXTERNAL_OR_RELAY_ROUTES_EXIST
P5_APPLY_PROFILE_FIRST_PERFORMANCE_ENGINEERING_AFTER_REAL_BOTTLENECKS_EXIST
P6_MAKE_SECURITY_AND_SUPPLY_CHAIN_EVIDENCE_PART_OF_RELEASE_REVIEW
```

This ordering prevents attractive donor features from derailing the scientific dependency frontier.

## 14. Gap-closure success criteria

This planning amendment should be considered successfully realized only when future bounded specs eventually prove, as applicable:

### Security

- closed threat taxonomy exists;
- deterministic pre-scan exists;
- canonical finding records exist;
- hard security gates are non-compensable;
- agent/tool least-privilege manifests exist;
- prompt/tool injection tests exist;
- network/credential boundaries are testable and fail closed;
- security evidence can be exported as SARIF without losing canonical identity.

### Secure engineering

- high-risk AI-generated patches require functional + security evidence;
- repository context is identity-bound;
- sandboxed dynamic verification exists only when separately authorized;
- instability/repeated-run risk is measured where justified.

### Supply chain

- root commandMed software-license posture is explicit;
- copied donor files have exact lineage;
- third-party/NOTICE obligations are preserved;
- SBOM/provenance exist for release artifacts;
- known vulnerabilities have explicit disposition.

### Performance

- optimizations are admitted only after profiling;
- microbenchmarks freeze exact comparable baselines;
- correctness is checked before speed claims;
- mixed/tail workloads are represented;
- end-to-end gain is confirmed;
- medical/safety equivalence survives optimization;
- hardware-specific code remains isolated behind explicit runtime/tier boundaries.

## 15. Features intentionally not added to the roadmap now

The deep review does **not** justify immediate addition of:

- a large security platform service;
- a web security dashboard;
- generic plugin marketplaces;
- an always-on LLM security judge;
- external-model relay infrastructure;
- CUDA kernel framework dependencies;
- a new GPU training program;
- vulnerability-PoC corpus ingestion;
- a second general orchestration framework.

These would violate Ponytail discipline without a measured need.

## 16. Founder / governance decisions that may become necessary later

Future irreversible transitions may require explicit decisions for:

1. commandMed root software-license/distribution posture;
2. whether copied donor code or pattern reimplementation is preferred for specific components;
3. whether external/relay model providers are ever an allowed production or evaluation route;
4. security dynamic-test sandbox budget and infrastructure;
5. target GPU/server tier if a future hpc-ops-derived performance path is justified;
6. acceptable security release thresholds beyond non-compensable critical failures.

These decisions should be requested only when they become the next dependency blocker.

## 17. Relationship to current E004

This amendment changes none of the following current E004 facts or gates:

```text
FOUR_CANDIDATE_MODEL_LOAD_COMPATIBILITY_GATE=PASS
CURRENT_AUTHORIZED_PREEXECUTION_SUBJECT_SHA256=NONE
SUCCESSOR_PASS_PREFLIGHT=NO
A15_ACTIVATION=ABSENT_NOT_AUTHORIZED
TOURNAMENT_EXECUTION_PERFORMED=NO
MODEL_WINNER_SELECTED=NO
TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The currently canonical operational-preflight Founder decision surface remains independent and must be followed exactly.

## 18. Final planning disposition

```text
AI_INFRA_GUARD=HIGH_VALUE_ADAPTIVE_SOURCE
AICGSECEVAL=HIGH_VALUE_EVALUATION_METHODOLOGY_SOURCE
HPC_OPS=HIGH_VALUE_FUTURE_PERFORMANCE_SOURCE

WHOLESALE_VENDORING=NO
PATTERN_FIRST_ADOPTION=YES
FILE_LEVEL_CODE_COPY=FUTURE_BOUNDED_AFTER_LICENSE_PROVENANCE_GATE
CURRENT_E004_MODIFICATION=NO
CURRENT_MODEL_OR_TOURNAMENT_AUTHORITY_EXPANSION=NONE
CURRENT_TRAINING_AUTHORITY=NONE
CURRENT_AUTHORIZED_SPEND_USD=0
```

The project should use the donor sources aggressively where they close measured gaps, but preserve commandMed's stronger medical governance, evidence discipline, minimalism and fail-closed authority model.
