supplies = ['pen', 'paper', 'scissors', 'stappler', 'book']

print('Which supply do you want to check?')
user_input = input()

if user_input in supplies:
    print('Yes, it is there in your supply list.')
elif user_input not in supplies:
    print('It is not in your supply list')

print('If you want to check your supply list (Type yes to view list and type no to exit)')
input = input()

if input == 'yes':
    for i in range(len(supplies)):
        print('Index ' + str(i) + ' in supplies is ' + supplies[i])
elif input == 'no':
    exit