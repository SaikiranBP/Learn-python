"""
This program is all about performing functions.
User have to type in the 3 numbers and
using those three numbers different functions are performed.

"""
try:
    num_1 = (input("Type 1st number: "))
    num_2 = (input("Type 2nd number: "))
    num_3 = (input("Type 3rd number: "))
except ValueError:
    print("Please type the numbers")

def add(a, b, c):
    return a + b + c
def sub(a, b, c):
    return a - b - c
def multiply(a, b, c):
    return a * b * c

add_a_b_c = add(num_1, num_2, num_3)
sub_a_b_c = sub(num_1, num_2, num_3)
multiply_a_b_c = multiply(num_1, num_2, num_3)

print("The addition of three numbers is: " + str(add_a_b_c))
print("The subtraction of three numbers is: " + str(sub_a_b_c))
print("The multiplication of three numbers is: " + str(multiply_a_b_c))