# -*- coding:utf-8 -*-
import time
import torchaudio
from speechbrain.pretrained import EncoderClassifier

audio = '/media/volume1/aicasr/meta-transfer-asr/tests/774.wav'
classifier = EncoderClassifier.from_hparams(
        source="speechbrain/spkrec-xvect-voxceleb", 
        savedir="pretrained_models/spkrec-xvect-voxceleb")

t_start = time.time()
signal, fs = torchaudio.load(audio)
embeddings = classifier.encode_batch(signal)
t_cost = time.time() - t_start

print(embeddings)
print(embeddings.size())
print("time: {}".format(t_cost))
