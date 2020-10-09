from django.db.models.signals import  pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from core.settings import MAX_DEEP_SUBJECT
from .utils import process_name,process_large_text
from .models import LearningLine,Subject
from decouple import config
from .errors import NameAlreadyUsedException,ParentLearningLineNotFoundException,ParentSubjectNotFoundException,SubjectCircularRealtionException,MaxDeepSubjectException

@receiver(pre_save,sender=LearningLine)
def unique_name_learningline(sender,instance, **kwargs):
    instance.name  = process_name(instance.name)
    instance.description = process_large_text(instance.description)
    other_objects = Subject.objects.filter(name=instance.name)
    if other_objects and other_objects[0].id != instance.id:
        raise NameAlreadyUsedException(_("LearningLine: name already used"))
    print("signal unique ll")
    

@receiver(pre_save,sender=Subject)
def unique_name_subject(sender,instance, **kwargs):
    instance.name  = process_name(instance.name)
    instance.description = process_large_text(instance.description)
    other_subjects = Subject.objects.filter(name=instance.name)
    if other_subjects and other_subjects[0].id != instance.id:
        raise NameAlreadyUsedException(_("Subject: name already used"))
    if instance.parent_id and not Subject.objects.filter(id=instance.parent_id):
        raise ParentSubjectNotFoundException(_("Subject: parent Subject not found"))
    if instance.learning_line_id and not  LearningLine.objects.filter(id=instance.learning_line_id):
        raise ParentLearningLineNotFoundException(_("Subject: parent Learning Line not found"))
    print("signal unique ss")

@receiver(pre_save,sender=Subject)
def subject_not_circular_relation(sender,instance, **kwargs):
    deep = 0
    parent = instance.parent
    while parent != None:
        if parent == instance:
            raise SubjectCircularRealtionException(_("Subject: Circular relation with parent"))
        parent = parent.parent
        deep+=1   
    if deep> MAX_DEEP_SUBJECT:
        raise MaxDeepSubjectException(_("Subject: Max subject deep is %d" % MAX_DEEP_SUBJECT))