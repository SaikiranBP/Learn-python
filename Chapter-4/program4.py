print('***********STATIONARY-LIST***********')

stationary_list = []

print('How many items do you want to enter into your list?')
user_input = int(input())

for i in range(1, user_input + 1):
    print('Please type the name of ' + str(i) + ' the item.')
    input_list = input()
    stationary_list.append(input_list)
print('Your list contains ' + str(stationary_list))

print('Do you want to sort your list?')
user_answer = input()

if user_answer == 'yes':
    stationary_list.sort()
    print('Your list after sorting is ' + str(stationary_list))
else:
    exit