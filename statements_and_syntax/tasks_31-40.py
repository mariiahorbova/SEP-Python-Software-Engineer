# 31. Write a Python program to iterate an array starting from the last element.
# Sample Output:
# Original array:
# [10, 20, 30, 40, 10, 10, 20]
# Reverse array:
# 20
# 10
# 10
# 40
# 30
# 20
# 10
def reverse_array(arr):
    i = len(arr) - 1
    while i >= 0:
        print(arr[i])
        i -= 1
        
        
print("Reverse array")
reverse_array([10, 20, 30, 40, 10, 10, 20])


# 32. Write a Python program to iterate over the first n elements of a given array.
# Sample Output:
# Original array:
# ["abcde", "abdf", "adeab", "abdgse", "bdefa", "bacdef"]
# First 3 elements:
# ["abcde", "abdf", "adeab"]
def first_n(arr, n):
    return arr[:n]


print("\nFirst n items in array")
print(first_n(["abcde", "abdf", "adeab", "abdgse", "bdefa", "bacdef"], 3))
print(first_n(["abcde", "abdf", "adeab", "abdgse", "bdefa", "bacdef"], 5))


# 33. Write a Python program to sort a given array of strings by length.
# Sample Output:
# Original array:
# ["abcde", "abdf", "adeab", "abdgeee", "bdefa", "abc", "ab", "a", "bacdef"]
# Sorted array of strings by length
# ["a", "ab", "abc", "abdf", "abcde", "adeab", "bdefa", "bacdef", "abdgeee"]
def sort_by_length(arr):
    return sorted(arr, key=len)


print("\nSort by length")
print(sort_by_length(["abcde", "abdf", "adeab",
      "abdgeee", "bdefa", "abc", "ab", "a", "bacdef"]))


# 34. Compress the array, and remove all 0 from it and fill in the elements on the right side of the last 0 with the values ​​- 1
def compress(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] != 0:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1
    arr = arr[:len(arr)- j + 1]
    arr[-1] = 1
    return arr


print("\nCompressing an array")
print(compress([1, 2, 0, 5, 0, 9, 0, 0]))


# 35. Convert the array so that the first go all negative elements, and then positive(0 is considered as positive)
def convert(arr):
    return sorted(arr)


print("\nConverted negative -> 0 -> positive")
print(convert([-7, 13, 0, -4, 8, 6]))


# 36. Write a program which counts the number of times a number appears in an array.
def count(arr):
    num_count = {}
    for i in range(len(arr)):
        if arr[i] not in num_count:
            num_count[arr[i]] = 0
        num_count[arr[i]] += 1
    return num_count


print("\nCount number of times a number enters an array")
print(count([10, 20, 10, 50, 30, 10, 20]))


# 37. In a two-dimensional array of order M and N, swap the specified columns.
def swap(arr, m, n):
    result = [[0]*m for i in range(n)]
    for i in range(m):
        for j in range(n):
            result[j][i] = arr[i][j]
    return result


print("\nSwaped two-dimentional array")
print(swap([[0, 1, 2], [3, 4, 5]], 2, 3))
            

# 38. Given the single-mass array with predefined values with a size of 10 items.  
# Show on the screen array, and find the values that are repeated two and more times.
def repeat(arr):
    print(f"\nOriginal array.\n{arr}")
    repeating = [0] * len(arr)
    print("Repeating two and more times:")
    for i in range(0, len(arr)):
        repeating[arr[i]] += 1
    for i in range(0, len(arr)):
        if (repeating[arr[i]] > 2):
            print(arr[i], end="\n")
            repeating[arr[i]] = 0


repeat([1, 3, 4, 5, 1, 2, 3, 1, 8, 5, 3])


# 39. Given the single-mass array with predefined values with a size of 10 items. 
# Show on the screen array, and find the value that is the smallest odd number.
def smallest_odd(arr):
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] % 2 != 0:
            if arr[i] < min:
                min = arr[i]
    return min


print("\nSmallest odd number: ")
print(smallest_odd([10, 15, 90, 8, 2, 75, 5, 17, 1, 13]))


# 40. Given the single-mass array. Cyclically shift the array on the K elements, on the right or left side.
def shift(arr, k):
    k = k % len(arr)
    for i in range(0, len(arr)):
        if(i < k):
            print(arr[len(arr) + i - k], end=" ")
        else:
            print(arr[i - k], end=" ")


print("\nRotated array to the right on k items:")
shift([1, 2, 3, 4, 5, 6], 2)
