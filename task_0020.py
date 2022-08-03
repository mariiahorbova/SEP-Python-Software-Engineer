# 20. Write a Python program to create a new string from a given string with the last character added at the front and back of the given string. The length of the given string must be 1 or more. 
# Sample Output:
# cabcc
# dabcdd
# ajavaa

def add_last(string):
    return string[-1] + string + string[-1]

print(add_last("abc"))
print(add_last("caroline"))
print(add_last("freddy"))
