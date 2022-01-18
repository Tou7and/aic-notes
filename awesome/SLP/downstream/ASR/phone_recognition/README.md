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


# [wav2vec2phoneme](https://huggingface.co/docs/transformers/model_doc/wav2vec2_phoneme)

## wav2vec2-lv-60-espeak
- [checkpoint on HuggingHub](https://huggingface.co/facebook/wav2vec2-lv-60-espeak-cv-ft)

### [Simple and Effective Zero-shot Cross-lingual Phoneme Recognition](https://arxiv.org/abs/2109.11680)
- Data:
  - CommonVoice (42 languages)
  - BABEL (19 languages)
  - MLS (six languages)

- Model:
  - pretrained checkpoint wav2vec2-large-lv60
  - fine-tuned on CommonVoice to recognize phonetic labels in multiple languages

- Phoeme Symbols: IPA (International Phonetic Alphabet)

### [G2P: Grapheme-to-phoneme transduction for cross-language asr](http://www.camille-g.com/slsp20.pdf)
> M. Hasegawa-Johnson et al., SLSP. Springer, 2020.

- Why IPA
- Training and Testing G2P
- 


# Tools for Syllable Processing
- [xpinyin](https://github.com/lxneng/xpinyin)
- [Dragon-Mapper](https://github.com/tsroten/dragonmapper)

