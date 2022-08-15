# 15. Write a Python program to check two integers and return true if one of them is 20 otherwise return their sum.

def check_20(num1, num2):
    return True if (num1 == 20 or num2 == 20) else num1 + num2

print(check_20(20, 19))
print(check_20(17, 19))
print(check_20(10, 14))
print(check_20(3, 20))
