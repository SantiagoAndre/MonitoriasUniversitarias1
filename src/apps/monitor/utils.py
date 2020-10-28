from .errors import ValidationError
import re


def process_name(name):
    return re.sub(" +", " ", name).strip().title()


def process_large_text(text):
    return re.sub(" +", " ", text).strip()


def validate_length(value, length, error_message):
    if len(value) > length:
        raise ValidationError(error_message)
    return value


def validate_blank_or_none(value, error_message):
    print("|%s|" % value)
    if value:
        return value
    raise ValidationError(error_message)


def validate_special_characters(value, error_message):
    string_check = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if string_check.search(value):
        raise ValidationError(error_message)
    return value
