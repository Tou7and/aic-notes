# Alzheimer: what causes Alzheimer Dementia? 

## Microbes Hypothesis
- [微生物感染：阿茲海默症的可能病因帶來新的治療希望](https://www.bbc.com/zhongwen/trad/science-59093440)
- [What if dormant microbes trigger the onset of Alzheimer's?](https://www.bbc.com/future/article/20211006-what-if-dormant-microbes-trigger-alzheimers)

# Detecting Alzheimer via Speech
Is it possible to early detect Alzheimer Dementia by analysing the speech of the people?
- [Linguistic markers predict onset of Alzheimer's disease](https://www.thelancet.com/action/showPdf?pii=S2589-5370%2820%2930327-8)
- [人工智能成預測失智症能手](https://www.bbc.com/zhongwen/trad/science-54663725)

## [Dementia and language](https://www.alzheimers.org.uk/about-dementia/symptoms-and-diagnosis/symptoms/dementia-and-language)
- How can dementia affect a person's communications?
  1. not able to find the right words
    - use a related word (for example, ‘book’ instead of ‘newspaper’)
    - use substitutes for words (for example, ‘thing that you sit on’ instead of ‘chair’)
    - use words that have no meaning
  2. not able to use the second languages
    - go back to the first language they learned
  3. have problems understanding what others said
    - not able to keep focused
    - thinking more slowly
- [Dementia and the brain](https://www.alzheimers.org.uk/about-dementia/symptoms-and-diagnosis/how-dementia-progresses/brain-dementia)

## Papers of Alzheimer and Speech

### [Alzheimer's disease and automatic speech analysis: a review](https://www.sciencedirect.com/science/article/pii/S0957417420300397)
- Pulido, M. L. B., Hernández, J. B. A., Ballester, M. Á. F., González, C. M. T., Mekyska, J., & Smékal, Z. (2020). Alzheimer's disease and automatic speech analysis: a review. Expert systems with applications, 150, 113213.
- Language problems are considered one of the most characteristic symptoms of AD
- Primary progressive aphasia (PPA)
- Linguistic tests
  - People with AD have more difficulties in these tests
  - Patterns: repeat the same ideas / less informative / simpler language structures / longer and empty pauses / monotonous prosody
  - Skills for evaluation: identification / comprehension / repetition / reading / Spontaneous Speech (SS)
- Alzheimer’s disease and voice processing
  - The techniques for analysis are very closed to speech emotion recognition
- Conclusion
  - Using ML algorithms to classify linguistic biomarkers through the verbal statements will facilitate the clinical diagnosis of AD
  - There is a need to train the evolving control models on larger data sets


# [The ADReSSo Challenge](http://www.homepages.ed.ac.uk/sluzfil/ADReSSo-2021/#baseline)
Alzheimer's Dementia Recognition through Spontaneous Speech

## Papers of ADReSS

### [Alzheimer’s Dementia Recognition through Spontaneous Speech: The ADReSS Challenge](https://arxiv.org/pdf/2004.06833.pdf)
- INTERSPEECH 2020

### [Detecting cognitive decline using speech only: The ADReSSo Challenge](http://www.homepages.ed.ac.uk/sluzfil/ADReSSo-2021/LuzEtAl21ADReSSo.pdf)
- Baseline Classification and regression Results

### [Tackling the ADReSS challenge: a multimodal approach to the automated recognition of Alzheimer’s dementia](http://www.interspeech2020.org/uploadfile/pdf/Wed-SS-1-6-1.pdf)
- INTERSPEECH 2020
- Dataset
  - recordings and transcripts of Cookie Theft picture descriptions
  - by 78 AD and 78 non-AD participants of the Boston Diagnostic Aphasia Exam
  - gender and age balanced
  - 4,076 normalized speech segments, on average 24.86 per participant
  - train set containing 108 examples and the test set containing 48 examples
- Feature engineering: audio features, TF-IDF features, readability features and embeddings
  - audio features: MFCC, ADR(eGeMAPS), Average duration
  - TF-IDF: Unigram, Bigram, Char4gram, Suffix, POS tag, Grammmatical dependency, Universal dependency
- Learning algorithms
  - Classification: Xgboost, Random forest, SVM, Logistic regression (LogR)
  - Regression: Xgboost, SVM, Random forest and Linear regression (LinR)
- Exploration of feature space and model selection
- Evalutation
  - For classification, accuracy is used for the performance evaluation
  - For regression, root mean square error (RMSE) is used

### [Classifying Alzheimer's Disease Using Audio and Text-Based Representations of Speech](https://www.frontiersin.org/articles/10.3389/fpsyg.2020.624137/full)
- audio features: i-vectors and x-vectors
- text features: word vectors, BERT embeddings, LIWC features, and CLAN features
- model for AD detect: neural networks
- model for MMSE scores: regression models

