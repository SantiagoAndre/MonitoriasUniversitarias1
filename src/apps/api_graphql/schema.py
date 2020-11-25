from graphene import ObjectType, Schema, List, String, Field
from graphene.relay import Node
from graphene_django.filter import DjangoFilterConnectionField

import graphene
from apps.learning_graph.models import Subject

from .learning_graph.objects import SubjectNode
from .monitor_graph.objects import MonitorNode

from .learning_graph.mutations.create import CreateSubject
from .learning_graph.mutations.update import UpdateSubject
from .learning_graph.mutations.delete import DeleteSubject
from .monitor_graph.mutations.create import CreateMonitor
from .monitor_graph.mutations.update import UpdateMonitor, UpdateIsActive
from .i18n import LanguageApplicationObject, SelectLanguage
from .i18n import current_language, DICT_LANGUAGES

# Schema definition


class Query(ObjectType):
    application_languages = graphene.List(LanguageApplicationObject)
    current_language = Field(LanguageApplicationObject)
    subject = Node.Field(SubjectNode)
    monitor = Node.Field(MonitorNode)
    all_subjects = DjangoFilterConnectionField(SubjectNode)
    all_monitors = DjangoFilterConnectionField(MonitorNode)

    def resolve_application_languages(self, info, *args, **kwargs):
        return DICT_LANGUAGES

    def resolve_current_language(self, info, *args, **kwargs):
        return current_language()


class Mutation(ObjectType):
    create_subject = CreateSubject.Field()
    update_subject = UpdateSubject.Field()
    delete_subject = DeleteSubject.Field()

    create_monitor = CreateMonitor.Field()
    update_monitor = UpdateMonitor.Field()
    update_monitor_is_active = UpdateIsActive.Field()
    select_language = SelectLanguage.Field()


ROOT_SCHEMA = Schema(query=Query, mutation=Mutation)
