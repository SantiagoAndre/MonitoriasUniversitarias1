from django.utils.translation import gettext_lazy as _


class NameAlreadyUsedException(Exception):
    pass

class MonitorLen(Exception):
    pass

class ValidationError(Exception):
    pass
