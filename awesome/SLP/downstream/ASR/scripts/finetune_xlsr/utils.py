import random
import re
import json
import torchaudio
import librosa
import numpy as np
import pandas as pd
from datasets import load_dataset, load_metric
from datasets import ClassLabel


def show_random_elements(dataset, num_examples=10):
    assert num_examples <= len(dataset), "Can't pick more elements than there are in the dataset."
    picks = []
    for _ in range(num_examples):
        pick = random.randint(0, len(dataset)-1)
        while pick in picks:
            pick = random.randint(0, len(dataset)-1)
        picks.append(pick)

    df = pd.DataFrame(dataset[picks])
    # display(HTML(df.to_html()))
    print(df)

def preprocess_text(batch):
    chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"\“\%\‘\”\�\，\？\。\、\！\「\」]'
    batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]).lower() + " "
    batch["sentence"] = " ".join(list(batch["sentence"]))
    batch["sentence"] = batch["sentence"].replace("  ", " ")
    return batch


def speech_file_to_array_fn(batch, resample=True):
    speech_array, sampling_rate = torchaudio.load(batch["path"])
    batch["speech"] = speech_array[0].numpy()
    batch["sampling_rate"] = sampling_rate
    batch["target_text"] = batch["text"]
    if resample:
        batch["speech"] = librosa.resample(np.asarray(batch["speech"]), 48_000, 16_000)
        batch["sampling_rate"] = 16_000
    return batch

def compute_metrics(pred):
    pred_logits = pred.predictions
    pred_ids = np.argmax(pred_logits, axis=-1)

    pred.label_ids[pred.label_ids == -100] = processor.tokenizer.pad_token_id

    pred_str = processor.batch_decode(pred_ids)
    # we do not want to group tokens when computing the metrics
    label_str = processor.batch_decode(pred.label_ids, group_tokens=False)

    wer_metric = load_metric("wer")
    wer = wer_metric.compute(predictions=pred_str, references=label_str)
    return {"wer": wer}

