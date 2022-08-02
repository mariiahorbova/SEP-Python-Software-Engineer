# 8. Write a Python program to check three numbers and return true if one or more of them are small. A number is called "small" if it is in the range 1..10 inclusive.
# Sample Output:
# true
# true
# false

def small_of_three(num1, num2, num3):
    return ((num1 >= 1 and num1 <= 10) or (num2 >= 1 and num2 <= 10) or (num3 >= 1 and num3 <= 10))


print(small_of_three(2, 17, 20))
print(small_of_three(20, 21, 30))
print(small_of_three(9, 17, 20))
print(small_of_three(10, 17, 20))
