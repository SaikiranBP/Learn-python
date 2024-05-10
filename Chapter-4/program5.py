import random
stationary_list = []
# asking user to enter the number of items to add into your list
print('How many items do you want to enter into your list?')
user_input = int(input())


for i in range(1, user_input + 1):
    print('Please type the name of ' + str(i) + ' item.')
    input_list = input()
    stationary_list.append(input_list)

print('Your list contains ' + str(stationary_list)) # prints the final list of items 

# if user_answer is random, the word will be removed from the list randomly, 
# if user_answer is last item then the last item will be removed from the list

while True:
    print()
    print("Type 'random' to remove random item from the list") 
    print("Type 'last item' to remove item which is at the end of the list")
    print("Type 4 to exit")

    user_answer = input()
    user_lowerletter = user_answer.lower() # converts the users input into lower letters

    if user_lowerletter == 'random':
        remove_word = ''.join(random.choices(stationary_list, k=1))
        stationary_list.remove(remove_word)
        print("The list contains: " + str(stationary_list))
        print("To view the popped item Type pop")
        pop_word = input()
        if pop_word == 'pop':
            print(remove_word)
        else:
            continue

    elif user_lowerletter == 'last item':
        deleted_word = stationary_list.pop()
        print("Your final list contains: " + str(stationary_list))
        print("To view the popped item Type pop")
        pop_word1 = input()
        if pop_word1 == 'pop':
            print(deleted_word)
        else:
            continue

    elif user_lowerletter == '4':
        break

    else:
        continue