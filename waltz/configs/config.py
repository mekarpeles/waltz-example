# -*- coding: utf-8 -*-
"""
    config.py
    ~~~~~~~~~

    This module is the middle man for handling/consolidating
    configurations for the Dungeons project.

    :copyright: (c) 2012 by Mek
    :license: BSD, see LICENSE for more details.
"""

import ConfigParser
from os import getcwd

config = ConfigParser.ConfigParser()

try:
    with open('configs/server.cfg') as f: pass
    config.read('configs/server.cfg')
except IOError as e:
    config.read('configs/server_defaults.cfg')

server = {"debug_mode": bool(config.get("server", "debug")),
          "secret": config.get("server", "secret"),
          "paths": {"~": getcwd(),
                    "sessions": config.get("paths", "sessions"),
                    "db": config.get("paths", "db")
                    }
          }
