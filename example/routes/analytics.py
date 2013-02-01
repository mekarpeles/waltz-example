#-*- coding: utf-8 -*-

"""
    routes.analytics
    ~~~~~~~~~~~~~~~~
    Analytics routes
"""

import web
from lazydb.lazydb import Db
from configs.config import server

class Analytics:

    def GET(self):
        """Add your own key in server config"""
        web.header('Content-Type', 'application/json')
        i = web.input(key="")
        if i.key == server['secret']:
            db = Db(server['paths']['db'])
            return db.get('analytics')
