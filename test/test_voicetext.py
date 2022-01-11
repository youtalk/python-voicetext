#!/usr/bin/env python3
import unittest

from voicetext import VoiceText


class VoiceTextTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls._vt = VoiceText("YOUR_API_KEY")

    def setUp(self):
        self._vt.restore_default()

    def test_speak(self):
        self._vt.speak("こんにちは。")

    def test_speak_speakers(self):
        self._vt.speaker = "show"
        self._vt.speak("ショウです。")
        self._vt.speaker = "haruka"
        self._vt.speak("ハルカです。")
        self._vt.speaker = "hikari"
        self._vt.speak("ヒカリです。")
        self._vt.speaker = "takeru"
        self._vt.speak("タケルです。")
        self._vt.speaker = "santa"
        self._vt.speak("サンタです。")
        self._vt.speaker = "bear"
        self._vt.speak("熊です。")

    def test_speak_emotions(self):
        self._vt.emotion = "happiness"
        self._vt.speak("喜び。")
        self._vt.emotion = "anger"
        self._vt.speak("怒り。")
        self._vt.emotion = "sadness"
        self._vt.speak("悲しみ。")

    def test_speak_pitches(self):
        for p in range(50, 201, 50):
            self._vt.pitch = p
            self._vt.speak("ピッチ%d" % p)

    def test_speak_speeds(self):
        for s in range(50, 401, 50):
            self._vt.speed = s
            self._vt.speak("スピード%d" % s)

    def test_speak_volumes(self):
        for v in range(50, 201, 50):
            self._vt.volume = v
            self._vt.speak("ボリューム%d" % v)


if __name__ == "__main__":
    unittest.main()
