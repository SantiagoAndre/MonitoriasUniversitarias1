from graphene import Field
from graphene import String
from graphene import Mutation

from apps.learning_graph.models import LearningLine


from apps.api_graphql.learning_graph.objects import LearningLineNode
from apps.api_graphql.learning_graph.inputs import UpdateLearningLineInput

from apps.api_graphql.utils import transform_global_ids
from apps.api_graphql.utils import delete_attributes_none

class UpdateLearningLine(Mutation):
    learning_line = Field(LearningLineNode)

    class Arguments:
        input = UpdateLearningLineInput(required=True)

    def mutate(self, info, input):
        LearningLine.objects.filter(pk=input.get('id')).update(**input)
        learning_line = LearningLine.objects.get(pk=input.get('id'))
        
        return UpdateLearningLine(learning_line=learning_line)