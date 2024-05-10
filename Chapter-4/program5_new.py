"""
This program provides the user 5 options to enter.
is the user types 1, he can add items into the list
if the user types 2, he will be able to view the list
if the user types 3, random item will be removed from the list
if the user types 4, last item from the list is removed
if the user types 5, the program will end.
"""

import random
stationary_list = []
while True:
    print("Type '1' to add the items into the list")
    print("Type '2' to view the list")
    print("Type '3' to remove a random item rom the list")
    print("Type '4' to remove the last item from the list")
    print("Type '5' to exit the program")

    user_input = int(input())

    if user_input == 1 :
        print('How many items do you want to enter into your list?')
        num_of_items = int(input())
        for i in range(1, num_of_items + 1):
            print('Please type the name of ' + str(i) + ' item.')
            name_of_items = input()
            stationary_list.append(name_of_items)

    elif user_input == 2:
        print("Your list contains " + str(stationary_list))

    elif user_input == 3 :
        item = ''.join(random.choices(stationary_list, k=1))
        stationary_list.remove(item)

    elif user_input == 4 :
        last_item = stationary_list.pop()

    elif user_input == 5 :
        break
