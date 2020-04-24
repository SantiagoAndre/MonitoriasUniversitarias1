from graphene import ObjectType,Schema
from graphene.relay import Node
from graphene_django.filter import DjangoFilterConnectionField


from apps.learning_graph.models import LearningLine, Subject

from .learning_graph.objects import LearningLineNode

from .learning_graph.mutations.create import CreateLearningLine
from .learning_graph.mutations.update import UpdateLearningLine
from .learning_graph.mutations.delete import DeleteLearningLine

# Schema definition


class Query(ObjectType):
    learning_line = Node.Field(LearningLineNode)

    all_learning_lines = DjangoFilterConnectionField(LearningLineNode)



class Mutation(ObjectType):
    create_learning_line = CreateLearningLine.Field()
    
    update_learning_line = UpdateLearningLine.Field()
    
    delete_learning_line = DeleteLearningLine.Field()
    


ROOT_SCHEMA = Schema(query=Query, mutation=Mutation)