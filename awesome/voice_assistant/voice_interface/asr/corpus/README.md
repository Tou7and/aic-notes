# Corpus for Speech Recognition
Some corpus for speech recognition. 

# Corpus

## Librispeech
[LIBRISPEECH: AN ASR CORPUS BASED ON PUBLIC DOMAIN AUDIO BOOKS](https://www.danielpovey.com/files/2015_icassp_librispeech.pdf)
- Partition: In order to guarantee that there was no speaker overlap between the training, development and test sets, we wanted to ensure that each recording is unambiguously attributable to a single speaker.



## TED-LIUM
[TED-LIUM 3: Twice as Much Data and Corpus Repartition for Experiments on Speaker Adaptation](https://arxiv.org/pdf/1805.04699.pdf)
- Partition: for the development and test datasets we chose only speakers who are not present in the training data set in other talks.


## AISHELL-1
https://arxiv.org/pdf/1709.05522.pdf
The entire corpus includes training, development and test sets, without speaker overlaping. The details are presented in Section 4


## National Education Radio
[Formosa Speech in the Wild Corpus for Improving Taiwanese Mandarin Speech-Enabled Human-Computer Interaction](https://link.springer.com/article/10.1007%2Fs11265-019-01483-4)
2019, 台灣中文語料庫 
- 介紹 NER 資料集的資訊以及 baseline 系統 (Kalid)。
- Radio speech provided by Taiwan’s National Education Radio
- Datasets split by programs: [Table 3](https://link.springer.com/article/10.1007/s11265-019-01483-4/tables/3)
- Baseline: Kaldi
- The evaluation results revealed that the best Taiwanese-specific MSR system achieved an 8.1% Chinese character error rate (CER). As reference, the performances of iFlyTek’s (ISCSLP 2018) and Google’s (2018) commercial MSR systems which were not optimized for this task were 18.8% and 20.6% CERs, respectively.
- Partition: For consistent performance comparison across different systems, the NER-Trs-Vol1 corpus is recommended to be split program-by-program into a training and an evaluation subse (以節目為單位來做訓練/驗證集的分割)
- The evaluation results revealed that the best Taiwanese-specific MSR system achieved an 8.1% Chinese character error rate (CER). As reference, the performances of iFlyTek’s (ISCSLP 2018) and Google’s (2018) commercial MSR systems which were not optimized for this task were 18.8% and 20.6% CERs, respectively

## SEAME
[SEAME on LDC](https://catalog.ldc.upenn.edu/LDC2015S04)
code switching 語料: 馬來西亞中文+英文


## CommonVoice
[CommonVoice - Mozilla](https://commonvoice.mozilla.org/zh-TW)
Powerd by Mozilla


# Questions

## Why speaker partitions?
We normally want a speaker independent ASR system.

And A lot of effort has been done to achieve this.
Related topics:
- speaker independent feature extraction
- speaker normalization
  - VTLN (vocal track normalization)
  - FMLLR
  - ...
 - speaker adaptation

referenc: [Automatic speech recognition and speech variability: A review](https://www.sciencedirect.com/science/article/pii/S0167639307000404#sec1)


