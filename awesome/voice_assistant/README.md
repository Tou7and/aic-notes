# Voice Assitants / Conversational AI
Voice Assistants (conversational AI) ~= Voice Interface + Chatbot Engine

Last update: 2021.11.24

# Tools
Tools for building voice assistants

## [HuggingFace](https://huggingface.co/)

## [NVIDIA/NeMo](https://github.com/NVIDIA/NeMo)
- uses [Pytorch Lightning](https://github.com/PyTorchLightning/pytorch-lightning) for multi-GPU/multi-node training
- uses [Hydra](https://github.com/facebookresearch/hydra) for configuring NeMo models and PyTorch Lightning Trainers
- support Kaldi Formatted Data
- pre-trained models available
  - packaged as a .nemo file, containing the PyTorch checkpoint along with everything needed

Tasks and examples
- Speech Processing
  - ASR: Jasper, QuartzNet, Citrinet, ContextNet, Conformer-CTC, Conformer-Transducer
  - Speaker Recognition: SpeakerNet, ECAPA-TDNN
  - Speaker Diarization: VAD (MarbleNet) --> Speaker Embedding Extraction (SpeakerNet & ECAPA-TDNN) --> Clustering
- Natural Language Processing (NLP)
- Text to Speech (TTS)
  - two stage pipeline: generate a mel spectrogram from text --> generate audio from a mel spectrogram
  - end-to-end approach

## [pytorch/fairseq](https://github.com/pytorch/fairseq)
Tasks: Translation, Language Modeling

Models: CNN, LSTM, Transformers
- Convolutional Neural Networks (CNN)
- Long Short-Term Memory (LSTM) networks
- Transformer (self-attention) networks

[Examples](https://github.com/pytorch/fairseq/tree/main/examples)

## [SpeechBrain](https://speechbrain.github.io/)
- Works well with HuggingFace
- Human friendly recipes (codes + configs)
- Google Colab [Tutorials](https://speechbrain.github.io/tutorial_advanced.html)

Tasks
- Speech Recognition
- Source Separation
- Multi-microphone processing
- ...


# Blogs
[Build a voice assistant with Rasa and Mozilla](https://rasa.com/blog/how-to-build-a-voice-assistant-with-open-source-rasa-and-mozilla-tools/)
- [Rasa](https://github.com/RasaHQ/rasa)
- [Mozilla DeepSpeech](https://github.com/mozilla/DeepSpeech)
- [Mozilla TTS](https://github.com/mozilla/TTS)
- [Rasa Voice Interface](https://github.com/RasaHQ/rasa-voice-interface)

# Githubs
[IBM/watson-voice-bot](https://github.com/IBM/watson-voice-bot)

