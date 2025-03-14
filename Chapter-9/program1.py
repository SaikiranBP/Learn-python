import shutil
import send2trash
import os
import zipfile

# shutil.copy(source, destination) - copies a single file from source to destination

# shutil.copytree(source, destination) - copies entire folder from source to destination

# shutil.move(source, destination) - moves a file from source to destination

# shutil.rmtree(path) - deletes the folder permanently

# send2trash.send2trash(path) - moves the file/folder to the recycle bin

# os.walk(path) - walks in each and every folder and file of a given path

# exampleZip = zipfile.ZipFile(path) - Creating a zip object to access the contents of zip file

# exampleZip.namelist() - prints out a list of strings of all files and folders contained in it

# exampleZip.extractall() - extracts all the files and folders to cwd