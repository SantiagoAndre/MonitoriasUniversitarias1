from django.db import models

from django.utils.translation import gettext_lazy as _

# Create your models here.
class LearningLine(models.Model):
    """Linea de aprendizaje"""
    class Meta:
        unique_together = ["name"]
    name = models.CharField(_("name"),max_length=100)
    description = models.CharField(_("description"),max_length=200)   
    def __str__(self):
        return self.name
class Subject(models.Model):
    """Tema academico"""
    class Meta:
        unique_together = ["name"]
    name = models.CharField(_("name"),max_length=100,blank=False,null=False)
    description = models.CharField(_("description"),max_length=200,blank=False,null=False)   
    parent = models.ForeignKey('self',verbose_name=_("parent subject"),on_delete=models.CASCADE,null=True)
    learning_line = models.ForeignKey(LearningLine,verbose_name=_("learning line"),on_delete=models.CASCADE,null=False)
    def __str__(self):
        return self.name
    