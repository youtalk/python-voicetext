python-voicetext
================

Voice synthesiser using [VoiceText Web API](https://cloud.voicetext.jp/webapi)

To use this software, first you need to [complete the user registration](https://cloud.voicetext.jp/webapi/api_keys/new) and get the API key.

Installation
------------

~~~sh
$ pip3 install python-voicetext
~~~

or

~~~sh
$ git clone git@github.com:youtalk/python-voicetext.git
$ cd python-voicetext
$ pipenv install
$ pipenv shell
$ python3 setup.py install
~~~

Usage
-----

~~~sh
$ python3
>> from voicetext import VoiceText
>> vt = VoiceText("YOUR_API_KEY")
>> vt.speak("こんにちは。")
>> vt.speaker = "takeru"
>> vt.emotion = "angry"
>> vt..speak("こんばんは。")
>> with open("greet.wav", "wb") as f:
.... f.write(vt.to_wave("おはよう。"))
~~~

For more information, see also [test/test_voicetext.py](https://github.com/youtalk/python-voicetext/blob/master/test/test_voicetext.py)
