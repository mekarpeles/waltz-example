#-*- coding: utf-8 -*-

"""
    ballroom.setup
    ~~~~~~~~~~~~~~
    Setup webpy app with additional waltz;
    Sessions and authentication, templates, etc.
"""

from configs.config import server

def dancefloor(web, urls, sessions=False, autoreload=False, **kwargs):
    """
    **kwargs:
        globals - a dict of vars or funcs which will be made globablly
                  available within the scope of html templates' context
        storage_method - can be overridden the web.session storage method
                         in the event the user prefers a DBStore
        session - a dictionary representing a default init'd session
    """
    app = web.application(urls, globals(), autoreload=autoreload) 
    
    env = {'ctx': web.ctx}
    env.update(kwargs.get('globals', {}))
    slender = web.template.render('templates/', globals=env)
    render = web.template.render('templates/', base='base', globals=env)
    env['render'] = slender

    def default_storage():
        return web.session.DiskStore(server['paths']['sessions'])

    if sessions is not False:
        store = kwargs.get('storage_method', default_storage())
        session = init_sessions(web, app, store, sessions)

        def inject_session():
            """closure; uncalled function which wraps session is
            passed to the web loadhook and invoked elsewhere and at a
            later point in time
            """
            web.ctx.session = session
        app.add_processor(web.loadhook(inject_session))
        env['session'] = session

    def render_hook(): web.ctx.render = render
    app.add_processor(web.loadhook(render_hook))
    return app

def init_sessions(web, app, store, session):
    """kwargs is used to inject options like 'cart' into session."""
    web.config.session_parameters['ignore_expiry'] = True
    return web.session.Session(app, store, initializer=session)
