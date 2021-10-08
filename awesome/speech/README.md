# ASR
Automatic Speech Recognition


# Frameworks

[SpeechBrain](https://github.com/speechbrain/speechbrain)
- Release: April, 2021

[meta transfer learning](https://github.com/audioku/meta-transfer-learning)
- meta training
- joint training
- transfer training 


# Papers 

## FST based ASR

[Povey, Daniel, et al. "The Kaldi speech recognition toolkit." IEEE 2011 workshop on automatic speech recognition and understanding. No. CONF. IEEE Signal Processing Society, 2011.](https://infoscience.epfl.ch/record/192584/files/Povey_ASRU2011_2011.pdf)
2011, Utilize OpenFST, HCLG decoding grpah


## End-to-End ASR

[Graves, Alex, and Navdeep Jaitly. "Towards end-to-end speech recognition with recurrent neural networks." International conference on machine learning. PMLR, 2014.](http://proceedings.mlr.press/v32/graves14.pdf)
2014, ASR without requiring an intermediate phonetic representation

[Chorowski, Jan, et al. "End-to-end continuous speech recognition using attention-based recurrent NN: First results." arXiv preprint arXiv:1412.1602 (2014).](https://arxiv.org/pdf/1412.1602)
2014, The alignment between the input and output sequences is established using an attention mechanism

[Chan, W., Jaitly, N., Le, Q., & Vinyals, O. (2016, March). Listen, attend and spell: A neural network for large vocabulary conversational speech recognition. In 2016 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 4960-4964). IEEE.](https://research.google/pubs/pub44926.pdf)
2016, The LAS structure proposed by Google Brain

[Watanabe, Shinji, et al. "Hybrid CTC/attention architecture for end-to-end speech recognition." IEEE Journal of Selected Topics in Signal Processing 11.8 (2017): 1240-1253.](https://www.merl.com/publications/docs/TR2017-190.pdf)
2017, 三菱電器研究實驗室, espnet

[Dong, Linhao, Shuang Xu, and Bo Xu. "Speech-transformer: a no-recurrence sequence-to-sequence model for speech recognition." 2018 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2018.](https://ieeexplore.ieee.org/abstract/document/8462506/)
2018, Transformer for speech recognition

[Sainath, T. N., Pang, R., Rybach, D., He, Y., Prabhavalkar, R., Li, W., ... & Chiu, C. C. (2019). Two-pass end-to-end speech recognition. arXiv preprint arXiv:1908.10992.](https://arxiv.org/pdf/1908.10992.pdf)
2019, Transducer ASR: the RNN-T model produces streaming predictions and the LAS decoder finalizes the prediction during inference

[Zhang, Qian, et al. "Transformer transducer: A streamable speech recognition model with transformer encoders and rnn-t loss." ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP). IEEE, 2020.](https://arxiv.org/pdf/2002.02562)
2020, Similar to RNN-T but use Transformer encoder instead of RNN 

[Conformer: Convolution-augmented Transformer for Speech Recognition](https://arxiv.org/abs/2005.08100)
convolution-augmented transformer for speech recognition, 2020, Google

[On the Comparison of Popular End-to-End Models for Large Scale Speech Recognition](https://www.isca-speech.org/archive/Interspeech_2020/pdfs/2846.pdf)
2020, Benmarks of E2E ASR Models

[Transformer Transducer: A Streamable Speech Recognition Model with Transformer Encoders and RNN-T Loss](https://arxiv.org/abs/2002.02562)
2020, Google.

[SpeechBrain: A General-Purpose Speech Toolkit](https://arxiv.org/pdf/2106.04624.pdf)
2021, Mirco Ravanelli, Titouan Parcollet, Yoshua Bengio


## Medical ASR

[speech recognition for medical conversation](https://arxiv.org/pdf/1711.07274.pdf)
ASR Systems for transcribing doctor-patient conversations, 2018, Google
- CTC: WER 20.1%
- LAS: WER 18.3%
- Trained on 14,000 hours of medical conversation
- Dataset split by speakers, no doctor overlap, male:female = 1:1

[Assessing the accuracy of automatic speech recognition for psychotherapy](https://www.nature.com/articles/s41746-020-0285-8#Sec7)
2020, Nature, Google ASR, Li Fei-Fei & Nigam H. Shah
- 針對輔助心理治療的語音技術進行評估(use Google ASR)
- For clinician-identified harm-related sentences, the word error rate was 34%
- Domain Agnostic Metric: WER
- Clinically-relevant Metric: [F1, Precision, Recall on PHQ9](https://www.nature.com/articles/s41746-020-0285-8/tables/3)
- Detail about corpus: [corpus creation process, annotation protocols](https://static-content.springer.com/esm/art%3A10.1038%2Fs41746-020-0285-8/MediaObjects/41746_2020_285_MOESM1_ESM.pdf)

[Design and Implementation of Cyrillic Mongolian Speech Input System for Thyroid Ultrasound Report](https://iopscience.iop.org/article/10.1088/1757-899X/768/7/072008/pdf)
- 語音超音波報告
- Speech input system: 自動載入病人資料及接收醫生語音輸入
- Cyrillic Mongolian Speech Recognition System: 蒙古 ASR
- Thyriod ultrasound reporting: 報告產生系統並含有載入相關病患資料以及歷史報告的功能
- CNN baseline / Dropout / Maxout

[Medical Speech Recognition:Reaching Parity with Humans](https://link.springer.com/chapter/10.1007/978-3-319-66429-3_51)
2017, SPECOM
- 270 小時的醫學語音數據+臨床事件文本
- WER ~ 16%

[A systematic comparison of contemporary automatic speech recognition engines for conversational clinical speech](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6371385/)
2018 AMIA Annu Symp Proc
- 臨床會話語音的系統 Benchmark
- 無腳本臨床場景錄製
- WER / Precision / Recall / F1


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


## Syllable Based Methods

[Syllable-Based Sequence-to-Sequence Speech Recognition with the Transformer in Mandarin Chinese](https://arxiv.org/pdf/1804.10752.pdf)
2018, 中文拼音, Transformer.

[Cascade rnn-transducer: Syllable based streaming on-device mandarin speech recognition with a syllable-to-character converter](https://arxiv.org/pdf/2011.08469.pdf)
2020, 中文拼音, Transducer
- A rich text repository can be easily used to strengthen the language model ability

[Syllable-Based Acoustic Modeling with CTC for Multi-Scenarios Mandarin speech recognition](https://ieeexplore.ieee.org/abstract/document/8489589)
2018, 中文拼音, CTC
- Syllables in the Chinese language have its inherent advantages, as its number is fixed (effective generalization, better robustness)


## Corpus

[SEAME on LDC](https://catalog.ldc.upenn.edu/LDC2015S04)
code switching 語料: 馬來西亞中文+英文

[Formosa Speech in the Wild Corpus for Improving Taiwanese Mandarin Speech-Enabled Human-Computer Interaction](https://link.springer.com/article/10.1007%2Fs11265-019-01483-4)
台灣中文語料庫
- Radio speech provided by Taiwan’s National Education Radio
- Datasets split by programs: [Table 3](https://link.springer.com/article/10.1007/s11265-019-01483-4/tables/3)
- Baseline: Kaldi
- The evaluation results revealed that the best Taiwanese-specific MSR system achieved an 8.1% Chinese character error rate (CER). As reference, the performances of iFlyTek’s (ISCSLP 2018) and Google’s (2018) commercial MSR systems which were not optimized for this task were 18.8% and 20.6% CERs, respectively.

[Common Voice](https://commonvoice.mozilla.org/zh-TW)
Powerd by Mozilla

