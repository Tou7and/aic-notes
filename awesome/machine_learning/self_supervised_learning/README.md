# Self Supervised Learning

## Githubs
[Awesome Self Supervised Learning](https://github.com/jason718/awesome-self-supervised-learning)

[SSL for Voice and Speech](https://github.com/Tou7and/aic-notes/tree/main/awesome/voice_interface/asr/ssl)

## Blogs
[self-supervised-learning-lil-log](https://lilianweng.github.io/lil-log/2019/11/10/self-supervised-learning.html)


# Papers of unsupervised learning

## [Deep Clustering for Unsupervised Learning of Visual Features](https://arxiv.org/pdf/1807.05520.pdf)
- Keywords: unsupervised learning, clustering
- 2019, Facebook AI Research
- Mathilde Caron, Piotr Bojanowski, Armand Joulin, and Matthijs Douze

Abstract
  - adapt clustering to the end-to-end (pre)training of features on large datasets
  - iteratively groups the features with a standard clustering k-means algorithms
  - uses the subsequent assignments as supervision to update the weights of the network

Methods
  - Model architectures: standard AlexNet
  - Training data: ImageNet, 1.3M images uniformly distributed into 1000 classes
  - Optimization:
    - dropout, a constant step size, an L2 penalization of the weights θ and a momentum of 0.9
    - For the clustering, features are PCA-reduced to 256 dimensions, whitened and L2-normalized
    - 500 epochs, which takes 12 days on a Pascal P100 GPU for AlexNet
  - Hyperparameter selection: select hyperparameters on a down-stream task
    - i.e., object classification on the validation set of Pascal VOC with no fine-tuning

Conclusion
  - propose a scalable clustering approach for the unsupervised learning of convnets
    1. iterates between clustering with k-means the features produced by the convnet
    2. update its weights by predicting the cluster assignments as pseudo-labels in a discriminative loss
  - achieves performance that are significantly better than the previous SOTA on every standard transfer task

