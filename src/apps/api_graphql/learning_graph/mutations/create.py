from graphene import Field
from graphene import Mutation

from apps.learning_graph.models import LearningLine,Subject


from apps.api_graphql.learning_graph.objects import LearningLineNode,SubjectNode
from apps.api_graphql.learning_graph.inputs import CreateLearningLineInput,CreateSubjectInput

from apps.api_graphql.utils import transform_global_ids
from apps.api_graphql.utils import delete_attributes_none

class CreateLearningLine(Mutation):
    learning_line = Field(LearningLineNode)

    class Arguments:
        input = CreateLearningLineInput(required=True)

    def mutate(self, info, input):
        learning_line = LearningLine.objects.create(**vars(input))
        return CreateLearningLine(learning_line=learning_line)


class CreateSubject(Mutation):
    learning_line = Field(SubjectNode)

    class Arguments:
        input = CreateSubjectInput(required=True)

    def mutate(self, info, input):
        learning_line = Subject.objects.create(**vars(input))

        return CreateSubject(learning_line=learning_line)
