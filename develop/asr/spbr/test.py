import speechbrain as sb
from speechbrain.lobes.models.huggingface_wav2vec import HuggingFaceWav2Vec2

source = sb.dataio.dataio.read_audio('../774.wav').squeeze()
print(source.shape)

source = source.unsqueeze(0)
print(source.shape)

# HuggingFace model hub
model_hub = "facebook/wav2vec2-large-xlsr-53"

model_huggingface = HuggingFaceWav2Vec2(model_hub, save_path="pretrained/")

fea_huggingface = model_huggingface(source)
print(fea_huggingface.shape)
