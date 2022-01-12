from transformers import Wav2Vec2CTCTokenizer
from transformers import Wav2Vec2FeatureExtractor
from transformers import Wav2Vec2Processor
from transformers import TrainingArguments
from transformers import Wav2Vec2ForCTC
from utils import show_random_elements, preprocess_text, speech_file_to_array_fn

model = Wav2Vec2ForCTC.from_pretrained("tmp/wav2vec2-large-xlsr-tw-demo/checkpoint-2000").to("cuda")
processor = Wav2Vec2Processor.from_pretrained("tmp/wav2vec2-large-xlsr-tw-demo")

speech_array = speech_file_to_array_fn("/media/volume1/aicasr/meta-transfer-asr/tests/10Hri-N28925-2.wav")


input_values = processor(batch["speech"], sampling_rate=batch["sampling_rate"][0]).input_values

input_dict = processor(input_values, return_tensors="pt", padding=True)
logits = model(input_dict.input_values.to("cuda")).logits
pred_ids = torch.argmax(logits, dim=-1)[0]

print("Prediction:")
print(processor.decode(pred_ids))
