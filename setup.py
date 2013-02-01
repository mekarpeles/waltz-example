#-*- coding: utf-8 -*-

"""
    ballet
    ~~~~~~
    Ballet is an example waltz application

    Setup
    `````
    $ sudo pip install -e .
"""

from distutils.core import setup

setup(
    name='ballet',
    version='0.1.62',
    url='http://github.com/mekarpeles/waltz-example',
    author='mek',
    author_email='michael.karpeles@gmail.com',
    packages=[
        'example',
        'example.routes',
        'example.subapps'
        ],
    platforms='any',
    scripts=[],
    license='LICENSE',
    install_requires=[
        'waltz >= 0.1.62'
    ],
    description="Example Waltz Application - Waltz is a web.py framework for designing web apps in 3/4 time.",
    long_description=open('README.txt').read(),
)
