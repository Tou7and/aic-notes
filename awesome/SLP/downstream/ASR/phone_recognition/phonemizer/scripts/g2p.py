import sys
from phonemizer import phonemize
from phonemizer.backend import EspeakBackend
backend = EspeakBackend('zh')

import opencc
converter = opencc.OpenCC('t2s.json')

# converter.convert('汉字')  # 漢字

if __name__ == "__main__":
    text = sys.argv[1]
    text = converter.convert(text)
    print(text)
    text_list = [[text]]
    
    phonemized = [backend.phonemize(line) for line in text_list]

    print(phonemized)
