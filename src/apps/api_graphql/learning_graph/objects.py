from graphene.relay import Node
from graphene_django import DjangoObjectType
from apps.api_graphql.connections import TotalCountConnection

from apps.learning_graph.models import LearningLine


class LearningLineNode(DjangoObjectType):

    class Meta:
        model = LearningLine
        filter_fields = ['name']
        interfaces = (Node, )
        connection_class = TotalCountConnection

