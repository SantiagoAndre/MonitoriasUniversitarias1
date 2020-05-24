from graphene import Schema

from api_graphql.schema import Query
from api_graphql.schema import Mutation


schema = Schema(query=Query, mutation=Mutation)