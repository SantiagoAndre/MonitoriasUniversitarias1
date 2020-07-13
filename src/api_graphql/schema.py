from graphene import ObjectType
from graphene.relay import Node
from graphene_django.filter import DjangoFilterConnectionField

from .monitors.objects import CollegeNode
from .monitors.objects import CareerNode
from .monitors.objects import CityNode
from .monitors.objects import ContactNode
from .monitors.objects import MonitorNode
from .monitors.objects import ServiceNode
from .monitors.objects import SkillNode
from .monitors.objects import ClientNode
from .monitors.objects import QuoationNode


from .monitors.mutations.create import CreateCollege
from .monitors.mutations.create import CreateCareer
from .monitors.mutations.create import CreateCity
from .monitors.mutations.create import CreateContact
from .monitors.mutations.create import CreateMonitor
from .monitors.mutations.create import CreateService
from .monitors.mutations.create import CreateSkill
from .monitors.mutations.create import CreateClient
from .monitors.mutations.create import CreateQuoation

from .monitors.mutations.update import UpdateCollege
from .monitors.mutations.update import UpdateCareer
from .monitors.mutations.update import UpdateCity
from .monitors.mutations.update import UpdateContact
from .monitors.mutations.update import UpdateMonitor
from .monitors.mutations.update import UpdateService
from .monitors.mutations.update import UpdateSkill
from .monitors.mutations.update import UpdateClient
from .monitors.mutations.update import UpdateQuoation

from .monitors.mutations.delete import DeleteCollege
from .monitors.mutations.delete import DeleteCareer
from .monitors.mutations.delete import DeleteCity
from .monitors.mutations.delete import DeleteContact
from .monitors.mutations.delete import DeleteMonitor
from .monitors.mutations.delete import DeleteService
from .monitors.mutations.delete import DeleteSkill
from .monitors.mutations.delete import DeleteClient
from .monitors.mutations.delete import DeleteQuoation

# Schema definition


class Query(ObjectType):
    college = Node.Field(CollegeNode)
    career = Node.Field(CareerNode)
    city = Node.Field(CityNode)
    contact = Node.Field(ContactNode)
    monitor = Node.Field(MonitorNode)
    service = Node.Field(ServiceNode)
    skill = Node.Field(SkillNode)
    client = Node.Field(ClientNode)
    quoation = Node.Field(QuoationNode)

    all_colleges = DjangoFilterConnectionField(CollegeNode)
    all_careers = DjangoFilterConnectionField(CareerNode)
    all_cities = DjangoFilterConnectionField(CityNode)
    all_contacts = DjangoFilterConnectionField(ContactNode)
    all_monitors = DjangoFilterConnectionField(MonitorNode)
    all_services = DjangoFilterConnectionField(ServiceNode)
    all_skills = DjangoFilterConnectionField(SkillNode)
    all_clients = DjangoFilterConnectionField(ClientNode)
    all_quoations = DjangoFilterConnectionField(QuoationNode)


class Mutation(ObjectType):
    create_college = CreateCollege.Field()
    create_career = CreateCareer.Field()
    create_city = CreateCity.Field()
    create_contact = CreateContact.Field()
    create_monitor = CreateMonitor.Field()
    create_service = CreateService.Field()
    create_skill = CreateSkill.Field()
    create_client = CreateClient.Field()
    create_quoation = CreateQuoation.Field()

    update_college = UpdateCollege.Field()
    update_career = UpdateCareer.Field()
    update_city = UpdateCity.Field()
    update_contact = UpdateContact.Field()
    update_monitor = UpdateMonitor.Field()
    update_service = UpdateService.Field()
    update_skill = UpdateSkill.Field()
    update_client = UpdateClient.Field()
    update_quoation = UpdateQuoation.Field()

    delete_college = DeleteCollege.Field()
    delete_career = DeleteCareer.Field()
    delete_city = DeleteCity.Field()
    delete_contact = DeleteContact.Field()
    delete_monitor = DeleteMonitor.Field()
    delete_service = DeleteService.Field()
    delete_skill = DeleteSkill.Field()
    delete_client = DeleteClient.Field()
    delete_quoation = DeleteQuoation.Field()
