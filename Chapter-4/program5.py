import random
stationary_list = []

print('How many items do you want to enter into your list?')  # asking user to enter the number of items to add into your list
user_input = int(input())


for i in range(1, user_input + 1):
    print('Please type the name of ' + str(i) + ' item.')
    input_list = input()
    stationary_list.append(input_list)

print('Your list contains ' + str(stationary_list))  # prints the final list of items
print("")
print('Do you want to remove an item from the list randomly or remove the last item from the list?') # asking the user whehter to remove an item from the list 
print("Type 'random' to remove random item from the list")
print("Type 'last item' to remove item which is at the end of the list")
user_answer = input()
user_lowerletter = user_answer.lower()  # converts the users input into lower letters

# if user_answer is random, the word will be removed from the list randomly, 
# if user_answer is last item then the last item will be removed from the list

if user_lowerletter == 'random':
      remove_word = ''.join(random.choices(stationary_list, k=1))
      stationary_list.remove(remove_word)
      print('The item which is removed from the list is: ' + str(remove_word))
      print('The final list contains ' + str(stationary_list))

elif user_lowerletter == 'last item':
    del stationary_list[user_input - 1]
    print("The final list contains: " + str(stationary_list))

else:
     print("Please type correct word")
    