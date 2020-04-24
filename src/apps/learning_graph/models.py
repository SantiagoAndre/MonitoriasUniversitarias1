from django.db import models

from django.utils.translation import gettext_lazy as _

# Create your models here.
class LearningLine(models.Model):
    """Linea de aprendizaje"""

    name = models.CharField(_("name"),max_length=100)
    description = models.CharField(_("description"),max_length=200)   
    def __str__(self):
        return self.name
class Subject(models.Model):
    """Tema academico"""
    name = models.CharField(_("name"),max_length=100)
    description = models.CharField(_("description"),max_length=200)   
    parent = models.ForeignKey('self',verbose_name=_("parent subject"),on_delete=models.CASCADE)
    def __str__(self):
        return self.name
    