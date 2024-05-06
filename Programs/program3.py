# This program checks whether the number is odd number or even number

print('Please type a number')

try:
    number = int(input())
    if number % 2 == 1:
        print('It is an odd number')
    elif number % 2 == 0:
        print('It is an even number')
except ValueError:
    print('Please type only intergers.')