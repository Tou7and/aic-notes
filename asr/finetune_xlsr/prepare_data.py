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

def prepare_ner_vol1(manifest_dir, vocab_file):
    """ Prepare NER Vol1 corpus for Wav2vec2.0 fine-tuning.

    Manifest directory:
        /mnt/smb01/Manifests/mtasr/ner_pp/vol1/
    Vocab file:
        /mnt/smb01/Models/v10/vocab_labels.json

    Src Columns: path, text_path, duration, n_words
    Dst Columns: path, sentence  

    Returns:
        dataset (dict)
        vocab_dict (dict)
    """
    train_csv = os.path.join(manifest_dir, "train.csv")
    dev_csv = os.path.join(manifest_dir, "dev.csv")

    with open(vocab_file, 'r') as reader:
        vocab_list = json.load(reader)
    # vocab_list = list(set(vocab_train["vocab"][0]) | set(vocab_test["vocab"][0]) | set(vocab_valid["vocab"][0]))
    vocab_dict = {v: k for k, v in enumerate(vocab_list)}
    vocab_dict["|"] = vocab_dict[" "]
    del vocab_dict[" "]
    vocab_dict["[UNK]"] = len(vocab_dict)
    vocab_dict["[PAD]"] = len(vocab_dict)
    print("Number of vocabulary: ", len(vocab_dict))

    the_dataset = load_dataset('csv', data_files={'train': [train_csv], 'dev': [dev_csv]}, column_names=["path", "text_path", "duration", "n_words"])
    the_dataset = the_dataset.map(read_text)

    the_dataset = the_dataset.remove_columns(["text_path", "duration", "n_words"])
    print(len(the_dataset))
    show_random_elements(the_dataset["train"])
    show_random_elements(the_dataset["dev"])
    return the_dataset, vocab_dict

def prepare_nursing():

    return

def prepare_commonvoice():
    common_voice_train = load_dataset("common_voice", "zh-TW", split="train")
    common_voice_valid = load_dataset("common_voice", "zh-TW", split="validation")
    common_voice_test = load_dataset("common_voice", "zh-TW", split="test")

    # {'accent': 'netherlands', 'age': 'fourties', 'client_id': 'bbbcb732e0f422150c30ff3654bbab572e2a617da107bca22ff8b89ab2e4f124d03b6a92c48322862f60bd0179ae07baf0f9b4f9c4e11d581e0cec70f703ba54', 'down_votes': 0, 'gender': 'male', 'locale': 'nl', 'path': 'nl/clips/common_voice_nl_23522441.mp3', 'segment': "''", 'sentence': 'Ik vind dat een dubieuze procedure.', 'up_votes': 2}
    common_voice_train = common_voice_train.remove_columns(["accent", "age", "client_id", "down_votes", "gender", "locale", "segment", "up_votes"])
    common_voice_valid = common_voice_valid.remove_columns(["accent", "age", "client_id", "down_votes", "gender", "locale", "segment", "up_votes"])
    common_voice_test = common_voice_test.remove_columns(["accent", "age", "client_id", "down_votes", "gender", "locale", "segment", "up_votes"])
    # show_random_elements(common_voice_train.remove_columns(["path"]))
    # Columns left: "path", "sentence"

    common_voice_train = common_voice_train.map(preprocess_text)
    common_voice_test = common_voice_test.map(preprocess_text)
    common_voice_valid = common_voice_test.map(preprocess_text)

    show_random_elements(common_voice_train.remove_columns(["path"]))

    common_voice_train.to_csv("data/train.csv", index=None)
    common_voice_test.to_csv("data/test.csv", index=None)
    common_voice_valid.to_csv("data/valid.csv", index=None)

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

