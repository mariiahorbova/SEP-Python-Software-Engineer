# 23. Write a Python program to print odd numbers from 10 to 1.
# Sample Output:
# Odd numbers between 9 to 1:
# 9
# 7
# 5
# 3
# 1

def odd():
    for i in range(10, 0, -1):
        if i % 2 != 0:
            print(i)


odd()
