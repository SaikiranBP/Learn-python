"""
This program is written using regular expressions.
This program validates the password if all the given conditions satisfy.
Conditions:
    1. The password should contain minimum 8 characters
    2. The password should contain uppercase letters, lowercase letters,
       special charcters and numbers
"""

import re

def validate_pass(passoword): 
    
    if len(passoword) < 8:
        return "Length of password should be more than 8"
    
    if not re.search("[A-Z]", passoword):
        return "Password must conatain uppercase letters"
    
    if not re.search("[a-z]", passoword):
        return "Password must contain lowercase letters"
    
    if not re.search("\d", passoword):
        return "Password must contain digits"
    
    if not re.search("[!@#$%^&*()-_?/]+", passoword):
        return "Password must contain atleast one special character"
    
    confirm_pass = input("Confirm the password: ")
    
    if confirm_pass == passoword:
        return "Password validation successfull"
    else:
        return "Password validation unsuccessfull"


input_pass = input("Enter password: ")
print(validate_pass(input_pass))