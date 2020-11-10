from graphene import Field
from graphene import Mutation

from apps.monitor.models import Monitor
from apps.learning_graph.models import Subject
from apps.api_graphql.utils import transform_global_ids, transform_global_ids_list
from apps.api_graphql.monitor_graph.inputs import MonitorInput
from apps.api_graphql.monitor_graph.objects import MonitorNode


class CreateMonitor(Mutation):
    user = Field(MonitorNode)

    class Arguments:
        input = MonitorInput(required=True)

    def mutate(self, info, input):
        input["username"] = input["email"]
        if input["subject"]:
            subjects_ids = input.pop("subject")
            service = input.pop("service_type")
            input = transform_global_ids(**input)
            user = Monitor(**(input))
            s = ''
            size = len(service)
            if size == 1:
                s = service[0]
            else:
                s = service[0]+", "+service[1]
            user.service_type = s
            user.save()
            subjects_ids = transform_global_ids_list(subjects_ids)

            for subject in subjects_ids:
                s = Subject.objects.get(pk=subject)
                user.subject.add(s)
            
        else:
            user = Monitor.objects.create(**(input))
        return CreateMonitor(user=user)
