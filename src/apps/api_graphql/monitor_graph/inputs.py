from graphene import InputObjectType
from graphene import String, Boolean, List, ID, Float, Int


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

    experience = String(required=True)
    service_type = List(of_type=String, required=True)
    short_job = Boolean()
    career_average = Float()
    work_hour = Int()
    informatic_tool = String()
    # username = String(required=True)
    # password = String(required=True)
    # is_superuser = Boolean()
    # is_staff = Boolean()


class UpdateMonitorInput(InputObjectType):
    id = ID(required=True)
    status = String(required=True)
