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
    version='0.1.2',
    url='http://github.com/mekarpeles/waltz',
    author='mek',
    author_email='michael.karpeles@gmail.com',
    packages=['waltz', 'waltz.test'],
    platforms='any',
    install_requires=[
        'lazydb>=0.1.4'
    ],
    scripts=[],
    license='LICENSE.txt',
    description="",
    long_description=open('README.txt').read(),
)
