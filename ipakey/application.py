# -*- coding: utf-8 -*-

import os
import settings
from handler import handlers
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web


def run(opts):
    os.environ['KRB5_CLIENT_KTNAME'] = settings.KRB5_CLIENT_KTNAME

    application = tornado.web.Application(handlers)
    application.listen(opts.port, opts.address)
    tornado.ioloop.IOLoop.instance().start()
