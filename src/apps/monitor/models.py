from django.db import models
from django.contrib.auth.models import User
from apps.learning_graph.models import Subject
from django.utils.translation import gettext_lazy as _
# Create your models here.


class Monitor(User):
    telephone = models.CharField(max_length=10, blank=False)
    residence = models.CharField(max_length=50, blank=False, null=False)
    level_education = models.CharField(max_length=50, blank=False, null=False)
    college = models.CharField(max_length=50, blank=False, null=False)
    college_career = models.CharField(max_length=50, blank=False,null=False)

    subject = models.ManyToManyField(
        Subject, blank=True, related_name='subjects',verbose_name=_("subjects"), max_length=25)

    def __str__(self):
        return self.first_name + self.last_name
