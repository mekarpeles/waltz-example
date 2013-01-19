#-*- coding: utf-8 -*-

"""
    ballroom.setup
    ~~~~~~~~~~~~~~
    Setup webpy app with additional waltz;
    Sessions and authentication, templates, etc.
"""

from configs.config import server

def dancefloor(web, urls, sessions=False, autoreload=False, **kwargs):
    app = web.application(urls, globals(), autoreload=autoreload)

    _globals = {'ctx': web.ctx,}
    slender  = web.template.render('templates/', globals=_globals)
    render  = web.template.render('templates/', base='base', globals=_globals)
    _globals['render'] = render

    def default_storage():
        return web.session.DiskStore(server['paths']['sessions'])

    if sessions is not False:
        store = kwargs.get('storage_method', default_storage())
        session = start_sessions(web, app, store)
        def session_hook(): web.ctx.session = session
        app.add_processor(web.loadhook(session_hook))

    def render_hook(): web.ctx.render = render
    app.add_processor(web.loadhook(render_hook))
    return app


def start_sessions(web, app, store, **kwargs):
    web.config.session_parameters['ignore_expiry'] = True
    default_session = {'logged': False,
                       'username': ''
                       }
    return web.session.Session(app, store, initializer=default_session)
