# 18. Write a Python program to compute the sum of the two integers, if the two values are equal return double their sum otherwise return their sum.
# Sample Output:
# 20
# 9

def sum_or_double(num1, num2):
    return (num1 + num2) * 2 if num1 == num2 else num1 + num2

print(sum_or_double(10, 10))
print(sum_or_double(4, 2))
print(sum_or_double(5, 5))
print(sum_or_double(8, 9))
