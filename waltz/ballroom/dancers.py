#-*- coding: utf-8 -*-

"""
    ballroom.dancers
    ~~~~~~~~~~~~~~~~    
"""

import web

class Coreographer(object):
    @property
    def session(self):
        return web.ctx.session

    @property
    def render(self):
        return web.ctx.render

session = Coreographer().session
render = Coreographer().render
