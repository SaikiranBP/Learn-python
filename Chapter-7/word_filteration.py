"""
This program is all about separating each word and
adding them to dictionaries with their respective keys.
If the given word contains only letters, then the word
will go to the key 'words' and if the given word contains
only numbers, then the word will be pushed to the key 'numbers'
and if the word has both numbers and letters, then it will be
pushed to the key 'others' in the dictionaries
"""

import re
my_dict = {"words" : [], "numbers" : [], "others" : []}

text = "This is Saikiran and I will be joining engineering in 2024."
separated_char = re.split("\s", text)

def fun_regex(item):   
   if re.findall("[A-Za-z]", item):
      my_dict['words'].append(item)
      return ""
   
   elif re.findall("\d", item):
      my_dict['numbers'].append(item)
      return ""

for word in separated_char:
   print(fun_regex(word))

print(my_dict)