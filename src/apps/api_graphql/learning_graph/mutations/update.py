from graphene import Field
from graphene import String
from graphene import Mutation

from apps.learning_graph.models import LearningLine,Subject


from apps.api_graphql.learning_graph.objects import LearningLineNode,SubjectNode
from apps.api_graphql.learning_graph.inputs import UpdateLearningLineInput,UpdateSubjectInput

from apps.api_graphql.utils import transform_global_ids
from apps.api_graphql.utils import delete_attributes_none
from graphql_relay.node.node import from_global_id
class UpdateLearningLine(Mutation):
    learning_line = Field(LearningLineNode)

    class Arguments:
        input = UpdateLearningLineInput(required=True)

    def mutate(self, info, input):
        input["id"]= from_global_id(input.get('id'))[1]
        
        
        LearningLine.objects.filter(pk=input.get('id')).update(**input)
        learning_line = LearningLine.objects.get(pk=input.get('id'))
        
        return UpdateLearningLine(learning_line=learning_line)



class UpdateSubject(Mutation):
    learning_line = Field(SubjectNode)

    class Arguments:
        input = UpdateSubjectInput(required=True)

    def mutate(self, info, input):
        id = from_global_id(input.get('id'))
        print("id", input.get('id'))
        print("id decode", id)
        Subject.objects.filter(pk=id).update(**input)
        learning_line = Subject.objects.get(pk=input.get('id'))
        
        return UpdateSubject(learning_line=learning_line)
