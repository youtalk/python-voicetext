voicetext4py
===========

Voice synthesiser with [VoiceText Web API](https://cloud.voicetext.jp/webapi)

To use this software, first you need to complete the user registration and get the API key.

Installation
------------

~~~sh
$ sudo apt-get install python-pyaudio
$ sudo pip install -U requests
~~~

Usage
-----

~~~sh
$ ipython -i voicetext.py -- --user YOUR_API_KEY
>> vt.speak('こんにちは。')
>> vt.speaker('takeru').emotion('angry').speak('こんばんは。')
~~~
