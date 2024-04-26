import sys

while True:
    print('Type exit to exit.')
    user_input = input()
    if user_input == 'exit':
        sys.exit()
    print('You typed ' + str(user_input) + '.')
    