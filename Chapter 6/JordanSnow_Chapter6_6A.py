"""This program is intended to validate phone numbers, social security numbers, and zip codes
using regular expressions. Once the program receives input for all three it will display if they
are valid entries for the specified type. """

# Import the Random Expression module to be used later in the program
import re

# Define "valid_phone_number" and pass in variable "phone_number"
def valid_phone_number(phone_number):

    # Create a variable "pattern" and set it equal to a raw string that identifies
    # the acceptable format of an entered "phone_number"
    pattern = r'^\(?\d{3}\)?[-.\s]\d{3}[-.\s]\d{4}$'

    # Return a boolean expression based off of the result of matching the defined "pattern" and entered "phone_number"
    return bool(re.match(pattern, phone_number))

# Define "phone_number_check" to be used to test if the "valid_phone_number"
# function is working as intended

# def phone_number_check():
#     valid_numbers = ['123-456-7890', '(123) 456-7890', '123 456 7890']
#
#     invalid_numbers = ['1234567890', '123-456-789', '123-456-789a']
#
#     for number in valid_numbers:
#         print(f'{number} is a valid phone number: {valid_phone_number(number)}')
#
#     for number in invalid_numbers:
#         print(f'{number} is a valid phone number: {valid_phone_number(number)}')
#
#
# phone_number_check()


# Define "valid_social_security_number" and pass in variable "ssn"
def valid_social_security_number(ssn):

    # Create a variable "pattern" and set it equal to a raw string that identifies
    # the acceptable format of an entered "ssn"
    pattern = '^(?!666|000|9\\d{2})\\d{3}-(?!00)\\d{2}-(?!0{4})\\d{4}$'

    # Return a boolean expression based off of the result of matching the defined "pattern" and entered "ssn"
    return bool(re.match(pattern, ssn))

# Define "social_security_number_check" to be used to test if the "valid_social_security_number"
# function is working as intended

# def social_security_number_check():
#     valid_ssn = ['876-54-3210', '123-45-6789']
#
#     invalid_ssn = ['000-12-3456', '123-45-0000']
#
#     for social in valid_ssn:
#         print(f'{social} is a valid social security number: {valid_social_security_number(social)}')
#
#     for social in invalid_ssn:
#         print(f'{social} is a valid social security number: {valid_social_security_number(social)}')
#
#
# social_security_number_check()


# Define "valid_zip_code" and pass in variable "zip_code"
def valid_zip_code(zip_code):

    # Create a variable "pattern" and set it equal to a raw string that identifies
    # the acceptable format of an entered "zip_code"
    pattern = r'^\d{5}(?:-\d{4})?$'

    # Return a boolean expression based off of the result of matching the defined "pattern" and entered "zip_code"
    return bool(re.match(pattern, zip_code))

# Define "social_security_number_check" to be used to test if the "valid_social_security_number"
# function is working as intended

# def zip_code_check():
#     valid_codes = ["12345", "12345-6789"]
#     invalid_codes = ["123456", "1234-5678", "abcde-fghi"]
#
#     for code in valid_codes:
#         print(f"{code} is a valid zip code: {valid_zip_code(code)}")
#
#     for code in invalid_codes:
#         print(f"{code} is a valid zip code: {valid_zip_code(code)}")
#
#
# zip_code_check()


# Define main
def main():

    # Create variable "phone_number" and set it equal to the input of a phone number from the user
    phone_number = input("Enter phone number (format is XXX-XXX-XXXX, spaces or hyphens allowed): ")

    # Create variable "ssn" and set it equal to the input of a social security number from the user
    ssn = input("Enter Social Security Number (format is XXX-XX-XXXX, must include hyphens): ")

    # Create variable "zip_code" and set it equal to the input of a zip code from the user
    zip_code = input("Enter zip code (XXXXX): ")

    # Print True/False answer if the entered "phone_number" is valid
    print("Phone number valid:", valid_phone_number(phone_number))

    # Print True/False answer if the entered "ssn" is valid
    print("SSN valid:", valid_social_security_number(ssn))

    # Print True/False answer if the entered "zip_code" is valid
    print("Zip code valid:", valid_zip_code(zip_code))


# Call main
main()
