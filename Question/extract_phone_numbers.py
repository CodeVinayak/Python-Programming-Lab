# Suppose a company has some old data that contains phone numbers but unfortunately the data is mixed up with some special characters as shown in example given below.
# Your task is to extract valid phone numbers that contains ten digits. For example, if the string is "123-456-7890 or 555-555-1212", you should extract 1234567890", and "5555551212". Write a Python program using regular expressions to accomplish the above task and also convert the extracted number into digits.

import re

# Input string with mixed data and phone numbers
input_string = "Some text with phone numbers: 123-456-7890 or 555-555-1212 and more."

# Compile the regular expression pattern
pattern = re.compile(r'\d{10}')

# Find all matches in the input string
matches = re.findall(pattern, input_string)

# Remove dashes and convert matches to digits
phone_numbers = [re.sub(r'-', '', match) for match in matches]

# Print the extracted phone numbers as digits
for number in phone_numbers:
    print(number)
