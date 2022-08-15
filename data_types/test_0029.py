# 29. Write a Python program to check whether a string 'Java' appears at index 1 in a given sting, 
# if 'Java' appears return the string without 'Java' otherwise return the string unchanged.
# Sample Output:
# Script
# Oldjava

def java_appearance(string):
    if string[1:5] == "Java":
        return string[5:]
    else:
        return string

print(java_appearance("PJavarelated"))
print(java_appearance("Oldjava"))
