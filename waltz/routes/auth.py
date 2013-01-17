#-*- coding: utf-8 -*-

"""
    routes.analytics
    ~~~~~~~~~~~~~~~~
    Authentication routes - login, logout
"""

import web
from ballroom import security
from ballroom.decorations import track
from ballroom.dancers import session, render
from configs.config import server

# Events (message/responses)
ALREADY_LOGGED = server['responses']['WARNING']['ALREADY_LOGGED']
LOGGED_OUT = server['responses']['SUCCESS']['LOGGED_OUT']

def redir2login(redir="/", msg=""):
    if web.ctx.homedomain:
        return web.seeother("{}/login?redir={}".format(web.ctx.homedomain, redir))
    return web.notfound()

class Login:
    @track
    def GET(self):
        ## TODO: Enforce https
        #redirect2https(web.ctx, '/login')
        i = web.input(msg="", redir="", err="")
        if session.logged:
            return render.auth.login(resp=ALREADY_LOGGED)
        return render.auth.login()

    def POST(self):
        i = web.input(username='', email='', password='', redir='/')
        i.email = i.email.lower()

        ## Implement your own logic here:
        #if (i.email and i.password) and auth_api._email_registered(i.email):
        #    if auth_api._passwords_match(i.email, i.password):
        #        session = auth_api._update_session_login(session, i.email)
        #        if i.redir:
        #            if not i.redir[0] == "/":
        #                i.redir = "/" + i.redir
        #            elif i.redir[0] == "/":
        #                i.redir = "/"
        #            raise web.seeother(web.ctx.homedomain + i.redir)
        #        else:
        #            raise web.seeother(web.ctx.homedomain + "/account/bookshelf")
        #    return render.login(msg=ERROR_LOGIN_PASSWD['key'])
        #return render.login(msg=ERROR_ACT_CREDS['key'])

        session.logged = True
        session.username = i.username
        raise web.seeother('/account')

class Logout:
    @track
    def GET(self):
        i = web.input(redir='')
        session.logged = False
        session.username= ''
        session.kill()
        if i.redir:
            raise web.seeother(i.redir)
        #raise redir2login(redir='/login')
        return render.auth.login(resp=LOGGED_OUT)

class Register:
    @track
    def GET(self):
        i = web.input(redir='')
        return render.auth.register()

    def POST(self):
        i = web.input(username='', email='', passwd1='', passwd2='',
                      redir='')
        return render.generic("registration workflow incomplete", "Registration backend coming soon, thanks for your patience!")
