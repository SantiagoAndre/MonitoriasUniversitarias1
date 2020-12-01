from django import forms
from django.utils.translation import gettext_lazy as _
#from multiselectfield import MultiSelectField
from collections.abc import Iterable  
from apps.learning_graph.models import Subject

from apps.users.models import Monitor,Contact
from .models import RegistryMonitor
  
# Formularios base
SERVICES = [(1,_("CLASS")), (2,_("ADVISORY")),(3,_("DO ACADEMIC WORK"))]
class RegistryMonitorForm(forms.Form):
    
    # <input type="text" minlength="5" maxlength="150" />
    first_name =  forms.CharField(label = _("first name"),min_length=5, max_length=150,required=True)
    last_name =  forms.CharField(label =_("last name"),min_length=5, max_length=150,required=True)
    email = forms.EmailField( label = _("email"),required=True)
    telephone = forms.CharField(label = _("telephone"), max_length=100, required=True)
    residence = forms.CharField( label = _("residence"),max_length=100, required=True)
    level_education = forms.CharField(label = _("level education"), max_length=100, required=True)
    college = forms.CharField( label = _("college"),max_length=100, required=True)
    college_career = forms.CharField( label = _("college career"),max_length=100, required=True)
    experience = forms.CharField(label = _("experience"), max_length=100, required=False)
    #service1 = MultiSelectField(choices=SERVICES)
 #  service_type = forms.MultipleChoiceField(label = _("service type"),
    #    choices=SERVICES, required=False)# TODO cambiar por  ModelChoiceFIeld
    short_job  = forms.BooleanField(label = _("short job"), required=False)
    career_average = forms.FloatField(label = _("career average"), required=False)
    work_hour = forms.IntegerField(label = _("work hour"), required=False)# TODO cambiar por horario
    informatic_tool = forms.CharField(label = _("informatic tool"), max_length=2, required=False)
    subject = forms.ModelMultipleChoiceField(label = _("subjects"),
    queryset=Subject.objects.all())# TODO chage to plural
    
 
    def save(self):
        # lógica de negocio
        # data ya está validada
        # print(self.cleaned_data) # campos validados y limpios
        # print(self.data) # campos sin validar y sin limpiar
        # Save monitor
        data = self.cleaned_data
        print(data)
        print("create user")
        # Save contact
        c = Contact.objects.create(
            telephone =  data['telephone'],
            residence = data['residence']
        )

        user = Monitor.objects.create(
            username = data['email'], # TODO  
            first_name  = data['first_name'],
            last_name = data['last_name'],
            email = data['email'],
            level_education = data['level_education'],
            college =  data['college'],
            college_career = data['college_career'],
            #service_type =  data['service_type'],
            work_hour = data['work_hour'],
            contact  = c
        )
        for s in data['subject']:
            user.subjects.add(s)

        
        print("create contact")
        # Save Registry Monitor
        r= RegistryMonitor.objects.create(
            experience = data['experience'],
            short_job =  data['short_job'],
            career_average =  data['career_average'],
            informatic_tool =  data['informatic_tool'],
            monitor = user
        )
        print("create registry")

