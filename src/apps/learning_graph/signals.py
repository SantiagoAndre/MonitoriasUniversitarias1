from django.db.models.signals import m2m_changed, pre_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from .utils import process_name
from .models import LearningLine
@receiver(pre_save,sender=LearningLine)
def unique_name_learningline(sender,instance, **kwargs):
    print("in signal")
    instance.name  = process_name(instance.name)

    if LearningLine.objects.filter(name=instance.name):
        raise Exception(_("name already used"))
    else:
        print("name is not used,:D")
