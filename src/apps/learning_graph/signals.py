from django.db.models.signals import  pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from core.settings import MAX_DEEP_SUBJECT
from .utils import process_name,process_large_text, validate_blank_or_none, validate_length, validate_special_characters
from .models import Subject
from decouple import config
from .errors import NameAlreadyUsedException,ParentSubjectNotFoundException,SubjectCircularRealtionException,MaxDeepSubjectException
'''
@receiver(pre_save,sender=LearningLine)
def unique_name_learningline(sender,instance, **kwargs):
    instance.name  = process_name(instance.name)
    instance.description = process_large_text(instance.description)
    other_objects = LearningLine.objects.filter(name=instance.name)
    if other_objects and other_objects[0].id != instance.id:
        raise NameAlreadyUsedException(_("LearningLine: name already used"))
    
    
'''

    
#bussines verifications
@receiver(pre_save,sender=Subject)
def unique_name_subject(sender,instance, **kwargs):
    instance.name  = process_name(instance.name)
    instance.description = process_large_text(instance.description)
    other_subjects = Subject.objects.filter(name=instance.name)
    if other_subjects and other_subjects[0].id != instance.id:
        raise NameAlreadyUsedException(_("Subject: name already used"))
    if instance.parent_id and not Subject.objects.filter(id=instance.parent_id):
        raise ParentSubjectNotFoundException(_("Subject: parent Subject not found"))
'''    
    if instance.learning_line_id and not  LearningLine.objects.filter(id=instance.learning_line_id):
        raise ParentLearningLineNotFoundException(_("Subject: parent Learning Line not found"))
''' 

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

#models validations
@receiver(pre_save,sender=Subject)
def subject_model_validations(sender,instance, **kwargs):
    len_name = 100
    len_description = 200
    validate_blank_or_none(instance.name, _("Subject: Name cannot be null or black"))
    validate_blank_or_none(instance.description, _("Subject: Description cannot be null or black"))
    validate_length(instance.name,len_name, _("Subject: Name length cannot exceed  %d"%len_name))
    validate_length(instance.description,len_description, _("Subject: Description length  cannot exceed  %d"%len_description))
    validate_special_characters(instance.name,_("Subject: Name field contains Special Characters"))
    validate_special_characters(instance.description,_("Subject: Description field contains Special Characters"))
