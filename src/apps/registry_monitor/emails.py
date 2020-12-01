
from django.core.mail import EmailMultiAlternatives
from django.template.loader  import get_template
from django.utils.translation import gettext_lazy as _
from .models import RegistryMonitor
from core import settings 
INFO_EMAIL = {
    RegistryMonitor.PRESELECTION:{
        "subject": _("Successful Registration"),
        "template": "emails/registered.html",
    },
    RegistryMonitor.TEST:{
        "subject": _("Welcome to trial period"),
        "template": "emails/trial_period.html",
    },
    RegistryMonitor.SELECTED:{
        "subject": _("Welcome to the Monitorías Universitarias Team"),
        "template": "emails/selected.html",
    }
}
def send_email_status_monitor(monitor):
    print("name; ",monitor.first_name)
    if monitor.status not in INFO_EMAIL:
        return
    info_email  = INFO_EMAIL[monitor.status]
    content = get_template(info_email["template"]).render(context = {"username": monitor.first_name})
    sender = getattr(settings, "EMAIL_HOST_USER","test@monitoriasuniversitarias.co")
    to = [monitor.email]
    email = EmailMultiAlternatives(
        info_email["subject"],
        _("Monitorías Universitarias hiring process"),
        sender,
        to
    )
    email.attach_alternative(content,"text/html")
    try:
        email.send()
    except:
        print("Internal Error: Internal Error Sending Email.")


