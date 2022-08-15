# 6. Write a Python program which accepts the user's first and last name and print them in reverse order with a space between them.
# Sample Output:
# Input your first name:
# Input your last name:
# Hello Lanoie Gary

def reverse_order():
    name = input("Input your first name:")
    surname = input("Input your last name:")
    print("Hello", surname, name)
    
reverse_order()
