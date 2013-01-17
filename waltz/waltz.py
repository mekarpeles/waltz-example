#-*- coding: utf-8 -*-

"""
    waltz
    ~~~~~

    Waltz is a web.py framework for designing web apps in 3/4
    time. Waltz comes pre-configured and includes features like
    out-of-the-box support for analytics tracking. Waltz and never miss
    a beat.

    :copyright: (c) 2012 by Mek
    :license: BSD, see LICENSE for more details.
"""

import web
from subapps import api
from routes import *
from ballroom import setup
from configs.config import server

if server['debug_mode']:
    from reloader import PeriodicReloader

# consider moving urls to ballroom
urls = ('/api', api.subapp,
        '/cart/?', 'routes.cart.Cart',
        '/login/?', 'routes.auth.Login',
        '/logout/?', 'routes.auth.Logout',
        '/register/?', 'routes.auth.Register',
        '/account/?', 'routes.account.Account',
        '/analytics/?', 'routes.analytics.Analytics',
        '/404', 'routes.responses.NotFound',
        '/', 'routes.home.Index',
        '(.*)', 'routes.responses.NotFound')

ballroom = setup.dancefloor(web, urls, sessions=True, autoreload=False)

if __name__ == "__main__":
    if server['debug_mode']:
        PeriodicReloader()
    ballroom.run()
