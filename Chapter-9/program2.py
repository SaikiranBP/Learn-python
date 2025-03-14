# This program copies all the jpg files to another path using shutil, re and os module

import shutil, re, os

extension = input("Enter the extension you want to copy: ")
for file in os.listdir("E:\FAREWELL"):
    if re.search(extension + "$", file):
       shutil.copy("E:\\FAREWELL\\" + str(file), "E:\\temp_folder")