import os
import sys
import re
import json
import unicodedata

from jiwer import wer

def text_normalize(text, sep=" ", replace_sp=True):
    """ Remove and record anything that are not Chinese, English and separator. 

    Returns:
        new_text(str)
    """
    # TODO: make the nested loop more readable, or replaced it with better approach 
    bad_symbols = dict()
    # non_enzh_symbols = dict()

    text = text.strip()
    text = text.replace("　", " ")
    text = text.lower()

    new_text = ""
    prev_char = " "
    for char in text:
        if is_english_char(char):
            if is_chinese_char(prev_char):
                new_text = new_text + sep + char
            else:
                new_text += char
            prev_char = char
            continue

        if is_chinese_char(char):
            if is_english_char(prev_char) or is_chinese_char(prev_char):
                new_text = new_text + sep + char
            else:
                new_text += char
            prev_char = char
            continue

        if char == sep:
            new_text += char
            prev_char = char
            continue

        if char in bad_symbols:
            bad_symbols[char]['counts'] += 1
        else:
            bad_symbols[char] = {'counts': 1}

    return new_text


def is_english_char(cc):
    """ Check if the character is English (lower)
    args:
        cc: char
    output:
        boolean
    """
    return unicodedata.category(cc) == 'Ll'


def is_chinese_char(cc):
    """ Check if the character is Chinese
    args:
        cc: char
    output:
        boolean
    """
    return unicodedata.category(cc) == 'Lo'


def compute_wer(ground_truth, hypothesis):
    error = wer(text_normalize(ground_truth), text_normalize(hypothesis))
    print(error)

if __name__ == "__main__":
    ref = sys.argv[1]
    hyp = sys.argv[2]
    compute_wer(ref, hyp)

