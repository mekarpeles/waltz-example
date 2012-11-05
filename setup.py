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
    version='0.1.1',
    url='http://github.com/mekarpeles/waltz',
    author='mek',
    author_email='michael.karpeles@gmail.com',
    packages=['waltz', 'waltz.test'],
    platforms='any',
    install_requires=[
        'lazydb>=0.1.4',
        'web>=0.36',
        'nose>=1.1.2'
    ],
    scripts=[],
    license='LICENSE',
    description="Waltz is a web.py framework for designing web apps in 3/4 time.",
    long_description=open('README.md').read(),
)
