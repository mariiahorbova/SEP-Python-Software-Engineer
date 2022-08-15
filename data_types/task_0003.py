# 3. Write a Python program to create a new string which is n copies of a given string where n is a non-negative integer.

# Sample Output:
# a
# aa
# aaa
# aaaa
# aaaaa

def copies():
    string = input("Enter a string:")
    n = int(input("Enter a non-negative number:"))
    while n < 1:
        n = int(input("Enter a non-negative number:"))
    for i in range(1, n + 1):
        print(string * i)

copies()
