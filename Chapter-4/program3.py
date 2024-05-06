# this program finds the finds the item in the list

supplies = ['pen', 'book', 'paper', 'eraser', 'scissor', 'scale', 'colours', 'paint']
print("Which item's index do you want to know")
user_input = input()
if user_input in supplies:
    print('Index of ' + str(user_input) + ' is ' + str(supplies.index(user_input)))
elif user_input not in supplies:
    print('This item is not in your list')
 