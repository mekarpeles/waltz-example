#-*- coding: utf-8 -*-

"""
    waltz
    ~~~~~

    Setup
    `````

    $ pip install waltz    
"""

from distutils.core import setup

setup(
    name='waltz',
    version='0.1.3',
    url='http://github.com/mekarpeles/waltz',
    author='mek',
    author_email='michael.karpeles@gmail.com',
    packages=[
        'waltz',
        'waltz.ballroom',
        'waltz.configs',
        'waltz.templates',
        'waltz.subapps',
        'waltz.routes',
        'waltz.test'
        ],
    platforms='any',
    scripts=[],
    license='LICENSE',
    install_requires=[
        'lazydb >= 0.1.4',
        'web.py >= 0.36',
        'nose >= 1.1.2'
    ],
    description="Waltz is a web.py framework for designing web apps in 3/4 time.",
    long_description=open('README.md').read(),
)
