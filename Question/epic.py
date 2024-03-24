# Write a Python program using regular expressions to validate the Electors Photo Identity Card (EPIC). its an identification proof for Indian citizens over the age of 18 years. Given some Voter ids, the task is to check if they are valid or not using regular expressions. The rules for the valid EPIC are as follows:
# EPIC Number is a unique alphanumeric code. combination of alphabets (A to Z)and digits (0 to 9).
# Its length should equal to 10. (3 Alphabets and 7 digits)
# EPIC Number starts with an alphabet and ends with a digit.
# EPIC number does not contain whitespaces and other special characters.
# EPIC number allows only Uppercase letters.

import re
userinput=input("Enter your EPIC number :")
userinput=userinput.upper()
exp="[A-Z]{3}[0-9]{7}"
randomvariable=re.compile(exp)
if(re.search(randomvariable,userinput)and len(userinput)==10):
    print(userinput + " is valid")
else:
    print(userinput + " is not valid")
