from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .utils import validate_blank_or_none, process_large_text, validate_length, validate_special_characters
from .models import Monitor
from .errors import MonitorLen
from decouple import config

# @receiver(pre_delete,sender=Monitor)
# def pre_delete_story(sender, instance, **kwargs):
#     for s in instance.subject.all():
#         s.delete()


@receiver(pre_save, sender=Monitor)
def monitor_names(sender, instance, **kwargs):
    instance.telephone = process_large_text(instance.telephone)
    instance.residence = process_large_text(instance.residence)
    instance.level_education = process_large_text(instance.level_education)
    instance.college = process_large_text(instance.college)
    instance.college_career = process_large_text(instance.college_career)
    instance.first_name = process_large_text(instance.first_name)
    instance.last_name = process_large_text(instance.last_name)
    instance.email = process_large_text(instance.email)

@receiver(pre_save, sender=Monitor)
def monitor_model_null_or_none(sender, instance, **kwargs):
    validate_blank_or_none(instance.telephone, _(
        "Monitor: telephone cannot be null or blank"))
    validate_blank_or_none(instance.residence, _(
        "Monitor: residence cannot be null or blank"))
    validate_blank_or_none(instance.level_education, _(
        "Monitor: level education cannot be null or blank"))
    validate_blank_or_none(instance.college, _(
        "Monitor: college cannot be null or blank"))
    validate_blank_or_none(instance.college_career, _(
        "Monitor: college career cannot be null or blank"))
    validate_blank_or_none(instance.first_name, _(
        "Monitor: first_name cannot be null or blank"))
    validate_blank_or_none(instance.last_name, _(
        "Monitor: last name cannot be null or blank"))
    validate_blank_or_none(instance.email, _(
        "Monitor: email cannot be null or blank"))

@receiver(pre_save, sender=Monitor)
def monitor_model_len(sender, instance, **kwargs):
    len_telephone = 10
    len_attr = 50
    validate_length(instance.telephone, len_telephone, _(
        "Monitor: telephone length cannot exceed  %d" % len_telephone))
    validate_length(instance.residence, len_attr, _(
        "Monitor: residence length  cannot exceed  %d" % len_attr))
    validate_length(instance.level_education, len_attr, _(
        "Monitor: level education length cannot exceed  %d" % len_attr))
    validate_length(instance.college, len_attr, _(
        "Monitor: college length  cannot exceed  %d" % len_attr))
    validate_length(instance.college_career, len_attr, _(
        "Monitor: college career length cannot exceed  %d" % len_attr))
    validate_length(instance.experience, len_attr, _(
        "Monitor: experience length  cannot exceed  %d" % len_attr))
    validate_length(instance.service_type, len_attr, _(
        "Monitor: service type length cannot exceed  %d" % len_attr))


@receiver(pre_save, sender=Monitor)
def monitor_model_len(sender, instance, **kwargs):
    validate_special_characters(instance.first_name, _(
        "Monitor: first name field contains Special Characters"))
    validate_special_characters(instance.last_name, _(
        "Monitor: last name field contains Special Characters"))
    validate_special_characters(instance.telephone, _(
        "Monitor: telephone field contains Special Characters"))
    validate_special_characters(instance.residence, _(
        "Monitor: residence field contains Special Characters"))
    validate_special_characters(instance.level_education, _(
        "Monitor: level education field contains Special Characters"))
    validate_special_characters(instance.college, _(
        "Monitor: college field contains Special Characters"))
    validate_special_characters(instance.college_career, _(
        "Monitor: college career field contains Special Characters"))
    validate_special_characters(instance.experience, _(
        "Monitor: experience field contains Special Characters"))
    validate_special_characters(instance.service_type, _(
        "Monitor: service type field contains Special Characters"))
