import re


def valid_phone_number(phone_number):

    pattern = r'^\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}$'

    return bool(re.match(pattern, phone_number))


def phone_number_check():
    valid_numbers = ['123-456-7890', '(123) 456-7890', '123 456 7890']

    invalid_numbers = ['1234567890', '123-456-789', '123-456-789a']

    for number in valid_numbers:
        print(f'{number} is a valid phone number: {valid_phone_number(number)}')

    for number in invalid_numbers:
        print(f'{number} is a valid phone number: {valid_phone_number(number)}')


phone_number_check()


def valid_social_security_number(ssn):
    pattern = '^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$'
    match = re.match(pattern, ssn)
    return bool(match)


def social_security_number_check():
    valid_ssn = ['876-54-3210', '123-45-6789']

    invalid_ssn = ['000-12-3456', '123-45-0000']

    for social in valid_ssn:
        print(f'{social} is a valid social security number: {valid_social_security_number(social)}')

    for social in invalid_ssn:
        print(f'{social} is a valid social security number: {valid_social_security_number(social)}')


social_security_number_check()


def valid_zip_code(zip_code):

    pattern = r'^\d{5}(?:-\d{4})?$'

    return bool(re.match(pattern, zip_code))


def zip_code_check():
    valid_codes = ["12345", "12345-6789"]
    invalid_codes = ["123456", "1234-5678", "abcde-fghi"]

    for code in valid_codes:
        print(f"{code} is a valid zip code: {valid_zip_code(code)}")

    for code in invalid_codes:
        print(f"{code} is a valid zip code: {valid_zip_code(code)}")


zip_code_check()


def main():
    phone_number = input("Enter phone number (format is XXX-XXX-XXXX, spaces or hyphens allowed): ")
    ssn = input("Enter Social Security Number (format is XXX-XX-XXXX, must include hyphens): ")
    zip_code = input("Enter zip code (XXXXX): ")

    print("Phone number valid:", valid_phone_number(phone_number))
    print("SSN valid:", valid_social_security_number(ssn))
    print("Zip code valid:", valid_zip_code(zip_code))


main()
