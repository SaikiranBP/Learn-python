"""
This program has a dictionary named with stationary_dict.
This program provides the user to add a key-value pair,
to print the dictionary.
This program uses setdefault() Method to set the value for key
if the key is not in the dictionary.
"""
stationary_dict = {
    "Pen" : "Butterflow",
    "Scale" : "Doms",
    "Rubber" : "Apsara",
    "Sharpner" : "Nataraj",
    "Book" : "Classmate"
}
while True:
    print("Type:")
    print("1: To add a key-value pair")
    print("2: To print the dictionary")
    print("3: To exit")
    user_input = int(input())

    if user_input == 1:
        print("Enter the name of the key")
        USER_KEY = str(input())
        if USER_KEY in stationary_dict.keys():
            print("The dictionary has already a key named with " + str(USER_KEY) + ".")
        elif USER_KEY not in stationary_dict.keys():
            print("Enter the name of the value")
            USER_VALUE = str(input())
        NEW_DICT = stationary_dict.setdefault(USER_KEY, USER_VALUE)
    elif user_input == 2:
        print(stationary_dict)
    elif user_input == 3:
        break
    else:
        continue
