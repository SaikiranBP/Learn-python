"""
This program is about opening a txt file and reading the contents of the file,
using open() and read() methods.
"""
print("Type: ")
print("1: To read the content of the file")
print("Press enter to exit")
user_input = int(input())

if user_input == 1:
    file = open("D:\\python_file.txt")
    read_file = file.read()
    print(read_file)

else:
    exit
