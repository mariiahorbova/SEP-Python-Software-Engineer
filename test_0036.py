# 36. Write a Python program to check if the sequence of numbers 10, 20, 30 appears anywhere in a given array of integers.

def appears_in_array(array):
    return True if ((10 in array) or (20 in array) or (30 in array)) else False


print(appears_in_array([12, 10, 15, 9]))
print(appears_in_array([1, 8, 15, 6]))
print(appears_in_array([20, 13, 15, 50]))
print(appears_in_array([30, 8, 6, 7]))
