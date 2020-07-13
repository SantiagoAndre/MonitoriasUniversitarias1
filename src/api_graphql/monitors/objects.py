from graphene.relay import Node
from graphene_django import DjangoObjectType

from monitors.models import College
from monitors.models import Career
from monitors.models import City
from monitors.models import Contact
from monitors.models import Monitor
from monitors.models import Service
from monitors.models import Skill
from monitors.models import Client
from monitors.models import Quoation
from api_graphql.connections import TotalCountConnection

# Create your objects types here.


class CollegeNode(DjangoObjectType):

    class Meta:
        model = College
        filter_fields = ['name']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class CareerNode(DjangoObjectType):

    class Meta:
        model = Career
        filter_fields = ['name', 'description']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class CityNode(DjangoObjectType):

    class Meta:
        model = City
        filter_fields = ['name']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class ContactNode(DjangoObjectType):

    class Meta:
        model = Contact
        filter_fields = ['address', 'phone', 'family_phone']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class MonitorNode(DjangoObjectType):

    class Meta:
        model = Monitor
        filter_fields = ['first_name', 'last_name', 'email']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class ServiceNode(DjangoObjectType):

    class Meta:
        model = Service
        filter_fields = ['name']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class SkillNode(DjangoObjectType):

    class Meta:
        model = Skill
        filter_fields = ['name']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class ClientNode(DjangoObjectType):

    class Meta:
        model = Client
        filter_fields = ['first_name', 'last_name', 'email']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class QuoationNode(DjangoObjectType):

    class Meta:
        model = Quoation
        filter_fields = ['acepted', 'created', 'expiration', 'delivery', 'price']
        interfaces = (Node, )
        connection_class = TotalCountConnection
