from django.db.models.signals import  pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from .utils import process_name,process_large_text
from .models import LearningLine,Subject
from decouple import config
@receiver(pre_save,sender=LearningLine)
def unique_name_learningline(sender,instance, **kwargs):
    instance.name  = process_name(instance.name)
    instance.description = process_large_text(instance.description)
    if LearningLine.objects.filter(name=instance.name):
        raise Exception(_("LearningLine: name already used"))
    print("signal unique ll")
    

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
    print("signal unique ss")

@receiver(pre_save,sender=Subject)
def subject_not_circular_relation(sender,instance, **kwargs):
    parent = instance.parent
    while parent != None:
        if parent == instance:
            raise Exception(_("Subject: Circular relation with parent"))
        parent = parent.parent
@receiver(pre_save,sender=Subject)
def subject_max_deep(sender,instance, **kwargs):
    
    MAX_DEEP_SUBJECT = config("MAX_DEEP_SUBJECT",default=4,cast=int)
    deep = 0
    parent = instance.parent
    while parent != None:
        parent = parent.parent
        deep+=1
    print("wenas deep is %d"% deep)
    if deep> MAX_DEEP_SUBJECT:
        raise Exception(_("Subject: Max subject deep is %d" % MAX_DEEP_SUBJECT))