#-*- coding: utf-8 -*-

"""
    routes.analytics
    ~~~~~~~~~~~~~~~~
    Authentication routes - login, logout
"""

import web
from ballroom.decorations import track
from ballroom.dancers import session, render, User
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

        u = User.register(i.username, i.password, email=i.email)

        if User.authenticate(i.username, i.password, u.salt, u.uhash):
            # Logic to populate session with user vars:
            session.logged = True
            session.username = i.username

            # migrate elsewhere, maybe utils redir
            if i.redir:
                if not i.redir[0] == "/":
                    i.redir = "/" + i.redir
                elif i.redir[0] == "/":
                    i.redir = "/"
                raise web.seeother(web.ctx.homedomain + i.redir)
            raise web.seeother(web.ctx.homedomain + "/account")
        return render.login(msg=ERROR_LOGIN_PASSWD['key'])


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
        if session.logged:
            raise web.seeother('/account')
        return render.auth.register()

    def POST(self):
        i = web.input(username='', email='', passwd1='', passwd2='',
                      redir='')
        u = User.register(i.username, i.passwd1, i.passwd2, i.email)
        session.logged = True
        session.username = u['name']
        return u
        # replace above return statement with the following redirect
        # once you've added this newly registered user into your
        # queryable Users database 
        #raise web.seeother('/account')
