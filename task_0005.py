# 5. Write a Python program to check if a string starts with "if".
# Sample Output:
# true
# false

def check_starts_on_if():
    s = input("Input a string:")
    s = s.lower()
    if s[0] == 'i' and s[1] == 'f':
        print('true')
    else:
        print('false')

check_starts_on_if()
