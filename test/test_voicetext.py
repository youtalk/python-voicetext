#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import, division, print_function, unicode_literals

import unittest

from voicetext import VoiceText, VoiceTextException


class VoiceTextTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.vt = VoiceText("YOUR_API_KEY")

    def setUp(self):
        self.vt.restore_default()

    def test_speak(self):
        self.vt.speak("こんにちは。")

    def test_speak_speakers(self):
        self.vt.speaker("show").speak("ショウです。")
        self.vt.speaker("haruka").speak("ハルカです。")
        self.vt.speaker("hikari").speak("ヒカリです。")
        self.vt.speaker("takeru").speak("タケルです。")
        self.vt.speaker("santa").speak("サンタです。")
        self.vt.speaker("bear").speak("熊です。")

    def test_speak_emotions(self):
        self.vt.emotion("happiness").speak("喜び。")
        self.vt.emotion("anger").speak("怒り。")
        self.vt.emotion("sadness").speak("悲しみ。")

    def test_speak_pitches(self):
        for p in range(50, 201, 50):
            self.vt.pitch(p).speak("ピッチ%d" % p)

    def test_speak_speeds(self):
        for s in range(50, 401, 50):
            self.vt.speed(s).speak("スピード%d" % s)

    def test_speak_volumes(self):
        for v in range(50, 201, 50):
            self.vt.volume(v).speak("ボリューム%d" % v)


if __name__ == "__main__":
    unittest.main()
