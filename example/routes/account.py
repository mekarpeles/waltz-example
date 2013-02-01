#-*- coding: utf-8 -*-

"""
    routes.account
    ~~~~~~~~~~~~~~
    Account pages for logged in users
"""

from waltz import web, session, render
from configs.config import server

class Account:

    def GET(self):
        if session().logged:
            return render().account.index()
        else:
            return render().generic("Permission Denied", 
                                    "Can't let you do that, " \
                                        "Starfox. Please " \
                                        "<a href='/login'>Login</a> " \
                                        "first.")
