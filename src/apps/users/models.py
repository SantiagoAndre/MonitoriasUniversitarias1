from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

from apps.learning_graph.models import Subject
# Create your models here.

class Contact(models.Model):
    telephone = models.CharField(max_length=10, blank=False)
    residence = models.CharField(max_length=50, blank=False, null=False)
    

class User(AbstractUser):
    first_name = models.CharField(_('first name'), max_length=150, blank=False,null=False)
    last_name = models.CharField(_('last name'), max_length=150,  blank=False,null=False)
    email = models.EmailField(_('email address'), blank=False, null=False)
    contact = models.OneToOneField("Contact", verbose_name=_("contact"), on_delete=models.CASCADE) 
   
class Monitor(User):
    raiting =  models.PositiveIntegerField(_("raiting"),null=True)#Cuando no ha dado ni una clase puede ser null este campo
    registry = models.OneToOneField("registry_monitor.RegistryMonitor", verbose_name=_("registry"), on_delete=models.CASCADE,null=True)
    level_education = models.CharField(max_length=50, blank=False, null=False)
    college = models.CharField(max_length=50, blank=False, null=False)
    college_career = models.CharField(max_length=50, blank=False,null=False)
    service_type = models.CharField(max_length=60,blank=True, null=True) # TODO service type es una tabla aparte, cambiar por ManytoManyField
    work_hour = models.IntegerField(verbose_name="work_hours", default=1)# TODO cambiar por horario de trabajo

    subjects = models.ManyToManyField(
        Subject, blank=True, related_name='subjects',verbose_name=_("subjects"), max_length=25)

