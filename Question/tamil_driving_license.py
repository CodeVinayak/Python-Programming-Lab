"""
Write a Python script to check the validity of a driving license using regular expression.
It should be sixteen characters long
The first two characters should be an upper case alphabet.
The third and fourth characters should be a number. The range should be 01-99.
The fifth character should be a white space.
The next four characters should be a number, but the first two characters should be either 19 or 20 and the third and fourth characters should be any number range between 00-99.
The last seven characters is a license numbers. It should be only numbers ranging between 0000001 -9999999.
Sample Test Cases:
Input 1: TN09.20181563489
Output 1: Valid Driving License
Input 2: TN16 16450265478
Output 2: Invalid Driving License
"""
import re

def check_license_validity(license_number):
    # Define the correct regular expression pattern for a valid driving license
    pattern = re.compile(r'^[A-Z]{2}\d{2}\s(?:19|20)\d{2}\d{7}$')

    # Check if the license number matches the pattern
    if pattern.match(license_number):
        return "Valid Driving License"
    else:
        return "Invalid Driving License"

# Corrected Sample Test Cases
test_case_1 = "TN09 20181563489"
test_case_2 = "TN16 16450265478"

# Output the results
print(f"Input 1: {test_case_1}")
print(f"Output 1: {check_license_validity(test_case_1)}\n")

print(f"Input 2: {test_case_2}")
print(f"Output 2: {check_license_validity(test_case_2)}")
