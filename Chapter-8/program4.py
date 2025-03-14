import re, os
files = os.listdir("D:\\Coding\\Learn-Python")
inp_txt = input("Enter the text you want to find: ")

for file_name in files:

    if re.search(".txt$", file_name):
        file = open(file_name, "r")
        content = file.read()

        if re.search(inp_txt, content):
            print(f"{inp_txt} found in file {file_name}")
        else:
            print(f"{inp_txt} not found in file {file_name}")
            break