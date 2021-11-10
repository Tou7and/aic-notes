# SLP: Speech and Language Processing
The term SLP is used in the introduction section of the
[MOCKINGJAY Paper (2020)](https://arxiv.org/pdf/1910.12638.pdf).

## SLP Tasks
[SUPERB](https://superbbenchmark.org/tasks) defines 10 speech processing tasks from 6 domains.
- Recognition
  - ASR: Automatic Speech Recognition
  - PR: Phoneme Recognition
- Detection
  - KS: Keyword Spotting
  - QbE: Query by Example
- Semantics
  - IC: Intent Classification
  - SF: Slot Filling
  - ST: Speech Translation
- Speaker
  - SID: Speaker Identification
  - SV: Speaker Verification
  - SD: Speaker Diarization
- Paralingustics
  - ER: Emotion Recognition
- Generation
  - SE: Speech Enhancement
  - SS: Source Separation

## SSL Techniques
- Constrastive
- Reconstrative
- Quantization

# Papers

## Self-Supervised Learning Frameworks
[MOCKINGJAY (2020)](https://arxiv.org/pdf/1910.12638.pdf)
- Mockingjay: Unsupervised speech representation learning with deep bidirectional transformer encoders.
- ICASSP 2020, National Taiwan University


[DECOAR 2.0 (2020)](https://arxiv.org/pdf/2012.06659.pdf)
- DEep COntextualized Acoustuc Representations with vector quantization
- Amazon AWS AI
- Masked Reconstration with Vector Quantization
- Contribution
  - use Transformer as encoding block instead of LSTM (vanilla DeCoAR)
  - the addition of a vector quantization layer
  - a new objective function that combines masked-based reconstruction loss with VQ diversity loss
- Exp Settings (similar to wav2vec2.0)
  - model dimension = 768
  - the inner dimension in feed forward sublayer = 3072
  - attention heads = 8
  - slice size K = 20
  - G(group) = 2 and V(codebook size) = 320 for the quantization module

[TERA (2021)](https://arxiv.org/pdf/2007.06028.pdf)
- Self-Supervised Learning of Transformer Encoder Representation for Speech
- self-supervised pre-training scheme
  - time alteration
  - frequency alteration
  - magnitude alteration

[HuBert(2021)](https://arxiv.org/abs/2106.07447)
- [Hubert on HugglingFace](https://huggingface.co/transformers/model_doc/hubert.html)

[WavLM]()

