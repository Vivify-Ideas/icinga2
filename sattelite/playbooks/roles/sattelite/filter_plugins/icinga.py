#!/usr/bin/python
from ansible.errors import AnsibleError


def icinga_ticket(value, salt):
    try:
        from pbkdf2 import PBKDF2
    except ImportError:
        raise AnsibleError('pbkdf2 library is required for `icinga_ticket` filter "pip install pbkdf2"')
    return PBKDF2(str(value), str(salt), iterations=50000).hexread(20)


class FilterModule(object):
    def filters(self):
        return dict(
            icinga_ticket=icinga_ticket,
        )