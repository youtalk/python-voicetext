voicetext4py
===========

Voice synthesiser with [VoiceText Web API](https://cloud.voicetext.jp/webapi)

To use this software, first you need to complete the user registration and get the API key.

Dependencies
------------

### Ubuntu

~~~sh
$ sudo apt-get install python-pyaudio
$ sudo pip install -U requests
~~~

### OSX

~~~sh
$ brew install portaudio
$ sudo pip install -U requests
$ sudo pip install -U PyAudio --allow-external PyAudio --allow-unverified PyAudio
~~~

Usage
-----

~~~sh
$ ipython -i voicetext.py -- --user YOUR_API_KEY
>> vt.speak('こんにちは。')
>> vt.speaker('takeru').emotion('angry').speak('こんばんは。')
>> with open('greet.wav', 'wb') as f:
.... f.write(vt.to_wave('おはよう。'))
~~~
