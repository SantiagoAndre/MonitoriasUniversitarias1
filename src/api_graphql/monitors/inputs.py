from graphene import ID
from graphene import Int
from graphene import String
from graphene import InputObjectType

# Create your inputs types here.


class CreateCollegeInput(InputObjectType):
    name = String(required=True)


class UpdateCollegeInput(InputObjectType):
    id = ID(required=True)
    name = String()


class CreateCollegeCareerInput(InputObjectType):
    name = String(required=True)
    description = String(required=True)


class UpdateCollegeCareerInput(InputObjectType):
    id = ID(required=True)
    name = String()
    description = String()


class CreateMonitorInput(InputObjectType):
    name = String(required=True)
    email = String(required=True)
    phone = Int(required=True)
    address = String(required=True)
    family_phone = Int(required=True)
    college_id = ID(required=True)
    career_id = ID(required=True)
    semester = Int(required=True)


class UpdateMonitorInput(InputObjectType):
    id = ID(required=True)
    name = String()
    email = String()
    phone = Int()
    address = String()
    family_phone = Int()
    college_id = ID()
    career_id = ID()
    semester = Int()


class CreateLearningLineInput(InputObjectType):
    name = String(required=True)
    description = String(required=True)
    career_id = ID(required=True)


class UpdateLearningLineInput(InputObjectType):
    id = ID(required=True)
    name = String()
    description = String()
    career_id = ID()


class CreateTopicInput(InputObjectType):
    name = String(required=True)
    description = String(required=True)
    learning_line_id = ID(required=True)


class UpdateTopicInput(InputObjectType):
    id = ID(required=True)
    name = String(required=True)
    description = String(required=True)
    learning_line_id = ID(required=True)


class CreateSubtopicInput(InputObjectType):
    name = String(required=True)
    description = String(required=True)
    topic_id = ID(required=True)


class UpdateSubtopicInput(InputObjectType):
    id = ID(required=True)
    name = String()
    description = String()
    topic_id = ID()


class CreateServiceInput(InputObjectType):
    name = String(required=True)
    description = String(required=True)


class UpdateServiceInput(InputObjectType):
    id = ID(required=True)
    name = String()
    description = String()
