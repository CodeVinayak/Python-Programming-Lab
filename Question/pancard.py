import re
PancardNo=input("Please enter your pancard No:")
exp="[A-Z]{5}[0-9]{4}[A-Z]{1}"
p=re.compile(exp)
if(re.search(p,PancardNo)and len(PancardNo)==10):
    print("valid")
else:
    print("Invalid")