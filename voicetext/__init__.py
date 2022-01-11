#!/usr/bin/env python3
import json
import logging
import os
import os.path
import wave
from typing import Optional

import pyaudio
import requests
from requests.auth import HTTPBasicAuth


class VoiceTextException(Exception):
    pass


class VoiceText:
    """
    Speech synthesizer by VoiceText Web API
    """

    URL = "https://api.voicetext.jp/v1/tts"
    CHUNK = 1024
    _audio = pyaudio.PyAudio()

    def __init__(
        self, user_name: str = "", password: str = "", speaker: str = "hikari"
    ) -> None:
        """
        :param user_name: Auth user name of VoiceText Web API
        :param password: Auth password of VoiceText Web API
        :param speaker: Speaker name
        """
        self._auth = HTTPBasicAuth(user_name, password)
        self._default_speaker = speaker
        self._data = {"speaker": self._default_speaker}

        logging.basicConfig(level=logging.INFO)
        self._logger = logging.getLogger(__name__)

        try:
            self.to_wave("test")
        except VoiceTextException:
            raise VoiceTextException("HTTP basic auth error")

    @property
    def logger(self) -> logging.Logger:
        return self._logger

    @logger.setter
    def logger(self, logger: logging.Logger) -> None:
        self._logger = logger

    def restore_default(self) -> None:
        """
        Restore default parameters.
        """
        self._data = {"speaker": self._default_speaker}

    @property
    def speaker(self) -> str:
        return self._data["speaker"]

    @speaker.setter
    def speaker(self, speaker: str) -> None:
        if speaker in ["show", "haruka", "hikari", "takeru", "santa", "bear"]:
            self._data["speaker"] = speaker
        else:
            self._logger.warning("Invalid speaker: %s" % str(speaker))

    @property
    def emotion(self) -> Optional[str]:
        return self._data.get("emotion")

    @emotion.setter
    def emotion(self, emotion: str) -> None:
        if emotion in ["happiness", "anger", "sadness"]:
            self._data["emotion"] = emotion
        else:
            self._logger.warning("Invalid emotion: %s" % str(emotion))

    @property
    def emotion_level(self) -> int:
        return self._data["emotion_level"] if "emotion_level" in self._data else 2

    @emotion_level.setter
    def emotion_level(self, level: int) -> None:
        if 1 <= level <= 4:
            self._data["emotion_level"] = level
        else:
            self._logger.warning(f"Invalid emotion_level: {level}")

    @property
    def pitch(self) -> int:
        return self._data["pitch"] if "pitch" in self._data else 100

    @pitch.setter
    def pitch(self, pitch: int) -> None:
        if pitch < 50:
            pitch = 50
        elif 200 < pitch:
            pitch = 200
        self._data["pitch"] = pitch

    @property
    def speed(self) -> int:
        return self._data["speed"] if "speed" in self._data else 100

    @speed.setter
    def speed(self, speed: int) -> None:
        if speed < 50:
            speed = 50
        elif 400 < speed:
            speed = 400
        self._data["speed"] = speed

    @property
    def volume(self) -> int:
        return self._data["volume"] if "volume" in self._data else 100

    @volume.setter
    def volume(self, volume: int):
        if volume < 50:
            volume = 50
        elif 200 < volume:
            volume = 200
        self._data["volume"] = volume

    def to_wave(self, text: str) -> bytearray:
        """
        Convert text to wave binary.
        :param text: Text to synthesize
        """
        self._data["text"] = text
        self._logger.debug("Post: %s" % str(self._data))
        request = requests.post(self.URL, self._data, auth=self._auth)
        self._logger.debug("Status: %d" % request.status_code)
        if request.status_code != requests.codes.ok:
            raise VoiceTextException("Invalid status code: %d" % request.status_code)
        return request.content

    def speak(self, text: str) -> None:
        """
        Speak text.
        :param text: Text to synthesize
        """
        self._data["text"] = text
        path = "/tmp/voicetext_%s.wav" % hash(json.dumps(self._data))
        if not os.path.exists(path):
            # cache not found
            w = self.to_wave(text)
            with open(path, "wb") as temp:
                temp.write(w)

        temp = wave.open(path)
        stream = self._audio.open(
            format=self._audio.get_format_from_width(temp.getsampwidth()),
            channels=temp.getnchannels(),
            rate=temp.getframerate(),
            output=True,
        )
        data = temp.readframes(self.CHUNK)
        while data:
            stream.write(data)
            data = temp.readframes(min(data, self.CHUNK))
        stream.close()
        temp.close()


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=VoiceText.__name__)
    parser.add_argument("--user", type=str, default="", help="user name")
    args, unknown = parser.parse_known_args()

    vt = VoiceText(user_name=args.user)
