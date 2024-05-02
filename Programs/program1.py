import random
import string

print('What should be the length of your password?  (Only intergers)')
user_input = int(input())

password = string.ascii_letters + string.digits + string.punctuation

user_password = ''.join(random.choices(password, k=user_input))
print('Your password is ' + str(user_password))

