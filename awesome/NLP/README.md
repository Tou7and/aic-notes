# Nature Language Processing

- [Summary of NLP Tasks](https://huggingface.co/docs/transformers/task_summary)



# Tools and Frameworks

## [HuggingFace](https://huggingface.co/)
- Build, train and deploy SOTA models powered by the reference open source in machine learning.


# The BERT paradigm

## [BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding](https://arxiv.org/abs/1810.04805)
> Official Github: [google-research/bert](https://github.com/google-research/bert)
> HuggingFace Model Hubs: [bert-base-uncased](https://huggingface.co/bert-base-uncased)

BERT is a transformers model pretrained on a large corpus of English data in a self-supervised fashion. It is pretrained on the raw texts only without human annotations.
- Propose a strong self-trainig and fine-tuning paradigm.


Self-pretrained with two objectives:
1. Masked language modeling (MLM)
  - the objective is to predict the original vocabulary id of the masked word based only on its context.
  - only predict the masked words rather than reconstructing the entire input
  - predict the original token with "cross entropy loss"
2. Next sentence prediction (NSP)
  - choosing the sentences A and B for each pretraining example, 50% of the time B is the actual next sentence that follows A (labeled as IsNext), and 50% of the time it is a random sentence from the corpus (labeled as NotNext).
> The NSP task is closely related to representationlearning objectives used in Jernite et al. (2017) and Logeswaran and Lee (2018).
> The training loss is the sum of the mean masked LM likelihood and the mean next sentence prediction likelihood.



## [AN EFFICIENT FRAMEWORK FOR LEARNING SENTENCE REPRESENTATIONS](https://arxiv.org/pdf/1803.02893.pdf)
> Logeswaran, L., & Lee, H. (2018). 
> An efficient framework for learning sentence representations. 
> arXiv preprint arXiv:1803.02893.

Proposing an objective that operates directly in the space of sentence embeddings:
- the generation objective is replaced by a discriminative approximation where the model attempts to identify the embedding of a correct target sentence given a set of sentence candidates. 
- In this context, we interpret the ‘meaning’ of a sentence as the information in a sentence that allows it to predict and be predictable from the information in context sentences. We name our approach quick thoughts (QT), to mean efficient learning of thought vectors.

Key features:
- We propose a simple and general framework for learning sentence representations efficiently. We train widely used encoder architectures an order of magnitude faster than previous methods, achieving better performance at the same time.
- We establish a new state-of-the-art for unsupervised sentence representation learning methods across several downstream tasks that involve understanding sentence semantics.


