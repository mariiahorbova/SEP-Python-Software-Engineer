# 11. Write a Python program to create a new string where "if" is added to the front of a given string. If the string already begins with "if", return the string unchanged.
# Sample Output:
# if else
# if else


def add_if(string):
    # using ternary operator
    return string if (string[0] == 'i' and string[1] == 'f') else 'if ' + string

    # ordinary if-else
    # if string[0] == 'i' and string[1] == 'f':
    #     return string
    # else:
    #     return 'if ' + string

print(add_if("if else"))
print(add_if("else"))
