from graphene import Field
from graphene import Mutation

from monitors.models import College
from monitors.models import Career
from monitors.models import City
from monitors.models import Contact
from monitors.models import Monitor
from monitors.models import Service
from monitors.models import Skill
from monitors.models import Client
from monitors.models import Quoation
from api_graphql.monitors.objects import CollegeNode
from api_graphql.monitors.objects import CareerNode
from api_graphql.monitors.objects import CityNode
from api_graphql.monitors.objects import ContactNode
from api_graphql.monitors.objects import MonitorNode
from api_graphql.monitors.objects import ServiceNode
from api_graphql.monitors.objects import SkillNode
from api_graphql.monitors.objects import ClientNode
from api_graphql.monitors.objects import QuoationNode
from api_graphql.monitors.inputs import CreateCollegeInput
from api_graphql.monitors.inputs import CreateCareerInput
from api_graphql.monitors.inputs import CreateCityInput
from api_graphql.monitors.inputs import CreateContactInput
from api_graphql.monitors.inputs import CreateMonitorInput
from api_graphql.monitors.inputs import CreateServiceInput
from api_graphql.monitors.inputs import CreateSkillInput
from api_graphql.monitors.inputs import CreateClientInput
from api_graphql.monitors.inputs import CreateQuoationInput
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


class CreateCareer(Mutation):
    career = Field(CareerNode)

    class Arguments:
        input = CreateCareerInput(required=True)

    def mutate(self, info, input):
        career = Career.objects.create(**vars(input))

        return CreateCareer(career=career)


class CreateCity(Mutation):
    city = Field(CityNode)

    class Arguments:
        input = CreateCityInput(required=True)

    def mutate(self, info, input):
        city = City.objects.create(**vars(input))

        return CreateCity(city=city)


class CreateContact(Mutation):
    contact = Field(ContactNode)

    class Arguments:
        input = CreateContactInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        contact = Contact.objects.create(**vars(input))

        return CreateContact(contact=contact)


class CreateMonitor(Mutation):
    monitor = Field(MonitorNode)

    class Arguments:
        input = CreateMonitorInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        monitor = Monitor.objects.create(**input)

        return CreateMonitor(monitor=monitor)


class CreateService(Mutation):
    service = Field(ServiceNode)

    class Arguments:
        input = CreateServiceInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        service = Service.objects.create(**input)

        return CreateService(service=service)


class CreateSkill(Mutation):
    skill = Field(SkillNode)

    class Arguments:
        input = CreateSkillInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        skill = Skill.objects.create(**input)

        return CreateSkill(skill=skill)


class CreateClient(Mutation):
    skill = Field(ClientNode)

    class Arguments:
        input = CreateClientInput(required=True)

    def mutate(self, info, input):
        client = Client.objects.create(**input)

        return CreateClient(client=client)


class CreateQuoation(Mutation):
    quoation = Field(QuoationNode)

    class Arguments:
        input = CreateQuoationInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)
        quoation = Quoation.objects.create(**input)

        return CreateQuoation(quoation=quoation)
