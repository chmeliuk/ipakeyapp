# -*- coding: utf-8 -*-

from ipakey import application
from tornado.options import define, options, parse_command_line


define('port', default=8888, help="port to listen on")
define('address', default='127.0.0.1', help="address to listen on")

if __name__ == "__main__":
    parse_command_line(final=False)
    application.run(options)