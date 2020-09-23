from graphene import ID
from graphene import Field
from graphene import Mutation

from graphql_relay.node.node import from_global_id

from apps.learning_graph.models import LearningLine


from apps.api_graphql.learning_graph.objects import LearningLineNode

from apps.api_graphql.utils import transform_global_ids
from apps.api_graphql.utils import delete_attributes_none

class DeleteLearningLine(Mutation):
    learning_line = Field(LearningLineNode)

    class Arguments:
        input = ID(required=True)

    def mutate(self, info, input):
        input = from_global_id(input)[1]
        try:
            learning_line = LearningLine.objects.get(pk=input)
            LearningLine.objects.filter(pk=input).delete()
        except LearningLine.DoesNotExist:
            raise GraphQLError('Learning Line does not delete')

        return DeleteLearningLine(learning_line=learning_line)