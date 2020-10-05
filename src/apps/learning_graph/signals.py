from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from .utils import process_name,process_large_text
from .models import LearningLine,Subject
@receiver(pre_save,sender=LearningLine)
def unique_name_learningline(sender,instance, **kwargs):
    instance.name  = process_name(instance.name)
    instance.description = process_large_text(instance.description)
    if LearningLine.objects.filter(name=instance.name):
        raise Exception(_("LearningLine: name already used"))
    

@receiver(pre_save,sender=Subject)
def unique_name_subject(sender,instance, **kwargs):
    instance.name  = process_name(instance.name)
    instance.description = process_large_text(instance.description)
    if Subject.objects.filter(name=instance.name):
        raise Exception(_("Subject: name already used"))
    if instance.parent_id and not Subject.objects.filter(id=instance.parent_id):
        raise Exception(_("Subject: parent Subject not found"))
    if not  LearningLine.objects.filter(id=instance.learning_line_id):
        raise Exception(_("Subject: parent Learning Line not found"))