from graphene import Field
from graphene import Mutation

from apps.learning_graph.models import Subject


from apps.api_graphql.learning_graph.objects import SubjectNode
from apps.api_graphql.learning_graph.inputs import CreateSubjectInput

from apps.api_graphql.utils import transform_global_ids
from apps.api_graphql.utils import delete_attributes_none
from graphql_relay.node.node import from_global_id
'''
class CreateLearningLine(Mutation):
    learning_line = Field(LearningLineNode)

    class Arguments:
        input = CreateLearningLineInput(required=True)

    def mutate(self, info, input):
        learning_line = LearningLine.objects.create(**vars(input))

        return CreateLearningLine(learning_line=learning_line)
'''

class CreateSubject(Mutation):

    subject = Field(SubjectNode)

    class Arguments:
        input = CreateSubjectInput(required=True)

    def mutate(self, info, input):
        new_input = {}
        #input["learning_line_id"] = int( from_global_id(input.get('learning_line_id'))[1] )
        if input.get("parent_id"):
            input["parent_id"]= int( from_global_id(input.get('parent_id'))[1] )
        subject = Subject.objects.create(**(input))
        
        return CreateSubject(subject=subject)
