from graphene import Field
from graphene import String
from graphene import Mutation

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
from api_graphql.monitors.inputs import CreateCollegeInput
from api_graphql.monitors.inputs import CreateCollegeCareerInput
from api_graphql.monitors.inputs import CreateMonitorInput
from api_graphql.monitors.inputs import CreateLearningLineInput
from api_graphql.monitors.inputs import CreateTopicInput
from api_graphql.monitors.inputs import CreateSubtopicInput
from api_graphql.monitors.inputs import CreateServiceInput
from api_graphql.utils import transform_global_ids
from api_graphql.utils import delete_attributes_none

# Create your mutations here


class CreateCollege(Mutation):
    college = Field(CollegeNode)

    class Arguments:
        input = CreateCollegeInput(required=True)

    def mutate(self, info, input):
        college = College.objects.create(**vars(input))

        return CreateCollege(college=college)


class CreateCollegeCareer(Mutation):
    college_career = Field(CollegeCareerNode)

    class Arguments:
        input = CreateCollegeCareerInput(required=True)

    def mutate(self, info, input):
        college_career = CollegeCareer.objects.create(**vars(input))
        
        return CreateCollegeCareer(college_career=college_career)


class CreateMonitor(Mutation):
    monitor = Field(MonitorNode)

    class Arguments:
        input = CreateMonitorInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        monitor = Monitor.objects.create(**input)

        return CreateMonitor(monitor=monitor)


class CreateLearningLine(Mutation):
    learning_line = Field(LearningLineNode)

    class Arguments:
        input = CreateLearningLineInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        learning_line = LearningLine.objects.create(**input)

        return CreateLearningLine(learning_line=learning_line)


class CreateTopic(Mutation):
    topic = Field(TopicNode)

    class Arguments:
        input = CreateTopicInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        topic = LearningLine.objects.create(**input)

        return CreateTopic(topic=topic)


class CreateSubtopic(Mutation):
    subtopic = Field(SubtopicNode)

    class Arguments:
        input = CreateSubtopicInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        subtopic = LearningLine.objects.create(**input)

        return CreateSubtopic(subtopic=subtopic)


class CreateService(Mutation):
    service = Field(SubtopicNode)

    class Arguments:
        input = CreateServiceInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        service = LearningLine.objects.create(**input)

        return CreateService(service=service)
