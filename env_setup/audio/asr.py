""" TorchServe ASR Clients
"""
# from cpwz.asr_clients import AICASR
import json
import requests

# ASR_URL_81 = "http://10.21.98.81:8080/predictions/speech"
ASR_URL_81 = "http://10.21.98.81:5580/predictions/zswj1"
PUNC_URL_81 = "http://10.21.98.81:5580/predictions/DeepPunc2"

ASR_URL_240 = "http://10.65.51.240:5580/predictions/zswj1"
PUNC_URL_240 = "http://10.65.51.240:5580/predictions/DeepPunc2"
NER_URL_240 = "http://10.65.51.240:5580/predictions/bm02"

def post_audio(url, audio):
    files = {'data': open(audio, 'rb')}
    req = requests.post(url, files=files)
    try:
        info = json.loads(req.text)
    except:
        print(req)
        info = json.loads(req)
    return info

def post_text(url, text):
    files = {'data': str(text)}
    req = requests.post(url, files=files)
    try:
        info = json.loads(req.text)
    except:
        print(req)
        info = json.loads(req)
    return info

if __name__ == "__main__":
    info = post_audio(ASR_URL_81 , "/home/t36668/projects/aic-notes/env_setup/ffmpeg/segments/chunk-0003.wav")
    print(info)
    # info = post_text(PUNC_URL_81, info["result"])
    # print(info)
    info = post_audio(ASR_URL_81 , "/home/t36668/projects/aic-notes/env_setup/ffmpeg/segments/chunk-0004.wav")
    print(info)

    info = post_audio(ASR_URL_81 , "/home/t36668/projects/aic-notes/env_setup/ffmpeg/segments/chunk-0005.wav")
    print(info)

