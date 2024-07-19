"""
This program has 4 functions named as add(), sub(), multiply(), divide()
All these 4 performs the functions using 2 numbers.
"""

num_1 = 30
num_2 = 20

def add(a, b):
    return a + b

def sub(x, y):
    return x - y

def multiply(c, d):
    return c * d

def divide(u, v):
    return u / v

add_a_b = add(num_1, num_2)
sub_x_y = sub(num_1, num_2)
multiply_c_d = multiply(num_1, num_2)
divide_u_v = divide(num_1, num_2)

print("Addition of num_1 and num_2 is:" + str(add_a_b))
print("Subtraction of num_1 and num_2 is: " + str(sub_x_y))
print("Multiplication of num_1 and num_2 is: " + str(multiply_c_d))
print("Division of num_1 and num_2 is: " + str(divide_u_v))
