# 30. Write a Python program to create a string using the first two characters(if present) of a given string 
# if the first character is 'p' and second one is 's' otherwise return a blank string.
# Sample Output:
# ps

def create_using_two(string):
    temp = ''
    if len(string) > 1:
        if string[0] == 'p': temp = temp + string[0]
        if len(string) > 2:
            if string[1] == 's': temp = temp + string[1]
    return temp


print(create_using_two("cd"))
print(create_using_two("psabcd"))
print(create_using_two("abcd"))
