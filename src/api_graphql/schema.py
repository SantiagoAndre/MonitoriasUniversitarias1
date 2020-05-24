from graphene import ObjectType
from graphene.relay import Node
from graphene_django.filter import DjangoFilterConnectionField

from monitors.models import College
from monitors.models import CollegeCareer
from monitors.models import Monitor
from monitors.models import LearningLine
from monitors.models import Topic
from monitors.models import Subtopic
from monitors.models import Service
from monitors.models import Quotation
from monitors.models import Poll
from .monitors.objects import CollegeNode
from .monitors.objects import CollegeCareerNode
from .monitors.objects import MonitorNode
from .monitors.objects import LearningLineNode
from .monitors.objects import TopicNode
from .monitors.objects import SubtopicNode
from .monitors.objects import ServiceNode
from .monitors.objects import QuotationNode
from .monitors.objects import PollNode
from .monitors.mutations.create import CreateCollege
from .monitors.mutations.create import CreateCollegeCareer
from .monitors.mutations.create import CreateMonitor
from .monitors.mutations.create import CreateLearningLine
from .monitors.mutations.create import CreateTopic
from .monitors.mutations.create import CreateSubtopic
from .monitors.mutations.create import CreateService

from .monitors.mutations.update import UpdateCollege
from .monitors.mutations.update import UpdateCollegeCareer
from .monitors.mutations.update import UpdateMonitor
from .monitors.mutations.update import UpdateLearningLine
from .monitors.mutations.update import UpdateTopic
from .monitors.mutations.update import UpdateSubtopic
from .monitors.mutations.update import UpdateService

from .monitors.mutations.delete import DeleteCollege
from .monitors.mutations.delete import DeleteCollegeCareer
from .monitors.mutations.delete import DeleteMonitor
from .monitors.mutations.delete import DeleteLearningLine
from .monitors.mutations.delete import DeleteTopic
from .monitors.mutations.delete import DeleteSubtopic
from .monitors.mutations.delete import DeleteService

# Schema definition


class Query(ObjectType):
    college = Node.Field(CollegeNode)
    college_career = Node.Field(CollegeCareerNode)
    monitor = Node.Field(MonitorNode)
    learning_line = Node.Field(LearningLineNode)
    topic = Node.Field(TopicNode)
    subtopic = Node.Field(SubtopicNode)
    service = Node.Field(ServiceNode)
    # quotation = Node.Field(QuotationNode)
    # poll = Node.Field(PollNode)

    all_colleges = DjangoFilterConnectionField(CollegeNode)
    all_college_careers = DjangoFilterConnectionField(CollegeCareerNode)
    all_monitors = DjangoFilterConnectionField(MonitorNode)
    all_learning_lines = DjangoFilterConnectionField(LearningLineNode)
    all_topics = DjangoFilterConnectionField(TopicNode)
    all_subtopics = DjangoFilterConnectionField(SubtopicNode)
    all_services = DjangoFilterConnectionField(ServiceNode)
    # all_quotations = DjangoFilterConnectionField(QuotationNode)
    # all_polls = DjangoFilterConnectionField(PollNode)


class Mutation(ObjectType):
    create_college = CreateCollege.Field()
    create_college_career = CreateCollegeCareer.Field()
    create_monitor = CreateMonitor.Field()
    create_learning_line = CreateLearningLine.Field()
    create_topic = CreateTopic.Field()
    create_subtopic = CreateSubtopic.Field()
    create_service = CreateService.Field()

    update_college = UpdateCollege.Field()
    update_college_career = UpdateCollegeCareer.Field()
    update_monitor = UpdateMonitor.Field()
    update_learning_line = UpdateLearningLine.Field()
    update_topic = UpdateTopic.Field()
    update_subtopic = UpdateSubtopic.Field()
    update_service = UpdateService.Field()

    delete_college = DeleteCollege.Field()
    delete_college_career = DeleteCollegeCareer.Field()
    delete_monitor = DeleteMonitor.Field()
    delete_learning_line = DeleteLearningLine.Field()
    delete_topic = DeleteTopic.Field()
    delete_subtopic = DeleteSubtopic.Field()
    delete_service = DeleteService.Field()