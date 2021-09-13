import os
import random
import re
import json
import pandas as pd
from datasets import load_dataset, load_metric
from datasets import ClassLabel


def read_text(batch):
    # speech_array, sampling_rate = torchaudio.load(batch["path"])
    with open(batch["text_path"], "r") as reader:
        batch["sentence"] = reader.read().strip()
    chars_to_ignore_regex = '[\,\?\.\!\-\;\:\"\“\%\‘\”\�\，\？\。\、\！\「\」]'
    batch["sentence"] = re.sub(chars_to_ignore_regex, '', batch["sentence"]) + " "
    batch["sentence"] = " ".join(list(batch["sentence"]))
    batch["sentence"] = re.sub(' +', ' ', batch["sentence"])
    return batch

def prepare_ner_vol1(manifest_dir):
    """ Prepare NER Vol1 corpus for Wav2vec2.0 fine-tuning.

    Src Columns: path, text_path, duration, n_words
    Dst Columns: path, sentence  

    Returns:
        dataset (dict)
        vocab_dict (dict)
    """
    train_csv = os.path.join(manifest_dir, "train.csv")
    dev_csv = os.path.join(manifest_dir, "dev.csv")


    the_dataset = load_dataset('csv', data_files={'train': [train_csv], 'dev': [dev_csv]}, column_names=["path", "text_path", "duration", "n_words"])
    the_dataset = the_dataset.map(read_text)

    the_dataset = the_dataset.remove_columns(["text_path", "duration", "n_words"])
    print(len(the_dataset))
    show_random_elements(the_dataset["train"])
    show_random_elements(the_dataset["dev"])
    return the_dataset, vocab_dict

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

dataset_ner, vocab_dict = prepare_ner_vol1(
    "/mnt/smb01/Manifests/mtasr/ner_pp/vol1/",
    "/mnt/smb01/Models/v10/vocab_labels.json"
)

