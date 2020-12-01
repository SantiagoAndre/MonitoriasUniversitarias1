from graphene import Field, String, Mutation

from apps.api_graphql.monitor_graph.inputs import UpdateMonitorInput, UpdateIsActiveInput
from apps.api_graphql.monitor_graph.objects import MonitorNode
from apps.registry_monitor.models import Monitor

from apps.api_graphql.utils import transform_global_ids


class UpdateMonitor(Mutation):
    monitor = Field(MonitorNode)

    class Arguments:
        input = UpdateMonitorInput(required=True)

    def mutate(self, info, input):
        input = transform_global_ids(**input)
        monitor = Monitor.objects.get(pk=input.get('id'))
        if not monitor:
            raise Monitor.DoesNoExist
        monitor.__dict__.update(**input)
        monitor.save()
        return UpdateMonitor(monitor=monitor)


class UpdateIsActive(Mutation):
    monitor = Field(MonitorNode)

    class Arguments:
        input = UpdateIsActiveInput(required=True)

    def mutate(self, info, input):
        input = transform_global_ids(**input)
        monitor = Monitor.objects.get(pk=input.get('id'))
        if not monitor:
            raise Monitor.DoesNoExist
        monitor.__dict__.update(**input)
        monitor.save()
        return UpdateMonitor(monitor=monitor)
