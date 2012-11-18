#-*- coding: utf-8 -*-

"""
    ballroom.setup
    ~~~~~~~~~~~~~~
    Setup webpy app with additional waltz;
    Sessions and authentication, templates, etc.
"""

from configs.config import server

def dancefloor(web, urls, sessions=False, autoreload=False):
    app = web.application(urls, globals(), autoreload=autoreload)

    _globals = {'ctx': web.ctx,}
    slender  = web.template.render('templates/', globals=_globals)
    render  = web.template.render('templates/', base='base', globals=_globals)
    _globals['render'] = render

    if sessions:
        storage_method = web.session.DiskStore(server['paths']['sessions'])
        session = start_sessions(web, app, storage_method)        
        def session_hook(): web.ctx.session = session
        app.add_processor(web.loadhook(session_hook))

    def render_hook(): web.ctx.render = render
    app.add_processor(web.loadhook(render_hook))
    return app


def start_sessions(web, app, storage_method, **kwargs):
    web.config.session_parameters['ignore_expiry'] = False

    def default_session(web_session):
        default_session = {'logged': False,
                           'username': ''
                           }
        web_session.update(default_session)
    session = web.session.Session(app, storage_method, initializer=default_session)
    return session
