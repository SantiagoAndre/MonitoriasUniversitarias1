from graphene import InputObjectType
from graphene import String, Boolean, List, ID


class MonitorInput(InputObjectType):
    first_name = String(required=True)
    last_name = String(required=True)
    email = String(required=True)
    telephone = String(required=True)
    residence = String(required=True)
    level_education = String(required=True)
    college = String(required=True)
    college_career = String(required=True)
    subject = List(of_type=ID)

    experience = String()
    service_type = String()
    short_job = Boolean()
    # username = String(required=True)
    # password = String(required=True)
    # is_superuser = Boolean()
    # is_staff = Boolean()
