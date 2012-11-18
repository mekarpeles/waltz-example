#-*- coding: utf-8 -*-

"""
    routes.home
    ~~~~~~~~~~~
    Homepage routes
"""

import web
from ballroom.decorations import track
from ballroom.dancers import session, render

class Index:
    @track
    def GET(self):
        return render().index()
