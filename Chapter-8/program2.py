"""
This program is all about opening a file
and using write() function to perform overwrite or append methods
"""

print("Type in the path of the file")
file_path = input()

if file_path == '':
    exit
else:
    print("Type:")
    print("1: To overwrite the file\n2: To append into the file")
    app_or_write = input()
    
    if app_or_write == '1':
        file = open(str(file_path), 'w')
        print("Type in the text")
        w_text = input()
        file.write(str(w_text))
        file.close()
    elif app_or_write == '2':
        file = open(str(file_path), 'a')
        print("Type in the text")
        a_text = input()
        file.write(str(a_text))
        file.close()
    else:
        exit
