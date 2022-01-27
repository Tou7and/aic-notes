# Phoneme Recognition
Convert Wave to units in the phoneme level.

What can a PR model do?
- A good PR model can work with forced alignment tasks to help detecting and correcting the errors.
  - [forced-alignments: commonly used for FST-based ASR training](https://isip.piconepress.com/projects/speech/software/tutorials/production/fundamentals/v1.0/section_04/s04_04_p01.html)


# From Phoneme Recognition to Speech Recognition
Maybe a well-trained PR model and corresponding P2G model(s) can also work as a good ASR model.

## Non-autoregressive Mandarin-English Code-switching Speech Recognition with Pinyin Mask-CTC and Word Embedding Regularization
> Shun-Po Chuang, Heng-Jui Chang, Sung-Feng Huang, Hung-yi Lee
> College of Electrical Engineering and Computer Science, National Taiwan University
- [ArXiv](https://arxiv.org/pdf/2104.02258.pdf)


## [Simple and Effective Zero-shot Cross-lingual Phoneme Recognition](https://arxiv.org/abs/2109.11680)
- wav2vec2-lv-60-espeak: [checkpoint on HuggingHub](https://huggingface.co/facebook/wav2vec2-lv-60-espeak-cv-ft)
- [wav2vec2phoneme introduction](https://huggingface.co/docs/transformers/model_doc/wav2vec2_phoneme)

- Data:
  - CommonVoice (42 languages)
  - BABEL (19 languages)
  - MLS (six languages)

- Model:
  - pretrained checkpoint wav2vec2-large-lv60
  - fine-tuned on CommonVoice to recognize phonetic labels in multiple languages

- Phoeme Symbols: IPA (International Phonetic Alphabet)

- Tools for phoneme processing
  - [Phonetisaurus: scripts for training grapheme-to-phoneme models for ASR using the OpenFst](https://github.com/AdolfVonKleist/Phonetisaurus)
    - Docker image available
  - [LanguageNet: Grapheme-to-Phoneme Transducers](https://github.com/uiuc-sst/g2ps)



### [G2P: Grapheme-to-phoneme transduction for cross-language asr](http://www.camille-g.com/slsp20.pdf)
> M. Hasegawa-Johnson et al., SLSP. Springer, 2020.

- Why IPA
- Training and Testing G2P


# Tools for Syllable Processing
- [xpinyin](https://github.com/lxneng/xpinyin)
  - Python library for pinyin processing
- [Dragon-Mapper](https://github.com/tsroten/dragonmapper)
  - Dragon Mapper is a Python library that provides identification and conversion functions for Chinese text processing.
- [IPA-DICT](https://github.com/open-dict-data/ipa-dict)
  - Monolingual wordlists with pronunciation information in IPA

