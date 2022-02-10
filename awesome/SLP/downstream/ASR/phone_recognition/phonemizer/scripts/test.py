from phonemizer import phonemize
from phonemizer.backend import EspeakBackend
backend = EspeakBackend('zh')

import opencc
converter = opencc.OpenCC('t2s.json')

# converter.convert('汉字')  # 漢字


text = "莘喵買醬油 每天吃豆腐"
text = "喵喵買醬油 每天吃豆腐"
text = converter.convert(text)
print(text)
text_list = [[text]]

phonemized = [backend.phonemize(line) for line in text_list]

print(phonemized)
