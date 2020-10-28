from django.db.models.signals import pre_save, pre_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .utils import validate_blank_or_none, validate_length, validate_special_characters
from .models import Monitor
from .errors import MonitorLen
from decouple import config

# @receiver(pre_delete,sender=Monitor)
# def pre_delete_story(sender, instance, **kwargs):
#     for s in instance.subject.all():
#         s.delete()


@receiver(pre_save, sender=Monitor)
def monitor_model_validations(sender, instance, **kwargs):
    len_telephone = 10
    len_attr = 50
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
