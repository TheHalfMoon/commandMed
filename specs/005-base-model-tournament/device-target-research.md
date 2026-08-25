# Spec 005 — Mass-Reach Device Target Research

**Lifecycle:** CLARIFY ONLY
**Evidence capture date:** 2026-08-23
**Canonical commandMed base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`
**Founder clarifications:** `MASS_REACH_FIVE_TARGET_SET` accepted on 2026-08-23 (bounded clarification session 3, question 1); `PLATFORM_NATIVE_PEAK_MEMORY` accepted on 2026-08-23 (bounded clarification session 4, question 2); `2G_CORE_HARD_CAP` accepted on 2026-08-23 (bounded clarification session 4, question 3)

> Read-only device-target, memory-measurement, and memory-threshold clarification evidence. No model was run on any device and no performance or measured-memory claim is made. Acceptance freezes the required target set, the platform-native peak-memory measurement method, and the 8K Core absolute peak-memory hard ceiling only; it does not authorize device execution, model access, weight retrieval, conversion, benchmark execution, or planning.

## 1. Why the existing two-tier wording is insufficient by itself

Founder decision `FD-002=FLAGSHIP_PLUS_MODERN_MIDRANGE` remains canonical, but the later `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY` requires evidence that reaches beyond a current flagship and one comfortable midrange phone.

A model intended for mass installation must eventually be tested against:

1. current flagship capability;
2. an older low-memory iPhone still representative of the installed base;
3. modern Android midrange hardware;
4. explicit 4-GB-class Android hardware;
5. a weak ordinary x86 laptop envelope.

The purpose is not to claim universal compatibility from five devices. The purpose is to anchor reproducible lower/upper resource boundaries instead of inferring deployability from parameter count.

## 2. Frozen named-device/resource set

### A. Current flagship Apple phone — iPhone 17 Pro

```text
ROLE=FLAGSHIP_PHONE_REPRESENTATIVE
DEVICE=Apple iPhone 17 Pro
OBSERVED_RAM=12_GB
RAM_EVIDENCE_SOURCE=Xcode_26_reported_by_MacRumors
PLATFORM=iOS
```

Apple does not advertise iPhone RAM directly; the 12 GB value is derived from Xcode 26 device information reported by MacRumors. The current iPhone 17 Pro therefore provides a high-end Apple performance/thermal/energy anchor, not the mass-reach lower bound.

### B. Low-memory Apple phone — iPhone 13

```text
ROLE=APPLE_LOW_RESOURCE_REPRESENTATIVE
DEVICE=Apple iPhone 13
OBSERVED_RAM=4_GB
SOC=A15_Bionic
PLATFORM=iOS
```

The 4 GB RAM value is derived from Xcode strings reported at launch. This device is materially more important to commandMed's “works on iPhones” ambition than testing only a current flagship because it establishes an older 4-GB-class Apple constraint.

### C. Modern midrange Android — Samsung Galaxy A56 5G

Frozen exact memory class:

```text
ROLE=MODERN_MIDRANGE_ANDROID_REPRESENTATIVE
DEVICE=Samsung Galaxy A56 5G
RAM=8_GB
STORAGE=128_OR_256_GB_SKU
PLATFORM=Android
```

Samsung Gulf's official product specifications report 8 GB memory for the inspected A56 5G SKUs.

### D. Low-resource Android — Samsung Galaxy A16 5G

Frozen exact memory class:

```text
ROLE=LOW_RESOURCE_ANDROID_REPRESENTATIVE
DEVICE=Samsung Galaxy A16 5G
RAM=4_GB
STORAGE=128_GB
PLATFORM=Android
```

Samsung Gulf's official specifications report 4 GB memory for the inspected 128 GB Galaxy A16 5G SKU. This gives Spec 005 a named physical Android representative for the already-frozen `LOW_RESOURCE_PHONE_TEST_ENVELOPE=4_GB_CLASS`.

### E. Weak-laptop resource envelope — Intel Processor N100 + 8 GB RAM

```text
ROLE=LOW_RESOURCE_X86_LAPTOP_ENVELOPE
CPU=Intel Processor N100
CPU_CORES=4
CPU_THREADS=4
MAX_TURBO=3.40_GHz
TDP=6_W
ISA=x86_64_AVX2
RAM=8_GB
GPU=Intel_UHD_integrated
TARGET_OS=Windows_11_x64_OR_EQUIVALENT_LINUX_x86_64
```

Intel's official specification lists the N100 as a 4-core/4-thread 6 W mobile processor with up to 3.40 GHz and AVX2 support. An 8 GB memory envelope is intentionally below the processor's supported 16 GB maximum and represents inexpensive ordinary laptops/mini PCs rather than a developer workstation.

A specific retail laptop SKU can be bound later if physical-device execution requires one. For deterministic evidence design, the CPU/RAM/OS envelope is the more important invariant.

## 3. Frozen target-set clarification policy

```text
DEVICE_EVIDENCE_POLICY=MASS_REACH_FIVE_TARGET_SET
FLAGSHIP_REPRESENTATIVE=Apple_iPhone_17_Pro_12GB
APPLE_LOW_RESOURCE_REPRESENTATIVE=Apple_iPhone_13_4GB
MODERN_MIDRANGE_ANDROID_REPRESENTATIVE=Samsung_Galaxy_A56_5G_8GB
LOW_RESOURCE_ANDROID_REPRESENTATIVE=Samsung_Galaxy_A16_5G_4GB
LOW_RESOURCE_LAPTOP_ENVELOPE=Intel_N100_8GB_x86_64
```

All five targets must eventually use the same canonical GGUF model identity wherever technically possible and the same immutable llama.cpp core revision under the separately frozen runtime-identity policy. Platform wrappers/builds may differ, but wrapper/runtime differences must be exact and cannot silently change the evaluated model artifact or shared core revision.

A physical-device substitution is not permitted after candidate results are observed. Before execution, any unavailable exact retail device may be replaced only through a separately reviewed pre-result clarification that preserves the same or stricter resource class and records the reason and new exact identity.

## 4. Frozen platform-native peak-memory measurement policy

For bounded clarification session 4 question 2, the founder accepted `PLATFORM_NATIVE_PEAK_MEMORY`:

```text
MEMORY_MEASUREMENT_POLICY=PLATFORM_NATIVE_PEAK_MEMORY

IOS_PRIMARY_PEAK_METRIC=LEDGER_PHYS_FOOTPRINT_PEAK
IOS_OS_MEMORY_TERMINATION=HARD_FAIL

ANDROID_PRIMARY_PEAK_METRIC=RSS_TRACE_PEAK
ANDROID_SECONDARY_MEMORY_METRIC=TOTAL_PSS
ANDROID_LMK_OR_OOM_TERMINATION=HARD_FAIL

LINUX_PRIMARY_PEAK_METRIC=CGROUP_V2_MEMORY_PEAK
LINUX_OOM_TERMINATION=HARD_FAIL

FULL_QUALIFICATION_PROCESS_SET_ACCOUNTED=YES
MEASUREMENT_WINDOW=FULL_COLD_QUALIFICATION_RUN
BASELINE_BEFORE_MODEL_LOAD=RECORDED
PEAK_ABSOLUTE_BYTES=RECORDED
PEAK_DELTA_FROM_BASELINE=RECORDED

PEAK_WORKING_RAM_ENGINEERING_TARGET=2_GiB_OR_LESS
CROSS_PLATFORM_RAW_METRIC_RANKING=PROHIBITED
```

Interpretation:

1. iOS qualification uses the platform's physical-footprint peak as the primary process-memory metric; a memory-pressure/OS termination during the measured qualification run is a hard runtime failure regardless of whether a final metric sample can be written;
2. Android qualification records a time-resolved RSS peak as the primary peak metric and total PSS as secondary context; LMK/OOM termination during the measured run is a hard runtime failure;
3. the Linux/x86-64 qualification path uses a dedicated cgroup v2 boundary for the complete required qualification process set and records `memory.peak`; OOM termination is a hard runtime failure;
4. if the eventual weak-laptop execution path uses Windows rather than Linux, a separately reviewed pre-execution clarification must bind a Windows-native peak-working-set/accounting method with semantics that cover the same required process set; this decision does not silently treat Linux cgroup metrics as Windows evidence;
5. the measured window spans the complete cold qualification run, including the required runtime/wrapper processes from the recorded pre-load baseline through model load, prompt processing, generation, and teardown/measurement capture as defined by the later exact run protocol;
6. the baseline before model load, absolute peak bytes, and peak delta from baseline are all recorded. The absolute platform-native peak is the primary resource evidence; delta is diagnostic and cannot hide a high absolute footprint;
7. memory accounting must cover the full qualification process set required to deliver the tested local inference path. Helper/runtime child processes may not be omitted merely to improve the reported number;
8. raw platform-native memory numbers are not mixed into a cross-platform scientific ranking metric because iOS footprint, Android RSS/PSS, and Linux cgroup accounting have different semantics. They are qualification/resource evidence interpreted within each frozen target path.

This policy freezes the measurement family and required records, not the exact sampling interval/tool invocation, concrete OS/runtime build, or performance threshold. Those remaining values must be bound before execution and cannot be chosen after candidate results are observed.

## 5. Frozen 8K Core RAM hard gate

For bounded clarification session 4 question 3, the founder accepted `2G_CORE_HARD_CAP`:

```text
CORE_8K_MEMORY_GATE=2G_CORE_HARD_CAP
CORE_8K_PEAK_MEMORY_HARD_CEILING=2_GiB
CORE_8K_PEAK_MEMORY_HARD_CEILING_BYTES=2147483648
CORE_8K_HARD_CEILING_APPLIES_TO_ALL_FIVE_TARGETS=YES
CORE_8K_HARD_CEILING_USES_PLATFORM_NATIVE_PRIMARY_METRIC=YES
CORE_8K_MEMORY_TERMINATION=HARD_FAIL

CORE_8K_PEAK_DELTA=DIAGNOSTIC_ONLY
CORE_8K_ABSOLUTE_PEAK=HARD_GATE_INPUT

STRESS_16K_PEAK_MEMORY=RECORDED
STRESS_16K_OS_MEMORY_TERMINATION=HARD_FAIL
STRESS_16K_ABSOLUTE_RAM_HARD_CEILING=NOT_FROZEN

CANDIDATE_SPECIFIC_RAM_EXCEPTION=PROHIBITED
POST_RESULT_RAM_CEILING_CHANGE=PROHIBITED
```

Interpretation:

1. the common `8192`-token Core qualification condition on every frozen target must remain at or below an absolute platform-native peak of `2 GiB` (`2147483648` bytes) for the complete qualification process set;
2. this is an absolute peak gate, not a baseline-subtracted gate. The recorded peak delta remains diagnostic only and cannot rescue a run whose absolute peak exceeds the ceiling;
3. OS/LMK/OOM memory termination remains a hard failure even if the last captured sample was below `2 GiB`;
4. the same `2 GiB` Core gate applies to the 4 GB, 8 GB, and 12 GB frozen targets. A higher-memory target does not receive a looser Core ceiling merely because more physical RAM is available;
5. the gate is evaluated using the platform-native primary metric frozen in `PLATFORM_NATIVE_PEAK_MEMORY`: iOS physical-footprint peak, Android RSS-trace peak, and Linux cgroup-v2 `memory.peak`; the Windows equivalent, if Windows is ultimately selected for the N100 path, must be separately bound before execution while preserving the same absolute `2 GiB` ceiling semantics;
6. required `16384`-token stress evidence records platform-native peak memory and treats OS memory termination as a hard failure, but this clarification does not impose the `2 GiB` absolute ceiling on the 16K stress tier;
7. no candidate-specific RAM exception, device-specific Core ceiling, or post-result increase of the `2 GiB` threshold is permitted. Any future universal replacement must occur through separately reviewed pre-result clarification before candidate outcomes are known.

This turns the previously frozen `<=2 GiB` engineering target into a hard qualification gate specifically for the 8K Core mass-reach condition. It does not create a new 16K absolute RAM ceiling and does not authorize execution.

## 6. What is now frozen — and what remains unresolved

The target set, common 8K/16K context policy, symmetric Q8_0 KV policy, fixed prompt/generation budget, cold 512/128 prompt-processing policy, immutable shared-core runtime identity method, platform-native peak-memory measurement method, and `2G_CORE_HARD_CAP` are frozen clarification contracts. They do not authorize execution.

Still unresolved:

- exact immutable llama.cpp core SHA and concrete platform build manifests;
- exact OS/build versions and iOS/Android wrapper/application identities;
- exact tokenizer/template and token-accounting implementation;
- exact memory instrumentation/tool invocation and sampling cadence where applicable, consistent with the frozen platform-native metric semantics;
- any 16K stress absolute RAM ceiling beyond mandatory peak recording and OS-termination failure semantics;
- TTFT/prefill/decode/sustained-throughput thresholds;
- battery/energy and thermal measurement protocol;
- repetition/warm-up/aggregation methodology;
- whether non-memory performance failures on each target are hard disqualifications versus separately scoped compatibility claims;
- the consequence of required 16K stress evidence beyond its mandatory evidence status where in scope.

Those must be frozen before execution and never chosen after observing candidate results.

## 7. Why this set and memory contract are preferable to flagship-only or one-number evidence

- iPhone 17 Pro proves current Apple performance potential but has 12 GB RAM and is too forgiving to serve as a mass-reach lower bound.
- iPhone 13 gives a 4 GB Apple constraint and a substantially older SoC generation.
- Galaxy A56 gives a current mainstream Android midrange anchor.
- Galaxy A16 5G gives a named 4 GB Android constraint.
- Intel N100 + 8 GB gives a low-power x86 laptop target with AVX2 and no assumption of a discrete GPU.
- Platform-native peak accounting avoids pretending that iOS physical footprint, Android RSS/PSS, and Linux cgroup usage are one interchangeable raw quantity.
- Recording both absolute peak and baseline delta makes hidden host/wrapper overhead visible without allowing baseline subtraction to turn an oversized process footprint into an artificially favorable result.
- A universal `2 GiB` hard Core ceiling prevents high-memory targets from masking a backbone that is unsuitable for the 4-GB mass-reach promise.
- Keeping the 16K stress tier separate avoids turning long-context stress evidence into a hidden second Core memory gate while still failing closed on OOM/OS termination.

If a commandMed build eventually qualifies across this set, the release story is much stronger than “runs on our flagship phone.” It still must not be marketed as universal compatibility without broader evidence.

## 8. Sources

Device-target sources:

- https://www.macrumors.com/2025/09/09/iphone-17-pro-iphone-air-ram-amounts/
- https://www.macrumors.com/2021/09/15/how-much-ram-in-iphone-13/
- https://www.samsung.com/ae/smartphones/galaxy-a/galaxy-a56-5g-awesome-olive-256gb-sm-a566bzgwmea/
- https://www.samsung.com/ae/smartphones/galaxy-a/galaxy-a16-5g-blue-black-128gb-sm-a166ezkdmea/
- https://www.intel.com/content/www/us/en/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/specifications.html

Memory-measurement primary documentation:

- https://developer.apple.com/documentation/Xcode/gathering-information-about-memory-use
- https://developer.android.com/reference/android/os/Debug.MemoryInfo
- https://developer.android.com/topic/performance/memory-overview
- https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html

## 9. Authority boundary

```text
DEVICE_SET_FROZEN=YES_MASS_REACH_FIVE_TARGET_SET
MEMORY_MEASUREMENT_POLICY_STATUS=FOUNDER_ACCEPTED_FROZEN_CLARIFICATION
CORE_8K_MEMORY_GATE_STATUS=FOUNDER_ACCEPTED_FROZEN_CLARIFICATION
CLARIFICATION_SESSION_4_QUESTION_2=ACCEPTED
CLARIFICATION_SESSION_4_QUESTION_3=ACCEPTED
CORE_8K_PEAK_MEMORY_HARD_CEILING=2_GiB
STRESS_16K_ABSOLUTE_RAM_HARD_CEILING=NOT_FROZEN
DEVICE_EXECUTION_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
BENCHMARK_PAYLOAD_EXECUTION_AUTHORITY=NONE
PLAN_AUTHORITY=NONE
NEXT_LIFECYCLE_STEP=CLARIFY
```
