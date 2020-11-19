from graphene import Field
from graphene import Mutation

from apps.monitor.models import Monitor
from apps.learning_graph.models import Subject
from apps.api_graphql.utils import transform_global_ids, transform_global_ids_list
from apps.api_graphql.monitor_graph.inputs import MonitorInput
from apps.api_graphql.monitor_graph.objects import MonitorNode
from apps.api_graphql.errors import InvalidIdException

class CreateMonitor(Mutation):
    user = Field(MonitorNode)

    class Arguments:
        input = MonitorInput(required=True)

    def mutate(self, info, input):
        input["username"] = input["email"]
        if input["subject"]:
            subjects_ids = transform_global_ids_list(input.pop("subject"))            
            input["service_type"] = ', '.join(input["service_type"])
            input = transform_global_ids(**input)
            user = Monitor(**(input))
            user.save()
            for subject in subjects_ids:
                s = Subject.objects.get(pk=subject)
                user.subject.add(s)
        else:
            raise InvalidIdException("there's no id provided")
        return CreateMonitor(user=user)
