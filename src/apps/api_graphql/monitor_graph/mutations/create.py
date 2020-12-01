from graphene import Field
from graphene import Mutation

from apps.registry_monitor.models import Monitor
from apps.learning_graph.models import Subject
from apps.api_graphql.utils import transform_global_ids, transform_global_ids_list
from apps.api_graphql.monitor_graph.inputs import MonitorInput
from apps.api_graphql.monitor_graph.objects import MonitorNode
from apps.api_graphql.errors import InvalidIdException
from apps.registry_monitor.forms import RegistryMonitorForm


from graphene_django.types import ErrorType
from graphene_django.forms.mutation import  DjangoFormMutation
'''
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
                if s :
                    user.subject.add(s)
                
        else:
            raise InvalidIdException("there's no id provided")
        return CreateMonitor(user=user)
'''
class CreateMonitor(DjangoFormMutation):
    user = Field(MonitorNode)
    class Meta:
       form_class = RegistryMonitorForm

    @classmethod
    def perform_mutate(cls,form, info):
        print("This only runs when the form is valid")

        form.save()
        return CreateMonitor(user=form.data,**form.data) # TODO cule machetaxo para mantener la compatibilidad con el front

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        input['subject'] = transform_global_ids_list(input['subject'])
        print(input)
        form = cls.get_form(root, info, **input)
        if form.is_valid():
            return cls.perform_mutate(form, info)
        else:
            errors = ErrorType.from_errors(form.errors)
            return CreateMonitor(errors=errors,user=form.data,**form.data) # TODO cule machetaxo para mantener la compatibilidad con el front
