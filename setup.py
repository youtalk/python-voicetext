# -*- coding: utf-8 -*-
from setuptools import find_packages, setup

version = "0.3.1"

setup(
    name="python-voicetext",
    version=version,
    license="Apache License 2.0",
    description="Voice synthesiser using VoiceText Web API",
    long_description="See also https://github.com/youtalk/python-voicetext#readme",
    author="Yutaka Kondo",
    author_email="yutaka.kondo@youtalk.jp",
    url="https://github.com/youtalk/python-voicetext",
    packages=find_packages(),
    download_url="https://github.com/youtalk/python-voicetext/releases/tag/" + version,
    install_requires=["requests", "playsound"],
    platforms=["POSIX", "Mac OS X", "Windows"],
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Multimedia :: Sound/Audio",
    ],
)
