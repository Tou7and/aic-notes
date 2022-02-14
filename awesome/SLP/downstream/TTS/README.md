# Text to Speech
Some documents and tools for speech synthesis.


# WaveNet
[WaveNet: A Generative Model for Raw Audio](https://arxiv.org/abs/1609.03499)
> [Submitted on 12 Sep 2016 (v1), last revised 19 Sep 2016 (this version, v2)]

[NVIDIA/nv-wavenet](https://github.com/NVIDIA/nv-wavenet/)
- nv-wavenet is a CUDA reference implementation of autoregressive WaveNet inference.
- implements the WaveNet variant described by Deep Voice. 
- only implements the autoregressive portion of the network; conditioning vectors must be provided externally. 
- More details: [NVIDIA Developer Blog](https://devblogs.nvidia.com/nv-wavenet-gpu-speech-synthesis/)


# Tacotron 2
[NATURAL TTS SYNTHESIS BY CONDITIONING WAVENET ON MEL SPECTROGRAM PREDICTIONS](https://arxiv.org/pdf/1712.05884.pdf)
2018, Google, Tacotron2
- Use [MOS](https://en.wikipedia.org/wiki/Mean_opinion_score) for quality estimates


# VoiceLoop
[VOICELOOP: VOICE FITTING AND SYNTHESIS VIA A PHONOLOGICAL LOOP](https://arxiv.org/pdf/1707.06588.pdf)
2018, ICLR, Facebook AI
- Features
  - unconstrained voice samples OK
  - alignment Free
  - multi-speaker TTS
- Prev Works
  - rule-based
  - concatentive
  - statistical-parametric
  - neural
    - Deep Voice System (DV1, DV2, ...)
    - WaveNet
    - Char2Wav
    - Tacotron: encoder-decoder architecture

