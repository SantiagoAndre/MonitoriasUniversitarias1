from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

from .utils import validate_blank_or_none, process_large_text, validate_length, validate_special_characters, validate_float, get_status_position
from .models import Monitor
from .errors import MonitorLen, InconsistentStatusException
from .emails import send_email_status_monitor


# @receiver(pre_delete,sender=Monitor)
# def pre_delete_story(sender, instance, **kwargs):
#     for s in instance.subject.all():
#         s.delete()


@receiver(pre_save, sender=Monitor)
def validate_status_change(sender, instance, **kwargs):
    
    VALID_STATUS_CHANGES = (
        (Monitor.PRESELECTION,Monitor.DISCARDED),
        (Monitor.PRESELECTION,Monitor.TEST),
        (Monitor.TEST,Monitor.DISCARDED),
        (Monitor.TEST,Monitor.SELECTED),
    )
    if instance._state.adding:
        if instance.status != Monitor.PRESELECTION: # Se esta creando
            raise InconsistentStatusException(_("First value Monitor status must be 'PRESELECTION'"))
    elif instance.status_tracker.has_changed("status"):
        previous =  instance.status_tracker.changed()["status"]
        actual = instance.status 
        if (previous,actual) not in VALID_STATUS_CHANGES:
            raise InconsistentStatusException(_("Monitor: cannot change status from %s to %s"%(previous,actual))) 


@receiver(post_save, sender=Monitor)
def send_email(sender, instance, **kwargs):
    if instance.status_tracker.has_changed("status"):
        send_email_status_monitor(instance)

@receiver(pre_save, sender=Monitor)
def monitor_names(sender, instance, **kwargs):
    validate_float(instance.career_average,_("Monitor: career average must to be float not string"))


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
    blank_or_none_message =  _("Monitor: %s  cannot be null or blank")
    validate_blank_or_none(instance.telephone, (blank_or_none_message % _("telephone") ))
    validate_blank_or_none(instance.residence,(blank_or_none_message % _("recidence") ) )
    validate_blank_or_none(instance.level_education,(blank_or_none_message % _("education level") ))
    validate_blank_or_none(instance.college,(blank_or_none_message % _("college") ))
    validate_blank_or_none(instance.college_career, (blank_or_none_message % _("college career") ))
    validate_blank_or_none(instance.first_name, (blank_or_none_message % _("first name") ))
    validate_blank_or_none(instance.last_name,(blank_or_none_message % _("last name") ))
    validate_blank_or_none(instance.email, (blank_or_none_message % _("email") ))
    # print(instance.service_type)
    validate_blank_or_none(instance.service_type,(blank_or_none_message % _("service type") ))


@receiver(pre_save, sender=Monitor)
def monitor_model_len(sender, instance, **kwargs):
    max_length_message = _("Monitor: %s length cannot exceed  %d")
    len_telephone = 10
    len_attr = 50
    validate_length(instance.telephone, len_telephone, (max_length_message % (_("telephone"),len_telephone)))
    validate_length(instance.residence, len_attr, (max_length_message % (_("residence"),len_attr)))
    validate_length(instance.level_education, len_attr, (max_length_message % (_("education level"),len_attr)))
    validate_length(instance.college, len_attr, (max_length_message % (_("college"),len_attr)))
    validate_length(instance.college_career, len_attr, (max_length_message % (_("college career"),len_attr)))
    validate_length(instance.experience, len_attr, (max_length_message % (_("experience"),len_attr)))
    validate_length(instance.service_type, 100, (max_length_message % (_("service type"),100)))


@receiver(pre_save, sender=Monitor)
def monitor_model_special_characteres(sender, instance, **kwargs):
    special_characters_msg= _("Monitor: %s field contains Special Characters")
    validate_special_characters(instance.first_name, (special_characters_msg % _("fist name")))
    validate_special_characters(instance.last_name, (special_characters_msg % _("last name")))
    validate_special_characters(instance.telephone,(special_characters_msg % _("telephone")))
    validate_special_characters(instance.residence, (special_characters_msg % _("residence")))
    validate_special_characters(instance.level_education, (special_characters_msg % _("education level")))
    validate_special_characters(instance.college,(special_characters_msg % _("college")))
    validate_special_characters(instance.college_career,(special_characters_msg % _("college career")))
    validate_special_characters(instance.experience,(special_characters_msg % _("experience")))
    validate_special_characters(instance.service_type,(special_characters_msg % _("fist name")))
