"""

"""
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

def num_1():
    input_num_1 = float(input("Type the 1st number: "))
    return input_num_1

def num_2():
    input_num_2 = float(input("Type the 2nd number: "))
    return input_num_2

print("********CALCULATOR********")
print("Type:")
print("1: To add the numbers\n2: To subtract the numbers")
print("3: To multiply the numbers\n4: To divide the numbers")
user_input = input()

if user_input == '1':
    print(add(num_1(), num_2()))
elif user_input == '2':
    print(subtract(num_1(), num_2()))
elif user_input == '3':
    print(multiply(num_1(), num_2()))
elif user_input == '4':
    try:
        print(divide(num_1(), num_2()))
    except ZeroDivisionError:
        print("Undefined term")
else:
    exit
