"""
This program asks the user to enter the age,
then the user_age is checked whether it is of only numerics,
if the user_age is not of numerics, then program asks the user 
to enter the age in numbers
In second block of code, programs asks the user to type their password
if the password is combination of algebric and numeric then program breaks,
if the password is other than nummerics and algebric,
then program asks the user to enter the password again.
"""
while True:
    print("Enter your age:")
    user_age = input()
    if user_age.isdecimal():
        break
    print("Type your age in numbers")
while True:
    print("Type your new password. (Should consists only of letters and numbers)")
    user_pass = input()
    if user_pass.isalnum():
        break
    print("Password must contain only letters and numbers")
