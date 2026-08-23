# Spec 005 — Mass-Reach Device Target Research

**Lifecycle:** CLARIFY ONLY
**Evidence capture date:** 2026-08-23
**Canonical commandMed base:** `19aa95bbd122f3e01421ba2618dc1efe2f088289`

> Read-only device-target research. No model was run on any device and no performance claim is made. The device set in this document is a recommendation until explicitly accepted and integrated into the Spec 005 clarification contract.

## 1. Why the existing two-tier wording is insufficient by itself

Founder decision `FD-002=FLAGSHIP_PLUS_MODERN_MIDRANGE` remains canonical, but the later `UNIVERSAL_LOW_RESOURCE_DISTRIBUTION_PRIORITY` requires evidence that reaches beyond a current flagship and one comfortable midrange phone.

A model intended for mass installation should be tested against:

1. current flagship capability;
2. an older low-memory iPhone still representative of the installed base;
3. modern Android midrange hardware;
4. explicit 4-GB-class Android hardware;
5. a weak ordinary x86 laptop envelope.

The purpose is not to claim universal compatibility from five devices. The purpose is to anchor reproducible lower/upper resource boundaries instead of inferring deployability from parameter count.

## 2. Recommended named-device/resource set

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

Recommended exact memory SKU:

```text
ROLE=MODERN_MIDRANGE_ANDROID_REPRESENTATIVE
DEVICE=Samsung Galaxy A56 5G
RAM=8_GB
STORAGE=128_OR_256_GB_SKU
PLATFORM=Android
```

Samsung Gulf's official product specifications report 8 GB memory for the inspected A56 5G SKUs.

### D. Low-resource Android — Samsung Galaxy A16 5G

Recommended exact memory SKU:

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

Intel's official specification lists the N100 as a 4-core/4-thread 6 W mobile processor with up to 3.40 GHz and AVX2 support. An 8 GB memory envelope is intentionally below the processor's supported 16 GB maximum and represents inexpensive ordinary laptops/min PCs rather than a developer workstation.

A specific retail laptop SKU can be bound later if physical-device execution requires one. For deterministic planning, the CPU/RAM/OS envelope is the more important invariant.

## 3. Recommended clarification policy

```text
DEVICE_EVIDENCE_POLICY=MASS_REACH_FIVE_TARGET_SET
FLAGSHIP_REPRESENTATIVE=Apple_iPhone_17_Pro_12GB
APPLE_LOW_RESOURCE_REPRESENTATIVE=Apple_iPhone_13_4GB
MODERN_MIDRANGE_ANDROID_REPRESENTATIVE=Samsung_Galaxy_A56_5G_8GB
LOW_RESOURCE_ANDROID_REPRESENTATIVE=Samsung_Galaxy_A16_5G_4GB
LOW_RESOURCE_LAPTOP_ENVELOPE=Intel_N100_8GB_x86_64
```

All five targets should eventually use the same canonical GGUF model identity wherever technically possible. Platform wrappers may differ, but wrapper/runtime differences must be exact and cannot silently change the evaluated model artifact.

## 4. What acceptance would and would not freeze

Acceptance of the five-target set would freeze **which resource targets must be represented**, not performance thresholds.

Still unresolved after acceptance:

- exact OS/build versions;
- exact llama.cpp revision;
- exact wrapper/application used on iOS and Android;
- context/KV condition;
- TTFT/prefill/decode/sustained-throughput thresholds;
- peak-RAM hard threshold beyond current engineering target;
- battery/energy and thermal measurement protocol;
- repetition/warm-up/aggregation methodology;
- whether a failure on each target is a hard disqualification versus separately scoped compatibility claim.

Those must be frozen before execution and never chosen after observing candidate results.

## 5. Why this set is preferable to flagship-only evidence

- iPhone 17 Pro proves current Apple performance potential but has 12 GB RAM and is too forgiving to serve as a mass-reach lower bound.
- iPhone 13 gives a 4 GB Apple constraint and a substantially older SoC generation.
- Galaxy A56 gives a current mainstream Android midrange anchor.
- Galaxy A16 5G gives a named 4 GB Android constraint.
- Intel N100 + 8 GB gives a low-power x86 laptop target with AVX2 and no assumption of a discrete GPU.

If a commandMed build is usable across this set, the release story is much stronger than “runs on our flagship phone.” It still must not be marketed as universal compatibility without broader evidence.

## 6. Sources

- https://www.macrumors.com/2025/09/09/iphone-17-pro-iphone-air-ram-amounts/
- https://www.macrumors.com/2021/09/15/how-much-ram-in-iphone-13/
- https://www.samsung.com/ae/smartphones/galaxy-a/galaxy-a56-5g-awesome-olive-256gb-sm-a566bzgwmea/
- https://www.samsung.com/ae/smartphones/galaxy-a/galaxy-a16-5g-blue-black-128gb-sm-a166ezkdmea/
- https://www.intel.com/content/www/us/en/products/sku/231803/intel-processor-n100-6m-cache-up-to-3-40-ghz/specifications.html

## 7. Authority boundary

```text
DEVICE_SET_FROZEN=NO_PENDING_FOUNDER_CLARIFICATION
DEVICE_EXECUTION_AUTHORITY=NONE
MODEL_EXECUTION_AUTHORITY=NONE
MODEL_WEIGHT_ACCESS_AUTHORITY=NONE
MODEL_CONVERSION_AUTHORITY=NONE
PLAN_AUTHORITY=NONE
NEXT_LIFECYCLE_STEP=CLARIFY
```
