import re
EmailID=input("Please enter your EmailId:")
exp="[a-z]{12}[.]{1}[a-z]{5}[0-9]{4}[@]{1}[a-z]{10}[.]{1}[a-z]{2}[.]{1}[a-z]{2}"
p=re.compile(exp)
if(re.search(p,EmailID)and len(EmailID)==39):
    print("valid")
else:
    print("Invalid")

#Input Email Id : vinayakkumar.singh2023@vitstudent.ac.in
