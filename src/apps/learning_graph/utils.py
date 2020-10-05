import re

def process_name(name):
    return re.sub(" +", " ",name).strip().title()
