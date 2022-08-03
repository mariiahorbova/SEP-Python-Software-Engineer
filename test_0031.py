# 31. Write a Python program to check two integers and 
# return whichever value is nearest to the value 10, 
# or return 0 if two integers are equal.
# Sample Output:
# 7
# 9
# 0

def nearest_10(num1, num2):
    check_num1 = abs(10 - num1)
    check_num2 = abs(10 - num2)
    if check_num1 < check_num2:
        return num1
    elif check_num2 < check_num1:
        return num2
    else:
        return 0

print(nearest_10(2, 9))
print(nearest_10(4, 4))
print(nearest_10(5, 7))
