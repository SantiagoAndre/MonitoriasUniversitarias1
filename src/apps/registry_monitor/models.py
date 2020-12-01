from django.db import models
from django.utils.translation import gettext_lazy as _
from model_utils import FieldTracker

from apps.users.models import Monitor
# Create your models here.


class RegistryMonitor(models.Model):
    # STATUS OPTIONS
    PRESELECTION = 'PRESELECTION'
    DISCARDED = 'DISCARDED'
    TEST = 'TEST'
    SELECTED = 'SELECTED'
    STATUS_CHOICES = ((PRESELECTION,_('In preselection')), (DISCARDED, _('Discarted')), (TEST, _('In test state')), (SELECTED, _('Permanent')))
    
    experience = models.CharField(max_length=50,blank=True, null=True)
    short_job = models.BooleanField(null=True,default=False)
    career_average = models.FloatField(blank=False, null=True, default=0.0)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=PRESELECTION, null=False, blank=True)
    informatic_tool = models.CharField(max_length=2,null=True, default='no')
    
    status_tracker = FieldTracker(fields=['status'])
    
    def __str__(self):
        return self.first_name + self.last_name
