# 12. Write a Python program to create a new string from a given string using the first three characters or whatever is there if the string is less than length 3. Return n copies of the string.
# Sample Output:
# abc
# abcabc
# abc
# abcabc
# abc
# abab

def string_of_three(string, n):
    return string[0:3] * n

print(string_of_three("some text", 4))
print(string_of_three("more", 5))
print(string_of_three("mriia", 7))
print(string_of_three("adding four", 6))
