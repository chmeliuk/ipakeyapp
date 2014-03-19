# -*- coding: utf-8 -*-

from tornado.web import RequestHandler
import settings
from auth import IpaAuth


class MainHandler(RequestHandler):
    def get(self):
        ipa_auth = IpaAuth(settings.HOSTNAME)

        self.write(ipa_auth.access_key)


handlers = [
    (r"/access", MainHandler),
]