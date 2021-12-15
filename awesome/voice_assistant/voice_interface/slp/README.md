# SLP: Speech and Language Processing
> Input = Speech waveforms(?)

# [SUPERB: Speech processing Universal PERformance Benchmark](https://arxiv.org/pdf/2105.01051.pdf)
> Yang, Shu-wen, et al. "SUPERB: Speech processing Universal PERformance Benchmark." arXiv preprint arXiv:2105.01051 (2021).
> [SUPERB official site](https://superbbenchmark.org/)
- SUPERB is a leaderboard to benchmark the performance of a shared model across a wide range of speech processing tasks with minimal architecture changes and labeled data
- Propose a simple framework to solve all SUPERB tasks (source code: [S3PRL](https://github.com/s3prl/s3prl))
- 將 SSL 的學習方法(Upstream Techniques)分為三種: Generative Modeling, Discriminative Modeling, Multi-task Learning
- 會執行十個下游任務(Downstream Tasks)，分別是: ASR, PR, KS, QbE, IC, SF, SID, SV, SD, ER ([SUPERB/tasks](https://superbbenchmark.org/tasks))
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



