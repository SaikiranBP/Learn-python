"""
This program has a dictionary named with stationary_list
The program asks the user to enter
the key to check the value of that key
It also handles the KeyError and ValueError 
"""
stationary_list = {
     1 : "pen",
     2 : "paper",
     3 : "scale",
     4 : "ink",
     5 : "books",
     6 : "eraser",
     7 : "sharpner"
}
while True:
    try:
        print("Please enter the key to check the value of the key")
        user_input = int(input())
        print("The value of key " + str(user_input) + " : " + str(stationary_list[user_input]))
        break
    except KeyError:
        print("The key which you have entered is out of range")
    except ValueError:
        continue
