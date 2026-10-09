# V5 S1 free Colab selection - 2026-10-04

The Founder subsequently instructed: "do not buy anything use free, its pro account anf colab says that pro account part of it. figure it out".

This selects the free resources exposed by the signed-in account while the existing Pro entitlement remains unverified. No purchase, upgrade, paid API, external paid resource, or incremental spend is admitted. The earlier existing-Pro authorization remains preserved; it is not evidence that Colab recognizes a paid entitlement.

The observed Colab Resources panel reports `You are not subscribed` and zero compute units. The normal runtime selector exposes a free T4 GPU option and disables premium GPU options. The actual accelerator must still be measured rather than assumed from that selector. This account-state discrepancy is operational evidence, not a scientific result.

Bfloat16 capability must be measured on the actual path. A native-support flag alone is neither sufficient nor necessary to qualify the exact authorized PyTorch bfloat16 path: the initial assigned T4 reports native support false and support including emulation true. Direct bfloat16 tensor operations may be checked without a model, dtype substitution, autocast, or optimizer. A passing primitive check does not qualify the full model. Exact artifact/environment/interface checks and fresh exact-run `PREFLIGHT_PASS` remain mandatory before model load; the model path and resource benchmark must subsequently pass before development execution.

Every other approved protocol boundary remains binding. This selection does not approve a custom emulation implementation, precision fallback, model substitution, favorable-hardware search, or bypass of Colab limits.
