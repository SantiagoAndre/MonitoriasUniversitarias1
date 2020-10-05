import re

def process_name(name):
    return re.sub(" +", " ",name).strip().title()
def process_large_text(text):
    return re.sub(" +", " ",text).strip()