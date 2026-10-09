# Architecture candidates

The primary study tests output and adaptation factors on a retained autoregressive backbone, beginning with the smallest lawfully runnable base. A shared trunk is an experimental design convenience; one checkpoint is not a success criterion.

| Architecture | Scientific use | Required discriminator |
|---|---|---|
| Frozen backbone + LM candidate logits | Minimal readout baseline | Decision NLL, calibration and latency |
| Frozen backbone + fitted typed head | Isolates representation/readout | Same training subset and capacity control |
| Shared trunk + head, joint LM maintenance | Primary factor cell | Proper scoring versus retained LM competence |
| Partially shared trunk / task-specific adapters | Interference mitigation control | Added capacity and compute matched explicitly |
| Adapter fusion / MoE / router-free expert blocks | Prior-art controls if justified | Routing overhead and capacity cannot be hidden |
| Decision-only model | Specialist/resource comparison | No retained generation claim |
| Shared embedding model / separate specialists | Non-unified control | Actual installed bytes, memory and quality |
| Two-stage distillation / teacher-student | Deferred alternative | Teacher derivative rights and extra supervision |
| Latent token / cross-attention bridge | Optional encoder-replacement follow-up | Conditioning semantics and resource frontier |
| Original independent image semantic encoder | Required image reference | No image path in primary factorial study |

Dyad, Chinese-Jev, Visual Jev, Uni-Med and Med-MoE-LoRA define strong neighboring mechanisms [@arxiv260936116; @arxiv260936965; @arxiv260925845; @arxiv240917508; @arxiv260107935]. HCF is deferred because it combines unqualified donor, bridge, image and decision factors before the causal question is resolved. Distillation and arbitrary tensor merging would introduce new confounding and license boundaries; they are not needed for the selected design.
