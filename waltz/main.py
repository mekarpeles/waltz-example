#-*- coding: utf-8 -*-

"""
    main.py
    ~~~~~~~

    Waltz is a web.py framework for designing web apps in 3/4
    time. Waltz comes pre-configured and includes features like
    out-of-the-box support for analytics tracking. Waltz and never miss
    a beat.

    :copyright: (c) 2012 by Mek
    :license: BSD, see LICENSE for more details.
"""

import web
from reloader import PeriodicReloader
from configs.config import server

urls = ('/', 'Index',
        '/404', 'NotFound',
        '(.*)', 'NotFound')

app = web.application(urls, globals(), autoreload=False)

_globals = {'ctx': web.ctx}
slender  = web.template.render('templates/', globals=_globals)
render  = web.template.render('templates/', base='base', globals=_globals)

def track(fn):
    """A decorator which wraps each route with analytics tracking."""
    def tracked(fn):
        """This setup w/ second inner function allows support for
        passing @track optional arguments and parameters, as well as
        allows for the special case of class methods which require
        self - methods(self).
        """
        print web.ctx
        def inner(*args, **kwargs):
            return fn(*args, **kwargs)
        return inner
    return tracked(fn)

class Index:

    @track
    def GET(self):
        return render.index()

class NotFound:
    def GET(self, err=None):
        raise web.notfound('')

if __name__ == "__main__":
    if server['debug_mode']:
        PeriodicReloader()
    app.run()
