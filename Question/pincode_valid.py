"""
Write a REGEX to validate the pin code of India
Test Cases:
1. It can be only six digits.
2. It should not start with zero.
3. First digit of the pin code must be from 1 to 9.
4. Next five digits of the pin code may range from 0 to 9.
5. It should allow only one white space, but after three digits,
although this is optional.
"""

import re

def validate_pin_code(pin):
    # Define the regular expression pattern for a valid Indian pin code
    pattern = re.compile(r'^[1-9][0-9]{2}\s?\d{3}$')

    # Check if the pin code matches the pattern
    if pattern.match(pin):
        return "Valid Pin Code"
    else:
        return "Invalid Pin Code"

# Test Cases
test_case_1 = "123456"
test_case_2 = "012345"
test_case_3 = "98765"
test_case_4 = "400 099"

print(f"Input 1: {test_case_1}")
print(f"Output 1: {validate_pin_code(test_case_1)}\n")

print(f"Input 2: {test_case_2}")
print(f"Output 2: {validate_pin_code(test_case_2)}\n")

print(f"Input 3: {test_case_3}")
print(f"Output 3: {validate_pin_code(test_case_3)}\n")

print(f"Input 4: {test_case_4}")
print(f"Output 4: {validate_pin_code(test_case_4)}\n")
