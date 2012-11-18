#-*- coding: utf-8 -*-

"""
    routes.analytics
    ~~~~~~~~~~~~~~~~
    Authentication routes - login, logout
"""

import web
from ballroom.decorations import track
from ballroom.dancers import session, render
from configs.config import server

def redir2login(redir="/", msg=""):
    if web.ctx.homedomain:
        return web.seeother("%s/login?redir=%s" % (web.ctx.homedomain, redir))
    return web.notfound()

class Login:
    @track
    def GET(self):
        ## TODO: Enforce https
        #redirect2https(web.ctx, '/login')
        i = web.input(msg="", redir="", err="")
        if session().logged:
            return "Already logged in"
        return "TODO Login page"

    def POST(self):
        i = web.input(username='', email='', password='', redir='/')
        i.email = i.email.lower()

        ## Implement your own logic here:
        #if (i.email and i.password) and auth_api._email_registered(i.email):
        #    if auth_api._passwords_match(i.email, i.password):
        #        web.ctx.session['session'] = auth_api._update_session_login(SESSION(), i.email)
        #        if i.redir:
        #            if not i.redir[0] == "/":
        #                i.redir = "/" + i.redir
        #            elif i.redir[0] == "/":
        #                i.redir = "/"
        #            raise web.seeother(web.ctx.homedomain + i.redir)
        #        else:
        #            raise web.seeother(web.ctx.homedomain + "/account/bookshelf")
        #    return RENDER().login(msg=ERROR_LOGIN_PASSWD['key'])
        #return RENDER().login(msg=ERROR_ACT_CREDS['key'])

        web.ctx.session().logged = True
        web.ctx.session().username = i.username
        raise web.seeother('/')

class Logout:
    @track
    def GET(self):
        i = web.input(redir='')
        session().logged = False
        session().username= ''
        session().kill()
        if i.redir:
            raise web.seeother(i.redir)
        raise redir2login(redir='/login')
