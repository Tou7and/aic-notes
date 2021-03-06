""" An Easy Wav2vec2.0 Training Pipeline
"""
import sys
import random
import re
import json
import pandas as pd
import numpy as np
from datasets import load_dataset, load_metric
from datasets import ClassLabel

import torch
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Union

from transformers import Wav2Vec2CTCTokenizer
from transformers import Wav2Vec2FeatureExtractor
from transformers import Wav2Vec2Processor
from transformers import TrainingArguments
from transformers import Wav2Vec2ForCTC
from transformers import Trainer

from utils import show_random_elements, preprocess_text, speech_file_to_array_fn
from prepare_cvtw import prepare_cvtw_local

print("Prepare Processor (Tokenizer + Feature Extractor) ...")
tokenizer = Wav2Vec2CTCTokenizer(
    "/media/volume1/aicasr/Manifests/vocab/enchars/hugface/vocab.json", 
    unk_token="[UNK]", 
    pad_token="[PAD]", 
    word_delimiter_token="|")

feature_extractor = Wav2Vec2FeatureExtractor(
    feature_size=1, 
    sampling_rate=16000, 
    padding_value=0.0, 
    do_normalize=True, 
    return_attention_mask=True)

PROCESSOR = Wav2Vec2Processor(
    feature_extractor=feature_extractor, 
    tokenizer=tokenizer)

PROCESSOR.save_pretrained("./tmp/wav2vec2-large-xlsr-tw-demo")

print("Setup Training Args")
TRAINING_ARGS = TrainingArguments(
    output_dir="./tmp/wav2vec2-large-xlsr-tw-demo",
    group_by_length=True,
    per_device_train_batch_size=16,
    gradient_accumulation_steps=2,
    evaluation_strategy="steps",
    num_train_epochs=30,
    fp16=True,
    save_steps=400,
    eval_steps=400,
    logging_steps=400,
    learning_rate=3e-4,
    warmup_steps=500,
    save_total_limit=3,
)

def prepare_dataset(batch):
    # check that all files have the correct sampling rate
    assert (
        len(set(batch["sampling_rate"])) == 1
    ), f"Make sure all inputs have the same sampling rate of {processor.feature_extractor.sampling_rate}."

    batch["input_values"] = PROCESSOR(batch["speech"], sampling_rate=batch["sampling_rate"][0]).input_values

    with PROCESSOR.as_target_processor():
        batch["labels"] = PROCESSOR(batch["target_text"]).input_ids
    return batch

@dataclass
class DataCollatorCTCWithPadding:
    """
    Data collator that will dynamically pad the inputs received.
    Args:
        processor (:class:`~transformers.Wav2Vec2Processor`)
            The processor used for proccessing the data.
        padding (:obj:`bool`, :obj:`str` or :class:`~transformers.tokenization_utils_base.PaddingStrategy`, `optional`, defaults to :obj:`True`):
            Select a strategy to pad the returned sequences (according to the model's padding side and padding index)
            among:
            * :obj:`True` or :obj:`'longest'`: Pad to the longest sequence in the batch (or no padding if only a single
              sequence if provided).
            * :obj:`'max_length'`: Pad to a maximum length specified with the argument :obj:`max_length` or to the
              maximum acceptable input length for the model if that argument is not provided.
            * :obj:`False` or :obj:`'do_not_pad'` (default): No padding (i.e., can output a batch with sequences of
              different lengths).
        max_length (:obj:`int`, `optional`):
            Maximum length of the ``input_values`` of the returned list and optionally padding length (see above).
        max_length_labels (:obj:`int`, `optional`):
            Maximum length of the ``labels`` returned list and optionally padding length (see above).
        pad_to_multiple_of (:obj:`int`, `optional`):
            If set will pad the sequence to a multiple of the provided value.
            This is especially useful to enable the use of Tensor Cores on NVIDIA hardware with compute capability >=
            7.5 (Volta).
    """

    processor: Wav2Vec2Processor
    padding: Union[bool, str] = True
    max_length: Optional[int] = None
    max_length_labels: Optional[int] = None
    pad_to_multiple_of: Optional[int] = None
    pad_to_multiple_of_labels: Optional[int] = None

    def __call__(self, features: List[Dict[str, Union[List[int], torch.Tensor]]]) -> Dict[str, torch.Tensor]:
        # split inputs and labels since they have to be of different lenghts and need
        # different padding methods
        input_features = [{"input_values": feature["input_values"]} for feature in features]
        label_features = [{"input_ids": feature["labels"]} for feature in features]

        batch = self.processor.pad(
            input_features,
            padding=self.padding,
            max_length=self.max_length,
            pad_to_multiple_of=self.pad_to_multiple_of,
            return_tensors="pt",
        )
        with self.processor.as_target_processor():
            labels_batch = self.processor.pad(
                label_features,
                padding=self.padding,
                max_length=self.max_length_labels,
                pad_to_multiple_of=self.pad_to_multiple_of_labels,
                return_tensors="pt",
            )

        # replace padding with -100 to ignore loss correctly
        labels = labels_batch["input_ids"].masked_fill(labels_batch.attention_mask.ne(1), -100)
        batch["labels"] = labels
        return batch

def compute_metrics(pred):
    pred_logits = pred.predictions
    pred_ids = np.argmax(pred_logits, axis=-1)

    pred.label_ids[pred.label_ids == -100] = PROCESSOR.tokenizer.pad_token_id

    pred_str = PROCESSOR.batch_decode(pred_ids)
    # we do not want to group tokens when computing the metrics
    label_str = PROCESSOR.batch_decode(pred.label_ids, group_tokens=False)

    wer_metric = load_metric("wer")
    wer = wer_metric.compute(predictions=pred_str, references=label_str)

    return {"wer": wer}

def main():
    """ Training pipeline.

    1. Prepare data
    2. Train
    3. Eval

    """
    print("Process training data ...")
    print("-"*30)
    dataset_cvtw = prepare_cvtw_local(
        "/media/volume1/aicasr/Manifests/commonvoice_tw/v02/pinyin/small/",
        "/media/volume1/aicasr/Manifests/vocab/enchars/vocab_pinyin.json"
    )
    # common_voice_train = common_voice_train.map(speech_file_to_array_fn, remove_columns=common_voice_train.column_names)
    # common_voice_valid = common_voice_valid.map(speech_file_to_array_fn, remove_columns=common_voice_valid.column_names)
    # common_voice_test = common_voice_test.map(speech_file_to_array_fn, remove_columns=common_voice_test.column_names)
    dataset_cvtw = dataset_cvtw.map(speech_file_to_array_fn)
    dataset_cvtw = dataset_cvtw.map(prepare_dataset, batch_size=8, num_proc=4, batched=True)
    # common_voice_train = common_voice_train.map(prepare_dataset, remove_columns=common_voice_train.column_names, batch_size=8, num_proc=4, batched=True)
    # common_voice_valid = common_voice_valid.map(prepare_dataset, remove_columns=common_voice_valid.column_names, batch_size=8, num_proc=4, batched=True)
    # common_voice_test = common_voice_test.map(prepare_dataset, remove_columns=common_voice_test.column_names, batch_size=8, num_proc=4, batched=True)

    print("Setup trainer ...")
    print("-"*30)
    data_collator = DataCollatorCTCWithPadding(processor=PROCESSOR, padding=True)

    print("Load pretrained Wave2vec2.0 ...")
    model = Wav2Vec2ForCTC.from_pretrained(
        "facebook/wav2vec2-large-xlsr-53",
        attention_dropout=0.1,
        hidden_dropout=0.1,
        feat_proj_dropout=0.0,
        mask_time_prob=0.05,
        layerdrop=0.1,
        gradient_checkpointing=True,
        ctc_loss_reduction="mean",
        pad_token_id=PROCESSOR.tokenizer.pad_token_id,
        vocab_size=len(PROCESSOR.tokenizer)
    )
    model.freeze_feature_extractor()
    print("Start Training ... ")
    print("-"*30)
    trainer = Trainer(
        model=model,
        data_collator=data_collator,
        args=TRAINING_ARGS,
        compute_metrics=compute_metrics,
        train_dataset=dataset_cvtw['train'],
        eval_dataset=dataset_cvtw['dev'],
        tokenizer=PROCESSOR.feature_extractor,
    )
    trainer.train()

if __name__ == "__main__":
    main()

