from graphene import ID
from graphene import Field
from graphene import Mutation
from graphql import GraphQLError
from graphql_relay.node.node import from_global_id

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


class DeleteCareer(Mutation):
    career = Field(CareerNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            career = Career.objects.get(pk=input)
            Career.objects.filter(pk=input).delete()
        except Career.DoesNotExist:
            raise GraphQLError('College career does not delete')

        return DeleteCareer(career=career)


class DeleteCity(Mutation):
    city = Field(CityNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            city = City.objects.get(pk=input)
            City.objects.filter(pk=input).delete()
        except City.DoesNotExist:
            raise GraphQLError('City does not delete')

        return DeleteCity(city=city)


class DeleteContact(Mutation):
    contact = Field(ContactNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            contact = Contact.objects.get(pk=input)
            Contact.objects.filter(pk=input).delete()
        except Contact.DoesNotExist:
            raise GraphQLError('Contact does not delete')

        return DeleteContact(contact=contact)


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


class DeleteSkill(Mutation):
    skill = Field(SkillNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            skill = Skill.objects.get(pk=input)
            Skill.objects.filter(pk=input).delete()
        except Skill.DoesNotExist:
            raise GraphQLError('Skill does not delete')

        return DeleteSkill(skill=skill)


class DeleteClient(Mutation):
    client = Field(ClientNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            client = Client.objects.get(pk=input)
            Client.objects.filter(pk=input).delete()
        except Client.DoesNotExist:
            raise GraphQLError('Client does not delete')

        return DeleteClient(client=client)


class DeleteQuoation(Mutation):
    quoation = Field(QuoationNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            quoation = Quoation.objects.get(pk=input)
            Quoation.objects.filter(pk=input).delete()
        except Quoation.DoesNotExist:
            raise GraphQLError('Quoation does not delete')

        return DeleteQuoation(quoation=quoation)
