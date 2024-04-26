while True:
    print('Who are you?')
    user_name = input()
    if user_name != 'Sai':
        continue
    print('Hello Sai, what is the password')
    user_pass = input()
    if user_pass == 'Swordfish':
        break
print('Thank you.')
