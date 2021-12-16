# Upstream Models
Upstream models learn to produce a better representations from the pre-training tasks.

[SuperB](https://arxiv.org/pdf/2105.01051.pdf) categorized SSL models into three learning approaches: 
1. Generative Modeling
  - pretraining with "generative loss"

2. Contrastive Modeling
  - pretraining with "discriminative loss"

3. Multi-task Learning
  - Multiple pretraining objectives are adopted


# Generative Modeling as Main Learning Methods
Models are pretrained with "generative loss" or "rescontruction loss".

## [APC](https://arxiv.org/pdf/1904.03240.pdf)
> Chung, Y.-A., Hsu, W.-N., Tang, H., and Glass, J. 
> An Unsupervised Autoregressive Model for Speech Representation Learning. 
> In Interspeech, pp. 146–150, 2019.
> Massachusetts Institute of Technology (MIT)

- The model is designed to preserve information for a wide range of downstream tasks
- The proposed model does not require any phonetic or word boundary labels, allowing the model to benefit from large quantities of unlabeled data
- Further analysis shows that different levels of speech information are captured by our model at different layers
  - The lower layers tend to be more discriminative for speakers, while the upper layers provide more phonetic content
- Motivated by the recent success in transfer learning from large-scale pre-trained language models (the BERT family)

The autoregressive loss
- Belongs to a large family of selfsupervised loss functions
  - X. Wang and A. Gupta, “Unsupervised learning of visual representations using videos,” in ICCV, 2015.
  - C. Doersch, A. Gupta, and A. Efros, “Unsupervised visual representation learning by context prediction,” in ICCV, 2015.
  - G. Larsson, M. Maire, and G. Shakhnarovich, “Colorization as a proxy task for visual understanding,” in CVPR, 2017.

Difference between CPC and APC (this may also be the difference of generative modeling and contrastive modeling)
- Both CPC and the proposed APCs consider the sequential structures of speech, and predict information about future frames. 
- However, the two models differ significantly in the type of information the corresponding loss function enforces them to capture
- While CPC representations are encouraged to focus on information that is most discriminative between the target and negative frames, 
- APCs have to encode information sufficient for predicting the target frame, and are allowed to only discard information that is common across the train dataset

Model Architecture
- A multi-layer unidirectional LSTM  network with residual connections between two consecutive layers
- The dimensionality of each layer is 512


## [VQ-APC](https://arxiv.org/pdf/2005.08392.pdf)
> Chung, Y.-A., Tang, H., and Glass, J. 
> Vector-quantized autoregressive predictive coding. 
> In Interspeech, pp. 3760–3764, 2020.
> Massachusetts Institute of Technology (MIT)

- Recent studies on VQ for representation learning, mostly motivated by the discrete nature of phonetic units, attempt to show that enforcing the quantization leads to a better representation for acoustic unit discovery [16, 17] and automatic speech recognition [7, 18]. 
- In contrast, our goal is not to discover the discrete units in speech. We treat VQ as a general approach to limit the model capacity, and study its impact on the information encoded in the learned representations.


## [MOCKINGJAY](https://arxiv.org/pdf/1910.12638.pdf)
> Liu, A. T., Yang, S.-w., Chi, P.-H., Hsu, P.-c., and Lee, H.-y. 
> Mockingjay: Unsupervised speech representation learning with deep bidirectional transformer encoders.
> ICASSP, 2020c.

Number of parameters:
- Mockingjay = 85.12M, trained on LS 360 hr


## [NPC](https://arxiv.org/pdf/2011.00406.pdf)
> Liu, A. H., Chung, Y. A., & Glass, J. (2020). 
> Non-autoregressive predictive coding for learning speech representations from local dependencies. 
> arXiv preprint arXiv:2011.00406. 


## [DeCoAR 2.0](https://arxiv.org/pdf/2012.06659.pdf)
> Ling, S. and Liu, Y. 
> DeCoAR 2.0: Deep contextualized acoustic representations with vector quantization. 
> arXiv preprint arXiv:2012.06659, 2020.
> Amazon AWS AI

DECOAR = DEep COntextualized Acoustuc Representations with vector quantization

Contribution (compared to DeCoAR 1.0)
  - use Transformer as encoding block instead of LSTM (vanilla DeCoAR)
  - the addition of a vector quantization layer
  - a new objective function that combines masked-based reconstruction loss with VQ diversity loss

Exp Settings (similar to wav2vec2.0)
  - model dimension = 768
  - the inner dimension in feed forward sublayer = 3072
  - attention heads = 8
  - slice size K = 20
  - G = 2 and V = 320
  - (G is group, V is the number of representations in the codebook)

This work categorized the proxy tasks in learning speech representation into two types. 
- The first type is based on contrastive loss
  - The wav2vec and its variants
  - The model is trained to learn representations containing information that most discriminates the future or masked frame from a set of negative sample via contrastive loss.
- The second type is based on reconstructive loss. 
  - The proxy task for these representation learning methods is to reconstruct temporal slices of acoustic features based on contextual
information. 
  - These reconstruction tasks can be defined as autoregressive reconstruction, or masked-based reconstruction. 
  - APC and its follow-up are examples to use autoregressive reconstruction loss. 
  - In many state-of-the-art pretrained language model task, masked-based prediction is adopted in the proxy tasks such as BERT and XLNet. 
  - In speech, instead of prediction, we randomly mask temporal slices of acoustic features and attempt to reconstruct them 


## [TERA](https://arxiv.org/pdf/2007.06028.pdf)
> Liu, A. T., Li, S.-W., and Lee, H.-y. 
> Tera: Self-supervised learning of transformer encoder representation for speech.
> arXiv preprint arXiv:2007.06028, 2020b.

- Self-Supervised Learning of Transformer Encoder Representation for Speech
- self-supervised pre-training scheme
  - time alteration
  - frequency alteration
  - magnitude alteration


# Discriminative Modeling as Main Learning Methods
Models are pretrained with "discriminative loss" or "contrastive loss".

## [CPC](https://arxiv.org/pdf/1807.03748.pdf)
> Oord, A. V. D., Li, Y., & Vinyals, O. (2018). 
> Representation learning with contrastive predictive coding. 
> arXiv preprint arXiv:1807.03748.
> DeepMind (acquired by Google in 2014).

- Use a probabilistic contrastive loss which induces the latent space to capture information that is maximally useful to predict future samples

InfoNCE
- Both the encoder and autoregressive model are trained to jointly optimize a loss based on NCE, which we will call InfoNCE
- Optimize given a set of N random samples containing one positive sample and d N − 1 negative samples
- The loss is the categorical cross-entropy of classifying the positive sample correctly


## wav2vec Series

### [wav2vec: Unsupervised pre-training for speech recognition](https://arxiv.org/pdf/1904.05862.pdf)
> Schneider, S., Baevski, A., Collobert, R., and Auli, M.
> wav2vec: Unsupervised pre-training for speech recognition. 
> In Interspeech, 2019.

Number of parameters:
- wav2vec = 32.54M, trained on LS 960 hr


### [vq-wav2vec: Self-supervised learning of discrete speech representations](https://arxiv.org/pdf/1910.05453.pdf)
> Baevski, A., Schneider, S., and Auli, M. 
> vq-wav2vec: Selfsupervised learning of discrete speech representations. 
> In ICLR, 2020a.

Number of parameters:
- vq-wav2vec = 34.15M, trained on LS 960 hr
> G = 32, V = 1280
> (G is group, V is the number of representations in the codebook)


### [wav2vec 2.0: A Framework for Self-Supervised Learning of Speech Representations](https://arxiv.org/pdf/2006.11477.pdf)
> Baevski, A., Zhou, Y., Mohamed, A., and Auli, M. 
> wav2vec 2.0: A framework for self-supervised learning of speech representations. 
> In NeurIPS, 2020b.
> Facebook AI.

Model pipeline:
  - Feature encoder: 7 blocks, 512 channels each block, about 20ms stride between each sample
  - Transformers: BASE contains 12 transformer blocks, model dimension 768, inner dimension (FFN) 3,072 and 8 attention heads
  - Quantization module: G(groupd) = 2 and V(entries) = 320, theoretical maximum codewords = 102.4k

Pre-training tasks (contrastive):
  - try to identify the true quantized representation for a masked time step within a set of distractors

Number of parameters:
- wav2vec 2.0 Base = 95.04M, trained on LS 960 hr
- wav2vec 2.0 Large = 317.38M, trained on LL 60k hr


### [Robust wav2vec 2.0]()
> Hsu, W.-N., Sriram, A., Baevski, A., Likhomanenko, T., Xu, Q., Pratap, V., Kahn, J., Lee, A., Collobert, R., Synnaeve, G., et al. 
> Robust wav2vec 2.0: Analyzing domain shift in self-supervised pre-training. 
> arXiv preprint arXiv:2104.01027, 2021b


### [XLSR](https://arxiv.org/pdf/2006.13979.pdf)
> Conneau, A., Baevski, A., Collobert, R., Mohamed, A., & Auli, M. (2020). 
> Unsupervised cross-lingual representation learning for speech recognition. 
> arXiv preprint arXiv:2006.13979.

XLSR = cross-lingual speech representations


### [XLS-R](https://arxiv.org/pdf/2111.09296.pdf)
> Babu, A., Wang, C., Tjandra, A., Lakhotia, K., Xu, Q., Goyal, N., ... & Auli, M. (2021). 
> XLS-R: Self-supervised Cross-lingual Speech Representation Learning at Scale. 
> arXiv preprint arXiv:2111.09296.
> Meta AI, Google AI, Outreach, Hugging Face

XLS-R = XLM-R for Speech (XLM-R is a multilingual NLU model)
- XLM (Lample and Conneau, 2019) have pushed the stateof-the-art on cross-lingual understanding tasks by jointly pretraining large Transformer models (Vaswani et al., 2017) on many languages.
- XLM-R: XLM-RoBERTa (XLM-R)
- [RoBERTa: A Robustly Optimized BERT Pretraining Approach](https://github.com/pytorch/fairseq/tree/main/examples/roberta)
  - RoBERTa iterates on BERT's pretraining procedure, including training the model longer, with bigger batches over more data; removing the next sentence prediction objective (NSP); training on longer sequences; and dynamically changing the masking pattern applied to the training data.

Number of parameters:
- XLS-R (0.3B)
- XLS-R (1B)
- XLS-R (2B)

## UniSpeech Series
### [UniSpeech-SAT](Universal Speech Representation Learning with Speaker Aware Pre-Training)
- [microsoft/UniSpeech](https://github.com/microsoft/UniSpeech)
- [HugglingFace: Unispeech-SAT](https://huggingface.co/transformers/model_doc/unispeech_sat.html)
- powerful performance on various speaker related benchmarks

### [HuBert(2021)](https://arxiv.org/abs/2106.07447)
- HuBERT: Self-Supervised Speech Representation Learning by Masked Prediction of Hidden Units
- Hsu et al., 2021a
- [Hubert on HugglingFace](https://huggingface.co/transformers/model_doc/hubert.html)

Number of parameters & data:
- HuBERT Base = 94.68M, trained on LS 960 hr
- HuBERT Large = 316.61M, trained on LL 60k hr


## [WavLM: Large-Scale Self-Supervised Pre-Training for Full Stack Speech Processing](https://arxiv.org/pdf/2110.13900.pdf)
Tasks:
- M-P + VQ 
- GREP
- Utterance Mixing

Number of parameters:
- WavLM Large: 316.62M

- WavLM is built based on the HuBERT framework, with an emphasis on
both spoken content modeling and speaker identity preservation.



# Multi-task Learning as Self-learning Methods
Multiple pretraining objectives are adopted.
(看到用很多種 loss 都先放這邊)


## [PASE+: Multi-task self-supervised learning for Robust Speech Recognition](https://arxiv.org/abs/2001.09239)
> Ravanelli, M., Zhong, J., Pascual, S., Swietojanski, P., Monteiro, J., Trmal, J., & Bengio, Y. (2020, May). 
> Multi-task self-supervised learning for robust speech recognition. 
> In ICASSP 2020-2020 IEEE International Conference on Acoustics, Speech and Signal Processing (ICASSP) (pp. 6989-6993). IEEE.
> Official Github: [santi-pdp/pase](https://github.com/santi-pdp/pase)

- Problem Agnostic Speech Encoder
- Encoder and workers are jointly trained with backpropagation by optimizing a total loss that is computed as the average of each worker cost



## [W2V-BERT: COMBINING CONTRASTIVE LEARNING AND MASKED LANGUAGE MODELING FOR SELF-SUPERVISED SPEECH PRE-TRAINING](https://arxiv.org/pdf/2108.06209v2.pdf)
This work focus on improving the unsupervised pretraining aspect of semi-supervised ASR by proposing a novel pre-training framework called w2v-BERT, which combines the core methodologies of wav2vec 2.0 and BERT.
> BERT: MLM pre-training objective
> wav2vec: contrastive task and discretized speech units via VQ(vector quantization)

Number of parameters: 
- w2v-BERT XL = 0.6 B 
- w2v-BERT XXL = 1.0 B
> Attention Heads = 8
> Codebook Size = 1024, Code Dim = 1024

Data:
- Libri-Light unlab-60k subset for pre-training w2v-BERT
- LibriSpeech 960hr subset for main ASR results




