import re

def valid_phone_number(phone_number):

    pattern = r'^\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}$'

    return bool(re.match(pattern, phone_number))

