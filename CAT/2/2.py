# Write a generalized Python Code to read a phone number in the pattern 415-555-4242 as input from the user and pass it as a parameter through the functions.
# Write a function called isphonenumber () to recognize the above pattern without using regular expression and another function chkphonenumber() to recognize the same pattern using regular expression. 

import re
def isphonenumber(phone_number):
    # Function to recognize phone number pattern without using regular expression
    if len(phone_number) != 12:
        return False
    for i in range(0, 3):
        if not phone_number[i].isdecimal():
            return False
    if phone_number[3] != '-':
        return False
    for i in range(4, 7):
        if not phone_number[i].isdecimal():
            return False
    if phone_number[7] != '-':
        return False
    for i in range(8, 12):
        if not phone_number[i].isdecimal():
            return False
    return True

def chkphonenumber(phone_number):
    # Function to recognize phone number pattern using regular expression
    pattern = re.compile(r'^\d{3}-\d{3}-\d{4}$')
    return bool(pattern.match(phone_number))

# Reading phone number from the user
user_input = input("Enter a phone number in the pattern 415-555-4242: ")

# Checking using isphonenumber function
result_without_regex = isphonenumber(user_input)
print("Result without regex:", result_without_regex)

# Checking using chkphonenumber function
result_with_regex = chkphonenumber(user_input)
print("Result with regex:", result_with_regex)