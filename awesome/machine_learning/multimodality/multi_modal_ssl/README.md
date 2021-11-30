# Multi-modal Self-supervised Learning
Multi-modality 的資料和 SSL 向性感覺很好?

# Look, Listen and Learn
- Arandjelovic, R., & Zisserman, A. (2017). 
- In Proceedings of the IEEE International Conference on Computer Vision (pp. 609-617).
- DeepMind, VGG - Department of Engineering Science - University of Oxford
- [arxiv](https://openaccess.thecvf.com/content_ICCV_2017/papers/Arandjelovic_Look_Listen_and_ICCV_2017_paper.pdf)
- [repository]()
- Data type: Visual and Audio

Keypoints
- The video itself contain rich information about the correspondence between the visual and the audio streams
- SSL task
  - The AVC task: binary classification determing if the video frame and the short audio clip correspond to each other or not
- Downstream tasks
  - Visual classification on ImageNet
  - Sound classification on ESC-50 and DCASE
- Network architecture
  - Vision subnetwork: VGG
  - Audio subnetwork: VGG with 1D intensities (log-spectrogram) instead of 3D (RGB)
  - Fusion network: 2 FC layers with ReLU in between
- Datasets (Video)
  - Flickr-SoundNet 
    - 500k videos (400k training, 50k validation and 50k test)
    - only use the first 10 seconds of each video.
  - Kinetics-Sounds 
    - subset of 19k 10 second video clips (15k training, 1.9k validation, 1.9k test)
    - cropped to 10 seconds

# ViLBERT
ViLBERT: Pretraining Task-Agnostic Visiolinguistic Representations for Vision-and-Language Tasks
- Lu, J., Batra, D., Parikh, D., & Lee, S. (2019). 
- Georgia Institute of Technology, Facebook AI Research, Oregon State University
- [arxiv](https://arxiv.org/pdf/1908.02265.pdf%20http://arxiv.org/abs/1908.02265.pdf)
- [repository](https://github.com/facebookresearch/vilbert-multi-task)
- [Huggingface: transformers4vl-vilbert (not sure)](https://huggingface.co/visualjoyce/transformers4vl-vilbert)
- Data type: Visual and Text

Keypoints
- Extending BERT to Jointly Represent Images and Text
- Discretizing the space of visual inputs into the visual tokens via clustering
- Start from a pretrained BERT model
- Develop a two-stream architecture modelling each modality separately
- Fusing them through a set of attention-based interactions
- SSL tasks
  - the masked language modelling task: like standard BERT
  - multi-modal alignment task: presented an image-text pair, predict whether the image and text are aligned
- Downstream tasks
  - Visual Question Answering (VQA)
  - Visual Commonsense Reasoning (VCR)
  - Grounding Referring Expressions
  - Caption-Based Image Retrieval
  - Zero-shot Caption-Based Image Retrieval

