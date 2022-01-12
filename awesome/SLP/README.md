# SLP: Speech and Language Processing
> Input = Speech waveforms(?)


# Self-supervised Learning Paradigm
1. Pretraining with unlabel data (upstream representations) 
2. Fine-tuning with labeled data (downstream tasks)

## [SUPERB: Speech processing Universal PERformance Benchmark](https://arxiv.org/pdf/2105.01051.pdf)
> Yang, Shu-wen, et al. "SUPERB: Speech processing Universal PERformance Benchmark." arXiv preprint arXiv:2105.01051 (2021).
> [SUPERB official site](https://superbbenchmark.org/)

Key Features
- SUPERB is a leaderboard to benchmark the performance of a shared model across a wide range of speech processing tasks with minimal architecture changes and labeled data
- Propose a simple framework to solve all SUPERB tasks (source code: [S3PRL](https://github.com/s3prl/s3prl))

Methods
- 將 SSL 的學習方法(Upstream Techniques)分為三種: Generative Modeling, Discriminative Modeling, Multi-task Learning
- 執行十個下游任務(Downstream Tasks)來製作計分板，分別是: ASR, PR, KS, QbE, IC, SF, SID, SV, SD, ER ([SUPERB/tasks](https://superbbenchmark.org/tasks))
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

Go to upstream and downstream for more.


# Unsupervised Learning

## [(SeqRQ-AE](https://arxiv.org/pdf/1910.12729.pdf)
> Liu, A. H., Tu, T., Lee, H. Y., & Lee, L. S. (2020, May). 
> Towards unsupervised speech recognition and synthesis with quantized speech representation learning. 
> In ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 7259-7263). IEEE.

Sequential Representation Quantization AutoEncoder (SeqRQ-AE)
- Learn from primarily unpaired audio data and produce sequences of representations very close to phoneme sequences of speech utterances
- The proposed framework is trained in an end-to-end manner without pre-training or fine-tuning.

Multiple Loss
- The reconstruction loss of unpaired speech 
- The CTC loss for the phoneme sequence pair 
- The TTS loss for the target sequence pair

