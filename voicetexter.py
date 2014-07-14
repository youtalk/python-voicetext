#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import wave

import requests
from requests.auth import HTTPBasicAuth
import pyaudio


class VoiceText(object):
    URL = 'https://api.voicetext.jp/v1/tts'
    CHUNK = 1024
    _audio = pyaudio.PyAudio()

    def __init__(self, user_name, password='', speaker='hikari'):
        self._auth = HTTPBasicAuth(user_name, password)
        self._data = {'speaker': speaker}

    def to_wave(self, text):
        self._data['text'] = text
        request = requests.post(self.URL, self._data, auth=self._auth)
        print request.status_code
        return request.content

    def speak(self, text):
        path = '/tmp/text.wav'
        with open(path, 'wb') as temp:
            temp.write(self.to_wave(text))

        temp = wave.open(path)
        stream = self._audio.open(
            format=self._audio.get_format_from_width(temp.getsampwidth()),
            channels=temp.getnchannels(),
            rate=temp.getframerate(),
            output=True)
        data = temp.readframes(self.CHUNK)
        while data:
            stream.write(data)
            data = temp.readframes(self.CHUNK)
        stream.close()
        temp.close()


if __name__ == '__main__':
    vt = VoiceText(user_name=sys.argv[1])
