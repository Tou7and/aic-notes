import json

def load_vocab(src_vocab, dst_vocab):
    with open(src_vocab, 'r') as reader:
        vocab_list = json.load(reader)
    # vocab_list = list(set(vocab_train["vocab"][0]) | set(vocab_test["vocab"][0]) | set(vocab_valid["vocab"][0]))
    vocab_dict = {v: k for k, v in enumerate(vocab_list)}
    vocab_dict["|"] = vocab_dict[" "]
    del vocab_dict[" "]
    vocab_dict["[UNK]"] = len(vocab_dict)
    vocab_dict["[PAD]"] = len(vocab_dict)

    print("Number of vocabulary: ", len(vocab_dict))
    print("Load vocabulary successfully.")

    with open(dst_vocab, 'w') as writer:
        json.dump(vocab_dict, writer)
    return vocab_dict

load_vocab(
    "/media/volume1/aicasr/Manifests/vocab/enchars/vocab_pinyin.json",
    "/media/volume1/aicasr/Manifests/vocab/enchars/hugface/vocab.json",
)

