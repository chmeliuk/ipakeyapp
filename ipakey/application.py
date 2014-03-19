# -*- coding: utf-8 -*-

import os
import settings
from handler import handlers
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


def run():
    os.environ['KRB5_CLIENT_KTNAME'] = settings.KRB5_CLIENT_KTNAME

    application = tornado.web.Application(handlers)
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(settings.APPLICATION_PORT)
    tornado.ioloop.IOLoop.instance().start()
