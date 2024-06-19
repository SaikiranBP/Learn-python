"""
This program is all about converting the given input by the user
to lower letters and matching it with the actual password.
"""
while True:
    print("What is the password?")
    user_pass = input()
    if user_pass.lower() == 'swordfish':
        print("Access granted")
        break
    elif user_pass.lower() != 'swordfish':
        print("You have typed the wrong password!")
