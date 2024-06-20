"""
This is a program which has a list and string.
This program provides user 2 options to enter.
1: To join the items into the list,
2: To split the string
This program uses both join and split methods to run the code.
"""
stationary_list = ["pen", "paper", "eraaser", "scale", "sharpner", "ink", "protractor",
                   "divider", "compass", "book", "glue", "scissor", "pad", "colours"]
stationary_string = ("There are many different kinds of animals that live in China."
                    "Tigers and leopards are animals that live in China's forests in the north."
                    "In the jungles, monkeys swing in the trees and elephants walk through the brush")
print("Type:")
print("1: To join the items\n2: To split the items\n3: To exit")
user_input = int(input())
while True:
    if user_input == 1:
        print("By what character do you want to join the items?")
        user_join = input()
        new_list = str(user_join).join(stationary_list)
        print(new_list)
        break
    elif user_input == 2:
        print("By what character do you want to split the string?")
        user_split = input()
        new_string = stationary_string.split(str(user_split))
        print(new_string)
        break
    elif user_input == 3:
        break
