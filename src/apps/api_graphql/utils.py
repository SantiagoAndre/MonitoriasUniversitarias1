from graphql_relay.node.node import from_global_id
from django.utils.translation import gettext_lazy as _

from apps.api_graphql.errors import InvalidIdException

# Functions utils


def transform_global_ids(**kwargs):
    for key, value in kwargs.items():

        if key.endswith('id'):
            try:
                new_value = from_global_id(value)[1]
                kwargs[key] = new_value
            except:
                raise InvalidIdException(
                    _("%s field contains invalid id" % key))
    return kwargs


def transform_global_ids_list(args):
    ids = []
    for value in args:
        # print(value)
        try:
            new_value = from_global_id(value)[1]
            ids.append(new_value)
        except:
            raise InvalidIdException(
                _("Subject field contains invalid id"))
    return ids


def delete_attributes_none(**kwargs):
    kwargs = {key: value for key, value in kwargs.items() if value is not None}
    return kwargs
