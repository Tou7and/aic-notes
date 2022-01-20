# SLU: Spoken Language Understanding
Can be done in 2 stages (transcribing speech into text -> predicting semantics on transcribed text),

or use end-to-end approaches (raw audio to task outputs).


# Intent Classification
classifies utterances into predefined classes to determine the intent of speakers.


## Dataset
Fluent Speech Commands 
- each utterance is tagged with three intent labels: action, object, and location

## Metrics
ACC


# Slot Filling
predicts a sequence of semantic slot-types from an utterance.

Similar to NER but not exactly same.
- [What is the difference between slot filling in NLU and named entity recognition in NLP?](https://www.reddit.com/r/LanguageTechnology/comments/45g5hr/what_is_the_difference_between_slot_filling_in/)


##  Data
- slot-type example: FromLocation 
- slot-value example: Taipei


## Metrics
- slot-type: F1 score 
- slot value:  CER


