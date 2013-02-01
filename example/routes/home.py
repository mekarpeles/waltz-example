#-*- coding: utf-8 -*-

"""
    routes.home
    ~~~~~~~~~~~
    Homepage routes
"""

from waltz import track, render

class Index:
    @track
    def GET(self):
        return render().index()
