# -*- coding: utf-8 -*-
from setuptools  import setup

setup(name='python-voicetext',
      version='0.1',
      license='Apache License 2.0',
      description='Python library of VoiceText Web API',
      author='Yutaka Kondo',
      author_email='yutaka.kondo@youtalk.jp',
      url='https://github.com/youtalk/python-voicetext',
      packages=['voicetext'],
      download_url='https://github.com/youtalk/python-voicetext/releases/tag/0.1',
      requires=['requests', 'PyAudio'],
      platforms = ['POSIX', 'Mac OS X', 'Windows'],
)
