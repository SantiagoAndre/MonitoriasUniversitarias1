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

from .objects import CollegeNode
from .objects import CollegeCareerNode
from .objects import MonitorNode
from .objects import LearningLineNode
from .objects import TopicNode
from .objects import SubtopicNode
from .objects import ServiceNode
from .objects import QuotationNode
from .objects import PollNode

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
