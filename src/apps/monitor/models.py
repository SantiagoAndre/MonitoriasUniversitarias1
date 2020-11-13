from django.db import models
from django.contrib.auth.models import User
from apps.learning_graph.models import Subject
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Monitor(User):
    # STATUS OPTIONS
    PRESELECTION = 'PRESELECTION'
    DISCARDED = 'DISCARDED'
    TEST = 'TEST'
    SELECTED = 'SELECTED'
    STATUS_CHOICES = ((PRESELECTION,_('In preselection')), (DISCARDED, _('Discarted')), (TEST, _('In test state')), (SELECTED, _('Permanent')))

    telephone = models.CharField(max_length=10, blank=False)
    residence = models.CharField(max_length=50, blank=False, null=False)
    level_education = models.CharField(max_length=50, blank=False, null=False)
    college = models.CharField(max_length=50, blank=False, null=False)
    college_career = models.CharField(max_length=50, blank=False,null=False)
    """Optionals"""
    experience = models.CharField(max_length=50,blank=True, null=True)
    service_type = models.CharField(max_length=60,blank=True, null=True)
    short_job = models.BooleanField(null=True,default=False)
    career_average = models.FloatField(blank=False, null=True, default=0.0)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default=PRESELECTION, null=False, blank=True)
    work_hour = models.IntegerField(verbose_name="work_hours", default=1)
    informatic_tool = models.CharField(max_length=2,null=True, default=False)
    
    subject = models.ManyToManyField(
        Subject, blank=True, related_name='subjects',verbose_name=_("subjects"), max_length=25)

    def __str__(self):
        return self.first_name + self.last_name
