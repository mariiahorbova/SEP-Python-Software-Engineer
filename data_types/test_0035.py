# 35. Write a Python program to check two non-negative integer values and return true if they have the same last digit.

def same_last_digit(num1, num2):
    return num1 % 10 == num2 % 10


print(same_last_digit(10, 100))
print(same_last_digit(13, 25))
print(same_last_digit(3, 3))
print(same_last_digit(852, 942))
print(same_last_digit(18, 36))
