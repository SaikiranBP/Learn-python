"""
This program is all about splitting of words
This program uses regular expressions to run the code.
"""
import re

text = "This is Saikiran and I will be joining engineering in 2024."
output = re.split("\s", text)
print(output)
