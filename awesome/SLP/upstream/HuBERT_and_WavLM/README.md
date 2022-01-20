# [UniSpeech-SAT](Universal Speech Representation Learning with Speaker Aware Pre-Training)
- [microsoft/UniSpeech](https://github.com/microsoft/UniSpeech)
- [HugglingFace: Unispeech-SAT](https://huggingface.co/transformers/model_doc/unispeech_sat.html)
- powerful performance on various speaker related benchmarks


# [HuBert](https://arxiv.org/abs/2106.07447)
> HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units
> Hsu et al., 2021a
- [Hubert on HugglingFace](https://huggingface.co/transformers/model_doc/hubert.html)

HuBert: DeepCluster + wav2vec2.0 + BERT
- Hidden Units
  - DeepCluster approach: iteratively learns the features and groups them
- Representation Learning via Masked Prediction
  - use wav2vec 2.0 techiques for mask generation (BERT-like prediction loss)


Number of parameters & data:
- HuBERT Base = 94.68M, trained on LS 960 hr
- HuBERT Large = 316.61M, trained on LL 60k hr

# [WavLM: Large-Scale Self-Supervised Pre-Training for Full Stack Speech Processing](https://arxiv.org/pdf/2110.13900.pdf)
WavLM is built based on the HuBERT framework, with an emphasis on both spoken content modeling and speaker identity preservation to improve model robustness to complex acoustic environments and the preservation of speaker identity.

Key Features
- Denoising Masked Speech Modeling (utterance mixing)
- Optimize Model Structure (gate relative position)
- Add Training Data (60k → 94k)


Number of parameters:
- Base / Base+:  94.70M
- Large: 316.62M

