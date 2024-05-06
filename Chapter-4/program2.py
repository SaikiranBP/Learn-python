supplies = ['pen', 'book', 'paper', 'eraser', 'scissor', 'scale', 'colours', 'paint']

print('Here is your list ', end='')
print(supplies)
print('Which item do you want delete from the list')

user_input = input()
if user_input in supplies:
    supplies.remove(user_input)
    print(supplies)
elif user_input not in supplies:
    print('This item is not in your list')
