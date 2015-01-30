python-voicetext
================

Voice synthesiser using [VoiceText Web API](https://cloud.voicetext.jp/webapi)

To use this software, first you need to [complete the user registration](https://cloud.voicetext.jp/webapi/api_keys/new) and get the API key.

Installation
------------

~~~sh
$ pip install python-voicetext
~~~

or

~~~sh
$ python setup.py install
~~~

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

For more information, see also [test/test_voicetext.py](https://github.com/youtalk/python-voicetext/blob/master/test/test_voicetext.py)
