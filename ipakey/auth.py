# -*- coding: utf-8 -*-

import kerberos


class IpaAuth(object):
    def __init__(self, hostname):
        self.hostname = hostname
        self.access_key = self.authenticate()

    def authenticate(self):
        gss_flags = kerberos.GSS_C_DELEG_FLAG | kerberos.GSS_C_MUTUAL_FLAG | kerberos.GSS_C_SEQUENCE_FLAG
        _ignore, context = kerberos.authGSSClientInit('HTTP@' + self.hostname, gssflags=gss_flags)
        _ignore = kerberos.authGSSClientStep(context, '')
        response = kerberos.authGSSClientResponse(context)

        return response