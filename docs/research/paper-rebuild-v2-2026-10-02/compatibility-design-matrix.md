# Static 5120-to-4096 conditioning study

Source model: Qwen/Qwen3.8-27B at 1d4bf0f2ff6012fd82039f2fa52739d0dd7c60c0. Image model: Qwen/Qwen-Image-2.1 at d26bb61231c349cf6b7896fa83353113880e1ba3. Model/config identity is distinct from the inspected Diffusers source revision 578c9b2c6636ab2424a0e56186268b83623656b2. Source text was read, not imported or executed. The current source contract is not a verified runtime for the pinned model.

| Contract | Source observation | Target observation | Consequence |
|---|---|---|---|
| Width | Qwen text hidden 5120, vision output 5120 | Qwen-Image condition joint_attention_dim 4096; txt_in expects 4096 | Projection required for this interface, but alignment/quality unproven |
| Sequence | Question/prompt tokens include model-specific visual token expansions | System-prefix tokens dropped; variable valid length, right padding after valid-token extraction | No assumed fixed L or token-wise correspondence; text-only/edit conditions distinct |
| Padding/mask | Encoder input left padding, attention mask, image_grid_thw and modality token type | Embedding right padding; separate image-pad mask and joint causal/padding mask | Rebuild masks from valid tokens; copying source indices may be wrong |
| Normalization | Text RMS norm epsilon 1e-6; final norm/hidden-layer choice matters | Pipeline expects pre-final-RMSNorm decoder state; source hook handles Transformers 5.x capture semantics | Same epsilon does not imply same distribution; pin runtime and selected state |
| Position | Qwen mixed-attention backbone; mrope sections [11,11,10], partial rotation .25, theta 10000000 | DiT rotary axes [16,56,56], condition/image geometry and joint sequence semantics | No copying Qwen position IDs as DiT rotary coordinates |
| Images | Vision patch16, spatial merge2, temporal patch2; out5120 | Ordered image placeholders expanded to latent slots; one vision token to four latent slots in inspected source | Grid/slot ordering and condition-image packing are independent obligations |
| Pixel/latent | Qwen vision input receives RGB condition after alpha-white compositing | Image21 VAE retains RGBA; 64 latent channels, spatial compression16 | No discarding alpha from latent route or treating pixels as diagnostic truth |
| Causal condition/cache | Source mixed full/linear cache representation | Condition prefix modulation t=0 and caching only valid prefix states | Prefix cache, negative conditions and editing layout require runtime identity checks |
| Projection | Input B,L,5120 | Output B,L-prime,4096 | Affine projection is a necessary shape bridge; no guarantee of semantic transport |

An affine 5120-to-4096 bridge with bias has 20,975,616 parameters by arithmetic. Rank-nullity gives a null space of dimension at least 1024 for a linear map; it cannot be injective over all of R^5120. That does not show that task-relevant conditioning needs all 5120 dimensions. A linear map may be sufficient on an appropriate low-dimensional subspace/manifold; no static proof establishes that this representation occupies one. No bridge can recover information absent from the source state.

| Bridge | Conditional adequacy | Failure discriminator |
|---|---|---|
| Linear affine | Cheapest shape-aligned baseline; sequence/grid semantics separately resolved | Frozen-generator condition matching and downstream quality |
| MLP | Can model nonlinear channel alignment; same sequence | Must exceed capacity-matched linear control, account for added parameters |
| Cross-attention/resampler | Can alter L and attend to source structure | Control latent count, compute, masks and positional geometry |
| Q-Former-like query bridge | Learned query bottleneck with flexible alignment | Query/task capacity may explain gain; compare same-budget resampler |

Static evidence establishes interface obligations, not necessity of an MLP, resampler or Q-Former. First later experiment should preserve DiT/VAE and compare original encoder conditions against projected source conditions with text-only and editing contracts separately. Runtime probes, licensed images and clinical-validity evaluation remain deferred. Diffusers Apache-2.0 software does not waive Qwen-Image's research-only model terms. A resource claim requires measured duplicated-encoder removal minus added bridge/runtime costs, not a rounded donor parameter label.

Inspected public source: https://github.com/huggingface/diffusers/blob/578c9b2c6636ab2424a0e56186268b83623656b2/src/diffusers/pipelines/qwenimage21/pipeline_qwenimage21.py (encoding, approximately lines 207–331); https://github.com/huggingface/diffusers/blob/578c9b2c6636ab2424a0e56186268b83623656b2/src/diffusers/models/transformers/transformer_qwenimage21.py (conditioning/masks, approximately lines 893–970). Hashes and retrieval times are recorded in source-retrieval-manifest.json. Line references are source-snapshot coordinates, not claimed version-equivalence tests.
