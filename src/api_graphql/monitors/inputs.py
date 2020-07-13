from graphene import ID
from graphene import Int
from graphene import String
from graphene import Boolean
from graphene import DateTime
from graphene import InputObjectType

# Create your inputs types here.


class CreateCollegeInput(InputObjectType):
    name = String(required=True)


class UpdateCollegeInput(InputObjectType):
    id = ID(required=True)
    name = String()


class CreateCareerInput(InputObjectType):
    name = String(required=True)
    description = String(required=True)

    college_id = ID(required=True)


class UpdateCareerInput(InputObjectType):
    id = ID(required=True)
    name = String()
    description = String()

    college_id = ID()


class CreateCityInput(InputObjectType):
    name = String(required=True)


class UpdateCityInput(InputObjectType):
    id = ID(required=True)
    name = String()


class CreateContactInput(InputObjectType):
    address = String(required=True)
    phone = Int(required=True)
    family_phone = Int(required=True)

    city_id = ID(required=True)


class UpdateContactInput(InputObjectType):
    id = ID(required=True)
    address = String()
    phone = Int()
    family_phone = Int()

    city_id = ID()


class CreateMonitorInput(InputObjectType):
    first_name = String(required=True)
    last_name = String(required=True)
    email = String(required=True)
    semester = Int(required=True)

    contact_id = ID(required=True)
    # TODO: m2m careers


class UpdateMonitorInput(InputObjectType):
    id = ID(required=True)
    first_name = String()
    last_name = String()
    email = String()
    semester = Int()

    contact_id = ID()
    # TODO: m2m careers


class CreateServiceInput(InputObjectType):
    name = String(required=True)
    description = String()

    monitor_id = ID(required=True)


class UpdateServiceInput(InputObjectType):
    id = ID(required=True)
    name = String()
    description = String()

    monitor_id = ID()


class CreateSkillInput(InputObjectType):
    name = String(required=True)
    # TODO: m2m monitors


class UpdateSkillInput(InputObjectType):
    id = ID(required=True)
    name = String()
    # TODO: m2m monitors


class CreateClientInput(InputObjectType):
    first_name = String(required=True)
    last_name = String(required=True)
    email = String(required=True)


class UpdateClientInput(InputObjectType):
    id = ID(required=True)
    first_name = String()
    last_name = String()
    email = String()


class CreateQuoationInput(InputObjectType):
    # TODO: define field file
    acepted = Boolean()
    created = DateTime()
    expiration = DateTime()
    delivery = DateTime()
    price = Int()

    monitor_id = ID(required=True)
    client_id = ID(required=True)


class UpdateQuoationInput(InputObjectType):
    id = ID(required=True)
    # TODO: define field file
    acepted = Boolean(required=True)
    created = DateTime(required=True)
    expiration = DateTime(required=True)
    delivery = DateTime(required=True)
    price = Int(required=True)

    monitor_id = ID()
    client_id = ID()
