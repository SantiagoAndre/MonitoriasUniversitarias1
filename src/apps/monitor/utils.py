from .errors import ValidationError
import re


def process_name(name):
    return re.sub(" +", " ", name).strip().title()


def process_large_text(text):
    return re.sub(" +", " ", text).strip()


def validate_length(value, length, error_message):
    if value != None:
        if len(value) > length:
            raise ValidationError(error_message)
    return value


def validate_blank_or_none(value, error_message):
    if value:
        return value
    raise ValidationError(error_message)


def validate_special_characters(value, error_message):
    string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if value != None:
        if string_check.search(value):
            raise ValidationError(error_message)
    return value

def validate_float(value, error_message):
    try:
        value = float(value)
    except expression as identifier:
        raise ValidationError(error_message)

def get_status_position(status, STATUS_TUPLE):
    for i,(vstatus,_) in enumerate(STATUS_TUPLE):
        if vstatus == status:
            return i
    return -1