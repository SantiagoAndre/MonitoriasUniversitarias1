from graphene import ObjectType,Schema
from graphene.relay import Node
from graphene_django.filter import DjangoFilterConnectionField


from apps.learning_graph.models import  Subject

from .learning_graph.objects import SubjectNode
from .monitor_graph.objects import MonitorNode

from .learning_graph.mutations.create import CreateSubject
from .learning_graph.mutations.update import UpdateSubject
from .learning_graph.mutations.delete import DeleteSubject
from .monitor_graph.mutations.create import CreateMonitor
# Schema definition


class Query(ObjectType):
    #learning_line = Node.Field(LearningLineNode)
    #all_learning_lines = DjangoFilterConnectionField(LearningLineNode)


    subject = Node.Field(SubjectNode)
    all_subjects = DjangoFilterConnectionField(SubjectNode)
    all_monitors = DjangoFilterConnectionField(MonitorNode)


class Mutation(ObjectType):
    #create_learning_line = CreateLearningLine.Field()
    #update_learning_line = UpdateLearningLine.Field()
    #delete_learning_line = DeleteLearningLine.Field()
    create_subject = CreateSubject.Field()
    update_subject = UpdateSubject.Field()
    delete_subject = DeleteSubject.Field()
    create_monitor = CreateMonitor.Field()

ROOT_SCHEMA = Schema(query=Query, mutation=Mutation)