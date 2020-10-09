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
        
        learning_line = LearningLine.objects.get(pk=input.get('id'))
        if not learning_line:
            raise LearningLine.DoesNoExist
        learning_line.__dict__.update(**input)
        learning_line.save()
        return UpdateLearningLine(learning_line=learning_line)



class UpdateSubject(Mutation):
    subject = Field(SubjectNode)

    class Arguments:
        input = UpdateSubjectInput(required=True)

    def mutate(self, info, input):
        input["id"]= int( from_global_id(input.get('id'))[1] )
        if "parent_id" in input:
            input["parent_id"]= int( from_global_id(input.get('parent_id'))[1] )
        if "learning_line_id" in input:
            input["learning_line_id"]= int( from_global_id(input.get('learning_line_id'))[1] )
        subject = Subject.objects.get(pk=input.get('id'))
        if not subject:
            raise Subject.DoesNoExist
        subject.__dict__.update(**input)
        subject.save()
        return UpdateSubject(subject=subject)
