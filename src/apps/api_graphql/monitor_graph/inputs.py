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
    subject = List(of_type=ID, required=True)

    experience = String(required=True)
    service_type = List(of_type=String, required=True)
    short_job = Boolean(required=True)
    career_average = Float(required=True)
    work_hour = Int(required=True)
    informatic_tool = String(required=True)


class UpdateMonitorInput(InputObjectType):
    id = ID(required=True)
    status = String(required=True)

class UpdateIsActiveInput(InputObjectType):
    id = ID(required=True)
    is_active=Boolean(required=True)