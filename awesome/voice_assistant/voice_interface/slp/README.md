# SLP: Speech and Language Processing
The term SLP is used in the introduction section of the
[MOCKINGJAY Paper (2020)](https://arxiv.org/pdf/1910.12638.pdf).

# SUPERB: Speech processing Universal PERformance Benchmark
[SUPERB official site](https://superbbenchmark.org/)

[SUPERB official paper](https://arxiv.org/pdf/2105.01051.pdf)

## SUPERB: Downstream Tasks for benchmarking
[SUPERB](https://superbbenchmark.org/tasks) 
- defines 6 domains of speech processing tasks
- use 10 tasks from 4 domains to do the benchmarks
  - ASR: Automatic Speech Recognition
  - PR: Phoneme Recognition
  - KS: Keyword Spotting
  - QbE: Query by Example
  - IC: Intent Classification
  - SF: Slot Filling
  - SID: Speaker Identification
  - SV: Speaker Verification
  - SD: Speaker Diarization
  - ER: Emotion Recognition

## SUPERB: Upstream Techniques for learning good representations (self-supervised learning)
- generative modeling
- discriminative modeling
- multi-task learning


# Papers of self-supervised learning

## [MOCKINGJAY (2020)](https://arxiv.org/pdf/1910.12638.pdf)
- Mockingjay: Unsupervised speech representation learning with deep bidirectional transformer encoders.
- ICASSP 2020, National Taiwan University

## [DECOAR 2.0 (2020)](https://arxiv.org/pdf/2012.06659.pdf)
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

## [TERA (2021)](https://arxiv.org/pdf/2007.06028.pdf)
- Self-Supervised Learning of Transformer Encoder Representation for Speech
- self-supervised pre-training scheme
  - time alteration
  - frequency alteration
  - magnitude alteration

## [HuBert(2021)](https://arxiv.org/abs/2106.07447)
- [Hubert on HugglingFace](https://huggingface.co/transformers/model_doc/hubert.html)

## [UniSpeech-SAT](Universal Speech Representation Learning with Speaker Aware Pre-Training)
- [microsoft/UniSpeech](https://github.com/microsoft/UniSpeech)
- powerful performance on various speaker related benchmarks

## [WavLM: Large-Scale Self-Supervised Pre-Training for Full Stack Speech Processing](https://arxiv.org/pdf/2110.13900.pdf)


