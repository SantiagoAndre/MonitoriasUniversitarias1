from graphene import ID
from graphene import Field
from graphene import Mutation
from graphql import GraphQLError
from graphql_relay.node.node import from_global_id

from monitors.models import College
from monitors.models import CollegeCareer
from monitors.models import Monitor
from monitors.models import LearningLine
from monitors.models import Topic
from monitors.models import Subtopic
from monitors.models import Service
from api_graphql.monitors.objects import CollegeNode
from api_graphql.monitors.objects import CollegeCareerNode
from api_graphql.monitors.objects import MonitorNode
from api_graphql.monitors.objects import LearningLineNode
from api_graphql.monitors.objects import TopicNode
from api_graphql.monitors.objects import SubtopicNode
from api_graphql.monitors.objects import ServiceNode

# Create your mutations here


class DeleteCollege(Mutation):
    college = Field(CollegeNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            college = College.objects.get(pk=input)
            College.objects.filter(pk=input).delete()
        except College.DoesNotExist:
            raise GraphQLError('College does not delete')

        return DeleteCollege(college=college)


class DeleteCollegeCareer(Mutation):
    college_career = Field(CollegeCareerNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            college_career = CollegeCareer.objects.get(pk=input)
            CollegeCareer.objects.filter(pk=input).delete()
        except CollegeCareer.DoesNotExist:
            raise GraphQLError('College career does not delete')

        return DeleteCollegeCareer(college_career=college_career)


class DeleteMonitor(Mutation):
    monitor = Field(MonitorNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            monitor = Monitor.objects.get(pk=input)
            Monitor.objects.filter(pk=input).delete()
        except Monitor.DoesNotExist:
            raise GraphQLError('Monitor does not delete')

        return DeleteMonitor(monitor=monitor)


class DeleteLearningLine(Mutation):
    learning_line = Field(LearningLineNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            learning_line = LearningLine.objects.get(pk=input)
            LearningLine.objects.filter(pk=input).delete()
        except LearningLine.DoesNotExist:
            raise GraphQLError('Learning line does not delete')

        return DeleteLearningLine(learning_line=learning_line)


class DeleteTopic(Mutation):
    topic = Field(TopicNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            topic = Topic.objects.get(pk=input)
            Topic.objects.filter(pk=input).delete()
        except Topic.DoesNotExist:
            raise GraphQLError('Topic does not delete')

        return DeleteTopic(topic=topic)


class DeleteSubtopic(Mutation):
    subtopic = Field(SubtopicNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            subtopic = Subtopic.objects.get(pk=input)
            Subtopic.objects.filter(pk=input).delete()
        except Subtopic.DoesNotExist:
            raise GraphQLError('Subtopic does not delete')

        return DeleteSubtopic(subtopic=subtopic)


class DeleteService(Mutation):
    service = Field(ServiceNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            service = Service.objects.get(pk=input)
            Service.objects.filter(pk=input).delete()
        except Service.DoesNotExist:
            raise GraphQLError('Service does not delete')

        return DeleteService(service=service)
