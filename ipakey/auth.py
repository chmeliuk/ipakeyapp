# -*- coding: utf-8 -*-

import kerberos
import subprocess
import settings


class IpaAuth(object):
    def __init__(self, hostname):
        self.hostname = hostname
        self.access_key = self.authenticate()

    def authenticate(self):
        if not has_kerberos_ticket():
            create_kerberos_ticket()

        gss_flags = kerberos.GSS_C_MUTUAL_FLAG | kerberos.GSS_C_SEQUENCE_FLAG
        _ignore, context = kerberos.authGSSClientInit('HTTP@' + self.hostname, gssflags=gss_flags)
        _ignore = kerberos.authGSSClientStep(context, '')
        response = kerberos.authGSSClientResponse(context)

        return response


def has_kerberos_ticket():
    return True if subprocess.call(['/usr/bin/klist', '-s']) == 0 else False


def create_kerberos_ticket():
    kinit_args = ['/usr/bin/kinit', '%s@%s' % ('admin', 'SF')]
    kinit = subprocess.Popen(kinit_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    kinit.stdin.write('%s\n' % settings.PASSWORD)
    kinit.wait()
