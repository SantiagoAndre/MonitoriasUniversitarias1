from graphene.relay import Node
from graphene_django import DjangoObjectType
from apps.api_graphql.connections import TotalCountConnection

from apps.learning_graph.models import Subject

'''
class LearningLineNode(DjangoObjectType):

    class Meta:
        model = LearningLine 
        filter_fields = {'name': ('exact','icontains','istartswith')}
        interfaces = (Node, )
        connection_class = TotalCountConnection
'''

class SubjectNode(DjangoObjectType):

    class Meta:
        model = Subject 
        filter_fields = {
            'name': ('exact','icontains','istartswith'),
            'parent_id':('exact','isnull')
        }
        interfaces = (Node, )
        connection_class = TotalCountConnection

