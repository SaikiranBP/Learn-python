"""
This program contains birthday dictionary, which has some key-value pairs
The program asks the user to enter a name, if the name is in birthday daictionary,
then program returns the value associated with the key
if the name is not in birthday dictionary,
then program asks the user to enter the birthday of the user
and the birthday dictionary gets updated.
"""
birthdays = {
    "Saikiran" : "July 8",
    "Savitri" : "Nov 18",
    "Basappa" : "Dec 25",
    "Yallaling" : "Sep 9"
}
while True:
    print("Enter a name: (Blank to quit)")
    user_name = input()
    if user_name in birthdays:
        print(str(birthdays[user_name] + " is the birtday of " + str(user_name)))
    elif user_name == "":
        break
    elif user_name not in birthdays:
        print("I do not have the birthday information for " + str(user_name))
        print("When is the birthday of " + str(user_name))
        user_birthday = input()
        birthdays[user_name] = user_birthday
        print("Birthday database has been updated.")
