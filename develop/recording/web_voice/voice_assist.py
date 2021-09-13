import os
import sys
import wave
from random import randint

def write_wav(byte_data, wav_path, raw=False):
    if raw:
        with wave.open(wav_path, 'wb') as writer:
            writer.setnchannels(1)
            writer.setsampwidth(2) # 16 bit = 2 byte
            writer.setframerate(16000)
            writer.writeframes(byte_data)
    else:
        with open(wav_path, 'wb') as writer:
            writer.write(byte_data)
    return

class VoiceAssist(object):
    def __init__(self):
        self.assist_id = "echo"

    def speech_to_text(speech_input):
        text = "[ unable to recognize ]"
        return text

    def text_to_speech(text):
        audio_output = None
        return audio_output

    def make_response(text):
        """ Echo: repeat the input and add random marks."""
        dice_result = randint(0, 1)
        if dice_result == 1:
            response = text + "!"
        else:
            response = text + "?"
        return response

class AzureAssit(VoiceAssist):
    def __init__(self, key_file, region="eastasia"):
        import azure.cognitiveservices.speech as speechsdk
        sub_key = self.get_key(key_file)
        self.speech_config = speechsdk.SpeechConfig(subscription=sub_key, region=region)

    def get_key(self, keyfile):
        with open(key_file, 'r') as reader:
            sub_key = reader.read()
        sub_key = sub_key.strip()
        return sub_key

    def speech_to_text(speech_input):
        if isinstance(speech_input, str):
            audio_input = speechsdk.AudioConfig(filename=speech_input)
            speech_recognizer = speechsdk.SpeechRecognizer(
                language="zh-TW",
                speech_config=self.speech_config,
                audio_config=audio_input
            )
            result = speech_recognizer.recognize_once_async().get()
            text = self.text_normalize(result.text)
        else:
            # raise NotImplemented("Only support audio path currently.")
            audio_input = speechsdk.AudioConfig(stream=speech_input)
            speech_recognizer = speechsdk.SpeechRecognizer(
                language="zh-TW",
                speech_config=self.speech_config,
                audio_config=audio_input
            )
            result = speech_recognizer.recognize_once_async().get()
            text = self.text_normalize(result.text)
        return text

    def text_normalize(self, text):
        text = text.replace("，", "")
        text = text.replace("。", "")
        text = text.replace("？", "")
        return text
