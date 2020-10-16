from .errors import ValidationError
import re

def process_name(name):
    return re.sub(" +", " ",name).strip().title()
def process_large_text(text):
    return re.sub(" +", " ",text).strip()
# validators
def validate_length(value,length,error_messaje):
    if len(value) > length:
        raise ValidationError(error_messaje)
    return value

def validate_blank_or_none(value,error_messaje):
    print("|%s|"% value)
    if value:
        return value
    raise ValidationError(error_messaje)
def validate_special_characters(value,error_messaje):
    print("en validators")
    # Make an RE character set and pass  
    # this as an argument in compile function

    string_check= re.compile('[@_!#$%^&*()<>?/\|}{~:]') 
        
    # Pass the string in search function  
    # of RE object (string_check).
        
    if string_check.search(value): 
        raise ValidationError(error_messaje)
    return value
