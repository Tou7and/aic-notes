# Alzheimer and Speech

## ADReSS
Alzheimer's Dementia Recognition through Spontaneous Speech

[The ADReSSo Challenge Home Pages](http://www.homepages.ed.ac.uk/sluzfil/ADReSSo-2021/#baseline)

### Papers
[Alzheimer’s Dementia Recognition through Spontaneous Speech: The ADReSS Challenge](https://arxiv.org/pdf/2004.06833.pdf)
- INTERSPEECH 2020

[Detecting cognitive decline using speech only: The ADReSSo Challenge](http://www.homepages.ed.ac.uk/sluzfil/ADReSSo-2021/LuzEtAl21ADReSSo.pdf)
- Baseline Classification and regression Results

[Tackling the ADReSS challenge: a multimodal approach to the automated recognition of Alzheimer’s dementia](http://www.interspeech2020.org/uploadfile/pdf/Wed-SS-1-6-1.pdf)
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


## Papers
[Pulido, M. L. B., Hernández, J. B. A., Ballester, M. Á. F., González, C. M. T., Mekyska, J., & Smékal, Z. (2020). Alzheimer's disease and automatic speech analysis: a review. Expert systems with applications, 150, 113213.](https://www.sciencedirect.com/science/article/pii/S0957417420300397)
2020, review
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


