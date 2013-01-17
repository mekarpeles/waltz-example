#-*- coding: utf-8 -*-

"""
    routes.account
    ~~~~~~~~~~~~~~
    Account pages for logged in users
"""

import web
from lazydb.lazydb import Db
from ballroom.dancers import session, render # rename to choreographer
from ballroom.treasury import Product, Coupon
from configs.config import server

class Cart:
    def GET(self):
        i = web.input(op=None, ref=None, qty=1)
        if i.ref:
            pid = long(i.ref)
        if i.op == "coupon":
            session.cart.coupon = Coupon(1, "1010", percent_off=10,
                                         value_off="200.00")
        if i.op == "add" and pid:
            # XXX Replace Product with some product retrieved from listing
            # XXX Must sanitize + normalize pid, assert not None in treasury
            p = Product(pid, "Example Product", price="1.00")
            session.cart.add(p)
        if i.op == "remove" and pid:
            # BROKEN!!!
            session.cart.remove(pid)
        if i.op == "reset":
            session.cart.empty()
        return session.cart

    def POST(self):
        pass
