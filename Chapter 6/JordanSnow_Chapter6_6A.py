import re

def valid_phone_number(phone_number):

    pattern = r'^\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}$'

    return bool(re.match(pattern, phone_number))

valid_numbers = ['123-456-7890', '(123) 456-7890', '123 456 7890']

invalid_numbers = ['1234567890', '123-456-789', '123-456-789a']

for number in valid_numbers:
    print(f'{number} is a valid phone number: {valid_phone_number(number)}')

for number in valid_numbers:
    print(f'{number} is a valid phone number: {valid_phone_number(number)}')

def valid_social_security_number(ssn):
    pattern = '^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$'
    match = re.match(pattern, ssn)
    return bool(match)

valid_ssn = ['123 45 6789', '987 65 4321', '123-45-6789']

invalid_ssn = ['000 12 3456', '123 45 0000']

