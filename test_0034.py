# 34. Write a Python program to count the number of 5's in a given array.
# Sample Output:
# 0
# 1
# 2

def array_count_5(array):
    counter = 0
    for item in array:
        if item == 5:
            counter += 1
    return counter

print(array_count_5([1, 3, 5, 7, 5, 10, 5]))
print(array_count_5([1, 3, 4, 8, 9]))
print(array_count_5([1, 3, 5, 7, 5, 10]))
