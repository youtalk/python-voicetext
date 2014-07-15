#!/usr/bin/env python
# -*- coding: utf-8 -*-

import wave
import logging

import requests
from requests.auth import HTTPBasicAuth
import pyaudio


class VoiceTexter(object):
    URL = 'https://api.voicetext.jp/v1/tts'
    CHUNK = 1024
    _audio = pyaudio.PyAudio()

    def __init__(self, user_name, password='', speaker='hikari'):
        if not user_name:
            raise Exception('%s needs correct "user_name"' % self.__class__.__name__)

        self._auth = HTTPBasicAuth(user_name, password)
        self._data = {'speaker': speaker}

    def speaker(self, speaker):
        if speaker in ['show', 'haruka', 'hikari', 'takeru']:
            self._data['speaker'] = speaker
        else:
            logging.warning('Unknown speaker: %s' % str(speaker))

        return self

    def emotion(self, emotion, level=1):
        if emotion in ['happiness', 'anger', 'sadness']:
            self._data['emotion'] = emotion
            if isinstance(level, int) and 1 <= level <= 2:
                self._data['emotion_level'] = level
        else:
            logging.warning('Unknown emotion: %s' % str(emotion))

        return self

    def pitch(self, pitch):
        if isinstance(pitch, int):
            if pitch < 50:
                pitch = 50
            elif 200 < pitch:
                pitch = 200
            self._data['pitch'] = pitch

        return self

    def speed(self, speed):
        if isinstance(speed, int):
            if speed < 50:
                speed = 50
            elif 400 < speed:
                speed = 400
            self._data['speed'] = speed

        return self

    def volume(self, volume):
        if isinstance(volume, int):
            if volume < 50:
                volume = 50
            elif 200 < volume:
                volume = 200
            self._data['volume'] = volume

        return self

    def to_wave(self, text):
        self._data['text'] = text
        logging.debug('Post: %s' % str(self._data))
        request = requests.post(self.URL, self._data, auth=self._auth)
        logging.debug('Status: %d' % request.status_code)
        if request.status_code != requests.codes.ok:
            raise Exception('Invalid status code: %d' % request.status_code)
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
            data = temp.readframes(min(data, self.CHUNK))
        stream.close()
        temp.close()


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description=VoiceTexter.__name__)
    parser.add_argument('--user', type=str, default='', help='user name')
    args, unknown = parser.parse_known_args()

    vt = VoiceTexter(user_name=args.user)
