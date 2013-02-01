#-*- coding: utf-8 -*-

"""
    routes.responses
    ~~~~~~~~~~~~~~~~
    Handles static responses like 404
"""

import web

class NotFound:
    def GET(self, err=None):
        raise web.notfound("404")
