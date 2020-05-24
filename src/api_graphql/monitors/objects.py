from graphene.relay import Node
from graphene_django import DjangoObjectType

from monitors.models import College
from monitors.models import CollegeCareer
from monitors.models import Monitor
from monitors.models import LearningLine
from monitors.models import Topic
from monitors.models import Subtopic
from monitors.models import Service
from monitors.models import Quotation
from monitors.models import Poll
from api_graphql.connections import TotalCountConnection

# Create your objects types here.


class CollegeNode(DjangoObjectType):

    class Meta:
        model = College
        filter_fields = ['name']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class CollegeCareerNode(DjangoObjectType):

    class Meta:
        model = CollegeCareer
        filter_fields = ['name']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class MonitorNode(DjangoObjectType):

    class Meta:
        model = Monitor
        filter_fields = ['name']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class LearningLineNode(DjangoObjectType):

    class Meta:
        model = LearningLine
        filter_fields = ['name']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class TopicNode(DjangoObjectType):

    class Meta:
        model = Topic
        filter_fields = ['name']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class SubtopicNode(DjangoObjectType):

    class Meta:
        model = Subtopic
        filter_fields = ['name']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class ServiceNode(DjangoObjectType):

    class Meta:
        model = Service
        filter_fields = ['name']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class QuotationNode(DjangoObjectType):

    class Meta:
        model = Quotation
        # filter_fields = ['']
        interfaces = (Node, )
        connection_class = TotalCountConnection


class PollNode(DjangoObjectType):

    class Meta:
        model = Poll
        # filter_fields = []
        interfaces = (Node, )
        connection_class = TotalCountConnection
