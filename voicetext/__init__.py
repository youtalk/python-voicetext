#!/usr/bin/env python3
import json
import logging
import os
import os.path
import wave
from typing import Optional

import requests
from playsound import playsound
from requests.auth import HTTPBasicAuth


class VoiceTextException(Exception):
    pass


class VoiceText:
    """
    Speech synthesizer by VoiceText Web API
    """

    URL = "https://api.voicetext.jp/v1/tts"
    CHUNK_SIZE = 1024

    def __init__(self, api_key: str = "", speaker: str = "hikari") -> None:
        """
        :param password: Auth password of VoiceText Web API
        :param speaker: Speaker name
        """
        self._auth = HTTPBasicAuth(api_key, "")
        self._default_speaker = speaker
        self._data = {"speaker": self._default_speaker}

        logging.basicConfig(level=logging.INFO)
        self._logger = logging.getLogger(__name__)

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

    def to_wave(self, text: str) -> Optional[bytearray]:
        """
        Convert text to wave binary.
        :param text: Text to synthesize
        """
        self._data["text"] = text
        self._logger.debug("Post: %s" % str(self._data))
        request = requests.post(self.URL, self._data, auth=self._auth)
        self._logger.debug("Status: %d" % request.status_code)
        if request.status_code != requests.codes.ok:
            return None
        return request.content

    def speak(self, text: str) -> None:
        """
        Speak text.
        :param text: Text to synthesize
        """
        self._data["text"] = text
        path = "/tmp/voicetext_%s.wav" % hash(json.dumps(self._data))
        if not os.path.exists(path):
            # Cache is not found
            w = self.to_wave(text)
            if w is not None:
                with open(path, "wb") as temp:
                    temp.write(w)

        playsound(path)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description=VoiceText.__name__)
    parser.add_argument("--api-key", type=str, default="", help="API key")
    args, unknown = parser.parse_known_args()

    vt = VoiceText(api_key=args.api_key)
