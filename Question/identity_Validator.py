"""
Write a REGEX to validate Identifier
Test Cases:
1. It must start with either lower case alphabet[a-z] or upper
case alphabet[A-Z] or
underscore()
2. It should be a single word, the white spaces are not allowed.
3. It should not start with digits.
"""
import re

def validate_identifier(identifier):
    # Define the regular expression pattern for a valid identifier
    pattern = re.compile(r'^[a-zA-Z_]\w*$')

    # Check if the identifier matches the pattern
    if pattern.match(identifier):
        return "Valid Identifier"
    else:
        return "Invalid Identifier"

# Test Cases
test_case_1 = "my_identifier"
test_case_2 = "123_identifier"
test_case_3 = "_underscore_identifier"
test_case_4 = "Invalid Identifier"

print(f"Input 1: {test_case_1}")
print(f"Output 1: {validate_identifier(test_case_1)}\n")

print(f"Input 2: {test_case_2}")
print(f"Output 2: {validate_identifier(test_case_2)}\n")

print(f"Input 3: {test_case_3}")
print(f"Output 3: {validate_identifier(test_case_3)}\n")

print(f"Input 4: {test_case_4}")
print(f"Output 4: {validate_identifier(test_case_4)}\n")
