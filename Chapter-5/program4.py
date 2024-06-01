"""

"""
cricketers = {
    "India" : "Virat Kohli",
    "Australia" : "David Warner",
    "South Africa" : "AB Devillers",
    "West Indies" : "Chris Gayle",
    "England" : "Joe Root",
    "New Zealand" : "Kane Williamson",
}
while True:
    print("Type:")
    print("1 : To check the key")
    print("2 : To check the value associated with the key")
    print("3 : To exit")
    user_input = int(input())
    if user_input == 1:
        print("Enter the name of the key")
        user_key = input()
        if user_key in cricketers.keys():
            print("The " + str(user_key) + " is in the dictionary.")
        elif user_key not in cricketers.keys():
            print("The " + str(user_key) + " is not in the dictionary")
    elif user_input == 2:
        print("Enter the name of the value")
        user_value = input()
        if user_value in cricketers.values():
            print("The " + str(user_value) + " is in the dictionary")
    elif user_input == 3:
        break