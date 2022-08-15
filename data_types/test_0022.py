# 22. Write a Python program to print even numbers from 1 to 10.
# Sample Output:
# Even numbers between 2 to 10:
# 2
# 4
# 6
# 8
# 10

def even():
    for i in range(1, 11):
        if i % 2 == 0:
            print(i)

even()
