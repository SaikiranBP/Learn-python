"""
This program is written using regular expressions.
This program validates the password if all the given conditions satisfy.
Conditions:
    1. The password should contain minimum 8 characters
    2. The password should contain uppercase letters, lowercase letters,
       special charcters and numbers.
    3. The password should start with uppercase letter
"""
import re

def validate_password():
    if not re.search("^[A-Z]", password):
        return "Password must start with uppercase letter"
    
    if not re.search("[a-z]", password):
        return "Password must contain lowercase letters"
    
    if not re.search("[A-Z]", password):
        return "Password must contain uppercase letters"
    
    if len(password) < 8:
        return "Password must contain minimum 8 characters"
    
    if not re.search("\d", password):
        return "Password must contain numbers"
    
    if not re.search("[!@#$%^&*()_-]", password):
        return "Password must contain atleast one special character"
    
    confirm_password = input("Confirm the password: ")

    if confirm_password == password:
        return "Password validation successful"
    else:
        return "Password validation unsuccessful"

password = input("Type the password: ")
print(validate_password())
