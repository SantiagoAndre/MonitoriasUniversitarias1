from graphene_django import DjangoObjectType
from graphene import relay, Node

from apps.api_graphql.connections import TotalCountConnection
from apps.monitor.models import Monitor


class MonitorNode(DjangoObjectType):
    class Meta:
        model = Monitor
        interfaces = (Node, )
        exclude_fields = ('is_staff', 'is_superuser', 'last_login', 'is_active', 'date_joined',
                          'password', 'username')
        filter_fields = ['first_name', 'last_name', 'subject__name', 'email']
        filter_fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact','icontains'],
            'email': ['exact'],
            'subject__name': ['exact', 'icontains','istartswith'],
        }
        connection_class = TotalCountConnection