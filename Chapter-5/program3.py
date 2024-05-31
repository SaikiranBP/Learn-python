"""
This program has a dictionary named marks,
Type:
1 : To print the keys
2 : To print the values associated with the keys
3 : To print the items from the dictionary
4 : To quit
"""
marks = {
    "Maths" : 95,
    "Physics" : 89,
    "Chemistry" : 85,
    "English" : 84,
    "Kannada" : 85,
    "Biology" : 90,
}
while True:
    print("Type:")
    print("1 : To print the keys")
    print("2 : To print the values associated with the keys")
    print("3 : To print the items from the dictionary")
    print("4 : To quit")
    user_input = int(input())
    if user_input == 1:
        for k in marks.keys():
            print(k)
    elif user_input == 2:
        for v in marks.values():
            print(v)
    elif user_input == 3:
        for i in marks.items():
            print(i)
    elif user_input == 4:
        break
