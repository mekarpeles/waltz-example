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

    _globals = {'ctx': web.ctx}
    slender  = web.template.render('templates/', globals=_globals)
    render  = web.template.render('templates/', base='base', globals=_globals)
    _globals['render'] = slender

    if sessions:
        storage_method = web.session.DiskStore(server['paths']['sessions'])
        session = init_sessions(web, app, storage_method)
        def inject_session():
            """closure; uncalled function which wraps session is
            passed to the web loadhook and invoked elsewhere and at a
            later point in time
            """
            web.ctx.session = session
        app.add_processor(web.loadhook(inject_session))
        _globals['session'] = session

    def render_hook(): web.ctx.render = render
    app.add_processor(web.loadhook(render_hook))
    return app

def init_sessions(web, app, storage_method, **kwargs):
    web.config.session_parameters['ignore_expiry'] = True

    default_session = {'logged': False,
                       'username': '',
                       'uid': -1 # user id
                       }
    session = web.session.Session(app, storage_method, initializer=default_session)
    return session
