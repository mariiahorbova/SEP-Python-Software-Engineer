# 14. Write a Python program to create a new string from a given string where the first and last characters have been exchanged.
# Sample Output:
# nythoP
# aavJ

def first_last_reverse(string):
    return string[-1] + string[1:-1] + string[0]

print(first_last_reverse("Lenny"))
print(first_last_reverse("Python"))
print(first_last_reverse("Java"))
