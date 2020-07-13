from graphene import Field
from graphene import String
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
from api_graphql.monitors.inputs import UpdateCollegeInput
from api_graphql.monitors.inputs import UpdateCareerInput
from api_graphql.monitors.inputs import UpdateCityInput
from api_graphql.monitors.inputs import UpdateContactInput
from api_graphql.monitors.inputs import UpdateMonitorInput
from api_graphql.monitors.inputs import UpdateServiceInput
from api_graphql.monitors.inputs import UpdateSkillInput
from api_graphql.monitors.inputs import UpdateClientInput
from api_graphql.monitors.inputs import UpdateQuoationInput
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


class UpdateCareer(Mutation):
    career = Field(CareerNode)

    class Arguments:
        input = UpdateCareerInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Career.objects.filter(pk=input.get('id')).update(**input)
        career = Career.objects.get(pk=input.get('id'))

        return UpdateCareer(career=career)


class UpdateCity(Mutation):
    city = Field(CityNode)

    class Arguments:
        input = UpdateCityInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        City.objects.filter(pk=input.get('id')).update(**input)
        city = City.objects.get(pk=input.get('id'))

        return UpdateCity(city=city)


class UpdateContact(Mutation):
    contact = Field(ContactNode)

    class Arguments:
        input = UpdateContactInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Contact.objects.filter(pk=input.get('id')).update(**input)
        contact = Contact.objects.get(pk=input.get('id'))

        return UpdateContact(contact=contact)


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


class UpdateSkill(Mutation):
    skill = Field(SkillNode)

    class Arguments:
        input = UpdateSkillInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Skill.objects.filter(pk=input.get('id')).update(**input)
        skill = Skill.objects.get(pk=input.get('id'))

        return UpdateSkill(skill=skill)


class UpdateClient(Mutation):
    client = Field(ClientNode)

    class Arguments:
        input = UpdateClientInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Client.objects.filter(pk=input.get('id')).update(**input)
        client = Client.objects.get(pk=input.get('id'))

        return UpdateClient(client=client)


class UpdateQuoation(Mutation):
    quoation = Field(QuoationNode)

    class Arguments:
        input = UpdateQuoationInput(required=True)

    def mutate(self, info, input):
        input = delete_attributes_none(**vars(input))
        input = transform_global_ids(**input)

        Quoation.objects.filter(pk=input.get('id')).update(**input)
        quoation = Quoation.objects.get(pk=input.get('id'))

        return UpdateQuoation(quoation=quoation)
