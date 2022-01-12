# ASR
Automatic Speech Recognition

# Frameworks
Tools for building ASR systems

## Kaldi
- Build on top of OpenFST
- HMM-GMM
- HMM-DNN

## ESPNET
- [espnet/espnet](https://github.com/espnet/espnet)
- [THE 2020 ESPNET UPDATE](https://arxiv.org/pdf/2012.13006.pdf)
  - Broadened applications: from ASR to TTS, VC, ST(translation), SE(enhancement).
  - Many neural architectures and learning methods: Transformer, conformer, RNN-T, ...


## NeMo
- Nividia

## FairSeq
- Facebook

## SpeechBrain
- [Github/SpeechBrain](https://github.com/speechbrain/speechbrain)
  - Release: April, 2021
- [SpeechBrain: A General-Purpose Speech Toolkit](https://arxiv.org/pdf/2106.04624.pdf)
  - 2021, Mirco Ravanelli, Titouan Parcollet, Yoshua Bengio

## Meta Transfer Learning
[meta transfer learning](https://github.com/audioku/meta-transfer-learning)
- meta training
- joint training
- transfer training 

# FST based ASR
Common approaches: use Kaldi

[Povey, Daniel, et al. "The Kaldi speech recognition toolkit." IEEE 2011 workshop on automatic speech recognition and understanding. No. CONF. IEEE Signal Processing Society, 2011.](https://infoscience.epfl.ch/record/192584/files/Povey_ASRU2011_2011.pdf)
2011, Utilize OpenFST, HCLG decoding grpah

# End-to-End ASR
Common approaches: 
- CTC
- Attention Models
  - LAS
  - Transformers
- Transducers

[On the Comparison of Popular End-to-End Models for Large Scale Speech Recognition](https://www.isca-speech.org/archive/Interspeech_2020/pdfs/2846.pdf)
2020, Benmarks of E2E ASR Models


## CTC
[Graves, Alex, and Navdeep Jaitly. "Towards end-to-end speech recognition with recurrent neural networks." International conference on machine learning. PMLR, 2014.](http://proceedings.mlr.press/v32/graves14.pdf)
2014, ASR without requiring an intermediate phonetic representation

## Attention Models
[Chorowski, Jan, et al. "End-to-end continuous speech recognition using attention-based recurrent NN: First results." arXiv preprint arXiv:1412.1602 (2014).](https://arxiv.org/pdf/1412.1602)
2014, The alignment between the input and output sequences is established using an attention mechanism

[Chan, W., Jaitly, N., Le, Q., & Vinyals, O. (2016, March). Listen, attend and spell: A neural network for large vocabulary conversational speech recognition. In 2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 4960-4964). IEEE.](https://research.google/pubs/pub44926.pdf)
2016, The LAS structure proposed by Google Brain

## CTC + Attention
[Watanabe, Shinji, et al. "Hybrid CTC/attention architecture for end-to-end speech recognition." IEEE Journal of Selected Topics in Signal Processing 11.8 (2017): 1240-1253.](https://www.merl.com/publications/docs/TR2017-190.pdf)
2017, 三菱電器研究實驗室, espnet

## Transformers
[Dong, Linhao, Shuang Xu, and Bo Xu. "Speech-transformer: a no-recurrence sequence-to-sequence model for speech recognition." 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2018.](https://ieeexplore.ieee.org/abstract/document/8462506/)
2018, Transformer for speech recognition

[Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100)
convolution-augmented transformer for speech recognition, 2020, Google


## Transducers
End-to-end network architecture for streaming ASR.

The architecture basically consists of a Audio Encoder, a Label Encoder, and a Joint Network.

See transducer for more.

## Multi-lingual / Code-Switching

[Multilingual Speech Recognition With A Single End-To-End Model](https://arxiv.org/pdf/1711.01694.pdf)
2017, Toyota, Google.

[Metrics for Modeling Code-Switching Across Corpora](https://www.researchgate.net/profile/Jacqueline-Serigos-2/publication/319185267_Metrics_for_Modeling_Code-Switching_Across_Corpora/links/5e1cc794a6fdcc283771144c/Metrics-for-Modeling-Code-Switching-Across-Corpora.pdf)
Language Entropy, M-index, I-index, 2017.

[Zhou, S., Xu, S., & Xu, B. (2018). Multilingual end-to-end speech recognition with a single transformer on low-resource languages. arXiv preprint arXiv:1806.05059.](https://arxiv.org/pdf/1806.05059.pdf)
2018, transformer for code-switching
- by any means / 八月零零 / バアエリミン
- 在 training 時加入 language symbol

[Sitaram, Sunayana, et al. "A survey of code-switched speech and language processing." arXiv preprint arXiv:1904.00784 (2019).](https://arxiv.org/pdf/1904.00784.pdf)
2019, metrics for measuring the amount of code-switching, code-switching ASR methods, ...

[Li, Ke, et al. "Towards code-switching ASR for end-to-end CTC models." ICASSP 2019-2019 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2019.](https://www.microsoft.com/en-us/research/uploads/prod/2019/09/Towards_code_switched_ASR_for_End_to_End_CTC_models.pdf)
2019, ICASSP
- 先 train 好 ZH 再 fine-tune CS
- CTC may perform better than Transformers for code-switching tasks?

[Meta-transfer learning for code-switched speech recognition](https://arxiv.org/pdf/2004.14228)
2020, MAML, Mandarin/English

[Du, Chenpeng, et al. "Data augmentation for end-to-end code-switching speech recognition." 2021 IEEE Spoken Language Technology Workshop (SLT). IEEE, 2021.](https://arxiv.org/pdf/2011.02160)
2021, Data Augmentation


[Multilingual Training and Cross-lingual Adaptation on CTC-based Acoustic Model](https://arxiv.org/pdf/1711.10025.pdf)



## Syllable Based Methods

[Syllable-Based Sequence-to-Sequence Speech Recognition with the Transformer in Mandarin Chinese](https://arxiv.org/pdf/1804.10752.pdf)
2018, 中文拼音, Transformer.

[Cascade rnn-transducer: Syllable based streaming on-device mandarin speech recognition with a syllable-to-character converter](https://arxiv.org/pdf/2011.08469.pdf)
2020, 中文拼音, Transducer
- A rich text repository can be easily used to strengthen the language model ability

[Syllable-Based Acoustic Modeling with CTC for Multi-Scenarios Mandarin speech recognition](https://ieeexplore.ieee.org/abstract/document/8489589)
2018, 中文拼音, CTC
- Syllables in the Chinese language have its inherent advantages, as its number is fixed (effective generalization, better robustness)


## Blogs

[An All-Neural On-Device Speech Recognizer](https://ai.googleblog.com/2019/03/an-all-neural-on-device-speech.html)
- RNN-T
- real-time
- parallel implementation
- decoder ~= a Finite State Transducer (FST)
- all-neural, on-device Gboard speech recognizer on all Pixel phones (American English only)

[Sequence-to-sequence learning with Transducers](https://lorenlugosch.github.io/posts/2020/11/transducer/)
- Encoder, Predictor and Joiner
- one may recognize that the Transducer graph is a weighted FST
  - an alignment forms the input labels
  - y forms the output labels
  - and the weight for each edge is dynamically generated by the joiner network

