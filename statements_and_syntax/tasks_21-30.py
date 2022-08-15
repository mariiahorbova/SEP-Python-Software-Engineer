# 21. Write a Python program to compute the sum of every third element of a given array of integers.
def every_third(array):
    sum = 0
    for element in array[::3]:
        sum += element
    return sum


print("Sum of every third element")
print(every_third([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# 22. Write a Python program to check whether every element is a 3 or a 5 in a given array of integers.
def check_3_or_5(arr):
    for element in arr:
        if element != 3 and element != 5:
            return False
        else:
            return True


print("\nElements are 3 or 5")
print(check_3_or_5([3, 3, 5, 3]))
print(check_3_or_5([2, 6, 3]))


# 23. Write a Python program to check whether a given value appears everywhere in a given array. 
# A value is "everywhere" in an array if it presents for every pair of adjacent elements in the array.
def check_everywhere(arr, val):
    i = 0
    while i < len(arr):
        if arr[i] != val and arr[i+1] != val:
            return False
        i += 1
    return True


print("\nChecking elements everywhere")
print(check_everywhere([3, 7, 3, 3], 3))
print(check_everywhere([2, 8, 2, 2], 2))
print(check_everywhere([3, 8, 5, 4, 3, 7], 5))


# 24. Write a Python program to check whether a given array contains a 3 next to a 3 or a 5 next to a 5, but not both.
def check_next(arr):
    no3pair = 1
    no5pair = 1
    i = 0
    while i < len(arr) - 1 and (no3pair + no5pair != 0):
        if(arr[i] == 3 and arr[i + 1] == 3):
            no3pair = 0
        elif (arr[i] == 5 and arr[i + 1] == 5):
            no5pair = 0
        i += 1
    return ((no3pair != no5pair) == 1)


print("\n3 next to 3 or 5 next to 5 bot not both")
print(check_next([3, 3, 7, 5]))
print(check_next([3, 3, 5, 5]))
print(check_next([3, 7, 5, 5]))


# 25. Write a Python program to check whether a given array of integers contains two 6's next to each other, 
# or there are two 6's separated by one element, such as [6, 2, 6].
def check_two_sixes(arr):
    for i in range(len(arr)):
        if (arr[i] == 6 and arr[i+1] == 6) or (arr[i] == 6 and arr[i+2] == 6):
            return True
    return False


print("\nCheck two sixes in an array")
print(check_two_sixes([6, 2, 6]))
print(check_two_sixes([1, 6, 2, 2]))
print(check_two_sixes([6, 6]))


# 26. Write a Python program to check whether there is a 2 in the array with a 3 somewhere later in a given array of integers.
def found_three(arr):
    found = False
    i = 0
    while i < len(arr):
        if arr[i] == 2:
            found = True
        if found and arr[i] == 3:
            return True
        i += 1
    return False


print("\nFound three after two in an array")
print(found_three([2, 4, 7, 3]))
print(found_three([2, 4, 7, 9]))
print(found_three([2, 3, 7, 10]))

# 27. Write a Python program to convert an array into a hash.
# Sample Output:
# Original array:
# [(10, 5), (20, 3), (30, 4), (10, 2)]
# Hash:
# {10: (5, 2), 20: (3), 30: (4)}
def array_to_hash(arr):
    d = {}
    for key in arr:
        if key[0] in d:
            if not isinstance(d[key[0]], list):
                d[key[0]] = [d[key[0]]]
            d[key[0]].append(key[1])
        else:
            d[key[0]] = key[1]
    return d


print("\nArray to hash")
print(array_to_hash([(10, 5), (20, 3), (30, 4), (10, 2)]))


# 28. Write a Python program to find the most occurred item in a given array.
# Sample Output:
# Original array:
# [10, 20, 30, 40, 10, 10, 20]
# Frequency of numbers:
# {10: 3, 20: 2, 30: 1, 40: 1}
def most_occured(arr):
    occurence = {}
    for i in range(len(arr)):
        if arr[i] not in occurence:
            occurence[arr[i]] = 0
        occurence[arr[i]] += 1
    return occurence


print("\nFrequency of numbers:")
print(most_occured([10, 20, 30, 40, 10, 10, 20]))


# 29. Write a Python program to check whether all items are identical in a given array.
# Sample Output:
# Original array:
# [10, 20, 30, 40, 10, 10, 20]
# If all items are identical?
# false
# Original array:
# [10, 10, 10]
# If all items are identical?
# true
def identical(arr):
    return True if arr.count(arr[0]) == len(arr) else False


print("\nCheck whether all items are identical in a given array.")
print(identical([10, 20, 30, 40, 10, 10, 20]))
print(identical([10, 10, 10]))


# 30. Write a Python program to search items starting with a specified string of a given array. 
# Sample Output:
# Original array:
# ["abcde", "abdf", "adeab", "abdgse", "bdefa", "bacdef"]
# Search items start with 'ab':
# ["abcde", "abdf", "abdgse"]
# Search items start with 'b':
# ["bdefa", "bacdef"]
def specific_start(arr, start):
    found = []
    for i in arr:
        if i.startswith(start):
            found.append(i)
    return found


print("\nSearch items starting with a specified string")
print(specific_start(["abcde", "abdf", "adeab", "abdgse", "bdefa", "bacdef"], 'ab'))
print(specific_start(["abcde", "abdf", "adeab", "abdgse", "bdefa", "bacdef"], 'b'))
