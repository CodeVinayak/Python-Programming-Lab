# . RTO wants to validate the Indian driving license number of five license 
# holders. Write a Python program using functions and applying appropriate 
# regular expressions to validate and return the Boolean expression affirming its 
# validity with a reason following the criteria specified below.
# • It should be 16 characters long
# • The first two characters should be upper-case alphabets that represent the
# • state code.
# • The next two characters (i.e., RTO code) should be digits with a hyphen
# placed after the state code (Example: TN-0619850034761) or a 
# whitespace to be included after the digits (Example: TN06 19850034761)
# • The next four characters should be digits that represent the license issued
# • from the year 1900 to 2030.
# • The next seven characters should be any digits from 0-9.
# Raise an exception that will be handled when the first two characters are not 
# uppercase alphabets. Create a file and store all the input and output processed 
# into a text file.
# Sample Input1:
# Input: str = “GJ-2420180”;
# Output: False
# Sample Input 2:
# Input: str = “HR-0619850034761”;
# Output: True
# Explanation: Valid driving license

import re

def validate_license_number(license_number):
    pattern = re.compile(r'^[A-Z]{2}[-\s]?\d{2}[-\s]?\d{4}\d{7}$')

    if not pattern.match(license_number):
        return False, "Invalid license number. Check the format and try again."
    return True, "Valid driving license."

# Sample Input 1
input_str1 = "GJ-2420180"
is_valid1, reason1 = validate_license_number(input_str1)
print(f"Input 1: {input_str1}")
print(f"Output 1: {is_valid1}")
print(f"Reason 1: {reason1}\n")

# Sample Input 2
input_str2 = "HR-0619850034761"
is_valid2, reason2 = validate_license_number(input_str2)
print(f"Input 2: {input_str2}")
print(f"Output 2: {is_valid2}")
print(f"Reason 2: {reason2}\n")

# Store the inputs and outputs in a text file
with open("license_validation_output.txt", "w") as file:
    file.write(f"Input 1: {input_str1}\n")
    file.write(f"Output 1: {is_valid1}\n")
    file.write(f"Reason 1: {reason1}\n\n")
    file.write(f"Input 2: {input_str2}\n")
    file.write(f"Output 2: {is_valid2}\n")
    file.write(f"Reason 2: {reason2}\n")
