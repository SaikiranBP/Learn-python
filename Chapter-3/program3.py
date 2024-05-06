print('Please type dividend ')
dividend = int(input())

print('Please type divisor')
divisor = int(input())

try:
    print(dividend / divisor)
except ZeroDivisionError:
    print('Error: Invalid argument')



