#-*- coding: utf-8 -*-

"""
    ballroom.decorations
    ~~~~~~~~~~~~~~~~~~~~
    A collection of route decorators

    :authors Mek
    :license pending
"""

import web
from copy import copy
from lazydb.lazydb import Db
from configs.config import server

def track(fn):
    """A decorator which wraps each route with analytics tracking."""
    def tracked(fn):
        """This setup w/ second inner function allows support for
        passing @track optional arguments and parameters, as well as
        allows for the special case of class methods which require
        self - methods(self).
        """        
        def inner(*args, **kwargs):
            """Copy web context environment, clean it to avoid
            pickeling issues, and dump it to lazydb before returning
            the route
            """
            db = Db(server['paths']['db'])
            ctx = copy(web.ctx['env'])
            del ctx['wsgi.errors']
            del ctx['wsgi.input']
            db.append('analytics', ctx)
            return fn(*args, **kwargs)        
        return inner
    return tracked(fn)
