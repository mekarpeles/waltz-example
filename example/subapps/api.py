#-*- coding: utf-8 -*-

"""
    subapps.api
    ~~~~~~~~~~~
"""

from waltz import web
import json
from configs.config import server

urls = ("/v([0-9])/(.*/.*/.*)/([0-9]+)/?", "Api",
        "/v([0-9])/(.*/.*)/([0-9]+)/?", "Api",
        "/v([0-9])/(.*)/([0-9]+)/?", "Api")

#apis = {"v1": {"api": lambda api_id: Api(api_id)._clean_keys()}}

class Api:
    def GET (self, version, api, api_id):
        i = web.input(token=None)
        web.header('Content-Type', 'application/json')
        web.header('Access-Control-Allow-Origin', '*')
        
        ## Enforce https
        # TODO: sever SSL_ENABLED flag
        #if not web.ctx.protocol == "https":
        #    raise web.seeother("/404")

        ## Only allow verified users
        # TODO: Standardize errors
        if not i.token and i.token != server['secret']:
            return json.dumps({"error": "Unauthorized access, attempt logged"})
        return json.dumps({"error": "No data source available"})
        #return json.dumps(apis[version][api](api_id))

    def POST(self, api, api_id):
        pass

subapp = web.application(urls, globals())
