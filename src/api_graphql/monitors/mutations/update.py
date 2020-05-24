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
from api_graphql.monitors.inputs import UpdateCollegeInput
from api_graphql.monitors.inputs import UpdateCollegeCareerInput
from api_graphql.monitors.inputs import UpdateMonitorInput
from api_graphql.monitors.inputs import UpdateLearningLineInput
from api_graphql.monitors.inputs import UpdateTopicInput
from api_graphql.monitors.inputs import UpdateSubtopicInput
from api_graphql.monitors.inputs import UpdateServiceInput
from api_graphql.utils import transform_global_ids
from api_graphql.utils import delete_attributes_none

# Create your mutations here


class UpdateCollege(Mutation):
    college = Field(CollegeNode)

    class Arguments:
        input = UpdateCollegeInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        College.objects.filter(pk=input.get('id')).update(**input)
        college = College.objects.get(pk=input.get('id'))

        return UpdateCollege(college=college)


class UpdateCollegeCareer(Mutation):
    college_career = Field(CollegeCareerNode)

    class Arguments:
        input = UpdateCollegeCareerInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        CollegeCareer.objects.filter(pk=input.get('id')).update(**input)
        college_career = CollegeCareer.objects.get(pk=input.get('id'))

        return UpdateCollegeCareer(college_career=college_career)


class UpdateMonitor(Mutation):
    monitor = Field(MonitorNode)

    class Arguments:
        input = UpdateMonitorInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Monitor.objects.filter(pk=input.get('id')).update(**input)
        monitor = Monitor.objects.get(pk=input.get('id'))

        return UpdateMonitor(monitor=monitor)


class UpdateLearningLine(Mutation):
    learning_line = Field(LearningLineNode)

    class Arguments:
        input = UpdateLearningLineInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        LearningLine.objects.filter(pk=input.get('id')).update(**input)
        learning_line = LearningLine.objects.get(pk=input.get('id'))

        return UpdateLearningLine(learning_line=learning_line)


class UpdateTopic(Mutation):
    topic = Field(TopicNode)

    class Arguments:
        input = UpdateTopicInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Topic.objects.filter(pk=input.get('id')).update(**input)
        topic = Topic.objects.get(pk=input.get('id'))

        return UpdateTopic(topic=topic)


class UpdateSubtopic(Mutation):
    subtopic = Field(SubtopicNode)

    class Arguments:
        input = UpdateSubtopicInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Subtopic.objects.filter(pk=input.get('id')).update(**input)
        subtopic = Subtopic.objects.get(pk=input.get('id'))

        return UpdateSubtopic(subtopic=subtopic)



class UpdateService(Mutation):
    service = Field(ServiceNode)

    class Arguments:
        input = UpdateServiceInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Service.objects.filter(pk=input.get('id')).update(**input)
        service = Service.objects.get(pk=input.get('id'))

        return UpdateService(service=service)
