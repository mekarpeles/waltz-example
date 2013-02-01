#-*- coding: utf-8 -*-

"""
    routes.cart
    ~~~~~~~~~~~
    Logic for interfacing with the shopping cart, if the route is
    enabled.    
"""

from waltz import web, track, session, render, Product, Coupon

class Cart:
    @track
    def GET(self):
        i = web.input(op=None, ref=None, qty=1)
        if i.ref:
            pid = long(i.ref)
        if i.op == "coupon":
            session().cart.coupon = Coupon(1, "1010", percent_off=10,
                                         value_off="200.00")
        if i.op == "add" and pid:
            # XXX Replace Product with some product retrieved from listing
            # XXX Must sanitize + normalize pid, assert not None in treasury
            p = Product(pid, "Example Product", price="1.00")
            session().cart.add(p)
        if i.op == "remove" and pid:
            session().cart.remove(pid)
        if i.op == "reset":
            session().cart.empty()
        return render().cart.index()

    def POST(self):
        pass
