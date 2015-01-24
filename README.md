python-voicetext
===========

Voice synthesiser with [VoiceText Web API](https://cloud.voicetext.jp/webapi)

To use this software, first you need to [complete the user registration](https://cloud.voicetext.jp/webapi/api_keys/new) and get the API key.

Dependencies
------------

### Ubuntu

~~~sh
$ sudo apt-get install python-pyaudio
~~~

### OSX

~~~sh
$ brew install portaudio
~~~

Installation
------------

~~~sh
$ pip install -U -r requirements.txt
$ python setup.py install
~~~

Usage
-----

~~~sh
$ ipython
>> from voicetext import VoiceText
>> vt = VoiceText('YOUR_API_KEY')
>> vt.speak('こんにちは。')
>> vt.speaker('takeru').emotion('angry').speak('こんばんは。')
>> with open('greet.wav', 'wb') as f:
.... f.write(vt.to_wave('おはよう。'))
~~~
