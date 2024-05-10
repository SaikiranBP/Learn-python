"""
This is a stationary list, which provides the user 5 options:
1: To add items into the list
2: To view the list
3: To remove random item from the list
4: To remove the last item from the list
5: To quit the program
"""
import random

print("---------STATIONARY LIST---------")
stationary_list = []
while True:
    print("Please choose from the below options")
    print("1: To add items into the list")
    print("2: To view the list")
    print("3: To remove the random item from the list")
    print("4: To remove the last item from the list")
    print("5: Quit")

    user_input = int(input())
    try:
        if user_input == 1 :
            print('How many items do you want to enter into your list?')
            num_of_items = int(input())
            for i in range(1, num_of_items + 1):
                print('Please type the name of ' + str(i) + ' item.')
                name_of_item = input()
                stationary_list.append(name_of_item)

        elif user_input == 2 :
            print("Your list contains " + str(stationary_list))

        elif user_input == 3 :
            ITEM = ''.join(random.choices(stationary_list, k=1))
            stationary_list.remove(ITEM)

        elif user_input == 4 :
            last_item = stationary_list.pop()

        elif user_input == 5 :
            break

    except IndexError:
        print("The list is empty. Add items into the list.")
    